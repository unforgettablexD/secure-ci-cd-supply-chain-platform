docker run --rm -v ${PWD}:/work -w /work python:3.11 sh -lc "pip install -r app/backend/requirements.txt >/dev/null 2>&1 && PYTHONPATH=app/backend pytest -q app/backend/tests"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Push-Location app/frontend
npm ci
if ($LASTEXITCODE -ne 0) { Pop-Location; exit $LASTEXITCODE }
npm test
$code = $LASTEXITCODE
Pop-Location
exit $code
