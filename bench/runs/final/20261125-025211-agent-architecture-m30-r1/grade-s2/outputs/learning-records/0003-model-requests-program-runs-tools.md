# The model requests a tool call; it does not run the tool (misconception M4 still open)

In quiz 0001 (submission s2), Riley correctly said the model outputs a request naming the tool and its arguments (q2) and that a tool result goes back as the model's next input (q5). In q4, though, Riley wrote that the model runs the tools itself (M4), and in q3 chose to let a stuck agent run longer (M6).

**Evidence:** quiz 0001, submission s2, items q2, q3, q4, q5, q6; grades/0001-s2.json.

**Implications:** Before moving on to context and memory, check that Riley can mark each step of a loop as "model" or "program", and knows the model chooses a tool from the description the program gives it, not from its name alone (q6, partial). A step limit as the safeguard against a stuck loop (q3) is still to be taught.
