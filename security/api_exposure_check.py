from __future__ import annotations

import re
from pathlib import Path


def main() -> int:
    target = Path("app/backend/src/main.py")
    source = target.read_text(encoding="utf-8")
    failures: list[str] = []
    checks = {
        "admin_audit_events": r"def admin_audit_events\((.*?)\)\s*->",
        "admin_orgs": r"def admin_orgs\((.*?)\)\s*->",
        "admin_create_org": r"def admin_create_org\((.*?)\)\s*->",
    }
    for name, pattern in checks.items():
        match = re.search(pattern, source, re.DOTALL)
        if not match:
            failures.append(f"{name} function missing")
            continue
        signature = match.group(1)
        if "Depends(require_admin)" not in signature:
            failures.append(f"{name} missing Depends(require_admin)")
    if failures:
        for fail in failures:
            print(f"[FAIL] {fail}")
        return 1
    print("API exposure check passed: admin endpoints require auth dependency.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
