---
name: quiz
description: Write a quiz and its answer key for the learner in this workspace, made of short scenario questions that test reasoning rather than recall of a definition; use it whenever the learner asks for a quiz, to be tested, or to check what they know.
argument-hint: "What should the quiz cover, and how many questions?"
---

# Quiz

You write one quiz and its key for this learner.
A good quiz here makes the learner reason about a situation they have not seen, and a poor one lets them match a definition they just read.
Do the job yourself, in this conversation and in one pass, and finish with a short message to the learner.

## The request

$ARGUMENTS

If the request above is empty, the request is the learner's latest message.
Do what it says now, without stopping to ask first; put any question for the learner at the end of your final message, since there may be no one to answer before the session ends.

## Read first

The current directory is the workspace root.
Use Read, Glob and Grep to look around and Write to create files; this job needs no shell.

1. `FORMATS.md`: the exact shape of the quiz and key files, their numbering and their JSON keys. Follow it to the letter.
2. `MISSION.md`, `NOTES.md` and every file in `learning-records/`: what the learner is building, what they know, and which misconceptions already have ids.
3. `PREFERENCES.md`: the examples this learner relates to and how dense they like things. The scenarios come from here.
4. The lessons on the objective in `lessons/`, if any, and the earlier files in `quizzes/` and `keys/`, so you repeat no item and reuse the misconception ids.

Never write under `.claude/`, and never change `PREFERENCES.md`, `FORMATS.md`, or an existing quiz, key or submission.

## Steps

1. **Pin down the objective**, its id and the number of items asked for; with no number, write five.
2. **List the core**: the three to five ideas a learner must get right to have met the objective, from its lessons or, when there are none, from a high-trust source you search for and read. Every item tests one of them; skip side details and phrasing a lesson happened to use.
3. **List the misconceptions** this learner has or is likely to have about that core, with their ids from the workspace.
4. **Write the items** as the next section describes.
5. **Check every item** with the four tests below, and rewrite any that fails.
6. **Write** `quizzes/NNNN.json` and `keys/NNNN.json` exactly as `FORMATS.md` shows.
7. **Finish** with a short message: the quiz's path, what it covers, and nothing from the key.
   When the objective has no lesson yet, say that the quiz is ahead of the lessons; do not write a lesson unless asked for one.

## Writing items that test reasoning

**Start every item from a situation, not from a term.**
The stem describes a small, concrete case and asks the learner to do something with it: predict what happens, pick the design that fits a stated constraint, find the mistake, trace the steps, or compute a quantity.

- Take the situations from the kinds of example `PREFERENCES.md` names and from the project in `MISSION.md`, and use a different situation for each item, so no item helps with another.
- Keep the situation short: two or three plain sentences with only the facts the answer depends on, including every number, unit and constraint. A learner who knows the idea can answer without a lesson open.
- When an item asks for the best or the right choice, the stem says best for what: the cost, the latency, the failure it must survive.

A recall item and the same idea as a reasoning item, on a database topic:

| Recall, do not write this | Reasoning, write this |
|---|---|
| "What does a database index do?" | "A lookup by `email` on a 2-million-row table takes 4 seconds, and the same lookup by `id` takes 3 ms. Nothing else differs between the two columns. What is the most likely reason?" |

At most one item in a quiz may be plain recall, and only for a term the rest of the quiz depends on.

**Difficulty.**
Most items apply one core idea to a new case.
One or two stretch the learner: they combine two ideas, or ask for a trace of several steps, or put a tempting shortcut in the way.
No item needs knowledge the learner was never given, and the hard items are spread through the quiz, not stacked at the end.

**Types.** Mix them when the objective allows it.

- `mcq` when the wrong answers are predictable. Each distractor is what a learner holding one misconception would pick in this situation, so a wrong pick says something.
  Three to five options, usually four, with the same number of words and the same grammar; vary which position is correct across the quiz.
- `numeric` when the situation has a quantity to work out. State the unit in the stem and in `unit`, and the precision expected.
- `short` when the learner should produce the idea themselves. Ask so that the answer is a word or a short phrase, such as which of two named designs, or what the system does next; the reasoning is in getting there. Never ask for an essay or an open list.

## The four tests

Run these on every item before you write the files.

1. **Answer it cold.** Answer the item from its stem alone, without looking at your key. Rewrite it if you hesitate, or if a careful expert could defend a second answer.
2. **The restating test.** Could a learner get it right by matching the stem or the correct option to a sentence from a lesson or a definition, without thinking about the situation? Then it is recall: change the situation until they have to reason.
3. **The giveaway test.** The correct option is not the longest or the most detailed, repeats no distinctive phrase from the stem that the others lack, and is not the only one that sounds like a definition. No item reveals another item's answer.
4. **The distractor test.** Each wrong option is plausible to someone with the misconception it stands for; none is a joke, and none is also correct under a fair reading.

## The key

- `answer`: the option id, the number in the item's unit, or the shortest complete reference answer for a `short` item.
- `accepted`: for a `short` item, every other wording that is just as correct: synonyms, a symbol, the common phrasings. Be generous here, because an answer is matched against these forms.
- `tolerance`: for a `numeric` item, the absolute tolerance the stem's precision implies.
- `rationale`: one or two sentences that walk the reasoning from the situation to the answer, then what a typical wrong answer shows. Write it the way this learner likes things explained: the answer first, then why it works.
- `distractors`: each wrong option built on a misconception, mapped to its id. Reuse the ids the workspace already has, and never invent one for a misconception that has one.

## A quiz in the chat

When the learner wants to take the quiz in a live session, show its title and each item's stem and options, and never anything from `keys/`.
Collect their answers and write them exactly as given to the next `submissions/sN.json`, as `FORMATS.md` shows, so they can be graded.
