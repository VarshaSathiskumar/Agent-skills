---
name: review-session
description: Run a short review session in the chat built from the learner's own past mistakes - the graded quiz items they got wrong or partly right, the misconceptions in their grades and learning records - as a few new practice questions, one at a time, that never repeat an earlier quiz or practice question; use it when the learner asks to review, practise, revise, go over their mistakes or work on their weak spots.
argument-hint: "What would you like to review? (leave empty to review your recent mistakes)"
---

# Review session

You run a short practice session on what this learner got wrong before.
It is not a quiz and not a lesson: a few new questions, each aimed at one mistake they actually made, answered one at a time, with feedback after each, so the mistake gets worked on instead of re-read.

## The request

$ARGUMENTS

If the request above is empty, it is the learner's latest message.
When it names a topic, an objective or a quiz, review the mistakes on that; otherwise, the most recent ones.
Do not stop to ask first: there may be no one to answer before the session ends, so start the session in this reply.

## Read first

The current directory is the workspace root.
Use Read, Glob and Grep to look around and Write for files; this job needs no shell.

1. `PREFERENCES.md`: how this learner likes to be asked and corrected, their kind of example, the length and the tone.
2. `MISSION.md` and `NOTES.md`: what they are building and what they know.
3. Every file in `grades/`: each item's verdict, misconception id and feedback, and each summary's "idea to work on".
4. Every file in `learning-records/`: which misconceptions are still open and which a later record shows corrected.
5. Every file in `quizzes/` and in `practice/`: every question already asked, so you repeat none.
6. The lesson in `lessons/` on the objective you will review, if there is one, for the section to point back to.

Never open `keys/`: the grades already say what was wrong and why, and this job needs nothing more.
Never write under `.claude/`, and never change `PREFERENCES.md`, `FORMATS.md`, or a quiz, grade or submission.

## Choose what to review

1. **List the mistakes**: every `wrong` or `partial` item in `grades/`, with its quiz, its misconception id (or `null`) and the mistake its feedback names.
2. **Drop what is settled**: a misconception that a later learning record or a later graded item shows corrected.
3. **Pick one or two targets**: the misconceptions that explain the most items, most recent first; a `null` partial mistake, such as a missing reason, counts as a target of its own.
   One idea at a time works better than a tour of every mistake.
4. **No grades yet**: when `grades/` is empty, or nothing is left to review, say so in a sentence and offer a quiz instead. Do not invent mistakes.
5. **Ungraded quizzes stay closed**: a quiz with no grade yet is never a source, and no practice question may be a reworded item of it.

## Write the practice

Three to five questions in all, for the one or two targets.

- **New every time.** A new scenario, with a different system, tool or numbers, from the kind of example `PREFERENCES.md` and `MISSION.md` point to. Never reuse a stem, a scenario or a set of numbers from `quizzes/` or from an earlier file in `practice/`; a question that only swaps a word of an old one is a repeat.
- **Aimed.** Each question is one the learner gets wrong if they still hold the misconception, and right only if they have fixed it. Name for yourself which mistake each question tests and what a wrong answer would show.
- **Reasoning, not recall.** Ask what happens, which choice fits and why, or what goes wrong; never for a definition.
- **Short answers.** A sentence or two, or one choice with its reason; a closed-choice question has three or four options with no giveaway in the wording.
- **Climbing.** The first question is the plainest case of the mistake; the last puts it in a case closer to the learner's project.

Write the session to `practice/NNNN-<slug>.md` before the first reply, numbered after the last file there (`0001` when there is none), in this shape:

```md
# Practice NNNN: <the idea being reviewed>

- Targets: <misconception ids or the named mistakes>, from <grades/NNNN-sN.json item ids>
- Lesson to reread: <lessons/... section, or none>

## P1
- Tests: <the mistake>
- Question: <the question as asked>
- Answer: <the right answer and why, in a sentence or two>
- Learner: <filled in when they answer: their answer, and right, partly right or not yet>

## P2
...
```

## Run the session

**The first reply** says in one or two sentences what you will review and why, naming the quiz items it comes from, then asks P1 and stops.
Ask one question per reply, never the whole set at once.

**After each answer**, give feedback in the same order as a grade, in at most about 80 words:

1. Whether it is right, partly right or not yet, in their terms.
2. For partly right or not yet: the exact part of their answer that is off. For partly right, give them one short "Try first:" question about the gap before you explain, and wait for their reply.
3. The correct reasoning, in one or two sentences, with the question's own case.

Then fill in the `Learner:` line in the practice file, and ask the next question.
When an answer shows the mistake is still there, make the next question another plain case of the same mistake instead of climbing; when two answers in a row are right, move on.
If the learner asks for the answer before trying, ask them for their best guess first, once, then explain.

**To finish**, after the last question or when the learner stops:

- One or two sentences on what they now get right, and what, if anything, still needs work, with the lesson section to reread.
- A learning record, as `FORMATS.md` describes, when the answers show a misconception corrected, or show it still open; its evidence names the practice file and the question ids.
- A line in `NOTES.md` on what changed.

## Before you send each reply

- One question in it, and no answer given away before they try.
- No question repeats an earlier quiz or practice question, and none rewords an ungraded quiz item.
- Feedback names something this learner wrote, not a general explanation of the topic.
- The tone and length follow `PREFERENCES.md`.
