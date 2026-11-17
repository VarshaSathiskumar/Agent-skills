# Evaluation report

This is the report on what each step of your architecture bought and what it cost.
I read it for one thing above all: whether each claim matches its evidence, including the steps that did not pay.
A step you measured carefully and then dropped is as good a result as a step that won.

Three kinds of material go here.
The tables are pasted from commands: `uv run p3 report --configs a,b` for the objective checks, the cost and your ratings, and `uv run p3 compare --reveal <session-id>` for each blind comparison.
Paste them as they are, and name the session id or the run ids next to each one, so I can find them in `bench/compare/` and `bench/runs/`.
The evidence from your reviews stays in `reviews/`, and here you point at it: name the round, such as `c2-review` Round 3, or the criterion, such as the `c1-skills` review's Wording and possible misreadings, so I can follow the trail.
The prose is yours.

Each section ends with a marker line.
Replace that line with your own writing; `uv run p3 check --final` fails while one is left.

Words used below.
**Your ratings** is the table `p3 report` prints from your major reviews, one row per criterion and one column per step, from 1 to 5.
A **round** is a quick round in one of your step files in `reviews/`, and its **What changed** is the change Claude Code made from your thoughts in it.
A **pass** is one revise-and-review iteration inside one of your tutor's review loops, so a loop capped at two passes reviews a draft at most twice.
A **tally** is the wins for each config and the ties in one blind comparison, and the **p-value** is the reveal's two-sided sign test on the picks that were not ties: with 10 such picks, 8 for one config is suggestive and 9 is strong.
**Could tell** is the share of pairs where you said you could tell which config made which.
The objective checks use the names `p3 report` prints, such as `teach_facts_correct`, `quiz_key_agreement`, `grade_false_wrong` and `tutor_leaks`, the README's section "The scenarios and the objective checks" lists them, and `guide/06-the-bench.html` ("The headline numbers") says what each one measures.
**Cost** is tokens, output tokens, minutes and subagents per scenario, and the list-price equivalent, which is not what you pay on a subscription.

---

## 1. The baseline, `c0-baseline`

Paste the `p3 report` table for `c0-baseline` (three full runs on the shared topic).

TODO: paste the table and name the three run ids.

What did the baseline do well, and where did it fall short, for each of the four jobs?
Read its outputs as you will read your own steps', because your `c1-skills` review compares against it.
Which of the gaps in `KNOWN-GAPS.md` did you see in your own runs, and did you find one that is not listed?
Which number moved the most from one run to the next, and what does that spread mean for a step measured on a single run?

TODO: your reading of the baseline.

---

## 2. Step 1: `c1-skills` against `c0-baseline`

### What changed

Name the rounds that built this step, such as `c1-skills` Rounds 1 to 4, and the inventory entries of the skills they added; the trail from thoughts to change to outcome is already in `reviews/` and `reviews/components.md`, so do not retell it here.
Then what you put in `PREFERENCES.md`, and anything about how the four skills work together that no single inventory entry says.

In c1-skills Rounds 1–5, I iteratively developed and refined the teach, quiz, grade, and tutor skills, as documented in their component inventory entries. I configured PREFERENCES.md to favor concrete examples before definitions, concise step-by-step explanations, practical code examples, and direct feedback that challenges incorrect reasoning. The skills work together by routing each learner request to the appropriate capability: teach explains concepts, quiz creates assessments, grade evaluates submissions, and tutor handles questions and follow-ups while protecting ungraded quiz answers. Each round addressed issues identified in the previous review.

### Your review, the objective checks and the cost

Paste `uv run p3 report --configs c0-baseline,c1-skills`: the objective checks, the cost per job, and your ratings.

## Results on agent-architecture

Scored full runs (quick runs and --only runs left out); each cell is the mean over the runs, with the range in brackets.

### Quality

| config | runs | teach facts | teach misconc. | length ratio | dead links | key agreement | wrong keys | ambiguous items | verdict agreement | false wrong | misconc. hit | leaks | behavior met |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 1.00 | 0 | 0.74 (0.69-0.80) | 0 | 1.00 | 0 | 0 | 1.00 | 0.00 | 1.00 | 0 | 0.56 (0.50-0.67) |
| `c1-skills` | 1 | 0.83 | 0 | 0.66 | 0 | 1.00 | 0 | 0 | 1.00 | 0.00 | 1.00 | 0 | 0.83 |

