# Open misconception: Riley thinks the model runs the tools itself

On quiz 0001 (submission s1), Riley chose the option where the model opens the booking system on its own (q2) and counted one model call for a three-tool request (q4). The model only writes a tool request; the program runs the tool and calls the model again, so each step is a separate model call.
Riley does see that results go back to the model (q5) and that tools are chosen from their descriptions (q6), but added that the model remembers tool choices across sessions (M3), which is not true without a memory feature.

**Evidence:** quiz 0001, submission s1, items q2, q4 (M4) and q6 (M3).

**Implications:** Revisit who acts at each step (model or program) before the lesson on context and memory. Submission s2 of the same quiz is still ungraded and shows whether this held after four days.
