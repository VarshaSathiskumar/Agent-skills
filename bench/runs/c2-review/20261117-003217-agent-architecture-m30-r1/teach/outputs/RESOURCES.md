# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic)](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)
  Primary source on context as a finite resource, just-in-time retrieval, compaction, tool result clearing, note-taking memory and sub-agents. Use for: anything about what goes in an agent's context and how to keep it small.
- [Docs: "Context windows" (Claude Platform)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  Official description of what counts toward the window, how history accumulates per turn, context rot and overflow behavior. Use for: exact facts about windows, tokens and limits.
- [Docs: "Context editing" (Claude Platform)](https://platform.claude.com/docs/en/build-with-claude/context-editing)
  Official detail on tool result clearing and its interaction with prompt caching. Use for: deciding when and how much to clear.
- [Article: "Contextual Retrieval" (Anthropic)](https://anthropic.com/research/contextual-retrieval)
  How adding context to chunks reduces failed retrievals, with measured results. Use for: improving search over the machine manuals.
- [Cookbook: "Contextual embeddings guide" (Claude Platform)](https://platform.claude.com/cookbook/capabilities-contextual-embeddings-guide)
  Code for embedding-based retrieval with contextual chunks. Use for: building the manual search later.

## Wisdom (Communities)

- None found yet.

## Gaps

- A high-quality, well-moderated community for people building agents, to point the learner to for design feedback.
- A source on the memory tool and multi-session patterns, for the next lesson on persistent memory.
