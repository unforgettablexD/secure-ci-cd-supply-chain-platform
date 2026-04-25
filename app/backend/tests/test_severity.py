def test_severity_classification(client, member_headers):
    response = client.post(
        "/api/severity/evaluate",
        headers=member_headers,
        json={
            "org_id": "org-001",
            "summary": "customer payment latency issue",
            "modifiers": [],
        },
    )
    assert response.status_code == 200
    assert response.json()["severity"] in {"medium", "high"}


def test_audit_event_creation(client, member_headers, admin_headers):
    response = client.post(
        "/api/severity/evaluate",
        headers=member_headers,
        json={
            "org_id": "org-001",
            "summary": "possible breach with ransomware indicators and p1 outage",
            "modifiers": ["external_customer_impact", "security_control_failure"],
        },
    )
    assert response.status_code == 200
    assert response.json()["severity"] == "critical"
    audit = client.get("/api/admin/audit-events", headers=admin_headers)
    assert audit.status_code == 200
    assert any(event["event_type"] == "severity_evaluated" for event in audit.json())
