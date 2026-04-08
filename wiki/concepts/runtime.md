---
type: concept
created: 2026-04-07
updated: 2026-04-07
sources: ["[[scion-docs]]"]
tags: [container, infrastructure, execution]
---

# Runtime

In [[scion]], the Runtime is the infrastructure layer responsible for executing [[agent]] containers. Scion abstracts container execution behind a common interface.

## Supported Runtimes

| Runtime | Platform | Notes |
|---------|----------|-------|
| Docker | Linux / macOS / Windows | Default fallback. Supports remote Docker hosts |
| Podman | Linux / macOS | Daemonless, rootless alternative |
| Apple Container | macOS | Native Virtualization Framework, improved performance |
| Kubernetes | Any (via kubeconfig) | Agents as Pods. Namespace isolation, resource specs, workspace sync via tar snapshots |

## Runtime Selection

Resolved by `GetRuntime` factory function:
1. Active profile's `runtime` field in `settings.yaml`
2. OS-level auto-detection (macOS with container CLI → Apple; Linux → Podman if available, else Docker)
3. Explicit CLI flag override

## Interface

The Runtime interface provides: `Run`, `Stop`, `Delete`, `List`, `GetLogs`, `Attach`, `ImageExists`, `PullImage`, `Sync`, `Exec`, `GetWorkspacePath`.

## See Also
- [[scion]]
- [[agent]]
- [[runtime-broker]]
