# Notes

## What Riley knows
- Python from classes: functions, lists and dicts, reading JSON, and calling a web API in one class project.
- Has used a chatbot for homework help and report drafts, and has noticed that it can state an outdated fact with confidence.
- A language model takes text in and writes text out, one token at a time, from patterns learned in training (learning record 0001).
- The agent loop at a high level: the model asks for an action, the action is carried out, the result comes back, and this repeats until it is done (learning record 0002).

- Quiz 0001, s1 (graded): knows what makes an agent (the loop), that a step limit stops a stuck loop, that a tool result goes back to the model, and that the model sees tools as names plus descriptions.

## What Riley does not know yet
- Believes the model runs tools itself (M4; q2, q4 of quiz 0001, s1): does not yet see that the program runs each tool and every step is a separate model call (learning record 0003).
- Believes the model remembers earlier sessions on its own (M3; q6); not yet clear why a tool result is sent back to the model (q5 gave only the what).
- Has never called a language model from code or written a tool definition.
- Has heard the words "token" and "context window" but cannot say what they limit or why they affect cost.
- Has not met memory, retrieval, workflows versus agents, or multi-agent systems.
- Has no machine-learning background beyond one statistics course.

## Working notes
- Quiz 0001 (the agent loop and tool calling) was taken twice: `submissions/s1.json` on the day of the agent-loop session, and `submissions/s2.json` four days later, from memory, as spaced practice.
  `s1` is now graded (`grades/0001-s1.json`); `s2` has not been graded yet.
- Next in the mission is context and memory, because the makerspace assistant has to answer from long machine manuals and remember each student's training status between visits.
