---
type: concept
created: 2026-04-07
updated: 2026-04-07
sources: ["[[scion-docs]]"]
tags: [extensibility, grpc, architecture]
---

# Plugin System

[[scion]] supports a plugin architecture built on `hashicorp/go-plugin` for extending system capabilities. Plugins communicate over gRPC.

## Plugin Types

- **Message Broker Plugins**: Custom message delivery backends for agent notifications and structured messaging
- **Agent Harness Plugins**: Custom [[harness]] implementations that integrate new LLM tools without modifying the core codebase

## Status

Currently in foundational stage, with reference implementations available for both plugin types.

## See Also
- [[scion]]
- [[harness]]
