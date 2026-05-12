---
type: analysis
created: 2026-04-15
updated: 2026-05-11
sources: ["[[autogen-multi-agent]]", "[[crewai-multi-agent]]", "[[langgraph-agent-orchestration]]", "[[openai-swarm]]", "[[openai-agents-sdk]]", "[[google-adk]]", "[[microsoft-agent-framework]]", "[[scion-docs]]", "[[kiro-autonomous-agent]]", "[[claude-code-docs]]", "[[paperclip]]", "[[gastown]]", "[[symphony]]", "[[multica]]"]
tags: [analysis, multi-agent, orchestration, frameworks, comparison]
---

# Choosing a Multi-Agent Framework in 2026

Synthesized from 14 sources across this wiki (updated May 2026). This analysis compares multi-agent frameworks and orchestration tools, maps their coordination philosophies, and provides a practical decision framework.

---

## The Landscape: Three Tiers

The wiki now covers fourteen distinct approaches to multi-agent orchestration, split across three tiers:

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

| Framework | Philosophy | Core Metaphor | Status |
|-----------|-----------|---------------|--------|
| [[openai-agents-sdk]] | Handoffs + guardrails | Functions that return agents | ✅ Active (26.2K stars) |
| [[google-adk]] | Workflow agents + transfer | Sequential/Parallel/Loop hierarchy | ✅ Active (ADK 2.0 beta) |
| [[microsoft-agent-framework]] | Graph workflows | Typed nodes + edges | ✅ Active (1.0 GA, LTS) |
| [[langgraph-agent-orchestration]] | Explicit state machines | Graph nodes + edges + checkpoints | ✅ Active (v1.0) |
| [[crewai-multi-agent]] | Role-based teams | Specialized experts collaborate | ✅ Active (v1.10+) |
| [[autogen-multi-agent]] | Conversation-based | Agents negotiate through dialogue | ⚠️ Legacy (→ MAF) |
| [[openai-swarm]] | Minimal handoffs | Functions that return agents | ⚠️ Legacy (→ Agents SDK) |

These aren't competing — they operate at different levels. You might use LangGraph to orchestrate agents that run inside Claude Code, coordinated by Gas Town at the workspace level, with Paperclip managing company goals above.

---

## The Seven Frameworks Compared

### OpenAI Agents SDK ✅

**Core idea**: Production successor to Swarm. Agents are model configs with tools. Handoffs are functions that return another agent. Adds guardrails, tracing, MCP, and sandboxes.

- **26.2K GitHub stars** — strong adoption
- **Python-only**, OpenAI-model-locked
- **Guardrails**: Input/output validation (Swarm had none)
- **Tracing**: Native OpenTelemetry for debugging handoff decisions
- **MCP support**: Native tool integration via Model Context Protocol
- **Sandboxes** (May 2026): Isolated environments for code execution, file inspection, long-horizon tasks
- **Strengths**: Simplest mental model, production-ready, excellent for OpenAI-only deployments
- **Weaknesses**: No multi-provider support, no graph workflows, Python-only
- **Best for**: Teams committed to OpenAI models wanting fast multi-agent prototypes that can go to production

**Key signal**: The handoff pattern from Swarm is now production-grade with proper guardrails and observability.

### Google Agent Development Kit (ADK) ✅

**Core idea**: Model-agnostic framework with deterministic workflow agents (Sequential/Parallel/Loop) plus LLM-driven delegation. Native A2A + MCP interoperability.

- **Four languages**: Python, TypeScript, Go, Java — broadest language support in the space
- **Model-agnostic**: Gemini, Claude, Ollama, vLLM, LiteLLM (10+ providers)
- **Workflow agents**: SequentialAgent, ParallelAgent, LoopAgent — deterministic orchestration without LLM overhead
- **Three interaction mechanisms**: Shared state, LLM transfer, AgentTool wrapping
- **Native A2A**: Expose/consume agents across frameworks via Agent-to-Agent protocol
- **Native MCP**: Full tool integration
- **ADK 2.0 Beta**: Graph-based workflows, collaborative agents, dynamic workflows
- **Built-in evaluation**: Multi-turn eval datasets, local eval via CLI/UI
- **Strengths**: Most polyglot, most interoperable, deterministic workflow control, built-in eval
- **Weaknesses**: Google ecosystem bias in deployment (Cloud Run, GKE), newer community
- **Best for**: Multi-language teams, model-agnostic deployments, teams needing A2A interop

