#!/usr/bin/env bash
set -euo pipefail

pip-audit -r app/backend/requirements.txt
cd app/frontend
npm ci
npm audit --audit-level=high
