# GAIA: A Benchmark for General AI Assistants

- **Authors**: Mialon, Fourrier, Swift, Wolf, LeCun, Scialom (Meta, Hugging Face)
- **Source**: https://arxiv.org/abs/2311.12983
- **Leaderboard**: https://huggingface.co/spaces/gaia-benchmark/leaderboard
- **Dataset**: https://huggingface.co/datasets/gaia-benchmark/GAIA
- **Date**: November 2023 (paper), ongoing leaderboard
- **Type**: Benchmark for general AI assistant evaluation

## What It Is

GAIA evaluates AI assistants on real-world tasks requiring reasoning, multi-modality handling, web browsing, and tool-use proficiency. Unlike task-specific benchmarks (GLUE for NLP, ImageNet for vision), GAIA measures generalized intelligence across multiple domains.

If solved, it would represent a milestone in AI research — a step toward evaluating true artificial general intelligence.

## Dataset

466 human-annotated questions. Each requires multiple reasoning steps. Many require:
- Tool use (web browser, code interpreter)
- Multi-modal input (images, videos, Excel sheets)

Tasks cover daily personal tasks, science, and general knowledge.

## Three Difficulty Levels

- **Level 1**: Generally no tools, ≤5 steps
- **Level 2**: Moderate tool use, multiple steps
- **Level 3**: Arbitrarily long sequences of actions, any number of tools

## Evaluation Method

Each task has a unique short answer (a few words or numbers). Verified via exact string match — cheap and unambiguous to evaluate.

- 300 test tasks (answers withheld, public leaderboard)
- 166 development tasks (answers included)

Unlike AgentBench, GAIA does NOT require simulated environments — significantly lower evaluation cost.

## Performance

Non-expert humans: ~92% average success rate (tasks are easy for humans, albeit tedious).

AI models (as of initial release): <50% on easiest tasks, worse on harder ones. Significant gap between human and AI performance — the inverse of many recent benchmarks where AI approaches or exceeds human scores.

## Key Design Principles

- Questions require fundamental abilities, not specialized knowledge
- Simple to verify (short text answers) but hard to solve (multi-step reasoning)
- Real-world grounding — tasks reflect actual assistant use cases
- Tool-use required — not just language understanding

## Limitations (Acknowledged by Authors)

- **Data contamination risk**: Relatively easy for humans to solve all tasks (~17 min max per task) and use for training
- **String matching may fail**: Some questions may have valid alternative phrasings
- **Reliance on external sources**: Web-dependent questions may break as sources change over time
- **Limited model coverage**: Initial leaderboard mostly GPT-family models

## Why It Matters for Evaluation

- Tests the full stack of assistant capabilities (reasoning + tools + multimodality)
- Human baseline provides clear target (92%)
- Cheap to evaluate (no simulated environments needed)
- Difficulty levels allow tracking progress across capability tiers
- Complements code-focused benchmarks (SWE-bench, HumanEval) with broader assistant evaluation

## References

- Paper: arXiv:2311.12983 (Mialon et al., 2023)
- Related: AgentBench (arXiv:2308.03688), GPQA (arXiv:2311.12022)
