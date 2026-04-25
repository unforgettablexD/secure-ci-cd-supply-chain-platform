# SBOM and Image Signing

SBOM:

```bash
make docker-build
make sbom
```

Image signing and verification:

```bash
COSIGN_ENABLE=true make sign-image
COSIGN_ENABLE=true make verify-image
```

In CI, signing/verification can be enforced by setting `COSIGN_ENABLE=true`.
