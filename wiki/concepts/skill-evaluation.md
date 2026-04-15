---
type: concept
created: 2026-04-08
updated: 2026-04-14
sources: ["[[evaluating-agent-skills-caparas]]", "[[ten-pillars-agentic-skill-design]]", "[[humaneval-benchmark]]", "[[swe-bench]]", "[[gaia-benchmark]]", "[[agentbench]]"]
tags: [evaluation, testing, methodology, economics, benchmarks]
---

# Skill Evaluation

Moving from "it feels better" to "I have proof" when measuring AI agent skill quality.

## The Problem

LLM agents are non-deterministic. Manual testing captures one sample from a distribution. "Vibes-based" evaluation misses regressions, false positives, and edge cases. As Karpathy noted: "The eval is often harder than the task itself."

## Three-Tier Framework

| Tier | Method | Cost | Frequency | Catches |
|------|--------|------|-----------|---------|
| 1 | Deterministic graders | ~$0 | Every commit | Command execution, file existence, sequence, format |
| 2 | LLM-as-judge | $0.01–0.20/eval | PRs, nightly | Code quality, conventions, readability (rubric-based) |
| 3 | Human review | $0.50–5.00/eval | Sparingly | Calibration, edge cases, high-stakes decisions |

"The best eval is one that actually gets run." — Anthropic

## Four Categories of Success Criteria

1. **Outcome**: Did the task complete? Is the output correct?
2. **Process**: Did the agent invoke the right skill? Follow intended steps?
3. **Style**: Does output follow conventions?
4. **Efficiency**: No thrashing? Reasonable token usage?

Every criterion must be binary and programmatically checkable.

## Test Design

- 20–50 prompts per skill minimum
- Include **negative controls** (prompts that should NOT trigger the skill)
- Use **pass@k** metrics (probability of success in k attempts) — run 5–10x minimum
- Feed production failures back into eval sets continuously

## LLM-as-Judge Pitfalls

- Position bias (prefers first/last options)
- Verbosity bias (longer = higher scores)
- Self-preference (models prefer own family's output)
- Inconsistency (same input, different scores across runs)
- GPT-4 class: 70–85% agreement with human evaluators

## What's Missing in the Ecosystem

The [[ten-pillars-agentic-skill-design]] paper explicitly acknowledged "no original controlled study" as a limitation. The [[key-insights-agentic-landscape]] analysis identified evaluation as a top gap. This framework provides the methodology to fill that gap, but no tool in the wiki has fully implemented it yet.

## See Also
- [[ten-pillars-agentic-skill-design]]
- [[agent-skills-standard]]
- [[prompt-engineering-patterns]]
- [[key-insights-agentic-landscape]]
- [[agent-benchmarks]]
- [[promptfoo]]
