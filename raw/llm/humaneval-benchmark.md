# HumanEval: Evaluating Large Language Models Trained on Code

- **Authors**: Mark Chen et al. (OpenAI, 69 researchers)
- **Source**: https://arxiv.org/abs/2107.03374
- **GitHub**: https://github.com/openai/human-eval
- **Leaderboard**: https://evalplus.github.io/leaderboard.html
- **Date**: July 2021 (paper), ongoing leaderboard
- **Type**: Benchmark for code generation evaluation

## What It Is

HumanEval is a benchmark of 164 hand-crafted Python programming problems designed to evaluate AI code generation capabilities. Released alongside OpenAI's Codex model, it introduced the pass@k metric and became the gold standard for measuring AI coding abilities.

## How It Works

Each problem consists of:
- A function signature (name, parameters, return type)
- A docstring explaining the task, often with examples
- Hidden unit tests to verify functional correctness (average 7.7 tests per problem)

Focus is on **functional correctness** — does the code actually work? Not style, efficiency, or best practices.

## The pass@k Metric

- **pass@1**: Probability that a single generated solution is correct
- **pass@10**: Probability that at least one of 10 attempts is correct
- **pass@100**: Probability that at least one of 100 attempts is correct

Acknowledges how programmers actually work — iterate, debug, refine. Generating multiple candidates and selecting the best is a valid capability.

## Performance Evolution

| Year | Model | pass@1 |
|------|-------|--------|
| 2021 | GPT-3 | 0% |
| 2021 | Codex | 28.8% |
| 2022 | Various | 50-60% |
| 2023 | Top models | 70-80% |
| 2024-25 | O1 Preview/Mini | 96.3% |

234% improvement from original Codex to current top models in ~3 years.

## EvalPlus (Enhanced Evaluation)

Adds additional test cases to expose edge cases and corner conditions. Same O1 models drop from 96.3% to 89% on EvalPlus — revealing gap between solving specific problems and robust programming.

Current EvalPlus leaderboard:
- Qwen2.5-Coder-32B-Instruct: 87.2%
- GPT-4o: 87.2%
- DeepSeek-V3: 86.6%
- Claude Sonnet 3.5: 81.7%

## Limitations

- **Contamination risk**: 164 problems widely available since 2021. Models may have encountered them during training. Teaching to the test.
- **Narrow scope**: Simple, self-contained problems solvable in a few lines. Real programming involves large codebases, debugging, ambiguous requirements.
- **Binary evaluation**: pass/fail doesn't account for readability, maintainability, efficiency, security.
- **Python-only**: Core benchmark tied to Python's specific characteristics.
- **Static problem set**: Fixed 164 problems become less useful as models approach perfect scores.
- **Measurement ceiling**: Multiple models at 95%+ — benchmark loses ability to differentiate.

## Spawned Ecosystem

- **EvalPlus**: More rigorous testing with additional test cases
- **HumanEval-X**: Multi-language evaluation (Python, Java, JavaScript, etc.)
- **HumanEval+**: Extended test cases
- **HumanEval-V**: Visual elements / multi-modal

## Key Insight

Models excel at pattern matching and reproducing solutions to familiar problems but struggle with variations requiring deeper understanding. The consistent 7-8 point gap between base and EvalPlus scores across all models reveals this systematic limitation.

## References

- Paper: arXiv:2107.03374 (Chen et al., 2021)
- EvalPlus: https://evalplus.github.io/leaderboard.html
- HumanEval-X: arXiv:2303.17568 (Zheng et al., 2023)
