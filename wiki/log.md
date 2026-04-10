# Wiki Log

## [2026-04-07] create | Wiki initialized
Wiki structure created: `CLAUDE.md` schema, `wiki/index.md`, `wiki/log.md`, directory scaffolding. Ready for first ingest.

## [2026-04-07] ingest | Scion Documentation
Source: https://googlecloudplatform.github.io/scion — multi-agent orchestration testbed by Google Cloud Platform. Created 13 wiki pages:
- Source: [[scion-docs]]
- Entities: [[scion]], [[google-cloud-platform]]
- Concepts: [[agent]], [[agent-state-model]], [[grove]], [[harness]], [[hub]], [[template]], [[runtime]], [[runtime-broker]], [[plugin-system]], [[multi-agent-orchestration]]

## [2026-04-07] ingest | Kiro Autonomous Agent
Source: https://kiro.dev/autonomous-agent/ — AWS's frontier agent for autonomous development tasks. Created 6 wiki pages, updated 1:
- Source: [[kiro-autonomous-agent]]
- Entities: [[kiro]], [[aws]]
- Concepts: [[frontier-agent]], [[kiro-powers]]
- Updated: [[multi-agent-orchestration]] — added Kiro as second approach, comparison with Scion

## [2026-04-07] ingest | Claude Code Documentation
Source: https://code.claude.com/docs/en — Anthropic's agentic coding tool. Created 4 wiki pages, updated 2:
- Source: [[claude-code-docs]]
- Entities: [[claude-code]], [[anthropic]]
- Concepts: [[mcp-protocol]]
- Updated: [[multi-agent-orchestration]] — added Claude Code as third approach alongside Scion and Kiro
- Updated: [[harness]] — added cross-reference to Claude Code entity

## [2026-04-07] update | Claude Code Documentation (deep ingest)
Discovered raw .md endpoints on the docs site. Re-ingested overview, how-claude-code-works, memory, sub-agents, permission-modes, hooks, and skills pages with full content. Updated:
- [[claude-code-docs]] — comprehensive takeaways from actual doc content
- [[claude-code]] — full architecture (agentic loop, tools, memory, permissions, extensibility)
- [[mcp-protocol]] — richer detail on Claude Code's MCP usage

## [2026-04-07] ingest | Anthropic Skills Repository & Agent Skills Spec
Source: https://github.com/anthropics/skills + https://agentskills.io/specification — open standard for agent skills and Anthropic's reference implementation. Created 2 wiki pages, updated 3:
- Source: [[anthropic-skills-repo]]
- Concepts: [[agent-skills-standard]]
- Updated: [[claude-code]] — linked skills to Agent Skills Standard
- Updated: [[mcp-protocol]] — clarified complementary relationship with Agent Skills
- Updated: [[multi-agent-orchestration]] — added Agent Skills to shared patterns

## [2026-04-08] ingest | The Ten Pillars of Agentic Skill Design
Source: ~/Documents/2-Areas/agentic-skills-research/agentic-skills-best-practices.pdf (.md version) — research paper by Ian Forster proposing a ten-pillar framework for skill design. Created 3 wiki pages, updated 2:
- Source: [[ten-pillars-agentic-skill-design]]
- Concepts: [[context-management]], [[prompt-engineering-patterns]]
- Updated: [[agent-skills-standard]] — cross-referenced Ten Pillars as design methodology
- Updated: [[multi-agent-orchestration]] — added skill design as open question

## [2026-04-08] ingest | LLM Wiki (Karpathy)
Source: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f — the foundational idea file for the LLM Wiki pattern. This wiki is a running instance of this pattern. Created 3 wiki pages:
- Source: [[llm-wiki-karpathy]]
- Entities: [[andrej-karpathy]]
- Concepts: [[llm-wiki-pattern]]
- Note: Meta-ingest — this source describes the methodology that governs how all other sources are ingested.

## [2026-04-08] ingest | Fabric
Source: https://github.com/danielmiessler/fabric — open-source framework with 251+ curated AI prompt patterns and composable strategies. Created 3 wiki pages, updated 2:
- Source: [[fabric-github]]
- Entities: [[fabric]], [[daniel-miessler]]
- Updated: [[prompt-engineering-patterns]] — added Fabric's composable strategies table
- Updated: [[agent-skills-standard]] — added Fabric Patterns to extension mechanisms comparison

## [2026-04-08] ingest | Personal AI Infrastructure (PAI)
Source: https://github.com/danielmiessler/Personal_AI_Infrastructure — personalized AI platform built on Claude Code with memory, skills, goals, and continuous learning. Created 2 wiki pages, updated 1:
- Source: [[personal-ai-infrastructure]]
- Entities: [[pai]]
- Updated: [[daniel-miessler]] — added PAI as second major project alongside Fabric

## [2026-04-08] query | Key Insights: The Agentic AI Landscape
Synthesized 10 key insights from all 8 sources in the wiki. Filed as analysis: [[key-insights-agentic-landscape]]. Covers: three architectural philosophies, the autonomy-interaction spectrum, emerging open standards, progressive disclosure consensus, memory as unsolved frontier, git as universal coordination, skill hierarchy crystallization, security trust models, the personal AI vision, and what's missing.

## [2026-04-08] ingest | How to Evaluate AI Agent Skills Without Relying on Vibes
Source: Article by JP Caparas — practical guide to skill evaluation with three-tier framework and economics. Created 2 wiki pages, updated 1:
- Source: [[evaluating-agent-skills-caparas]]
- Concepts: [[skill-evaluation]]
- Updated: [[key-insights-agentic-landscape]] — enriched evaluation gap (insight #10) with reference to this framework

## [2026-04-09] ingest | strAIght talk: AI Tips for Amazonians
Source: Podcast notes from raw/human/ai-technique-podcast.md — Amazon employees sharing AI workflow tactics. Created 1 wiki page:
- Source: [[ai-technique-podcast]]
- Cross-referenced: [[pai]], [[fabric]], [[llm-wiki-pattern]], [[context-management]], [[prompt-engineering-patterns]]
- Key insight: "context beats clever prompting" — validates the progressive disclosure and context document approaches seen across the wiki
