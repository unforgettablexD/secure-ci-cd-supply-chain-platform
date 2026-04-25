package main

deny[msg] {
  input.kind == "Deployment"
  container := input.spec.template.spec.containers[_]
  contains(container.image, ":latest")
  msg := "image tag must not be latest"
}

deny[msg] {
  input.kind == "Secret"
  input.type == "Opaque"
  key := object.keys(input.stringData)[_]
  val := input.stringData[key]
  contains(lower(val), "password")
  msg := "hardcoded password-like value detected in secret manifest"
}

deny[msg] {
  input.kind == "Namespace"
  ns := input.metadata.name
  startswith(ns, "prod")
  ns != "prod"
  msg := "production deployment must use approved namespace 'prod'"
}
