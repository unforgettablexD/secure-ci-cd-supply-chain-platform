from __future__ import annotations

from dataclasses import dataclass

from fastapi import Depends, Header, HTTPException, status


@dataclass
class Principal:
    user_id: str
    role: str
    org_id: str


ORGS: dict[str, dict[str, str]] = {
    "org-001": {"name": "Acme Bank"},
    "org-002": {"name": "Zephyr Retail"},
}


def _parse_auth_header(authorization: str | None) -> Principal:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing bearer token")
    token = authorization.removeprefix("Bearer ").strip()
    try:
        user_id, role, org_id = token.split("|")
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token format",
        ) from exc
    if org_id not in ORGS:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Unknown org")
    return Principal(user_id=user_id, role=role, org_id=org_id)


def get_current_principal(authorization: str | None = Header(default=None)) -> Principal:
    return _parse_auth_header(authorization)


def require_admin(principal: Principal = Depends(get_current_principal)) -> Principal:
    if principal.role != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin role required")
    return principal


def enforce_org_access(principal: Principal, target_org_id: str) -> None:
    if principal.role != "admin" and principal.org_id != target_org_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Cross-org access denied")


def reset_orgs() -> None:
    ORGS.clear()
    ORGS.update(
        {
            "org-001": {"name": "Acme Bank"},
            "org-002": {"name": "Zephyr Retail"},
        }
    )
