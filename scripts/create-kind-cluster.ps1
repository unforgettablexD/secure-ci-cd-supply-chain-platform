kind create cluster --config k8s/kind-config.yaml
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
kubectl apply -f k8s/namespace.yaml
exit $LASTEXITCODE
