from __future__ import annotations

import time
import uuid
from typing import Any

from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import PlainTextResponse
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest
from pydantic import BaseModel, Field

from .audit import list_audit_events
from .auth import ORGS, Principal, enforce_org_access, get_current_principal, require_admin
from .logging_config import configure_logging
from .metrics import QUOTE_GENERATED_TOTAL, REQUEST_COUNT, REQUEST_LATENCY_SECONDS
from .payments import PAYMENTS, QUOTES, create_quote, process_webhook, start_payment
from .severity import evaluate_severity

configure_logging()
app = FastAPI(title="secure-ci-cd-supply-chain-platform", version="0.1.0")


@app.middleware("http")
async def request_metrics_middleware(request: Request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    latency = time.perf_counter() - start
    REQUEST_COUNT.labels(request.method, request.url.path, response.status_code).inc()
    REQUEST_LATENCY_SECONDS.labels(request.method, request.url.path).observe(latency)
    return response


class QuoteRequest(BaseModel):
    org_id: str
    licenses: int = Field(ge=1, le=5000)
    quote_type: str = Field(pattern="^(one_time|subscription)$")
    unit_price: int = Field(ge=1, le=100000)


class PaymentStartRequest(BaseModel):
    org_id: str
    quote_id: str
    purchase_targets: list[str] = Field(default_factory=list)


class WebhookRequest(BaseModel):
    payment_id: str
    event_type: str
    signature: str


class SeverityRequest(BaseModel):
    org_id: str
    summary: str
    modifiers: list[str] = Field(default_factory=list)


class OrgRequest(BaseModel):
    org_id: str
    name: str


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "secure-supply-chain-backend"}


@app.get("/metrics")
def metrics() -> PlainTextResponse:
    return PlainTextResponse(generate_latest(), media_type=CONTENT_TYPE_LATEST)


@app.post("/api/quotes")
def quotes(
    payload: QuoteRequest,
    principal: Principal = Depends(get_current_principal),
) -> dict[str, Any]:
    enforce_org_access(principal, payload.org_id)
    quote_id = f"qt-{uuid.uuid4().hex[:10]}"
    quote = create_quote(
        quote_id=quote_id,
        org_id=payload.org_id,
        amount=payload.licenses * payload.unit_price,
        licenses=payload.licenses,
        quote_type=payload.quote_type,
    )
    QUOTE_GENERATED_TOTAL.inc()
    return quote


@app.post("/api/payments/start")
def payments_start(
    payload: PaymentStartRequest, principal: Principal = Depends(get_current_principal)
) -> dict[str, Any]:
    enforce_org_access(principal, payload.org_id)
    if payload.quote_id not in QUOTES:
        raise HTTPException(status_code=404, detail="Quote not found")
    payment_id = f"pay-{uuid.uuid4().hex[:10]}"
    return start_payment(
        payment_id=payment_id,
        quote_id=payload.quote_id,
        org_id=payload.org_id,
        purchase_targets=payload.purchase_targets or [payload.org_id],
    )


@app.post("/api/payments/webhook")
def payments_webhook(payload: WebhookRequest) -> dict[str, Any]:
    if payload.payment_id not in PAYMENTS:
        raise HTTPException(status_code=404, detail="Payment not found")
    try:
        return process_webhook(payload.payment_id, payload.event_type, payload.signature)
    except ValueError as exc:
        raise HTTPException(status_code=401, detail=str(exc)) from exc


@app.post("/api/severity/evaluate")
def severity_route(
    payload: SeverityRequest, principal: Principal = Depends(get_current_principal)
) -> dict[str, str | int]:
    enforce_org_access(principal, payload.org_id)
    return evaluate_severity(
        org_id=payload.org_id,
        actor=principal.user_id,
        summary=payload.summary,
        modifiers=payload.modifiers,
    )


@app.get("/api/admin/audit-events")
def admin_audit_events(admin: Principal = Depends(require_admin)) -> list[dict[str, Any]]:
    return list_audit_events(org_id=admin.org_id)


@app.get("/api/admin/orgs")
def admin_orgs(admin: Principal = Depends(require_admin)) -> dict[str, dict[str, str]]:
    _ = admin
    return ORGS


@app.post("/api/admin/orgs")
def admin_create_org(
    payload: OrgRequest,
    admin: Principal = Depends(require_admin),
) -> dict[str, Any]:
    _ = admin
    ORGS[payload.org_id] = {"name": payload.name}
    return {"created": payload.org_id}
