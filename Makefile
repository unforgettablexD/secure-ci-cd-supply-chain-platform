.PHONY: prereqs install test lint sast dep-scan secret-scan docker-build container-scan sbom sign-image verify-image policy security-all kind-create helm-deploy-staging helm-deploy-prod clean

prereqs:
	powershell -ExecutionPolicy Bypass -File scripts/check-prereqs.ps1

install:
	python -m pip install -r app/backend/requirements.txt
	cd app/frontend && npm ci

test:
	powershell -ExecutionPolicy Bypass -File scripts/test-all.ps1

lint:
	ruff check app/backend/src app/backend/tests

sast:
	powershell -ExecutionPolicy Bypass -File scripts/run-sast.ps1

dep-scan:
	powershell -ExecutionPolicy Bypass -File scripts/run-dependency-scan.ps1

secret-scan:
	powershell -ExecutionPolicy Bypass -File scripts/run-secret-scan.ps1

docker-build:
	docker build -t $${IMAGE_NAME:-secure-supply-chain-backend}:$${IMAGE_TAG:-local} app/backend

container-scan:
	powershell -ExecutionPolicy Bypass -File scripts/run-container-scan.ps1

sbom:
	powershell -ExecutionPolicy Bypass -File scripts/generate-sbom.ps1

sign-image:
	powershell -ExecutionPolicy Bypass -File scripts/sign-image.ps1

verify-image:
	powershell -ExecutionPolicy Bypass -File scripts/verify-image.ps1

policy:
	powershell -ExecutionPolicy Bypass -File scripts/run-policy-checks.ps1

security-all: sast dep-scan secret-scan container-scan policy

kind-create:
	powershell -ExecutionPolicy Bypass -File scripts/create-kind-cluster.ps1

helm-deploy-staging:
	powershell -ExecutionPolicy Bypass -File scripts/deploy-helm.ps1 -Environment staging -Namespace secure-supply-chain-staging

helm-deploy-prod:
	powershell -ExecutionPolicy Bypass -File scripts/deploy-helm.ps1 -Environment prod -Namespace prod

clean:
	powershell -ExecutionPolicy Bypass -File scripts/clean.ps1
