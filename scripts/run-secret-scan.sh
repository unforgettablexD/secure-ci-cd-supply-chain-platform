#!/usr/bin/env bash
set -euo pipefail

gitleaks detect --source . --config security/gitleaks.toml --redact
