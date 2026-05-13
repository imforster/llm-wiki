---
type: concept
created: 2026-05-12
updated: 2026-05-12
sources: ["[[vibe-coding-lessons-k10s]]", "[[claude-code-token-optimization]]"]
tags: [ai-coding, anti-patterns, development-practice]
---

# Vibe Coding

The practice of building software primarily through AI prompting with minimal human code review or architectural oversight. The developer describes features in natural language, the AI generates code, and the developer verifies it compiles and passes the happy path — without deeply reading or understanding the generated code.

## Characteristics

- Extreme velocity on individual features
- Developer stays "out of the loop" on implementation details
- Each feature works in isolation but accumulates hidden coupling
- Feels like 10× speed until complexity budget is exhausted

## Failure Modes (from [[vibe-coding-lessons-k10s]])

1. **God objects** — AI defaults to single-struct-holds-everything because it satisfies the immediate prompt
2. **Scope creep** — velocity illusion makes every feature feel "free," widening scope beyond original intent
3. **Positional data** — AI picks `[]string` over typed structs because it's faster to satisfy the prompt
4. **State transition bugs** — AI generates closures that mutate shared state without synchronization
5. **Feature bleeding** — no view isolation means features interfere with each other as they accumulate

## The Complexity Budget Insight

> "You have infinite LINE budget. But you have the same finite complexity budget as always."

AI can generate unlimited code, but the architecture can only support so many features before it buckles — regardless of how fast they were written. The velocity metric ("you're shipping!") masks the complexity accumulation.

## Mitigation: CLAUDE.md as Guardrails

The primary defense is encoding architectural constraints in persistent context files (CLAUDE.md, AGENTS.md) so the AI sees them on every prompt:
- Architecture invariants (view isolation, state ownership)
- Scope boundaries (who you're NOT building for)
- Data representation rules (typed structs, not positional arrays)
- Concurrency rules (message passing, not shared mutation)

The AI follows rules it can see. It just won't invent them.

## See Also
- [[context-management]]
- [[claude-code]]
- [[agentic-ux-patterns]]
- [[ten-pillars-agentic-skill-design]]
