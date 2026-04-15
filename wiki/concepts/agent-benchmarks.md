---
type: concept
created: 2026-04-14
updated: 2026-04-14
sources: ["[[humaneval-benchmark]]", "[[swe-bench]]", "[[gaia-benchmark]]", "[[agentbench]]"]
tags: [evaluation, benchmarks, testing, code-generation, agents]
---

# Agent Benchmarks

Standardized benchmarks for measuring LLM and agent capabilities. The wiki previously identified evaluation as "the weakest link" ([[key-insights-agentic-landscape]]). These four benchmarks represent the current state of the art across code generation, software engineering, general reasoning, and interactive agent tasks.

## The Benchmark Landscape

| Benchmark | Focus | Scale | Format | Top Score |
|-----------|-------|-------|--------|-----------|
| [[humaneval-benchmark]] | Code generation | 164 Python problems | Single-turn, pass@k | 96.3% (O1) |
| [[swe-bench]] | Software engineering | 2,294 GitHub issues | Patch generation | 74.4% (Claude 4.5 Opus) |
| [[gaia-benchmark]] | General AI assistant | 466 questions | Multi-step Q&A + tools | <50% AI vs 92% human |
| [[agentbench]] | Agent decision-making | 8 environments | Multi-turn interactive | Commercial >> open-source |

## Evolution of Difficulty

The benchmarks form a progression from narrow to broad:

1. **HumanEval** (2021): Can the model write a function? → Largely solved (96%+)
2. **SWE-bench** (2023): Can the model fix a real bug in a real codebase? → Rapidly improving (74%)
3. **GAIA** (2023): Can the model reason across domains with tools? → Still far from human (92% vs <50%)
4. **AgentBench** (2023): Can the model act autonomously across diverse environments? → Commercial models lead, open-source lags

## Key Patterns Across Benchmarks

- **Contamination risk**: all face it. HumanEval most vulnerable (164 fixed problems since 2021).
- **Narrow vs broad**: models that excel on narrow benchmarks (HumanEval) may struggle with breadth (AgentBench General).
- **The last 25%**: SWE-bench's self-driving car analogy — remaining unsolved problems may be disproportionately hard.
- **Human baselines**: GAIA uniquely provides one (92%). Most benchmarks lack clear human comparison.

## What's Still Missing

Per [[skill-evaluation]] and [[how-to-eval-a-skill]]:
- No standard benchmark for **skill-level evaluation** (individual agent capabilities, not whole-model)
- No benchmark for **multi-agent coordination** quality
- No benchmark for **memory/persistence** quality (though LOCOMO from [[mem0-memory-management]] is closest)
- No integrated **cost-per-task** metric alongside accuracy

## Connection to Wiki Eval Framework

The [[skill-evaluation]] three-tier framework (deterministic → LLM-judge → human) and [[how-to-eval-a-skill]] practical guide complement these benchmarks. Benchmarks measure model-level capability; the wiki's eval framework measures skill-level quality in production.

## See Also
- [[skill-evaluation]]
- [[how-to-eval-a-skill]]
- [[promptfoo]]
- [[key-insights-agentic-landscape]]
