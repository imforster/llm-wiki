# SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

- **Authors**: Carlos E. Jimenez et al. (Princeton University)
- **Source**: https://arxiv.org/abs/2310.06770
- **Leaderboard**: https://www.swebench.com/
- **Date**: October 2023 (paper), ongoing leaderboard
- **Type**: Benchmark for real-world software engineering evaluation

## What It Is

SWE-bench evaluates whether AI models can solve real-world software engineering tasks. Instead of testing code generation in isolation, it presents models with actual GitHub issues from popular open-source Python repositories and asks them to produce a patch that resolves the issue and passes the associated test suite.

## How It Works

Each task consists of:
- A GitHub issue description — the natural-language problem statement as written by the original issue author
- A codebase snapshot — the state of the repository at the time the issue was filed
- A gold patch and test suite — the model's output is evaluated by checking whether it passes the same tests used to validate the human-authored fix

Models scored on **% resolved** — fraction of issues where generated patch passes the full test suite. More rigorous than benchmarks that only check if code compiles or passes a single test case.

## Dataset

Original SWE-bench: 2,294 tasks from 12 widely used Python repositories (Django, scikit-learn, sympy, etc.).

## SWE-bench Verified

OpenAI collaborated with the SWE-bench team to create a human-filtered subset of 500 tasks where annotators confirmed:
- Issue description contains enough information to identify the problem
- Test suite reliably validates correct solutions
- Task is not ambiguous or under-specified

SWE-bench Verified is now the standard subset for leaderboard comparisons.

## Current Results (Early 2025)

Bash Only leaderboard (SWE-bench Verified, same shell-based interface):

| Model | % Resolved |
|-------|-----------|
| Claude 4.5 Opus (medium) | 74.40% |
| Gemini 3 Pro Preview | 74.20% |
| Claude 4.5 Sonnet | 70.60% |
| Claude 4 Opus (May 2025) | 67.60% |
| GPT-5 (medium reasoning) | 65.00% |

For context: best scores were ~50% in early 2024. Rapid improvement.

## Important Caveats

- **Curated subset**: SWE-bench Verified filters out ambiguous, under-documented, or hard-to-test issues. Real-world GitHub issues are messier.
- **Single-repo Python focus**: Currently draws from well-maintained Python libraries. Generalization to other languages, less-documented codebases, or proprietary software is open question.
- **No deployment or integration testing**: Tests whether patch passes unit/integration tests, not whether it would be accepted in code review or function correctly at scale.
- **Self-driving car analogy**: Rapid progress on structured benchmarks led many to predict full autonomy was imminent. The remaining 25-30% of unresolved issues — and the much larger space of tasks not captured by the benchmark — may prove disproportionately difficult.

## Why It Matters

- Tests end-to-end problem-solving (reading issue, understanding codebase, writing correct fix) rather than narrow code completion
- One of the more meaningful benchmarks for evaluating practical coding ability
- Rough barometer for how quickly AI coding capabilities are improving
- Reality check on what "AI can code" actually means today

## References

- Paper: arXiv:2310.06770 (Jimenez et al., 2024)
- SWE-bench Verified: https://openai.com/index/introducing-swe-bench-verified/
