Remove-Item -Recurse -Force .pytest_cache,.ruff_cache,app/backend/.pytest_cache,app/backend/.ruff_cache -ErrorAction SilentlyContinue
Remove-Item -Force reports/*.json -ErrorAction SilentlyContinue
