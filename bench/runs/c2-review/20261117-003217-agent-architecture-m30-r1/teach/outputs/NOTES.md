# Notes

## What Riley knows
- Python from classes: functions, lists and dicts, reading JSON, and calling a web API in one class project.
- Has used a chatbot for homework help and report drafts, and has noticed that it can state an outdated fact with confidence.
- A language model takes text in and writes text out, one token at a time, from patterns learned in training (learning record 0001).
- The agent loop at a high level: the model asks for an action, the action is carried out, the result comes back, and this repeats until it is done (learning record 0002).

## What Riley does not know yet
- Has never called a language model from code or written a tool definition.
- Has heard the words "token" and "context window" but cannot say what they limit or why they affect cost.
- Has not met memory, retrieval, workflows versus agents, or multi-agent systems.
- Has no machine-learning background beyond one statistics course.

## Working notes
- Quiz 0001 (the agent loop and tool calling) was taken twice: `submissions/s1.json` on the day of the agent-loop session, and `submissions/s2.json` four days later, from memory, as spaced practice.
  Neither attempt has been graded yet.
- Lesson 0001 (`lessons/0001-context-and-memory-in-an-agent.html`, objective O3, 30 minutes) is written; it has not been taken yet and nothing is shown about how it went. It covers the context window, message history, tool result clearing, notes between sessions and retrieval, with a cheat sheet in `cheatsheets/context-and-memory.html`.
- Not yet taught: compaction (summarizing), embeddings and contextual retrieval, prompt caching in depth, the memory tool, sub-agents.
- The lesson stresses that training status is written by the program from the sign-off record, never from chat. Check that this lands when the quiz is graded.
- No community link has been found yet for testing agent design skills (see `RESOURCES.md` gaps).
