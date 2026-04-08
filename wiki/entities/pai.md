---
type: entity
created: 2026-04-08
updated: 2026-04-08
sources: ["[[personal-ai-infrastructure]]"]
tags: [tool, personal-ai, open-source, claude-code, infrastructure]
---

# PAI (Personal AI Infrastructure)

An open-source personalized AI platform by [[daniel-miessler]], built natively on [[claude-code]]. Turns Claude Code from a stateless tool into a persistent assistant that knows your goals, preferences, and history.

Mission: "AI should magnify everyone — not just the top 1%."

## Three Levels of AI

1. **Chatbots**: Ask → Answer → Forget
2. **Agentic Platforms**: Ask → Use tools → Get result
3. **PAI**: Observe → Think → Plan → Execute → Verify → **Learn** → Improve

The key differentiator is the **learn** step.

## Core Primitives

| Primitive | Purpose |
|-----------|---------|
| **TELOS** | 10 files capturing who you are: MISSION, GOALS, PROJECTS, BELIEFS, MODELS, STRATEGIES, NARRATIVES, LEARNED, CHALLENGES, IDEAS |
| **User/System separation** | USER/ (yours, upgrade-safe) vs SYSTEM/ (PAI infra) |
| **Skill system** | CODE → CLI → PROMPT → SKILL hierarchy. Deterministic outcomes first. |
| **Memory system** | Three-tier (hot/warm/cold). Continuous learning from ratings, sentiment, outcomes. |
| **Hook system** | 8 event types for lifecycle automation |
| **Security system** | Policy-based, no `--dangerously-skip-permissions` needed |
| **Voice system** | ElevenLabs TTS with prosody |
| **Notifications** | ntfy push, Discord, duration-aware routing |

## Scale (v4.0.0)

63 skills, 21 hooks, 180 workflows, 14 agents, 12 packs.

## 16 Design Principles

Key ones: User centricity, scaffolding > model, deterministic infrastructure, code before prompts, UNIX philosophy, CLI as interface, continuous learning, permission to fail.

## Packs (Standalone Modules)

Research, Security, Thinking, Media, ContentAnalysis, Investigation, Scraping, Telos, Utilities, ContextSearch, Agents, USMetrics.

## Relationship to Fabric

Same author. [[fabric]] = patterns (what to ask AI). PAI = infrastructure (how the AI operates). Complementary — many PAI users integrate Fabric patterns into skills.

## In the Ecosystem

- Built on [[claude-code]] — the most ambitious layer on top of its primitives
- Implements the [[llm-wiki-pattern]] insight (persistent compounding knowledge) but for self-knowledge rather than external sources
- Skill system is more opinionated than [[agent-skills-standard]] — prioritizes deterministic outcomes
- Memory system is a concrete implementation of [[context-management]] strategies

## See Also
- [[daniel-miessler]]
- [[claude-code]]
- [[fabric]]
- [[llm-wiki-pattern]]
- [[agent-skills-standard]]
- [[context-management]]
