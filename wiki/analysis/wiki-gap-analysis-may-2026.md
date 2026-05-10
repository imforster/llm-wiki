---
type: analysis
created: 2026-05-09
updated: 2026-05-09
sources: ["[[gastown]]", "[[symphony]]", "[[multica]]", "[[orchestration-tools-compared]]"]
tags: [analysis, gaps, status, roadmap]
---

# Wiki Gap Analysis: Status Tracker (May 2026)

Monthly health check. Assesses progress since April, identifies new gaps from recent ingests, and tracks open items.

## Wiki Stats

| Metric | April 15 | May 9 | Delta |
|--------|----------|-------|-------|
| Sources | 39 | 42 | +3 |
| Entities | 17 | 20 | +3 |
| Concepts | 20 | 20 | — |
| Analyses | 12 | 13 | +1 |
| Themes | 12 | 12 | — |
| Multi-agent orchestration sources | 7 | 10 | +3 |

## May Activity

3 ingests, 1 analysis:
- **Gas Town** — workspace-first orchestration (git worktrees, merge queue, federation)
- **Symphony** — OpenAI's spec-first orchestration (WORKFLOW.md, per-issue workspaces)
- **Multica** — platform-first orchestration (agents as teammates, compounding skills)
- **Orchestration Tools Compared** — analysis synthesizing 3 external comparison sources

## April Open Gaps: Status Update

| # | Gap | April Status | May Status | Notes |
|---|-----|---|---|---|
| 3 | Team knowledge management agents | ⬜ Open | 🟡 Partial | Multica's "agents as teammates" + compounding skills partially addresses this |
| 4 | Knowledge quality eval metrics | ⬜ Open | ⬜ Open | No new sources |
| 17 | Content creation workflow (analysis → blog) | ⬜ Open | ⬜ Open | No progress |
| 18 | AI-assisted writing/editing for prose | ⬜ Open | ⬜ Open | No progress |
| 19 | Wiki "publish" operation | ⬜ Open | ⬜ Open | No progress |

**Summary**: 0 of 5 April gaps fully closed. Content pipeline gaps (#17-19) remain the highest priority — they directly support the 6-month goal of turning wiki knowledge into publishable content.

## New Gaps Identified (May 2026)

From the orchestration tools ingest and analysis:

| # | Gap | Category | Priority | Next Action |
|---|-----|----------|----------|-------------|
| 21 | Harness engineering practices | Dev Practice | Medium | Research: OpenAI's "harness engineering" concept — preparing codebases for autonomous agents |
| 22 | Cross-model adversarial review | Trust/Quality | Medium | Research: Metaswarm's pattern (writer ≠ reviewer), fresh reviewer on retry, blocking quality gates |
| 23 | Agent reputation/identity systems | Architecture | Low | Research: Gas Town's Agent Beads as permanent capability ledger, Wasteland reputation stamps |
| 24 | Workspace isolation patterns | Architecture | Low | Covered partially by Gas Town (worktrees) and Symphony (per-issue dirs), but no dedicated concept page |
| 25 | Agent-native version control | Architecture | Low | Research: AgentHub's branchless DAG + message board (Karpathy) — git redesigned for agent swarms |
| 26 | Multica/Paperclip comparison depth | Comparison | Low | The wiki has both but no deep analysis of "lightweight vs heavy governance" tradeoffs |

## Concept Pages Needed

The following concepts are referenced across multiple sources but lack dedicated wiki pages:

| Concept | Mentioned In | Priority |
|---------|-------------|----------|
| Harness engineering | Symphony, orchestration analysis | Medium |
| GUPP / pull-based execution | Gas Town, orchestration analysis | Low |
| Agent identity persistence | Gas Town, orchestration analysis | Low |
| Workspace isolation | Gas Town, Symphony, Multica | Low |

## Strengths

The wiki's **multi-agent orchestration** coverage is now comprehensive:
- 10 sources feeding the concept page
- 7 distinct approaches documented (loop → spec → handoff → workspace → platform → graph → company)
- Head-to-head comparison analysis with decision framework
- External validation from 3 independent comparison articles
- Clear architectural taxonomy (conversation-as-control vs process-model)

## Weaknesses

1. **Content pipeline gaps persist** (#17-19) — the user's stated goal of analysis → blog post workflow has no progress since April
2. **No new concept pages created in May** — ingests added sources and entities but didn't expand the concept layer
3. **Orchestration-heavy** — 3/3 May ingests are orchestration tools. Other wiki themes (memory, eval, governance, cost) haven't grown
4. **Overview.md is stale** — last updated April 15, doesn't reflect May additions

## Recommended Next Actions (Priority Order)

1. **Content pipeline** (gaps #17-19): Define a publish workflow, research AI writing tools, create a template for analysis → blog post conversion. This is the user's 6-month goal.
2. **Update overview.md**: Reflect 42 sources, new orchestration landscape, May activity.
3. **Harness engineering concept page** (gap #21): New concept emerging from Symphony/OpenAI — worth a dedicated page since it's a prerequisite for autonomous agent adoption.
4. **Refresh stale analyses**: [[cross-source-themes]] and [[key-insights-agentic-landscape]] were refreshed at 33 sources but are now at 42.
5. **Diversify ingests**: Next sources should target non-orchestration gaps — content creation, knowledge quality, or AI writing.

## See Also
- [[wiki-gap-analysis-apr-2026]]
- [[orchestration-tools-compared]]
- [[cross-source-themes]]
- [[multi-agent-orchestration]]
