---
type: analysis
created: 2026-04-15
updated: 2026-05-09
sources: ["[[autogen-multi-agent]]", "[[crewai-multi-agent]]", "[[langgraph-agent-orchestration]]", "[[openai-swarm]]", "[[scion-docs]]", "[[kiro-autonomous-agent]]", "[[claude-code-docs]]", "[[paperclip]]", "[[gastown]]", "[[symphony]]", "[[multica]]"]
tags: [analysis, multi-agent, orchestration, frameworks, comparison]
---

# Choosing a Multi-Agent Framework in 2026

Synthesized from 11 sources across this wiki (updated May 2026 with Gas Town, Symphony, and Multica). This analysis compares the open-source multi-agent frameworks and orchestration tools, maps their coordination philosophies, and provides a practical decision framework.

---

## The Landscape: Three Tiers

The wiki now covers eleven distinct approaches to multi-agent orchestration, split across three tiers:

**Product-level** (opinionated, integrated):

| Tool | Philosophy | Layer |
|------|-----------|-------|
| [[scion]] | Infrastructure-first. Hypervisor for agents. Container isolation. | Infrastructure |
| [[kiro]] | Product-first. Frontier agent. Hours of autonomy. PR output. | Tool |
| [[claude-code]] | Tool-first. Subagents, MCP, skills, permission modes. | Tool |
| [[paperclip]] | Company-first. Org charts, budgets, governance above agents. | Company |

**Orchestration tools** (workspace/platform-level, agent-agnostic):

| Tool | Philosophy | Core Metaphor |
|------|-----------|---------------|
| [[gastown]] | Workspace-first. Git worktrees, merge queue, 20-30 agents. Process model. | Town with Mayor, Polecats, Refinery |
| [[symphony]] | Spec-first. Language-agnostic protocol. WORKFLOW.md. Per-issue workspaces. | Scheduler/runner daemon |
| [[multica]] | Platform-first. Agents as teammates. Compounding skills. Cloud-first. | Team collaboration board |

**Open-source frameworks** (composable, bring-your-own-model):

| Framework | Philosophy | Core Metaphor |
|-----------|-----------|---------------|
| [[autogen-multi-agent]] | Conversation-based | Agents negotiate through dialogue |
| [[crewai-multi-agent]] | Role-based teams | Specialized experts collaborate |
| [[langgraph-agent-orchestration]] | Explicit state machines | Graph nodes + edges + checkpoints |
| [[openai-swarm]] | Minimal handoffs | Functions that return agents |

These aren't competing — they operate at different levels. You might use LangGraph to orchestrate agents that run inside Claude Code, coordinated by Gas Town at the workspace level, with Paperclip managing company goals above.

---

## The Four Open-Source Frameworks Compared

### AutoGen (Microsoft)

**Core idea**: Agents communicate through structured multi-turn conversations. The framework handles message routing and dialogue history.

- **56.8K GitHub stars** — largest community
- **Transitioning**: entering maintenance mode in 2026. Development shifting to Microsoft Agent Framework (MAF), which merges AutoGen + Semantic Kernel into graph-based workflows.
- **Magentic-One**: generalist agent team (web browsing, file management, code execution). CLI: `m1 "task"`
- **Strengths**: Pioneering framework, large ecosystem, code execution built in
- **Weaknesses**: Non-deterministic behavior, complex debugging, implicit coordination (Manager Agent decides who speaks)
- **Best for**: Research, prototyping, code generation + review workflows

**Key signal**: AutoGen moving to graph-based workflows validates LangGraph's approach.

### CrewAI (João Moura)

**Core idea**: Agents defined by role + goal + backstory, organized into "crews" with process strategies.

- **Four abstractions**: Agent, Task, Crew, Process
- **Process strategies**: Sequential (ordered) or Hierarchical (manager delegates, can reassign)
- **Built-in memory**: short-term (current execution), long-term (across executions), entity memory
- **Role + backstory**: shapes agent personality. "Senior Security Auditor" with detailed backstory produces different output than generic "Reviewer." This is persona-based [[context-management]].
- **Strengths**: Intuitive team metaphor, built-in memory, delegation support
- **Weaknesses**: Less explicit control than graphs, process strategies are coarse-grained
- **Best for**: Complex research tasks, content creation, multi-perspective analysis

