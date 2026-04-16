# How Hungry is AI? Benchmarking Energy, Water, and Carbon Footprint of LLM Inference

- **Authors**: Nidhal Jegham, Marwan Abdelatti, Lassad Elmoubarki, Abdeltawab Hendawi
- **Source**: https://arxiv.org/html/2505.09598v1
- **Date**: May 2025
- **Type**: Academic paper (arXiv, University of Rhode Island)

## Key Findings

- o3 and DeepSeek-R1: most energy-intensive, >33 Wh per long prompt — 70× GPT-4.1 nano consumption
- Claude 3.7 Sonnet: highest eco-efficiency (DEA score 0.886)
- Single short GPT-4o query: 0.43 Wh. Scaled to 700M queries/day → annual impact = 35,000 US homes electricity, 1.2M people's drinking water, Chicago-sized forest to offset carbon
- Inference = up to 90% of model's lifetime energy use (not training)

## Energy Per Model (Medium Prompt, 1K input + 1K output)

| Model | Energy (Wh) |
|-------|------------|
| GPT-4.1 nano | 0.45 |
| GPT-4o | 1.79 |
| Claude 3.7 Sonnet | ~2.5 |
| GPT-4.1 | 2.51 |
| LLaMA-3.3 70B | 0.86 |
| DeepSeek-R1 | 33.6 |
| o3 | 39.2 |

## Eco-Efficiency Rankings (Cross-Efficiency DEA)

| Model | Score | Notes |
|-------|-------|-------|
| Claude 3.7 Sonnet | 0.886 | Highest — strong reasoning + efficient infrastructure |
| o4-mini (high) | 0.867 | Good reasoning at lower cost |
| GPT-4.1 mini | 0.802 | Strong balance |
| GPT-4o | 0.762 | Current default, efficient |
| DeepSeek-R1 | 0.058 | Lowest — high capability but disproportionate resource use |
| DeepSeek-V3 | 0.060 | Infrastructure inefficiencies |

## Carbon and Water Per Query

- Average AI query: 0.03-1.14 grams CO₂e (range depends on model + infrastructure)
- 1M tokens on current hardware: 200-500 Wh, producing 40-100g CO₂ (UK grid)
- Reasoning models (o3, DeepSeek-R1): 8× more tokens → 8× more energy per prompt
- GPT-4o annual (2025 est): 138,125-163,441 tons CO₂e, 1.3-1.6M kiloliters water

## Jevons Paradox

Per-query efficiency improving, but total usage expanding far faster. Efficiency gains don't reduce overall impact — they enable more usage. Agentic revolution could increase energy/carbon by 10,000-fold over current usage.

## Infrastructure Matters More Than Model Size

GPT-4o mini (smaller model) consumes ~20% MORE energy than GPT-4o on long queries — because it runs on older A100 hardware vs H100/H200. DeepSeek models have high footprints partly due to data center inefficiencies (higher PUE, suboptimal cooling).

## Policy Implications

- Thresholds on permissible environmental footprint per inference
- Transparency: per-inference energy, water, carbon reporting
- Batching strategies: batch size 4→8 reduces energy ~45%, 8→16 another ~43%
- Dielectric liquid cooling could eliminate water use in data centers
