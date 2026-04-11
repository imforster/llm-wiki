---
type: analysis
created: 2026-04-08
updated: 2026-04-10
sources: ["[[scion-docs]]", "[[kiro-autonomous-agent]]", "[[claude-code-docs]]", "[[anthropic-skills-repo]]", "[[ten-pillars-agentic-skill-design]]", "[[llm-wiki-karpathy]]", "[[fabric-github]]", "[[personal-ai-infrastructure]]", "[[evaluating-agent-skills-caparas]]", "[[ai-technique-podcast]]", "[[skills-pipeline-sleestk]]", "[[anthropic-eval-guide]]", "[[promptfoo]]", "[[paperclip]]", "[[spec-kit]]", "[[bmad-method]]"]
tags: [synthesis, landscape, insights, agentic-ai]
---

# Key Insights: The Agentic AI Landscape (April 2026)

Synthesized from 16 sources across this wiki. This analysis captures the patterns, tensions, and emerging consensus visible when you look across the entire landscape rather than at any single tool.

---

## 1. Five Layers Are Emerging

The landscape has organized into five distinct layers:

| Layer | Representative | Core Bet |
|-------|---------------|----------|
| **Company** | [[paperclip]] | Orchestrate agents into companies with org charts, budgets, governance. |
| **Methodology** | [[spec-kit]], [[bmad-method]] | Structure the development process. Specs before code, or adaptive agile workflows. |
| **Infrastructure** | [[scion]] (GCP) | The agent runtime is the hard problem. Be a hypervisor. Stay agnostic. |
| **Product** | [[kiro]] (AWS) | Ship an opinionated end-to-end agent. Autonomy and scale matter most. |
| **Tool** | [[claude-code]] (Anthropic), [[fabric]] | Make the individual agent excellent. Let users compose upward. |

The methodology layer is new — [[spec-kit]] ("specs before code") and [[bmad-method]] ("expert collaboration over autopilot") represent two competing philosophies for structuring AI-assisted development. [[paperclip]] adds the company layer above everything, orchestrating agents into organizations with budgets and governance.

## 2. The Autonomy–Interaction Spectrum Is the Central Design Tension

Every tool in this wiki takes a position on how much autonomy to give agents:

```
← More Human Control                              More Agent Autonomy →

Claude Code        Claude Code       Scion           Kiro            PAI
(default mode)     (auto mode)       (--yolo +       (frontier       (learn +
reads only,        classifier        container       agent, hours    self-modify)
ask permission     reviews actions   isolation)      independent)
```

- [[scion]]'s philosophy: "Interaction is imperative." Don't expect agents to finish alone.
- [[kiro]]'s philosophy: "Frontier agents work independently for hours or days."
- [[claude-code]]: Offers a dial — six permission modes from `default` to `bypassPermissions`.
- [[pai]]: Goes furthest — the agent modifies *itself* based on what it learns.

No consensus exists. The right answer likely depends on task type, risk tolerance, and trust level. Claude Code's configurable permission modes may be the most pragmatic approach.

## 3. Two Open Standards Are Emerging as the Interoperability Layer

| Standard | What It Does | Who Uses It |
|----------|-------------|-------------|
| [[mcp-protocol]] | Connects agents to external tools and data | Claude Code, Kiro, Fabric (via plugins) |
| [[agent-skills-standard]] | Packages reusable agent capabilities | Claude Code, open standard at agentskills.io |

MCP and Agent Skills are complementary, not competing. Skills teach agents *how* to do things (instructions, workflows). MCP connects agents to external *tools and data* (APIs, databases). Together they form a two-layer extensibility stack that could become the shared substrate across tools.

[[fabric]] Patterns are the simpler predecessor — same concept as skills (curated prompts by task) but without scripts, progressive disclosure, or tool integration. The evolution: Fabric Patterns (2023) → Agent Skills Standard (2025) → Claude Code Skills (2026).

## 4. Progressive Disclosure Is the Consensus Solution to Context Management

Every tool that scales has independently converged on the same pattern: **load metadata first, full content only when needed**.

| Tool | Implementation |
|------|---------------|
| [[agent-skills-standard]] | ~100 tokens (name+description) at startup → <5000 tokens when activated → resources on demand |
| [[claude-code]] | MCP tool definitions deferred (names only until used). Skills load on demand. Subagents get isolated context. |
| [[scion]] | Each agent gets its own container with its own context. No shared context pollution. |
| [[llm-wiki-pattern]] | Read index first (~catalog), drill into relevant pages only. |

This is the answer to "how do you give an agent lots of capabilities without filling up the context window." The [[ten-pillars-agentic-skill-design]] framework formalizes this with four concrete recipes (chunking, progressive summarization, selective loading, persona templates).

## 5. Memory Is the Unsolved Frontier

The biggest divergence across tools is how they handle persistent knowledge:

