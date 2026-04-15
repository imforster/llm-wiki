---
type: concept
created: 2026-04-08
updated: 2026-04-14
sources: ["[[ten-pillars-agentic-skill-design]]", "[[claude-code-docs]]", "[[notebooklm-notes-guide]]", "[[mem0-memory-management]]", "[[continuum-memory-architectures]]", "[[efficient-memory-architectures]]", "[[agent-memory-systems-2026]]"]
tags: [context, tokens, optimization, multi-agent, patterns]
---

# Context Management

Strategies for managing the limited context window available to LLM agents, especially in multi-skill pipelines where different agent personas must share information efficiently.

## Why It Matters

Context windows are finite. Every skill, instruction, tool definition, and conversation turn consumes tokens. Without management, agents hit limits, lose early instructions, or waste budget on irrelevant context.

## Progressive Disclosure

The [[agent-skills-standard]] and [[claude-code]] both use this pattern:
- **Metadata** (~100 tokens): Loaded at startup for all skills — just name + description
- **Instructions** (<5000 tokens): Loaded only when skill activated
- **Resources**: Loaded only when specifically needed

[[claude-code]] extends this: MCP tool definitions are deferred by default (only names consume context until a tool is used).

## Four Recipes (from [[ten-pillars-agentic-skill-design]])

### 1. Chunking
Split large documents into semantic chunks with overlap for context continuity. Overlap last 2 sentences between chunks.

### 2. Progressive Summarization
Two-pass compression: extract key facts, then compress to target ratio. Preserves critical details while reducing token count.

### 3. Selective Context Loading
A ContextManager that registers which context keys each skill needs, then loads only relevant context with priority-based budget allocation. Each skill gets only what it needs.

### 4. Agent Persona Context Templates
Minimal context handoff between agent personas. Define required vs. optional fields per handoff (analyst→engineer→reviewer). Only required fields guaranteed; optional added if budget permits.

## Implementations Across Tools

| Tool | Context Strategy |
|------|-----------------|
| [[claude-code]] | Auto-compaction, deferred MCP tools, subagent isolation, CLAUDE.md under 200 lines |
| [[scion]] | Each agent gets own container with own context. No shared context beyond git. |
| [[kiro]] | Persistent context across tasks/repos/sessions. Learns from feedback. |

## Key Tension

- **Persistent context** (Kiro, Claude Code auto memory): Agent accumulates knowledge over time. Risk: stale or wrong memories.
- **Fresh context** (Scion, Claude Code sessions): Each task starts clean. Risk: re-discovering known information.
- **Selective loading** (Ten Pillars recipes): Middle ground — load only what's relevant per skill/task.

For a deep dive into memory architectures that address this tension, see [[agent-memory-persistence]]. The [[continuum-memory-architectures]] paper formalizes six requirements any real memory system must meet. [[mem0]] provides the most benchmarked production implementation.

## Provenance as Context Metadata

[[notebooklm]] takes a different approach to context management: rather than token budgets and progressive disclosure, it separates context by *authorship*. Written Notes (human) and Saved Responses (AI) are distinct types, making provenance visible. This is a lightweight form of context metadata — knowing *who produced* a piece of context, not just *what* it contains. The 5,000-word note query limit is a concrete example of context window constraints surfacing in a consumer product.

## See Also
- [[ten-pillars-agentic-skill-design]]
- [[agent-skills-standard]]
- [[claude-code]]
- [[multi-agent-orchestration]]
- [[notebooklm]]
- [[agent-memory-persistence]]
- [[mem0]]
