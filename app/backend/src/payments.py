from __future__ import annotations

from typing import Any

from .audit import add_audit_event
from .metrics import PAYMENT_FAILURE_TOTAL, PAYMENT_SUCCESS_TOTAL

PAYMENT_STATES = [
    "quote_created",
    "payment_started",
    "payment_processing",
    "payment_success",
    "license_active",
    "license_suspended",
    "license_inactive",
]

PAYMENTS: dict[str, dict[str, Any]] = {}
QUOTES: dict[str, dict[str, Any]] = {}


def create_quote(
    quote_id: str,
    org_id: str,
    amount: int,
    licenses: int,
    quote_type: str,
) -> dict[str, Any]:
    quote = {
        "quote_id": quote_id,
        "org_id": org_id,
        "amount": amount,
        "licenses": licenses,
        "quote_type": quote_type,
        "state": "quote_created",
    }
    QUOTES[quote_id] = quote
    return quote


def start_payment(
    payment_id: str,
    quote_id: str,
    org_id: str,
    purchase_targets: list[str],
) -> dict[str, Any]:
    payment = {
        "payment_id": payment_id,
        "quote_id": quote_id,
        "org_id": org_id,
        "purchase_targets": purchase_targets,
        "state": "payment_started",
    }
    PAYMENTS[payment_id] = payment
    add_audit_event(
        "payment_started",
        actor="system",
        org_id=org_id,
        details={"payment_id": payment_id, "targets": purchase_targets},
    )
    return payment


def process_webhook(payment_id: str, event_type: str, signature: str) -> dict[str, Any]:
    # Real systems should verify provider signatures (Stripe/Supabase webhook secret)
    # and persist immutable payment events in durable storage.
    if signature != "demo-valid-signature":
        PAYMENT_FAILURE_TOTAL.inc()
        raise ValueError("Invalid webhook signature placeholder")
    payment = PAYMENTS[payment_id]
    if event_type == "payment_intent.succeeded":
        payment["state"] = "payment_success"
        PAYMENT_SUCCESS_TOTAL.inc()
        add_audit_event(
            "payment_success",
            actor="webhook",
            org_id=payment["org_id"],
            details=payment,
        )
        payment["state"] = "license_active"
    elif event_type == "payment_intent.failed":
        payment["state"] = "license_suspended"
        PAYMENT_FAILURE_TOTAL.inc()
        add_audit_event(
            "payment_failed",
            actor="webhook",
            org_id=payment["org_id"],
            details=payment,
        )
    return payment


def reset_payments() -> None:
    PAYMENTS.clear()
    QUOTES.clear()
