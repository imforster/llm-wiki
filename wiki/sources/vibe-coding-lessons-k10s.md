---
type: source
created: 2026-05-12
updated: 2026-05-12
origin: llm
sources: []
tags: [vibe-coding, ai-coding, anti-patterns, architecture, claude-code]
---

# I'm Going Back to Writing Code by Hand

[Original](https://blog.k10s.dev/im-going-back-to-writing-code-by-hand/?utm_source=tldrdev) | [Raw](../../raw/llm/vibe-coding-lessons-k10s.md)

**Author:** shvbsle (k10s.dev)
**Published:** 2026-05-09

## Summary

A developer vibe-coded a GPU-aware Kubernetes TUI (k10s) for 7 months using [[claude-code]], then archived the entire codebase and started over. The project grew from a focused GPU dashboard to a bloated k9s clone because AI-generated velocity made every feature feel "free." The resulting 1,690-line god object with 110 switch/case branches became unmaintainable. The post extracts **five tenets** — hard-won lessons about what AI gets wrong when projects grow complex.

Core thesis: **AI writes features, not architecture. The longer you let it drive without constraints, the worse the wreckage gets.**

## The Five Tenets

### Tenet 1: AI Builds Features, Not Architecture

Each feature was implemented in isolation — "make this work right now" — without awareness of 49 other features sharing state. Nine manual `= nil` cleanup assignments scattered across the file. Miss one → ghost data from previous views.

**Fix:** Write architecture yourself before any code. Put invariants in CLAUDE.md:
- Each view implements the View trait. Views do NOT access other views' state.
- Adding a new view MUST NOT require modifying existing views.
- The App struct is a thin router — navigation and dispatch only.

### Tenet 2: The God Object Is the Default AI Artifact

AI gravitates toward single-struct-holds-everything because it satisfies the immediate prompt with minimal ceremony. Result: one keybinding (`s`) meant three different things depending on view state. 20+ occurrences of string-comparison type discrimination in one file.

**Fix:** State ownership rules in CLAUDE.md:
- NEVER add fields to the App struct for view-specific state
- Each view declares its own key bindings
- If your change requires modifying existing views, stop and ask

### Tenet 3: Velocity Illusion Widens Your Scope

Vibe-coding makes everything feel cheap. The developer went from "GPU dashboard for cluster operators" to "general-purpose Kubernetes TUI for everyone" because each feature took one session. But: **infinite line budget ≠ infinite complexity budget.**

**Fix:** Explicit scope boundary in CLAUDE.md:
- Define who you're NOT building for
- Reject features that don't serve the core audience
- Say no in advance, before the velocity high convinces you to say yes

### Tenet 4: Positional Data Is a Time Bomb

All Kubernetes resources were flattened to `[]string`. Column identity was purely positional (`ra[3]` = Alloc). Add a column → every sort, conditional render, and accessor silently breaks. Compiler can't help because it's all strings.

**Fix:** Never flatten structured data into positional arrays. All data flows as typed structs until the render() call. Sort functions operate on named fields, never indices.

### Tenet 5: AI Doesn't Own State Transitions

A closure mutated Model fields from inside a goroutine while `View()` read the same fields on the main goroutine. No lock. Textbook data race that worked 99% of the time.

**Fix:** Background tasks NEVER mutate UI state directly. They send typed messages through a channel. Only the main event loop applies mutations. `render()`/`view()` is a pure function.

## Meta-Insight: CLAUDE.md as Architecture Enforcement

Every tenet's fix is the same pattern: **write the constraint in CLAUDE.md so the AI sees it on every prompt.** The AI will follow rules if you write them down — it just won't invent them for you. The developer's job is to make the correct path also the shortest path.

## Connections

- Validates [[context-management]] — CLAUDE.md as persistent architectural constraint
- Extends [[agentic-ux-patterns]] — the "Autonomy Dial" applied to coding: human sets architecture, AI implements within bounds
- Connects to [[claude-code-token-optimization]] — CLAUDE.md sizing (keep it lean but include invariants)
- Validates [[agent-skills-standard]] — skills need scope boundaries (Pillar 1: Scope/SRP)
- Connects to [[ten-pillars-agentic-skill-design]] — Tenet 3 is Pillar 1 (scope), Tenet 1 is Pillar 4 (context)
- Potential new concept: [[vibe-coding]] — the practice and its failure modes

## Key Quotes

> "AI writes features, not architecture. The longer you let it drive without constraints, the worse the wreckage gets."

> "You have infinite LINE budget. But you have the same finite complexity budget as always."

> "The AI will follow these if you write them down. It just won't invent them for you."

## See Also
- [[claude-code]]
- [[context-management]]
- [[agent-cost-economics]]
- [[agentic-ux-patterns]]
- [[ten-pillars-agentic-skill-design]]
