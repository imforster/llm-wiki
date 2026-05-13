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

## [2026-04-15] create | Analysis: Memory Architecture Comparison

Created `wiki/analyses/memory-architecture-comparison.md` — "How AI Agents Remember: Four Patterns for Persistent Memory"

Synthesizes 8 sources into a comprehensive comparison:
- Four architecture patterns (vector-only, graph+vector, file+DB, hierarchical) with decision matrix
- CMA's six formal requirements mapped against each pattern
- Four failure modes of flat vector storage
- Cognitive science memory types (working, episodic, semantic, procedural)
- Forgetting as design requirement (Bjork, Ebbinghaus, RIF scoring)
- Benchmark landscape (full-context 72.9% vs Mem0g 68.4% at 93% fewer tokens)
- Tool comparison (Scion 0/6 CMA → PAI 5/6 CMA)
- Progression path: start vector-only → add graph → add hierarchy → add forgetting
- Five open questions for future research

First of five planned analyses from Six Thinking Hats session. Blog post candidate: "How AI Agents Remember: Four Patterns for Persistent Memory"

## [2026-04-15] create | Analysis: Multi-Agent Framework Guide

Created `wiki/analyses/multi-agent-framework-guide.md` — "Choosing a Multi-Agent Framework in 2026"

Synthesizes 8 sources (4 OSS frameworks + 4 product tools) into a comprehensive guide:
- Two-tier landscape: product-level (Scion, Kiro, Claude Code, Paperclip) + open-source (AutoGen, CrewAI, LangGraph, Swarm)
- Decision matrix across 8 factors (production readiness, control, state, memory, debugging, etc.)
- Graph convergence thesis: AutoGen and LangGraph both moving to graphs as consensus architecture
- Emerging stack: Paperclip → LangGraph/MAF → Claude Code/Kiro → Scion
- Multi-agent memory problem: shared memory, conflicting memories, cascading permissions, cost multiplication
- Progression path: Swarm (learn) → CrewAI (prototype) → LangGraph (production) → MAF/Paperclip (enterprise)

Second of five planned analyses. Blog post candidate: "Choosing a Multi-Agent Framework in 2026"

## [2026-04-15] create | Analysis: Cost Optimization Guide

Created `wiki/analyses/cost-optimization-guide.md` — "Why Your AI Agent Costs 10× More Than It Should"

Synthesizes 6 sources connecting token economics to architectural decisions:
- Five waste vectors (60-80% of tokens wasted) with specific fixes
- Architecture-cost connections: memory choice → token cost, multi-agent → cost multiplication, context management → direct savings
- Three-tier optimization playbook ordered by ROI (caching → routing → memory architecture)
- Macro picture: $5T capex, 3.2% base ROI, token explosion, three historical analogies
- Cost-Quality-Speed triangle: best optimizations improve two dimensions simultaneously

Third of five planned analyses. Blog post candidate: "Why Your AI Agent Costs 10× More Than It Should"

## [2026-04-15] create | Analysis: Governance & Safety Overview

Created `wiki/analyses/governance-safety-overview.md` — "The Shadow AI Problem: Governing Agents You Don't Know About"

Connects governance gap to wiki's existing security models. Five pillars mapped to six UX patterns as user-facing governance layer. Regulatory landscape (NIST, EU AI Act, OWASP, Singapore). Implementation roadmap (4 phases). Key finding: Autonomy Dial = Claude Code permission modes at different layers.

Fourth of five planned analyses. Blog post candidate: "The Shadow AI Problem: Governing Agents You Don't Know About"

## [2026-04-15] create | Analysis: Beyond Code Industry Impact

Created `wiki/analyses/beyond-code-industry-impact.md` — "Agentic AI Beyond Software: Six Industries Being Transformed"

Tests whether wiki's eight themes generalize beyond software development. Six industries analyzed (finance, healthcare, legal, manufacturing, telecoms, transport). Verdict: all themes are universal, but stakes are higher outside code. SaaS disruption thesis. Agent maturity levels 0-4.

