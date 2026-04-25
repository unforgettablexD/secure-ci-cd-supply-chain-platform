def test_org_based_access_isolation(client):
    member_org1 = {"Authorization": "Bearer user-01|member|org-001"}
    response = client.post(
        "/api/quotes",
        headers=member_org1,
        json={"org_id": "org-002", "licenses": 2, "quote_type": "one_time", "unit_price": 20},
    )
    assert response.status_code == 403


def test_api_exposure_protection_admin_audit(client, admin_headers):
    response = client.get("/api/admin/audit-events", headers=admin_headers)
    assert response.status_code == 200
