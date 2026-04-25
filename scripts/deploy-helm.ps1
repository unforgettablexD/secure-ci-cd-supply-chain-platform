param(
  [string]$Environment = "staging",
  [string]$Namespace = "secure-supply-chain-staging"
)

$valuesFile = "helm/secure-app/values-$Environment.yaml"
helm upgrade --install secure-app helm/secure-app `
  --namespace $Namespace --create-namespace `
  -f helm/secure-app/values.yaml -f $valuesFile
exit $LASTEXITCODE
