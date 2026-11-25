---
name: grade
description: Grade the learner's answers to a quiz in this workspace - a verdict for every item and short feedback in one fixed order that says what was right, names the exact mistake, and gives the correct reasoning; use it whenever the learner asks for a submission to be graded or marked, or hands in a full set of answers to a quiz.
argument-hint: "Which submission should I grade?"
---

# Grade

You run the grading of one submission to one quiz.
The answer keys in `keys/` are closed to this conversation: a guard blocks every read, search or listing of them here, and it is not to be worked around.
So the grading itself is done by the `grader` subagent, the only agent allowed to read the key; the `grade-reviewer` subagent checks its draft; and you start them in turn, write the final files, and finish with a short message to the learner.

## The request

$ARGUMENTS

If the request above is empty, the request is the learner's latest message.
Do what it says now, without stopping to ask first; put any question for the learner at the end of your final message, since there may be no one to answer before the session ends.

When the learner gave a full set of answers in the chat, first write them exactly as given to the next `submissions/sN.json`, as `FORMATS.md` shows, then grade that submission.
One answer offered to check before handing a quiz in is not a submission: it is a question for the tutor skill, and you do not grade it.

## Read first

The current directory is the workspace root.
Use Read, Glob and Grep to look around and Write to create files; this job needs no shell.
Never open anything in `keys/`: you only need its path, `keys/NNNN.json`, named after the quiz.

1. `FORMATS.md`: the shape and name of the grades file and of a learning record.
2. The submission in `submissions/`, to know which quiz it answers, and that quiz in `quizzes/`.
3. `PREFERENCES.md`: how this learner likes to be talked to, for your final message.
4. `NOTES.md` and the files in `learning-records/`, so what you record next fits what is there.

Never write under `.claude/`, and never change `PREFERENCES.md`, `FORMATS.md`, or a quiz, key or submission.

## Steps

1. **Start the `grader` subagent** for the first draft, with the Agent tool, and wait for its report. Its task message gives the paths of the quiz, its key and the submission, and the path to write to, `drafts/NNNN-sN-grades-v1.json`, and nothing else.
2. **Run the review loop** in "The review loop" below.
3. **Write the final file once**: read the last version of the draft and write it to `grades/NNNN-sN.json`, unchanged, directly with the file-writing tool. No shell command is needed or allowed, so do not try to copy a file. Never write a draft into `grades/`.
4. **Write the record** to `review-records/NNNN-sN-grade.md`, as below.
5. **Record what the grades show**: a learning record for real understanding of something that matters or for a misconception to work on, as `FORMATS.md` describes, and what the learner now knows and does not know in `NOTES.md`, both from the final grades.
6. **Finish** with a short message: the summary and the one next step from the final grades.

Never write or change a verdict, a misconception id or an item's feedback yourself: only the grader decides them, because only it has read the key.

## The review loop

A second reader with a fresh context, the `grade-reviewer` subagent, checks the draft against a fixed checklist, and the grader answers what it finds.
The loop runs **at most two passes**; a pass is one review and the revision that answers it.

1. **Start the `grade-reviewer` subagent** with the Agent tool, and **wait for its report** before you do anything else: do not run it in the background, and do not start the grader, write the final file or finish until the report is back.
   Its task message gives only the paths of the quiz, its key, the submission and the current draft of the grades.
   Pass nothing else: not the grader's report, not which verdicts were in doubt. The point of the review is a reading without them.
2. **If the verdict is "No findings"**, the loop ends; the current draft is final.
3. **Otherwise start the `grader` again** to revise, and wait for its report. Its task message gives the paths of the quiz, its key, the submission and the current draft, the reviewer's findings word for word, and the path of the next version, `drafts/NNNN-sN-grades-v2.json`, then `-v3`.
4. **After the first pass**, start the reviewer again on the new version, exactly as in step 1, and go back to step 2.
   **After the second pass**, the loop ends at the cap: do not start a third review, and the latest version is final.

### The record

Write `review-records/NNNN-sN-grade.md` after the final file, from the reviewers' and the grader's reports, in this shape:

```md
# Grades for quiz NNNN, submission sN: review record

- Graded by: the grader subagent
- Passes: <1 or 2>, ended <with no findings | at the cap of two passes>
- Drafts: drafts/NNNN-sN-grades-v1.json to drafts/NNNN-sN-grades-vK.json
- Verdicts changed by the review: <item ids, or none>

## Pass 1

| Finding | Check | Item | What the reviewer said | What changed |
|---|---|---|---|---|
| F1 | 4 | q5 | <one line> | <what the grader changed, or "declined: <why>"> |

## Pass 2

<the same table, or "No findings.">

## Kept unchanged

<the item ids no finding touched>
```
