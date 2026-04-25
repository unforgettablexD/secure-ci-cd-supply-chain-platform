# Threat Model

Practical STRIDE-oriented threats:

- Spoofing: forged webhook events.
- Tampering: payment state manipulation, unsigned image substitution.
- Repudiation: missing audit evidence for admin/payment actions.
- Information disclosure: leaked secrets, public admin APIs, cross-org data access.
- Denial of service: vulnerable dependencies/images increasing outage risk.
- Elevation of privilege: privileged Kubernetes workloads, root containers.

Focused risk scenarios:

- Exposed admin APIs
- Leaked secrets in commits
- Vulnerable dependencies
- Vulnerable base/container packages
- Unsigned/tampered images
- Insecure Kubernetes manifests
- Cross-org access control bypass
- Payment webhook validation bypass
