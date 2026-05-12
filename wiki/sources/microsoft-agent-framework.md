---
type: source
created: 2026-05-11
updated: 2026-05-11
origin: llm
tags: [multi-agent, framework, microsoft, enterprise, graph-workflows]
---

# Microsoft Agent Framework 1.0

[Original](https://github.com/microsoft/agent-framework) | [Raw](../../raw/llm/microsoft-agent-framework.md)

## Summary

Microsoft Agent Framework 1.0 GA shipped April 3, 2026 — the production-ready convergence of [[autogen-multi-agent|AutoGen]] (56.8K stars) and Semantic Kernel (18K+ stars) into a single unified SDK. Supports .NET and Python, six model providers, native MCP + A2A, graph-based workflows, and ships with an LTS commitment.

## Key Takeaways

- **The merger**: Semantic Kernel becomes the foundation layer (kernel, plugins, connectors). AutoGen's orchestration becomes the graph workflow engine on top. One SDK, one mental model.
- **75K+ stars unified**: Combined community of both predecessor projects.
- **Six providers, one-line swap**: Azure OpenAI, OpenAI, Anthropic Claude, Amazon Bedrock, Google Gemini, Ollama. Truly model-agnostic.
- **Native MCP + A2A**: Full interoperability story at 1.0. Not bolt-on.
- **LTS from day one**: Stable API surface, documented upgrade path. Rare in this space.
- **Graph workflows**: Four canonical patterns — round-robin, supervisor, hierarchical, dynamic hand-off.
- **DevUI**: Browser-based local debugger showing message graphs, tool invocations, token latency, orchestration decisions. Unique differentiator.
- **AutoGen is now legacy**: Maintenance mode. Plan migrations during 2026.
- **.NET + Python first-class**: Same concepts, same API shape, idiomatic in each language.

## Architecture (Five Layers)

1. **Connectors** — provider adapters (six providers)
2. **Kernel** — DI container, config (from Semantic Kernel)
3. **Agents** — instructions, tools, memory, state
4. **Orchestration** — graph workflow engine (from AutoGen concepts)
5. **Interop** — MCP + A2A protocol adapters

## Orchestration Patterns

| Pattern | Use When |
|---------|----------|
| Round-robin | Deterministic pipeline, clear turns |
| Supervisor | One coordinator routes to specialists |
| Hierarchical | Tree topology, managers own sub-teams |
| Dynamic hand-off | Runtime peer transfer decisions |

## Positioning

| Dimension | Microsoft Agent Framework 1.0 |
|-----------|-------------------------------|
| Model support | 6 providers (Azure OpenAI, OpenAI, Claude, Bedrock, Gemini, Ollama) |
| Languages | .NET 9+ (C# 13), Python 3.10+ |
| Orchestration | Graph workflows (typed edges) |
| State | Agent-level state + session |
| Interop | MCP (tools) + A2A (agents) |
| Production features | DevUI, OpenTelemetry, Azure deployment, LTS |
| Graph workflows | Yes (core architecture) |

## Legacy Migration

- **Semantic Kernel** → continues maintenance, lazy migration OK
- **AutoGen** → maintenance mode, plan migration during 2026
- Published migration guides for both at learn.microsoft.com

## See Also
- [[autogen-multi-agent]] — predecessor (now legacy)
- [[multi-agent-orchestration]]
- [[google-adk]] — similar scope, Google ecosystem
- [[langgraph-agent-orchestration]] — graph-first OSS alternative
- [[openai-agents-sdk]] — simpler, OpenAI-locked
- [[mcp-protocol]]
