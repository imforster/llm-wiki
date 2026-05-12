---
type: source
created: 2026-05-11
updated: 2026-05-11
origin: llm
tags: [multi-agent, framework, openai, python]
---

# OpenAI Agents SDK

[Original](https://github.com/openai/openai-agents-python) | [Raw](../../raw/llm/openai-agents-sdk.md)

## Summary

The OpenAI Agents SDK is a production-ready Python framework for building multi-agent systems, launched as the successor to the experimental [[openai-swarm]]. With 26.2K GitHub stars, it provides handoffs, guardrails, tracing, and MCP integration on top of OpenAI models.

## Key Takeaways

- **Swarm is now legacy**: The Agents SDK is the official production path. Swarm remains educational only.
- **Two core primitives**: Agents (model + tools + instructions) and Handoffs (functions that return another agent). Same conceptual model as Swarm but with production features.
- **Guardrails**: Built-in input/output validation — a major gap in Swarm.
- **Tracing**: Native OpenTelemetry support for debugging reasoning paths and handoff decisions.
- **MCP support**: Native Model Context Protocol integration for external tools.
- **Sandbox environments** (May 2026): Agents can inspect files, run commands, edit code in isolated containers — positioning for coding agent use cases.
- **OpenAI-model-locked**: No multi-provider support. This is the key limitation vs [[google-adk]] and [[microsoft-agent-framework]].
- **Python-only**: No .NET, Go, Java, or TypeScript SDK (TypeScript planned).

## Architecture

Flat handoff-based coordination (not graph-based):
- Agent wraps model config + tools
- Handoff = function returning another Agent
- SDK handles context switch automatically
- Cheaper models for routing, stronger for reasoning

## Production Control Patterns (April 2026)

1. Guardrails — validate/block risky work
2. Human approvals — pause before sensitive actions
3. Orchestration — specialist ownership vs bounded helper
4. MCP trust boundaries — control external capability access
5. Tracing + trace-based evals — score workflow behavior

## Positioning

| Dimension | OpenAI Agents SDK |
|-----------|-------------------|
| Model support | OpenAI only |
| Languages | Python |
| Orchestration | Flat handoffs |
| State | Session-based |
| Interop | MCP (tools) |
| Production features | Guardrails, tracing, sandboxes |
| Graph workflows | No |

## See Also
- [[openai-swarm]] — predecessor (now legacy)
- [[multi-agent-orchestration]]
- [[google-adk]] — model-agnostic alternative
- [[microsoft-agent-framework]] — enterprise alternative
- [[mcp-protocol]]
