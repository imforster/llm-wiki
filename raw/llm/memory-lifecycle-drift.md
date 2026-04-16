# Stop Treating AI Memory Like a Search Problem

- **Author**: Benjamin Nweke
- **Source**: https://towardsdatascience.com/stop-treating-ai-memory-like-a-search-problem/
- **Date**: April 12, 2026
- **Type**: Technical deep-dive (Towards Data Science)

## The Problem

A system that remembers everything doesn't have a memory — it has an archive. Store-and-retrieve works for filing cabinets, not for assistants you rely on for months. Memories pile up, decisions get reversed, preferences shift. The system doesn't notice.

## Memory Lifecycle System (5 Components)

### 1. Memory Decay
Each memory has decay_score (0-1). Starts at 1.0, decays based on time since last access. Frequently accessed memories stay fresh. Half-life tunable (30 days for conversational, 90+ for long-running projects). Below 0.1 threshold → archived (not deleted).

Formula: score = e^(-0.693 × days_idle / half_life) + min(0.3, access_count × 0.03)

### 2. Contradiction Detection
When new memory stored, LLM checks against existing store for contradictions. Old memories marked as "superseded" with contradicted_by reference. Resolves at write time, not query time. Example: "uses PostgreSQL" superseded by "migrated to MySQL."

Key: NOT contradictions = additive facts ("likes Python" + "also uses JavaScript"). IS contradiction = replacement facts ("deadline March 15" superseded by "deadline pushed to April 1").

### 3. Confidence Scoring
LLM rates confidence at write time (0.0-1.0):
- 1.0 = explicit direct statement
- 0.7 = clearly implied
- 0.5 = reasonable inference
- 0.3 = weak inference
- 0.1 = speculation

High-confidence weak memory beats low-confidence strong memory in retrieval.

### 4. Compression (Weekly)
Find groups of memories repeating themselves across conversations. Replace N memories with one better entry. Two-pass: gpt-4o-mini identifies clusters, gpt-4o synthesizes merged memory. Merged memory gets confidence=0.85 (synthesis may lose nuance).

### 5. Expiry
Some memories have natural end dates (deadlines, temporary states, one-time events). LLM detects at write time, sets expires_at. Daily purge archives expired memories.

## Retrieval with Lifecycle

Sort by: importance × confidence × decay_score. This composite score is where all five lifecycle concepts converge. Important but poorly supported memory surfaces below moderately important, consistently reinforced one.

## Key Insight

If you're manually cleaning the memory system, the system isn't working. The overhead is small: decay/expiry are pure SQLite (milliseconds), contradiction detection adds one gpt-4o-mini call per write (~200ms), compression runs weekly. Cost: a few extra mini calls per conversation + weekly synthesis job.

## Schema Fields

Standard: content, summary, tags. Lifecycle additions: importance, confidence, access_count, decay_score, status (active/archived/superseded/compressed/expired), contradicted_by, created_at, last_accessed, expires_at. Plus memory_events audit table.
