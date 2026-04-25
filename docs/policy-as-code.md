# Policy-as-Code

Conftest policies enforce:

- containers run as non-root
- no privilege escalation
- requests/limits required
- probes required
- image tag not `latest`
- basic secret hardcoding checks in manifests
- production namespace constraint

Run locally:

```bash
make policy
```
