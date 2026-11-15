# The loop is solid; who runs tools, tool descriptions and stopping conditions are open

On the spaced retry of quiz 0001 (submission s2), Riley identified the loop as what makes an agent, knew the model outputs a tool request, and explained that the result goes back as the next input so the model can decide its next step.
Still open: Riley wrote that the model "runs" the tools itself (M4), thought the model picks a tool "by the name" alone, and believed a looping agent will eventually fix the bug without a stopping condition (M6).

**Evidence:** quiz 0001, submission s2, items q2, q3, q4, q5, q6.

**Implications:** Before building on tool use, revisit that the program runs tools and the model only requests them, that the model chooses from the full tool description (relevant to writing descriptions for the makerspace tools), and that loops need a step limit, which also protects the budget.