Teach facts, key agreement, verdict agreement, false wrong, misconception hit and behavior met are shares (0 to 1); misconceptions, dead links, wrong keys, ambiguous items and leaks are counts per run.
A dash means no run could be scored on that check, and n= says how many of the runs could.
A job that failed counts against the config: no lesson scores 0 teach facts, no quiz and key 0 key agreement, a missing grades file disagrees on every item, and a tutor scenario with no reply is not met; leaks need a reply to check, so such a scenario is left out of them.
The length ratio is a rough reading-time estimate (visible words / 150) over the minutes requested; 0.6 to 1.5 counts as on length.

### Cost: teach

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 598.4k (569.9k-646.1k) | 31.2k (30.6k-31.9k) | 3.1 (3.0-3.4) | 0 | 0.62 (0.59-0.66) |
| `c1-skills` | 1 | 455.2k | 23.5k | 2.5 | 0 | 0.50 |

### Cost: quiz

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 148.5k (134.7k-171.8k) | 5.4k (5.0k-6.0k) | 0.7 (0.6-0.7) | 0 | 0.18 (0.18-0.19) |
| `c1-skills` | 1 | 126.9k | 5.8k | 0.8 | 0 | 0.18 |

### Cost: grade

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 285.3k (271.4k-312.1k) | 7.6k (7.5k-7.8k) | 1.0 (0.9-1.1) | 0 | 0.33 (0.33-0.34) |
| `c1-skills` | 1 | 244.8k | 6.6k | 0.9 | 0 | 0.29 |

### Cost: tutor

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 539.2k (454.1k-612.0k) | 10.9k (9.8k-11.7k) | 1.6 (1.5-1.6) | 0 | 0.67 (0.64-0.69) |
| `c1-skills` | 1 | 461.9k | 6.5k | 1.1 | 0 | 0.48 |

### Cost: all jobs

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 1.57M (1.44M-1.67M) | 55.1k (53.6k-56.5k) | 6.4 (6.1-6.7) | 0 | 1.82 (1.74-1.88) |
| `c1-skills` | 1 | 1.29M | 42.4k | 5.4 | 0 | 1.44 |

Costs are per run, summed over the job's scenarios; list-price $ is the list-price equivalent, not what you pay on a subscription.

## Your ratings

Your ratings from 1 to 5 in the major reviews (reviews/<step>.md), which review full runs on the shared topic; a dash means no rating there yet, one that p3 check does not accept, or a job that step does not review (Tutor in c2-review; Quiz, Feedback and Tutor in c3-split).

| job | criterion | c1-skills | c2-review | c3-split | final |
|---|---|---:|---:|---:|---:|
| Lesson | Technical correctness and facts | 4 | - | - | - |
| Lesson | Pedagogy | 4 | - | - | - |
| Lesson | Alignment with the learning goal | 5 | - | - | - |
| Lesson | Overall quality | 4 | - | - | - |
| Quiz | Difficulty | 4 | - | - | - |
| Quiz | Coverage of the lesson's core | 5 | - | - | - |
| Quiz | Wording and possible misreadings | 4 | - | - | - |
| Quiz | Writing quality | 4 | - | - | - |
| Quiz | Alignment with the learning goal | 5 | - | - | - |
| Feedback | Useful | 4 | - | - | - |
| Feedback | Explains enough | 5 | - | - | - |
| Feedback | Personalized to how I like things explained | 4 | - | - | - |
| Tutor | Guardrails | 4 | - | - | - |
| Tutor | Personalization | 4 | - | - | - |

### What the step bought and what it cost

For each job: what did your major review find against `c0-baseline`, and did the objective checks agree?
Where they disagree, which do you believe, and why?
`c1-skills` is also the first config with your `PREFERENCES.md`, while `c0-baseline` keeps the neutral one: which of the differences could come from your preferences rather than the skills?
What did the step cost per scenario, and was the gain worth it?
Say what one run of `c1-skills` against three of `c0-baseline` lets you claim, and what it does not.

I found the c1-skills lesson better than the baseline in terms of how it teaches. It uses concrete examples, small Python traces, and clear "Why this works" explanations, which match my learning preferences. I rated its pedagogy and overall quality 4/5 and alignment with the learning goal 5/5.

