# Lesson 0001: review record

- Objective: O3, Explain context and memory in an agent: the context window, what is kept between steps and between sessions, and retrieval and notes as memory.
- Plan: drafts/0001-plan.md, 5 concept sections plus opening, worked example and summary, 4500 words budgeted; changes you made to the plan: none (budget sums to 4500, every key fact K1 to K8 is taught in a section).
- Writer: drafts/0001-writer-notes.md, 7 departures from the plan, 7 kept; items you put back after the writer: none. The writer's one known typo ("a effect") was fixed.
- Passes: 2, ended at the cap of two passes; review rounds started: 2; findings in round 1: 41 (facts 10, pedagogy 14, alignment 7, quality 10), in round 2: 37 (facts 5, pedagogy 18, alignment 3, quality 11)
- Draft: drafts/0001-context-and-memory.html

## Pass 1

### lesson-facts-reviewer

| Finding | Check | Section | What the reviewer said | Source | What changed |
|---|---|---|---|---|---|
| F1 | 3 | 1 and 5 | Corpus sizes contradict (60,000-token chapter vs 80,000 for twelve manuals; 900,000 set) | calculation | Chapter 6,000 tokens; failure 1 became a 230,000-token long chat; S5 notes 80,000 would still fit the window |
| F2 | 3 | 2 | Figure 2 bars not on one scale | calculation | Widths 80/305/335 -> 121/305/328, labels moved |
| F3 | 3 | 5 | Preload comparison counted two calls | calculation | "81,000 x2 = 162,000" -> one preloaded call vs two retrieval calls |
| F4 | 2, 5 | 2, 3 | Caching and cost of the summary call missing | https://platform.claude.com/docs/en/build-with-claude/context-windows | Added caching parenthesis in S2; added one-off summary-call cost in S3 |
| F5 | 2 | 5 | How search finds pages not said | https://anthropic.com/engineering/effective-context-engineering-for-ai-agents | Added short aside on keyword match and index/tool description |
| F6 | 4 | 1, 3 | Trigger for compaction and the output-headroom case missing | https://platform.claude.com/docs/en/build-with-claude/context-windows | Added token counting before each call and 75% threshold (S3, S1); headroom case added in round 2 |
| F7 | 8 | 5 | Memory-tool docs cited for slower-runtime claim | https://anthropic.com/engineering/effective-context-engineering-for-ai-agents | Removed memory tool citation from that sentence |
| F8 | 3 | opening, worked example | Three places promised, official record shown as a fourth; 400/600 vs 500/500 prompt and tool sizes | calculation | Lead, mission box and Figure 1 caption now name the official record; S5 sizes made 400 + 500 + 600 |
| F9 | 6 | 4 | student_id must not come from model output | none (reasoning, flagged unverified) | Added one sentence: id comes from the signed-in session |
| F10 | 7 | 4 | `str_replace` cannot add a line; handler showed only view | https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool | Monday trace now uses `view` then `create`; handler code removed |

### lesson-pedagogy-reviewer

| Finding | Check | Section | What the reviewer said | What changed |
|---|---|---|---|---|
| F1 | 2 | 1 | Section 1 carries too many concepts | Partly: window size sentence moved to aside; split declined (it would break the "five ideas" promise and the 30-minute budget) |
| F2 | 6 | 1 | Token and tool definition used before defined | Added a one-line gloss before the table |
| F3 | 4 | 1 | Check replays the section's failure | Replaced by a two-request case (A over, B inside with buried line) |
| F4 | 4 | 3 | Checks answerable by matching | Second check replaced by a new wheelchair-constraint case; first kept |
| F5 | 7 | 3 | Forward reference to "checked record" | Reworded to "Section 4 shows where such facts should live" |
| F6 | 2 | 3 | Context editing named in S3 | Moved to Go further |
| F7 | 2 | 4 | Four ideas in S4 | Partly: handler code and trace removed, safeguards made a list, book_slot moved out of the box; split into 4a/4b declined (same reasons as F1) |
| F8 | 5 | 4 | Path code and trace too long | Removed |
| F9 | 4 | 4 | Checks answerable by matching | First check replaced (preference vs live calendar); second reworded |
| F10 | 2 | 5 | Too much in S5 | Declined: hybrid is in the plan and checks; tool-description fix kept as part of the failure example |
| F11 | 4 | 5 | Second check repeats text; options uneven | Second check replaced (3,000-token table); first check's options reworded |
| F12 | 4 | worked example | Hints all visible, packed in a paragraph | Done in pass 2 (hints in a `details`) |
| F13 | 9 | all checks | "Show the answer" repeats feedback | Removed from the two checks I rewrote in S1 and S3/S4/S5; declined for the rest: low value, they work as a fallback without a click |
| F14 | 10 | 5 | Retrieval never set against notes | Added aside: retrieval is memory too, store vs notes |

