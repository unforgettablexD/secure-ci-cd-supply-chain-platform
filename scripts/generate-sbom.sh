#!/usr/bin/env bash
set -euo pipefail

IMAGE_NAME="${IMAGE_NAME:-secure-supply-chain-backend}"
IMAGE_TAG="${IMAGE_TAG:-local}"
mkdir -p reports
syft "${IMAGE_NAME}:${IMAGE_TAG}" -o spdx-json > "reports/sbom-${IMAGE_TAG}.spdx.json"
echo "SBOM generated at reports/sbom-${IMAGE_TAG}.spdx.json"