**Key signal**: ADK 2.0 adding graph workflows validates the convergence thesis while keeping deterministic workflow agents as a unique differentiator.

### Microsoft Agent Framework 1.0 ✅

**Core idea**: Convergence of Semantic Kernel (foundation) + AutoGen (orchestration) into one production SDK with graph-based workflows, six providers, and LTS commitment.

- **1.0 GA**: April 3, 2026 — first enterprise agent SDK with LTS
- **75K+ stars merged**: Combined community of Semantic Kernel + AutoGen
- **.NET + Python**: Same concepts, same API shape, idiomatic in each language
- **Six providers**: Azure OpenAI, OpenAI, Claude, Bedrock, Gemini, Ollama — one-line swap
- **Graph workflows**: Round-robin, supervisor, hierarchical, dynamic hand-off
- **Native MCP + A2A**: Full interoperability at 1.0
- **DevUI**: Browser-based local debugger (message graphs, tool invocations, token latency, orchestration decisions)
- **Strengths**: Enterprise-grade, LTS, broadest provider support, excellent debugging, .NET first-class
- **Weaknesses**: Microsoft ecosystem bias, newer than LangGraph for graph workflows
- **Best for**: Enterprise teams, Azure-centric stacks, .NET shops, teams needing LTS guarantees

**Key signal**: AutoGen and Semantic Kernel are now officially legacy. MAF is the canonical Microsoft path through 2027+.

### LangGraph (LangChain) ✅

**Core idea**: Agent workflows as explicit state-machine graphs. Nodes are LLM calls or tools. Edges define transitions.

- **v1.0 shipped** (2026) — mature, battle-tested
- **Checkpointing**: Pause/resume at any point, survive process restarts. The killer feature.
- **Human-in-the-loop**: First-class at any node (not bolted on)
- **Conditional edges**: Branching based on state (deterministic or LLM-decided)
- **Cycles**: Graphs can loop for iterative refinement
- **Streaming**: Intermediate results as workflow progresses
- **LangSmith integration**: Tracing and debugging
- **Production users**: Klarna, Replit, Elastic, Uber, LinkedIn, GitLab
- **Strengths**: Most battle-tested graph framework, explicit control, error recovery, checkpointing
- **Weaknesses**: Steeper learning curve, LangChain ecosystem coupling, Python/TypeScript only
- **Best for**: Production stateful workflows, anything needing pause/resume or human approval gates

**Key insight**: LangGraph is where you go when "it works in a demo" needs to become "it works in production." Now at v1.0 with proven enterprise adoption.

### CrewAI ✅

**Core idea**: Agents defined by role + goal + backstory, organized into "crews" with process strategies.

- **v1.10+** with A2A/MCP support, Flows, Enterprise platform
- **Four abstractions**: Agent, Task, Crew, Process
- **Process strategies**: Sequential or Hierarchical (manager delegates)
- **Built-in memory**: Short-term, long-term, entity memory
- **Flows**: Structured workflow orchestration (added 2025)
- **Role + backstory**: Persona-based [[context-management]] — shapes agent behavior
- **Strengths**: Most intuitive team metaphor, built-in memory, A2A/MCP support, Enterprise platform
- **Weaknesses**: Less explicit control than graphs, process strategies are coarse-grained
- **Best for**: Complex research tasks, content creation, multi-perspective analysis, rapid prototyping

**Key insight**: CrewAI's backstory pattern remains the most accessible way to implement persona-based agents. Now with A2A/MCP interop it's no longer isolated.

### AutoGen (Microsoft) ⚠️ Legacy

**Core idea**: Agents communicate through structured multi-turn conversations.

- **56.8K GitHub stars** — largest historical community
- **⚠️ Now in maintenance mode**: Development shifted to [[microsoft-agent-framework]]
- **Magentic-One**: Generalist agent team still available via CLI: `m1 "task"`
- **Best for**: Existing codebases not yet migrated. Plan migration during 2026.

### OpenAI Swarm ⚠️ Legacy

**Core idea**: Agents are system prompts with functions. Handoffs are functions that return another agent.

- **⚠️ Superseded by [[openai-agents-sdk]]**: Swarm remains educational only
- **Two primitives**: Routines + Handoffs — still the best way to learn multi-agent patterns
- **Best for**: Learning. Build it yourself in 50 lines to understand the primitives.

---

## Decision Matrix

