# Open misconception: the model runs tools itself (M4), and remembers across sessions (M3)

On quiz 0001 (submission s1), Riley believed the model opens systems and runs the tools itself, and also that it remembers earlier sessions on its own.
In fact the model only writes a tool request; the program runs the tool and feeds the result back, and each step is a separate model call.
Riley does know that the model picks a tool from the names and descriptions it is given, and that a step limit stops a stuck loop.

**Evidence:** quiz 0001, submission s1, items q2, q4 (M4) and q6 (M3); q1 and q3 correct.

**Implications:** Work on "who acts, the model or the program" before moving to context and memory, since memory is something the program supplies.
