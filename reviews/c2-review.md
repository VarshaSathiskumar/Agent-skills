# Reviews: c2-review

Your quick rounds while you build the review loops on teach, quiz and grade, and then the major review of `c2-review`.
Add one reviewer subagent per round, so the run before it shows the output without it and the run after it shows the output with it.
The major review covers the lesson, the quiz and the feedback, and its previous step is `c1-skills`.
Say in it whether the problems your `c1-skills` review found are gone.
`reviews/README.md` says how to write each part.
You write your thoughts, ratings and feedback; Claude Code writes only the What changed part of each round.
Keep every heading as it is, because `p3 check` reads them, and add a round by copying the last one with its marker lines.

## Quick rounds

### Round 1

 **Run:** bench/runs/c1-skills/20261116-025134-agent-architecture-m30-r1, the c1-skills full run

**My thoughts:**

The c1-skills quiz improved, but some questions were still too easy. In q1, the correct option closely matched the concept being tested, while q4 had obvious distractors. In q5, the wording "Which steps come next depends on what each manual search returns" almost gave away the answer.

I want a quiz reviewer subagent to check each draft before it is finalized. It should flag questions where the stem reveals the answer, correct options repeat the tested concept, or distractors are too easy to eliminate. It should also check that questions require reasoning rather than just recalling definitions, while keeping examples like q2's cost calculation and q3's retry loop.

The review loop should allow at most **two passes** to avoid timeouts. Draft quizzes should be stored in `drafts/`, separate from the final scored outputs, and each review should leave a short record in `review-records/` showing what was flagged and changed.

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/quiz-reviewer.md, tutor/.claude/skills/quiz/SKILL.md
- Why: The c1-skills quiz still had a stem that gave its answer away (q5), a right option that restated the concept (q1) and distractors that fell away without thought (q4); a quiz-reviewer with those checks reads the draft in drafts/ with a fresh context and only reports, and the quiz skill now revises at most twice, writes quizzes/ and keys/ once at the end, and records each pass in review-records/NNNN-quiz.md.

### Round 2

**Run:** bench/runs/_live/20261116-152035-agent-architecture-m30-r1, quiz and grade-s1

**My thoughts:**

The quiz reviewer helped improve the questions. In q1, the obvious definition-based answer was replaced with a code-tracing question. Q4 now has more plausible distractors, although the scenario still makes the correct answer fairly obvious. Q5 improved by asking me to compare two features instead of giving away the agent distinction. I didn't find any clearly ambiguous questions, but the quiz took around 4.3 minutes compared with under a minute before. The improvement was useful, but the cost seems high. The loop also stopped after two passes, leaving the final revision unreviewed, which is a limitation worth addressing.

Next, I want to add a grade reviewer, even though the current feedback is already good. In s1 q4, it correctly connects repeated mistakes, and s1 q5 clearly explains what was right and what was missing. However, s1 q5 and q6 immediately reveal the full correction instead of offering a guiding question, which I also noted in my c1 review. The reviewer should check verdict accuracy, specific explanations, personalization, and whether feedback gives learners a chance to self-correct when appropriate. I want a maximum of two review passes, with drafts stored in drafts/ and review findings saved in review-records/.

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/grade-reviewer.md, tutor/.claude/skills/grade/SKILL.md
- Why: Grading had no second reader, and s1 q5 and q6 went straight to the full correction with no chance to self-correct; a grade-reviewer re-judges every verdict before reading the draft and checks that feedback is specific, explains enough, follows PREFERENCES.md and gives a partial answer one "Try first:" question, and the grade skill now drafts in drafts/, revises at most twice, writes grades/ once and records each pass in review-records/NNNN-sN-grade.md.


 ### Round 3

**Run:** bench/runs/_live/20261116-153742-agent-architecture-m30-r1, grade-s1 and teach

  **My thoughts:**

The grade reviewer made a small improvement. In q5 and q6, it added "Try first:" questions that encourage the learner to think about what is missing. However, the full correction still appears immediately afterward, so there is no real chance to answer first. The review record reported one pass with no findings, which suggests the feedback was already strong, but the reviewer missed this remaining issue.

For the lesson, I want to build four separate reviewers, adding one per round, so the teach loop can support more reviewers later. I want to start with a facts reviewer, since the c1-skills lesson missed a key fact and did not fully explain what happens when the context limit is exceeded. In "Keeping the context lean," it also said "Bigger is not free" without clearly explaining caching or why larger windows still need context management. In the latest lesson's "Between sessions: notes," saved training information is treated as sufficient for booking without verifying it. The reviewer should check that key facts are covered, calculations and examples are consistent, and safety-related claims are properly supported. It must verify claims using WebSearch and WebFetch and cite sources for corrections, rather than relying on its own judgment.