However, the numbers show a regression. Teach facts dropped from 1.00 to 0.83, and the length ratio decreased from 0.74 to 0.66. The missing fact was that a larger context window still requires context management, including techniques such as caching. I trust my assessment of the improved teaching style, but the lower fact coverage is a real weakness that should be fixed. Overall, I preferred the c1-skills lesson despite the weaker numbers, because its explanations were easier for me to understand. I would keep its structure while improving factual completeness and lesson depth.


I found the `c1-skills` quiz and grading feedback better than the baseline. In my Round 2 thoughts, I noted that the quiz used more practical, scenario-based questions, while Round 4 showed that the grading feedback became more concise and identified exact mistakes, such as distinguishing what was correct from what was missing in s1 q5. However, the Quality table shows no change: both configurations have 1.00 key agreement, zero wrong keys or ambiguous items, 1.00 verdict agreement, zero false wrong, and 1.00 misconception hit rate. These checks confirm that both versions are correct, but they do not capture the improvements in question quality and explanatory feedback that I identified in my reviews.


I found the c1-skills tutor better than the baseline, especially in Guardrails and Personalization: Rounds 3–5 improved its ability to protect quiz answers while offering useful, practical guidance. The numbers agree: both had zero leaks, but behavior met increased from 0.56 (baseline range 0.50–0.67) to 0.83, above the baseline's normal run-to-run variation. The judge marked tutor-p05 not met, but I partly disagree because it avoided the PPO derivation, explained the concept simply, and redirected the learner toward practical tool improvements, although it still used some advanced terminology.

The c1-skills configuration was cheaper than the baseline, reducing total tokens from 1.57M to 1.29M, runtime from 6.4 to 5.4 minutes, and estimated list-price cost from $1.82 to $1.44 per run. I think the gain was worth it because the tutor's behavior improved, the lessons became easier to follow, and the quiz and feedback were more useful, all while reducing cost. However, the lesson's factual coverage declined slightly, so that remains an area to improve in the next step.


I think the quiz and grading improvements came mainly from the skills, while the clearer examples and explanations in the lesson came from both my preferences and the teach skill.

The results look promising, especially the tutor's improvement to 0.83, above the baseline range of 0.50–0.67. However, with only one c1-skills run, I can't say these improvements are consistent or that the drop in teach facts is a recurring issue.


---

## 3. Step 2: `c2-review` against `c1-skills`

### What changed

Name the rounds that built this step and the inventory entries of the reviewers they added, as in step 1.
Then the loops' design, for each of teach, quiz and grade: who reviews, what is on each reviewer's checklist and which items came from your `c1-skills` major review, how each reviewer gets a fresh context, how many passes a loop may run and what ends it early, and what each loop records.
Then one design choice you could have made the other way, such as one reviewer against several, a cap of one pass against three, or a reviewer that edits against one that only reports, and why you chose as you did.

Rounds 1 to 6 of c2-review added the quiz, grade, lesson facts, lesson pedagogy, lesson quality, and lesson alignment reviewers, respectively. I chose four separate lesson reviewers instead of one so each could focus on a specific quality criterion without overlooking issues in other areas.

Quiz loop: The quiz-reviewer checks difficulty, weak distractors, ambiguous wording, and answer leakage, addressing the problems identified in q1, q4, and q5 of my c1-skills review. It independently reads the draft without the writer's reasoning, runs at most two passes, and stops early if no revision is needed. Findings, revisions, and declined suggestions are documented in review-records/.

Grade loop: The grade-reviewer checks verdict accuracy, misconception IDs, feedback quality, and whether "Try first:" questions encourage independent reasoning. It reads the draft with fresh context and uses PREFERENCES.md to evaluate personalization. The loop allows two passes, stops early if no revision is needed, and documents findings and changes in review-records/.

Teach loop: Four lesson reviewers run in parallel, checking technical facts against named web sources, pedagogy, objective alignment, and overall quality. Their checklists address earlier issues such as missing facts, crowded sections, and inconsistent lesson length. Each receives only the draft path, objective, and requested minutes. The loop allows two passes and stops early if all reviewers report no findings. When reviewers disagree, correct facts are preserved and the teaching is reorganized. Findings, sources, and before-and-after changes are documented in review-records/.

