---
type: source
created: 2026-05-12
updated: 2026-05-12
origin: llm
sources: []
tags: [context-engineering, orchestration, filesystem, unix, folder-method]
---

# Interpretable Context Methodology: Folder Structure as Agent Architecture

[Original](https://arxiv.org/html/2603.16021v2) | [Raw](../../raw/llm/icm-folder-structure-agent-architecture.md)

**Authors:** Jake Van Clief, David McDermott (Eduba, University of Edinburgh)
**Published:** 2026-03-18 (arXiv)
**License:** CC BY 4.0 | MIT (protocol)

## Summary

Academic paper presenting **Interpretable Context Methodology (ICM)** — a method that replaces multi-agent framework orchestration with filesystem structure. Numbered folders represent pipeline stages. Markdown files carry prompts and context. One agent reads the right files at the right moment, doing the work that would otherwise require a multi-agent framework.

Core thesis: **for sequential, human-reviewed workflows, the filesystem IS the orchestration layer.** No framework code, no server, no developer dependency for day-to-day operation.

## The Five-Layer Context Hierarchy

| Layer | Purpose | Changes Between Runs? |
|-------|---------|----------------------|
| 0 | Global identity (which workspace, folder map) | No |
| 1 | Task routing (which stage handles what) | No |
| 2 | Stage contract (inputs, process, outputs) | No |
| 3 | Reference material (voice, design, conventions) | No — "the factory" |
| 4 | Working artifacts (previous stage output, source material) | Yes — "the product" |

Key insight: **Layer 3 (internalize as constraints) vs Layer 4 (process as input)** — structurally separating these gives the model clearer signals about which information constrains behavior vs. which to transform.

## Five Design Principles

1. **One stage, one job** — McIlroy's Unix principle + Parnas information hiding
2. **Plain text as interface** — markdown/JSON, no binary formats, any tool can participate
3. **Layered context loading** — prevention over compression; each stage gets 2,000-8,000 tokens vs. 30,000-50,000 monolithic
4. **Every output is an edit surface** — human can open, read, edit between stages
5. **Configure the factory, not the product** — workspace set up once, runs repeatedly

## Token Efficiency

- Each stage: 2,000-8,000 focused tokens
- Monolithic equivalent: 30,000-50,000 tokens (most irrelevant to current task)
- Avoids "lost in the middle" degradation (Liu et al.) **by construction** — irrelevant tokens are never loaded
- Contrast with prompt compression (LLMLingua): ICM prevents the problem rather than treating it

## Stage Contracts

```markdown
## Inputs
- Layer 4 (working): ../01_research/output/
- Layer 3 (reference): ../../_config/voice.md
## Process
Write a script based on the research output.
## Outputs
- script_draft.md -> output/
```

The CONTEXT.md file is simultaneously the agent instruction AND the human documentation. Self-documenting by design (echoes Knuth's literate programming).

## Practitioner Findings (52-member community)

- **U-shaped intervention**: heavy editing at stage 1 (creative direction) and final stage (alignment debugging), light in middle (constrained execution)
- **Non-technical users** successfully modified stage behavior by editing markdown CONTEXT.md files
- **Three non-coders** created and ran workspaces producing 10-minute animated videos without developer assistance
- **Workspace duplication**: users copy and adapt existing workspaces rather than building from scratch (mirrors Unix shell script culture)

## Where It Works / Doesn't Work

**Works:** Sequential workflows, human review at each stage, repeatable pipelines (content production, training materials, research, policy)

**Doesn't work:** Real-time multi-agent collaboration, high-concurrency systems, complex automated branching

## Intellectual Lineage

Unix pipes (McIlroy 1978) → Make (Feldman 1979) → Pipe-and-filter (Shaw/Garlan 1996) → Multi-pass compilation (Aho et al.) → Plan 9 "everything is a file" → ICM "everything is a folder"

Also draws on: Parnas (information hiding), Dijkstra (separation of concerns), Knuth (literate programming), Gabriel ("worse is better"), Horvitz (mixed-initiative), Rudin (inherent interpretability over post-hoc explanation).

## Connections

- **Formalizes** what [[context-management]] describes as "selective context loading" — ICM is the architectural pattern that implements it
- **Complements** [[multi-agent-orchestration]] — ICM explicitly says "for sequential workflows, you don't need multi-agent; one agent + right context suffices"
- **Validates** [[vibe-coding-lessons-k10s]] — ICM's stage contracts are the structural answer to "AI builds features not architecture"
- **Extends** [[symphony]] — both are spec-first, filesystem-based; Symphony targets concurrent multi-agent, ICM targets sequential single-agent
- **Connects to** [[spec-kit]] — Caskey Coding article explicitly links ICM to Spec Kit's four-phase workflow
- **Implements** [[ten-pillars-agentic-skill-design]] Pillar 4 (Context Management) as an architectural pattern
- **Relates to** [[llm-wiki-pattern]] — both use filesystem structure as knowledge architecture; ICM for workflows, wiki for knowledge

## Key Quotes

> "The simplest viable architecture for this class of problem is one that already exists on every computer: the filesystem."

> "The AI will follow rules if you write them down. It just won't invent them for you." (echoed from practitioner experience)

> "A workspace is a folder. It can be copied to another machine, committed to Git, emailed as a zip file."

## See Also
- [[context-management]]
- [[multi-agent-orchestration]]
- [[symphony]]
- [[spec-kit]]
- [[vibe-coding-lessons-k10s]]
- [[llm-wiki-pattern]]