The lesson loop should have a maximum of two review passes, keep intermediate drafts in drafts/ rather than lessons/, and save reviewer findings and changes in review-records/.

  **What changed:**

  - Kind: new subagent
  - Files: tutor/.claude/agents/lesson-facts-reviewer.md, tutor/.claude/skills/teach/SKILL.md
  - Why: The c1-skills lesson missed a key fact, never said what happens past the context limit, said "bigger is not free" without the reason, and treated saved training status as enough; a lesson-facts-reviewer with those checks verifies the lesson's key claims with WebSearch and WebFetch and names a source for every correction, and the teach skill now drafts in drafts/, revises at most twice, writes lessons/ once and records each pass in review-records/NNNN-lesson.md, with a table of reviewers the next teach reviewers join.



### Round 4

  **Run:** bench/runs/_live/20261116-155624-agent-architecture-m30-r1, teach

  **My thoughts:**

**My thoughts:**

The facts reviewer improved the lesson by addressing the gaps I identified in Round 3. "What is kept between steps" now explains context-limit errors, caching, and why larger windows still need management. "What is kept between sessions" also separates verified training records from agent-written notes and makes it clear that booking permissions must be enforced in code. I agree with these corrections because they make the examples more accurate. However, the section on context growth became denser, introducing several technical concepts together. The run took about 6.8 minutes and 15 web lookups, which feels expensive for one lesson, although the factual improvements were useful.

Next, I want to add a Teaching Quality reviewer alongside the facts reviewer. It should check that each section starts with a concrete example, introduces one concept at a time, explains why each step works, and includes useful practice. In my c1-skills review, I noted that some sections were too long, and the latest "What is kept between steps" section still combines context growth, caching, API errors, and compaction. The pedagogy reviewer should catch this kind of overload while preserving technical accuracy and the existing practical examples. I would also like the loop to retain each draft version so I can compare what changed between passes.

  **What changed:**

  - Kind: new subagent
  - Files: tutor/.claude/agents/lesson-pedagogy-reviewer.md, tutor/.claude/skills/teach/SKILL.md
  - Why: The facts reviewer's corrections made "What is kept between steps" carry context growth, caching, API errors and compaction at once, and nothing checked how the lesson teaches; a lesson-pedagogy-reviewer runs beside the facts reviewer and checks example first, one concept per section, a real reason in each "Why this works", useful practice and density, and the teach skill now keeps every correct fact when the two disagree and fixes overload by splitting or moving it.
    

### Round 5

   **Run:** bench/runs/_live/20261116-194003-agent-architecture-m30-r1, teach

  **My thoughts:**

The Teaching Quality Reviewer helped fix my Round 4 concern. "What is kept between steps" now focuses on context growth, while "Keeping the history small" explains tool-result clearing separately. I agree with the reviewer findings that moved examples before definitions and split explanations covering multiple ideas. However, the final note in "Finding the right page: retrieval" still combines safety rules, context limits, and compaction. The record also shows two teaching-quality findings declined because the loop reached its cap. The run took 9.9 minutes compared with 6.8 minutes for the facts reviewer alone. Finding another 17 issues in pass 2 suggests that revisions can introduce new problems, so I would keep the two-pass limit and prioritize the most important fixes.

Next, I want an Overall Quality Reviewer to focus on the finished lesson's presentation rather than repeat the facts and teaching checks. It should evaluate whether the lesson has a clean, consistent layout, appropriate length, readable figures, and useful references. I especially want it to check whether diagrams are visually clear, well-structured, logically arranged, and easy to follow, with consistent labels, arrows, colors, and spacing. The reviewer should also ensure that visuals support the explanation rather than add unnecessary clutter. This would help make the lesson more polished and visually engaging without duplicating the other reviewers' responsibilities.

  **What changed:**

  - Kind: new subagent
  - Files: tutor/.claude/agents/lesson-quality-reviewer.md, tutor/.claude/skills/teach/SKILL.md
  - Why: No reviewer looked at the finished page, its layout, length, figures and references, and a closing note in the retrieval section still crammed several ideas together; a lesson-quality-reviewer joins the teach loop and checks every figure's SVG for overlapping or tiny labels, misplaced arrows, uneven spacing and colors that break dark mode, plus layout drift, length and the Go further links, ranking findings by severity, and the teach skill now fixes the most important findings first within the two-pass cap.


### Round 6

**Run:** bench/runs/_live/20261116-205953-agent-architecture-m30-r1, teach

**My thoughts:**

