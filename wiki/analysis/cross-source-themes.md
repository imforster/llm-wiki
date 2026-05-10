---
type: analysis
created: 2026-04-09
updated: 2026-05-09
sources: ["[[scion-docs]]", "[[kiro-autonomous-agent]]", "[[claude-code-docs]]", "[[anthropic-skills-repo]]", "[[ten-pillars-agentic-skill-design]]", "[[llm-wiki-karpathy]]", "[[fabric-github]]", "[[personal-ai-infrastructure]]", "[[evaluating-agent-skills-caparas]]", "[[ai-technique-podcast]]", "[[skills-pipeline-sleestk]]", "[[anthropic-eval-guide]]", "[[promptfoo]]", "[[paperclip]]", "[[spec-kit]]", "[[bmad-method]]", "[[notebooklm-notes-guide]]", "[[mem0-memory-management]]", "[[continuum-memory-architectures]]", "[[agent-memory-systems-2026]]", "[[efficient-memory-architectures]]", "[[humaneval-benchmark]]", "[[swe-bench]]", "[[gaia-benchmark]]", "[[agentbench]]", "[[autogen-multi-agent]]", "[[crewai-multi-agent]]", "[[langgraph-agent-orchestration]]", "[[openai-swarm]]", "[[agent-cost-economics]]", "[[agentic-ai-governance]]", "[[agentic-ai-non-code-domains]]", "[[agentic-ux-patterns]]", "[[gastown]]", "[[symphony]]", "[[multica]]"]
tags: [analysis, themes, cross-source, synthesis]
---

# Cross-Source Theme Analysis

42 sources, 12 tools, 4 OSS frameworks, 4 benchmarks, 2 standards, 3 methodologies, 4 memory systems, and sources covering cost, governance, UX, and industry impact. Here are the themes that appear across 3+ sources independently.

> **Refresh history**: Originally written against 11 sources (Apr 9). Refreshed Apr 15 against 33 sources. Refreshed May 9 against 42 sources — added Gas Town, Symphony, Multica evidence to existing themes.

---

## Theme 1: Context Is King (15/33 sources) ⭐⭐⭐⭐⭐

The single most repeated idea. Now backed by quantitative evidence from memory research.

| Source | How it appears |
|--------|---------------|
| [[agent-skills-standard]] | Progressive disclosure: ~100 tokens at startup, full content only when activated |
| [[claude-code]] | MCP tools deferred, skills load on demand, subagent context isolation, CLAUDE.md under 200 lines |
| [[ten-pillars-agentic-skill-design]] | Pillar 9: four context management recipes |
| [[pai]] | TELOS (10 files), three-tier memory, "context document" as core primitive |
| [[fabric]] | Per-pattern model mapping, composable strategies |
| [[ai-technique-podcast]] | "Context beats clever prompting." |
| [[skills-pipeline-sleestk]] | Reference files loaded on demand, minimal structured context forward |
| [[llm-wiki-pattern]] | Index-first navigation — read catalog, drill into relevant pages only |
| [[scion]] | Each agent gets own container with own context. No shared pollution. |
| [[mem0-memory-management]] | Four memory layers. 93% token reduction with selective retrieval vs full-context. |
| [[continuum-memory-architectures]] | Six formal requirements for context persistence. CMA won 82/92 vs RAG. |
| [[efficient-memory-architectures]] | Four failure modes of flat vector storage. MemGPT: 90% token savings. |
| [[agent-cost-economics]] | Five waste vectors — 60-80% of tokens wasted on wrong context. |
| [[crewai-multi-agent]] | Role + backstory as persona-based context management |
| [[langgraph-agent-orchestration]] | Checkpointed state as persistent context across workflow steps |

**Strengthened consensus**: Not just "load the right thing" but now quantified: selective retrieval = 93% fewer tokens for ~5% accuracy tradeoff ([[mem0-memory-management]]). Context management is simultaneously a quality strategy AND a cost strategy ([[agent-cost-economics]]).

---

## Theme 2: Composition Over Monoliths (17/42 sources) ⭐⭐⭐⭐⭐

Validated across every framework — product-level and open-source alike.

