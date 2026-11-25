# Open misconceptions: an agent will eventually succeed (M6), and the model runs its own tools (M4)

On quiz 0001 (submission s2, taken from memory four days after the lesson), Riley chose "left to run longer, it will eventually fix the bug" for a looping agent (M6), and said the model "runs" each tool itself (M4), though the count of model calls was right.
Riley does understand that a tool result goes back in as the next input (q5) and that the model only outputs a request for a tool (q2).

**Evidence:** quiz 0001, submission s2, items q2, q3, q4, q5.

**Implications:** Revisit the stopping condition (step limit, report back) and the split of roles: the model requests, the program runs. Also, the model picks tools from their descriptions, not just names (q6, partial).
