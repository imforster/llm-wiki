# CrewAI: Role-Based Multi-Agent Orchestration

- **Author**: João Moura (open-source)
- **Source**: https://kindatechnical.com/agentic-ai/crewai-role-based-multi-agent-orchestration.html
- **GitHub**: https://github.com/crewAIInc/crewAI
- **Date**: 2024 (initial), ongoing development
- **Type**: Open-source Python framework for role-based multi-agent systems

## What It Is

CrewAI orchestrates role-playing autonomous AI agents that work together as a cohesive team ("crew"). Built on the insight that the best results come from teams of specialized agents, each with a distinct role, expertise, and perspective — like a real team of human experts.

## Four Core Abstractions

1. **Agent** — autonomous entity with role, goal, backstory, and tools. Backstory shapes personality and approach.
2. **Task** — specific work assigned to an agent, with description, expected output, and optional dependencies.
3. **Crew** — collection of agents and tasks with a process strategy defining coordination.
4. **Process** — execution strategy: sequential, hierarchical, or consensual.

## Process Strategies

- **Sequential**: tasks execute in order. Each receives output of previous tasks via `context` parameter. Simplest and most predictable.
- **Hierarchical**: a manager agent automatically delegates tasks to the most appropriate crew member. Can reassign work if quality is insufficient.

## Memory System

Three memory types:
- **Short-term memory** — context within current crew execution
- **Long-term memory** — lessons learned across multiple executions
- **Entity memory** — information about specific entities encountered

Supports cross-agent knowledge sharing and multi-turn stateful execution.

## Key Design Decisions

- **Role-based**: agents defined by role + goal + backstory (not just instructions)
- **Delegation**: agents with `allow_delegation=True` can ask other crew members for help
- **Task dependencies**: tasks connected through `context` parameter so agents build on each other's work
- **Tool integration**: agents can use external tools (search, web scraping, file reading, code execution)

## Comparison to Other Frameworks

| Feature | CrewAI | AutoGen | LangGraph | Swarm |
|---------|--------|---------|-----------|-------|
| Core metaphor | Team of experts | Conversation | State machine | Handoffs |
| Agent definition | Role + goal + backstory | System prompt + functions | Node in graph | System prompt + functions |
| Coordination | Sequential/hierarchical process | Multi-turn dialogue | Graph edges + conditions | Function-based handoffs |
| Memory | Short/long/entity memory | Conversation history | Checkpointed state | Context variables |
| Best for | Complex research tasks | Code generation + review | Stateful workflows | Customer service routing |

## Wiki Connection

CrewAI represents the "team of experts" coordination philosophy. Aligns with wiki Theme 2 (Composition over Monoliths) — each agent is specialized. The role/backstory pattern is a form of persona-based context management (wiki Pillar 9). Memory system maps to the wiki's memory hierarchy discussion. Contrasts with Scion (infrastructure-level isolation) and Paperclip (company-level orchestration).