| Source | How it appears |
|--------|---------------|
| [[fabric]] | 251 focused patterns. Unix philosophy: pipe and compose. |
| [[skills-pipeline-sleestk]] | 6-stage YouTube pipeline. Each skill is one domain. |
| [[claude-code]] | Subagents (Explore, Plan, General-purpose). Skills per task. |
| [[scion]] | Harness per tool. Template per agent. Grove per project. |
| [[agent-skills-standard]] | One skill per directory. Under 500 lines. |
| [[ten-pillars-agentic-skill-design]] | Pillar 3 (SRP), Pillar 4 (modularity). |
| [[pai]] | 63 skills, 21 hooks, 14 agents, 12 standalone packs. |
| [[kiro]] | Powers as modular packages. Sub-agents for coordination. |
| [[autogen-multi-agent]] | Specialized agents communicate through dialogue |
| [[crewai-multi-agent]] | Crew of role-specialized agents with task dependencies |
| [[langgraph-agent-orchestration]] | Nodes as composable units in a graph |
| [[openai-swarm]] | Agents as system prompts + functions. Minimal units. |
| [[paperclip]] | Agents organized into companies with specialized roles |
| [[spec-kit]] | 30+ agents, 50+ extensions, each with focused scope |
| [[gastown]] | Seven specialized roles (Mayor, Polecats, Refinery, Witness, Deacon, Dogs). Molecules as composable workflow units. |
| [[symphony]] | WORKFLOW.md per repo. Each issue gets isolated workspace + agent session. Separation of scheduler from agent. |
| [[multica]] | Reusable skills that compound. Each agent is a focused teammate with a specific runtime. |

**Strongest convergence in the wiki.** Every single multi-agent framework chose small, focused, composable units. No exceptions.

---

## Theme 3: The Human Stays in the Loop — But How Much? (13/33 sources) ⭐⭐⭐⭐⭐

Now formalized with measurable UX patterns and a phased adoption framework.

| Source | Position |
|--------|----------|
| [[scion]] | "Interaction is imperative." |
| [[kiro]] | Frontier agents: hours/days of autonomy. PR-only output. |
| [[claude-code]] | 6 permission modes — configurable dial. |
| [[pai]] | Self-modifying, but human sets goals (TELOS). |
| [[evaluating-agent-skills-caparas]] | Human review is Tier 3 — expensive, use sparingly. |
| [[ai-technique-podcast]] | "AI as thinking partner, not executor only." |
| [[llm-wiki-pattern]] | Human curates sources. LLM does everything else. |
| [[agentic-ux-patterns]] | **Six UX patterns** with metrics: Intent Preview (>85% acceptance), Autonomy Dial (4 levels), Confidence Signal, Audit & Undo (<5% reversion), Escalation (>90% recovery). |
| [[agentic-ai-governance]] | Kill switches, dynamic least privilege, continuous observability. |
| [[autogen-multi-agent]] | Configurable human participation in agent conversations. |
| [[crewai-multi-agent]] | Delegation: agents can ask humans or other agents for help. |
| [[langgraph-agent-orchestration]] | Human-in-the-loop at any node (first-class). |
| [[agentic-ai-non-code-domains]] | Healthcare demands human oversight; finance requires compliance gates. |

**New**: The [[agentic-ux-patterns]] source formalizes this spectrum into six measurable patterns. The Autonomy Dial (Observe → Propose → Confirm → Autonomous) maps directly to Claude Code's permission modes. Phased adoption: safety first → calibrated autonomy → proactive delegation.

---

## Theme 4: Skills Are Evolving Into a Standard (6/33 sources) ⭐⭐⭐⭐

Unchanged from original analysis. The evolution trajectory remains clear.

Fabric Patterns (2023) → Agent Skills Standard (2025) → Claude Code Skills (2026) → Pipelines + Evaluation. From simple prompt files to a full lifecycle.

---

## Theme 5: Memory Is No Longer the Unsolved Frontier (10/33 sources) ⭐⭐⭐⭐⭐

**Upgraded from "unsolved" to "understood with clear tradeoffs."** Four new memory sources provide formal requirements, benchmarks, and architecture patterns.

