# Cosign Signing and Verification

Default behavior is safe for public repos: signing is skipped unless explicitly enabled.

```bash
COSIGN_ENABLE=true IMAGE_NAME=secure-supply-chain-backend IMAGE_TAG=local bash scripts/sign-image.sh
COSIGN_ENABLE=true IMAGE_NAME=secure-supply-chain-backend IMAGE_TAG=local bash scripts/verify-image.sh
```

Use keyless signing (OIDC) for GitHub/GitLab where available, or configure a key pair in secure CI variables.
