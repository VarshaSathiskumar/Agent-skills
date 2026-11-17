# Agent architecture Resources

## Knowledge

- [Anthropic Engineering: "Effective context engineering for AI agents"](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Attention budget, context rot, compaction, structured note-taking, just-in-time retrieval. Use for: any decision about what goes in an agent's context.
- [Claude docs: "Context windows"](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  What counts toward the window, how turns accumulate, compaction and context editing. Use for: exact behaviour, limits and token accounting.
- [Anthropic Research: "Contextual retrieval"](https://anthropic.com/research/contextual-retrieval)
  Adding context to chunks before indexing to improve retrieval. Use for: improving how the assistant finds manual pages.

## Wisdom (Communities)

No community chosen yet; the learner's design review and team serve for now.

## Gaps

- A high-trust community for testing agent designs.
- A source on retrieval evaluation (how to test whether search returns the right page).