Fifth of five planned analyses. Blog post candidate: "Agentic AI Beyond Software: Six Industries Being Transformed"

All five planned analyses from Six Thinking Hats session now complete. Wiki has 9 analyses total (up from 4).

## [2026-04-15] lint | Wiki health check

**Fixed:**
- Removed duplicate [[bmad-method]] entry in index (was listed twice)
- Corrected overview concept count: 22 → 20

**Stale analyses flagged for refresh (future task):**
- [[cross-source-themes]] — written against 11 sources, wiki now has 33. File itself recommends refresh at 20+.
- [[key-insights-agentic-landscape]] — written against 16 sources. Doesn't reflect memory, eval, multi-agent, cost, governance, or industry sources.

**Info noted:**
- 9 thin Scion-specific concept pages (grove, harness, hub, template, runtime, runtime-broker, plugin-system, agent-state-model, kiro-powers) — 1 source each, few inbound links
- Missing entity pages for Microsoft, OpenAI, LangChain, Princeton, Meta — minor, referenced but not deeply analyzed

## [2026-04-15] update | Refreshed cross-source-themes and key-insights for 33 sources

**cross-source-themes.md**: Refreshed from 11 → 33 sources.
- Original 8 themes retained and strengthened with new evidence
- Theme 1 (Context): now quantified (93% token reduction)
- Theme 3 (Human-in-loop): formalized as 6 UX patterns
- Theme 5 (Memory): upgraded from "unsolved" to "understood with clear tradeoffs"
- Theme 7 (Evaluation): upgraded from "weakest link" to "framework exists"
- 4 new themes added: graph convergence, token economics, governance, beyond-code

**key-insights-agentic-landscape.md**: Refreshed from 16 → 33 sources.
- 6 layers (was 5, added Memory layer)
- Autonomy spectrum formalized with UX patterns and metrics
- Memory upgraded from "unsolved frontier" to "understood"
- Evaluation upgraded with 4 benchmarks
- 4 new insights: token economics, multi-agent philosophies, governance pillars, remaining gaps
- "What's Still Missing" section updated for current state

## [2026-04-15] query + create | Conversational query test → gap analysis

Tested wiki with cross-cutting query: "Build a long-running knowledge management agent — what does the wiki recommend?"

Wiki provided strong architectural guidance across memory (Graph+Vector), coordination (LangGraph), cost ($200-500/mo), trust (Autonomy Dial), and non-code considerations.

Exposed 5 gaps filed as `wiki/analyses/wiki-gap-analysis-apr-2026.md`:
1. No "getting started" tutorial (what to choose vs how to wire it)
2. No LangGraph + Mem0 integration source
3. No team-level knowledge management agent sources
4. No knowledge quality evaluation metrics
5. No agent observability tooling sources

## [2026-04-15] ingest | Gap-filling batch: 4 sources addressing high-priority gaps

Researched and ingested 4 sources addressing gaps identified by conversational query testing:

- **[[memory-lifecycle-drift]]** — TDS (Nweke, Apr 2026): five lifecycle components (decay, contradiction detection, confidence scoring, compression, expiry). Fills gaps #6-7 (memory quality metrics, regression).
- **[[langgraph-mem0-integration]]** — DigitalOcean (Payong, Mar 2026): step-by-step LangGraph + Mem0 integration with production considerations. Fills gap #2.
- **[[multi-agent-observability]]** — Future AGI (Mar 2026): OpenTelemetry spans, debugging patterns, key metrics for multi-agent systems. Fills gaps #5, #10.
- **[[ai-environmental-impact]]** — arXiv (Jegham et al., May 2025): energy/carbon/water benchmarks across 30 models. o3 = 70× GPT-4.1 nano. Claude 3.7 Sonnet most eco-efficient. Fills gaps #12-13.

Wiki now has 37 sources. Gaps addressed: #2, #5, #6, #7, #10, #12, #13.