| Factor | Agents SDK | Google ADK | MAF 1.0 | LangGraph | CrewAI |
|--------|-----------|-----------|---------|-----------|--------|
| Production readiness | ★★★ | ★★★ | ★★★ | ★★★ | ★★ |
| Ease of getting started | ★★★ | ★★ | ★★ | ★★ | ★★★ |
| Explicit control | ★★ (handoffs) | ★★★ (workflow agents) | ★★★ (graph edges) | ★★★ (graph edges) | ★★ (process) |
| State persistence | ★★ (session) | ★★★ (state + memory) | ★★★ (agent state) | ★★★ (checkpointed) | ★★ (three types) |
| Human-in-the-loop | ★★ (approvals) | ★★★ (PolicyEngine) | ★★ (graph nodes) | ★★★ (any node) | ★★ (delegation) |
| Model support | ★ (OpenAI only) | ★★★ (10+ providers) | ★★★ (6 providers) | ★★★ (any via LangChain) | ★★★ (any) |
| Language support | ★ (Python) | ★★★ (Py/TS/Go/Java) | ★★ (.NET/Python) | ★★ (Python/TS) | ★ (Python) |
| Interop (MCP/A2A) | ★★ (MCP only) | ★★★ (MCP + A2A) | ★★★ (MCP + A2A) | ★★ (MCP) | ★★ (MCP + A2A) |
| Debugging | ★★ (tracing) | ★★ (Dev UI) | ★★★ (DevUI) | ★★★ (LangSmith) | ★★ |
| Enterprise/LTS | ★ | ★★ | ★★★ (LTS) | ★★ | ★★ (Enterprise) |

---

## When to Use What

```
Learning multi-agent patterns?        → Swarm (simplest mental model, educational)
OpenAI-only, fast to production?      → OpenAI Agents SDK (handoffs + guardrails)
Multi-language team?                  → Google ADK (Python/TS/Go/Java)
Model-agnostic, interop needed?       → Google ADK (A2A + MCP native)
Enterprise, Azure/.NET?               → Microsoft Agent Framework 1.0 (LTS)
Production stateful workflows?        → LangGraph (checkpointing, human-in-loop)
Quick multi-perspective prototype?    → CrewAI (role + backstory, intuitive)
Need human approval gates?            → LangGraph or ADK (PolicyEngine)
20-30 parallel coding agents?         → Gas Town (process-model, merge queue)
Issue-tracker automation?             → Symphony (Linear → Codex, WORKFLOW.md)
Agents as teammates on a board?       → Multica (11 runtimes, compounding skills)
Company-level governance?             → Paperclip (org charts, budgets)
```

### Progression Path

1. **Learn**: Build a Swarm-style handoff system to understand the primitives
2. **Prototype**: CrewAI for quick multi-agent prototypes (intuitive team metaphor)
3. **Ship (simple)**: OpenAI Agents SDK if you're OpenAI-only and want minimal ceremony
4. **Ship (complex)**: LangGraph or MAF when you need checkpointing, graphs, or human-in-the-loop
5. **Scale (multi-language)**: Google ADK when your team spans Python/Go/Java/.NET
6. **Scale (parallel)**: Gas Town for 20-30 parallel agents with merge queue
7. **Automate**: Symphony to turn issue tracker work into autonomous agent runs
8. **Collaborate**: Multica when your team (humans + agents) needs shared visibility
9. **Govern**: Paperclip for company-level orchestration with budgets and accountability

---

## The Graph Convergence (Confirmed)

The most significant finding across all sources: **graph-based workflows are the consensus architecture for production multi-agent systems.** What was a thesis in April is now confirmed:

| Framework | Graph Status |
|-----------|-------------|
| [[langgraph-agent-orchestration]] | Built on graphs from day one (v1.0 shipped) |
| [[microsoft-agent-framework]] | Graph workflows as core architecture (1.0 GA) |
| [[google-adk]] | ADK 2.0 beta adding graph-based workflows |
| [[autogen-multi-agent]] | Abandoned GroupChat for graph-based MAF |
| [[scion]] | Directed workflows for agent coordination |
| [[kiro]] | Structured task graphs internally |

Why graphs win:
- **Explicit**: You define the flow, not the conversation
- **Debuggable**: Visualize the graph, trace execution path
- **Checkpointable**: Pause/resume at any node
- **Composable**: Subgraphs as reusable components
- **Enforceable**: Security invariants at the graph level

