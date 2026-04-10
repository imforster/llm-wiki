---
type: source
created: 2026-04-09
updated: 2026-04-09
sources: []
tags: [skills, pipeline, obsidian, youtube, saas, claude-code]
---

# Skills Pipeline (Sleestk)

[Original](https://github.com/Sleestk/Skills-Pipeline) | [Obsidian Skill](https://github.com/Sleestk/Skills-Pipeline/tree/main/Obsidian)

## Summary

A collection of Claude skills organized as multi-stage pipelines. Three skill sets: a six-stage YouTube video production pipeline, a four-skill SaaS development stack, and a comprehensive Obsidian power user skill. Demonstrates how skills can be chained — each stage takes the previous stage's output as input.

## Key Takeaways

- **Skills as pipelines, not standalone units**: The YouTube pipeline chains 6 skills sequentially: Research → Script → SEO → Visual Director → Editor Brief → Thumbnail. Each skill's output is the next skill's input. This is a concrete implementation of the multi-skill pipeline pattern described in [[ten-pillars-agentic-skill-design]] (Pillar 9: Context Management Recipes).
- **Follows the Agent Skills format**: Each skill is a directory with a `SKILL.md` file using YAML frontmatter (`name`, `description`) — exactly the [[agent-skills-standard]] spec. The Obsidian skill also uses `references/` subdirectory for progressive disclosure.
- **Progressive disclosure in practice**: The Obsidian skill loads reference files on demand ("Read the relevant reference file(s) before responding"). 8 reference files covering editing, linking, canvas, bases, plugins, publish, vault architecture. Quick-reference syntax is inline; deep details are deferred. This is the [[agent-skills-standard]]'s progressive disclosure pattern working in production.
- **Persona-driven skills**: Each skill defines a persona ("seasoned Obsidian knowledge architect", "expert Next.js developer"). The persona sets tone, output standards, and a core rule. This maps to the agent persona concept in [[ten-pillars-agentic-skill-design]] (Pillar 5).
- **Output format standards as tables**: The Obsidian skill defines exact output formats per type (notes → markdown, canvas → JSON, bases → YAML, folder structures → tree + bash script). This is deterministic output specification — related to [[skill-evaluation]]'s outcome goals.
- **Decision logic before responding**: The Obsidian skill has explicit decision logic: identify output type → load reference files → produce complete output → handle multi-category requests. This is a lightweight version of the agentic loop.
- **Test prompts included**: 10 validation prompts built into the skill itself. This is inline evaluation — the skill ships with its own test cases, directly implementing [[skill-evaluation]]'s "start small with a targeted prompt set" advice.

## The Three Skill Sets

### YouTube Pipeline (6 stages)
1. `research-agent.md` → Research Brief
2. `script-agent.md` → Production-ready script
3. `seo-agent.md` → YouTube metadata package
4. `visual-director.md` → Visual Production Brief
5. `editor-brief.md` → Complete editing guide
6. `thumbnail-agent.md` → Thumbnail Creative Brief

### SaaS Stack (4 skills)
- `nextjs-developer` — Next.js 16.2.1 expert
- `supabase-js` — Full-stack Supabase developer
- `stripe-developer` — Stripe payment integrations
- `vercel-developer` — Deploy and manage on Vercel

### Obsidian Power User (1 skill + 8 references)
Comprehensive Obsidian expert covering vault design, canvas, bases, Dataview, Templater, all core plugins, Publish, Web Clipper, CSS snippets, URI links, and MOC notes.

## Connections

- **[[agent-skills-standard]]**: Follows the spec exactly — SKILL.md with frontmatter, references/ directory, progressive disclosure.
- **[[ten-pillars-agentic-skill-design]]**: Demonstrates Pillar 4 (modularity — composable pipeline), Pillar 5 (persona-driven prompts), Pillar 9 (context management — each stage passes minimal context forward).
- **[[skill-evaluation]]**: Ships test prompts inline — the skill is its own eval suite.
- **[[context-management]]**: The pipeline pattern is a concrete implementation of the "Agent Persona Context Templates" recipe — each stage produces structured output that becomes the next stage's input.
- **[[llm-wiki-pattern]]**: The Obsidian skill is directly relevant to this wiki's tooling — it could enhance how we work with Obsidian as the wiki's IDE.

## See Also
- [[agent-skills-standard]]
- [[ten-pillars-agentic-skill-design]]
- [[skill-evaluation]]
- [[context-management]]
- [[llm-wiki-pattern]]
