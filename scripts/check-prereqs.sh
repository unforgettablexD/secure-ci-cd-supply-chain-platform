#!/usr/bin/env bash
set -euo pipefail

required=(python node npm docker kind helm kubectl)
optional=(bandit semgrep pip-audit gitleaks trivy syft cosign conftest)

for cmd in "${required[@]}"; do
  command -v "$cmd" >/dev/null 2>&1 || { echo "Missing required command: $cmd"; exit 1; }
done

for cmd in "${optional[@]}"; do
  if command -v "$cmd" >/dev/null 2>&1; then
    echo "Found optional command: $cmd"
  else
    echo "Optional command not found: $cmd"
  fi
done

echo "Prerequisite check complete."
