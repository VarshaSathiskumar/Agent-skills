# Components

One entry for every skill and every subagent you built, from `c1-skills` to `final`, including the ones you dropped, even one you took out again before any snapshot.
The heading is the skill's folder name or the subagent's `name` from its frontmatter, and `reviews/README.md` says what each field holds.
Replace the empty entry at the bottom with your first component, and copy it for each one after that.
Claude Code may fill in Kind, Step added, and With and without; Purpose, Review and Kept in final are yours.

<!--
An example of a finished entry:

### quiz-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: My c1 review found two quiz items that could be read two ways (q2 and q4) and one whose correct option repeated the stem; a reviewer with a fresh context reads the draft the way a learner will, which the quiz skill writing its own items cannot do, so it is a subagent and not a step in the skill.
- With and without: reviews/c2-review.md, Round 1 (without) and Round 2 (with)
- Review: Without it, q2 asked which design "is better" with no criterion; with it, every stem names its criterion and the reviewer's record shows two items flagged and fixed in one pass, for about 0.6M more tokens per quiz, which I think a quiz is worth, because a misread item teaches the wrong thing.
- Kept in final: yes
-->

### quiz

- Kind: skill
- Step added: c1-skills
- Purpose: The quiz skill creates practical, scenario-based questions that test understanding and reasoning rather than simple recall. It is a skill because quiz generation is a repeatable part of the tutor's normal workflow and does not require an independent agent or fresh context.
- With and without: reviews/c1-skills.md, Round 1 (without) and Round 2 (with)
- Review: In Round 1, q1 was a straightforward recall question, while Round 2 introduced more practical scenario-based, numeric, and short-answer questions. However, one question was still too easy, and the quiz cost stayed about the same in both configurations.
- Kept in final: TODO

### tutor

- Kind: skill
- Step added: c1-skills
- Purpose: The tutor skill prevents leading hints that reveal quiz answers and guides learners through reasoning, it is a skill because it controls the main conversation's replies without needing a separate subagent.
- With and without: reviews/c1-skills.md, Round 2 (without) and Round 3 (with)
- Review: In Round 2, the tutor gave hints that made quiz answers too obvious, while Round 3 avoided this but offered little help. After the Round 4 fix, p02 used a practical get_order_status example to guide reasoning, and the full run showed improvement from 0.56 to 0.83 in behavior met, with lower tutor cost.
- Kept in final: TODO

### grade

- Kind: skill
- Step added: c1-skills
- Purpose: The grade skill gives clear, specific feedback on what was right, wrong, or missing, instead of vague hints or lengthy explanations. It is a skill because grading happens within the tutor's existing workflow and doesn't need a separate context.
- With and without: reviews/c1-skills.md, Round 3 (without) and Round 4 (with)
- Review: Before the grade skill, q4's feedback was wordy and gave away the explanation too quickly; after the skill, it directly identified the mistake. The useful "what" versus "why" feedback in q5 was preserved, while verdict agreement stayed at 1.00 in both configurations.
- Kept in final: TODO

### teach

- Kind: skill
- Step added: c1-skills
- Purpose: The rewritten teach skill creates clearer, step-by-step lessons with practical examples instead of introducing too many concepts at once. It works as a skill because the tutor can teach directly in the main conversation without needing a separate context.
- With and without: reviews/c1-skills.md, Round 5 (without) and the major review's full run of c1-skills (with)
- Review: The rewritten teach skill made lessons easier to follow with practical examples, one concept at a time, and clearer "Why this works" explanations. However, teach facts dropped from 1.00 to 0.83 and the length ratio from 0.74 to 0.66, so the teaching style improved but factual coverage and lesson depth got worse.
- Kept in final: TODO

### quiz-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: The quiz reviewer checks for obvious answers, weak distractors, and questions that reveal the correct response. As a separate subagent, it reviews the draft with fresh context, making it more likely to catch problems the quiz writer overlooked.
- With and without: reviews/c2-review.md, Round 1 (without) and Round 2 (with)
- Review: The quiz reviewer improved q1 by replacing definition recall with code-based reasoning, but q5 still gave away clues and q6 remained ambiguous. The improvement partly justified the increased cost from 127k to 552k tokens and 0.8 to 4.0 minutes.
- Kept in final: TODO

