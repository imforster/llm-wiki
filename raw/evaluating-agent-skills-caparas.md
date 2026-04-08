# How to Evaluate AI Agent Skills Without Relying on Vibes

Source: Article by JP Caparas
Retrieved: 2026-04-08

A practical, platform-agnostic guide to skill evaluation, from first test case to production pipeline. Deeply indebted to OpenAI's guide "Testing Agent Skills Systematically with Evals".

## Core Argument

"It feels better" isn't good enough. We need proof. We've built increasingly powerful AI agents, but our ability to measure them hasn't kept pace. As Andrej Karpathy put it: "LLM evaluations are notoriously difficult. The eval is often harder than the task itself."

## Industry Convergence on Skill Format

Despite the fragmented AI landscape, the industry has quietly converged on a common format (JSON Schema variants):
- OpenAI (Functions/Tools): JSON Schema with name, description, parameters
- Anthropic Claude: JSON with name, description, input_schema
- Google Gemini: Protocol buffer-style function declarations
- LangChain: Python decorators/Tool objects compiling to same structure
- MCP: Open standard for tools, resources, prompts

## Human vs AI Performance Gap

- Coding tasks (SWE-bench Verified): agents ~74%, humans ~90%
- Interactive desktop tasks (OSWorld): agents ~22%, humans ~72%
- The gap isn't uniform — evaluation helps you understand where your specific skills sit

## Define Success Before Writing the Skill

Four categories of success criteria:
1. Outcome goals: Did the task complete? Is the output correct?
2. Process goals: Did the agent invoke the skill when it should? Follow intended steps?
3. Style goals: Does output follow conventions? Correct formatting?
4. Efficiency goals: No thrashing? Reasonable token usage?

Each criterion should be binary — checkable programmatically, no ambiguity.

## Start Small: Targeted Prompt Set

"50–100 well-chosen examples often outperform thousands of poorly chosen ones." — Anthropic Engineering

For a single skill, 20–50 prompts is enough. Include:
- Explicit invocation (names the skill directly)
- Implicit invocation (describes what skill does without naming it)
- Contextual invocation (realistic, slightly noisy prompt)
- Negative controls (should NOT trigger the skill)

Negative controls are critical — catch false positives where skill activates too eagerly.

## Three Tiers of Evaluation

### Tier 1: Deterministic Graders (first line of defence)
- Command execution checks
- File creation verification
- Sequence verification
- Output format matching
- Cost: ~$0. Run on every commit.

### Tier 2: LLM-as-Judge (qualitative evaluation)
- Use LLM to grade outputs against a rubric
- Known pitfalls: position bias, verbosity bias, self-preference, inconsistency
- GPT-4 class models achieve 70–85% agreement with human evaluators
- Cost: $0.01–0.20 per eval. Run on PRs or nightly.

### Tier 3: Human Review
- For calibration, edge cases, high-stakes decisions
- Cost: $0.50–5.00 per eval. Use sparingly.

"The best eval is one that actually gets run." — Anthropic Engineering

## Evaluation Economics

At 1,000 evaluations/day:
- Deterministic only: ~$0
- LLM-as-judge at $0.10 each: $100/day ($3,000/month)
- Human at $2.00 each: $2,000/day ($60,000/month)

Build evaluation budgets from day one.

## Extending Evals as Skills Mature

- Command count and thrashing detection
- Token budget monitoring
- Build and runtime checks (actually run the build)
- Repository cleanliness
- CI/CD integration

Tools: LangSmith, Braintrust, Promptfoo, Arize Phoenix, DeepEval

## Common Mistakes

1. Testing only happy paths (agents fail on edge cases)
2. Single-run evaluations (agents are non-deterministic; use pass@k, run 5-10x minimum)
3. Overfitting to benchmarks (Goodhart's Law)
4. Ignoring evaluation costs
5. Static evaluation sets (add production failures continuously)
6. Evaluating in isolation (skills operate within systems)

## References

- Testing Agent Skills Systematically with Evals — OpenAI
- Demystifying Evals for AI Agents — Anthropic
- LangSmith, Braintrust, Promptfoo, MT-Bench, SWE-bench, GAIA
