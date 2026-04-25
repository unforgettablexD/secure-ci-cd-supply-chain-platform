# Architecture

## Application Architecture

- FastAPI backend exposes health, metrics, quote, payment, severity, and admin audit/org routes.
- In-memory stores model orgs, quotes, payments, and audit events.
- RBAC + org checks protect admin and tenant boundaries.

## CI/CD Security Architecture

- GitLab CI and GitHub Actions run equivalent controls:
  - SAST (Bandit, Semgrep)
  - Dependency audit (pip-audit, npm audit)
  - Secret scanning (Gitleaks)
  - Container scanning (Trivy)
  - SBOM generation (Syft)
  - Image signing/verification (Cosign, opt-in)
  - Policy-as-code (Conftest/OPA)
  - Custom API exposure gate

## Deployment Flow

1. Build/test/security gates run first.
2. Build image.
3. Generate SBOM.
4. Optional signing + verification.
5. Conftest policy gate.
6. Deploy staging via Helm only if all gates pass.
7. Deploy production is manual approval.
