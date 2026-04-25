# Local GitLab Integration

1. Create project in local GitLab (`http://localhost:8080`) named `secure-ci-cd-supply-chain-platform`.
2. Push repo:

```bash
git remote add gitlab http://localhost:8080/root/secure-ci-cd-supply-chain-platform.git
git push -u gitlab main
```

3. Ensure local Docker runner is online and allowed to run untagged jobs.
4. Configure GitLab CI/CD variables:
   - `KUBECONFIG_B64` (base64 kubeconfig for kind)
   - optional registry vars (`CI_REGISTRY`, `CI_REGISTRY_USER`, `CI_REGISTRY_PASSWORD`)
   - optional `COSIGN_ENABLE=true` if signing should be enforced
5. Run pipeline and inspect stage-by-stage security gates.
6. Deploy staging via `deploy_staging_helm`.

Troubleshooting:

- If checkout/upload fails with hostname issues on Docker Desktop, use runner `url` and `clone_url` as `http://host.docker.internal:8929`.
- If Helm TLS cert mismatch occurs, use `--kube-tls-server-name localhost`.