## [2026-04-15] create | Analysis: Getting Started Guide

Created `wiki/analyses/getting-started-guide.md` — "Building Your First Long-Running Agent"

Five-phase guide synthesizing wiki's consensus recommendations:
1. Single agent + Mem0 memory (Week 1)
2. Memory lifecycle: decay, contradiction, confidence, compression, expiry (Week 2)
3. Human-in-the-loop: Plan & Propose → Act with Confirmation (Week 3)
4. Observability: OpenTelemetry spans + key metrics (Week 4)
5. Scale to multi-agent (Month 2+)

Includes cost budgets per phase ($80-500/mo), common mistakes, and what's still not covered.
Fills gap #1 from wiki-gap-analysis. Wiki now has 11 analyses.

## [2026-04-15] ingest | Multi-agent advanced gaps: 2 sources

- **[[crewai-production-guide]]** — Practical crew patterns (content pipeline, customer support, event-driven), production deployment, cost tracking. Fills gaps #9 (CrewAI examples), #11 (role design patterns).
- **[[shared-agent-memory]]** — Shared memory layer pattern (solution store + write hook + retrieval step + threshold), conflict resolution status (implicit via recency, explicit remains unsolved), partial/failed solution storage. Fills gaps #14, #15, #16.

Wiki now has 39 sources. Multi-agent advanced gaps: 5/5 addressed (though explicit conflict resolution confirmed as open problem across all sources).

## [2026-04-15] create | Analysis: Hybrid Memory Architecture (Wiki + Mem0)

Created `wiki/analyses/hybrid-memory-architecture.md` — "Combining Wiki + Mem0"

Novel architecture synthesized from 7 wiki sources (not documented in any single source):
- Layer 1: Mem0 as fast memory (working + session + user) — sub-second retrieval, automatic forgetting
- Layer 2: Wiki as deep memory (semantic + organizational) — synthesis, provenance, git history
- Layer 3: Bridge — bidirectional sync (wiki→Mem0 index extraction, Mem0→wiki consolidation)
- Achieves 5/6 CMA compliance (matching PAI) with full transparency
- Implementation in 5 phases, $1-55/month cost estimate
- Directly supports content pipeline goal (interactions → Mem0 → wiki → blog posts)

Wiki now has 12 analyses.

## [2026-05-08] ingest | Gas Town

Source: https://github.com/gastownhall/gastown — open-source multi-agent workspace orchestration system (Go). Coordinates 20-30+ AI coding agents with git-worktree persistence, Bors-style merge queue, three-tier health monitoring, and federated cross-workspace coordination.

Created 2 wiki pages, updated 2:
- Source: [[gastown]]
- Entity: [[gastown]]
- Updated: [[multi-agent-orchestration]] — added Gas Town as fifth approach ("Workspace-first"), source count now 8
- Updated: [[index]] — added source and entity entries

Key insight: Gas Town represents the most complete implementation of "git as universal coordination" in the wiki — git worktrees for persistence, git-backed issue tracking (beads), and a merge queue that enforces quality gates. Fills the gap between tool-level orchestration (Claude Code) and organizational orchestration (Paperclip) with a practical workspace layer.

## [2026-05-09] ingest | Symphony + Multica

Two multi-agent orchestration tools ingested:

- **[[symphony]]** — OpenAI's spec-first orchestration (23K stars). A 78KB language-agnostic specification (SPEC.md) that teams implement in their own language. Elixir reference implementation. Reads Linear issues, creates per-issue isolated workspaces, runs Codex app-server. WORKFLOW.md as single source of truth. No database, no UI — intentionally minimal scheduler/runner.

- **[[multica]]** — Open-source managed agents platform (26.6K stars). Agents as first-class teammates with profiles, board presence, comments, blocker reporting. Reusable skills that compound. Cloud-first (Next.js + Go + PostgreSQL). Most vendor-neutral: 11 agent CLIs supported. Lighter than Paperclip, heavier than Symphony.

