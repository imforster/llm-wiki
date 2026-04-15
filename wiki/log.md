# Wiki Log

## [2026-04-07] create | Wiki initialized
Wiki structure created: `CLAUDE.md` schema, `wiki/index.md`, `wiki/log.md`, directory scaffolding. Ready for first ingest.

## [2026-04-07] ingest | Scion Documentation
Source: https://googlecloudplatform.github.io/scion — multi-agent orchestration testbed by Google Cloud Platform. Created 13 wiki pages:
- Source: [[scion-docs]]
- Entities: [[scion]], [[google-cloud-platform]]
- Concepts: [[agent]], [[agent-state-model]], [[grove]], [[harness]], [[hub]], [[template]], [[runtime]], [[runtime-broker]], [[plugin-system]], [[multi-agent-orchestration]]

## [2026-04-07] ingest | Kiro Autonomous Agent
Source: https://kiro.dev/autonomous-agent/ — AWS's frontier agent for autonomous development tasks. Created 6 wiki pages, updated 1:
- Source: [[kiro-autonomous-agent]]
- Entities: [[kiro]], [[aws]]
- Concepts: [[frontier-agent]], [[kiro-powers]]
- Updated: [[multi-agent-orchestration]] — added Kiro as second approach, comparison with Scion

## [2026-04-07] ingest | Claude Code Documentation
Source: https://code.claude.com/docs/en — Anthropic's agentic coding tool. Created 4 wiki pages, updated 2:
- Source: [[claude-code-docs]]
- Entities: [[claude-code]], [[anthropic]]
- Concepts: [[mcp-protocol]]
- Updated: [[multi-agent-orchestration]] — added Claude Code as third approach alongside Scion and Kiro
- Updated: [[harness]] — added cross-reference to Claude Code entity

## [2026-04-07] update | Claude Code Documentation (deep ingest)
Discovered raw .md endpoints on the docs site. Re-ingested overview, how-claude-code-works, memory, sub-agents, permission-modes, hooks, and skills pages with full content. Updated:
- [[claude-code-docs]] — comprehensive takeaways from actual doc content
- [[claude-code]] — full architecture (agentic loop, tools, memory, permissions, extensibility)
- [[mcp-protocol]] — richer detail on Claude Code's MCP usage

## [2026-04-07] ingest | Anthropic Skills Repository & Agent Skills Spec
Source: https://github.com/anthropics/skills + https://agentskills.io/specification — open standard for agent skills and Anthropic's reference implementation. Created 2 wiki pages, updated 3:
- Source: [[anthropic-skills-repo]]
- Concepts: [[agent-skills-standard]]
- Updated: [[claude-code]] — linked skills to Agent Skills Standard
- Updated: [[mcp-protocol]] — clarified complementary relationship with Agent Skills
- Updated: [[multi-agent-orchestration]] — added Agent Skills to shared patterns

## [2026-04-08] ingest | The Ten Pillars of Agentic Skill Design
Source: ~/Documents/2-Areas/agentic-skills-research/agentic-skills-best-practices.pdf (.md version) — research paper by Ian Forster proposing a ten-pillar framework for skill design. Created 3 wiki pages, updated 2:
- Source: [[ten-pillars-agentic-skill-design]]
- Concepts: [[context-management]], [[prompt-engineering-patterns]]
- Updated: [[agent-skills-standard]] — cross-referenced Ten Pillars as design methodology
- Updated: [[multi-agent-orchestration]] — added skill design as open question

## [2026-04-08] ingest | LLM Wiki (Karpathy)
Source: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f — the foundational idea file for the LLM Wiki pattern. This wiki is a running instance of this pattern. Created 3 wiki pages:
- Source: [[llm-wiki-karpathy]]
- Entities: [[andrej-karpathy]]
- Concepts: [[llm-wiki-pattern]]
- Note: Meta-ingest — this source describes the methodology that governs how all other sources are ingested.

