---
type: source
created: 2026-04-14
updated: 2026-04-14
origin: llm
tags: [multi-agent, orchestration, role-based, open-source, memory]
---

# CrewAI: Role-Based Multi-Agent Orchestration

[Original](https://kindatechnical.com/agentic-ai/crewai-role-based-multi-agent-orchestration.html) | [Raw](../../raw/llm/crewai-multi-agent.md)

Open-source Python framework by João Moura for role-based multi-agent systems. Agents defined by role + goal + backstory, organized into "crews" with sequential or hierarchical process strategies.

## Four Core Abstractions

1. **Agent** — role, goal, backstory, tools. Backstory shapes personality.
2. **Task** — work assigned to agent, with dependencies via `context` parameter.
3. **Crew** — collection of agents + tasks + process strategy.
4. **Process** — sequential (ordered) or hierarchical (manager delegates).

## Memory System

- **Short-term** — context within current crew execution
- **Long-term** — lessons learned across executions
- **Entity memory** — info about specific entities encountered

Cross-agent knowledge sharing and stateful execution built in.

## Key Design: Role + Backstory

Unlike other frameworks where agents are just system prompts, CrewAI's backstory shapes the agent's personality and approach. "Senior Security Auditor" with a detailed backstory produces different output than a generic "Reviewer." This is a form of persona-based [[context-management]].

## See Also
- [[multi-agent-orchestration]]
- [[autogen-multi-agent]]
- [[langgraph-agent-orchestration]]
- [[context-management]]
