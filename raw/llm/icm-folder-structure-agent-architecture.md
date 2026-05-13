---
title: "Interpretable Context Methodology: Folder Structure as Agent Architecture"
source: "https://arxiv.org/html/2603.16021v2"
author:
  - "[[Jake Van Clief]]"
  - "[[David McDermott]]"
published: 2026-03-18
created: 2026-05-12
description: "ICM replaces framework-level orchestration with filesystem structure. Numbered folders represent stages. Plain markdown files carry prompts and context. One agent reads the right files at the right moment."
tags:
  - "clippings"
  - "arxiv"
  - "context-engineering"
  - "folder-method"
---

# Interpretable Context Methodology: Folder Structure as Agent Architecture

arXiv:2603.16021v2 [cs.AI] 18 Mar 2026

Jake Van Clief, David McDermott — Eduba, University of Edinburgh

## Abstract

Current approaches to AI agent orchestration typically involve building multi-agent frameworks that manage context passing, memory, error handling, and step coordination through code. These frameworks work well for complex, concurrent systems. But for sequential workflows where a human reviews output at each step, they introduce engineering overhead that the problem does not require. This paper presents Interpretable Context Methodology (ICM), a method that replaces framework-level orchestration with filesystem structure. Numbered folders represent stages. Plain markdown files carry the prompts and context that tell a single AI agent what role to play at each step. Local scripts handle the mechanical work that does not need AI at all. The result is a system where one agent, reading the right files at the right moment, does the work that would otherwise require a multi-agent framework. This approach applies ideas from Unix pipeline design, modular decomposition, multi-pass compilation, and literate programming to the specific problem of structuring context for AI agents. The protocol is open source under the MIT license.

GitHub: https://github.com/RinDig/Interpretable-Context-Methodology-ICM-

## Key Concepts

### Five Design Principles
1. One stage, one job (McIlroy/Parnas)
2. Plain text as the interface (Kernighan/Pike)
3. Layered context loading (less irrelevant context = better performance)
4. Every output is an edit surface (Horvitz mixed-initiative)
5. Configure the factory, not the product (continuous delivery)

### Five-Layer Context Hierarchy
- Layer 0: Global identity file (which workspace, folder structure)
- Layer 1: Workspace-level task routing (which stage handles what)
- Layer 2: Stage-specific contract (inputs, process, outputs)
- Layer 3: Reference material (voice rules, design systems, conventions) — stable across runs
- Layer 4: Working artifacts (previous stage output, user source material) — changes each run

### Stage Contracts
Each stage defines: Inputs (which files from L3/L4), Process (what to do), Outputs (what to write). The CONTEXT.md file IS the contract AND the documentation.

### Token Efficiency
- Each stage receives 2,000-8,000 focused tokens
- Monolithic approach: 30,000-50,000 tokens (most irrelevant)
- Avoids "lost in the middle" degradation by construction

## Where It Works
- Sequential workflows with human review at each stage
- Repeatable pipelines (same structure, different input each run)
- Content production, training materials, research analysis, policy workflows

## Where It Doesn't Work
- Real-time multi-agent collaboration (needs message-passing)
- High-concurrency systems (needs queueing/state isolation)
- Complex branching logic based on AI decisions mid-pipeline

## Implementations
- Script-to-animation pipeline (3 stages)
- Course deck production (5 stages)
- Workspace-builder (5 stages — builds new workspaces)
- All tested with Claude Opus 4.6 + Sonnet 4.6 sub-agents

## Key Findings
- U-shaped intervention pattern: heavy editing at stage 1 (direction) and final stage (alignment), light in middle
- Non-technical users successfully modified stage behavior by editing markdown
- Three community members with no coding experience created and ran workspaces producing animated videos
- 52-member practitioner community across AI engineers, business owners, content creators, academics

## Future Directions
- ICM as multi-pass incremental compilation
- Semantic debugging (tracing output back to source context)
- Source integrity (editing source files vs. editing output)
- Output provenance through identifiers