| Source | Memory approach |
|--------|---------------|
| [[pai]] | Three-tier hot/warm/cold. Self-modification. Most sophisticated product. |
| [[claude-code]] | CLAUDE.md + auto memory. Per working tree. |
| [[kiro]] | Persistent context. Learns from code reviews. |
| [[llm-wiki-pattern]] | The wiki IS the memory. File + Database pattern. |
| [[scion]] | No memory. Each agent starts fresh. |
| [[mem0-memory-management]] | Graph+vector, four layers, five scopes. LOCOMO benchmarks. |
| [[continuum-memory-architectures]] | Six formal CMA requirements. 82/92 wins vs RAG. |
| [[agent-memory-systems-2026]] | Four patterns: vector-only, graph+vector, file+DB, hierarchical. |
| [[efficient-memory-architectures]] | H-MEM, MemGPT (90% savings), GraphRAG, selective forgetting. |
| [[crewai-multi-agent]] | Built-in short/long/entity memory across agents. |

**Key advances**: CMA defines six necessary conditions (RAG meets none). Mem0 provides production benchmarks (93% token reduction). Forgetting is now recognized as a design requirement, not a failure. See [[memory-architecture-comparison]] for the full analysis.

---

## Theme 6: Git as Universal Substrate (9/42 sources) ⭐⭐⭐⭐⭐

**Upgraded from ⭐⭐⭐⭐ to ⭐⭐⭐⭐⭐.** Gas Town and Symphony provide the strongest evidence yet that git is the coordination primitive for multi-agent systems.

| Source | How it appears |
|--------|---------------|
| [[scion]] | Git worktrees per agent |
| [[kiro]] | Git branches, PR output |
| [[claude-code]] | Git-based workspaces |
| [[gastown]] | Git worktrees for every polecat. Dolt (git-for-data) for beads. Merge queue (Refinery). Wasteland federation via DoltHub. **Most git-native tool in the wiki.** |
| [[symphony]] | Per-issue workspace directories. Workspaces persist across runs. WORKFLOW.md version-controlled with the codebase. |
| [[multica]] | Git-based workspace isolation per agent task |
| [[paperclip]] | Agent-agnostic but assumes git-based code output |
| [[spec-kit]] | Spec-driven development with git-versioned artifacts |
| [[llm-wiki-pattern]] | The wiki itself is git-backed |

**Key advance (May 2026)**: Gas Town takes git further than any other tool — worktrees for isolation, Dolt for cell-level merge of concurrent agent writes, and a Bors-style merge queue for quality gates. Symphony uses git implicitly (workspaces are filesystem directories that can be git repos via hooks). The pattern is universal.

---

## Theme 7: Evaluation Has a Framework Now (8/33 sources) ⭐⭐⭐⭐

**Upgraded from "weakest link" to "framework exists, adoption lags."**

| Source | Contribution |
|--------|-------------|
| [[evaluating-agent-skills-caparas]] | Three-tier framework (deterministic → LLM-judge → human) |
| [[ten-pillars-agentic-skill-design]] | Pillar 7. Acknowledged "no controlled study." |
| [[anthropic-eval-guide]] | Success criteria, eval types, design principles |
| [[promptfoo]] | Open-source eval CLI, YAML test cases, CI/CD |
| [[humaneval-benchmark]] | Code generation: 164 problems, pass@k, 0% → 96.3% |
| [[swe-bench]] | Real-world SE: 2,294 GitHub issues, top 74.4% resolved |
| [[gaia-benchmark]] | General AI: 466 questions, humans 92% vs AI <50% |
| [[agentbench]] | Agent decision-making: 8 environments, multi-turn |

**Key advance**: The benchmark landscape now covers code generation (solved at 96%), real-world SE (rapidly improving at 74%), general reasoning (far from human at <50%), and interactive agents (commercial >> open-source). See [[agent-benchmarks]] for the full comparison. Still missing: skill-level eval, multi-agent coordination quality, memory quality benchmarks.

---

## Theme 8: Open Standards Are Winning (5/33 sources) ⭐⭐⭐

Unchanged. MCP + Agent Skills as two-layer open substrate.

---

## NEW Theme 9: Graphs Are Becoming the Consensus Orchestration Architecture (4/33 sources) ⭐⭐⭐

| Source | Evidence |
|--------|---------|
| [[langgraph-agent-orchestration]] | Built on graphs from day one. Most production-ready OSS. |
| [[autogen-multi-agent]] | Transitioning from GroupChat to graph-based MAF. |
| [[scion]] | Directed workflows for agent coordination. |
| [[kiro]] | Sub-agents coordinated through structured task graphs. |

Both AutoGen (via MAF) and LangGraph converging on typed nodes + edges. The conversation-based approach (AutoGen v0.2 GroupChat) is being abandoned by its own creators. See [[multi-agent-framework-guide]].

