# Open misconception: the model runs the tools itself (M4)

In quiz 0001 (submission s1), Riley answered that the model itself fetches calendar data (q2) and that the model runs the three tools itself, counting 1 model call instead of 4 (q4).
The model only writes text, including requests for tools; the program runs them, and each step is a separate model call.
Riley also added that the assistant remembers tool choices across sessions on its own (M3), which matters for the next topic, memory.

**Evidence:** quiz 0001, submission s1, items q2, q4, q6.

**Implications:** Before context and memory, have Riley trace one request step by step, marking whether the model or the program does each step. Riley does know the loop (q1), the stopping condition (q3) and that tools are described by name and description (q6, first part).
