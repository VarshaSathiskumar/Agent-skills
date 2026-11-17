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
- Review: TODO
- Kept in final: TODO

### grade-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: TODO
- With and without: reviews/c2-review.md, Round 2 (without) and Round 3 (with)
- Review: TODO
- Kept in final: TODO

### lesson-facts-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: TODO
- With and without: reviews/c2-review.md, Round 3 (without) and Round 4 (with)
- Review: TODO
- Kept in final: TODO

### lesson-pedagogy-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: TODO
- With and without: reviews/c2-review.md, Round 4 (without) and Round 5 (with)
- Review: TODO
- Kept in final: TODO

### lesson-quality-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: TODO
- With and without: reviews/c2-review.md, Round 5 (without) and Round 6 (with)
- Review: TODO
- Kept in final: TODO

### lesson-alignment-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: TODO
- With and without: reviews/c2-review.md, Round 6 (without) and the major review's full run of c2-review (with)
- Review: TODO
- Kept in final: TODO
