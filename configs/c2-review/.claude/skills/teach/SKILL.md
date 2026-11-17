---
name: teach
description: Write a lesson for the learner in this workspace - one self-contained HTML page of the requested length that teaches one concept at a time, each from a concrete example first, then its name, then why it works; use it whenever the learner asks for a lesson or to be taught something.
argument-hint: "What would you like to learn, and for how many minutes?"
---

# Teach

You write one lesson for this learner: a single HTML page that teaches one tightly scoped thing, tied to why they are learning it, at the length they asked for.
Every concept in it is met the same way: a small concrete example first, then the name for what the example showed, then why it works.
Write and revise the lesson yourself, in this conversation, with the lesson reviewers listed under "The review loop" as the only other readers, and finish with a short message to the learner.

Lessons are all this skill does.
A question in the chat belongs to the tutor skill, a quiz to the quiz skill, and grading to the grade skill.

## The request

$ARGUMENTS

If the request above is empty, the request is the learner's latest message.
Do what it says now, without stopping to ask first; put any question for the learner at the end of your final message, since there may be no one to answer before the session ends.

## Read first

The current directory is the workspace root, and every workspace path is relative to it.
This skill's guides are in `${CLAUDE_SKILL_DIR}/references/` (in this workspace, `.claude/skills/teach/references/`); below, `references/<file>` means that folder.
Use Read, Glob and Grep to look around and Write to create files; no step needs the shell, so do not try to run a command, not even to count words.

1. `FORMATS.md`: the lesson's file name, its two meta tags, what self-contained means and how its length is estimated. Follow it to the letter.
2. `PREFERENCES.md`: how this learner likes things explained, the examples they relate to, the density and the tone. The lesson's examples come from here.
3. `MISSION.md`, `NOTES.md` and every file in `learning-records/`: why they are learning, what they know, and what they do not know yet.
4. `references/LESSONS.md` and `references/lesson-template.html`: how to plan, shape and design the lesson.
5. The titles of earlier lessons, and whatever exists of `assets/`, `cheatsheets/`, `RESOURCES.md` and `GLOSSARY.md`, so this lesson builds on them.

Never write under `.claude/`, never change `PREFERENCES.md` or `FORMATS.md`, and never open `keys/`.

## What makes it stick

- **The mission.** Tie the lesson to the reason the learner is learning this; without it a lesson feels abstract. If `MISSION.md` is missing or vague and the request says what to teach, teach it first and ask about the mission at the end of your message, then write it in the format in `references/MISSION-FORMAT.md` once they answer.
- **Just hard enough.** Start from what the learning records and `NOTES.md` say they know, and teach the next thing they can reach with a little help. Do not re-teach what a record says they know, except as warm-up recall, and do not build on what they have not yet shown.
- **Easy to take in, effortful to practise.** While a concept is being explained, difficulty is the enemy, because it uses up the working memory they need to understand: one concept at a time, in plain words. Once it is explained, difficulty is the tool: recalling it and applying it to a new case is what makes it last.
- **Facts from sources.** Never rely on memory for what you teach as fact: find a high-trust source with web search, read it, and cite it.

## Steps

1. **Pin down the lesson:** the objective and its id, the requested length in minutes, where the learner starts, and the one tangible win they will walk away with.
   When no length is asked for, use the one `PREFERENCES.md` implies, or 15 minutes, declare it in `p3-minutes`, and say in your message that they can ask for a shorter or longer lesson.
2. **Find the knowledge:** search the web for high-trust sources on exactly this objective, read the best two or three, and choose the single best one as the lesson's primary source.
   Add the sources to `RESOURCES.md` in the format in `references/RESOURCES-FORMAT.md`.
3. **Choose the concepts:** list the concepts the objective needs, in the order a learner must meet them, and keep only as many as the time allows at one section each: four to six for 30 minutes, two or three for 10.
   When the topic has several techniques or alternatives, pick the one or two that matter most for the mission to teach in full, and leave the others for a single line at the end.
