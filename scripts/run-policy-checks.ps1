helm template secure-app helm/secure-app -f helm/secure-app/values.yaml -f helm/secure-app/values-staging.yaml > rendered.yaml
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

docker run --rm -v ${PWD}:/work -w /work openpolicyagent/conftest:v0.57.0 test rendered.yaml -p security/conftest
exit $LASTEXITCODE
