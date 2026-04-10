# Wiki Index

## Sources

| Page | Summary | Date |
|------|---------|------|
| [[llm-wiki-karpathy]] | The LLM Wiki pattern — foundational idea file for this wiki (Karpathy) | 2026-04-08 |
| [[scion-docs]] | Scion multi-agent orchestration testbed documentation (GCP) | 2026-04-07 |
| [[kiro-autonomous-agent]] | Kiro autonomous agent product page — frontier agent for async dev tasks (AWS) | 2026-04-07 |
| [[claude-code-docs]] | Claude Code documentation — agentic coding tool by Anthropic | 2026-04-07 |
| [[anthropic-skills-repo]] | Anthropic skills repository & Agent Skills open standard specification | 2026-04-07 |
| [[ten-pillars-agentic-skill-design]] | Research paper: ten-pillar framework for agentic skill design (Forster) | 2026-04-08 |
| [[evaluating-agent-skills-caparas]] | Practical guide to skill evaluation — three-tier framework with economics (Caparas) | 2026-04-08 |
| [[ai-technique-podcast]] | strAIght talk podcast — AI as workflow replacement layer, daily prompts, context documents | 2026-04-09 |
| [[skills-pipeline-sleestk]] | Skills Pipeline — chained skill pipelines for YouTube, SaaS, and Obsidian (Sleestk) | 2026-04-09 |
| [[fabric-github]] | Fabric: open-source framework with 251+ curated AI prompt patterns (Miessler) | 2026-04-08 |
| [[personal-ai-infrastructure]] | PAI: personalized AI platform built on Claude Code — memory, skills, goals (Miessler) | 2026-04-08 |

## Entities

| Page | Type | Summary |
|------|------|---------|
| [[andrej-karpathy]] | person | AI researcher, author of the LLM Wiki pattern |
| [[daniel-miessler]] | person | Security researcher, creator of Fabric and PAI |
| [[scion]] | tool | Experimental multi-agent orchestration testbed — hypervisor for LLM agents |
| [[kiro]] | tool | Agentic IDE by AWS with autonomous agent, CLI, and IDE surfaces |
| [[claude-code]] | tool | Agentic coding tool by Anthropic — terminal, IDE, web, Slack, GitHub |
| [[fabric]] | tool | Open-source framework with 251+ curated prompt patterns and composable strategies |
| [[pai]] | tool | Personal AI Infrastructure — persistent memory, skills, goals on Claude Code |
| [[google-cloud-platform]] | organization | Cloud platform by Google, hosts the Scion project |
| [[aws]] | organization | Amazon Web Services, behind Kiro and the frontier agent concept |
| [[anthropic]] | organization | AI safety company, builds Claude models and Claude Code |

## Concepts

| Page | Summary | Source Count |
|------|---------|--------------|
| [[llm-wiki-pattern]] | Pattern for LLM-maintained personal knowledge bases — the methodology behind this wiki | 1 |
| [[agent]] | Isolated process running an LLM + harness loop against a task | 1 |
| [[agent-state-model]] | Three-dimensional state tracking: Phase, Activity, Detail | 1 |
| [[agent-skills-standard]] | Open standard (agentskills.io) for packaging reusable agent capabilities | 2 |
| [[context-management]] | Strategies for managing limited context windows in multi-skill pipelines | 2 |
| [[prompt-engineering-patterns]] | CoT, ReAct, Reflexion, composable strategies, and other prompting techniques | 2 |
| [[skill-evaluation]] | Three-tier framework for measuring agent skill quality (deterministic → LLM-judge → human) | 2 |
| [[grove]] | Project workspace where agents live (.scion directory) | 1 |
| [[harness]] | Adapter for LLM tools (Gemini, Claude, OpenCode, Codex) into Scion | 1 |
| [[hub]] | Central control plane for hosted/distributed Scion deployments | 1 |
| [[template]] | Versioned blueprint for creating agents | 1 |
| [[runtime]] | Infrastructure layer for executing agent containers | 1 |
| [[runtime-broker]] | Compute node providing execution capacity to the Hub | 1 |
| [[plugin-system]] | Extension architecture via hashicorp/go-plugin over gRPC | 1 |
| [[multi-agent-orchestration]] | Coordinating multiple LLM agents — comparing Scion, Kiro, and Claude Code | 3 |
| [[frontier-agent]] | AWS term for autonomous, scalable, independently-operating AI agents | 1 |
| [[kiro-powers]] | Specialized packages enhancing Kiro agents with domain expertise | 1 |
| [[mcp-protocol]] | Open protocol for connecting LLMs to external tools — shared by Claude Code and Kiro | 2 |

## Analyses

| Page | Summary | Date |
|------|---------|------|
| [[key-insights-agentic-landscape]] | 10 key insights synthesized across all 8 sources — architectural philosophies, design tensions, emerging standards, and gaps | 2026-04-08 |
| [[ten-pillars-evidence-map]] | Evidence map: how 11 wiki sources validate each of the Ten Pillars, with strength rankings and v3 recommendations | 2026-04-09 |
| [[cross-source-themes]] | 8 common themes across 11 sources — context is king, composition over monoliths, memory frontier, evaluation gap | 2026-04-09 |