**May 2026 nuance**: [[gastown]] proves graphs aren't the only path to production scale. Gas Town's process-model (deterministic routing via external state, GUPP pull-based execution) scales to 20-30 agents without graphs. The graph convergence applies to *framework-level* orchestration; workspace-level orchestration may use different primitives entirely.

---

## NEW Theme 10: Token Economics Drive Architecture (5/33 sources) ⭐⭐⭐

| Source | Evidence |
|--------|---------|
| [[agent-cost-economics]] | 60-80% of tokens wasted. Five waste vectors. $5T infrastructure bet. |
| [[mem0-memory-management]] | 93% token reduction with selective retrieval. |
| [[efficient-memory-architectures]] | MemGPT: 90% token savings via OS-style paging. |
| [[context-management]] | Progressive disclosure, scoped instructions, deferred tools. |
| [[agent-memory-systems-2026]] | Cost comparison across four memory patterns. |

Cost optimization is not a billing concern — it's an architectural concern. Every memory, context, and orchestration decision has a direct token cost implication. See [[cost-optimization-guide]].

---

## NEW Theme 11: Governance Is the Next Frontier (4/33 sources) ⭐⭐⭐

| Source | Evidence |
|--------|---------|
| [[agentic-ai-governance]] | Five pillars. Shadow AI ($412K/yr). NIST AI Agent Standards Initiative. |
| [[agentic-ux-patterns]] | Six UX patterns as user-facing governance layer. |
| [[agentic-ai-non-code-domains]] | Regulated industries (healthcare, finance) demand governance for deployment. |
| [[agent-cost-economics]] | 68% of employees use AI without IT approval. |

Legacy security models fail for agents (speed, identity, permissions all different). Regulatory landscape crystallizing: NIST, EU AI Act, OWASP, Singapore framework. See [[governance-safety-overview]].

---

## NEW Theme 12: Agentic AI Is Expanding Beyond Code (3/33 sources) ⭐⭐⭐

| Source | Evidence |
|--------|---------|
| [[agentic-ai-non-code-domains]] | Six industries: finance (40-60% compliance reduction), healthcare, legal, manufacturing, telecoms, transport. |
| [[agent-cost-economics]] | Enterprise ARPU $450-500/mo. SaaS disruption. $24.2B raised in 2025. |
| [[llm-wiki-pattern]] | Applies to research, reading, business — anywhere knowledge accumulates. |

The wiki's themes generalize across all industries. Main difference: non-code domains have higher stakes (healthcare hallucinations, legal liability). See [[beyond-code-industry-impact]].

---

## Theme Matrix (Updated May 2026)

| Theme | Sources | Strength | Change |
|-------|---------|----------|--------|
| Context is king | 15/42 | ⭐⭐⭐⭐⭐ | → Quantified (93% token reduction) |
| Composition over monoliths | 17/42 | ⭐⭐⭐⭐⭐ | ↑ Gas Town, Symphony, Multica all validate |
| Human in the loop (spectrum) | 13/42 | ⭐⭐⭐⭐⭐ | → Formalized as 6 UX patterns |
| Memory architectures | 10/42 | ⭐⭐⭐⭐⭐ | → "Understood" |
| Git as universal substrate | 9/42 | ⭐⭐⭐⭐⭐ | ↑↑ Gas Town is most git-native tool ever |
| Evaluation frameworks | 8/42 | ⭐⭐⭐⭐ | → "Framework exists" |
| Skills evolving into standard | 6/42 | ⭐⭐⭐⭐ | → Unchanged |
| Open standards winning | 5/42 | ⭐⭐⭐ | → Unchanged |
| Token economics drive architecture | 5/42 | ⭐⭐⭐ | → |
| Graph orchestration convergence | 4/42 | ⭐⭐⭐ | ~ Gas Town proves alternative path |
| Governance is next frontier | 4/42 | ⭐⭐⭐ | → |
| Expanding beyond code | 3/42 | ⭐⭐⭐ | → |

## See Also
- [[key-insights-agentic-landscape]]
- [[memory-architecture-comparison]]
- [[multi-agent-framework-guide]]
- [[cost-optimization-guide]]
- [[governance-safety-overview]]
- [[beyond-code-industry-impact]]
- [[agent-benchmarks]]
