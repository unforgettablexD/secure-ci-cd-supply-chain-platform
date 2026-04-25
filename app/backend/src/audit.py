from __future__ import annotations

from datetime import UTC, datetime
from typing import Any

from .metrics import SECURITY_AUDIT_EVENTS_TOTAL

AUDIT_EVENTS: list[dict[str, Any]] = []


def add_audit_event(event_type: str, actor: str, org_id: str, details: dict[str, Any]) -> None:
    AUDIT_EVENTS.append(
        {
            "ts": datetime.now(UTC).isoformat(),
            "event_type": event_type,
            "actor": actor,
            "org_id": org_id,
            "details": details,
        }
    )
    SECURITY_AUDIT_EVENTS_TOTAL.inc()


def list_audit_events(org_id: str | None = None) -> list[dict[str, Any]]:
    if org_id is None:
        return AUDIT_EVENTS
    return [event for event in AUDIT_EVENTS if event["org_id"] == org_id]


def reset_audit_events() -> None:
    AUDIT_EVENTS.clear()
