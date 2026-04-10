---
type: source
created: 2026-04-09
updated: 2026-04-09
sources: []
tags: [evaluation, tool, open-source, promptfoo, openai]
---

# Promptfoo: LLM Evals & Red Teaming

[Original](https://github.com/promptfoo/promptfoo) | [Docs](https://www.promptfoo.dev/docs/) | [Raw](../../raw/llm/promptfoo-readme.md)

## Summary

Open-source CLI and library for evaluating and red-teaming LLM apps. Now part of OpenAI. MIT licensed. The closest thing to a turnkey skill eval tool — YAML-based test cases, CI/CD integration, model comparison, and red teaming. Powers LLM apps serving 10M+ users in production.

## Key Takeaways

- **Developer-first**: Fast, with live reload and caching. Runs 100% locally — prompts never leave your machine.
- **YAML-based test cases**: Define inputs, expected outputs, and grading criteria in YAML. Directly maps to the `eval.yaml` format proposed in [[how-to-eval-a-skill]].
- **Multiple grading methods**: Exact match, contains, regex, LLM-as-judge, custom functions. Covers both deterministic (Tier 1) and LLM-graded (Tier 2) evaluation.
- **CI/CD integration**: Run evals in GitHub Actions, block merges on failures. This is the "eval on every commit" pattern from [[evaluating-agent-skills-caparas]].
- **Red teaming**: Vulnerability scanning for prompt injection, jailbreaks, and other attacks. Relevant to [[ten-pillars-agentic-skill-design]] Pillar 6 (security).
- **Model comparison**: Side-by-side comparison across providers (OpenAI, Anthropic, Azure, Bedrock, Ollama). Useful for the per-pattern model mapping that [[fabric]] supports.
- **Now part of OpenAI**: Acquired but remains open source and MIT licensed.

## Connections

- **[[skill-evaluation]]**: Promptfoo is the most practical tool for implementing the three-tier eval framework. Its YAML test cases + CI/CD integration + LLM-as-judge support covers Tiers 1 and 2.
- **[[how-to-eval-a-skill]]**: The `eval.yaml` format we proposed could be implemented directly in Promptfoo's YAML config format.
- **[[agent-skills-standard]]**: An `evals/` directory in the skill structure could contain Promptfoo config files, making skills self-evaluating.

## See Also
- [[skill-evaluation]]
- [[how-to-eval-a-skill]]
- [[evaluating-agent-skills-caparas]]
- [[agent-skills-standard]]
