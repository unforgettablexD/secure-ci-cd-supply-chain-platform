from __future__ import annotations

from .audit import add_audit_event
from .metrics import SEVERITY_EVALUATION_TOTAL, SEVERITY_HIGH_TOTAL

KEYWORD_WEIGHTS = {
    "outage": 30,
    "breach": 40,
    "ransomware": 50,
    "latency": 15,
    "p1": 25,
    "payment": 15,
}


def evaluate_severity(
    org_id: str,
    actor: str,
    summary: str,
    modifiers: list[str],
) -> dict[str, str | int]:
    score = 10
    lower_summary = summary.lower()
    for keyword, weight in KEYWORD_WEIGHTS.items():
        if keyword in lower_summary:
            score += weight
    for modifier in modifiers:
        if modifier == "external_customer_impact":
            score += 20
        if modifier == "security_control_failure":
            score += 25
    if score >= 90:
        level = "critical"
    elif score >= 70:
        level = "high"
    elif score >= 40:
        level = "medium"
    else:
        level = "low"
    SEVERITY_EVALUATION_TOTAL.inc()
    if level in {"high", "critical"}:
        SEVERITY_HIGH_TOTAL.inc()
    add_audit_event(
        "severity_evaluated",
        actor=actor,
        org_id=org_id,
        details={"summary": summary, "score": score, "level": level},
    )
    return {"score": score, "severity": level}