**Exception**: Gas Town's process-model proves graphs aren't the only path to scale. External state coordination (Dolt/Git) enables 20-30 agents without graph overhead.

---

## The Protocol Layer (New in 2026)

A major development since April: the interoperability story is crystallizing around three protocols:

| Protocol | Layer | Purpose | Adopted By |
|----------|-------|---------|-----------|
| **MCP** (Model Context Protocol) | Tools | Connect agents to external tools/data | All frameworks |
| **A2A** (Agent-to-Agent) | Agents | Cross-framework agent communication | ADK, MAF, CrewAI |
| **AG-UI** (Agent-User Interaction) | Frontend | Agent-to-user interaction in UIs | CopilotKit, LlamaIndex |

**Key insight**: MCP won for tools. A2A is emerging for agent interop. These are complementary layers, not competitors. The "Will MCP become the standard?" question from April is partially answered: MCP is the tool layer; A2A is the agent layer.

Frameworks with native A2A support can coordinate agents across different runtimes — a Google ADK agent can collaborate with a Microsoft Agent Framework agent via structured protocol messaging.

---

## How Product-Level Tools Relate

| Tool | What It Provides | Framework Complement |
|------|-----------------|---------------------|
| [[claude-code]] | The agent itself (LLM + tools + skills) | LangGraph/ADK orchestrate multiple instances |
| [[kiro]] | Autonomous frontier agent | Could be a node in a LangGraph/MAF workflow |
| [[scion]] | Container isolation + lifecycle | Provides the runtime for any framework's agents |
| [[gastown]] | Workspace orchestration + merge queue | Coordinates Claude Code/Codex/Copilot (20-30 agents) |
| [[symphony]] | Issue-to-agent automation | Reads Linear, spawns Codex sessions per issue |
| [[multica]] | Team collaboration platform | Assigns issues to agents, compounds skills (11 runtimes) |
| [[paperclip]] | Company-level governance | Sits above frameworks, manages goals and budgets |

The emerging stack:

```
Paperclip (company goals/governance)
    → Multica (team collaboration + skill compounding)
        → Gas Town (workspace orchestration + merge queue)
            → LangGraph / MAF / ADK (workflow graphs)
                → Claude Code / Kiro / Codex (individual agents)
                    → Scion (infrastructure isolation)
```

---

## The Architectural Split

| Architecture | Control Plane | Scale | Tools |
|---|---|---|---|
| **Handoff-based** | Function returns | 2-5 agents | Agents SDK, Swarm |
| **Conversation-as-control** | LLM routes via messages | 3-5 agents | AutoGen, CrewAI |
| **Workflow-agent** | Deterministic Sequential/Parallel/Loop | 5-15 agents | Google ADK |
| **Graph-as-control** | Explicit edges + conditions | 5-15 agents | LangGraph, MAF |
| **Process-model** | Deterministic routing via external state | 20-30 agents | Gas Town |
| **Issue-tracker-driven** | Tracker polls + workspace isolation | Bounded (default 10) | Symphony |
| **Platform-driven** | Web UI + daemon dispatch | Runtime-bound | Multica |

---

## Coordination Patterns Across All Fourteen Approaches

| Pattern | Who Uses It | How |
|---------|------------|-----|
| **Git-based coordination** | Scion, Kiro, Claude Code, Gas Town, Symphony | Worktrees/branches per agent, PRs as output |
| **Graph-based** | LangGraph, MAF, ADK 2.0, Scion | Explicit nodes + edges + conditions |
| **Workflow agents** | Google ADK | Sequential/Parallel/Loop deterministic control |
| **Conversation-based** | AutoGen, Claude Code (subagents) | Agents negotiate through dialogue |
| **Role-based delegation** | CrewAI, Paperclip, Gas Town | Specialized agents with defined responsibilities |
| **Function handoffs** | Agents SDK, Swarm, Claude Code (tool use) | Functions transfer control between agents |
| **Process-model (GUPP)** | Gas Town | Pull-based: work on hook → agent executes |
| **Issue-tracker polling** | Symphony, Multica | Daemon reads issues, dispatches agents per task |
| **Container isolation** | Scion | Each agent in its own container |
| **Permission modes** | Claude Code | Configurable dial from full control to full autonomy |
| **A2A protocol** | ADK, MAF, CrewAI | Cross-framework agent communication |
| **Compounding skills** | Multica | Solutions become reusable team capabilities |

---

## The Multi-Agent Memory Problem

