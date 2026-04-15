# Designing for Agentic AI: UX Patterns for Control, Consent, and Accountability

- **Source**: https://ide.com/designing-for-agentic-ai-practical-ux-patterns-for-control-consent-and-accountability/
- **Date**: February 11, 2026
- **Type**: UX design patterns guide for agentic systems

## Core Thesis

Designing for agentic AI is designing for a relationship. Autonomy is an output of a technical system, but trustworthiness is an output of a design process. The goal: autonomy feels like a privilege granted by the user, not a right seized by the system.

Only 6% of companies fully trust AI agents for core processes.

## The Shift: UX to AX (Agent Experience)

UX traditionally: user-driven, system responds. AX: autonomous/semi-autonomous agents that recommend, decide, or act without direct user input. Interaction design shifts from predicting user behavior to orchestrating human-agent collaboration.

## Six Core UX Patterns

### 1. Intent Preview (Pre-Action)
"Here's what I'm about to do. Are you okay with that?"
- Clear, concise plan summary before any significant action
- Sequential steps revealing agent's logic
- Three choices: Proceed / Edit Plan / Handle it Myself
- Non-negotiable for: irreversible actions, financial transactions, sharing info with others
- Metric: >85% acceptance rate. Override >10% triggers model review.

### 2. Autonomy Dial (Pre-Action)
User sets preferred level of agent independence per task type:
- **Observe & Suggest**: notify of opportunities, never propose plans
- **Plan & Propose**: create plans, user reviews every one
- **Act with Confirmation**: prepare actions, user gives final go/no-go
- **Act Autonomously**: pre-approved tasks, notify after the fact
- Granular per task type (scheduling vs sending emails)
- Metric: Setting Churn — high churn indicates trust volatility

### 3. Explainable Rationale (In-Action)
Proactively answers "Why did it do that?" before it's asked.
- Not a technical log — human-readable explanation grounded in user's own preferences
- Example: "I rebooked because your original flight was canceled and you pre-approved autonomous rebooking for same-day non-stops"
- Metric: "Why?" ticket volume per 1,000 active users

### 4. Confidence Signal (In-Action)
Agent communicates its own confidence level:
- Confidence score (percentage)
- Scope declaration ("Travel bookings only")
- Visual cues (green checkmark vs yellow question mark)
- Prevents automation bias — users scrutinize low-confidence plans
- Metric: Calibration Score (Pearson correlation between confidence and acceptance rate, target >0.8)

### 5. Action Audit & Undo (Post-Action)
The ultimate safety net:
- Timeline view of all agent-initiated actions
- Clear status indicators (successful, in progress, undone)
- Time-limited undos with transparent windows
- Metric: Reversion Rate >5% for a task → disable automation for that task
- Safety Net Conversion: users who upgrade to autonomous within 7 days of successful undo

### 6. Escalation Pathway (Post-Action)
Agent knows when to ask for help instead of guessing:
- Request clarification ("Do you mean Sept 30 or Oct 7?")
- Present options (multiple valid paths)
- Request human intervention for high-stakes/ambiguous tasks
- Metric: Escalation Frequency 5-15% is healthy. Recovery Success Rate target >90%.

## Summary Table

| Pattern | Best For | Primary Risk | Key Metric |
|---------|----------|-------------|------------|
| Intent Preview | Irreversible/financial actions | User feels ambushed | >85% Acceptance |
| Autonomy Dial | Variable risk tasks | Total feature abandonment | Setting Churn |
| Explainable Rationale | Background/autonomous tasks | User perceives bugs | "Why?" Tickets |
| Confidence Signal | Expert/high-stakes systems | Automation bias | Scrutiny Delta |
| Action Audit & Undo | All agentic systems | Permanent trust loss | <5% Reversion |
| Escalation Pathway | Ambiguous user intent | Catastrophic guesses | >90% Recovery |

## Designing for Repair

Service recovery paradox: a well-handled mistake can build more trust than flawless execution.
- Acknowledge the error clearly
- State immediate correction
- Provide path to human support
- Treat errors as relationship ruptures to mend

## Phased Adoption Approach

Phase 1 (Foundational Safety): Intent Preview + Action Audit & Undo infrastructure
Phase 2 (Calibrated Autonomy): Autonomy Dial + Explainable Rationale
Phase 3 (Proactive Delegation): Act Autonomously for pre-approved tasks, monitor and iterate

## Wiki Connection

Directly maps to wiki Theme 3 (Human-in-the-Loop spectrum). The Autonomy Dial is essentially what Claude Code's 6 permission modes implement. The phased approach mirrors the trust-building progression from Scion ("interaction is imperative") to Kiro ("hours of autonomy"). Provides the UX research framework missing from the wiki's architectural analysis.
