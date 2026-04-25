def test_admin_routes_require_auth(client):
    response = client.get("/api/admin/orgs")
    assert response.status_code == 401


def test_admin_routes_require_admin_role(client, member_headers):
    response = client.get("/api/admin/orgs", headers=member_headers)
    assert response.status_code == 403


def test_admin_routes_with_admin(client, admin_headers):
    response = client.get("/api/admin/orgs", headers=admin_headers)
    assert response.status_code == 200
