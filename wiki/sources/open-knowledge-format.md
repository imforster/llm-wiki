---
type: source
created: 2026-07-02
updated: 2026-07-02
origin: llm
sources: []
tags: [open-standard, knowledge-format, interoperability, context, metadata, google-cloud]
---

# Introducing the Open Knowledge Format

[Original](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing) | [Raw](../../raw/llm/open-knowledge-format.md)

**Authors**: Sam McVeety & Amir Hormati (Google Cloud, Data Analytics Engineering)
**Published**: June 12, 2026

## Summary

Google Cloud introduces the **Open Knowledge Format (OKF)**, an open specification that formalizes the [[llm-wiki-pattern]] into a portable, vendor-neutral, interoperable standard for representing metadata, context, and curated knowledge that AI agents need.

OKF v0.1 is deliberately minimal: a directory of markdown files with YAML frontmatter. The only required field is `type`. Everything else — what types exist, what fields to include, what sections the body has — is left to the producer.

## Key Claims

1. **The context problem is universal**: Organizational knowledge is fragmented across catalogs, wikis, drives, code comments, and people's heads. Every agent builder solves context-assembly from scratch.
2. **What's missing is a format, not a service**: The answer isn't another knowledge platform — it's an interoperability standard that anyone can produce/consume without an SDK.
3. **OKF formalizes existing patterns**: Obsidian vaults, AGENTS.md/CLAUDE.md convention files, index.md + log.md artifacts, and "metadata as code" repos all use the same shape. OKF makes them interoperable.
4. **Explicitly cites [[andrej-karpathy]]'s LLM Wiki gist** as the intellectual origin of the pattern.

## Design: One Screen

An OKF **bundle** is a directory of markdown files. Each file is a **concept** (table, metric, playbook, API, etc.). File path = identity.

```yaml
---
type: BigQuery Table
title: Orders
description: One row per completed customer order.
resource: https://console.cloud.google.com/bigquery?p=acme&d=sales&t=orders
tags: [sales, revenue]
timestamp: 2026-05-28T14:30:00Z
---
```

Concepts link via standard markdown links → directory becomes a knowledge graph. Optional `index.md` for progressive disclosure; optional `log.md` for change history.

## Three Design Principles

1. **Minimally opinionated** — Only `type` is required. The spec defines the interoperability surface, not the content model.
2. **Producer/consumer independence** — Who writes and who reads are cleanly separated. Human-authored bundles consumed by agents; LLM-generated bundles browsed by humans; one LLM's output queried by another.
3. **Format, not platform** — No proprietary account, SDK, or cloud required. Value comes from how many parties speak it, not who owns it.

## Reference Implementations

- **Enrichment agent**: Walks BigQuery datasets → drafts OKF concept per table/view → second LLM pass enriches with citations, schemas, join paths.
- **Static HTML visualizer**: Turns any bundle into interactive graph view — single file, no backend, no data leaves the page.
- **Three sample bundles**: GA4 e-commerce, Stack Overflow, Bitcoin public datasets.
- **Google Cloud Knowledge Catalog**: Updated to ingest OKF and serve to agents.

## Connections to This Wiki

- This wiki's schema (`.kiro/steering/llm-wiki-schema.md`) is essentially a pre-OKF implementation of the same pattern — markdown + YAML frontmatter + cross-links + index.md + log.md. OKF formalizes what we've been doing.
- OKF's `type` field maps to our frontmatter `type: source | entity | concept | analysis`.
- OKF's progressive disclosure via index.md matches our wiki/index.md as entry point.
- OKF's "format not platform" principle aligns with [[icm-folder-structure]]'s "filesystem as architecture" thesis.
- The fragmented context landscape problem is the same problem [[context-management]] addresses at the agent level — OKF solves it at the organizational/interchange level.

## What's New vs. Karpathy's Gist

Karpathy described the *pattern*. OKF provides:
- A minimal interoperability contract (required fields, reserved filenames)
- Conformance criteria for tooling to validate against
- Producer/consumer separation as explicit design goal
- Organizational scope (team wikis, metadata catalogs) vs. personal scope

## See Also
- [[llm-wiki-pattern]]
- [[andrej-karpathy]]
- [[context-management]]
- [[icm-folder-structure]]
- [[google-cloud-platform]]