The Overall Quality Reviewer improved the lesson's presentation. The diagrams in "The context window: what the model sees" and "Retrieval: finding the right page" are cleaner and easier to follow. The section times now add up to 30 minutes, and "Go further" includes useful references. I agree with correcting "third" to "second" and keeping explanations that add value. However, some content still feels repetitive. The run took 11.1 minutes compared with 9.9 minutes previously, so the improvements were useful, but the additional length and runtime are worth monitoring.

For the final round, I want an Alignment Reviewer to check whether every section, example, and practice question directly supports the learning objective and the learner's makerspace project. In my c1-skills review, "Worked example and practice" was useful because it connected the concepts to real design decisions. However, the latest lesson introduces three information-storage choices in the introduction but asks learners to classify information into "four spots" in the worked example. The reviewer should catch unexplained changes in scope, off-topic content, and missing connections to the learning goal without duplicating the facts, teaching quality, or presentation checks. I would also like every draft version preserved for comparison and the grade reviewer's "Try first:" questions to give learners a chance to think before revealing the full answer.

  **What changed:**

  - Kind: new subagent
  - Files: tutor/.claude/agents/lesson-alignment-reviewer.md, tutor/.claude/skills/teach/SKILL.md
  - Why: No reviewer checked the lesson against its objective and the learner's mission, so the opening promised three storage choices while the worked example used four, and an example could still treat saved notes as verified records; a lesson-alignment-reviewer joins the teach loop and checks that every part of the objective is taught, every section serves it, every count and promise matches, the level fits, examples come from the mission and no example teaches a habit that would hurt the learner's project, and the teach skill now fixes those findings right after anything misleading.


## Major review

 **Run:** bench/runs/c2-review/20261117-003217-agent-architecture-m30-r1

**Live tries:**

I asked for a 10-minute lesson on how an agent decides when it is done. The lesson, "How an agent decides when it is done," clearly explained the two exits: the model finishes with end_turn, or the program stops the loop using a turn cap. I liked the Python trace, diagrams, and "Why this works" explanations. However, the order-tracking example could have been connected more closely to the makerspace project.

I then took a two-question quiz on the same objective. q1 tested whether I could identify why a run failed even though the model produced answer text, while q2 asked me to calculate a turn cap within a token budget. Both questions required applying what the lesson taught rather than just recalling definitions.

I scored 2/2, and the grading was accurate and specific. For q2, it explained, "7 calls read 84,000 tokens, while 8 would read 96,000." I also liked that the tutor challenged me with follow-up questions about max_tokens and an incomplete send_email request. Instead of immediately giving the answer, it asked me to reason through the problem first, which matched my learning preferences.

### Lesson

#### Technical correctness and facts

Rating: 4

The lesson is technically accurate overall, and the facts score improved from 0.83 in c1-skills to 1.00. In "The context window: all the model sees," it now explains the window limit and the "prompt is too long" error, addressing the missing fact from my earlier review. "What is kept between steps" also explains repeated token costs and caching. I liked that "Between sessions: notes" distinguishes verified training records from model-written notes. However, the clearing section still introduces several technical cautions together, and the lesson could explain them more simply. These are minor issues rather than major factual errors.

#### Pedagogy

Rating: 4

The lesson teaches the concepts clearly, starting with practical makerspace examples before introducing definitions. I liked how "What is kept between steps" uses a Python trace and token calculations, followed by a "Why this works" explanation. The earlier c1-skills problem of introducing several concepts at once has mostly been resolved, with separate sections for context growth, clearing, notes, and retrieval. The practice questions also help reinforce each concept. However, "Long manuals: retrieval" still introduces chunking, search scoring, memory comparison, and token costs in one section, making it slightly dense for a beginner. Overall, the teaching is much better structured, with a few areas that could be simplified.

#### Alignment with the learning goal

Rating: 4

The lesson stays focused on O3 and connects the concepts to the learner's makerspace project through examples involving machine manuals, training records, and bookings. I liked how "Worked example and practice" asks learners to decide where information belongs, which directly supports the learning objective. The earlier mismatch between three and four storage choices is mostly resolved. The practice now uses three boxes: context, saved records, and manual chunks. However, some information, such as Saturday's calendar results, can exist both in external storage and in the context after a tool call, so this distinction could be explained more clearly. Overall, the alignment reviewer improved the consistency, with only minor ambiguity remaining.

#### Overall quality

Rating: 4

I would want to learn from this lesson because it is well organized, visually clear, and supported by useful references. The diagrams in "What is kept between steps" and "Long manuals: retrieval" make it easier to understand how context grows and how information moves between storage and the model. The length ratio improved from 0.66 to 0.80, and the extra content feels useful rather than just longer, especially the worked examples and misconception boxes. However, some explanations are still repetitive, and "When the context fills up: clearing" feels slightly dense. Overall, the quality reviewer improved the presentation and readability, though the lesson could still be tightened.

