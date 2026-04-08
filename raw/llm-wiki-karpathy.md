# LLM Wiki

Source: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
Author: Andrej Karpathy
Retrieved: 2026-04-08

A pattern for building personal knowledge bases using LLMs.

This is an idea file, it is designed to be copy pasted to your own LLM Agent (e.g. OpenAI Codex, Claude Code, OpenCode / Pi, or etc.). Its goal is to communicate the high level idea, but your agent will build out the specifics in collaboration with you.

## The core idea

Most people's experience with LLMs and documents looks like RAG: you upload a collection of files, the LLM retrieves relevant chunks at query time, and generates an answer. This works, but the LLM is rediscovering knowledge from scratch on every question. There's no accumulation.

The idea here is different. Instead of just retrieving from raw documents at query time, the LLM incrementally builds and maintains a persistent wiki — a structured, interlinked collection of markdown files that sits between you and the raw sources. When you add a new source, the LLM doesn't just index it for later retrieval. It reads it, extracts the key information, and integrates it into the existing wiki — updating entity pages, revising topic summaries, noting where new data contradicts old claims, strengthening or challenging the evolving synthesis. The knowledge is compiled once and then kept current, not re-derived on every query.

The wiki is a persistent, compounding artifact. The cross-references are already there. The contradictions have already been flagged. The synthesis already reflects everything you've read.

You never (or rarely) write the wiki yourself — the LLM writes and maintains all of it. You're in charge of sourcing, exploration, and asking the right questions. The LLM does all the grunt work.

## Architecture

Three layers:
- Raw sources — immutable source documents. The LLM reads but never modifies.
- The wiki — LLM-generated markdown files. Summaries, entity pages, concept pages, comparisons, overview, synthesis.
- The schema — a document (CLAUDE.md, AGENTS.md) that tells the LLM how the wiki is structured, conventions, and workflows.

## Operations

- Ingest: Drop a source, LLM processes it, creates/updates wiki pages, updates index and log. A single source might touch 10-15 pages.
- Query: Ask questions against the wiki. Good answers can be filed back as new pages.
- Lint: Health-check for contradictions, stale claims, orphan pages, missing cross-references, data gaps.

## Indexing and Logging

- index.md: Content-oriented catalog. LLM reads it first on every query. Works well at moderate scale (~100 sources, ~hundreds of pages).
- log.md: Chronological append-only record. Parseable with grep.

## Why this works

The tedious part of maintaining a knowledge base is the bookkeeping. Humans abandon wikis because the maintenance burden grows faster than the value. LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass.

Related in spirit to Vannevar Bush's Memex (1945) — a personal, curated knowledge store with associative trails between documents. The part Bush couldn't solve was who does the maintenance. The LLM handles that.