Created 4 wiki pages, updated 2:
- Sources: [[symphony]], [[multica]]
- Entities: [[symphony]], [[multica]]
- Updated: [[multi-agent-orchestration]] — added Symphony (Spec-first) and Multica (Platform-first) as 6th and 7th approaches, source count now 10
- Updated: [[index]] — added source and entity entries

Key insight: The multi-agent orchestration space now has a clear spectrum of approaches in the wiki — from minimal spec/protocol (Symphony) through workspace CLI (Gas Town) to full SaaS platform (Multica) to company simulator (Paperclip). Symphony's "spec-first" approach is unique: publish a protocol, let teams implement it. Multica's "agents as teammates" metaphor is the most human-centric UX framing.

## [2026-05-09] create | Analysis: Orchestration Tools Compared

Created `wiki/analyses/orchestration-tools-compared.md` — "Agent Orchestration Tools Compared: The 2026 Landscape"

Synthesizes wiki sources (Gas Town, Symphony, Multica, Paperclip, + 4 OSS frameworks) with 3 external comparison articles:
- rywalker.com: 10-tool comparison (March 2026)
- tmchow gist: Gas Town vs 7 frameworks deep survey (March 2026)
- championswimmer gist: Agent stack from LLM call to orchestrator (Feb 2026)

Key findings:
- Fundamental architectural split: conversation-as-control (3-5 agents) vs process-model (20-30 agents)
- Seven distinct orchestration philosophies from simple loop (Ralph) to company sim (Paperclip)
- Gas Town's GUPP + Dolt cell-level merge is genuinely unique — no other framework has crash-surviving pull-based execution
- Symphony's spec-first approach is unique — publish a protocol, not a product
- Multica is the only tool designed for multi-user team collaboration with agents
- Cross-model adversarial review (Metaswarm) emerging as strongest trust pattern
- Prediction: by 2028, "autonomous agent" and "orchestrator" categories merge

## [2026-05-09] lint | Wiki Gap Analysis: May 2026

Created `wiki/analysis/wiki-gap-analysis-may-2026.md` — monthly health check.

Stats: 42 sources (+3), 20 entities (+3), 20 concepts (—), 13 analyses (+1).

