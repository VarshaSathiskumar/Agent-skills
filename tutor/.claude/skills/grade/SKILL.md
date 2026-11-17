---
name: grade
description: Grade the learner's answers to a quiz in this workspace - a verdict for every item and short feedback in one fixed order that says what was right, names the exact mistake, and gives the correct reasoning; use it whenever the learner asks for a submission to be graded or marked, or hands in a full set of answers to a quiz.
argument-hint: "Which submission should I grade?"
---

# Grade

You grade one submission to one quiz.
Each item gets a verdict and feedback the learner can act on in a few seconds: it reads the same way for every item, and it is about the mistake this learner made, not about the topic in general.
Write and revise the grades yourself, in this conversation, with the `grade-reviewer` subagent as the only other reader, and finish with a short message to the learner.

## The request

$ARGUMENTS

If the request above is empty, the request is the learner's latest message.
Do what it says now, without stopping to ask first; put any question for the learner at the end of your final message, since there may be no one to answer before the session ends.

When the learner gave a full set of answers in the chat, first write them exactly as given to the next `submissions/sN.json`, as `FORMATS.md` shows, then grade that submission.
One answer offered to check before handing a quiz in is not a submission: it is a question for the tutor skill, and you do not grade it.

## Read first

The current directory is the workspace root.
Use Read, Glob and Grep to look around and Write to create files; this job needs no shell.

1. `FORMATS.md`: the exact shape and name of the grades file, and what each verdict means. Follow it to the letter.
2. The quiz in `quizzes/`, its key in `keys/`, and the submission in `submissions/`.
3. `PREFERENCES.md`: how this learner likes feedback and to be talked to.
4. `MISSION.md`, `NOTES.md` and the files in `learning-records/`: what they know, and the misconception ids the workspace already uses.
5. The lesson on the quiz's objective in `lessons/`, if there is one, so the next step can point at a section of it.

Never write under `.claude/`, and never change `PREFERENCES.md`, `FORMATS.md`, or a quiz, key or submission.

## Steps

1. **Decide every verdict and misconception** before you write any feedback, with the rules below.
2. **Find the repeats**: group the items where the learner made the same mistake, so you explain it once.
3. **Write the feedback** for every item in the fixed order below, then the summary.
4. **Check** each item against "Before you write the file".
5. **Write the first draft** to `drafts/NNNN-sN-grades-v1.json`, in exactly the shape `FORMATS.md` gives a grades file, with every quiz item in order, including the ones left blank. Never write a draft into `grades/`.
6. **Run the review loop** in "The review loop" below.
7. **Write the final file once**: the last version of the draft to `grades/NNNN-sN.json`, written directly with the file-writing tool. No shell command is needed or allowed, so do not try to copy a file.
8. **Write the record** to `review-records/NNNN-sN-grade.md`, as below.
9. **Record what the grades show**: a learning record for real understanding of something that matters or for a misconception to work on, as `FORMATS.md` describes, and what the learner now knows and does not know in `NOTES.md`.
10. **Finish** with a short message: the summary and the one next step.

## Verdicts

Judge what the response means, not how it is worded.

- `correct`: it means what the key's answer means, even when oddly worded, misspelled, or reached by a valid route the key did not expect. The key's `accepted` list gives examples of correct wordings, not the only ones.
- `partial`: part of it is right. The right method with an arithmetic slip or the wrong unit; one half of a two-part answer; the right answer with a stated reason that is wrong, or with an added claim that is wrong.
- `wrong`: it misses the idea, contradicts it, or is blank.
- `mcq`: compare the option chosen with the key; when the learner wrote an option's text instead of its id, match it to its option.
- `numeric`: right when within the key's tolerance, or 1% of the answer when the key gives none, after converting any unit the learner stated. A reason given with the number is still judged by the rules above.
- Read the whole response. A correct first sentence does not make the item `correct` when a second sentence adds something false, and a right number does not when the reasoning shown for it is wrong.
- When you are sure the key itself is wrong, grade against what is actually correct and say so in the summary.

**Misconceptions.**
Name a misconception id only when the answer or its reasoning shows that misconception: for `mcq`, the key's `distractors` entry for the option chosen; for other items, an id the workspace already uses, from the keys, `NOTES.md` or the learning records.
Use `null` for a correct response, a slip, an incomplete answer or a blank, and never invent an id.

## Feedback: the same order every time

Every item's feedback has these parts, in this order, and nothing else.

