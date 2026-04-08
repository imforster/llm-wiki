---
type: concept
created: 2026-04-07
updated: 2026-04-07
sources: ["[[scion-docs]]"]
tags: [adapter, llm, integration]
---

# Harness

In [[scion]], a Harness is an adapter that allows a specific LLM tool to run within the Scion orchestration layer. It handles provisioning, configuration, and execution for that tool inside an OCI container.

## Purpose

The harness ensures that generic Scion commands (`start`, `stop`, `attach`, `resume`) work consistently regardless of the underlying agent software.

## Interface

Each harness implements (Go):
- `DiscoverAuth()` — Locate credentials on the host
- `GetEnv()` — Map credentials to container environment variables
- `GetCommand()` — Build the correct CLI invocation
- `Provision()` — Harness-specific setup during agent creation
- `PropagateFiles()` — Copy config files into agent home
- `GetVolumes()` — Define volume mounts

## Supported Harnesses

| Harness | Target Tool | Notes |
|---------|-------------|-------|
| `gemini` | [[gemini-cli]] | Default harness. API key / OAuth / Vertex AI auth |
| `claude` | [[claude-code]] | Anthropic API key / Vertex AI auth. See [[claude-code]] for full capabilities. |
| `opencode` | [[opencode]] | Experimental. No hook support |
| `codex` | [[codex]] | Runs `--full-auto` by default |
| `generic` | Any CLI tool | Fallback adapter |

## Capability Matrix

| Capability | Gemini | Claude | OpenCode | Codex |
|---|---|---|---|---|
| Resume | ✅ | ✅ | ✅ | ✅ |
| Resume with Prompt | ✅ | ✅ | ✅ | ❌ |
| Hooks | ✅ | ✅ | ❌ | ❌ |
| OpenTelemetry | ✅ | ✅ | ❌ | ✅ |
| System Prompt Override | ✅ | ✅ | ❌ | ❌ |

## Extensibility

New harnesses can be added via the [[plugin-system]] (hashicorp/go-plugin over gRPC) without modifying the core codebase.

## See Also
- [[scion]]
- [[agent]]
- [[template]]
- [[plugin-system]]
