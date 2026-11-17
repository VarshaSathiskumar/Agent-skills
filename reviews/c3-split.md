# Reviews: c3-split

Your quick rounds while you split up the teach job, and then the major review of `c3-split`.
Add one subagent of the teach pipeline per round, so the run before it shows the lesson without it and the run after it shows the lesson with it.
The major review covers the lesson only, and its previous step is `c2-review`.
`reviews/README.md` says how to write each part.
You write your thoughts, ratings and feedback; Claude Code writes only the What changed part of each round.
Keep every heading as it is, because `p3 check` reads them, and add a round by copying the last one with its marker lines.

## Quick rounds

### Round 1

**Run:** bench/runs/c2-review/20261117-003217-agent-architecture-m30-r1, the c2-review full run

**My thoughts:**

Although the reviewers improved factual accuracy, some sections remained dense and repetitive. The "What is kept between steps" section improved after separating concepts, but the retrieval section still introduced several ideas together. The lesson also fell short of the requested length, with a length ratio of 0.80.

I want to introduce a lesson-planner subagent that reads the lesson request, learning objective, MISSION.md and PREFERENCES.md. It should write a structured plan into drafts/ containing the section order, concepts to cover, word budget, estimated reading time, practical examples, and exercises for each section. The teach skill should use this plan to write the lesson before passing it to the existing four reviewers. I expect this to improve lesson structure, length accuracy, and factual coverage while reducing the need for repeated revisions.

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/lesson-planner.md, tutor/.claude/skills/teach/SKILL.md
- Why: The c2-review lesson came in at 0.80 of its length with a retrieval section that still packed several ideas together, because the teach skill planned and wrote in one go; a lesson-planner subagent now reads the request, MISSION.md, NOTES.md and PREFERENCES.md, finds the objective's key facts with their sources, and writes drafts/NNNN-plan.md with one concept per section, an example and a check for each, the promises the lesson makes, and a word budget that adds up to the requested minutes, and the teach skill writes the draft from that plan before the four reviewers read it.

### Round 2

**Run:** bench/runs/_live/20261117-054839-agent-architecture-m30-r1, teach

**My thoughts:**

The planner improved the lesson structure compared to c2-review, with clearer concept separation and consistent examples from the learner's mission. However, "When the window fills" still combines compaction, context rot, API errors, and safety concerns, while "Finding the right manual page" becomes repetitive in its "Two common mix-ups" box. The lesson mostly follows the plan but moves the overflow example from S1 to S3, misses planned knowledge checks in S4 and S5, and adds content beyond the planned scope. The length ratio improved from 0.80 to 0.87, while runtime increased from 12.1 to 13.4 minutes.

I want to introduce a lesson-writer subagent that reads the planner's output, PREFERENCES.md and MISSION.md, and writes the HTML lesson into drafts/. It should follow the planned concepts, section budgets, examples, and exercises, documenting any necessary deviations before handing the draft back to the teach skill for the existing four-reviewer process. This will help ensure that the planner's decisions are reflected in the actual lesson while bringing the total number of subagents to eight.

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/lesson-writer.md, tutor/.claude/skills/teach/SKILL.md
- Why: The teach skill wrote the lesson itself and drifted from the plan, moving the overflow example to another section, dropping the checks planned for S4 and S5, adding scope and repeating a mix-ups box; a lesson-writer subagent now writes the first draft from the plan alone, with every planned section, check and promise and each section to its budget, records every departure in drafts/NNNN-writer-notes.md, and the teach skill checks the draft and the departures against the plan before the four reviewers read it.


### Round 3

  **Run:** bench/runs/_live/20261117-060936-agent-architecture-m30-r1, teach

  **My thoughts:**

The lesson writer improved plan adherence, but some problems remain. The overflow example is still in "When the context fills up" instead of S1. S4 now includes two knowledge checks, while S5 still has only one. The retrieval section is clearer, but references to embeddings and vector search add unnecessary detail, and S3 remains heavy with API-specific terminology. The departures documented in the writer's notes are reasonable, particularly avoiding unverified reference URLs, although the writer did not verify the actual word counts against the planned budgets. The length ratio improved from 0.87 to 0.92, and runtime decreased from 13.4 to 9.6 minutes. However, teach facts dropped to 0.83, with F3.4 missing again.

The review loop stopped after one pass because "the revision answered every high-priority finding," even though the existing rule allows early termination only when every reviewer reports no findings. I want the teach skill to enforce this rule strictly: if any reviewer raises a finding in the first pass, it must run a second pass after revisions, regardless of whether the findings were addressed or declined. The review record must document whether the loop ended with no findings or at the two-pass cap. This round should only fix the teach skill's orchestration without adding a new subagent or modifying the existing planner, writer, or reviewers.

  **What changed:**

  - Kind: modified skill
  - Files: tutor/.claude/skills/teach/SKILL.md
  - Why: The teach skill ended the review loop after one pass because it judged the high-priority findings answered, though the rule allowed an early end only on "No findings"; the loop now ends in only two ways, every reviewer's "No findings" in the same round or the second pass done, a second round of reviews is required whenever round 1 raised any finding, fixed or declined, the skill checks the count before writing the final lesson, and the record states how the loop ended, how many review rounds ran and how many findings each raised.


## Major review

**Run:** bench/runs/c3-split/TODO

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

### Compared with the previous step

TODO

### What the next step should fix

TODO
