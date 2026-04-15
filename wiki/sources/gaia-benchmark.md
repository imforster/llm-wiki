---
type: source
created: 2026-04-14
updated: 2026-04-14
origin: llm
tags: [benchmark, evaluation, general-ai, reasoning, tool-use, multimodal]
---

# GAIA: A Benchmark for General AI Assistants

[Original](https://arxiv.org/abs/2311.12983) | [Raw](../../raw/llm/gaia-benchmark.md)

Benchmark by Mialon et al. (Meta, Hugging Face) for evaluating AI assistants on real-world tasks requiring reasoning, tool use, web browsing, and multimodal understanding. Unlike code-focused benchmarks, GAIA measures generalized intelligence.

## Dataset

466 human-annotated questions across three difficulty levels:
- **Level 1**: ≤5 steps, generally no tools
- **Level 2**: moderate tool use, multiple steps
- **Level 3**: arbitrarily long action sequences, any number of tools

Evaluation via exact string match — cheap and unambiguous.

## Performance Gap

- Non-expert humans: ~92% success rate
- AI models (initial): <50% on easiest tasks

The inverse of most recent benchmarks where AI approaches human scores. GAIA tasks are easy for humans but hard for AI — testing fundamental abilities, not specialized knowledge.

## Key Design Principles

- Simple to verify but hard to solve
- Real-world grounding (actual assistant use cases)
- Tool-use required, not just language understanding
- No simulated environments needed (unlike [[agentbench]])

## Limitations

Data contamination risk, string matching may miss valid phrasings, web-dependent questions may break over time.

## See Also
- [[agent-benchmarks]]
- [[skill-evaluation]]
- [[agentbench]]