### lesson-alignment-reviewer

| Finding | Check | Section | What the reviewer said | What changed |
|---|---|---|---|---|
| F1 | 3 | lead, figure, worked example | Three-way promise vs fourth place | Lead, mission box, Figure 1 caption updated |
| F2 | 3 | 1 and 5 | Manual sizes inconsistent | As facts F1 |
| F3 | 1 | 5 | Search internals and retrieval vs notes thin | As facts F5 and pedagogy F14 |
| F4 | 2, 4 | 4 | Path-traversal code beyond level and objective | Code and second trace removed; one bullet remains |
| F5 | 3, 7 | header, practice | Times add to 32; practice too thin | Times now 1+5+5+4+5+5+4+1 = 30; practice 4 min |
| F6 | 6 | 4 | Booking saved as a note, then contradicted | Monday note now holds preference and topic only |
| F7 | 8 | 4 | Safety point repeated about six times | Trimmed the Why box clause and the practice solution's closing sentence; kept the box, the table row and the summary |

### lesson-quality-reviewer

| Finding | Severity | Check | Place | What the reviewer said | What changed |
|---|---|---|---|---|---|
| F1 | high | 5 | Figure 2 | Bars not on one scale | Widths and label positions fixed |
| F2 | high | 5 | Figure 2 caption | Caption claims containment the bars do not draw | Caption reworded to what is drawn |
| F3 | medium | 5 | Figure 1 caption | Three boxes but a fourth place later | Caption names the official record; extra box declined |
| F4 | medium | 3 | Figure 2 | Arithmetic repeated three times | Sum removed from caption |
| F5 | medium | 8 | S4 box | Box holds code and enforcement | Code and enforcement moved into the main text after the box |
| F6 | low | 5 | Figure 1 | Repeats the text | Declined: low, one-line fix not available |
| F7 | low | 5 | Lesson-wide | Only two figures | Declined: low; a new figure is not a one-line change |
| F8 | low | 6 | Go further | No community line | Declined: no community URL came from this session |
| F9 | low | 7 | Section times | Times drift from words | Times retimed to total 30 |
| F10 | low | 8 | Solution and safeguards | Dense paragraphs | Solution and safeguards set as lists |

## Pass 2

### lesson-facts-reviewer

| Finding | Check | Section | What the reviewer said | Source | What changed |
|---|---|---|---|---|---|
| F1 | 4 | 1 | Input plus output headroom and `model_context_window_exceeded` missing | https://platform.claude.com/docs/en/build-with-claude/context-windows | "comfortably inside" -> "inside the window with little room left"; added the cut-off stop reason, cited |
| F2 | 7 | 5 | Answer text says third option, correct is second | draft trace | "third option" -> "second option" |
| F3 | 2, 3 | 5 | Retrieved pages are resent too | calculation | Added sentence: 1,200 x 5 = 6,000 extra tokens, return only the best pages |
| F4 | 4 | 4 | Size cap consequence missing | https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool | Added reason to the cap bullet: notes are read back into the window |
| F5 | 6 | 3 | Summary example carried a "certified" claim | draft's own rule | Removed the certification from the sample summary |

### lesson-pedagogy-reviewer

