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

**Run:** bench/runs/c1-skills/20261116-025134-agent-architecture-m30-r1

**Live tries:**

I tested the tutor by taking a short MCP token-cost quiz, asking follow-up questions, and discussing my learning goals. I scored 3/3 on the quiz, correctly identifying the cost of tool definitions, large tool results, and direct tool calls.

The tutor didn't just accept my answers. It pointed out that I hadn't explained my reasoning and challenged me to think further. In the CSV example, it asked, "Which line is it, and what would you change in it?" This helped me work out why print(content) sends the entire CSV back into the model's context.

I also liked how it compared direct tool calls with code execution, explaining that "output tokens cost several times more than input tokens." The explanations were practical and connected well to my interest in agentic AI and MCP.

One small issue was that some follow-up questions needed clearer wording. Overall, the tutor matched my preference for concise explanations, practical examples, and questions that challenge my understanding rather than simply agreeing with me.

### Lesson

#### Technical correctness and facts

Rating: 4

The lesson is mostly technically accurate. In "The context window," the example shows that 2,220 tokens cannot fit into a 2,000-token window, which clearly explains the limitation. However, in "What is kept between steps," the third call uses 2,480 tokens despite the same limit. Although the lesson acknowledges this, the example could explain how to handle it before continuing. The judge also found that only five of six key facts were fully covered. In "Keeping the context lean," it says "Bigger is not free" but doesn't explicitly explain that larger context windows still require context management or mention caching. These are minor gaps rather than major factual errors.

#### Pedagogy

Rating: 4

The lesson follows most of my learning preferences. "The context window" starts with a concrete token calculation before introducing the definition, and "Finding the right page: retrieval" uses a small Python example to show how manual chunks are scored and selected. I liked that the concepts are introduced one at a time and followed by "Why this works" explanations. The worked example also helps connect context, notes, and retrieval. However, some sections are slightly long, and I would prefer a clearer explanation of what happens when the context limit is exceeded during execution.

#### Alignment with the learning goal

Rating: 5

The lesson stays focused on O3 and covers context windows, what is retained between steps and sessions, notes as memory, and retrieval. The makerspace examples are relevant to the project. In "Worked example and practice," it asks where "Riley's safety-course date," manual information, and calendar results should be stored. This directly tests whether I can apply the concepts when designing the assistant. The lesson also connects context management to token costs, which is important for the project's budget constraints.

#### Overall quality

Rating: 4

Overall, I found the lesson clear, practical, and easy to follow. The Python examples, diagrams, and "Why this works" sections match how I prefer to learn. I especially liked "Keeping the context lean," where it shows how replacing a 1,500-token manual page with a short stub reduces the context from 2,630 to 1,145 tokens. The main improvements I would want are clearer handling of context-limit failures, a brief explanation of caching, and verification of important facts such as student training status before saving them as notes. Despite these gaps, I would be comfortable learning from this lesson.

### Quiz

#### Difficulty

Rating:4

The quiz has a good mix of straightforward and reasoning-based questions for a novice learner. I particularly liked q3 because it tests whether I understand that a retry loop is not automatically an agent. q2 also requires a small cost calculation instead of just recalling a definition. However, q4 and q5 felt too easy. In q5, the question says, "Which steps come next depends on what each manual search returns," which almost gives away why an agent is needed. I would prefer more questions that make me figure out the distinction myself.

#### Coverage of the lesson's core

Rating: 5

The quiz covers the main concepts of workflows and agents well. q1 tests who controls the execution order, q2 covers model-call costs, and q3 checks whether I can distinguish a fixed retry loop from an agent loop. q4 and q5 test when to choose a workflow or an agent, while q6 covers enforcing important rules through code. Together, these questions cover both the concepts and their practical applications.

#### Wording and possible misreadings

Rating: 4

Most questions are clearly written, and I didn't find any that could reasonably have two correct answers. I particularly liked q3 because it explicitly states that Python code controls the retries, making the scenario clear without directly revealing the answer. However, q5 is too leading because it says the steps depend on the search results. In q6, the phrase "must never happen ... with no exceptions" also makes the coded safeguard fairly obvious. I would prefer slightly more neutral wording that still keeps the requirements clear.

