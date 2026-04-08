---
type: concept
created: 2026-04-07
updated: 2026-04-07
sources: ["[[scion-docs]]"]
tags: [control-plane, distributed, orchestration]
---

# Hub

In [[scion]], the Hub is the central control plane of the hosted (distributed) architecture. It coordinates state across multiple users, [[grove]]s, and [[runtime-broker]]s.

## Responsibilities

- **Identity & Auth**: Manages user identities via OAuth, issues tokens for brokers and agents
- **State Persistence**: Stores definitive state of agents, groves, and templates in a central database (SQLite)
- **Orchestration**: Dispatches agent lifecycle commands to appropriate [[runtime-broker]]s
- **Collaboration**: Provides shared view via Web Dashboard and Hub API

## Communication with Brokers

- **Direct HTTP**: When broker has a reachable endpoint
- **Control Channel (WebSocket tunnel)**: When broker is behind NAT/firewall

## Agent Creation Flow (Hosted)

1. CLI syncs grove with Hub
2. `POST /api/v1/groves/{groveId}/agents`
3. Hub selects a [[runtime-broker]]
4. Merges environment variables and secrets from all scopes (user → grove → broker)
5. Resolves [[template]] with content hash for broker-side caching
6. Dispatches to broker
7. Broker provisions and starts [[agent]]
8. Status reported back via heartbeats

## See Also
- [[scion]]
- [[runtime-broker]]
- [[grove]]
- [[agent]]
