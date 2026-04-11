---
type: analysis
created: 2026-04-09
updated: 2026-04-09
sources: ["[[scion-docs]]", "[[kiro-autonomous-agent]]", "[[claude-code-docs]]", "[[anthropic-skills-repo]]", "[[ten-pillars-agentic-skill-design]]", "[[llm-wiki-karpathy]]", "[[fabric-github]]", "[[personal-ai-infrastructure]]", "[[evaluating-agent-skills-caparas]]", "[[ai-technique-podcast]]", "[[skills-pipeline-sleestk]]"]
tags: [analysis, themes, cross-source, synthesis]
---

# Cross-Source Theme Analysis

16 sources, 8 tools, 2 standards, 3 methodologies, 1 practitioner account, 2 skill/eval resources. Here are the themes that appear across 3+ sources independently — not because they reference each other, but because they converged on the same ideas.

> **Note**: This analysis was originally written against 11 sources. The 5 newest sources (Paperclip, Spec Kit, BMad Method, Anthropic Eval Guide, Promptfoo) strengthen existing themes — particularly Theme 3 (human-in-the-loop spectrum) and Theme 7 (evaluation). A full refresh is recommended when the wiki reaches 20+ sources.

---

## Theme 1: Context Is King (9/11 sources)

The single most repeated idea across the wiki. Almost every source says some version of "getting the right context loaded matters more than anything else."

| Source | How it appears |
|--------|---------------|
| [[agent-skills-standard]] | Progressive disclosure: ~100 tokens at startup, full content only when activated |
| [[claude-code]] | MCP tools deferred, skills load on demand, subagent context isolation, CLAUDE.md under 200 lines |
| [[ten-pillars-agentic-skill-design]] | Pillar 9: four context management recipes (chunking, summarization, selective loading, persona templates) |
| [[pai]] | TELOS (10 files about you), three-tier memory (hot/warm/cold), "context document" as core primitive |
| [[fabric]] | Per-pattern model mapping, composable strategies applied on top of patterns |
| [[ai-technique-podcast]] | "Context beats clever prompting." Maintain a context document. Daily prompt anchored around priorities/constraints. |
| [[skills-pipeline-sleestk]] | Reference files loaded on demand, pipeline stages pass minimal structured context forward |
| [[llm-wiki-pattern]] | Index-first navigation — read the catalog, drill into relevant pages only |
| [[scion]] | Each agent gets its own container with its own context. No shared context pollution. |

**The consensus**: Don't load everything. Load the right thing at the right time. Every tool that scales has independently arrived at some form of progressive disclosure.

---

## Theme 2: Composition Over Monoliths (8/11 sources)

No one builds monolithic agents or skills. Everyone decomposes.

| Source | How it appears |
|--------|---------------|
| [[fabric]] | 251 focused patterns, each doing one thing. Unix philosophy: pipe and compose. |
| [[skills-pipeline-sleestk]] | 6-stage YouTube pipeline. 4-skill SaaS stack. Each skill is one domain. |
| [[claude-code]] | Subagents (Explore, Plan, General-purpose). Skills per task. MCP per service. |
| [[scion]] | Harness per tool. Template per agent. Grove per project. |
| [[agent-skills-standard]] | One skill per directory. "Keep SKILL.md under 500 lines." |
| [[ten-pillars-agentic-skill-design]] | Pillar 3 (SRP), Pillar 4 (modularity). Anti-pattern: monolithic skills. |
| [[pai]] | 63 skills, 21 hooks, 14 agents, 12 standalone packs. |
| [[kiro]] | Powers as modular packages. Sub-agents for coordination. |

**The consensus**: Small, focused, composable. The YouTube pipeline (6 stages) vs. a single "make a video" skill is the clearest illustration. This is the strongest convergence in the wiki.

---

## Theme 3: The Human Stays in the Loop — But How Much? (7/11 sources)

Every source addresses the human-agent boundary, but they disagree on where to draw it.

| Source | Position |
|--------|----------|
| [[scion]] | "Interaction is imperative." Humans must be involved. |
| [[kiro]] | Frontier agents work independently for hours/days. PR-only output for review. |
| [[claude-code]] | 6 permission modes — a configurable dial from full control to full autonomy. |
| [[pai]] | Agent learns and self-modifies, but human sets goals (TELOS) and reviews. |
| [[evaluating-agent-skills-caparas]] | Human review is Tier 3 evaluation — expensive, use sparingly. |
| [[ai-technique-podcast]] | "AI as thinking partner, not executor only." Let AI ask YOU questions back. |
| [[llm-wiki-pattern]] | Human curates sources and asks questions. LLM does everything else. |

**The spectrum**: From Scion (always interactive) to Kiro (hours of autonomy) to PAI (self-modifying). No consensus. Claude Code's approach — making it a configurable dial — may be the most pragmatic.

---

## Theme 4: Skills Are Evolving Into a Standard (6/11 sources)

The concept of "a reusable unit of agent capability" is converging on a common format.

| Source | Stage of evolution |
|--------|-------------------|
| [[fabric]] | **Patterns** (2023): system.md only. No metadata, no progressive disclosure. |
| [[agent-skills-standard]] | **Spec** (2025): SKILL.md + frontmatter + scripts/references/assets. Open standard. |
| [[claude-code]] | **Implementation** (2026): Extends spec with invocation control, subagent execution, MCP integration. |
| [[skills-pipeline-sleestk]] | **Production** (2026): Follows spec exactly. Chains skills into pipelines. Ships with test prompts. |
| [[ten-pillars-agentic-skill-design]] | **Methodology** (2024): Design principles for building effective skills. |
| [[evaluating-agent-skills-caparas]] | **Evaluation** (2026): How to measure whether skills actually work. |

