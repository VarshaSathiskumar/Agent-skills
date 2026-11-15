# Notes

## What Riley knows
- Python from classes: functions, lists and dicts, reading JSON, and calling a web API in one class project.
- Has used a chatbot for homework help and report drafts, and has noticed that it can state an outdated fact with confidence.
- A language model takes text in and writes text out, one token at a time, from patterns learned in training (learning record 0001).
- The agent loop at a high level: the model asks for an action, the action is carried out, the result comes back, and this repeats until it is done (learning record 0002).

## What Riley does not know yet
- Has never called a language model from code or written a tool definition.
- Has heard the words "token" and "context window"; lesson 0001 (O3) now explains them, but nothing yet shows they understand them.
- Has not met workflows versus agents or multi-agent systems.
- Has no machine-learning background beyond one statistics course.

## Working notes
- Quiz 0001 (the agent loop and tool calling) was taken twice: `submissions/s1.json` on the day of the agent-loop session, and `submissions/s2.json` four days later, from memory, as spaced practice.
  Neither attempt has been graded yet.
- Lesson `lessons/0001-context-and-memory-in-an-agent.html` (O3, 30 min) and quiz 0002 are written; not yet taken.
- Misconception ids used in key 0002: M1 = the model itself remembers earlier calls or sessions; M2 = a bigger window is memory, or removes the need to choose what to include; M3 = retrieval means the model has read the whole manual.
- Open question to check in a quiz: does Riley see that the program re-sends the whole history on every call (the cost driver)?
- Next in the mission: workflows versus agents, then multi-agent splits (sub-agent context isolation was only mentioned in lesson 0001).