Multi-agent systems multiply the [[agent-memory-persistence]] challenge:

- **Shared memory**: How do agents share what they've learned? CrewAI has built-in cross-agent memory. LangGraph uses checkpointed state. ADK has session state + memory service. Agents SDK has session-based state.
- **Conflicting memories**: When Agent A and Agent B learn contradictory facts, who wins? No framework has a standard resolution mechanism.
- **Cascading permissions**: When Agent A delegates to Agent B, does B inherit A's full memory access? ([[agentic-ai-governance]] flags this as a key risk)
- **Cost multiplication**: Each agent consumes tokens independently. Poor memory management across N agents means N× the waste ([[agent-cost-economics]]).

---

## Production Challenges (Common Across All)

1. **Non-determinism**: Same input → different agent dialogues → different outcomes. Testing is hard.
2. **Debugging complexity**: Tracing failures across multiple agents. MAF's DevUI and LangGraph's LangSmith help most here.
3. **Context switching overhead**: Maintaining coherence as control passes between agents.
4. **Cost scaling**: More agents = more tokens. Model routing becomes critical.
5. **Emergent behavior**: Individual agents within guardrails can produce unanticipated combined outcomes.
6. **Interop friction**: Despite A2A/MCP, cross-framework coordination is still early.

---

## Recommendations

1. **If you're new to multi-agent**: Start with Swarm's handoff pattern. Build it yourself in 50 lines. Understand the primitives before adopting a framework.

2. **If you need a quick prototype**: CrewAI. Define roles, backstories, tasks. Sequential process. Working multi-agent system in an afternoon.

3. **If you're OpenAI-only and want production**: OpenAI Agents SDK. Handoffs + guardrails + tracing with minimal ceremony.

4. **If you need multi-language support**: Google ADK. Python/TypeScript/Go/Java with the same concepts across all four.

5. **If you need cross-framework interop**: Google ADK or Microsoft Agent Framework. Both have native A2A + MCP.

6. **If you're going to production with complex workflows**: LangGraph. Checkpointing, human-in-the-loop, explicit graph control, and proven enterprise adoption (Klarna, Replit, Uber).

7. **If you're on Azure/.NET**: Microsoft Agent Framework 1.0. LTS commitment, DevUI, six providers, graph workflows. The canonical choice through 2027.

8. **If you need company-level orchestration**: [[paperclip]] above whatever framework you choose.

9. **If you need 20-30 parallel agents**: [[gastown]]. Process-model with crash-surviving state and merge queue.

10. **If you want issue-tracker-driven automation**: [[symphony]]. Minimal infrastructure, WORKFLOW.md as policy-as-code.

11. **If you want agents as teammates**: [[multica]]. Cloud-first platform with compounding skills and 11 runtime support.

12. **For everyone**: Plan for the graph convergence. Even if you start with CrewAI or Agents SDK, your production system will likely end up as a graph. But note: Gas Town's process-model proves graphs aren't the only path to scale.

---

## Open Questions

- Will A2A achieve the same ubiquity as MCP, or will it fragment?
- Can CrewAI's intuitive role metaphor be preserved within a graph-based architecture?
- How should multi-agent memory be shared without cascading errors?
- What's the right granularity for task decomposition across agents?
- Will the product-level tools (Claude Code, Kiro) eventually embed framework-level orchestration natively?
- Will Google ADK's four-language approach force other frameworks to expand language support?
- How will the LTS commitment from Microsoft affect framework choice in regulated industries?
- Will cross-model adversarial review (Metaswarm pattern) become standard for trust?
- Can Multica's compounding skills scale to large teams?
- Will AG-UI become the standard for agent-to-frontend communication?

---

*Analysis based on 14 sources ingested into this wiki between 2026-04-07 and 2026-05-11. Updated May 2026 with OpenAI Agents SDK, Google ADK, Microsoft Agent Framework 1.0, and the A2A/MCP protocol landscape. See [[orchestration-tools-compared]] for the Gas Town/Symphony/Multica head-to-head.*

## See Also
- [[multi-agent-orchestration]]
- [[orchestration-tools-compared]]
- [[openai-agents-sdk]]
- [[google-adk]]
- [[microsoft-agent-framework]]
- [[gastown]]
- [[symphony]]
- [[multica]]
- [[agent-memory-persistence]]
- [[memory-architecture-comparison]]
- [[agent-cost-economics]]
- [[agentic-ai-governance]]
- [[mcp-protocol]]
