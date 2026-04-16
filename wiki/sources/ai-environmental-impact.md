---
type: source
created: 2026-04-15
updated: 2026-04-15
origin: llm
tags: [environment, energy, carbon, water, sustainability, benchmarks]
---

# How Hungry is AI? Energy, Water, and Carbon Footprint of LLM Inference

[Original](https://arxiv.org/html/2505.09598v1) | [Raw](../../raw/llm/ai-environmental-impact.md)

Academic paper (Jegham et al., University of Rhode Island, May 2025) benchmarking environmental footprint across 30 models. First infrastructure-aware, prompt-level sustainability benchmark. Fills the wiki's environmental impact gap.

## Key Numbers

- o3/DeepSeek-R1: >33 Wh per long prompt — 70× GPT-4.1 nano
- Claude 3.7 Sonnet: highest eco-efficiency (DEA 0.886)
- GPT-4o annual (2025): electricity of 35,000 US homes, water for 1.2M people, Chicago-sized forest to offset carbon
- Inference = up to 90% of model's lifetime energy (not training)
- Reasoning models use 8× more tokens → 8× more energy

## Infrastructure > Model Size

GPT-4o mini (smaller) consumes ~20% MORE energy than GPT-4o on long queries — runs on older A100 vs H100/H200. Deployment infrastructure can overshadow model size.

## Jevons Paradox

Per-query efficiency improving, but total usage expanding faster. Agentic revolution could increase energy/carbon 10,000-fold. Efficiency gains enable more usage, not less.

## See Also
- [[agent-cost-economics]]
- [[cost-optimization-guide]]