## [2026-04-08] ingest | Fabric
Source: https://github.com/danielmiessler/fabric — open-source framework with 251+ curated AI prompt patterns and composable strategies. Created 3 wiki pages, updated 2:
- Source: [[fabric-github]]
- Entities: [[fabric]], [[daniel-miessler]]
- Updated: [[prompt-engineering-patterns]] — added Fabric's composable strategies table
- Updated: [[agent-skills-standard]] — added Fabric Patterns to extension mechanisms comparison

## [2026-04-08] ingest | Personal AI Infrastructure (PAI)
Source: https://github.com/danielmiessler/Personal_AI_Infrastructure — personalized AI platform built on Claude Code with memory, skills, goals, and continuous learning. Created 2 wiki pages, updated 1:
- Source: [[personal-ai-infrastructure]]
- Entities: [[pai]]
- Updated: [[daniel-miessler]] — added PAI as second major project alongside Fabric

## [2026-04-08] query | Key Insights: The Agentic AI Landscape
Synthesized 10 key insights from all 8 sources in the wiki. Filed as analysis: [[key-insights-agentic-landscape]]. Covers: three architectural philosophies, the autonomy-interaction spectrum, emerging open standards, progressive disclosure consensus, memory as unsolved frontier, git as universal coordination, skill hierarchy crystallization, security trust models, the personal AI vision, and what's missing.