**Key insight**: CrewAI's backstory pattern is the most accessible way to implement the [[ten-pillars-agentic-skill-design]] Pillar 9 (persona templates).

### LangGraph (LangChain)

**Core idea**: Agent workflows as explicit state-machine graphs. Nodes are LLM calls or tools. Edges define transitions.

- **Checkpointing**: pause/resume at any point, survive process restarts. The killer feature.
- **Human-in-the-loop**: first-class at any node (not bolted on)
- **Conditional edges**: branching based on state (deterministic or LLM-decided)
- **Cycles**: graphs can loop for iterative refinement (unlike simple chains)
- **Streaming**: intermediate results available as workflow progresses
- **LangSmith integration**: tracing and debugging
- **Strengths**: Most production-ready OSS framework, explicit control, error recovery in graph structure
- **Weaknesses**: Steeper learning curve, graph definition overhead for simple tasks
- **Best for**: Production workflows, stateful long-running tasks, anything needing pause/resume or human approval gates

**Key insight**: LangGraph is where you go when "it works in a demo" needs to become "it works in production."

### OpenAI Swarm

**Core idea**: Agents are system prompts with functions. Handoffs are functions that return another agent. That's it.

- **Two primitives**: Routines (prompt + functions) and Handoffs (function → agent)
- **Context variables**: shared state without polluting conversation history
- **Dynamic instructions**: agent prompts can be functions incorporating context
- **Explicitly educational**: OpenAI says NOT for production
- **Strengths**: Radically simple, demonstrates core patterns, implementable with any SDK
- **Weaknesses**: No persistence, no memory, no checkpointing, no human-in-the-loop
- **Best for**: Learning multi-agent patterns, customer service routing, simple triage

**Key insight**: The handoff pattern IS production-ready even though Swarm isn't. You can implement it in 50 lines with any LLM SDK.

---

## Decision Matrix

| Factor | AutoGen | CrewAI | LangGraph | Swarm |
|--------|---------|--------|-----------|-------|
| Production readiness | ★★ (transitioning) | ★★ | ★★★ | ★ (educational) |
| Ease of getting started | ★★ | ★★★ | ★★ | ★★★ |
| Explicit control | ★★ (implicit dialogue) | ★★ (process strategies) | ★★★ (graph edges) | ★★ (function returns) |
| State persistence | ★★ (conversation) | ★★ (short/long/entity) | ★★★ (checkpointed) | ★ (context vars only) |
| Human-in-the-loop | ★★ (configurable) | ★★ (via delegation) | ★★★ (any node) | ★ (not built in) |
| Memory | ★★ (conversation history) | ★★★ (three types) | ★★ (checkpointed state) | ★ (ephemeral) |
| Community/ecosystem | ★★★ (56.8K stars) | ★★ | ★★★ (LangChain ecosystem) | ★★ (OpenAI backing) |
| Debugging | ★ (non-deterministic) | ★★ | ★★★ (graph visualization) | ★★ (simple = debuggable) |

---

## When to Use What

```
Learning multi-agent patterns?        → Swarm (simplest mental model)
Research / prototyping?               → AutoGen or CrewAI
Content creation / multi-perspective? → CrewAI (role + backstory)
Code generation + review?             → AutoGen (Magentic-One)
Production stateful workflows?        → LangGraph (checkpointing)
Customer service routing?             → Swarm pattern (DIY or framework)
Need human approval gates?            → LangGraph (human-in-loop at any node)
Enterprise with Azure?                → Microsoft Agent Framework (MAF)
```

### Progression Path

Similar to memory architectures, start simple and add complexity:

1. **Learn**: Build a Swarm-style handoff system to understand the patterns
2. **Prototype**: Use CrewAI for quick multi-agent prototypes (intuitive team metaphor)
3. **Production**: Move to LangGraph when you need checkpointing, human-in-the-loop, or error recovery
4. **Scale**: Consider MAF for enterprise Azure integration or Paperclip for company-level orchestration

---

## The Convergence Toward Graphs

The most significant finding across all sources: **graph-based workflows are becoming the consensus architecture for production multi-agent systems.**

Evidence:
- [[langgraph-agent-orchestration]] built on graphs from day one
- [[autogen-multi-agent]] transitioning from implicit GroupChat to explicit graph-based MAF
- [[scion]] uses directed workflows for agent coordination
- [[kiro]] coordinates sub-agents through structured task graphs internally

