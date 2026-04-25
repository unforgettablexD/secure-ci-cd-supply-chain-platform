# GitHub Actions

Workflow: `.github/workflows/secure-supply-chain.yml`

It validates lint, tests, SAST, dependency scan, secret scan, image scan, SBOM, policy checks, and custom API exposure checks.

To publish image to GHCR:

1. Enable workflow permissions for package write.
2. Add login step + `docker push` in the workflow.
3. Use `ghcr.io/<org>/<repo>/secure-supply-chain-backend:<sha>` image refs.

Signing is intentionally a placeholder by default to keep public forks runnable without secrets.
