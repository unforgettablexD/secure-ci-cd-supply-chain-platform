# Remediation Guide

- Bandit fail: fix insecure APIs, subprocess calls, or crypto misuse.
- Semgrep fail: remove unsafe patterns and add secure alternatives.
- pip-audit fail: upgrade vulnerable Python dependencies.
- npm audit fail: update/replace vulnerable Node packages.
- Gitleaks fail: rotate credential, remove secret, rewrite history if needed.
- Trivy fail: update base image/dependencies; rebuild image.
- Conftest fail: update Helm manifests to satisfy policy.
- Cosign verify fail: reject deploy, rebuild and re-sign image.
- API exposure check fail: enforce `Depends(require_admin)` on admin routes.
