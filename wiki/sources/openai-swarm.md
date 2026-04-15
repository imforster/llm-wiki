---
type: source
created: 2026-04-14
updated: 2026-04-14
origin: llm
tags: [multi-agent, orchestration, lightweight, handoffs, educational]
---

# OpenAI Swarm: Lightweight Multi-Agent Orchestration

[Original](https://kindatechnical.com/agentic-ai/openai-swarm-and-handoff-patterns.html) | [Raw](../../raw/llm/openai-swarm.md)

OpenAI's experimental/educational framework (October 2024). Radically minimal: agents are system prompts with functions, handoffs are functions that return another agent. Explicitly NOT for production — demonstrates patterns implementable with any LLM SDK.

## Two Primitives

1. **Routines** — system prompt + callable functions
2. **Handoffs** — functions that return another Agent, transferring control

That's the entire framework on top of Chat Completions API.

## Context Variables

Shared state between agents without putting it in conversation history. Keeps sensitive data out of messages. Passed at runtime.

## Design Philosophy

Shows multi-agent orchestration doesn't require complex infrastructure. The handoff pattern itself IS production-ready even though Swarm isn't. Echoes [[pai]]'s CODE → CLI → PROMPT → SKILL hierarchy: use the simplest tool that works.

## Limitations

No state persistence, no memory beyond context variables, no checkpointing, no human-in-the-loop. Educational only.

## See Also
- [[multi-agent-orchestration]]
- [[autogen-multi-agent]]
- [[crewai-multi-agent]]
- [[langgraph-agent-orchestration]]
