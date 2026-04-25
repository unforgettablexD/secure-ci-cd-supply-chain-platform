# Kubernetes Helm Deployment

Create cluster:

```bash
bash scripts/create-kind-cluster.sh
```

Deploy staging:

```bash
bash scripts/deploy-helm.sh staging secure-supply-chain-staging
```

Deploy production:

```bash
bash scripts/deploy-helm.sh prod prod
```

Security hardening in chart:

- non-root user
- readOnlyRootFilesystem
- allowPrivilegeEscalation false
- dropped Linux capabilities
- liveness/readiness probes
- resource requests/limits
