$image = if ($env:IMAGE_NAME) { $env:IMAGE_NAME } else { "secure-supply-chain-backend" }
$tag = if ($env:IMAGE_TAG) { $env:IMAGE_TAG } else { "local" }
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy:0.63.0 image --severity CRITICAL --ignore-unfixed --skip-version-check --exit-code 1 "$image`:$tag"
exit $LASTEXITCODE
