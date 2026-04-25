#!/usr/bin/env bash
set -euo pipefail

helm template secure-app helm/secure-app -f helm/secure-app/values.yaml -f helm/secure-app/values-staging.yaml > /tmp/secure-app-rendered.yaml
conftest test /tmp/secure-app-rendered.yaml -p security/conftest
