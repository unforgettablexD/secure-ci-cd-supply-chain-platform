#!/usr/bin/env bash
set -euo pipefail

kind create cluster --config k8s/kind-config.yaml
kubectl apply -f k8s/namespace.yaml