Why graphs win:
- **Explicit**: you define the flow, not the conversation
- **Debuggable**: visualize the graph, trace execution path
- **Checkpointable**: pause/resume at any node
- **Composable**: subgraphs as reusable components
- **Enforceable**: security invariants at the graph level

The conversation-based approach (AutoGen v0.2 GroupChat) is being abandoned by its own creators. The role-based approach (CrewAI) works well for simpler workflows but lacks the explicit control graphs provide. The handoff approach (Swarm) is a lightweight graph in disguise.

---

## How Product-Level Tools Relate

The open-source frameworks don't replace the product-level tools — they complement them:

| Tool | What It Provides | Framework Complement |
|------|-----------------|---------------------|
| [[claude-code]] | The agent itself (LLM + tools + skills) | LangGraph/CrewAI orchestrate multiple Claude Code instances |
| [[kiro]] | Autonomous frontier agent | Could be a node in a LangGraph workflow |
| [[scion]] | Container isolation + lifecycle | Provides the runtime for any framework's agents |
| [[gastown]] | Workspace orchestration + merge queue | Coordinates Claude Code/Codex/Copilot with persistent state (20-30 agents) |
| [[symphony]] | Issue-to-agent automation | Reads Linear, spawns Codex sessions per issue with WORKFLOW.md policy |
| [[multica]] | Team collaboration platform | Assigns issues to agents, tracks progress, compounds skills (11 runtimes) |
| [[paperclip]] | Company-level governance | Sits above frameworks, manages goals and budgets |

The emerging stack (updated May 2026):

```
Paperclip (company goals/governance)
    → Multica (team collaboration + skill compounding)
        → Gas Town (workspace orchestration + merge queue)
            → LangGraph/MAF (workflow graphs)
                → Claude Code/Kiro/Codex (individual agents)
                    → Scion (infrastructure isolation)
```

### The Architectural Split (May 2026 Update)

External comparison sources reveal a fundamental split in how multi-agent systems coordinate:

| Architecture | Control Plane | Scale | Tools |
|---|---|---|---|
| **Conversation-as-control** | LLM routes via messages | 3-5 agents | AutoGen, CrewAI, Swarm |
| **Graph-as-control** | Explicit edges + conditions | 5-15 agents | LangGraph, MAF |
| **Process-model** | Deterministic routing via external state | 20-30 agents | Gas Town |
| **Issue-tracker-driven** | Tracker polls + workspace isolation | Bounded (default 10) | Symphony |
| **Platform-driven** | Web UI + daemon dispatch | Runtime-bound | Multica |

Gas Town is the only tool using a **process model** — agents coordinate via external state (Dolt/Git), not via LLM conversation. This is why it scales to 20-30 parallel agents while conversation-based frameworks struggle beyond 3-5.

---

## Coordination Patterns Across All Eleven Approaches

| Pattern | Who Uses It | How |
|---------|------------|-----|
| **Git-based coordination** | Scion, Kiro, Claude Code, Gas Town, Symphony | Worktrees/branches per agent, PRs as output |
| **Conversation-based** | AutoGen, Claude Code (subagents) | Agents negotiate through dialogue |
| **Graph-based** | LangGraph, MAF, Scion | Explicit nodes + edges + conditions |
| **Role-based delegation** | CrewAI, Paperclip, Gas Town | Specialized agents with defined responsibilities |
| **Function handoffs** | Swarm, Claude Code (tool use) | Functions transfer control between agents |
| **Process-model (GUPP)** | Gas Town | Pull-based: work on hook → agent executes immediately |
| **Issue-tracker polling** | Symphony, Multica | Daemon reads issues, dispatches agents per task |
| **Container isolation** | Scion | Each agent in its own container, no shared context |
| **Permission modes** | Claude Code | Configurable dial from full control to full autonomy |
| **Compounding skills** | Multica | Solutions become reusable team capabilities |

---

## The Multi-Agent Memory Problem

Multi-agent systems multiply the [[agent-memory-persistence]] challenge:

