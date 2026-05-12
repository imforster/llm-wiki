---
type: source
created: 2026-04-14
updated: 2026-05-11
origin: llm
tags: [multi-agent, orchestration, microsoft, open-source, conversation]
---

# AutoGen: Microsoft's Multi-Agent Framework

[Original](https://sanj.dev/post/autogen-microsoft-multi-agent-framework/) | [Raw](../../raw/llm/autogen-multi-agent.md)

Microsoft Research's pioneering open-source framework (56.8K GitHub stars) for multi-agent collaboration. Agents communicate through structured multi-turn conversations.

> ⚠️ **Legacy (May 2026)**: AutoGen is now in maintenance mode. [[microsoft-agent-framework|Microsoft Agent Framework 1.0]] shipped GA on April 3, 2026, merging AutoGen + Semantic Kernel into a single production SDK. Plan migrations during 2026.

## Current State (2026): Three Paths

1. **Microsoft Agent Framework (MAF)** — production successor. Merges AutoGen + Semantic Kernel. Graph-based workflows, checkpointing, Azure AI Foundry integration.
2. **AutoGen v0.7.x** — maintenance line. Async actor-model. Research/prototyping. Home of Magentic-One.
3. **AG2** — community fork. Backward-compatible with v0.2 GroupChat.

## Key Transition: GroupChat → Graph Workflows

Old: implicit GroupChat where Manager Agent decides who speaks next. New (MAF): explicit Workflow with typed nodes and edges. This convergence toward graph-based orchestration mirrors [[langgraph-agent-orchestration]].

## Magentic-One

Generalist agent team: web browsing, file management, code execution. Available as CLI: `m1 "task"`.

## Production Challenges

Non-deterministic behavior, complex debugging, growing overhead with agent count, context switching between agents.

## See Also
- [[multi-agent-orchestration]]
- [[langgraph-agent-orchestration]]
- [[crewai-multi-agent]]