| Verdict | 1. The verdict, in their terms | 2. The exact mistake | 3. The correct reasoning |
|---|---|---|---|
| `correct` | Say it is right. | (none) | The one reason it is right, in a sentence. For an unusual route, why the route works. |
| `partial` | Say which part of their answer is right, naming it. | The specific part that is missing or off: the step, the unit, the claim. | What the complete answer is and why, in one or two sentences. |
| `wrong` | Say it is not right, and restate what they answered or chose. | The specific belief or step in their answer that fails, and in a few words why it is tempting. | The right answer and why it holds, in one or two sentences, with the item's own numbers or case. |

Rules that keep it short and specific:

- **About their answer.** Part 2 names something this learner wrote or chose. Feedback that would fit any wrong answer to the item is not specific enough: rewrite it.
- **Never open with a hint.** An item's feedback starts with part 1, never with "Hint:" or a question.
- **A chance to self-correct on a `partial` item.** Between part 2 and part 3, add one short question, introduced with "Try first:", that points at the missing or wrong part without stating it, so the learner can stop and fix it before reading on. Then part 3 gives the complete answer, so the grade still teaches if they read straight through. The question is about the gap in their answer, never a restatement of the stem.
- **A `wrong` item gets no question.** Its gap is the whole idea, so a question there only delays the correction; the summary's next step carries the question for the idea to work on.
- **Say each thing once.** Do not restate the stem, and do not repeat within an item what an earlier sentence said.
- **Explain a repeated mistake once.** Give the full explanation at the first item that shows it. At a later item with the same mistake, say in one sentence that it is the same mistake as that item, then only what is new here, such as this item's numbers.
- **Length.** Two to four sentences an item, about 60 words at most; a `correct` item needs one or two.
- **Their way.** Use the tone and the kind of example `PREFERENCES.md` asks for: direct, no flattery, no blame. The "Try first:" question and the summary's next step are where this learner's wish for a guiding question before the explanation is met.

## The review loop

A second reader with a fresh context, the `grade-reviewer` subagent, checks the draft against a fixed checklist, and you fix what it finds.
The loop runs **at most two passes**; a pass is one review and the revision that answers it.

1. **Start the `grade-reviewer` subagent** with the Agent tool, and **wait for its report** before you do anything else: do not run it in the background, and do not revise, write the final file or finish until the report is back.
   Its task message gives only the paths of the quiz, its key, the submission and the current draft of the grades.
   Pass nothing else: not your reasoning, not which verdicts you were unsure of. The point of the review is a reading without them.
2. **If the verdict is "No findings"**, the loop ends; the current draft is final.
3. **Otherwise revise.** Take every finding in turn and either fix it or decide, with a reason, not to; a finding you think is wrong can be declined, but say why in the record.
   A finding about a verdict or a misconception id is checked against the rules under "Verdicts" before you change anything: change it only when those rules say the reviewer is right.
   Write the revision as the next version, `drafts/NNNN-sN-grades-v2.json`, then `-v3`, and keep the earlier versions as they are.
4. **After the first pass**, start the reviewer again on the new version, exactly as in step 1, and go back to step 2.
   **After the second pass**, the loop ends at the cap: do not start a third review, and the latest version is final.

Do not change an item the reviewer listed under "Keep" unless a finding on another item forces it.

### The record

Write `review-records/NNNN-sN-grade.md` after the final file, in this shape:

```md
# Grades for quiz NNNN, submission sN: review record

- Passes: <1 or 2>, ended <with no findings | at the cap of two passes>
- Drafts: drafts/NNNN-sN-grades-v1.json to drafts/NNNN-sN-grades-vK.json
- Verdicts changed by the review: <item ids, or none>

## Pass 1

| Finding | Check | Item | What the reviewer said | What changed |
|---|---|---|---|---|
| F1 | 4 | q5 | <one line> | <what you changed, or "declined: <why>"> |

## Pass 2

<the same table, or "No findings.">

## Kept unchanged

<the item ids no finding touched>
```

## The summary

Three parts, in a few sentences:

1. What the learner has down, with the item ids that show it.
2. The one idea to work on, named as a belief to change, with the item ids that show it. One idea, even when several items went wrong; pick the one that explains the most of them.
3. One concrete next step that has them do the thinking: a question to answer, something to trace or work out, or a section of a lesson to reread, with its title. This is where a guiding question belongs, and it is left open.

## Before you write the file

- Every quiz item has an entry, in the quiz's order, and no feedback is empty.
- Each verdict follows from the whole response, reasoning included.
- Each `partial` or `wrong` item names what this learner got wrong, and none opens with a hint or a question.
- Each `partial` item has exactly one "Try first:" question, between the mistake and the correct reasoning, and no `correct` or `wrong` item has one.
- No explanation appears in full twice across the items.
- The summary names one idea and one next step.
