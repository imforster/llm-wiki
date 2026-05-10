---
type: analysis
created: 2026-04-08
updated: 2026-05-09
sources: ["[[scion-docs]]", "[[kiro-autonomous-agent]]", "[[claude-code-docs]]", "[[anthropic-skills-repo]]", "[[ten-pillars-agentic-skill-design]]", "[[llm-wiki-karpathy]]", "[[fabric-github]]", "[[personal-ai-infrastructure]]", "[[evaluating-agent-skills-caparas]]", "[[ai-technique-podcast]]", "[[skills-pipeline-sleestk]]", "[[anthropic-eval-guide]]", "[[promptfoo]]", "[[paperclip]]", "[[spec-kit]]", "[[bmad-method]]", "[[notebooklm-notes-guide]]", "[[mem0-memory-management]]", "[[continuum-memory-architectures]]", "[[agent-memory-systems-2026]]", "[[efficient-memory-architectures]]", "[[humaneval-benchmark]]", "[[swe-bench]]", "[[gaia-benchmark]]", "[[agentbench]]", "[[autogen-multi-agent]]", "[[crewai-multi-agent]]", "[[langgraph-agent-orchestration]]", "[[openai-swarm]]", "[[agent-cost-economics]]", "[[agentic-ai-governance]]", "[[agentic-ai-non-code-domains]]", "[[agentic-ux-patterns]]", "[[gastown]]", "[[symphony]]", "[[multica]]"]
tags: [synthesis, landscape, insights, agentic-ai]
---

# Key Insights: The Agentic AI Landscape (May 2026)

Synthesized from 42 sources across this wiki. This analysis captures the patterns, tensions, and emerging consensus visible when you look across the entire landscape.

> **Refresh history**: Originally written against 16 sources (Apr 8-10). Refreshed Apr 15 against 33 sources. Refreshed May 9 against 42 sources — added Gas Town, Symphony, Multica; updated layers, multi-agent philosophies, and "What's Still Missing."

---

## 1. Seven Layers Have Emerged (was Six)

| Layer | Representatives | Core Bet |
|-------|----------------|----------|
| **Company** | [[paperclip]] | Org charts, budgets, governance, goal alignment |
| **Methodology** | [[spec-kit]], [[bmad-method]] | Specs, plans, tasks, quality gates |
| **Orchestration** | [[gastown]], [[symphony]], [[multica]] | Workspace coordination, issue-to-agent automation, team collaboration |
| **Infrastructure** | [[scion]], [[langgraph-agent-orchestration]], [[autogen-multi-agent]] | Containers, runtimes, graph orchestration |
| **Tool** | [[claude-code]], [[kiro]], [[crewai-multi-agent]] | Agentic loop, skills, hooks, MCP |
| **Pattern** | [[fabric]], [[agent-skills-standard]], [[openai-swarm]] | Curated prompts, composable strategies, handoffs |
| **Memory** | [[mem0]], [[agent-memory-persistence]] | Persistence, retrieval, forgetting, knowledge graphs |

**New (May 2026)**: Orchestration is now its own layer between Methodology and Infrastructure. Gas Town (workspace/process-model), Symphony (spec/scheduler), and Multica (platform/teammates) represent three distinct approaches at this layer. The emerging stack: Paperclip → Multica → Gas Town → LangGraph/MAF → Claude Code/Kiro → Scion → Mem0.

## 2. The Autonomy–Interaction Spectrum Is Formalized

No longer just a spectrum — now has measurable UX patterns ([[agentic-ux-patterns]]):

```
← More Human Control                              More Agent Autonomy →

Observe &     Plan &       Act with        Act
Suggest       Propose      Confirmation    Autonomously
(Scion)       (CrewAI)     (Claude Code)   (Kiro, PAI)
```

The Autonomy Dial provides four levels with metrics: >85% acceptance rate, <5% reversion rate, >90% escalation recovery. Phased adoption: safety first → calibrated autonomy → proactive delegation.

## 3. Two Open Standards + Graph Convergence