| Finding | Check | Section | What the reviewer said | What changed |
|---|---|---|---|---|
| F1 | 8 | opening | Win sentence holds four destinations | Declined: the official-record exception is needed for the worked example to be honest |
| F2 | 1 | 1 | Token defined twice | Dropped the second definition; the parenthesis remains |
| F3 | 2, 5, 6 | 1 | Split S1 | Declined: cap reached, split would break the "five ideas" promise and time budget |
| F4 | 4 | 1 | Check replays failures | Declined: it now needs both limits and is a new case; option-length balance left for a later revision |
| F5 | 2, 6 | 2 | Caching parenthetical | Declined: one cited sentence, answers a budget question the learner has |
| F6 | 2, 5, 7 | 3 | Detail after the concept | Declined: threshold and one-off cost answer the facts reviewer's findings |
| F7 | 4 | 3 | Second check option lengths | Declined: low value |
| F8 | 2, 3, 7 | 4 | Split S4 | Declined: as pedagogy F3 |
| F9 | 4 | 4 | Second check answerable by matching | Declined: kept as a short recall of the section's rule |
| F10 | 2, 5, 6 | 5 | Split S5 | Declined: as pedagogy F3 |
| F11 | 4 | 5 | Wrong answer key; uneven options | Answer key fixed (see facts F2); options left |
| F12 | 10 | 5 | No misconception box for "retrieval is always better" | Declined: covered by the hybrid check and its feedback |
| F13 | 5 | all | Lesson over budget | Declined: bench estimate is about 4,950 words, inside 2,700 to 6,750 |
| F14 | 8 | practice | Drop from worked example to faded task too big | Hints put in their own `details`; step count unchanged |
| F15 | 2, 6 | practice | "Who verifies" column untaught | Declined: kept; it is the reason for the S4 split |
| F16 | 8 | Go further | No community | Declined: no community URL came from this session |
| F17 | 9 | checks | Wrong clicks give the full reason, not a hint | Declined: several feedback lines already open with a guiding hint; a two-click design is out of scope for the cap |
| F18 | 9 | 4, 5 | Add figures | Declined: low; no new figure at the cap |

### lesson-alignment-reviewer

| Finding | Check | Section | What the reviewer said | What changed |
|---|---|---|---|---|
| F1 | 2, 3 | lead, figure, S3 | Compaction not in the promise; defence only by accuracy and cost | Lead now says "accuracy, cost and safety"; S3 stays (it covers what happens when kept history outgrows the window); S5 aside says retrieval is memory |
| F2 | 6 | 3 | Sample summary carries a certification | Removed the certification from the sample summary |
| F3 | 8 | several | Repeats | Token defined once; the other repeats declined (recall in the worked example and summary is deliberate) |

### lesson-quality-reviewer

| Finding | Severity | Check | Place | What the reviewer said | What changed |
|---|---|---|---|---|---|
| F1 | high | 5 | S5 check | "Show the answer" names the wrong option | Fixed to "second option" |
| F2 | medium | 5 | Figure 2 | Caption says the calendar result is shown, bars have no segments | Caption reworded to "re-sends everything before it" |
| F3 | medium | 5 | Figure 1 | No relations; fourth place not drawn | Declined: map kept simple; caption names the exception |
| F4 | medium | 6 | Checks | Show-the-answer blocks inconsistent | Declined: feedback after a click already carries the answer |
| F5 | medium | 8 | S5 | Paragraph packs four ideas | Search internals and the notes/store contrast moved into one short aside |
| F6 | medium | 8 | Your turn | Hints all visible | Hints moved into a closed `details` |
| F7 | low | 6 | Box order | Why box after misconception in S4 | Declined: low, not a one-line change |
| F8 | low | 9 | Go further | Bullet without link; no community | Declined: low; no community URL from this session |
| F9 | low | 5 | Whole lesson | Add a figure for S5 | Declined: low |
| F10 | low | 8 | S3 | Meta aside; two ideas in the last paragraph | Aside deleted; paragraph left |
| F11 | low | 6 | S1 | Token defined twice | Second definition removed |