### Quiz

#### Difficulty

Rating: 4

The quiz is more challenging than the c1-skills version because it uses practical scenarios that require reasoning rather than simply recalling definitions. The earlier q1 problem is mostly fixed, as the new q1 requires understanding whether the model controls the next step. I liked q3 because it applies the concept to a real cost calculation, while q5 requires choosing between a workflow and an agent based on the task. However, q2 is still too straightforward, and q4 and q5 give strong clues to the correct answers. The reviewer improved the difficulty without making the quiz too hard, but a few questions still need more thought-provoking distractors.

#### Coverage of the lesson's core

Rating: 4

The quiz covers the main parts of O4 well, especially identifying who controls the next step and deciding when a fixed workflow is better. q1 and q2 test the difference between workflows and agents, while q4 and q5 apply that understanding to practical design decisions. q3 also connects the choice to the learner's goal of keeping model costs low. However, q6 is slightly ambiguous because searching manuals does not always require an agent. Overall, the quiz stays focused on the objective without drifting into unnecessary details.

#### Wording and possible misreadings

Rating: 3

The quiz reviewer caught several wording problems, but some remain after two passes. Like q5 in my c1-skills review, the new q5 still gives clues through the phrase "each chosen from the last result," which points toward an agent for log searches. q4 also hints at option d by emphasizing that the calendar must be checked before every booking. More importantly, q6 can be read two ways because searching manuals could use either an agent or a fixed retrieval workflow. The key assumes adaptive searching, but the stem does not clearly require it. I agree with the intended answer, but the ambiguity should have been fixed.

#### Writing quality

Rating: 4

The questions are mostly clear and concise, and the answer key provides useful explanations rather than just repeating the correct answer. I liked how q1 explains why using model outputs does not automatically make a system an agent, and q3 shows the calculation step by step. The rationale for q5 also explains why the other designs are less suitable. However, q6's rationale assumes the search steps depend on previous results, which the question itself does not clearly state. Overall, the rationales are helpful, but a few items need clearer wording.

#### Alignment with the learning goal

Rating: 4

The quiz aligns well with O4 by testing whether learners can distinguish workflows from agents based on who controls the next step. q1 and q2 test this distinction directly, while q4 and q5 ask learners to choose an appropriate design for practical situations. q3 also supports the learner's goal of building cost-efficient agents. However, q6 could better explain why adaptive control flow is necessary instead of assuming that searching multiple manuals requires an agent. Overall, the quiz stays focused on the learning objective with only minor gaps.

### Feedback

#### Useful

Rating: 4

The feedback is useful because it identifies the learner's mistakes and explains what to improve next. In s1 q4, it connects the mistake to q2, saying, "This is the same mistake as q2: the program runs the tools, not the model," which helps identify a repeated misconception. In s2 q3, it explains why repeating the same failed attempt will not help and recommends a stopping condition. However, the "Try first:" questions in s2 q4 and q6 are immediately followed by the complete answers, leaving no chance for the learner to think independently. Overall, the feedback is specific and actionable, but the hint-first approach needs improvement.

#### Explains enough

Rating: 5

The grade reviewer maintained the standard I rated 5 in c1-skills. The feedback clearly explains why answers are correct, wrong, or partial without being too lengthy. In s1 q5, it acknowledges what the learner understood and explains the missing reasoning: how the model uses the tool result to decide its next step. In s2 q4, it explains why the answer of 4 calls is correct but the reasoning about the model running tools is wrong. The "Try first:" questions add useful prompts for reflection, but the complete answers immediately follow them, reducing their effectiveness. Overall, the explanations are accurate, concise, and sufficient to correct misunderstandings.

#### Personalized to how I like things explained

Rating: 3

The feedback mostly matches my preferences for concise, direct explanations that identify what went wrong and why. In s1 q4, it connects the mistake to q2, helping the learner recognize a repeated misconception. However, s2 q6 asks, "What else would the model need to tell them apart?" and immediately reveals the answer. My PREFERENCES.md asks for hints that let me think before seeing the correction. In my live try, the tutor gave me that opportunity, so this grading feedback still needs improvement.

### Compared with the previous step

The grade reviewer maintained the accurate, personalized explanations from c1-skills and improved the summary in s2 by focusing on one misconception. However, the main issue remained: the "Try first:" questions still reveal the full answer immediately. The reviewer identified this problem but declined the findings, so the improvement was limited.

### What the next step should fix

The next step should make the hint-first approach genuinely interactive by letting learners respond to a guiding question before showing the complete explanation. It should also make the grade reviewer check whether feedback follows PREFERENCES.md, rather than accepting a "Try first:" question simply because it is present.
