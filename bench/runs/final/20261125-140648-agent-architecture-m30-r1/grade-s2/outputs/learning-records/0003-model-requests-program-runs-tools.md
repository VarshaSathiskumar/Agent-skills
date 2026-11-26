# Riley knows the model only requests a tool call; the "model runs the tool" slip is still open

On quiz 0001 (second attempt, s2), Riley correctly said the model outputs a request naming the tool and arguments (q2), and that the result goes back as the next input for another model call (q5). In q4, though, Riley wrote that the model "runs" each tool itself (misconception M4), and q3 showed a belief that a stuck agent will eventually fix itself (M6).
Later lessons should keep the split between what the model outputs and what the program does explicit.

**Evidence:** quiz 0001, submission s2, items q2, q4, q5.

**Implications:** q6 shows Riley picks tools by name; the tool description and parameters are still to be taught.
