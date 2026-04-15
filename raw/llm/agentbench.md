# AgentBench: Evaluating LLMs as Agents

- **Authors**: Liu et al. (Tsinghua University — THUDM)
- **Source**: https://arxiv.org/abs/2308.03688
- **GitHub**: https://github.com/THUDM/AgentBench
- **Venue**: ICLR 2024
- **Date**: August 2023 (paper), ICLR 2024 (accepted)
- **Type**: Multi-dimensional benchmark for LLM-as-Agent evaluation

## What It Is

AgentBench is a comprehensive benchmark that evaluates LLMs as autonomous agents across eight distinct interactive environments. It assesses reasoning and decision-making abilities in multi-turn, open-ended settings — not just single-turn Q&A.

## Eight Environments

1. **Operating System** — shell command execution, file manipulation
2. **Database** — SQL queries, data retrieval and manipulation
3. **Knowledge Graph** — structured knowledge traversal and reasoning
4. **Digital Card Game** — strategic decision-making under uncertainty
5. **Lateral Thinking Puzzles** — creative reasoning and deduction
6. **House-Holding** — embodied task planning in simulated environments
7. **Web Shopping** — navigating e-commerce sites, finding and purchasing items
8. **Web Browsing** — general web navigation and information extraction

Spans code, game, and web-grounded tasks. Estimated solving turns per problem: 5 to 50.

## Evaluation

- Multi-turn interactive challenges (not single-shot)
- Metrics: success rate, overall reward, F1 score (varies by environment)
- Tests planning, reasoning, and decision-making holistically

## Key Findings

Tested 29 API-based and open-source LLMs:
- Top commercial LLMs (GPT-4 class) show strong ability as agents in complex environments
- Significant performance disparity between commercial models and open-source competitors (even those up to 70B parameters)
- Performance varies significantly across environments — models strong in one area may be weak in another

## General AgentBench (2025 Extension)

A newer version studies test-time scaling behaviors:
- **Sequential scaling**: iterative interaction (more turns)
- **Parallel scaling**: sampling multiple trajectories

Key finding: substantial performance degradation when moving from domain-specific evaluations to general-agent settings. Models that look good on narrow benchmarks may struggle with breadth.

## Why It Matters

- **Breadth**: 8 environments test diverse agent capabilities, not just coding or Q&A
- **Multi-turn**: Reflects real agent workflows (5-50 turn interactions)
- **Reveals gaps**: Exposes the difference between commercial and open-source agent capabilities
- **Practical**: Environments mirror real-world tasks (OS, databases, web, shopping)
- **Complements other benchmarks**: Where SWE-bench tests coding and GAIA tests general reasoning, AgentBench tests interactive decision-making across domains

## Comparison to Other Benchmarks

| Benchmark | Focus | Format | Environments |
|-----------|-------|--------|-------------|
| HumanEval | Code generation | Single-turn, 164 problems | Python only |
| SWE-bench | Software engineering | Single-turn patch generation | GitHub repos |
| GAIA | General AI assistant | Multi-step Q&A | Real-world questions |
| AgentBench | Agent decision-making | Multi-turn interactive | 8 diverse environments |

## References

- Paper: arXiv:2308.03688 (Liu et al., 2023)
- ICLR 2024: https://iclr.cc/virtual/2024/poster/17388
- General AgentBench: arXiv:2602.18998 (2025)