### grade-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: The grade reviewer checks whether feedback accurately identifies misconceptions and provides guiding questions that help learners recognize and correct their mistakes independently before seeing the full answer. It is a subagent because fresh context enables an independent evaluation without being influenced by the grade writer's reasoning.
- With and without: reviews/c2-review.md, Round 2 (without) and Round 3 (with)
- Review: The reviewer provided little improvement over the original grade skill. All s1 findings were declined, s2 only improved the summary, and the "Try first:" issue remained unresolved, making the increase from 245k to 625k tokens and 0.9 to 2.5 minutes unjustified.
- Kept in final: TODO

### lesson-facts-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: The lesson facts reviewer checks technical accuracy and missing facts, addressing the incomplete coverage in c1-skills, where teach facts scored 0.83. It is a subagent because it independently verifies claims against web sources without being influenced by the lesson writer's reasoning.
- With and without: reviews/c2-review.md, Round 3 (without) and Round 4 (with)
- Review: The reviewer filled the missing technical gaps, including per-call input billing and prompt caching, contributing to teach facts reaching 1.00 in the full run. However, the additional explanations made some sections denser, creating a trade-off between technical completeness and readability.
- Kept in final: TODO

### lesson-pedagogy-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: The lesson pedagogy reviewer checks whether concepts are introduced one at a time, explanations are easy to follow, and sections are not overloaded. It is a subagent because an independent reading can identify teaching problems that the lesson writer may overlook.
- With and without: reviews/c2-review.md, Round 4 (without) and Round 5 (with)
- Review: The reviewer improved the structure of "What is kept between steps" by separating concepts, but the retrieval section's closing note remained crowded. The runtime increased from 6.8 to 9.9 minutes, making the improvement useful but incomplete.
- Kept in final: TODO

### lesson-quality-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: The lesson quality reviewer evaluates the finished lesson as a whole, checking its length, layout, figures, and references. It is a subagent because a fresh reading helps identify visual inconsistencies and usability issues that the lesson writer may overlook.
- With and without: reviews/c2-review.md, Round 5 (without) and Round 6 (with)
- Review: The reviewer improved the figures, corrected the section timings to 30 minutes, fixed an incorrect answer panel reference, and made the "Go further" references more useful. However, some content remained repetitive, and the runtime increased from 9.9 to 11.1 minutes.
- Kept in final: TODO

### lesson-alignment-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: The lesson alignment reviewer checks whether the lesson covers its objective, delivers what it promises, and supports the learner's mission using MISSION.md. It is a subagent because an independent reading can identify inconsistencies and scope drift that the lesson writer may overlook.
- With and without: reviews/c2-review.md, Round 6 (without) and the major review's full run of c2-review (with)
- Review: The reviewer addressed the inconsistency between the three promised storage choices and the four used in the worked example. However, some sections still introduced details beyond the objective, and my alignment rating dropped from 5 to 4, showing that the reviewer only partially achieved its purpose.
- Kept in final: TODO

### lesson-planner

- Kind: subagent
- Step added: c3-split
- Purpose: he lesson planner creates a structured outline with one concept per section, realistic word budgets, and examples aligned with the learner's mission, addressing the short and crowded lessons in c2-review. It is a subagent because a fresh context and dedicated instructions allow it to focus on planning without simultaneously managing lesson writing.
- With and without: reviews/c3-split.md, Round 1 (without) and Round 2 (with)
- Review: The lesson planner creates a structured outline with one concept per section, realistic word budgets, and examples aligned with the learner's mission, addressing the short and crowded lessons in c2-review. It is a subagent because a fresh context and dedicated instructions allow it to focus on planning without simultaneously managing lesson writing.
- Kept in final: TODO

### lesson-writer

- Kind: subagent
- Step added: c3-split
- Purpose: The lesson writer turns the planner's outline into an HTML lesson while following its section budgets, examples, and exercises. It is a subagent because a fresh context focused on the plan and lesson format improves adherence, while requiring every departure to be documented.
- With and without: reviews/c3-split.md, Round 2 (without) and Round 3 (with)
- Review: The writer improved plan adherence, documented reasonable departures, and increased the length ratio from 0.87 to 0.92, although the overflow example remained in S3 and S5 still had only one check. Teach facts dropped to 0.83, but I suspect the skipped second review pass contributed more to this gap than the writer itself, which is why Round 3 fixed the loop's stopping rule.
- Kept in final: TODO

### grader

- Kind: subagent
- Step added: final
- Purpose: TODO
- With and without: reviews/final.md, Round 1 (without) and Round 2 (with)
- Review: TODO
- Kept in final: TODO

### review-session

- Kind: skill
- Step added: final
- Purpose: TODO
- With and without: reviews/final.md, Round 2 (without) and Round 3 (with)
- Review: TODO
- Kept in final: TODO
