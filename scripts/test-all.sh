#!/usr/bin/env bash
set -euo pipefail

python -m pip install -r app/backend/requirements.txt
PYTHONPATH=app/backend pytest -q app/backend/tests
cd app/frontend
npm ci
npm test
