---
type: source
created: 2026-04-14
updated: 2026-04-14
origin: llm
tags: [benchmark, evaluation, code-generation, pass-at-k]
---

# HumanEval: Evaluating Large Language Models Trained on Code

[Original](https://arxiv.org/abs/2107.03374) | [Raw](../../raw/llm/humaneval-benchmark.md)

The foundational code generation benchmark by Chen et al. (OpenAI, 2021). 164 hand-crafted Python problems. Introduced the pass@k metric that became the standard for measuring AI coding capabilities.

## The pass@k Metric

- **pass@1**: probability single generated solution is correct
- **pass@10/100**: probability at least one of k attempts is correct

Acknowledges how programmers actually work — iterate, debug, refine.

## Performance Evolution (0% → 96.3% in 3 years)

| Year | Model | pass@1 |
|------|-------|--------|
| 2021 | GPT-3 | 0% |
| 2021 | Codex | 28.8% |
| 2023 | Top models | 70-80% |
| 2024-25 | O1 Preview/Mini | 96.3% |

## EvalPlus (Enhanced)

Additional test cases expose edge cases. O1 drops from 96.3% → 89%. The consistent 7-8 point gap across all models reveals systematic limitation: pattern matching works, robust reasoning doesn't.

## Limitations

- **Contamination**: 164 problems widely available since 2021
- **Narrow scope**: simple self-contained problems, not real codebases
- **Binary evaluation**: pass/fail ignores readability, efficiency, security
- **Measurement ceiling**: multiple models at 95%+ — can't differentiate

## Spawned Ecosystem

EvalPlus, HumanEval-X (multi-language), HumanEval+ (extended tests), HumanEval-V (visual/multi-modal).

## See Also
- [[agent-benchmarks]]
- [[skill-evaluation]]
- [[swe-bench]]
