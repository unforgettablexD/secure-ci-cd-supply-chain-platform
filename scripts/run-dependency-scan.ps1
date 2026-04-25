docker run --rm -v ${PWD}:/work -w /work python:3.11 sh -lc "pip install pip-audit >/dev/null 2>&1 && pip-audit -r app/backend/requirements.txt"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Push-Location app/frontend
npm ci
if ($LASTEXITCODE -ne 0) { Pop-Location; exit $LASTEXITCODE }
npm audit --audit-level=high
$code = $LASTEXITCODE
Pop-Location
exit $code
