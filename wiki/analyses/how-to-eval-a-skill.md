---
type: analysis
created: 2026-04-09
updated: 2026-04-09
sources: ["[[evaluating-agent-skills-caparas]]", "[[ten-pillars-agentic-skill-design]]", "[[skills-pipeline-sleestk]]", "[[agent-skills-standard]]", "[[claude-code-docs]]"]
tags: [analysis, evaluation, skills, practical, how-to]
---

# How to Eval a Skill (Practical Guide)

Anthropic's prompt evals measure whether a prompt produces good output. Skill evals are harder because a skill has more surface area: it needs to trigger correctly, execute the right steps, use the right tools, produce the right output, and NOT trigger on the wrong inputs.

This guide maps Anthropic's eval methodology onto skills, drawing from the wiki's sources.

---

## The Key Difference: Prompts vs. Skills

| | Prompt Eval | Skill Eval |
|---|---|---|
| **What you test** | Does this prompt produce good output? | Does this skill trigger, execute, and produce correctly? |
| **Input** | A prompt + expected output | A prompt + context + expected behavior chain |
| **Failure modes** | Bad output | Wrong trigger, wrong steps, wrong tools, bad output, false positive activation |
| **Non-determinism** | Output varies | Trigger, routing, tool selection, AND output all vary |

A skill eval must test the full chain: **routing → activation → execution → output → side effects**.

---

## Step 1: Define Your Eval Cases (Before Writing the Skill)

Create a CSV or YAML file alongside your SKILL.md:

```yaml
# eval.yaml — lives next to SKILL.md
skill: my-skill-name
cases:
  # === SHOULD TRIGGER ===
  - id: explicit-01
    type: positive
    prompt: "Use my-skill to process this data"
    expect:
      triggered: true
      output_contains: ["## Summary", "## Recommendations"]
      files_created: ["output/report.md"]

  - id: implicit-01
    type: positive
    prompt: "I need to analyze this CSV and give me insights"
    expect:
      triggered: true
      output_contains: ["## Summary"]

  - id: context-01
    type: positive
    prompt: "Take a look at this spreadsheet and tell me what's interesting"
    expect:
      triggered: true

  # === SHOULD NOT TRIGGER ===
  - id: negative-01
    type: negative
    prompt: "Fix the CSS in my React app"
    expect:
      triggered: false

  - id: negative-02
    type: negative
    prompt: "Write a unit test for the auth module"
    expect:
      triggered: false

  # === EDGE CASES ===
  - id: edge-01
    type: positive
    prompt: "Analyze this" # too vague — should it trigger?
    expect:
      triggered: false  # define your boundary
```

**Minimum viable eval set**: 5 positive + 5 negative + 2 edge cases = 12 cases. The [[evaluating-agent-skills-caparas]] article recommends 20-50, but 12 gets you started.

The negative cases are critical. From the Caparas article: "I've watched skills hijack prompts they were never meant to handle because the description was too broad."

---

## Step 2: Three Tiers of Checks

### Tier 1: Deterministic (run every time, ~$0)

These are binary pass/fail checks on the trace:

```python
def eval_skill_run(trace, case):
    results = {}

    # Did the skill trigger (or correctly NOT trigger)?
    was_triggered = skill_name_in_trace(trace, case["skill"])
    results["trigger"] = was_triggered == case["expect"]["triggered"]

    # If it shouldn't have triggered, we're done
    if not case["expect"]["triggered"]:
        return results

    # Output contains expected strings?
    output = get_final_output(trace)
    for expected in case["expect"].get("output_contains", []):
        results[f"contains_{expected[:20]}"] = expected in output

    # Expected files created?
    for f in case["expect"].get("files_created", []):
        results[f"file_{f}"] = os.path.exists(f)

    # Token budget?
    tokens = count_tokens_in_trace(trace)
    max_tokens = case["expect"].get("max_tokens", 50000)
    results["token_budget"] = tokens <= max_tokens

    # Command count (thrashing detection)?
    cmds = count_commands_in_trace(trace)
    max_cmds = case["expect"].get("max_commands", 20)
    results["no_thrashing"] = cmds <= max_cmds

    return results
```

What this catches: wrong triggers, missing output, missing files, token blowup, thrashing.

### Tier 2: LLM-as-Judge (run on changes, $0.01-0.20/eval)

For qualitative checks that deterministic graders can't catch:

```yaml
rubric:
  criteria:
    follows_conventions: "Output follows the format specified in SKILL.md"
    completeness: "All required sections are present and substantive"
    accuracy: "Claims are supported by the input data"
    no_hallucination: "No information fabricated beyond what the input provides"
  pass_threshold: 70
  judge_model: claude-sonnet  # use a different model family than the skill runs on
  temperature: 0  # minimize judge variance
  runs: 3  # run 3x, take majority vote
```

