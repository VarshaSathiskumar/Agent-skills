# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Context, context rot, attention budget, just-in-time retrieval, compaction, notes, sub-agents. Use for: anything about what to keep in context.
- [Docs: Context windows (Claude Platform)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  What counts toward the window, accumulation over turns, compaction, window sizes. Use for: token and cost reasoning, current limits.
- [Article: "Introducing Contextual Retrieval" (Anthropic Engineering)](https://www.anthropic.com/engineering/contextual-retrieval)
  Chunking, embeddings, BM25, reranking, and the 200,000-token rule of thumb. Use for: retrieval over the manuals.
- [Docs: Memory tool (Claude Platform)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  Files-based memory across conversations, run by the application. Use for: saving state between sessions.

## Wisdom (Communities)

- Local: makerspace staff and course instructor
  Use for: the questions students really ask, and checking retrieval on real questions.
