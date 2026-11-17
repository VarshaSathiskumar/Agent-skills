# Lesson 0001: review record

- Objective: O3, Explain context and memory in an agent: the context window, what is kept between steps and between sessions, and retrieval and notes as memory.
- Plan: drafts/0001-plan.md, 5 concept sections plus worked example, 4,500 words budgeted; changes I made to the plan: removed a stray "NOT used" line from the Promises section (planner's wording error). A stray file `drafts/0001-plan.md.promises-note` could not be deleted (no shell); it is unused.
- Writer: drafts/0001-writer-notes.md, 5 departures from the plan, 5 kept; items I put back after the writer: none. I fixed the muddled "10,000 tokens" distractor in the S2 check myself (now 9,000 / 8,000 / 15,000 / 25,000).
- Passes: 2, ended at the cap of two passes; review rounds started: 2; findings in round 1: 43 (facts 7, pedagogy 13, alignment 8, quality 15); in round 2: 35 (facts 6, pedagogy 11, alignment 6, quality 12)
- Draft: drafts/0001-context-and-memory.html

The tables below are summaries by theme, not finding by finding. Before/after is given for every change that matters; the draft was revised in place.

## Pass 1

### lesson-facts-reviewer

| Finding | Check | Section | What the reviewer said | Source | What changed |
|---|---|---|---|---|---|
| F1 | 1 | 1 | Input tokens are not the whole bill; the table is context size, not billing | https://platform.claude.com/docs/en/build-with-claude/context-windows | "input tokens are what your bill is made of" -> input billed every call, output too at a higher rate; table shows size, not bill |
| F2 | 3 | 5 | 200+300+800 is 1,300, not 1,100; disagrees with worked example 1,150 | calculation | Table now 1,100 manual text + 200 ToC separately; worked example uses 1,100 |
| F3 | 6 | 2 | Laser cutter booked with no training check contradicts section 4 | lesson's own section 4 | S2 trace switched to a 3D printer, with a note that restricted machines come in section 4 |
| F4 | 7 | 4 | `end_session` fails if memory/ missing; student_id unsafe | Python behaviour | Added `os.makedirs`, rule that student_id is program-issued |
| F5 | 7 | 1 | Dict is a simplification of a real request | context-windows page | Added "simplified... a real call also sets model and max_tokens, tools holds schema dicts" |
| F6 | 2 | 2 | Prompt caching and compaction by the platform missing | context-windows page | Added a short caching sentence; platform compaction declined (off scope, model-specific per plan) |
| F7 | 9 | 1 | "Model sees only the text" ignores training | context-windows page | "Beyond what it learned in training, the model sees only the text in the call" |

### lesson-pedagogy-reviewer

| Finding | Check | Section | What the reviewer said | What changed |
|---|---|---|---|---|
| F1 | 1 | Opening | Two lists state answers before any example | Deleted both lists; five questions folded into the lead; roadmap sentence in the mission box |
| F2 | 2 | 1 | Overflow error, stop_reason, counting API crowd section 1 | Overflow paragraph moved to section 3 and reduced to the 400 error and counting API; stop_reason dropped |
| F3 | 5 | 1 | "Token" never defined | One-sentence definition added at first use |
| F4 | 2 | 3 | Rot, clearing, summarizing in one section; split it | declined: the plan sets rot and compaction as one section, and a split costs words in a lesson already near its length; second reviewer round raised it again, still declined |
| F5 | 6 | 3, 4 | Jargon: attention budget, high-signal tokens, system of record | "high-signal" replaced; "system of record" -> "source of truth" everywhere; "attention budget" kept in the why box |
| F6 | 2 | 4 | Memory tool, privacy and safety crowd section 4 | Memory tool cut to one sentence; privacy and source-of-truth moved to two notes; misconception box shortened |
| F7 | 5 | 5 | Table counts inconsistent with section 2's billing | Table total fixed; full billing comparison left as per-call |
| F8 | 4 | checks | Right option often longest or in positions 3-4 | declined: positions not rotated, to avoid rewriting all checks; second round raised it again |
| F9 | 7 | 1 | Check feedback refers forward to section 3 | Forward references removed |
| F10 | 5 | checks | "Show the answer" blocks repeat click feedback | Removed from all multiple-choice checks except a cost detail in section 5 |
| F11 | 8 | Summary | Summary copies the opening | Rewritten as five answers, one per question |
| F12 | 8 | Worked | Recap rather than trace | Kept the five steps; budget line later given a per-call trace (pass 2) |
| F13 | 10 | 1, 4 | "A bigger window fixes it" left to chance | Added to section 4: a bigger window does not carry Monday over |

### lesson-alignment-reviewer

| Finding | Check | Section | What the reviewer said | What changed |
|---|---|---|---|---|
| F1 | 3 | 1, 5, worked | Tool count and token figures disagree | Tool list stated in section 1; worked example uses five tools; 1,100 everywhere |
| F2 | 6 | 2 | Trace books a restricted machine with no training check | Switched to 3D printer (see facts F3) |
| F3 | 6 | 4 | Notes loaded into system prompt unlabelled | Code now labels notes "Unverified notes, for context only", goes in first message; rule on what may be saved |
| F4 | 1 | Opening, 5 | Retrieval never connected to memory | Added a paragraph in section 5 contrasting notes (loaded whole) with manuals (one page); summary mentions it |
| F5 | 4 | 1 | Token undefined | See pedagogy F3 |
| F6 | 2 | 1, 4 | Error codes and memory-tool details off-level | Trimmed as above |
| F7 | 8 | several | Same argument repeated four times | Worked example budget line shortened; section 1 check kept; partial |
| F8 | 7 | Worked | Only 3 minutes for the practice | Relabelled 4 min; second section 3 check kept |

### lesson-quality-reviewer

| Finding | Severity | Check | Place | What the reviewer said | What changed |
|---|---|---|---|---|---|
| F1 | high | 5 | Section 5 table | 1,100 / 1,150 / 1,300 disagree | Fixed as above |
| F2 | medium | 5 | Figure 1 | Repeats the table | Added a zero baseline; split bars declined (pass 1 and pass 2) |
| F3 | medium | 6 | Opening | Bare headings with inline styles | Removed with the lists; TOC straight after header |
| F4 | medium | 8 | Section 4 box | Four ideas in one block | Box shortened; two notes |
| F5 | medium | 6 | Code blocks | Lines too long | Dict and S2 code lines shortened with comments on their own lines |
| F6 | medium | 6 | Box labels | "A common mix-up: a note is a fact" differs | Label now "A common mix-up" |
| F7 | medium | 3 | Figure 2 | Last box smaller | All four boxes 120 wide |
| F8 | medium | 5 | Figure 2 caption | Describes things not drawn | Caption now describes what is drawn |
| F9 | medium | 7 | Worked label | 3 min understates | 4 min |
| F10-F15 | low | various | Meta line, lead length, arrow ends, community link, time labels | Meta line cut, lead rewritten, arrows fixed; community link declined (no source found); labels rebalanced |

## Pass 2

### lesson-facts-reviewer

| Finding | Check | Section | What the reviewer said | Source | What changed |
|---|---|---|---|---|---|
| F1 | 3 | Worked | Budget line 6,000 does not match the call sizes (about 6,560) | calculation | Per-call trace added: 1,690 + 2,020 + 2,850 = about 6,560 |
| F2 | 4 | 3 | Never says what happens if nothing is done | context-windows page | Paragraph added: history grows, 400 error, measure first |
| F3 | 2 | 2 | Prompt caching only half a sentence | context-windows page | declined: pedagogy asks for fewer terms; one sentence kept |
| F4 | 6 | 4 | Check relies on the model calling the training tool | none (own rule) | Note added: `book_slot` code must itself check the record |
| F5 | 7 | 4 | Code comment says "labelled" but does not label | trace | Code now adds the label and uses `with open` |
| F6 | 8 | 2 | "Main cost driver" cited to a page that does not say it | context-windows page | Reworded as the lesson's own reasoning; citation kept for the caching clause only |

### lesson-pedagogy-reviewer

| Finding | Check | Section | What the reviewer said | What changed |
|---|---|---|---|---|
| F1 | 1 | 1 | Token defined before the example | declined: the counts in the dict cannot be read without it |
| F2 | 2 | 1 | Resend arithmetic and 400 error in section 1 | 5,070 trace and error paragraph removed from section 1; section 3 now holds the error |
| F3 | 2 | 2 | Caching is a second technique; figure, table and text repeat numbers | Caching cut to one clause; repetition declined |
| F4 | 2 | 3 | Split section 3 | declined: see pass 1 |
| F5 | 2 | 4 | Sample note contradicts the "never clearance" rule | Sample line changed to "asked about acrylic settings"; box wording changed to "Suppose a note said..." |
| F6, F7 | 4 | checks | Positions and section 5 check too close to the trace | declined for positions; section 5 check kept |
| F8 | 5 | 5 | No-result branch, hybrid, embeddings add terms | "hybrid" removed; embedding note cut to one line; no-result branch kept as a safety point |
| F9 | 6 | whole | "system of record" vs "source of truth" | One term used |
| F10 | 8 | Worked | Budget line has no trace | Fixed (see facts F1) |
| F11 | 9 | checks | Hint before reason; add a figure in section 1 | declined: no new figure at the cap; hint-first feedback would rewrite every check |

### lesson-alignment-reviewer

| Finding | Check | Section | What the reviewer said | What changed |
|---|---|---|---|---|
| F1 | 3 | Lead | Lead promises three decisions, body delivers five | Lead rewritten around the five questions |
| F2 | 6 | 4 | Sample note stores a clearance claim; label only in a comment | Fixed (see pedagogy F5, facts F5); allowed-kinds rule added |
| F3 | 8 | 4 | The note-is-not-a-fact point made three times | Box shortened; one note for the source of truth; later recalls left as one-liners |
| F4 | 2 | several | Extra terms (400 error, caching, sub-agents, hybrid) | Sub-agents aside and hybrid removed; caching and 400 error kept in one place each |
| F5 | 3 | Worked | Budget line has no trace | Fixed |
| F6 | 8 | 1, 2 | Section 1 gives the resend explanation before section 2 | Section 1 now says only that section 2 shows the bill |

### lesson-quality-reviewer

| Finding | Severity | Check | Place | What the reviewer said | What changed |
|---|---|---|---|---|---|
| F1 | medium | 6 | Section 5 and 2 checks | Trace text visible before answering | Section 5 moved into a details block; section 2 line removed |
| F2, F3 | medium | 5 | Figure 1 | Single bars do not show resent vs new; accent meaningless | declined: redrawing is more than a one-line change at the cap |
| F4, F5 | medium | 5 | Figure 2, section 1 | Figure 2 repeats the list; section 1 has no figure | declined at the cap |
| F6 | medium | 8 | Section 4 aside | Two ideas in one note | Split into two notes |
| F7 | low | 6 | Section 3 label, `<details>` | "second case" label | Label fixed; template `<details>` fallbacks declined |
| F8-F12 | low | various | Figure 2 box labels, box order, lead length, time labels, community link | Time labels rebalanced (S1 4.5, S2 4.5, S3 4.5, S4 5, S5 5, worked 4, warm-up 2, summary 1); community link line removed; the rest declined |

Not fixed and worth a later look: the lesson's word count is about 4,900 by the quality reviewer's estimate (about 33 minutes at 150 words a minute, inside the 0.6 to 1.5 band); section 3 still holds two techniques; right options sit mostly in position 3 or 4.
