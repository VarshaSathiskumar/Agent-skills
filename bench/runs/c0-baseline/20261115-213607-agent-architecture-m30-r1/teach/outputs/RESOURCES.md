# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Context rot, just-in-time retrieval, compaction, structured note-taking and sub-agents, with trade-offs. Use for: deciding what stays in context, what is fetched, what is saved.
- [Docs: Context windows (Claude Platform)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  What counts toward the window, how history accumulates across turns, overflow behavior. Use for: token and cost reasoning.
- [Article: Managing context on the Claude Developer Platform](https://claude.com/blog/context-management)
  The memory tool (client-side, file-based) and context editing. Use for: how to implement notes between sessions.
- [Article: "LLM Powered Autonomous Agents" by Lilian Weng](https://lilianweng.github.io/posts/2023-06-23-agent)
  Overview of agents including short-term and long-term memory. Use for: the wider agent picture and memory vocabulary.

## Wisdom (Communities)

- [r/LLMDevs](https://www.reddit.com/r/LLMDevs/)
  Developer discussion of agents, memory and retrieval. Use for: asking how others handle long-document assistants.
