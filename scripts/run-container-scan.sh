#!/usr/bin/env bash
set -euo pipefail

IMAGE_NAME="${IMAGE_NAME:-secure-supply-chain-backend}"
IMAGE_TAG="${IMAGE_TAG:-local}"

trivy image --config security/trivy.yaml --severity CRITICAL --ignore-unfixed --exit-code 1 "${IMAGE_NAME}:${IMAGE_TAG}"
