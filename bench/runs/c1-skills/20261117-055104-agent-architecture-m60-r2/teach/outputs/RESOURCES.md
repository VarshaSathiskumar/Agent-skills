# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Context rot, attention budget, clearing, compaction, note-taking, just-in-time retrieval. Use for: anything about what to keep in context and why.
- [Docs: Context windows (Claude API)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  How the window fills across turns and what counts toward it. Use for: token accounting, window sizes, overflow behaviour.
- [Docs: Memory tool (Claude API)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  Notes across sessions as files the application controls. Use for: designing what the assistant saves between visits.
- [Docs: Context editing (Claude API)](https://platform.claude.com/docs/en/build-with-claude/context-editing)
  Clearing old tool results. Use for: cutting cost in long tool loops.
- [Docs: Compaction (Claude API)](https://platform.claude.com/docs/en/build-with-claude/compaction)
  Server-side summarizing near the limit. Use for: very long conversations (later lesson).
- [Article: "Contextual Retrieval" (Anthropic)](https://www.anthropic.com/research/contextual-retrieval)
  Chunking, embeddings plus keyword search, reranking, with measured results. Use for: finding the right page in a long manual.

## Wisdom (Communities)

None found yet.

## Gaps

- A well-moderated community for agent builders to test designs against; none was verified in this session's searches.