**The evolution**: Fabric Patterns → Agent Skills Standard → Claude Code Skills → Pipelines + Evaluation. The trajectory is clear: from simple prompt files to a full lifecycle (design → build → test → deploy → evaluate).

---

## Theme 5: Memory Is the Next Frontier (6/11 sources)

How agents persist and accumulate knowledge is the most actively divergent area.

| Source | Memory approach |
|--------|---------------|
| [[pai]] | Three-tier (hot/warm/cold). Continuous signal capture. Self-modification. Most sophisticated. |
| [[claude-code]] | Dual system: CLAUDE.md (human-written) + auto memory (agent-written). Per working tree. |
| [[kiro]] | Persistent context across tasks/repos/sessions. Learns from code reviews. |
| [[llm-wiki-pattern]] | The wiki IS the memory — compiled, interlinked, maintained by the LLM. |
| [[ai-technique-podcast]] | "Context document technique." Maintain a persistent document about your role, goals, constraints. |
| [[scion]] | No shared memory. Each agent starts fresh in its own container. |

**The tension**: Persistent memory compounds value (PAI, Kiro, wiki pattern) but also compounds errors (stale learnings, wrong memories). Scion's fresh-start approach avoids this but wastes re-discovery. No one has solved the "memory hygiene" problem — how to keep accumulated knowledge accurate over time. The [[llm-wiki-pattern]]'s "lint" operation (health-check for contradictions) is the closest thing to a solution.

---

## Theme 6: Git as Universal Substrate (6/11 sources)

Git isn't just version control — it's the coordination layer, isolation mechanism, and review process.

| Source | Git usage |
|--------|-----------|
| [[scion]] | Git worktrees per agent (local), git init+fetch (hosted). Branches as isolation. |
| [[claude-code]] | Git worktrees for parallel sessions. PRs as output. Checkpointing via git. |
| [[kiro]] | Creates coordinated PRs across multiple repos. |
| [[pai]] | "The wiki is just a git repo." Version control everything, roll back when needed. |
| [[llm-wiki-pattern]] | "You get version history, branching, and collaboration for free." |
| [[skills-pipeline-sleestk]] | Skills stored in git. Versioned, shareable, forkable. |

**The consensus**: Git is the one coordination mechanism everyone agrees on. No one is building a custom protocol. But git only works for text-shaped artifacts — the open question is what coordinates non-code knowledge.

---

## Theme 7: Evaluation Is the Weakest Link (4/11 sources)

The gap between "building agents" and "knowing if they work" is acknowledged but unsolved.

| Source | What it says |
|--------|-------------|
| [[evaluating-agent-skills-caparas]] | Three-tier framework. "It feels better isn't good enough." LLM-as-judge only 70-85% agreement with humans. |
| [[ten-pillars-agentic-skill-design]] | Pillar 7. But explicitly acknowledges "no original controlled study." Benefits are "anticipated, not proven." |
| [[skills-pipeline-sleestk]] | Ships 10 inline test prompts — but happy-path only. No negative controls. |
| [[claude-code]] | 25+ hook events provide observability infrastructure, but no built-in eval framework. |

**The gap**: Everyone knows evaluation matters. Almost no one does it rigorously. The Caparas article provides the methodology; the Skills Pipeline shows inline testing; but no tool has an integrated eval pipeline. This is the biggest opportunity in the ecosystem.

---

## Theme 8: Open Standards Are Winning (5/11 sources)

Proprietary approaches are losing to open protocols.

| Source | Standard |
|--------|----------|
| [[mcp-protocol]] | Open protocol for tool integration. Used by Claude Code and Kiro. |
| [[agent-skills-standard]] | Open spec at agentskills.io. Used by Claude Code. |
| [[fabric]] | MIT licensed. 251 open patterns. Community-driven. |
| [[claude-code]] | Follows Agent Skills standard. MCP for tools. AGENTS.md import for cross-tool compatibility. |
| [[scion]] | Harness-agnostic. Supports any LLM tool via adapter pattern. |

**The trend**: MCP (tools/data) and Agent Skills (capabilities) are emerging as the two-layer open substrate. Fabric's patterns are the community-driven content layer. Proprietary approaches (Kiro Powers) exist but are converging toward open standards.

---

## Theme Matrix

How many sources support each theme:

| Theme | Sources | Strength |
|-------|---------|----------|
| Context is king | 9/11 | ⭐⭐⭐⭐⭐ |
| Composition over monoliths | 8/11 | ⭐⭐⭐⭐⭐ |
| Human in the loop (spectrum) | 7/11 | ⭐⭐⭐⭐ |
| Skills evolving into standard | 6/11 | ⭐⭐⭐⭐ |
| Memory as next frontier | 6/11 | ⭐⭐⭐⭐ |
| Git as universal substrate | 6/11 | ⭐⭐⭐⭐ |
| Open standards winning | 5/11 | ⭐⭐⭐ |
| Evaluation is weakest link | 4/11 | ⭐⭐⭐ |

## See Also
- [[key-insights-agentic-landscape]]
- [[ten-pillars-evidence-map]]
- [[multi-agent-orchestration]]
- [[context-management]]
