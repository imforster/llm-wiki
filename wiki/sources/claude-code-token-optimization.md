---
type: source
created: 2026-05-12
updated: 2026-05-12
origin: llm
sources: []
tags: [token-optimization, claude-code, cost, context-management]
---

# 7 Practical Ways to Reduce Claude Code Token Usage

[Original](https://www.kdnuggets.com/7-practical-ways-to-reduce-claude-code-token-usage) | [Raw](../../raw/llm/claude-code-token-optimization.md)

**Author:** Kanwal Mehreen (KDNuggets)
**Published:** 2026-05-03

## Summary

Practical guide to reducing [[claude-code]] token costs. The core insight: **you're not paying for the prompt you typed — you're paying for the entire context window**, which includes prior messages, files read, tool outputs, and persistent files like `CLAUDE.md`. Most token waste comes from messy context, not bad prompting.

## Key Takeaways

### 1. Switch Models by Task Complexity
- **Opus** (5× Sonnet cost): complex multi-file architecture, gnarly debugging
- **Sonnet**: day-to-day — tests, edits, explaining, refactoring
- **Haiku**: mechanical — lookups, formatting, renaming, repetitive tasks
- Use `/effort` to reduce thinking budget on straightforward tasks

### 2. Keep CLAUDE.md Small and Useful
- CLAUDE.md loads on **every single turn** — a 5,000-token file costs 5,000 tokens per message
- Put stable instructions: test commands, package manager, formatting rules, architectural constraints, directories to avoid
- Keep it lean — no meeting notes, design history, or long implementation guides
- Works best as a **lookup table**, not a brain dump

### 3. Delegate Verbose Work to Subagents
- Subagents run in isolated context windows — verbose output stays contained, only summary returns
- **Not automatically cheaper** — startup overhead (prompts, tool definitions, round trips) makes them wasteful for small tasks
- Rule: use subagents when saved main-context clutter > startup overhead

### 4. Point Claude to Exact Files and Line Ranges
- Vague tasks trigger expensive exploration (opening files, dead ends, reconstructing context)
- Specific: `"Compare src/auth/session.ts lines 30-90 with src/api/login.ts lines 10-60"`
- **Use plan mode** (`Shift+Tab`) before expensive operations — review plan, cut unnecessary steps, then execute

### 5. Use /compact Proactively
- Compact **before** context gets overloaded, not after Claude starts forgetting
- Best timing: after exploration is done and important parts are clear, before next phase
- Early compaction produces better summaries than late compaction

### 6. Check /context Before Optimizing
- `/context` shows what's actually consuming the window
- Biggest improvements often come from spotting one "quiet offender" riding along every turn
- Inspect first, then optimize — don't optimize blindly

### 7. Keep Tooling Setup Simple
- More connected tools = more context overhead
- Only load integrations that solve a real repeated problem

## Key Quote

> "Stop thinking only about prompts and start thinking about **context architecture**."

## Connections

- Validates [[context-management]] as the primary lever for cost control
- Extends [[agent-cost-economics]] with practical per-developer tactics (vs. macro-level analysis)
- Updates [[claude-code]] with operational best practices
- CLAUDE.md sizing connects to [[vibe-coding-lessons-k10s]] Tenet 1 (architecture directives in CLAUDE.md)
- Subagent isolation pattern connects to [[multi-agent-orchestration]]

## See Also
- [[claude-code]]
- [[context-management]]
- [[agent-cost-economics]]
- [[cost-optimization-guide]]
