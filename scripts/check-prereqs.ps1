$required = @("python", "node", "npm", "docker", "kind", "helm", "kubectl")
$optional = @("bandit", "semgrep", "pip-audit", "gitleaks", "trivy", "syft", "cosign", "conftest")

foreach ($cmd in $required) {
  if (-not (Get-Command $cmd -ErrorAction SilentlyContinue)) {
    Write-Error "Missing required command: $cmd"
    exit 1
  }
}

foreach ($cmd in $optional) {
  if (Get-Command $cmd -ErrorAction SilentlyContinue) {
    Write-Host "Found optional command: $cmd"
  } else {
    Write-Host "Optional command not found: $cmd"
  }
}

Write-Host "Prerequisite check complete."
