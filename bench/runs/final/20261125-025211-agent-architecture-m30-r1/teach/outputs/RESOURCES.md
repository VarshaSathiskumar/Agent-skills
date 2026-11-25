# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Primary source on what belongs in an agent's context, context rot, compaction, notes and just-in-time retrieval. Use for: deciding what the makerspace assistant keeps in context and how it loads manual pages.
- [Docs: Context windows (Claude API docs)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  Defines the context window, how history accumulates across turns and what happens when input is too long. Use for: window limits, errors, and why cost grows per step.
- [Docs: Memory tool (Claude API docs)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  How file-based memory works across sessions, with the application running the storage, plus security cautions. Use for: designing saved notes and their safeguards.

## Wisdom (Communities)

None yet; no community preference has been stated.

## Gaps

- How retrieval search works (embeddings, chunking, ranking): needed for the next lesson on finding the right manual page.
