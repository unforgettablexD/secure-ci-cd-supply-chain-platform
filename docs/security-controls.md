# Security Controls Mapping

- RBAC and org-based checks -> prevent admin abuse and cross-org access.
- Pytest coverage -> regression prevention for auth/payment/severity behavior.
- Bandit + Semgrep -> code-level flaw detection.
- pip-audit + npm audit -> vulnerable dependency detection.
- Gitleaks -> secret exposure prevention.
- Trivy -> container and package vulnerability detection.
- Syft -> SBOM generation for dependency transparency.
- Cosign -> image integrity and provenance (opt-in gate).
- Conftest -> Kubernetes manifest policy enforcement.
- Custom API exposure check -> ensures admin routes remain protected.
- Audit logs + Prometheus counters -> detection and post-incident traceability.