## [2026-04-08] ingest | How to Evaluate AI Agent Skills Without Relying on Vibes
Source: Article by JP Caparas — practical guide to skill evaluation with three-tier framework and economics. Created 2 wiki pages, updated 1:
- Source: [[evaluating-agent-skills-caparas]]
- Concepts: [[skill-evaluation]]
- Updated: [[key-insights-agentic-landscape]] — enriched evaluation gap (insight #10) with reference to this framework

## [2026-04-09] ingest | strAIght talk: AI Tips for Amazonians
Source: Podcast notes from raw/human/ai-technique-podcast.md — Amazon employees sharing AI workflow tactics. Created 1 wiki page:
- Source: [[ai-technique-podcast]]
- Cross-referenced: [[pai]], [[fabric]], [[llm-wiki-pattern]], [[context-management]], [[prompt-engineering-patterns]]
- Key insight: "context beats clever prompting" — validates the progressive disclosure and context document approaches seen across the wiki

## [2026-04-09] update | Overview
Updated overview.md with current stats (10 sources, 18 concepts, 10 entities), added "Key Themes" section synthesizing cross-cutting patterns, added [[ai-technique-podcast]] to practitioner insights.

## [2026-04-09] ingest | Skills Pipeline (Sleestk)
Source: https://github.com/Sleestk/Skills-Pipeline — chained skill pipelines for YouTube production, SaaS development, and Obsidian. Created 1 wiki page:
- Source: [[skills-pipeline-sleestk]]
- Key insight: Skills as pipelines — each stage's output is the next stage's input. Concrete implementation of progressive disclosure and context management recipes. Ships with inline test prompts.

## [2026-04-09] query | Ten Pillars Evidence Map
Synthesized evidence from all 11 wiki sources supporting each pillar of the Ten Pillars framework. Filed as analysis: [[ten-pillars-evidence-map]]. Strongest pillars: Scope (SRP), Modularity, Context Management. Weakest: Versioning, Testing. Identified 4 gaps for v3.

## [2026-04-09] query | Cross-Source Theme Analysis
Identified 8 common themes across all 11 sources with evidence tables and strength rankings. Filed as analysis: [[cross-source-themes]]. Strongest: "Context is king" (9/11), "Composition over monoliths" (8/11). Weakest: "Evaluation is weakest link" (4/11 — but universally acknowledged as a gap).

## [2026-04-09] query | How to Eval a Skill
Practical guide mapping Anthropic's prompt eval methodology onto skills. Filed as analysis: [[how-to-eval-a-skill]]. Covers: 5 testable surfaces (routing, tool selection, process, side effects, output quality), 3 tiers, pass@k, eval.yaml format, Claude Code hook integration, CI/CD pipeline.

## [2026-04-09] ingest | Anthropic Eval Guide + Promptfoo
Two eval resources ingested. Created 3 wiki pages:
- Source: [[anthropic-eval-guide]] — canonical eval methodology (SMART criteria, eval types, "volume over quality")
- Source: [[promptfoo]] — open-source eval CLI (YAML test cases, CI/CD, red teaming)
- Entity: [[promptfoo]] — the closest existing tool to a turnkey skill eval pipeline

## [2026-04-09] ingest | Paperclip
Source: https://github.com/paperclipai/paperclip — open-source orchestration for zero-human companies. Created 2 wiki pages, updated 1:
- Source: [[paperclip]]
- Entity: [[paperclip]]
- Updated: [[multi-agent-orchestration]] — added Paperclip as fourth approach (company-level orchestration above infrastructure, product, and tool layers)

## [2026-04-10] ingest | Spec Kit
Source: https://github.com/github/spec-kit — GitHub's spec-driven development toolkit. Created 2 wiki pages:
- Source: [[spec-kit]]
- Entity: [[spec-kit]]
- Key insight: SDD is progressive disclosure applied to development — each step produces a focused artifact that feeds the next. Agent-agnostic (30+ agents), with 50+ community extensions. Operates at the methodology layer between organizational orchestration (Paperclip) and tool-level execution (Claude Code).

## [2026-04-10] ingest | BMad Method
Source: https://github.com/bmad-code-org/BMAD-METHOD — AI-driven agile framework with scale-adaptive intelligence. Created 2 wiki pages:
- Source: [[bmad-method]]
- Entity: [[bmad-method]]
- Key insight: "Expert collaboration over autopilot" — agents guide your thinking rather than replacing it. Scale-adaptive planning adjusts depth to project complexity. Party Mode enables multi-persona dialogue in a single session.

## [2026-04-11] ingest | NotebookLM Notes Guide
Source: https://medium.com/@stevenbjohnson/getting-the-most-out-of-notes-in-notebooklm-d9d70316b780 — how-to guide by Steven Johnson on NotebookLM's notes system. Created 3 wiki pages, updated 2:
- Source: [[notebooklm-notes-guide]]
- Entities: [[notebooklm]], [[steven-johnson]]
- Updated: [[context-management]] — added provenance-as-context-metadata section, NotebookLM's 5K word limit as concrete context constraint
- Updated: [[llm-wiki-pattern]] — added contrast section comparing NotebookLM's session-oriented approach to the cumulative wiki pattern
- Key insight: NotebookLM validates the "human curates, AI processes" principle from a different angle — interactive exploration with provenance tracking vs. structured ingest with automatic cross-references.

## [2026-04-14] ingest | Batch 1: Agent Memory & Persistence (4 sources)

Ingested four sources addressing the wiki's "memory is the unsolved frontier" gap:

- **[[mem0-memory-management]]** — Mem0 engineering team: four memory layers, two-phase extraction pipeline (ADD/UPDATE/DELETE/NOOP), LOCOMO benchmarks (93% token reduction), graph-enhanced retrieval
- **[[continuum-memory-architectures]]** — CMA paper (Logan, arXiv): six formal requirements for agent memory (persistence, selective retention, retrieval-driven mutation, associative routing, temporal continuity, consolidation). CMA won 82/92 trials vs RAG.
- **[[agent-memory-systems-2026]]** — Bswen practitioner comparison: four patterns (vector-only, graph+vector, file+DB, hierarchical) with cost estimates and decision framework
- **[[efficient-memory-architectures]]** — Towards AI guide: four failure modes of flat vector storage, H-MEM, MemGPT (90% token savings), GraphRAG, selective forgetting (RIF formula)

New pages created:
- `wiki/sources/mem0-memory-management.md`
- `wiki/sources/continuum-memory-architectures.md`
- `wiki/sources/agent-memory-systems-2026.md`
- `wiki/sources/efficient-memory-architectures.md`
- `wiki/concepts/agent-memory-persistence.md`
- `wiki/entities/mem0.md`

Updated pages:
- `wiki/concepts/context-management.md` — added memory architecture cross-references, linked to [[agent-memory-persistence]]
- `wiki/index.md` — added 4 sources, 1 entity, 1 concept

## [2026-04-14] ingest | Batch 2: Evaluation Benchmarks (4 sources)

Ingested four benchmark sources addressing the wiki's "evaluation is the weakest link" gap:

- **[[humaneval-benchmark]]** — OpenAI (Chen et al., 2021): 164 Python problems, pass@k metric, 0% → 96.3% in 3 years. EvalPlus reveals 7-8 point robustness gap.
- **[[swe-bench]]** — Princeton (Jimenez et al., 2023): 2,294 real GitHub issues, top 74.4% resolved. SWE-bench Verified (500 tasks) is the standard.
- **[[gaia-benchmark]]** — Meta/HF (Mialon et al., 2023): 466 questions requiring reasoning + tools + multimodality. Humans 92%, AI <50%. Inverse of most benchmarks.
- **[[agentbench]]** — Tsinghua (Liu et al., ICLR 2024): 8 interactive environments, multi-turn. Commercial >> open-source. General AgentBench shows narrow-to-broad degradation.

New pages created:
- `wiki/sources/humaneval-benchmark.md`, `wiki/sources/swe-bench.md`, `wiki/sources/gaia-benchmark.md`, `wiki/sources/agentbench.md`
- `wiki/concepts/agent-benchmarks.md`

Updated pages:
- `wiki/concepts/skill-evaluation.md` — added benchmark cross-references
- `wiki/index.md` — added 4 sources, 1 concept

## [2026-04-14] ingest | Batch 3: Multi-Agent Frameworks (4 sources)

Ingested four open-source multi-agent framework sources, filling the gap where only product-level tools (Scion, Kiro, Claude Code) were represented:

- **[[autogen-multi-agent]]** — Microsoft Research (56.8K stars): conversation-based coordination, transitioning to graph-based Microsoft Agent Framework. Magentic-One generalist team.
- **[[crewai-multi-agent]]** — João Moura: role+goal+backstory agents, sequential/hierarchical processes, built-in short/long/entity memory.
- **[[langgraph-agent-orchestration]]** — LangChain: state-machine graphs, checkpointing (pause/resume), human-in-loop at any node. Most production-ready OSS framework.
- **[[openai-swarm]]** — OpenAI: educational, radically minimal. Two primitives (routines + handoffs). Not for production but pattern is production-ready.

Convergence signal: both AutoGen (MAF) and LangGraph moving to graph-based workflows — graphs becoming consensus architecture.

New pages: 4 source pages
Updated: [[multi-agent-orchestration]] concept (added open-source frameworks comparison table), index

## [2026-04-14] ingest | Batch 4: Gaps 4-7 (cost, governance, non-code, UX)

Ingested four sources covering the remaining wiki gaps:

- **[[agent-cost-economics]]** — Token costs ($80-1500/mo by profile), five waste vectors (60-80% waste), optimization playbook, $5T macro investment thesis, ROI scenarios (3.2% base vs 14.6% optimistic)
- **[[agentic-ai-governance]]** — Five-pillar governance framework, Shadow AI ($412K/yr), NIST AI Agent Standards Initiative (Jan 2026), EU AI Act, OWASP AIVSS, prompt injection, kill switches
- **[[agentic-ai-non-code-domains]]** — Six industries (finance 40-60% compliance reduction, legal existential disruption, healthcare, manufacturing, telecoms, transport), SaaS disruption, agent maturity levels 0-4
- **[[agentic-ux-patterns]]** — Six UX patterns (Intent Preview, Autonomy Dial, Explainable Rationale, Confidence Signal, Audit & Undo, Escalation), phased adoption, service recovery paradox

New pages: 4 source pages
Updated: index

## [2026-04-14] update | Overview rewrite for 33 sources

Rewrote `wiki/overview.md` to reflect expanded wiki:
- 33 sources (up from 17), 22 concepts (up from 18), 17 entities (up from 16)
- Six-layer stack (added Memory layer)
- Four new themes: graph convergence, token economics, governance frontier, beyond-code expansion
- Original themes strengthened with new evidence (memory no longer "unsolved", eval no longer "weakest link")