| Standard | What It Does | Adoption |
|----------|-------------|----------|
| [[mcp-protocol]] | Connects agents to external tools/data | Claude Code, Kiro, Fabric |
| [[agent-skills-standard]] | Packages reusable agent capabilities | Claude Code, agentskills.io |

**New**: Graph-based workflows are converging as the third standard — not a formal spec, but a consensus architecture. Both AutoGen (MAF) and LangGraph use typed nodes + edges. The conversation-based approach (GroupChat) is being abandoned by its own creators.

## 4. Progressive Disclosure Is Quantified

The consensus solution to context management now has benchmarks:

| Approach | Tokens | Accuracy | Source |
|----------|--------|----------|--------|
| Full-context (send everything) | ~26,000 | 72.9% | [[mem0-memory-management]] |
| Selective retrieval (Mem0) | ~1,800 | 66.9% | [[mem0-memory-management]] |
| Graph-enhanced (Mem0g) | ~1,800 | 68.4% | [[mem0-memory-management]] |
| MemGPT paging | ~1,000 | — | [[efficient-memory-architectures]] |

93% fewer tokens for ~5% accuracy tradeoff. For any interactive agent, selective retrieval is the production-viable path.

## 5. Memory Is Understood (Was "Unsolved Frontier")

Four architecture patterns documented ([[memory-architecture-comparison]]):
- **Vector-Only**: fast, no relationships (1/6 CMA compliance)
- **Graph+Vector** ([[mem0]]): relationships + semantic search (4/6 CMA)
- **File+Database** ([[llm-wiki-pattern]]): human-readable, git-friendly (2/6 CMA)
- **Hierarchical** (MemGPT, [[pai]]): mimics human cognition (5/6 CMA)

Six formal CMA requirements defined ([[continuum-memory-architectures]]). Standard RAG meets none. Forgetting is a design requirement, not a failure. Progression: start vector-only → add graph → add hierarchy → add forgetting.

## 6. Git Remains the Universal Coordination Mechanism

Unchanged. Every tool uses git. No one is building a custom protocol. But git only works for text-shaped artifacts.

## 7. The Skill Hierarchy Is Crystallizing

Unchanged. Fabric Patterns → Agent Skills Standard → Claude Code Skills → PAI Skills. PAI's insight: CODE → CLI → PROMPT → SKILL (code before prompts).

## 8. Security Models Now Have a Governance Layer

**Expanded** from tool-level security to organizational governance ([[agentic-ai-governance]]):

| Layer | Approach | Source |
|-------|----------|--------|
| Infrastructure | Container isolation | [[scion]] |
| Agent | Permission modes + classifier | [[claude-code]] |
| Output | Sandbox + PR-only | [[kiro]] |
| Policy | Hooks + allowlists | [[pai]] |
| **Organization** | Five pillars: inventory, identity, least privilege, observability, compliance | [[agentic-ai-governance]] |
| **User-facing** | Six UX patterns: intent preview, autonomy dial, rationale, confidence, audit, escalation | [[agentic-ux-patterns]] |

Shadow AI: 68% of employees use AI without IT approval. $412K/yr average cost. Regulatory landscape crystallizing (NIST, EU AI Act, OWASP, Singapore).

## 9. The "Personal AI" Vision Extends to Every Industry

**Expanded** from coding to six industries ([[agentic-ai-non-code-domains]]):

| Industry | Impact | Key Tension |
|----------|--------|-------------|
| Financial Services | 40-60% compliance time reduction | Regulatory compliance |
| Healthcare | Enormous potential | Hallucination = life-threatening |
| Professional Services | Existential SaaS disruption | Hourly-billing model at risk |
| Manufacturing | Adaptive vs rigid automation | Physical-digital convergence |
| Telecoms | 8-15% cost reductions | Underutilized data |
| Transportation | 12-20% delivery improvements | Clear quantifiable ROI |

The wiki's themes generalize across all industries. Stakes are higher outside code. Domain expertise is the moat.

## 10. Evaluation Has Benchmarks Now (Was "Weakest Link")

**Upgraded** with four standardized benchmarks ([[agent-benchmarks]]):

