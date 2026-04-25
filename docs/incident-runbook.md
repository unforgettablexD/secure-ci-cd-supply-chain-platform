# Incident Runbook

Scenarios:

- Secret detected in repo:
  - revoke/rotate immediately, remove from history, validate no downstream abuse.
- Critical dependency vulnerability:
  - patch/upgrade, re-run scans, redeploy patched image.
- Critical container vulnerability:
  - update base image and rebuild.
- Unsigned image detected:
  - block deploy, verify provenance chain.
- Failed policy gate:
  - patch Helm manifests; require review before retry.
- Failed deployment after passing gates:
  - rollback Helm release; inspect cluster events.
- Suspected image tampering:
  - quarantine artifact, verify signature/SBOM mismatch.
- Cross-org access bug:
  - disable affected endpoint, hotfix auth check, audit access logs.
- Payment webhook validation failure:
  - reject event, alert on anomaly, inspect signature verification path.
