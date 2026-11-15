# Open gaps after the agent-loop quiz retake: stopping conditions, who runs tools, tool descriptions

On the spaced retake of quiz 0001 (s2), Riley showed the loop (q1), that the model only emits a tool request (q2), and that a tool result goes back as the next input (q5).
Still open: M6 (picked "it will eventually fix the bug", so no sense yet that a loop needs a stopping condition), M4 resurfacing in q4's reasoning ("the model runs one tool itself"), and a partial answer that the model picks tools "by the name" rather than from the full description.

**Evidence:** quiz 0001, submission s2, items q3, q4, q6 (grade `grades/0001-s2.json`).

**Implications:** Before building on context and memory, revisit stopping conditions (cost relates directly to the budget) and tool descriptions. Check M4 again with a new example. Not yet corrected, so these are still open.