April gaps: 0/5 fully closed. Content pipeline (#17-19) remains top priority.
New gaps: 6 identified from orchestration ingests (harness engineering, cross-model review, agent identity, workspace isolation, agent-native VCS, governance depth).

Strengths: Multi-agent orchestration coverage now comprehensive (10 sources, 7 approaches, external validation).
Weaknesses: Content pipeline stalled, no new concepts, overview.md stale, orchestration-heavy month.

## [2026-05-09] update | Multi-Agent Framework Guide refreshed for 11 sources

Updated `wiki/analysis/multi-agent-framework-guide.md` from 8 → 11 sources:
- Added Gas Town, Symphony, Multica to landscape (now three tiers: product, orchestration, framework)
- Added "Architectural Split" section (conversation vs graph vs process-model vs issue-tracker vs platform)
- Expanded coordination patterns table (7 → 10 patterns)
- Updated recommendations (#6-8 for Gas Town, Symphony, Multica)
- Updated progression path (7 steps from Learn → Govern)
- Added 4 new open questions
- Updated emerging stack diagram
- Cross-referenced [[orchestration-tools-compared]] analysis

## [2026-05-09] update | Refreshed cross-source-themes and key-insights for 42 sources

**cross-source-themes.md**: Refreshed from 33 → 42 sources.
- Theme 2 (Composition): 14/33 → 17/42. Added Gas Town (7 roles, molecules), Symphony (WORKFLOW.md, isolated workspaces), Multica (compounding skills).
- Theme 6 (Git): 6/33 → 9/42. Upgraded to ⭐⭐⭐⭐⭐. Gas Town is most git-native tool in wiki (worktrees + Dolt + merge queue + federation).
- Theme 9 (Graphs): Added nuance — Gas Town's process-model proves graphs aren't the only path to scale.
- Theme matrix updated with new counts.

**key-insights-agentic-landscape.md**: Refreshed from 33 → 42 sources.
- Insight 1: Six layers → Seven layers. Added Orchestration layer (Gas Town, Symphony, Multica).
- Insight 12: Four philosophies → Seven philosophies. Split into frameworks + orchestration tools. Added architectural split finding.
- Insight 14: Added 3 new gaps (harness engineering, cross-model review, content pipeline).
- Updated emerging stack diagram.

## [2026-05-11] ingest | OpenAI Agents SDK, Google ADK, Microsoft Agent Framework 1.0
Three major multi-agent frameworks ingested to update the landscape analysis. Created:
- Sources: [[openai-agents-sdk]], [[google-adk]], [[microsoft-agent-framework]]
Updated:
- [[autogen-multi-agent]] — added legacy/maintenance note (superseded by MAF)
- [[openai-swarm]] — added superseded note (replaced by Agents SDK)
- [[multi-agent-orchestration]] — expanded framework table from 4 to 7, updated convergence signal
- [[multi-agent-framework-guide]] — full rewrite: 14 sources, 7 OSS frameworks (5 active + 2 legacy), protocol layer (MCP/A2A/AG-UI), confirmed graph convergence, updated decision matrix and recommendations
- [[index]] — added three new source entries, updated analysis summary

## [2026-05-12] ingest | Batch: Token Optimization, Vibe Coding, Rex, Kiro CLI 2.0

Four sources ingested covering practical AI development patterns:

- **[[claude-code-token-optimization]]** — KDNuggets (Mehreen, May 2026): 7 practical tactics for reducing Claude Code token waste. Core insight: "stop thinking about prompts, start thinking about context architecture." Model switching, CLAUDE.md sizing, subagent isolation, /compact timing, /context diagnostics.

- **[[vibe-coding-lessons-k10s]]** — k10s.dev (shvbsle, May 2026): 7 months of vibe-coding a GPU Kubernetes TUI, archived and rewritten. Five tenets: AI builds features not architecture, god objects are the default AI artifact, velocity illusion widens scope, positional data is a time bomb, AI doesn't own state transitions. Key meta-insight: CLAUDE.md as architecture enforcement mechanism.

- **[[trusted-remote-execution-rex]]** — AWS Open Source Blog (MacDonald/Brindle, May 2026): Rex — open-source policy-enforced scripting runtime. Rhai (sandboxed language) + Cedar (policy language). First concrete implementation of policy-enforced agent execution in the wiki. Host owner controls permissions regardless of agent behavior.

- **[[kiro-cli-2.0]]** — Kiro Blog (April 2026): CLI 2.0 with headless mode (API key → CI/CD automation), Windows support, subagent monitoring (ctrl+g), task lists. Moves Kiro from interactive tool to agentic platform.

New pages created:
- Sources: [[claude-code-token-optimization]], [[vibe-coding-lessons-k10s]], [[trusted-remote-execution-rex]], [[kiro-cli-2.0]]
- Entities: [[rex]], [[cedar]]
- Concepts: [[vibe-coding]], [[policy-enforced-execution]]

Updated pages:
- [[kiro]] — added CLI 2.0 section (headless, subagents, task lists)
- [[claude-code]] — added token optimization section
- [[context-management]] — added CLAUDE.md as architecture enforcement + token optimization tactics (source count 7 → 9)
- [[index]] — added 4 sources, 2 entities, 2 concepts

## [2026-05-12] ingest | LYT Web Clipper Prompt

- **[[lyt-web-clipper-prompt]]** — Nick Milo's Obsidian Web Clipper interpreter prompt: three-layer AI processing (summary, headlines, things). Model-agnostic. Lightweight complement to the LLM Wiki pattern — capture-time vs. ingest-time processing.