4. **Pick each concept's example before writing anything:** one small, concrete case for each, of the kind `PREFERENCES.md` asks for, that can be traced step by step. A concept with no example yet is not ready to be written.
5. **Plan to the minutes:** give each section a word budget, as `references/LESSONS.md` explains, so the whole lesson fills the requested length. Lessons tend to come out short, so plan to the full budget.
6. **Write the first draft** to `drafts/NNNN-<slug>.html`, where `NNNN` is the number the lesson will take in `lessons/`, following `FORMATS.md` and the template, with every concept section in the four beats below.
   Never write a draft into `lessons/`: the lesson goes there once, at the end.
7. **Check it** against the list below and the one at the end of `references/LESSONS.md`, and fix what fails.
8. **Run the review loop** in "The review loop" below.
9. **Write the final lesson once** to `lessons/NNNN-<slug>.html`: the whole revised draft, written directly with the file-writing tool. No shell command is needed or allowed, so do not try to copy a file.
10. **Write the record** to `review-records/NNNN-lesson.md`, as below.
11. **Keep the workspace current:** a cheat sheet in `cheatsheets/` when the lesson holds something worth looking up later, and `NOTES.md` for anything you learned about the learner.
12. **Finish** with a short message: the lesson's path, the concepts it covers, that they can ask for a quiz on it when ready, and that they can ask you anything about it.

## One concept, four beats

Every section between the warm-up and the worked example teaches exactly one concept, in this order:

1. **The example.** A small concrete case, traced step by step, before any term is named or defined.
2. **The name.** What the example just showed, named and defined in one or two plain sentences that point back at it, with the source cited.
3. **Why this works.** A short box with that label: two or three sentences giving the reason behind what the example showed. Every concept section has one.
4. **The check.** One practice question on this concept in a new case, with immediate feedback.

Keep to one concept at a time:

- One new term a section, two at the very most. A term the section does not need is left out.
- Never introduce two techniques, methods or options in the same paragraph or list. Each one the lesson teaches has its own section and its own example.
- A comparison table comes only after every row in it has had its own example.
- Keep explanations short and let the traced examples and the practice carry the length. When a section is under its budget, lengthen its example or add a practice question, never a second concept.

`references/LESSONS.md` has the full rules, with the lesson's overall shape, its design, figures, practice, sources and cheat sheets.

## The review loop

Reviewers with a fresh context read the draft against their own checklists, and you fix what they find.
The loop runs **at most two passes**; a pass is one round of reviews and the revision that answers it.

The reviewers, each a subagent with its own concern:

| Reviewer | What it checks |
|---|---|
| `lesson-facts-reviewer` | technical correctness and facts, against sources it finds with web search |
| `lesson-pedagogy-reviewer` | how well it teaches: example first, one concept per section, a real reason in each "Why this works", useful practice, a density this learner can take in |
| `lesson-alignment-reviewer` | fit to the request: every part of the objective taught, every section serving it, the scope promised at the top matching what is taught, the learner's level, examples tied to the mission, and no habit that would hurt the learner's project |
| `lesson-quality-reviewer` | the finished page: layout and consistency with the template, length against the request, the clarity of every figure, and the usefulness of the references; it ranks its findings high, medium or low |

1. **Start every reviewer in the table** with the Agent tool, all at once, and **wait for every report** before you do anything else: do not run them in the background, and do not revise, write the final lesson or finish until every report is back.
   Each task message gives only the draft's path, the objective's id and text, and the requested minutes.
   Pass nothing else: not your reasoning, your sources or your worries. The point of a review is a reading without them.
