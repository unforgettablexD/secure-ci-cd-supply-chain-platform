$image = if ($env:IMAGE_NAME) { $env:IMAGE_NAME } else { "secure-supply-chain-backend" }
$tag = if ($env:IMAGE_TAG) { $env:IMAGE_TAG } else { "local" }

if ($env:COSIGN_ENABLE -ne "true") {
  Write-Host "Cosign signing skipped. Set COSIGN_ENABLE=true to sign."
  exit 0
}

cosign sign --yes "$image`:$tag"
exit $LASTEXITCODE
