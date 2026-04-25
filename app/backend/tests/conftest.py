from __future__ import annotations

import pytest
from fastapi.testclient import TestClient

from src.audit import reset_audit_events
from src.auth import reset_orgs
from src.main import app
from src.payments import reset_payments


@pytest.fixture(autouse=True)
def reset_state() -> None:
    reset_orgs()
    reset_payments()
    reset_audit_events()


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


@pytest.fixture
def member_headers() -> dict[str, str]:
    return {"Authorization": "Bearer user-01|member|org-001"}


@pytest.fixture
def admin_headers() -> dict[str, str]:
    return {"Authorization": "Bearer admin-01|admin|org-001"}
