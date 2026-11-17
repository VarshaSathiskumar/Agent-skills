# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Defines context, context rot, just-in-time retrieval, compaction, structured note-taking and sub-agents. Use for: deciding what goes in context, what is saved, and what is fetched on demand.
- [Docs: Context windows (Claude API)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  How turns accumulate, what counts toward the window, overflow behaviour, compaction pointers. Use for: token and cost reasoning about the loop.
- [Docs: Memory tool (Claude API)](https://platform.claude.com/docs/es/agents-and-tools/tool-use/memory-tool)
  File-based memory exposed as a client-side tool that your code runs. Use for: designing what the assistant saves between sessions. (The URL is the one seen in search results; the page may show in Spanish, an English version exists under /docs/en/.)

## Wisdom (Communities)

No community vetted yet.

## Gaps

- A vetted community for people building agents, to test design skills.
- A source on how retrieval search ranks results (keyword versus embeddings), for a later lesson.
