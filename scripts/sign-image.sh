#!/usr/bin/env bash
set -euo pipefail

IMAGE_NAME="${IMAGE_NAME:-secure-supply-chain-backend}"
IMAGE_TAG="${IMAGE_TAG:-local}"
FULL_IMAGE="${IMAGE_NAME}:${IMAGE_TAG}"

if [[ "${COSIGN_ENABLE:-false}" != "true" ]]; then
  echo "Cosign signing skipped. Set COSIGN_ENABLE=true to sign."
  exit 0
fi

cosign sign --yes "${FULL_IMAGE}"
