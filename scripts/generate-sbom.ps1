$image = if ($env:IMAGE_NAME) { $env:IMAGE_NAME } else { "secure-supply-chain-backend" }
$tag = if ($env:IMAGE_TAG) { $env:IMAGE_TAG } else { "local" }
New-Item -ItemType Directory -Force -Path reports | Out-Null
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock anchore/syft:latest "$image`:$tag" -o spdx-json > "reports/sbom-$tag.spdx.json"
exit $LASTEXITCODE