| Benchmark | What It Tests | Top Score | Human Baseline |
|-----------|--------------|-----------|---------------|
| [[humaneval-benchmark]] | Code generation | 96.3% | — |
| [[swe-bench]] | Real-world SE | 74.4% | — |
| [[gaia-benchmark]] | General AI assistant | <50% | 92% |
| [[agentbench]] | Interactive agents (8 envs) | Commercial >> OSS | — |

Progression: code gen (solved) → real-world SE (improving fast) → general reasoning (far from human) → interactive agents (commercial leads). Still missing: skill-level eval, multi-agent quality, memory quality benchmarks.

## 11. Token Economics Are an Architectural Concern (NEW)

60-80% of agent tokens are waste ([[agent-cost-economics]]). Five waste vectors: file reading loops, retry tax, over-qualified models, no caching, context contamination.

$5T infrastructure bet with base case 3.2% ROI. Per-token costs falling 85% but total cost flat/increasing due to volume. Reasoning models use 8× more tokens. The industry's viability depends on enterprise adoption at $450-500/mo ARPU.

Optimization is architecture: model routing (5-8× savings), prompt caching (90% discount), session discipline, selective retrieval (93% reduction). See [[cost-optimization-guide]].

## 12. Multi-Agent Has Seven Philosophies Now (was Four) (NEW → EXPANDED)

**Frameworks** (composable, bring-your-own-model):

| Framework | Philosophy | Best For |
|-----------|-----------|----------|
| [[autogen-multi-agent]] | Conversation | Research, prototyping |
| [[crewai-multi-agent]] | Role-based teams | Complex research |
| [[langgraph-agent-orchestration]] | State machine graphs | Production workflows |
| [[openai-swarm]] | Minimal handoffs | Simple routing, learning |

**Orchestration tools** (workspace/platform-level):

| Tool | Philosophy | Best For |
|------|-----------|----------|
| [[gastown]] | Process-model (GUPP) | 20-30 parallel agents, crash-surviving state |
| [[symphony]] | Spec/protocol (WORKFLOW.md) | Issue-tracker-driven automation, minimal infra |
| [[multica]] | Platform (agents as teammates) | Team collaboration, compounding skills |

**Key architectural split**: Conversation-as-control (3-5 agents) vs process-model (20-30 agents). Gas Town is the only tool using deterministic routing via external state rather than LLM conversation for coordination. See [[orchestration-tools-compared]] and [[multi-agent-framework-guide]].

## 13. Governance Requires Five Pillars (NEW)

From [[agentic-ai-governance]]: Agent Inventory → Agent Identity (NHI) → Dynamic Least Privilege → Continuous Observability → Continuous Compliance. Legacy security fails because agents violate every assumption (identity, permissions, behavior, speed, audit trail). Kill switches are non-negotiable. See [[governance-safety-overview]].

## 14. What's Still Missing

Gaps visible across 42 sources:
- **Skill-level evaluation**: benchmarks test whole models, not individual skills
- **Multi-agent coordination quality**: no benchmark for how well agents work together
- **Memory quality benchmarks**: LOCOMO is closest, but no standard for long-term memory accuracy
- **Conflict resolution**: when agents or memories contradict, no standard mechanism
- **Cross-framework interoperability**: MCP connects tools, but no standard for agent-to-agent handoff across frameworks
- **Environmental impact**: $5T infrastructure has energy implications (partially addressed by [[ai-environmental-impact]])
- **Harness engineering practices**: Symphony/OpenAI coined the term but no comprehensive guide exists
- **Cross-model adversarial review**: Metaswarm pattern (writer ≠ reviewer) is promising but not yet in wiki as a source
- **Content pipeline**: turning wiki/agent knowledge into publishable content (the user's stated goal)

---

*Analysis based on 42 sources ingested between 2026-04-07 and 2026-05-09. Refreshed 2026-05-09.*

## See Also
- [[cross-source-themes]]
- [[orchestration-tools-compared]]
- [[multi-agent-framework-guide]]
- [[memory-architecture-comparison]]
- [[cost-optimization-guide]]
- [[governance-safety-overview]]
- [[beyond-code-industry-impact]]
- [[agent-benchmarks]]
