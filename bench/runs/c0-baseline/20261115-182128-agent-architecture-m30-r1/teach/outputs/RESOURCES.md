# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Primary source on context rot, attention budget, just-in-time retrieval, compaction, note-taking and sub-agents. Use for: anything on what an agent keeps in context and how to keep it small.
- [Docs: "Context windows" (Anthropic)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  Official description of what counts toward the window, how turns accumulate, and compaction. Use for: window sizes by model and token accounting; check current sizes before relying on them.
- [Paper: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" (Lewis et al., 2020)](https://arxiv.org/abs/2005.11401)
  The paper that introduced RAG. Use for: the origin of retrieval as "non-parametric memory".

## Wisdom (Communities)

- Local: the team's design reviews, course instructors and makerspace staff.
  Use for: real student questions to test retrieval, and policy on storing student data.

## Gaps

- A beginner-friendly, high-trust guide to chunking and search choices (keyword vs embedding) for a small document set.
- A high-moderation online community for agent builders; none verified yet.
