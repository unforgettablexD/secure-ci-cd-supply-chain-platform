#!/usr/bin/env bash
set -euo pipefail

ENVIRONMENT="${1:-staging}"
NAMESPACE="${2:-secure-supply-chain-staging}"
VALUES_FILE="helm/secure-app/values-${ENVIRONMENT}.yaml"

helm upgrade --install secure-app helm/secure-app \
  --namespace "${NAMESPACE}" --create-namespace \
  -f helm/secure-app/values.yaml -f "${VALUES_FILE}"
