# An agent that repeats itself needs a stopping condition (M6 open)

On the spaced re-take of quiz 0001, Riley chose "left to run longer, it will eventually fix the bug" for a coding agent that repeated the same failing edit 40 times (misconception M6).
Riley also wrote that the model "runs" each tool itself in q4 (M4), though q2 was answered correctly, so the model-requests / program-runs split is not yet firm.

**Evidence:** quiz 0001, submission s2, items q3 and q4.

**Implications:** Next, work on stopping conditions (step limit, repeat detection) for the makerspace assistant's loop.
Riley does have the loop structure (q1, q2) and how results feed back to the model (q5); q6 gave only the tool name, not its whole description.
