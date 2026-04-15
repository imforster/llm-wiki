---
type: source
created: 2026-04-14
updated: 2026-04-14
origin: llm
tags: [benchmark, evaluation, agents, multi-turn, interactive, ICLR]
---

# AgentBench: Evaluating LLMs as Agents

[Original](https://arxiv.org/abs/2308.03688) | [Raw](../../raw/llm/agentbench.md)

Multi-dimensional benchmark by Liu et al. (Tsinghua, ICLR 2024) evaluating LLMs as autonomous agents across eight interactive environments. The broadest agent benchmark in the wiki — tests decision-making, not just generation.

## Eight Environments

1. Operating System (shell commands)
2. Database (SQL)
3. Knowledge Graph (structured traversal)
4. Digital Card Game (strategic decisions)
5. Lateral Thinking Puzzles (creative reasoning)
6. House-Holding (embodied task planning)
7. Web Shopping (e-commerce navigation)
8. Web Browsing (information extraction)

5-50 turns per problem. Multi-turn interactive, not single-shot.

## Key Findings

- Top commercial LLMs (GPT-4 class) strong as agents
- Significant gap between commercial and open-source (even 70B models)
- Performance varies across environments — strength in one ≠ strength in all

## General AgentBench (2025)

Substantial performance degradation moving from domain-specific to general-agent settings. Models that look good on narrow benchmarks struggle with breadth.

## Benchmark Landscape Comparison

| Benchmark | Focus | Format |
|-----------|-------|--------|
| [[humaneval-benchmark]] | Code generation | Single-turn, 164 problems |
| [[swe-bench]] | Software engineering | Patch generation |
| [[gaia-benchmark]] | General AI assistant | Multi-step Q&A |
| [[agentbench]] | Agent decision-making | Multi-turn, 8 environments |

## See Also
- [[agent-benchmarks]]
- [[skill-evaluation]]
- [[multi-agent-orchestration]]
