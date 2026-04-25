SHELL := /bin/bash

.PHONY: prereqs install test lint sast dep-scan secret-scan docker-build container-scan sbom sign-image verify-image policy security-all kind-create helm-deploy-staging helm-deploy-prod clean

prereqs:
	bash scripts/check-prereqs.sh

install:
	python -m pip install -r app/backend/requirements.txt
	cd app/frontend && npm ci

test:
	bash scripts/test-all.sh

lint:
	ruff check app/backend/src app/backend/tests

sast:
	bash scripts/run-sast.sh

dep-scan:
	bash scripts/run-dependency-scan.sh

secret-scan:
	bash scripts/run-secret-scan.sh

docker-build:
	docker build -t $${IMAGE_NAME:-secure-supply-chain-backend}:$${IMAGE_TAG:-local} app/backend

container-scan:
	bash scripts/run-container-scan.sh

sbom:
	bash scripts/generate-sbom.sh

sign-image:
	bash scripts/sign-image.sh

verify-image:
	bash scripts/verify-image.sh

policy:
	bash scripts/run-policy-checks.sh

security-all: sast dep-scan secret-scan container-scan policy

kind-create:
	bash scripts/create-kind-cluster.sh

helm-deploy-staging:
	bash scripts/deploy-helm.sh staging secure-supply-chain-staging

helm-deploy-prod:
	bash scripts/deploy-helm.sh prod prod

clean:
	bash scripts/clean.sh
