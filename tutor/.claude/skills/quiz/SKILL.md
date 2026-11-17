---
name: quiz
description: Write a quiz and its answer key for the learner in this workspace, made of short scenario questions that test reasoning rather than recall of a definition; use it whenever the learner asks for a quiz, to be tested, or to check what they know.
argument-hint: "What should the quiz cover, and how many questions?"
---

# Quiz

You write one quiz and its key for this learner.
A good quiz here makes the learner reason about a situation they have not seen, and a poor one lets them match a definition they just read.
Write and revise the quiz yourself, in this conversation, with the `quiz-reviewer` subagent as the only other reader, and finish with a short message to the learner.

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
6. **Write the first draft** to `drafts/NNNN-quiz-v1.json` and `drafts/NNNN-key-v1.json`, where `NNNN` is the number the quiz will take in `quizzes/`, in exactly the shapes `FORMATS.md` gives a quiz and a key.
   Never write a draft into `quizzes/` or `keys/`.
7. **Run the review loop** in "The review loop" below.
8. **Write the final files once**: the last version of the draft to `quizzes/NNNN.json` and `keys/NNNN.json`, exactly as `FORMATS.md` shows, written directly with the file-writing tool. No shell command is needed or allowed, so do not try to copy a file.
9. **Write the record** to `review-records/NNNN-quiz.md`, as below.
10. **Finish** with a short message: the quiz's path, what it covers, and nothing from the key.
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

## The review loop

A second reader with a fresh context, the `quiz-reviewer` subagent, checks the draft against a fixed checklist, and you fix what it finds.
The loop runs **at most two passes**; a pass is one review and the revision that answers it.

1. **Start the `quiz-reviewer` subagent** with the Agent tool, and **wait for its report** before you do anything else: do not run it in the background, and do not revise, write a final file or finish until the report is back.
   Its task message gives only:
   - the paths of the current draft quiz and draft key;
   - the objective's id and text, and the number of items asked for.

   Pass nothing else: not your reasoning, not which items you worry about, not the answers. The point of the review is a reading without them.
2. **If the verdict is "No findings"**, the loop ends; the current draft is final.
3. **Otherwise revise.** Take every finding in turn and either fix it or decide, with a reason, not to; a finding you think is wrong can be declined, but say why in the record.
   Write the revision as the next version, `drafts/NNNN-quiz-v2.json` and `drafts/NNNN-key-v2.json`, then `-v3`, and keep the earlier versions as they are.
   Run the four tests below again on every item you changed.
4. **After the first pass**, start the reviewer again on the new version, exactly as in step 1, and go back to step 2.
   **After the second pass**, the loop ends at the cap: do not start a third review, and the latest version is final.

Do not change an item the reviewer listed under "Keep" unless a finding on another item forces it.

### The record

Write `review-records/NNNN-quiz.md` after the final files, in this shape:

```md
# Quiz NNNN: review record

- Objective: <id>, <text>
- Passes: <1 or 2>, ended <with no findings | at the cap of two passes>
- Drafts: drafts/NNNN-quiz-v1.json to drafts/NNNN-quiz-vK.json

## Pass 1

| Finding | Check | Item | What the reviewer said | What changed |
|---|---|---|---|---|
| F1 | 1 | q5 | <one line> | <what you changed, or "declined: <why>"> |

## Pass 2

<the same table, or "No findings.">

## Kept unchanged

<the item ids no finding touched>
```

## The key

- `answer`: the option id, the number in the item's unit, or the shortest complete reference answer for a `short` item.
- `accepted`: for a `short` item, every other wording that is just as correct: synonyms, a symbol, the common phrasings. Be generous here, because an answer is matched against these forms.
- `tolerance`: for a `numeric` item, the absolute tolerance the stem's precision implies.
- `rationale`: one or two sentences that walk the reasoning from the situation to the answer, then what a typical wrong answer shows. Write it the way this learner likes things explained: the answer first, then why it works.
- `distractors`: each wrong option built on a misconception, mapped to its id. Reuse the ids the workspace already has, and never invent one for a misconception that has one.

## A quiz in the chat

When the learner wants to take the quiz in a live session, show its title and each item's stem and options, and never anything from `keys/`.
Collect their answers and write them exactly as given to the next `submissions/sN.json`, as `FORMATS.md` shows, so they can be graded.
