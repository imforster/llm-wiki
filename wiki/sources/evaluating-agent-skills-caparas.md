---
type: source
created: 2026-04-08
updated: 2026-04-08
sources: []
tags: [evaluation, testing, skills, methodology, evals]
---

# How to Evaluate AI Agent Skills Without Relying on Vibes

[Original](../../raw/evaluating-agent-skills-caparas.md)

Author: JP Caparas (building on OpenAI's "Testing Agent Skills Systematically with Evals")

## Summary

A practical guide to moving from "it feels better" to "I have proof" when evaluating AI agent skills. Proposes a three-tier evaluation framework (deterministic → LLM-as-judge → human review) with concrete economics, and argues that the industry's convergence on JSON Schema skill formats makes these principles platform-agnostic.

## Key Takeaways

- **Define success before writing the skill**: Four categories — outcome, process, style, efficiency. Every criterion must be binary and programmatically checkable. This directly complements the [[ten-pillars-agentic-skill-design]] framework (Pillar 7: Testing and Validation).
- **Start small**: 20–50 prompts per skill, including negative controls (prompts that should NOT trigger the skill). "50–100 well-chosen examples often outperform thousands of poorly chosen ones." (Anthropic)
- **Three-tier evaluation economics**:
  - Tier 1 — Deterministic graders: ~$0, run on every commit. Command execution, file existence, sequence, format.
  - Tier 2 — LLM-as-judge: $0.01–0.20/eval, run on PRs/nightly. Rubric-based qualitative scoring. Known biases: position, verbosity, self-preference, inconsistency.
  - Tier 3 — Human review: $0.50–5.00/eval, use sparingly. Calibration and edge cases only.
- **"The best eval is one that actually gets run"**: An expensive eval nobody runs is worthless. A cheap eval on every commit is invaluable.
- **Industry convergence on skill format**: OpenAI, Anthropic, Google, LangChain, [[mcp-protocol]] all use JSON Schema variants. Evaluation principles are portable.
- **Human vs AI gap is non-uniform**: Coding (SWE-bench) ~74% vs ~90% human. Desktop tasks (OSWorld) ~22% vs ~72% human. Evaluation helps you understand where your specific skills sit.
- **Common mistakes**: Testing only happy paths, single-run evals (agents are non-deterministic — use pass@k), overfitting to benchmarks (Goodhart's Law), static eval sets, evaluating in isolation.

## Connections

- **[[ten-pillars-agentic-skill-design]]**: This article operationalizes Pillar 7 (Testing and Validation) with concrete economics and tiered methodology. The Ten Pillars paper acknowledged "no original controlled study" as a limitation — this article provides the framework for how to do those studies.
- **[[agent-skills-standard]]**: The convergence on JSON Schema formats means evaluation tooling can be built once and applied across platforms. The spec's `allowed-tools` field (experimental) could enable deterministic grading of tool usage.
- **[[context-management]]**: Token budget monitoring as an evaluation metric connects to context management strategies. Efficiency goals (no thrashing, reasonable token usage) are measurable proxies for good context management.
- **[[prompt-engineering-patterns]]**: The negative control testing pattern (prompts that should NOT trigger) is a form of adversarial evaluation for skill descriptions and routing.

## See Also
- [[skill-evaluation]]
- [[ten-pillars-agentic-skill-design]]
- [[agent-skills-standard]]
- [[mcp-protocol]]