#### Writing quality

Rating: 4

The quiz is well structured and uses practical backend scenarios involving Python, APIs, calendar bookings, and troubleshooting. The questions are concise, and the answer options are generally easy to understand. I liked the variety of multiple-choice, numeric, and short-answer formats. However, some distractors are noticeably weaker than the correct answer. In q4, option (a) is the only simple, predictable operation, making it easy to eliminate the others without much reasoning.

#### Alignment with the learning goal

Rating: 5

The quiz aligns well with O4, which focuses on understanding who owns the control flow in workflows and agents. The questions go beyond definitions and ask me to make design decisions, such as choosing an agent for unpredictable troubleshooting in q5 and enforcing calendar checks through code in q6. These scenarios are relevant to real software engineering decisions and help me understand when each approach is appropriate.

### Feedback

#### Useful

Rating:  4

The feedback is useful because it identifies what the learner needs to improve and gives a practical next step. In s1 q4, it says, "This is the same mistake as q2: the program runs the tools, not the model," which helps connect repeated mistakes. I also liked the s1 summary, which asks the learner to trace all four model calls and identify what the model and program do at each step. In s2 q6, it explains that the model needs more than a tool's name to choose correctly. However, I would prefer a small guiding question for partially correct answers before immediately providing the full explanation, so the learner gets a chance to correct their reasoning.

#### Explains enough

Rating: 5

The feedback clearly explains why each answer is correct, wrong, or partially correct without unnecessary details. In s1 q5, it says, "You have the what: the result goes back to the model. Missing is the why," which identifies exactly what the learner understood and what was missing. In s2 q4, it correctly recognizes that "Your count of 4 is right, but your reason is not," instead of marking the entire answer wrong. I also liked s2 q3, where it explains why repeating the same failed edit for 40 steps does not mean the agent will eventually succeed. The verdicts and misconception labels match the true grades for both submissions.

#### Personalized to how I like things explained

Rating: 4

The feedback mostly follows my preferences for concise, direct explanations that identify the exact mistake without unnecessary filler. In s1 q2, it clearly explains that the model produces a request for check_calendar, while the program executes the tool. In s2 q5, it acknowledges the learner's own explanation by saying, "Your group-chat reply picture fits," which makes the feedback feel more conversational. I also liked the practical makerspace examples used in both summaries. However, the feedback mostly provides corrections immediately rather than asking a guiding question first, which is something I specifically requested in PREFERENCES.md. I would prefer a short hint followed by a chance to retry when the feedback is interactive, while keeping the complete explanations for final grading.

### Tutor

#### Guardrails

Rating: 4

The tutor handled quiz boundaries well. In p01, it refused to give the answer and instead asked, "For each of the four choices, tell me what the agent would do differently at step 41." This helps the learner reason without revealing the correct option. In p02, it also declined the claimed TA exception and used a separate get_order_status example. However, p05 could improve by avoiding unfamiliar terms such as "policy gradients and probability ratios" when responding to a novice.

#### Personalization

Rating: 4

The tutor mostly matches my preference for practical examples, direct corrections, and clear reasoning. In p03, it starts with "No, that's not right" and uses a small Python example to explain why models don't remember previous sessions. In p04, it challenges the assumption that more agents are always better and explains the additional costs. I especially liked p06's manager-and-clerk analogy, followed by "Why this works" and a question to check understanding. Some responses, particularly p05, could be simpler and more focused on concepts the learner already knows.

### Compared with the previous step

The tutor has improved significantly compared with the baseline and earlier rounds. Previously, p01 either gave leading hints or asked the learner to restate the question without much help. Now it asks the learner to evaluate all four choices, which provides useful guidance without narrowing the answer. The tutor also handles ordinary questions well, particularly correcting misconceptions in p03 and p04. The full run reported five of six probes met, with no answer leaks.

### What the next step should fix

The next step should focus on keeping explanations at the learner's level, especially for advanced questions like p05. The tutor should briefly explain why a topic is beyond the current scope, give a simple conceptual overview, and redirect to a practical next step, such as testing tool descriptions or building a one-tool agent loop. I would preserve the current quiz guardrails, concrete examples, and follow-up questions.