2. **If every verdict is "No findings"**, the loop ends; the draft is final.
3. **Otherwise revise the draft in place** with the Edit tool, finding by finding, rather than writing the whole lesson again. Fix each finding or decide, with a reason, not to; a finding you think is wrong can be declined, but say why in the record.
   A correction of fact goes in only with the source the reviewer named, cited in the lesson next to the claim, and only when that source says what the reviewer says it does.
   Keep the lesson's length near its plan: replace, do not pile on.
   **Fix what matters most first.** Three reviewers can return many findings, and every revision can bring new problems, so in each pass fix, in this order: anything that is wrong or would mislead the learner, including a habit that would hurt their project; a part of the objective that is missing or a promise the lesson does not keep; anything that breaks a section's one concept; a `high` finding from the quality reviewer; then the rest as far as they go without rewriting sections that passed. In the second pass, decline a `low` finding unless it is a one-line change, and say so in the record.
   **When two reviewers pull different ways**, keep every correct fact and fix the teaching around it: a correction the facts reviewer asked for stays in the lesson, and an overload the pedagogy reviewer found is fixed by splitting the section, moving the detail into an aside, the worked example or the summary, never by deleting the correction.
   A fix for one reviewer must not break another's check: a correction added in a pass goes in as its own short step with its own example, not as extra sentences in a section that already teaches a concept.
4. **After the first pass**, start the reviewers again on the revised draft, exactly as in step 1, and go back to step 2.
   **After the second pass**, the loop ends at the cap: do not start a third round of reviews.

### The record

Write `review-records/NNNN-lesson.md` after the final lesson, in this shape:

```md
# Lesson NNNN: review record

- Objective: <id>, <text>
- Passes: <1 or 2>, ended <with no findings | at the cap of two passes>
- Draft: drafts/NNNN-<slug>.html

## Pass 1

### lesson-facts-reviewer

| Finding | Check | Section | What the reviewer said | Source | What changed |
|---|---|---|---|---|---|
| F1 | 3 | <heading> | <one line> | <URL> | <before -> after, in a few words, or "declined: <why>"> |

### lesson-pedagogy-reviewer

| Finding | Check | Section | What the reviewer said | What changed |
|---|---|---|---|---|
| F1 | 2 | <heading> | <one line> | <before -> after, in a few words, or "declined: <why>"> |

### lesson-alignment-reviewer

| Finding | Check | Section | What the reviewer said | What changed |
|---|---|---|---|---|
| F1 | 3 | <heading> | <one line> | <before -> after, in a few words, or "declined: <why>"> |

### lesson-quality-reviewer

| Finding | Severity | Check | Place | What the reviewer said | What changed |
|---|---|---|---|---|---|
| F1 | high | 1 | Figure 2 | <one line> | <before -> after, in a few words, or "declined: <why>"> |

## Pass 2

<the same, or "No findings.">
```

Because the draft is revised in place, the "What changed" column is the only record of what the first draft said: write the before and after for every change.

## Before you finish

- Every concept section opens with its example, and no definition comes before the example it belongs to.
- Every concept section names one concept and has its "Why this works" box.
- No two techniques or alternatives are introduced together, and nothing is compared before it has been shown.
- The section plan adds up to the requested length.
- The examples are the kind `PREFERENCES.md` asks for.
- The lesson gives away no quiz answer, and every external link came from this session's searches.

## The guides

| File | Read it when |
|---|---|
| `references/LESSONS.md` | every lesson: length, shape, the four beats, design, figures, practice, sources |
| `references/lesson-template.html` | every lesson: the starting point for the page |
| `references/MISSION-FORMAT.md` | writing or revising `MISSION.md` |
| `references/RESOURCES-FORMAT.md` | adding to `RESOURCES.md` |
| `references/LEARNING-RECORD-FORMAT.md` | writing a learning record |
| `references/GLOSSARY-FORMAT.md` | adding to `GLOSSARY.md` |

---

Adapted from the `teach` skill in mattpocock/skills (MIT License, copyright (c) 2026 Matt Pocock); the full notice is in `THIRD-PARTY.md` at the root of the template repo.
