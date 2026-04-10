---
type: source
created: 2026-04-09
updated: 2026-04-09
sources: []
tags: [evaluation, anthropic, methodology, evals, testing]
---

# Anthropic: Define Success Criteria and Build Evaluations

[Original](https://docs.anthropic.com/en/docs/build-with-claude/develop-tests) | [Raw](../../raw/llm/anthropic-eval-guide.md)

## Summary

[[anthropic]]'s canonical guide to building evaluations for LLM applications. Establishes the methodology that the Caparas article and the broader eval ecosystem builds on. Covers success criteria design, eval types (exact match, cosine similarity, LLM-graded), and the principle that automated volume beats hand-graded quality.

## Key Takeaways

- **Success criteria must be SMART**: Specific, Measurable, Achievable, Relevant. "The model should classify sentiments well" is bad. "F1 score of at least 0.85 on 10,000 diverse tweets" is good.
- **Common criteria dimensions**: Task fidelity, consistency, relevance/coherence, tone/style, privacy preservation, context utilization, latency, price. Most use cases need multidimensional evaluation.
- **Three eval design principles**: (1) Be task-specific — mirror real-world distribution including edge cases. (2) Automate when possible — structure for automated grading. (3) Prioritize volume over quality — more questions with automated grading beats fewer with human grading.
- **Eval types by complexity**:
  - Exact match: Binary correct/incorrect. Best for categorical tasks.
  - Cosine similarity: Semantic similarity between embeddings. Best for consistency testing.
  - LLM-as-judge: Use a model to grade another model's output against a rubric.
- **Even "hazy" topics can be quantified**: Ethics and safety can be measured — e.g., "less than 0.1% of outputs flagged for toxicity out of 10,000 trials."
- **Edge cases matter**: Irrelevant input, overly long input, harmful user input, ambiguous cases where even humans disagree.

## Connections

- **[[skill-evaluation]]**: This guide provides the foundational methodology. The three-tier framework (deterministic → LLM-judge → human) from [[evaluating-agent-skills-caparas]] is a direct application of these principles to skills specifically.
- **[[how-to-eval-a-skill]]**: Our practical guide extends Anthropic's prompt eval methodology to the five surfaces of skill evaluation (routing, tool selection, process, side effects, output quality).
- **[[ten-pillars-agentic-skill-design]]**: Pillar 7 (Testing and Validation) is operationalized by this guide's methodology.

## See Also
- [[skill-evaluation]]
- [[evaluating-agent-skills-caparas]]
- [[how-to-eval-a-skill]]
- [[anthropic]]
