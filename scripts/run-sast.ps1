docker run --rm -v ${PWD}:/work -w /work python:3.11 sh -lc "pip install -r app/backend/requirements.txt >/dev/null 2>&1 && bandit -c security/bandit.yaml -r app/backend/src"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

docker run --rm -v ${PWD}:/src semgrep/semgrep:1.86.0 semgrep --config /src/security/semgrep/rules.yaml /src/app/backend/src
exit $LASTEXITCODE
