def _create_quote(client, headers):
    quote = client.post(
        "/api/quotes",
        headers=headers,
        json={"org_id": "org-001", "licenses": 5, "quote_type": "subscription", "unit_price": 30},
    )
    assert quote.status_code == 200
    return quote.json()["quote_id"]


def test_quote_generation(client, member_headers):
    quote_id = _create_quote(client, member_headers)
    assert quote_id.startswith("qt-")


def test_payment_started(client, member_headers):
    quote_id = _create_quote(client, member_headers)
    payment = client.post(
        "/api/payments/start",
        headers=member_headers,
        json={"org_id": "org-001", "quote_id": quote_id, "purchase_targets": ["org-001"]},
    )
    assert payment.status_code == 200
    assert payment.json()["state"] == "payment_started"


def test_payment_success_and_license_activation(client, member_headers):
    quote_id = _create_quote(client, member_headers)
    payment = client.post(
        "/api/payments/start",
        headers=member_headers,
        json={"org_id": "org-001", "quote_id": quote_id},
    ).json()
    response = client.post(
        "/api/payments/webhook",
        json={
            "payment_id": payment["payment_id"],
            "event_type": "payment_intent.succeeded",
            "signature": "demo-valid-signature",
        },
    )
    assert response.status_code == 200
    assert response.json()["state"] == "license_active"


def test_webhook_signature_placeholder_validation(client, member_headers):
    quote_id = _create_quote(client, member_headers)
    payment = client.post(
        "/api/payments/start",
        headers=member_headers,
        json={"org_id": "org-001", "quote_id": quote_id},
    ).json()
    response = client.post(
        "/api/payments/webhook",
        json={
            "payment_id": payment["payment_id"],
            "event_type": "payment_intent.succeeded",
            "signature": "bad",
        },
    )
    assert response.status_code == 401
