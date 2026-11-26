# Lesson 0001: review record

- Objective: O3, Explain context and memory in an agent: the context window, what is kept between steps and between sessions, and retrieval and notes as memory.
- Plan: drafts/0001-plan.md, 6 concept sections plus opening and warm-up, worked example and summary, 4,500 words budgeted; changes you made to the plan: the planner's single S3 ("compaction", which also introduced clearing) taught two techniques in one section, so I split it into S3 (clearing old tool results, 400 words) and S3b (compaction, 300 words) with their own examples, and updated the promises and budget table. I also added `RESOURCES.md` from the plan's two sources.
- Writer: drafts/0001-writer-notes.md, 6 departures from the plan, 6 kept (S3 numbers fixed because the plan's 14,000 did not follow from its inputs; worked example uses four calls; extra hybrid check; one misconception box; no community link; "Builds on" in plain text); items you put back after the writer: none. The hybrid check was later removed (see pass 1 and 2 notes).
- Passes: 2, ended at the cap of two passes; review rounds started: 2; findings in round 1: 40, in round 2: 43
- Draft: drafts/0001-context-and-memory.html

## Pass 1

### lesson-facts-reviewer

| Finding | Check | Section | What the reviewer said | Source | What changed |
|---|---|---|---|---|---|
| F1 | 6 | What is kept between steps | Trace books the laser cutter after only a calendar check, with no training check, and the student only asked "can I book" | https://platform.claude.com/docs/en/build-with-claude/context-windows (internal consistency) | Added a sentence that the program, not the model, guards `book_slot` (made explicit in pass 2) |
| F2 | 3 | Context window / clearing / retrieval | Page size is 8,000, about 1,000, 900 and 1,500 tokens in different places; 400 x 900 is not 600,000 | calculation | Manual set now 400 pages x about 1,000 = about 400,000 tokens; the 8,000 figure is described as "long manual sections" |
| F3 | 1 | Finding the right page | "600,000 tokens is too big for most windows" is wrong against 200k to 1M windows | https://platform.claude.com/docs/en/build-with-claude/context-windows | Now says windows run about 200,000 to 1 million and argues on cost and rot instead of fit |
| F4 | 3 | Notes / retrieval | Notes cost 200 tokens per call not per session; retrieval's "5,000 total" is per call | calculation | "200 tokens on every call, about 800 across four calls"; retrieval reworded to per-call size |
| F5 | 1 | When the window fills | Newer models accept input plus `max_tokens` over the window; "reserves room" feedback is wrong | https://platform.claude.com/docs/en/build-with-claude/context-windows | Reworded the overflow detail; removed the `max_tokens` option and its feedback; later reduced to the 400-error sentence |
| F6 | 7 | What is kept between steps | Loop not labelled pseudocode, wrong result format, no step cap | https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls | Labelled pseudocode, mentioned `tool_result` block, added `MAX_STEPS` |
| F7 | 3 | Worked example | Total omits the booking call and final answer | calculation | Added call 5 (booking), total 9,530 |
| F8 | 2 | Finding the right page / summary | No note on how search ranks pages; server-side compaction not mentioned | https://platform.claude.com/docs/en/build-with-claude/context-windows | Added "ranking is a later lesson, plan for it to be wrong"; added server-side options note |
| F9 | 3 | Header and section times | Times sum to 32 | calculation | Re-timed sections; pass 2 re-timed again to total 30 |
| F10 | 6 | Notes between sessions | Student-written notes placed in system prompt with no warning | https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls | Notes labelled "unverified, hints only"; added id-from-login and short-facts habits |
| F11 | 8 | When the window fills | "Lightest" wording cited to the wrong page | https://anthropic.com/engineering/effective-context-engineering-for-ai-agents | Cites the docs for the feature and the engineering article for "among the lightest" |

### lesson-pedagogy-reviewer

| Finding | Check | Section | What the reviewer said | What changed |
|---|---|---|---|---|
| F1 | 9 | Opening | Seven labelled ideas before any example | Deleted the "two limits and two fixes" paragraph; split the win into two sentences (reduced to one in pass 2) |
| F2 | 6 | Context window | Token, system prompt, tool definition used before explained | Added plain definitions (in pass 2 moved into code comments after the example) |
| F3 | 5 | Context window | Second `cancel_booking` trace and "one question" paragraph over-explain | Trace moved to a margin note; "one question" paragraph cut |
| F4 | 4 | What is kept between steps, check | Right option longest and only numeric | New 3-call case; every option has numbers; correct option moved |
| F5 | 2, 5 | When the window fills | Four ideas in one section | Error detail moved to an aside; pass 2 gave context rot its own section |
| F6 | 1 | When the window fills | Rot named with no trace | Added two-run example (pass 2, own section) |
| F7 | 4 | When the window fills, check | Right answer repeats the stem; `max_tokens` option undefined | New case with eight pasted pages; options rewritten |
| F8 | 7 | Clearing / compaction | Forward references to notes and fetching; compaction check trivial | Forward references reworded; compaction check now compares summaries |
| F9 | 2 | Notes between sessions | Two concepts: notes and note-versus-record | Split into S4 and new S4b "A note is a claim, not a record" |
| F10 | 4 | Notes check | Options echo the section's own examples | New check on a returning student's stable preference |
| F11 | 2 | Finding the right page | Wrong-page failure and hybrid in one section | Wrong-page failure moved to new S5b; hybrid sentence and hybrid check removed |
| F12 | 4 | Finding the right page, check | Two options are the same idea; right one is the only one with code | Three distinct strategies, no code formatting |
| F13 | 4, 8 | Your turn | Notes not stated; every step faded at once | Notes stated in the task; steps partly given |

### lesson-alignment-reviewer

| Finding | Check | Section | What the reviewer said | What changed |
|---|---|---|---|---|
| F1 | 3 | Opening, worked example, summary | "Three places" promise but a fourth category (the record) is applied | Opening and summary say "three places plus one check"; worked example step labelled "(the check)" |
| F2 | 3 | Section times | Times sum to 32 | Re-timed |
| F3 | 4 | Context window / clearing | `max_tokens`, `stop_reason`, token counting API unexplained | Trimmed to plain wording; pass 2 reduced further |
| F4 | 6 | Notes between sessions | Notes in system prompt look like instructions | Labelled as unverified hints, safety aside added |
| F5 | 8 | Several | Record rule and "model only knows training" repeated | Cut S1 "one question" paragraph and the S5 pointer; shortened S3b torque line |
| F6 | 1 | Finding the right page | Retrieval not framed as memory | Added a sentence on retrieval as read-only memory and a summary table of the three places |

### lesson-quality-reviewer

| Finding | Severity | Check | Place | What the reviewer said | What changed |
|---|---|---|---|---|---|
| F1 | high | 1 | Figure 1 | "Total in the window" label collides with the value | Label shortened to "Total" |
| F2 | medium | 4 | Figure 2 legend | Spaces collapse; colours named not shown | Swatches and separate labels |
| F3 | medium | 5 | Figure 2 vs table | Figure repeats the table | Table deleted; the sum is drawn in the figure |
| F4 | medium | 5 | Whole lesson | Organising idea not drawn | Added the three-places figure (placed in the summary in pass 2) |
| F5 | medium | 8 | Summary aside | One sentence lists four topics | Cut to one next-lesson pointer |
| F6 | low | 7 | Section times | Sum to 32 | Re-timed |
| F7 | low | 5 | Figure 1 | Title says "stack" but bars are separate | Title and caption changed to "bars, proportional to tokens" |
| F8 | low | 6 | Code blocks | Long lines scroll sideways | Long lines broken |
| F9 | low | 9 | Go further | No community, few sources | Declined to add unseen links; kept the two read sources (a one-line community note was added then removed in pass 2 as filler) |
| F10 | low | 6 | Template drift | Orienting paragraphs in header; check labels long; warm-up in one `<p>` | Moved to a "map" section (removed in pass 2); labels shortened; warm-up split into two paragraphs |

## Pass 2

### lesson-facts-reviewer

| Finding | Check | Section | What the reviewer said | Source | What changed |
|---|---|---|---|---|---|
| F1 | 2, 5 | Between steps / Finding the right page | Prompt caching changes price not window use, and is missing | https://platform.claude.com/docs/en/build-with-claude/context-windows | Added a caching aside in S2 and "assume no caching" |
| F2 | 7, 6 | Notes between sessions | Model supplies `student_id` to `save_note`, contradicting the advice | calculation | `save_note(text=...)` only; program adds id from the login |
| F3 | 6 | Worked example | Student asked for a feed rate, but the model books | calculation | Student now asks for a booking, with a note about offering a slot otherwise |
| F4 | 4, 7 | Between steps | Loop has no handling when the step limit is hit | calculation | Added `for ... else` branch |
| F5 | 3 | Context window / steps / retrieval | Fixed overhead 400 vs 1,000; `read_page` missing from tools; range 4,000 to 5,000 | calculation | Four tools in S1 (800 tokens, total 4,470, figure updated); S2 marked as a simplified assistant; range 4,000 to 5,500 |
| F6 | 3 | When the window fills | "Call fails or is cut off" is wrong for the 66,000 example | https://platform.claude.com/docs/en/build-with-claude/context-windows | "The call fails with an error" |
| F7 | 6 | Notes between sessions | Notes in system prompt could carry instructions | reasoned point, no source | Aside: notes are untrusted, can contain instructions, never unlock a machine; kept the label. Not moved to a user-message block, declined: the code access check is the real safeguard and the lesson says so |
| F8 | 3 | Between steps | "as in lesson 2" inconsistent | draft header | Comment changed to "a step limit, so it always ends" |

### lesson-pedagogy-reviewer

| Finding | Check | Section | What the reviewer said | What changed |
|---|---|---|---|---|
| F1 | 1 | "How this lesson is organised" | Terms and a figure before any example | Section removed; figure moved to the summary |
| F2 | 8 | Header | Win is two long sentences | One sentence |
| F3 | 1, 2, 6, 9 | Context window | Four terms defined before the example | Definitions moved to code comments; token defined inline; window and token named after the trace |
| F4 | 2, 6 | Between steps | `stop_reason`, "lesson 2", "stateless" undefined, access check aside | `wants_tool` comment; stateless defined in the Why box; access aside cut to a short pointer |
| F5 | 5 | Between steps | Nine quantities in one paragraph | Declined: the figure now carries the totals and the trace is already the section's example |
| F6 | 2, 5, 6 | When the window fills | Aside carries four ideas | New section "context rot" with example, name, why and check; aside cut to the 400 error and server-side note |
| F7 | 6, 7 | Clearing | "Lightest forms of compaction" names compaction early; rot used before taught | Wording changed; rot now taught first |
| F8 | 2, 4, 7 | Clearing / compaction checks | Right answers detectable by surface cues | Right option reworded; compaction summaries now differ by one detail each |
| F9 | 2, 5 | Notes between sessions | Cost and security rules after the concept | Security rules moved to an aside; cost kept to one line |
| F10 | 4 | S4b and S5b checks | Right options repeat section phrases | Declined: options are paraphrased and the cases are new; a further rewrite would not change the skill tested |
| F11 | 5 | Whole lesson | About 40 minutes; answer drawers repeat feedback | Declined deleting the drawers (they help non-click readers and print); length stays within the fit band |
| F12 | 9 | Checks | No guiding question before the explanation | Wrong-answer feedback now opens "Ask yourself what that option assumes, then read on:" |
| F13 | 10 | Whole lesson | Common misconceptions not named | Declined adding more boxes: S2's figure, S3b's dropped detail and S5's 400,000-token case already show them; length |

### lesson-alignment-reviewer

| Finding | Check | Section | What the reviewer said | What changed |
|---|---|---|---|---|
| F1 | 2 | Clearing and compaction | Overflow handling is a neighbouring topic and takes 5 minutes | Declined: the mission asks the learner to "decide what the assistant keeps in its context", so clearing and compaction serve it; detail was trimmed |
| F2 | 2 | A note is a claim | Reads as a fourth category | Added "limits of notes, not a fourth kind of memory"; kept the section and its check |
| F3 | 3 | Between steps | "lesson 2" does not exist | Fixed (see facts F8) |
| F4 | 3 | Opening vs summary | Opening and summary promise different lists | Win is now one sentence; summary and figure agree |
| F5 | 1 | Notes between sessions | Steps versus sessions never put side by side | Added a two-sentence contrast in S4 |
| F6 | 4 | Clearing | `max_tokens`, `stop_reason`, 400 unfamiliar | Removed `max_tokens` and `stop_reason`; kept the 400 error in one sentence |
| F7 | 7 | Worked example / practice | Practice is mostly recall, not decisions | Added a four-item sort task with solution |
| F8 | 8 | Several | Frame and note rule repeated | Summary bullet shortened; the worked example uses one-line recalls |

### lesson-quality-reviewer

| Finding | Severity | Check | Place | What the reviewer said | What changed |
|---|---|---|---|---|---|
| F1 | high | 1 | Figure 1 (map) | Bottom text clipped | Figure rebuilt with the text in a dashed box |
| F2 | high | 1 | Figure 3 | Billed line clipped | Two lines, viewBox 262 high |
| F3 | medium | 3 | Map figure | No arrowheads | Added markers |
| F4 | medium | 5 | Map figure | Check drawn as floating text | Dashed box added |
| F5 | medium | 7 | Section times | Clearing, S4b and summary overrun | Re-timed to sum to 30 |
| F6 | medium | 6 | Table of contents | Map section missing | Map section removed; TOC updated for new sections |
| F7 | medium | 8 | Clearing aside | Dense list | Aside cut; rot moved to its own section |
| F8 | medium | 6 | Cross-reference | "lesson 2" | Fixed |
| F9 | low | 1 | Figure legend | Text touches swatch | Swatch and label moved right |
| F10 | low | 6 | Go further | Filler sentence | Deleted |
| F11 | low | 6 | `.place` class | New class | Declined: harmless, consistent |
| F12 | low | 8 | Notes between sessions | Cost and security in one paragraph | Security habits in an aside |
| F13 | low | 3 | Map figure | Uneven padding | Boxes made 64 tall |
| F14 | low | 9 | Go further | Add Context editing and Compaction docs pages | Declined: those URLs were not seen in this session's results |
