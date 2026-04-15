---
type: source
created: 2026-04-14
updated: 2026-04-14
origin: llm
tags: [UX, design, trust, autonomy, human-agent, interaction, patterns]
---

# Designing for Agentic AI: UX Patterns for Control, Consent, and Accountability

[Original](https://ide.com/designing-for-agentic-ai-practical-ux-patterns-for-control-consent-and-accountability/) | [Raw](../../raw/llm/agentic-ux-patterns.md)

UX design patterns guide (IDE, February 2026) for building trustworthy agentic systems. Provides the human-agent interaction framework missing from the wiki's architectural analysis. Only 6% of companies fully trust AI agents for core processes.

## Core Thesis

Designing for agentic AI is designing for a relationship. Autonomy is an output of a technical system; trustworthiness is an output of a design process. The shift from UX to AX (Agent Experience).

## Six UX Patterns

| Pattern | Phase | Purpose | Key Metric |
|---------|-------|---------|------------|
| **Intent Preview** | Pre-action | "Here's what I'll do. OK?" | >85% acceptance |
| **Autonomy Dial** | Pre-action | User sets independence level per task | Setting churn |
| **Explainable Rationale** | In-action | Proactive "why" grounded in user prefs | "Why?" ticket volume |
| **Confidence Signal** | In-action | Agent communicates certainty level | Calibration score >0.8 |
| **Action Audit & Undo** | Post-action | Timeline + reversal for every action | <5% reversion rate |
| **Escalation Pathway** | Post-action | Agent asks for help vs guessing | >90% recovery success |

## Autonomy Dial Levels

1. Observe & Suggest — notify only
2. Plan & Propose — user reviews every plan
3. Act with Confirmation — final go/no-go
4. Act Autonomously — pre-approved tasks, notify after

Maps directly to [[claude-code]]'s 6 permission modes and the wiki's autonomy spectrum (Theme 3).

## Phased Adoption

Phase 1: Intent Preview + Audit/Undo (foundational safety)
Phase 2: Autonomy Dial + Explainable Rationale (calibrated autonomy)
Phase 3: Act Autonomously for pre-approved tasks (proactive delegation)

## Service Recovery Paradox

A well-handled mistake can build more trust than flawless execution. Acknowledge error → state correction → provide human support path.

## See Also
- [[multi-agent-orchestration]]
- [[context-management]]
- [[agentic-ai-governance]]
- [[claude-code]]
