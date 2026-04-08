---
type: concept
created: 2026-04-08
updated: 2026-04-08
sources: ["[[ten-pillars-agentic-skill-design]]"]
tags: [prompting, cot, react, reflexion, patterns]
---

# Prompt Engineering Patterns

Structured techniques for crafting prompts within agentic skills, drawn from research and the [[ten-pillars-agentic-skill-design]] framework.

## Chain of Thought (CoT)

Structure prompts to encourage step-by-step reasoning. Break complex tasks into numbered steps. Wei et al. (2022).

## ReAct Pattern

Integrate reasoning and acting in a loop (Yao et al., 2023):
```
Thought: [reasoning about what to do]
Action: [specific action to take]
Observation: [result of the action]
... (repeat until task complete)
```

## Self-Reflection (Reflexion)

Enable agents to learn from mistakes (Shinn & Labash, 2023):
- Include feedback loops in skill workflows
- Store successful patterns in memory
- Adjust strategies based on outcomes

## Tree of Thoughts

Deliberate problem solving by exploring multiple reasoning paths (Yao et al., 2023). Useful for complex architectural decisions.

## Key Elements for Skill Prompts

- System messages defining agent roles and expertise
- Stepwise instructions to guide reasoning
- Controlled temperature and token limits
- Few-shot examples for complex tasks
- Clear success/failure criteria

## Anti-Patterns

- **Overly generic prompts**: Vague instructions → inconsistent outputs. Use specific, structured prompts with examples.
- **Ignoring token limits**: Skills exceed context windows. Implement chunking and [[context-management]].
- **Unnecessary reasoning steps**: LLMs often overthink. Implement trajectory monitoring and early stopping.

## Composable Strategies (Fabric)

[[fabric]] implements these patterns as composable JSON strategies applied on top of any pattern, cleanly separating *what* to do from *how* to reason:

| Strategy | Pattern |
|----------|---------|
| `cot` | Chain-of-Thought |
| `tot` | Tree-of-Thought |
| `reflexion` | Reflexion |
| `self-refine` | Self-Refinement |
| `cod` | Chain-of-Draft (minimal notes) |
| `aot` | Atom-of-Thought (atomic sub-problems) |
| `ltm` | Least-to-Most |
| `self-consistent` | Multiple paths with consensus |

## See Also
- [[ten-pillars-agentic-skill-design]]
- [[context-management]]
- [[agent-skills-standard]]
