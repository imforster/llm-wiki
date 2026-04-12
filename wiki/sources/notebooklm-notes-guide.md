---
type: source
created: 2026-04-11
updated: 2026-04-11
origin: llm
sources: []
tags: [notebooklm, notes, knowledge-management, google, ai-tools]
---

# Getting The Most Out Of Notes In NotebookLM

[Original](https://medium.com/@stevenbjohnson/getting-the-most-out-of-notes-in-notebooklm-d9d70316b780) | [Raw](../../raw/llm/notebooklm-notes-guide.md)

A how-to guide by [[steven-johnson]], co-founder and editorial director of [[notebooklm]], published March 2024. Part of a series on using the Gemini-powered writing and research tool from Google Labs.

## Key Takeaways

- **Two note types with clear provenance**: Written Notes (user-authored, editable) and Saved Responses (AI-generated or source quotes, immutable). The immutability of Saved Responses is a deliberate design choice for tracking what the human wrote vs. what the AI wrote.
- **Pin-then-organize workflow**: Have an exploratory conversation with the AI grounded in your sources, pin interesting responses as you go, then revisit and structure later. Brainstorming first, organizing second.
- **Reading-integrated note-taking**: Selecting text in a source triggers AI actions — Add to Note, Summarize to Note, Help Me Understand, Suggest Related Ideas. The AI enhances the reading process, not just the writing process.
- **5,000-word note query limit**: Selected notes exceeding 5,000 words cannot be queried via the chatbox. Workaround: combine all notes into one, then re-add as a source — converting notes into a queryable source.
- **Cross-notebook portability**: The combine-and-copy pattern lets you move note collections between notebooks by pasting combined notes as a new source.

## Design Philosophy

NotebookLM's notes system embodies a specific stance on AI-assisted knowledge work: the AI is grounded in user-curated sources (not the open web), conversations are exploratory, and the user captures what matters. This is closer to the [[llm-wiki-pattern]]'s "human curates, LLM processes" division of labor than to a general-purpose chatbot.

The provenance separation (editable vs. immutable notes) addresses a problem that [[context-management]] strategies in agentic tools also face: knowing the origin and reliability of information in a growing knowledge store.

## Limitations Noted

- 5,000-word ceiling on note queries (workaround provided)
- Saved Responses are not editable (by design, for provenance)
- No native cross-notebook note access (workaround provided)

## See Also
- [[notebooklm]]
- [[steven-johnson]]
- [[llm-wiki-pattern]]
- [[context-management]]
