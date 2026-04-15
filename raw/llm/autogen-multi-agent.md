# AutoGen: Microsoft's Multi-Agent Framework

- **Author**: Microsoft Research (open-source)
- **Sources**: https://sanj.dev/post/autogen-microsoft-multi-agent-framework/, https://github.com/microsoft/autogen
- **Date**: Originally 2023, major transition 2026
- **Type**: Open-source multi-agent orchestration framework
- **GitHub Stars**: 56,800+

## What It Is

AutoGen is Microsoft Research's pioneering open-source framework for building applications where multiple AI agents collaborate. It handles message routing, dialogue history, and workflow execution for multi-agent systems.

## Current State (2026): Three Paths

1. **Microsoft Agent Framework (MAF)** — official production-grade successor. Merges AutoGen's orchestration with Semantic Kernel's enterprise stability. Explicit graph-based workflows.
2. **AutoGen v0.7.x** — stable maintenance line. Async actor-model architecture. Best for research and prototyping. Where Magentic-One (generalist agent team) lives.
3. **AG2** — community-led fork (ag2ai/ag2). Backward-compatible with legacy v0.2 "GroupChat" style.

AutoGen announced entering maintenance mode in 2026, with development shifting to Agent Framework.

## Core Architecture

- **Conversational agents**: agents communicate through structured multi-turn conversations
- **Message routing**: framework handles who speaks next and dialogue history
- **Code execution**: agents can write and execute code in sandboxed environments
- **Human-in-the-loop**: configurable human participation in agent conversations
- **Natural-language handoffs**: reduce bespoke protocol work

## Key Transition: GroupChat → Graph-based Workflows

Old way (v0.2): implicit "GroupChat" management where a Manager Agent decides who speaks next.
New way (MAF): explicit Workflow with typed nodes and edges. You define handoff logic explicitly.

## Microsoft Agent Framework (MAF)

- Unifies AutoGen + Semantic Kernel into single SDK
- Built-in checkpointing (designed for "millions of steps")
- Native Azure AI Foundry integration
- State persistence and observability for enterprise deployments
- Graph-based workflow definition with typed nodes and edges

## Magentic-One

Generalist agent team built on AutoGen that can:
- Browse the web
- Manage files
- Execute code autonomously
- Available as CLI tool: `m1 "task description"`

## Production Challenges

- Non-deterministic behavior: identical prompts can trigger wildly different agent dialogues
- Debugging multi-agent conversations is complex
- Overhead grows with number of specialized agents
- Context switching between agents while maintaining coherence is persistent challenge

## When to Use

- **Prototyping/research**: AutoGen v0.7.x (latest playground, Magentic-One components)
- **Production enterprise**: Microsoft Agent Framework (checkpointing, observability, Azure integration)
- **Legacy compatibility**: AG2 fork (backward-compatible with v0.2 GroupChat)

## Wiki Connection

Represents the "conversation-based" coordination philosophy — agents negotiate through structured dialogue. Contrasts with Scion (container isolation), Kiro (PR-based output), and Claude Code (permission modes). AutoGen's transition to graph-based workflows mirrors LangGraph's approach.
