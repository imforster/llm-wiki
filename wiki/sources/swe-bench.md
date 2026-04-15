---
type: source
created: 2026-04-14
updated: 2026-04-14
origin: llm
tags: [benchmark, evaluation, software-engineering, coding, github]
---

# SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

[Original](https://arxiv.org/abs/2310.06770) | [Raw](../../raw/llm/swe-bench.md)

Benchmark by Jimenez et al. (Princeton) evaluating whether AI models can solve real-world software engineering tasks — actual GitHub issues from popular Python repositories. The most meaningful benchmark for practical coding ability in the wiki.

## How It Works

Each task: GitHub issue description + codebase snapshot + gold patch and test suite. Models scored on **% resolved** — fraction where generated patch passes the full test suite.

- Original dataset: 2,294 tasks from 12 Python repos (Django, scikit-learn, sympy)
- **SWE-bench Verified**: human-filtered subset of 500 tasks (now the standard)

## Current Results (Early 2025, Verified)

| Model | % Resolved |
|-------|-----------|
| Claude 4.5 Opus (medium) | 74.40% |
| Gemini 3 Pro Preview | 74.20% |
| Claude 4.5 Sonnet | 70.60% |
| GPT-5 (medium reasoning) | 65.00% |

Best scores were ~50% in early 2024. Rapid improvement trajectory.

## Caveats

- Curated subset filters out messy real-world issues
- Single-repo Python focus — generalization to other languages unknown
- No deployment/integration testing — only unit/integration test pass
- Self-driving car analogy: remaining 25-30% may be disproportionately difficult

## See Also
- [[agent-benchmarks]]
- [[skill-evaluation]]
- [[humaneval-benchmark]]
