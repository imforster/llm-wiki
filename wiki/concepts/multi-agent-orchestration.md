---
type: concept
created: 2026-04-07
updated: 2026-04-14
sources: ["[[scion-docs]]", "[[kiro-autonomous-agent]]", "[[claude-code-docs]]", "[[autogen-multi-agent]]", "[[crewai-multi-agent]]", "[[langgraph-agent-orchestration]]", "[[openai-swarm]]"]
tags: [multi-agent, orchestration, ai, architecture]
---

# Multi-Agent Orchestration

The practice of coordinating multiple LLM-based [[agent]]s to work on tasks concurrently, with isolation, specialization, and collaboration.

## Three Approaches Emerging

### Infrastructure-first: Scion

[[scion]] positions itself as a "hypervisor for agents" — providing the infrastructure layer (containers, isolation, lifecycle management) while treating higher-level concerns as orthogonal. Harness-agnostic. Emphasizes human interaction as imperative.

### Product-first: Kiro Autonomous Agent

[[kiro]]'s autonomous agent is an opinionated product — a [[frontier-agent]] that handles the full stack from task intake to PR creation. Coordinates specialized sub-agents internally. Emphasizes autonomy and independence.

### Tool-first: Claude Code

[[claude-code]] approaches multi-agent from the individual tool outward — custom subagents, agent teams, and a rich extensibility stack (MCP, plugins, skills, hooks). Terminal-native, multi-platform. The agent itself can spawn and coordinate other agents.

### Company-first: Paperclip

[[paperclip]] operates above all three — orchestrating agents into companies with org charts, budgets, goals, governance, and accountability. Agent-agnostic (works with Claude Code, Codex, Cursor, etc.). Not an agent framework — it's the organizational layer. "Manage business goals, not pull requests."

## Shared Patterns

All three share:
- **Isolated execution**: Containers (Scion) / sandboxes (Kiro) / permission modes (Claude Code)
- **Git-based workspaces**: Worktrees or branches per agent
- **Sub-agent coordination**: Agents spawning and managing other agents
- **PR-based output**: Changes surfaced as pull requests for human review
- **Extensibility**: Plugins (Scion), Powers (Kiro), MCP/plugins/skills (Claude Code), [[agent-skills-standard]] (open standard)

## Key Design Tensions

- **Autonomy vs. interaction**: Kiro favors long-running independence; Scion says interaction is imperative; Claude Code offers configurable permission modes
- **Opinionated vs. agnostic**: Kiro is a specific agent product; Scion is infrastructure for any agent; Claude Code is a specific tool that Scion can orchestrate
- **Isolation model**: Scion uses containers + `--yolo` mode; Kiro uses sandboxes; Claude Code uses permission modes within the tool itself

## Open-Source Multi-Agent Frameworks

Four open-source frameworks represent different coordination philosophies:

| Framework | Core Metaphor | Coordination | State | Best For |
|-----------|--------------|-------------|-------|----------|
| [[autogen-multi-agent]] | Conversation | Multi-turn dialogue | Conversation history | Research, prototyping |
| [[crewai-multi-agent]] | Team of experts | Sequential/hierarchical process | Short/long/entity memory | Complex research tasks |
| [[langgraph-agent-orchestration]] | State machine | Graph edges + conditions | Checkpointed, persistent | Production workflows |
| [[openai-swarm]] | Handoffs | Function returns | Context variables (ephemeral) | Simple routing |

**Convergence signal**: Both AutoGen (via Microsoft Agent Framework) and LangGraph are moving toward graph-based workflows with typed nodes and edges. This suggests graphs are becoming the consensus architecture for production multi-agent systems.

## Open Questions

- How should agents coordinate on shared state beyond git?
- What's the right granularity for task decomposition?
- How to handle conflicting changes from concurrent agents?
- Does persistent context/memory (Kiro, Claude Code) outperform fresh-context-per-task?
- Will [[mcp-protocol]] become the interoperability layer between these tools?
- What design principles make skills effective? (See [[ten-pillars-agentic-skill-design]] for a proposed framework)

## See Also
- [[scion]]
- [[kiro]]
- [[claude-code]]
- [[frontier-agent]]
- [[agent]]
- [[mcp-protocol]]
- [[agent-memory-persistence]]
- [[paperclip]]
