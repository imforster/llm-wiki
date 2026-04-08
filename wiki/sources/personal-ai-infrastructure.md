---
type: source
created: 2026-04-08
updated: 2026-04-08
sources: []
tags: [pai, personal-ai, infrastructure, claude-code, memory, skills]
---

# Personal AI Infrastructure (PAI)

[Original](../../raw/personal-ai-infrastructure.md) | [GitHub](https://github.com/danielmiessler/Personal_AI_Infrastructure)

Author: [[daniel-miessler]]

## Summary

PAI is a personalized AI platform built natively on [[claude-code]], designed to turn it from a stateless tool into a persistent assistant that knows your goals, preferences, and history. It adds memory, skills, hooks, security, voice, and a "TELOS" goal system on top of Claude Code's primitives. Open source (MIT), TypeScript/Bash. v4.0.3 as of March 2026.

## Key Takeaways

- **Three levels of AI**: Chatbots (ask→answer→forget) → Agentic platforms (ask→use tools→get result) → PAI (observe→think→plan→execute→verify→learn→improve). The key differentiator is the **learn** step — continuous feedback capture and self-improvement.
- **Goal-oriented, not task-oriented**: PAI's primary focus is the human and their goals, not the tech. TELOS system: 10 files capturing who you are (MISSION.md, GOALS.md, PROJECTS.md, BELIEFS.md, MODELS.md, STRATEGIES.md, NARRATIVES.md, LEARNED.md, CHALLENGES.md, IDEAS.md).
- **Built on Claude Code, not replacing it**: "Claude Code is the engine. PAI is everything else that makes it *your* car." Uses Claude Code's hooks, slash commands, MCP servers, context files as building blocks.
- **16 design principles**: User centricity, foundational algorithm (scientific method loop), scaffolding > model, deterministic infrastructure, code before prompts, UNIX philosophy, CLI as interface, skill management, memory system, agent personalities, and more.
- **Primitives (architecture)**:
  - **TELOS**: Deep goal understanding via 10 structured files
  - **User/System separation**: USER/ (your stuff, upgrade-safe) vs SYSTEM/ (PAI infra)
  - **Skill system**: Deterministic outcomes first — CODE → CLI → PROMPT → SKILL hierarchy
  - **Memory system**: Three-tier (hot/warm/cold), continuous learning from ratings/sentiment/outcomes
  - **Hook system**: 8 event types for lifecycle automation
  - **Security system**: Policy-based, no need for `--dangerously-skip-permissions`
  - **Voice system**: ElevenLabs TTS with prosody enhancement
  - **Notification system**: ntfy push, Discord, duration-aware routing
- **Packs**: Standalone, AI-installable capability modules (Research, Security, Thinking, Media, etc.) that work without full PAI installation.
- **Scale**: v4.0.0 has 63 skills, 21 hooks, 180 workflows, 14 agents.
- **Relationship to Fabric**: "Fabric is a collection of AI prompts (patterns) for specific tasks. PAI is infrastructure for *how your DA operates*. They're complementary."

## Connections

- **[[llm-wiki-pattern]]**: PAI's memory system and TELOS are a different instantiation of the same insight — persistent, compounding knowledge. The wiki pattern compiles knowledge from external sources; PAI compiles knowledge about *you*.
- **[[claude-code]]**: PAI is the most ambitious layer built on top of Claude Code's primitives. It validates that Claude Code's hooks, skills, and memory are sufficient building blocks for a full personal AI platform.
- **[[fabric]]**: Same author. Fabric = patterns (what to ask). PAI = infrastructure (how the AI operates). Complementary. Many PAI users integrate Fabric patterns.
- **[[agent-skills-standard]]**: PAI's skill system follows a CODE → CLI → PROMPT → SKILL hierarchy — more opinionated than the Agent Skills spec, with deterministic outcomes prioritized.
- **[[ten-pillars-agentic-skill-design]]**: PAI implements many of the ten pillars: architecture (Pillar 1), scope (Pillar 3), modularity (Pillar 4), tool integration (Pillar 6), testing (Pillar 7), versioning (Pillar 8), and anti-patterns (Pillar 10).
- **[[context-management]]**: PAI's three-tier memory (hot/warm/cold) is a concrete implementation of context management strategies.

## See Also
- [[pai]]
- [[daniel-miessler]]
- [[claude-code]]
- [[fabric]]
- [[llm-wiki-pattern]]
- [[context-management]]
