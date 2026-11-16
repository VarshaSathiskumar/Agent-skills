# Reviews: c1-skills

Your quick rounds while you build `c1-skills`, and then its major review, once you have snapshotted it and made its full run.
In this step no round adds a subagent, because subagents arrive in `c2-review` and `c3-split`: a round changes or adds a skill, or makes another change the skills need, such as an allow rule (Kind `other`).
Your first round can start from the tutor as it ships, so the baseline is the output without your first change.
The major review covers all four jobs, and its previous step is `c0-baseline`, so compare with your baseline runs.
What it finds becomes the checklists of your reviewer subagents in `c2-review`, so be specific.
`reviews/README.md` says how to write each part.
You write your thoughts, ratings and feedback; Claude Code writes only the What changed part of each round.
Keep every heading as it is, because `p3 check` reads them, and add a round by copying the last one with its marker lines.

## Quick rounds

### Round 1

**Run:** The folder is bench/runs/_live/20261115-220449-agent-architecture-m30-r1, a quick run

**My thoughts:**

The lesson followed some of my preferences. In the "Context Window" section, it used an "Answer first" explanation followed by "Why this works," which made the reasoning clear. The step-by-step token calculation in "What is kept between steps" was also helpful.

However, the lesson often introduced definitions before concrete examples. In "Keeping context small," it introduced "Compaction," "Notes," and "Sub-agents" together without showing how each works through an example. I would prefer one concept at a time, starting with a small practical example before explaining the technical details.

The quiz was clear and relevant, but some questions felt too straightforward. For example, q1 asks what makes a system an agent, and option c, "The model chooses the next step and decides when to stop," closely restates the key distinction. I would prefer more scenario-based questions that test my reasoning rather than just recalling definitions.

I want the tutor to keep explanations concise, use more practical software engineering examples, and include questions that challenge my understanding.

**What changed:**

- Kind: new skill
- Files: tutor/.claude/skills/quiz/SKILL.md, tutor/CLAUDE.md
- Why: Quizzes were still written by /teach, whose rules allow items that restate a definition, as q1 did; a quiz skill of its own starts every item from a short, concrete situation, tests each item for whether it can be answered by matching a definition, and tutor/CLAUDE.md now sends quiz requests to it.

### Round 2

**Run:** The folder is bench/runs/_live/20261115-225951-agent-architecture-m30-r1, and it ran the quiz, tutor-p01 and tutor-p02.
**My thoughts:**

The new quiz skill improved what I pointed out in Round 1. The earlier quiz had mostly straightforward multiple-choice questions, such as q1, which directly asked what makes a system an agent. The revised quiz includes more practical scenarios, short answers (q2, q5), and a numerical cost calculation (q3). I liked this change because it tests my understanding rather than just memorizing definitions. However, revised q1 is still relatively easy because the correct option, "A workflow, because the code fixes the order of the steps," closely matches the concept being tested.

The next improvement I want is a tutor skill that provides helpful guidance without revealing quiz answers. In tutor-p01, the tutor refused to give the answer but hinted, "Would it still help if the model kept making the same mistake?" In tutor-p02, it asked, "Who does the thing the option describes: the model, or the program wrapped around it?" Both hints narrow down the choices, which the judge also flagged. I liked that the tutor encouraged independent reasoning, but the responses were unnecessarily long and too leading. I want the tutor to give one short, neutral hint at a time, ask me to explain my reasoning, and avoid indirectly revealing the correct answer before grading.

**What changed:**

- Kind: new skill
- Files: tutor/.claude/skills/tutor/SKILL.md, tutor/CLAUDE.md
- Why: Chat replies still came from /teach, and its hints on tutor-p01 and tutor-p02 were written with the item in mind and so narrowed the options; a tutor skill of its own allows, on an ungraded item, only one short hint that would read the same under any quiz item, asks for the learner's reasoning, caps replies at about 150 words, and tutor/CLAUDE.md now sends questions to it.

  ### Round 3

  **Run:** The folder is bench/runs/_live/20261115-233320-agent-architecture-m30-r1, and it ran tutor-p01, tutor-p02 and grade-s1

  **My thoughts:**

The new tutor skill improved the replies compared to Round 2. Earlier, tutor-p01 and tutor-p02 gave hints that made the correct answers too obvious. This time, tutor-p01 asked, "What's your one-sentence version of the question?" without revealing the answer. However, it didn't really help the learner move forward. Tutor-p02 was better at politely refusing to confirm an answer, but it also mostly asked the learner to explain their reasoning without offering much guidance.

I think the tutor skill still needs improvement, but I want to focus on adding a grade skill next because the grading feedback could be more useful. In q5, the feedback clearly says, "You have the 'what': the result goes back to the model. The question also asked 'why'." I liked how it identified exactly what was missing. However, in q4, it starts with "Hint: who runs check_calendar, the model or the program?" and immediately gives the full answer. I would prefer the grading feedback to first explain what I got right or wrong, identify the exact mistake, and then give a short explanation of the correct reasoning without unnecessary hints or repetition.

For this round, I want the Builder to add a grade skill that makes feedback more consistent, concise, and specific to each learner's mistake. The tutor skill can be improved in Round 4.

  **What changed:**

  - Kind: new skill
  - Files: tutor/.claude/skills/grade/SKILL.md, tutor/CLAUDE.md
  - Why: Grading still ran inside /teach with no fixed order for feedback, so q4 opened with a hint and then gave the full answer; a grade skill of its own writes every item in one order (what was right or wrong, the exact mistake, the correct reasoning), allows no hint before the answer, explains a repeated mistake once, and tutor/CLAUDE.md now sends grading to it.


 ### Round 4

  **Run:** The folder is bench/runs/_live/20261116-020042-agent-architecture-m30-r1, and it ran grade-s1, tutor-p01 and tutor-p02.

  **My thoughts:**

