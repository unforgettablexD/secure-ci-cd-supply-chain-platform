# Pipeline Design

Stages:

1. `validate` verifies required project structure.
2. `lint` enforces style and static correctness.
3. `test` runs backend + frontend tests.
4. `security` runs SAST, dependency, secret, and container scans.
5. `build` builds deployable image.
6. `sbom` generates SPDX SBOM.
7. `sign` performs optional cosign sign/verify.
8. `policy` runs OPA/Conftest and custom API exposure checks.
9. `deploy_staging` deploys Helm chart after all gates pass.
10. `deploy_prod` requires manual approval.

Failure behavior:

- Any gate failure blocks subsequent stages.
- Deploy jobs are gated by prior stage success and kubeconfig variable availability.
