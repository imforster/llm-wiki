---
type: concept
created: 2026-04-07
updated: 2026-04-07
sources: ["[[scion-docs]]"]
tags: [distributed, compute, broker]
---

# Runtime Broker

In [[scion]], a Runtime Broker is a compute node that registers with a [[hub]] to provide execution capacity for [[agent]]s.

## Responsibilities

- Manages local lifecycle of agents dispatched from the Hub
- Handles workspace synchronization
- Template hydration (with content hash caching)
- Log streaming
- Reports status back via heartbeats and agent status updates

## Communication

Connects to the Hub via:
- **Direct HTTP** — when broker has a reachable endpoint
- **WebSocket Control Channel** — when behind NAT/firewall

## Examples of Broker Nodes

A server, laptop, or Kubernetes cluster — any machine that can run containers.

## See Also
- [[hub]]
- [[scion]]
- [[agent]]
- [[runtime]]
