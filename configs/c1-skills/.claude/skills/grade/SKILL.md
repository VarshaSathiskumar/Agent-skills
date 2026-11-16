---
name: grade
description: Grade the learner's answers to a quiz in this workspace - a verdict for every item and short feedback in one fixed order that says what was right, names the exact mistake, and gives the correct reasoning; use it whenever the learner asks for a submission to be graded or marked, or hands in a full set of answers to a quiz.
argument-hint: "Which submission should I grade?"
---

# Grade

You grade one submission to one quiz.
Each item gets a verdict and feedback the learner can act on in a few seconds: it reads the same way for every item, and it is about the mistake this learner made, not about the topic in general.
Do the job yourself, in this conversation and in one pass, and finish with a short message to the learner.

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
5. **Write** `grades/NNNN-sN.json` exactly as `FORMATS.md` shows, with every quiz item in order, including the ones left blank.
6. **Record what the grades show**: a learning record for real understanding of something that matters or for a misconception to work on, as `FORMATS.md` describes, and what the learner now knows and does not know in `NOTES.md`.
7. **Finish** with a short message: the summary and the one next step.

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
- **No hint before the answer.** A grade is read once, with the answer right below, so a guiding question that the next sentence answers is noise. Never open with "Hint:", and ask no question the feedback then answers itself. Keep the learner's wish to work it out for themselves for the summary's next step.
- **Say each thing once.** Do not restate the stem, and do not repeat within an item what an earlier sentence said.
- **Explain a repeated mistake once.** Give the full explanation at the first item that shows it. At a later item with the same mistake, say in one sentence that it is the same mistake as that item, then only what is new here, such as this item's numbers.
- **Length.** Two to four sentences an item, about 60 words at most; a `correct` item needs one or two.
- **Their way.** Use the tone and the kind of example `PREFERENCES.md` asks for: direct, no flattery, no blame. Where a preference asks for a hint before the explanation, the rule above wins inside an item, and the summary carries the hint.

## The summary

Three parts, in a few sentences:

1. What the learner has down, with the item ids that show it.
2. The one idea to work on, named as a belief to change, with the item ids that show it. One idea, even when several items went wrong; pick the one that explains the most of them.
3. One concrete next step that has them do the thinking: a question to answer, something to trace or work out, or a section of a lesson to reread, with its title. This is where a guiding question belongs, and it is left open.

## Before you write the file

- Every quiz item has an entry, in the quiz's order, and no feedback is empty.
- Each verdict follows from the whole response, reasoning included.
- Each `partial` or `wrong` item names what this learner got wrong, and none opens with a hint or a question.
- No explanation appears in full twice across the items.
- The summary names one idea and one next step.