| Approach | Tools | Tradeoff |
|----------|-------|----------|
| **No memory** | Scion (each agent starts fresh) | Clean but wasteful — re-discovers known information |
| **Instruction files** | Claude Code (CLAUDE.md), Scion (templates) | Human-maintained, explicit, but static |
| **Auto memory** | Claude Code (auto memory), Kiro (learns from reviews) | Accumulates automatically, but risk of stale/wrong memories |
| **Structured self-knowledge** | PAI (TELOS: 10 files about you) | Deep personalization, but high setup cost |
| **Compiled knowledge base** | [[llm-wiki-pattern]] (this wiki) | Compounding synthesis, but requires active curation |

PAI's three-tier memory (hot/warm/cold) with continuous signal capture is the most sophisticated implementation. But no one has solved the fundamental tension: **persistent context compounds value but also compounds errors**. Stale memories, wrong learnings, and outdated instructions degrade over time. The wiki pattern's "lint" operation (health-check for contradictions and stale claims) is one approach to this, but it's manual.

## 6. Git Is the Universal Coordination Mechanism

Every tool uses git as the shared state layer for multi-agent work:

- [[scion]]: Git worktrees (local) or git init+fetch (hosted) per agent
- [[kiro]]: Creates PRs across multiple repos
- [[claude-code]]: Git worktrees for parallel sessions, PRs as output
- [[pai]]: Git-backed, version control everything

Git is the one thing all approaches agree on. It provides isolation (branches/worktrees), coordination (PRs), history (commits), and review (diffs). No one is building a custom coordination protocol — git is good enough.

But git only works for code-shaped artifacts. The open question: what's the coordination mechanism for non-code knowledge? The [[llm-wiki-pattern]] uses markdown files in a git repo, which works, but it's not clear this scales to team-level knowledge management.

## 7. The Skill Hierarchy Is Crystallizing

A clear hierarchy of "how to extend an agent" has emerged, from simplest to most complex:

```
Fabric Patterns     →  Agent Skills      →  Claude Code Skills  →  PAI Skills
(system.md only)       (SKILL.md +          (+ invocation         (CODE → CLI →
                        scripts/assets)       control, subagent     PROMPT → SKILL
                                              execution, MCP)       hierarchy)
```

PAI's insight is the most radical: **code before prompts**. If you can solve it with a bash script, don't use AI. The hierarchy CODE → CLI → PROMPT → SKILL prioritizes deterministic outcomes. This inverts the usual assumption that AI should handle everything.

## 8. Security Models Reflect Trust Philosophies

| Tool | Security Approach | Philosophy |
|------|-------------------|------------|
| [[scion]] | Container isolation + `--yolo` mode | Guardrail *outside* the agent |
| [[claude-code]] | Permission modes + classifier (auto mode) | Guardrail *inside* the agent |
| [[kiro]] | Sandbox environments + PR-only output | Guardrail at the *output* layer |
| [[pai]] | Policy-based hooks + allowlists | Guardrail via *deterministic rules* |

The [[ten-pillars-agentic-skill-design]] framework (Pillar 6) recommends defense-in-depth: credential management, input validation, sandboxing, human-in-the-loop, and prompt injection defenses. No single tool implements all five layers.

## 9. The "Personal AI" Vision Is Bigger Than Coding

Most tools in this wiki focus on software development. But two sources point to something larger:

- **[[llm-wiki-pattern]]**: Applies to research, reading, business, personal development — anywhere you accumulate knowledge over time.
- **[[pai]]**: "AI should magnify everyone — not just the top 1%." TELOS captures your mission, goals, beliefs, strategies. The AI knows *you*, not just your codebase.

The coding agent landscape may be a proving ground for a broader pattern: **persistent, personalized AI infrastructure that compounds knowledge and capability over time**. The tools that win in coding will likely expand to other domains.

## 10. What's Missing

Gaps visible across the entire wiki:

- **Evaluation**: No standard way to measure whether a skill, pattern, or agent configuration actually works better than alternatives. The [[ten-pillars-agentic-skill-design]] paper explicitly acknowledges this — its benefits are "anticipated, not proven." The [[evaluating-agent-skills-caparas]] article proposes a three-tier framework (deterministic → LLM-as-judge → human review) with concrete economics. [[promptfoo]] (now part of OpenAI) provides the closest turnkey tooling. [[spec-kit]]'s `/speckit.checklist` and `/speckit.analyze` commands show built-in quality gates emerging. But no tool has an integrated end-to-end skill eval pipeline yet.
- **Conflict resolution**: When multiple agents make conflicting changes, or when memory contradicts new information, there's no standard resolution mechanism.
- **Cost modeling**: No tool provides clear cost-per-task estimates. PAI tracks signals but doesn't model costs. The Ten Pillars framework notes this gap.
- **Non-code domains**: Almost everything is optimized for software development. The [[llm-wiki-pattern]] and [[pai]] gesture toward broader applications, but tooling lags.
- **Interoperability**: MCP and Agent Skills are emerging standards, but no tool can seamlessly hand off work to another tool. Scion comes closest (harness-agnostic) but requires containerization.

---

*Analysis based on 16 sources ingested into this wiki between 2026-04-07 and 2026-04-10. Represents the state of the landscape as observed from public documentation and open-source repositories.*

## See Also
- [[multi-agent-orchestration]]
- [[context-management]]
- [[agent-skills-standard]]
- [[llm-wiki-pattern]]
- [[prompt-engineering-patterns]]