Mitigations for known biases (from Caparas):
- Use a different model family as judge than the skill uses
- Run 3x minimum, take majority vote
- Randomize option order if comparing outputs
- Use explicit length-agnostic criteria

### Tier 3: Human Review (calibration only)

Run 5-10 cases through human review to calibrate your LLM-as-judge rubric. If the judge disagrees with humans more than 20% of the time, refine the rubric.

---

## Step 3: The pass@k Problem

Skills are non-deterministic. A skill that passes 4 out of 5 runs is very different from one that passes 1 out of 5.

```
pass@k = probability of at least 1 success in k attempts
```

**Minimum**: Run each eval case 3x. Report pass@3.
**Better**: Run 5x. Report pass@5.
**Production**: Run 10x. Report pass@10 and the raw success rate.

A skill with 90% pass@1 has pass@3 ≈ 99.9%. A skill with 60% pass@1 has pass@3 ≈ 93.6%. The difference matters.

---

## Step 4: What to Eval (The Five Surfaces)

A skill has five testable surfaces. Most people only test #5.

| # | Surface | What to check | Tier |
|---|---------|---------------|------|
| 1 | **Routing** | Does the skill trigger on the right prompts? NOT trigger on wrong ones? | Deterministic |
| 2 | **Tool selection** | Does it use the right tools? Avoid unnecessary ones? | Deterministic |
| 3 | **Process** | Does it follow the intended steps in order? | Deterministic |
| 4 | **Side effects** | Files created? APIs called? Git changes? | Deterministic |
| 5 | **Output quality** | Is the output good? Complete? Accurate? | LLM-as-judge |

Most eval effort goes to surface 5 (output quality), but surfaces 1-4 are where skills actually break in production. A skill that produces beautiful output but triggers on the wrong prompts is worse than useless.

---

## Step 5: Integrate Into Your Workflow

### With Claude Code

Claude Code's hook system gives you eval infrastructure for free:

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Task",
      "hooks": [{
        "type": "command",
        "command": "python3 .claude/evals/run_eval.py --trace $CLAUDE_TRACE_FILE"
      }]
    }]
  }
}
```

### With the Agent Skills Standard

Add an `evals/` directory alongside your SKILL.md:

```
my-skill/
├── SKILL.md
├── scripts/
├── references/
└── evals/
    ├── eval.yaml          # test cases
    ├── rubric.yaml        # LLM-as-judge criteria
    └── run_eval.py        # eval runner
```

This follows the [[skills-pipeline-sleestk]] pattern of shipping test prompts inline with the skill, but extends it with negative controls and deterministic checks.

### CI/CD

```yaml
# In your GitHub Actions workflow
- name: Run skill evals
  run: |
    python3 evals/run_eval.py --cases evals/eval.yaml --runs 3
    # Fail the build if pass@3 < 100% on deterministic checks
    # Warn if LLM-as-judge score < 70%
```

---

## Step 6: The Eval Lifecycle

```
Write eval cases (Step 1)
    ↓
Write the skill
    ↓
Run Tier 1 (deterministic) — fix until green
    ↓
Run Tier 2 (LLM-as-judge) — refine skill until scores pass
    ↓
Calibrate with Tier 3 (human review) — adjust rubric
    ↓
Ship
    ↓
Production failure → add as new eval case → loop
```

The eval set is a living document. Every production failure becomes a new test case. Over time, your eval set becomes the most valuable artifact — more valuable than the skill itself, because it encodes everything you've learned about how the skill can fail.

---

## What Anthropic's Prompt Eval Framework Adds

Anthropic's eval methodology (referenced by Caparas) contributes three ideas that apply directly to skills:

1. **Evals before building**: Write the eval cases before writing the skill. This forces you to define success concretely. Same as TDD for code.
2. **Negative controls are non-negotiable**: If you don't test what should NOT trigger, you'll discover false positives in production.
3. **The best eval is one that actually gets run**: A $0 deterministic check on every commit beats a $5 human review that happens quarterly.

---

## Current Gap

No tool in this wiki provides an integrated skill eval pipeline. The pieces exist:
- [[claude-code]]: 25+ hook events for observability
- [[agent-skills-standard]]: Directory structure supports an `evals/` directory
- [[skills-pipeline-sleestk]]: Inline test prompts as precedent
- [[evaluating-agent-skills-caparas]]: Three-tier methodology with economics

But no one has assembled them into a turnkey `skills-eval` tool. This is the biggest opportunity in the ecosystem (see [[cross-source-themes]], Theme 7).

## See Also
- [[skill-evaluation]]
- [[evaluating-agent-skills-caparas]]
- [[agent-skills-standard]]
- [[ten-pillars-agentic-skill-design]]
- [[cross-source-themes]]
