docker run --rm --entrypoint /bin/sh -v ${PWD}:/work -w /work zricethezav/gitleaks:v8.24.2 -lc "gitleaks detect --source . --config security/gitleaks.toml --redact"
exit $LASTEXITCODE
