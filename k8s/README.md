# Local kind Cluster

```bash
kind create cluster --config k8s/kind-config.yaml
kubectl apply -f k8s/namespace.yaml
```

Default context expected by CI examples: `kind-secure-supply-chain-lab`.