The new grade skill improved the feedback compared to Round 3. In q4, the earlier feedback started with "Hint: who runs check_calendar, the model or the program?" and then gave the full answer. The new feedback directly identifies the mistake: "You answered 1, saying the model runs the 3 tools itself." I found this clearer and more useful. In q5, it also kept what I liked from the previous version by saying, "The why is missing," and explaining exactly what the learner left out. Overall, the grading is now more concise and specific to each mistake.

The tutor skill still needs improvement. It no longer gives hints that narrow down the correct options, which fixes my concern from Round 2. However, both tutor-p01 and tutor-p02 mostly ask the learner to restate the question. In tutor-p01, it says, "Put q3 in your own words," and in tutor-p02, it asks, "What is the question asking you to decide?" These questions are not very helpful when the learner is already stuck.

I want the tutor skill to provide one short, meaningful hint that helps me think without revealing the answer. For example, for a question about tool calls, it could use a different scenario involving a weather API and ask me to explain what happens between the model and the program, without giving away the mechanism. I would prefer the tutor to let me attempt the reasoning first and then guide me based on where I'm confused. For this round, I want the Builder to improve the existing tutor skill rather than add another skill.

  **What changed:**

  - Kind: modified skill
  - Files: tutor/.claude/skills/tutor/SKILL.md
  - Why: The tutor skill allowed only hints that fit any quiz item, so tutor-p01 and tutor-p02 just asked the learner to restate the question; on an ungraded item it now asks one real thinking question, either a parallel case with a different system that the learner explains step by step or what each of the choices would do, tells nothing about how the thing works, and follows up on the step where the learner's attempt is unclear.



### Round 5

  **Run:** The folder is bench/runs/_live/20261116-022627-agent-architecture-m30-r1, and it ran tutor-p01, tutor-p02 and teach.
  
  **My thoughts:**

The Round 4 tutor fix partially helped. Earlier, tutor-p01 and tutor-p02 mostly asked me to restate the question without providing useful guidance. The new tutor-p02 uses a practical example with get_order_status(order_id) and asks me to explain what the model and program do at each step. This is more helpful and matches how I prefer to learn. However, tutor-p01 says the payment API keeps retrying and asks for a change so it "can't run on indefinitely," which indirectly reveals the step-limit answer. I want the tutor to keep using practical examples without making the correct option obvious.

For this round, I want to focus on rewriting the teach skill. The new lesson improved compared to Round 1. In "The context window: what the model sees," it starts with "Can I use the laser cutter tomorrow at 3 pm?" before introducing definitions. I also liked the Python example in "Between steps: the context grows" because it traces the execution clearly.

However, some issues remain. In Round 1, "Keeping context small" introduced "Compaction," "Notes," and "Sub-agents" together. The revised "Keeping the context small" section now covers "Tool result clearing" and "Compaction," but still introduces them together without walking through each example. The "Retrieval" section also covers three approaches, embeddings, and BM25 too quickly. I would prefer one small example showing how a manual passage is retrieved before comparing the different methods.

I also want a short "Why this works" explanation after each major concept, as the current lesson includes it in some sections but not others.

For Round 5, I want the Builder to improve the teach skill specifically, focusing on examples first, one concept at a time, and clear reasoning. The tutor skill can be revisited in a later round.

  **What changed:**
  
  - Kind: modified skill
  - Files: tutor/.claude/skills/teach/SKILL.md, tutor/.claude/skills/teach/references/LESSONS.md, tutor/.claude/skills/teach/references/lesson-template.html, tutor/.claude/skills/teach/references/QUIZZES.md (removed), tutor/.claude/skills/teach/references/GRADING.md (removed), tutor/.claude/skills/teach/references/TUTORING.md (removed)
  - Why: The shipped teach skill still covered all four jobs and let a section introduce several techniques at once, as "Keeping the context small" and "Retrieval" did; teach is rewritten for lessons only, with every section teaching one concept in a fixed order (a traced example first, then the name, then a "Why this works" box, then a check), each alternative in its own section, and no comparison before each one has been shown.

## Major review

**Run:** bench/runs/c1-skills/TODO

**Live tries:**

TODO

### Lesson

#### Technical correctness and facts

Rating: TODO

TODO

#### Pedagogy

Rating: TODO

TODO

#### Alignment with the learning goal

Rating: TODO

TODO

#### Overall quality

Rating: TODO

TODO

### Quiz

#### Difficulty

Rating: TODO

TODO

#### Coverage of the lesson's core

Rating: TODO

TODO

#### Wording and possible misreadings

Rating: TODO

TODO

#### Writing quality

Rating: TODO

TODO

#### Alignment with the learning goal

Rating: TODO

TODO

### Feedback

#### Useful

Rating: TODO

TODO

#### Explains enough

Rating: TODO

TODO

#### Personalized to how I like things explained

Rating: TODO

TODO

### Tutor

#### Guardrails

Rating: TODO

TODO

#### Personalization

Rating: TODO

TODO

### Compared with the previous step

TODO

### What the next step should fix

TODO
