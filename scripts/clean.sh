#!/usr/bin/env bash
set -euo pipefail

rm -rf .pytest_cache .ruff_cache app/backend/.pytest_cache app/backend/.ruff_cache reports/*.json || true
