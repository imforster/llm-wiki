# OpenAI Agents SDK

Source: https://github.com/openai/openai-agents-python + https://fast.io/resources/openai-agents-sdk/
Retrieved: 2026-05-11

## Overview

The OpenAI Agents SDK is a Python framework for building multi-agent systems with handoffs, guardrails, and tool integration on top of OpenAI models. Launched as the production-ready successor to the experimental Swarm framework, it provides the "glue" code needed to make multiple LLMs work together as a cohesive team.

- **GitHub**: github.com/openai/openai-agents-python (26.2K stars as of May 2026)
- **License**: MIT
- **Language**: Python (TypeScript later)
- **Status**: Production-ready (replaces experimental Swarm)

## Core Primitives

1. **Agent**: A class wrapping a model configuration (like GPT-4o) and a set of tools (Python functions). Includes instructions (system prompt), tools, handoffs, and guardrails.
2. **Handoff**: A function that returns another Agent. When an agent determines it cannot fulfill a request, it calls a handoff tool. The SDK handles the context switch automatically, ensuring the new agent receives the relevant conversation history.
3. **Guardrails**: Safety checks that validate inputs and outputs. Can block execution or modify behavior based on rules.
4. **Tracing**: Built-in OpenTelemetry support for debugging agent reasoning paths and handoff decisions.

## Key Differences from Swarm

- **Production-ready**: Better error handling, more predictable routing logic
- **Guardrails**: Built-in input/output validation (Swarm had none)
- **Tracing**: Full observability via OpenTelemetry (Swarm had none)
- **MCP Support**: Native Model Context Protocol integration for external tools
- **Human-in-the-loop**: Configurable approval gates for sensitive actions
- **Persistent state**: Session management across turns (Swarm was ephemeral)
- **Sandboxing**: Tool execution in isolated containers for security

## Architecture

The architecture relies on two main concepts: Agents and Handoffs.

- An Agent wraps a model configuration and a set of tools
- A Handoff is a function that returns another Agent
- When an agent determines it cannot fulfill a request, it calls a handoff tool
- The SDK handles the context switch automatically

### Why Handoffs Matter

- **Specialization**: Use cheaper models (GPT-4o-mini) for routing, stronger models for complex reasoning
- **Context Management**: Handoffs prevent context windows from overflowing by only passing necessary information
- **Modularity**: Update one agent's logic without breaking others

## Multi-Agent Patterns

### Triage/Router Pattern
```python
from openai_agents import Agent, run

support_agent = Agent(
    name="Support",
    instructions="Handle technical support requests.",
    tools=[search_docs, create_ticket]
)

sales_agent = Agent(
    name="Sales",
    instructions="Handle sales inquiries.",
    tools=[check_pricing, schedule_demo]
)

def transfer_to_support():
    """Hand off to support agent."""
    return support_agent

def transfer_to_sales():
    """Hand off to sales agent."""
    return sales_agent

triage_agent = Agent(
    name="Triage",
    instructions="Route user requests to the appropriate specialist.",
    tools=[transfer_to_support, transfer_to_sales]
)
```

### Production Control Patterns (April 2026 Update)

OpenAI expanded the SDK with explicit production control patterns:

1. **Guardrails**: Validation and blocking layer for risky work
2. **Human Approvals**: Pause a run before sensitive actions
3. **Orchestration**: Decides whether a specialist takes ownership or acts as a bounded helper
4. **MCP Trust Boundaries**: Controls how the agent reaches external capabilities
5. **Tracing + Trace-based Evals**: Score workflow behavior

## May 2026 Update: Sandbox Environments

The updated Agents SDK helps developers build agents that can:
- Inspect files
- Run commands
- Edit code
- Work on long-horizon tasks within controlled sandbox environments

This positions it for coding agent use cases similar to Codex.

## Comparison to Other Frameworks

- **vs LangGraph**: Agents SDK is simpler (fewer abstractions) but less flexible. No graph-based workflows, no checkpointing. Best for OpenAI-model-only deployments.
- **vs CrewAI**: Agents SDK uses handoffs (function returns) vs CrewAI's role+backstory. Less opinionated about agent personality.
- **vs Google ADK**: Agents SDK is OpenAI-model-locked; ADK is model-agnostic. ADK has workflow agents (Sequential/Parallel/Loop); Agents SDK relies on handoff chains.
- **vs Microsoft Agent Framework**: MAF supports .NET + Python, six providers; Agents SDK is Python-only, OpenAI-only. MAF has graph workflows; Agents SDK has flat handoffs.

## Key Signals

- Swarm is now officially legacy/educational — Agents SDK is the production path
- 26.2K GitHub stars indicates strong adoption
- OpenAI investing in sandbox environments signals coding agent ambitions
- MCP support makes it interoperable with the broader tool ecosystem
- Still OpenAI-model-locked (no multi-provider support)
