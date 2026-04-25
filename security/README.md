# Security Controls

This directory contains scanner configuration and policy-as-code rules:

- `bandit.yaml` Python SAST config
- `semgrep/rules.yaml` custom secure-coding rules
- `gitleaks.toml` secret scan config with vulnerable-demo allowlist
- `trivy.yaml` container vulnerability/secret scan config
- `conftest/*.rego` deployment and image policies
- `api_exposure_check.py` custom admin API exposure gate