I chose a two-pass cap instead of one or three passes to balance quality, runtime, and token costs. A single pass might miss problems introduced during revision, while three mandatory passes could add unnecessary cost. An optional third pass for unresolved high-priority findings could be a better alternative.

### The loops as they ran

For teach, quiz and grade: how many review passes ran in your bench run, what the reviewers flagged, and whether the revisions moved anything you can point at, a fact corrected, an ambiguous item rewritten, feedback that changed.
The loop records in the run's outputs are the evidence; name the files.

The quiz loop ran two passes and ended at the cap. In q1, the reviewer flagged that the stem revealed the fixed order and the correct option restated the definition, so the stem was rewritten using handler code to test reasoning rather than recall. These findings and revisions are documented in quiz/outputs/review-records/0002-quiz.md.

For s1, the grade loop ended after one pass with every finding declined, including F1, where the reviewer requested a "Try first:" question for q2, but the skill provides direct feedback for wrong answers. For s2, the loop ran two passes, ending at the cap without changing any verdicts, but F5 improved the summary by focusing on one misconception about the stopping condition. These findings are documented in grade-s1/outputs/review-records/0001-s1-grade.md and grade-s2/outputs/review-records/0001-s2-grade.md.

The teach loop ran two passes, with four reviewers in each pass, and ended at the cap. The facts reviewer flagged in F5 that the token cost mechanism and caching were missing, so the revision added per-call input billing and a short caching aside, closing the gap identified in my c1-skills review. Since only one draft was kept, `teach/outputs/review-records/0001-lesson.md` is the only evidence of what changed.

### Your review, the objective checks and the cost

Paste `uv run p3 report --configs c1-skills,c2-review`.

The c1-skills run is 20261116-025134-agent-architecture-m30-r1, and the c2-review run is 20261117-003217-agent-architecture-m30-r1.

## Results on agent-architecture

Scored full runs (quick runs and --only runs left out); each cell is the mean over the runs, with the range in brackets.

### Quality

| config | runs | teach facts | teach misconc. | length ratio | dead links | key agreement | wrong keys | ambiguous items | verdict agreement | false wrong | misconc. hit | leaks | behavior met |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `c1-skills` | 1 | 0.83 | 0 | 0.66 | 0 | 1.00 | 0 | 0 | 1.00 | 0.00 | 1.00 | 0 | 0.83 |
| `c2-review` | 1 | 1.00 | 0 | 0.80 | 0 | 1.00 | 0 | 0 | 1.00 | 0.00 | 1.00 | 0 | 0.50 |

Teach facts, key agreement, verdict agreement, false wrong, misconception hit and behavior met are shares (0 to 1); misconceptions, dead links, wrong keys, ambiguous items and leaks are counts per run.
A dash means no run could be scored on that check, and n= says how many of the runs could.
A job that failed counts against the config: no lesson scores 0 teach facts, no quiz and key 0 key agreement, a missing grades file disagrees on every item, and a tutor scenario with no reply is not met; leaks need a reply to check, so such a scenario is left out of them.
The length ratio is a rough reading-time estimate (visible words / 150) over the minutes requested; 0.6 to 1.5 counts as on length.

### Cost: teach

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c1-skills` | 1 | 455.2k | 23.5k | 2.5 | 0 | 0.50 |
| `c2-review` | 1 | 3.87M | 156.5k | 12.1 | 8 | 3.10 |

### Cost: quiz

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c1-skills` | 1 | 126.9k | 5.8k | 0.8 | 0 | 0.18 |
| `c2-review` | 1 | 551.9k | 32.4k | 4.0 | 2 | 0.66 |

### Cost: grade

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c1-skills` | 1 | 244.8k | 6.6k | 0.9 | 0 | 0.29 |
| `c2-review` | 1 | 625.2k | 21.8k | 2.5 | 3 | 0.66 |

### Cost: tutor

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c1-skills` | 1 | 461.9k | 6.5k | 1.1 | 0 | 0.48 |
| `c2-review` | 1 | 468.1k | 6.4k | 1.1 | 0 | 0.48 |