- **Shared memory**: How do agents share what they've learned? CrewAI has built-in cross-agent memory. LangGraph uses checkpointed state. Swarm has only ephemeral context variables.
- **Conflicting memories**: When Agent A and Agent B learn contradictory facts, who wins? No framework has a standard resolution mechanism.
- **Cascading permissions**: When Agent A delegates to Agent B, does B inherit A's full memory access? ([[agentic-ai-governance]] flags this as a key risk)
- **Cost multiplication**: Each agent in a multi-agent system consumes tokens independently. Poor memory management across N agents means N× the waste ([[agent-cost-economics]]).

---

## Production Challenges (Common Across All)

1. **Non-determinism**: Same input → different agent dialogues → different outcomes. Testing is hard.
2. **Debugging complexity**: Tracing failures across multiple agents is significantly harder than single-agent debugging. LangGraph's graph visualization helps most here.
3. **Context switching overhead**: Maintaining coherence as control passes between agents. Each handoff risks losing context.
4. **Cost scaling**: More agents = more tokens. Model routing ([[agent-cost-economics]]) becomes critical.
5. **Emergent behavior**: Individual agents within guardrails can produce unanticipated combined outcomes ([[agentic-ai-governance]]).

---

## Recommendations

1. **If you're new to multi-agent**: Start with Swarm's handoff pattern. Build it yourself in 50 lines. Understand the primitives before adopting a framework.

2. **If you need a quick prototype**: CrewAI. Define roles, backstories, tasks. Sequential process. You'll have a working multi-agent system in an afternoon.

3. **If you're going to production**: LangGraph. Checkpointing, human-in-the-loop, explicit graph control, and debugging tools are non-negotiable for production.

4. **If you're on Azure/Microsoft**: Microsoft Agent Framework (MAF). It's where AutoGen is going, with enterprise features built in.

5. **If you need company-level orchestration**: [[paperclip]] above whatever framework you choose. It manages goals and budgets, not agent internals.

6. **If you need 20-30 parallel agents**: [[gastown]]. Process-model architecture with crash-surviving state, merge queue, and three-tier monitoring. Requires tmux comfort.

7. **If you want issue-tracker-driven automation**: [[symphony]]. Minimal infrastructure (no DB, no UI), WORKFLOW.md as policy-as-code. Currently Linear-only, Codex-only.

8. **If you want agents as teammates on a team board**: [[multica]]. Cloud-first platform with compounding skills, 11 runtime support, multi-user collaboration.

9. **For everyone**: Plan for the graph convergence. Even if you start with CrewAI or Swarm, your production system will likely end up as a graph. But note: Gas Town's process-model proves graphs aren't the only path to scale.

---

## Progression Path (Updated May 2026)

1. **Learn**: Build a Swarm-style handoff system to understand the patterns
2. **Prototype**: Use CrewAI for quick multi-agent prototypes (intuitive team metaphor)
3. **Automate**: Use Symphony to turn issue tracker work into autonomous agent runs
4. **Production**: Move to LangGraph when you need checkpointing, human-in-the-loop, or error recovery
5. **Scale**: Gas Town for 20-30 parallel agents with merge queue and monitoring
6. **Collaborate**: Multica when your team (humans + agents) needs shared visibility
7. **Govern**: Paperclip for company-level orchestration with budgets and accountability

---

## Open Questions

- Will MCP become the standard interoperability layer between frameworks?
- Can CrewAI's intuitive role metaphor be preserved within a graph-based architecture?
- How should multi-agent memory be shared without cascading errors?
- What's the right granularity for task decomposition across agents?
- Will the product-level tools (Claude Code, Kiro) eventually embed framework-level orchestration natively?
- Will Symphony expand beyond Linear? The spec mentions pluggable tracker adapters as future work.
- Will Gas Town's process-model be adopted by others, or remain unique?
- Will cross-model adversarial review (Metaswarm pattern) become standard for trust?
- Can Multica's compounding skills scale to large teams?

---

*Analysis based on 11 sources ingested into this wiki between 2026-04-07 and 2026-05-09. Updated May 2026 with Gas Town, Symphony, and Multica. See [[orchestration-tools-compared]] for the detailed head-to-head analysis.*

## See Also
- [[multi-agent-orchestration]]
- [[orchestration-tools-compared]]
- [[gastown]]
- [[symphony]]
- [[multica]]
- [[agent-memory-persistence]]
- [[memory-architecture-comparison]]
- [[agent-cost-economics]]
- [[agentic-ai-governance]]
