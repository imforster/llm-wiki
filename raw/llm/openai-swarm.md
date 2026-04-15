# OpenAI Swarm: Lightweight Multi-Agent Orchestration

- **Author**: OpenAI
- **Source**: https://kindatechnical.com/agentic-ai/openai-swarm-and-handoff-patterns.html
- **GitHub**: https://github.com/openai/swarm
- **Date**: October 2024 (released)
- **Type**: Experimental/educational multi-agent framework

## What It Is

Swarm is OpenAI's experimental framework for lightweight multi-agent orchestration. Radically simple: agents are just system prompts with functions, and handoffs are just functions that return another agent. No complex orchestration layer, no state machines, no message queues — just function calls that transfer control.

Explicitly NOT intended for production use. Educational framework demonstrating patterns implementable with any LLM SDK.

## Two Core Primitives

1. **Routines** — a system prompt + a set of callable functions that define an agent's capabilities
2. **Handoffs** — functions that return another Agent object, transferring conversation control

That's it. The entire framework adds just these two concepts on top of the Chat Completions API.

## How Handoffs Work

A handoff is a regular Python function that returns an Agent:
```
def transfer_to_billing():
    """Transfer the customer to the billing specialist."""
    return billing_agent
```

When the LLM calls this function, Swarm transfers control to the returned agent. The docstring tells the LLM when to invoke the handoff.

## Context Variables

Shared state passed between agents without putting it in conversation history:
- customer_id, region, plan tier, etc.
- Passed at runtime, available to all agents via `context_variables` parameter
- Keeps sensitive data out of conversation history

## Dynamic Instructions

Agent instructions can be functions that incorporate context variables — instructions adapt based on customer plan, region, etc.

## Design Philosophy

- Intentionally minimal — demonstrates patterns, not a production framework
- Shows that multi-agent orchestration doesn't require complex infrastructure
- Handoff pattern is production-ready even if Swarm itself isn't
- Can be implemented with any LLM SDK (OpenAI, Anthropic, etc.)

## When to Use Swarm vs. Others

| Scenario | Best Framework |
|----------|---------------|
| Customer service routing | Swarm (natural handoff pattern) |
| Complex research tasks | CrewAI (role-based delegation) |
| Code generation with review | AutoGen (conversational iteration) |
| Stateful workflows | LangGraph (checkpoint and persistence) |
| Simple routing | Swarm pattern DIY (no framework needed) |

## Limitations

- No state persistence across sessions
- No built-in memory beyond context variables
- No checkpointing or pause/resume
- Educational only — OpenAI explicitly says not for production
- No built-in human-in-the-loop mechanisms
- Overhead grows as number of specialized agents increases

## Wiki Connection

Swarm represents the minimalist end of the orchestration spectrum. Aligns with wiki Theme 2 (Composition) — each agent is a focused unit. The handoff pattern maps to wiki's autonomy spectrum (Theme 3) at the "more human control" end — explicit routing rather than autonomous coordination. Contrasts with Scion's container isolation and Kiro's autonomous frontier agents. The "implement it yourself" philosophy echoes PAI's CODE → CLI → PROMPT → SKILL hierarchy — use the simplest tool that works.