### Cost: all jobs

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c1-skills` | 1 | 1.29M | 42.4k | 5.4 | 0 | 1.44 |
| `c2-review` | 1 | 5.52M | 217.1k | 19.6 | 13 | 4.90 |

Costs are per run, summed over the job's scenarios; list-price $ is the list-price equivalent, not what you pay on a subscription.

## Your ratings

Your ratings from 1 to 5 in the major reviews (reviews/<step>.md), which review full runs on the shared topic; a dash means no rating there yet, one that p3 check does not accept, or a job that step does not review (Tutor in c2-review; Quiz, Feedback and Tutor in c3-split).

| job | criterion | c1-skills | c2-review | c3-split | final |
|---|---|---:|---:|---:|---:|
| Lesson | Technical correctness and facts | 4 | 4 | - | - |
| Lesson | Pedagogy | 4 | 4 | - | - |
| Lesson | Alignment with the learning goal | 5 | 4 | - | - |
| Lesson | Overall quality | 4 | 4 | - | - |
| Quiz | Difficulty | 4 | 4 | - | - |
| Quiz | Coverage of the lesson's core | 5 | 4 | - | - |
| Quiz | Wording and possible misreadings | 4 | 3 | - | - |
| Quiz | Writing quality | 4 | 4 | - | - |
| Quiz | Alignment with the learning goal | 5 | 4 | - | - |
| Feedback | Useful | 4 | 4 | - | - |
| Feedback | Explains enough | 5 | 5 | - | - |
| Feedback | Personalized to how I like things explained | 4 | 3 | - | - |
| Tutor | Guardrails | 4 | - | - | - |
| Tutor | Personalization | 4 | - | - | - |


### What the step bought and what it cost

Did the problems your `c1-skills` review found go away, and which ratings moved?
Which loop earned its cost and which did not?
If a loop ran several passes and the final output was no better than the first draft, say so, because that is the finding.

The lesson loop improved technical completeness, with teach facts increasing from 0.83 to 1.00 and the length ratio from 0.66 to 0.80. It addressed the missing explanation of context management and caching from c1-skills. However, my technical correctness, pedagogy, and overall quality ratings remained at 4, while alignment dropped from 5 to 4 because some sections remained crowded and introduced details beyond the objective.

The cost increased from 455k to 3.87M tokens and from 2.5 to 12.1 minutes. Although the lesson improved, I do not think the improvement fully justified the 8.5-fold increase in tokens. I would keep the review process but make the reviewers more selective about which findings require revisions.

The quiz loop partly justified its cost, improving q1 through code-based reasoning, although q5 and q6 still had wording issues. Tokens increased from 127k to 552k, and runtime from 0.8 to 4.0 minutes. 

The grade loop did not justify its cost. Only the s2 summary improved, while the "Try first:" issue remained unresolved. Tokens increased from 245k to 625k, and runtime from 0.9 to 2.5 minutes, with no meaningful improvement in grading quality.

Overall, c2-review did not fully justify its cost, using 5.52M tokens, 19.6 minutes, and 13 subagent starts compared to 1.29M tokens and 5.4 minutes in c1-skills. The unchanged tutor's behavior score dropped from 0.83 to 0.50, demonstrating run-to-run variability. Therefore, improvements such as teach facts increasing from 0.83 to 1.00 are promising but not conclusive, and repeated runs are needed to determine whether the reviewers consistently improve quality.

---

## 4. Step 3: `c3-split` against `c2-review`

### What changed

Name the rounds that built this step and the inventory entries of the pipeline's subagents.
Then the split: the roles you split the teach job into, what each one receives and returns, what runs in order and what in parallel, and who puts the lesson together at the end.
Why this split and not a smaller one, and what did you try that you took out again?

  - Sentence 1: which rounds built this step, and what each round added. You built six rounds, each adding one reviewer: a quiz reviewer, a grade reviewer, and four lesson reviewers (facts, pedagogy, quality, alignment).
  - Sentence 2: why you chose four lesson reviewers instead of one.

The quiz-reviewer subagent independently reviews each quiz draft with fresh context, without seeing the quiz writer's reasoning. It checks for questions that are too easy, correct options that repeat definitions (like q1 in c1-skills), weak distractors (q4), and wording that gives away the answer (q5). The loop allows at most two review passes and stops early if no revision is needed. It records the reviewer's findings, changes made, and declined suggestions in a review record under review-records/, while preserving draft versions for comparison.


The grade-reviewer subagent independently checks the grading draft using fresh context, without the grade writer's reasoning, and reads PREFERENCES.md to make sure the feedback matches how I like to learn. It checks whether verdicts and misconception IDs are correct, whether feedback explains the learner's specific mistakes, and whether the "Try first:" questions encourage independent thinking, an issue I identified in c1-skills. The loop allows at most two review passes and stops early when no changes are needed. It records findings, revisions, and declined suggestions in review-records/, while preserving draft versions for comparison.

The teach loop runs four reviewers in parallel: the facts reviewer checks technical accuracy and missing facts against named web sources, the pedagogy reviewer checks crowded sections and example-first teaching, the alignment reviewer checks objective and mission coverage, and the quality reviewer checks length, figures, and layout. Each receives only the draft path, objective, and requested minutes, ensuring fresh context without the writer's reasoning. The loop runs at most two passes and stops early if all reviewers report no findings. When reviewers disagree, correct facts are preserved and the teaching is reorganized to reduce overload. Findings, sources, before-and-after changes, and reasons for declined suggestions are documented.

I chose a cap of two review passes instead of one or three to balance output quality, runtime, and token costs. However, the second lesson review still identified several issues, and the final revision was never reviewed again. A third pass might have been worthwhile for lessons with unresolved high-priority findings rather than applying it to every lesson.

### Your review, the objective checks and the cost

Paste `uv run p3 report --configs c2-review,c3-split`.

TODO: paste the report tables.

### What the step bought and what it cost

What did the split change in the lesson: its structure, its figures, its references, its fit to you, and how did your four Lesson ratings move against `c2-review`'s?
What did it cost in tokens, minutes and subagents against `c2-review`, and how much of that was overhead rather than writing?
Each step has one run, so say how confident you are, and what would change your mind.

TODO: your judgment of step 3.

---

## 5. `final` against `c0-baseline`, with repeats

### What went into `final`

A diagram of `final`: the main conversation, each skill, each subagent and the guard hook, with arrows for who starts whom and which files each one reads and writes.
ASCII art in a code block or a Mermaid block are both fine; for example:

```
/quiz (skill, main conversation)  writes drafts/0002.json
  -> quiz-reviewer (subagent, fresh context)  reads drafts/
  <- revise, at most 2 passes
  => quizzes/NNNN.json, keys/NNNN.json, review-records/NNNN-quiz.md
