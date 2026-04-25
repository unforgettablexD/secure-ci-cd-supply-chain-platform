#!/usr/bin/env bash
set -euo pipefail

bandit -c security/bandit.yaml -r app/backend/src
semgrep --config security/semgrep/rules.yaml app/backend/src