```

Draw yours, all four jobs, and delete the example.

TODO: your diagram.

What did you keep from each step, what did you drop, and why?
Point at the inventory entries in `reviews/components.md` rather than repeating them.
If `final` had to get cheaper tomorrow, which component would you cut first and which last, and what do you expect the tutor to lose?

TODO: what `final` is made of, and what you would cut first.

### Your review, the objective checks and the cost

Paste `uv run p3 report --configs c0-baseline,final`, with three scored runs of each.

TODO: paste the report tables.

### What the repeats let you claim

For each headline number: is the difference between the two configs larger than the spread between runs of the same config?
Where the ranges overlap, say "not distinguishable with three runs", and do not rank the two by their means.
Then the overall cost: how many times more tokens and minutes per scenario does `final` take, and for which jobs is it worth it, by your review and by the numbers?

TODO: your reading of `final` against the baseline.

---

## 6. The ablation

Which component did `final-minus-<x>` remove, and what did you expect to happen before you ran it?
Paste `uv run p3 report --configs final,final-minus-<x>`.
What changed, in quality and in cost, and does one run against three let you say the component matters?
If you looked at its outputs, what did you see that the numbers do not show?

TODO: your ablation, its prediction, its table and your reading.

---

## 7. The guard

What does your guard block, and what does it allow, and how does it tell the grader from the main conversation?
Why is it a PreToolUse hook in `tutor/.claude/settings.json`, and not a permission deny rule, a hook in a subagent's frontmatter, a subagent's `tools` list, or an instruction in a skill?
What changed elsewhere in the tutor because of it, such as grading handed to a subagent the guard allows?
Paste the result of running its tests, and list the cases they cover: the main conversation reading `keys/` with each of Read, Grep, Glob, Bash and PowerShell, the grader reading them, and the reads that must still work.
Then the bench evidence that the hook runs in the bench and not only in its tests: the run id and scenario of a trace where it allowed the grader's read of `keys/` or blocked the main conversation's, since a hook that fails to start lets every call through.
Then `tutor_leaks` for `final` against `c0-baseline`, and any denial of the guard you found in a trace.
Last, the gap you know of: one way the main conversation could still reach a key, or a case your tests do not cover, and why you accepted it or how you closed it.

TODO: the guard, its tests and the evidence.

---

## 8. The blind comparison

### `c0-baseline` against `final`

Paste the reveals of the four sessions (teach, quiz, grade, tutor), three run pairs each, with their session ids.

TODO: paste the four reveals with their session ids.

### Your open reviews against your blind picks

This is the check on your own bias, as lecture 24 checks a model judge's.
For each job, what did your open reviews say about `final` against `c0-baseline`: your `final` major review, written before the blind comparison, your `c1-skills` review's comparison with the baseline, and your ratings across the ladder?
Then, for each job, did the blind tally and your reasons agree with them?
Where they disagree, what do you think happened: knowing the labels shaped what you saw in the open, the outputs you judged blind differed from the ones you reviewed, or the difference was too small to see?
Did your picks follow your open reviews more often in the pairs where you could tell than in the pairs where you could not?
Which do you believe now, and what does that say about the ratings in your reviews?

TODO: your open reviews against your blind picks.

### A second blind comparison

For 498E this is optional: if you made one, say which configs and job, why you chose it, paste its reveal, and say whether it agreed with your open reviews.
For 598E, and for the length-study stretch, the length study's three comparisons are your second; say so here and write them up in section 13.
If you made no second comparison, say so in one line.

TODO: your second blind comparison, or why there is none.

---

## 9. The test topics

### The two topics

Name each topic and its id, why you chose it, and the commit in which you committed its items, before its first run.
If you fixed a real mistake in a topic after its runs, as `bench/own/README.md` describes, list the run ids you deleted, what you changed and why.

TODO: your two topics and their commits.

### Results

For each topic, paste `uv run p3 report --topic <id> --configs c0-baseline,final`, and sum up your open review of the topic in `reviews/final.md` in two or three sentences.

TODO: paste the tables for both topics, with your summaries.

### Did the architecture still pay off?

Compare each topic with the shared topic: did `final` win where it won before, and did it fail somewhere new?
Was there anything about the topic, its kind of knowledge or its learner, that explains the difference?
On the life-skill topic, did both configs stay inside general knowledge when your probe asked for personal advice?

TODO: your reading of the test topics.

### Your learning sessions against the bench

Your three learning sessions are in `reviews/final.md`.
Did the bench predict what you saw in them?
Which failure from your sessions would a check or a review of a bench run have caught, and which could no fixed test have caught?
Would you use this tutor again for something you need to learn, and what would it need first?

TODO: the bench against your sessions.

---

## 10. The judge check

Take ten decisions the judge made: for example ten tutor replies it marked met or not met, or ten fact verdicts from your lessons (the judge checks six facts in each lesson on the shared topic, so ten come from two lessons).
Label each one yourself before you look at the judge's verdict, and list your ten labels and its ten verdicts here, with the run id and the scenario of each.
How many of ten did you agree on?
Read the disagreements: is the judge wrong, are you, or is the expected behavior unclear?
What does that agreement mean for the judge numbers you reported above?

TODO: your ten labels, the agreement, and what it means.

---

## 11. A change that did not pay off

At least one change, anywhere in the project, that cost you tokens, time or complexity and did not buy a difference you could see in your reviews or measure in the checks.
What was it, what did you expect, what did the evidence show, and what did you do about it?
Name the round or the inventory entry where it shows.

TODO: the change that did not pay off.

---

## 12. The trade-offs

Paste your ratings across the whole ladder, from `uv run p3 report --reviews`, and the cost of each step, from `uv run p3 report --configs c0-baseline,c1-skills,c2-review,c3-split,final`.

TODO: paste the ratings and cost tables for the whole ladder.

Looking at the whole ladder: which machinery paid for itself, which did not, and how do you know?
If you rebuilt this tutor for P4 with a third of the token budget, what would you keep?
Which number in this report do you trust least, your own ratings included, and why?

TODO: your trade-offs.

---

## 13. The stretch

For 598E this is the rider, and its write-up goes here, with `PREREG.md` beside it.
Cover five things:

1. the option's name;
2. what you did, and the files that hold it;
3. the evidence: the reviews, the blind comparisons, the objective checks and the cost it rests on, pasted or named;
4. what that evidence lets you claim, and what it does not;
5. one thing you would do next, and what result would tell you it worked.

TODO: your stretch.
