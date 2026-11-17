# Lesson 0001: review record

- Objective: O3, Explain context and memory in an agent: the context window, what is kept between steps and between sessions, and retrieval and notes as memory.
- Passes: 2, ended at the cap of two passes
- Draft: drafts/0001-context-and-memory-in-an-agent.html

## Pass 1

### lesson-facts-reviewer

| Finding | Check | Section | What the reviewer said | Source | What changed |
|---|---|---|---|---|---|
| F1 | 4 | Clearing | No window size or what happens at the limit | https://platform.claude.com/docs/en/build-with-claude/context-windows | Added window sizes and the "prompt is too long" error (section 1 note) and an overflow caution (section 3 note) |
| F2 | 4 | Notes | Notes grow without bound, so "~40 tokens" stops being true | https://www.anthropic.com/research/effective-context-engineering-for-ai-agents | Why box now says to cap or summarize records |
| F3 | 6 | Notes, worked example, check | Training status treated as authoritative; "it records that" implies chat-written | none (internal consistency) | Priya story: program records instructor sign-off; `trained` vs `notes` fields; booking tool re-checks; check case changed |
| F4 | 3 | Retrieval | search_manuals result size 1,500 vs "about 300" | none (own numbers) | Real chunks 300-500 tokens, k=3 gives about 1,500; toy chunks noted as tiny |
| F5 | 5 | Between steps | Cost lever stated without mechanism; caching missing | https://platform.claude.com/docs/en/build-with-claude/context-windows | Per-call input billing in Why box; caching in a short aside |
| F6 | 7 | Clearing | Tool results are not role "tool_result" messages in the real API | none | Labeled the list as simplified |
| F7 | 1 | Clearing | Source treats clearing as a form of compaction | https://www.anthropic.com/research/effective-context-engineering-for-ai-agents | "lightest way" -> "one of the lightest forms of compaction" |

### lesson-pedagogy-reviewer

| Finding | Check | Section | What the reviewer said | What changed |
|---|---|---|---|---|
| F1 | 2 | Notes | Load and save_note and who-writes caveat in one section | Kept one flow; moved the caveat into its own box; simplified save_note |
| F2 | 2 | Retrieval | Aside adds embeddings and contextual retrieval; "just-in-time" label | Aside cut to one idea; dropped "just-in-time" |
| F3 | 4 | Retrieval | Check options uneven, right one longest | Rewrote check in later pass (see pass 2); options equalized |
| F4 | 4 | Checks | Weak distractors; right option usually last | Rewrote distractors; correct option positions varied |
| F5 | 5 | Between steps | Three observations in one paragraph | Kept re-sending and 7,220 total; stale results moved to section 3 opening |
| F6 | 5 | Notes | setdefault chain adds Python detail | Used a list append in code, setdefault only in save_note |
| F7 | 6 | Context window | Tokens and cost not explained | Added token aside |
| F8 | 7 | Context window | search tool and booking tool appear before they are described | Added book_slot to the tool list; forward pointer in section 2 |
| F9 | 8 | Whole lesson | Warm-up thin, sketch step missing | Declined partly: kept one warm-up; added a second question in pass 2 |
| F10 | 9 | Checks | Feedback not hint-first | Script gives a hint on the first wrong click, full reason on the second |
| F11 | 10 | Between steps | Misconception about remembering steps unnamed | Added "model remembers step 1 by itself" box |

### lesson-alignment-reviewer

| Finding | Check | Section | What the reviewer said | What changed |
|---|---|---|---|---|
| F1 | 2 | Clearing | Not an objective part; costs time | Declined cutting: shortened to 4 min, kept because the facts reviewer needed limits and the budget goal needs cost control |
| F2 | 7 | Opening, practice | Promises a sketch, never practised | Reworded the lead; Your turn includes a sketch step |
| F3 | 3 | Times | Section times add to 38 | Set times to 2+4+5+4+5+5+4+1 = 30 |
| F4 | 1 | Retrieval | Link between retrieval and memory thin | Added a notes vs retrieval table |
| F5 | 4 | Context window | Window size and token not defined | Added token aside and size note |
| F6 | 6 | Notes | Unsafe habit of model-recorded training | Rewrote Priya story, split fields, re-check in booking tool |
| F7 | 8 | Notes | "Weights do not change" made four times | Shortened the section 4 box and the check |

### lesson-quality-reviewer

| Finding | Severity | Check | Place | What the reviewer said | What changed |
|---|---|---|---|---|---|
| F1 | high | 1 | Figure 2 | Arrow cuts through label | Moved labels clear of arrows; boxes equalized |
| F2 | medium | 3 | Figure 2 | Left arrow shows only inflow | Added arrowhead at the records end |
| F3 | medium | 7 | Times | Heading times sum to 38 | Times now sum to 30 |
| F4 | medium | 7 | Length | About 3,740 words, thin | Added misconception boxes, table, longer practice; now about 4,250 |
| F5 | low | 6 | Header | Builds-on not a link | Declined: no earlier lesson file exists |
| F6 | low | 5 | Figure 1 | Figure repeats code numbers | Split bars to show the re-sent manual pages and added the total |
| F7 | low | 3 | Figure 2 | Box widths differ | Both 280 wide |
| F8 | medium | 8 | Retrieval | Aside holds four ideas | Cut to one |
| F9 | medium | 8 | Notes | Misconception box holds two ideas | Split into two boxes |
| F10 | low | 9 | Go further | Cookbook overstated; no community | Reworded; stated no community link was found |
| F11 | medium | 8 | Code blocks | Long lines scroll | Reflowed to short lines |

## Pass 2

### lesson-facts-reviewer

| Finding | Check | Section | What the reviewer said | Source | What changed |
|---|---|---|---|---|---|
| F1 | 2 | Clearing | Compaction and overflow modes only in an aside | https://platform.claude.com/docs/en/build-with-claude/context-windows | Partly declined: kept compaction as a one-line pointer for a later lesson (one concept per section); overflow caution kept in the note |
| F2 | 5 | Clearing | Clearing breaks the cached prefix; clear in batches | https://platform.claude.com/docs/en/build-with-claude/context-editing | Added to the section 3 note, after I opened the page and confirmed it |
| F3 | 7 | Notes | Trace text differs from real f-string output; save_note KeyError | none (hand trace) | Trace says "in effect"; save_note uses setdefault |

### lesson-pedagogy-reviewer

| Finding | Check | Section | What the reviewer said | What changed |
|---|---|---|---|---|
| F1 | 1 | Context window | Token defined as a side clause | Moved into a margin note |
| F2 | 2 | Context window | Sizes, error, output limit and cost crowd the section | Sizes and error in a note; output limit and cost clause removed |
| F3 | 2 | Between steps | Prompt caching in the Why box | Moved to a one-line aside |
| F4 | 2 | Clearing | Several terms in aside | Aside now two cautions and one pointer; kept context rot as the second term |
| F5 | 2 | Notes | Authority rule is its own concept | Made its own box; kept cap/summarize clause in the Why box (declined moving, one sentence) |
| F6 | 4 | Checks | Notes and section 1 checks reuse the section case | Notes check now a new case (Marcus's bed preference); section 1 check kept (declined: it applies the rule to a new scenario) |
| F7 | 4 | Checks | Clearing check solvable by elimination; retrieval options absurd | Retrieval check rewritten as three reasoned options; clearing check kept (declined: low) |
| F8 | 6 | Several | "Weights" undefined | Replaced with "the model itself" |
| F9 | 7 | Clearing | Depends on retrieval before taught | Kept: forward pointer in section 2 |
| F10 | 8 | Warm-up, practice | Warm-up thin; faded task not faded | Second warm-up question; steps 1 and 2 given |
| F11 | 9 | Repetition | Same points repeated | Shortened the section 4 misconception; cost cut from section 1 |
| F12 | 10 | Retrieval | Bigger window idea only in a check | Added a "paste the whole manual" misconception box with 240,000 vs 6,000 |

### lesson-alignment-reviewer

| Finding | Check | Section | What the reviewer said | What changed |
|---|---|---|---|---|
| F1 | 2 | Clearing | Clearing not promised; compaction and caching terms | Kept section; compaction and caching reduced to short notes |
| F2 | 6 | Notes, worked example | Model-written note could be read as a status claim | Example note changed to "asked about CNC router and acrylic bit"; box says loaded notes are unverified text |
| F3 | 7 | Practice | Sketch only for one request | Lead now says "one request"; Your turn places six items in three boxes |
| F4 | 8 | Repetition | Same points made repeatedly | See pedagogy F11 |

### lesson-quality-reviewer

| Finding | Severity | Check | Place | What the reviewer said | What changed |
|---|---|---|---|---|---|
| F1 | medium | 8 | Clearing aside | Three ideas in one aside | Reduced |
| F2 | medium | 8 | Notes aside | Safety point in grey small type | Promoted to a "risky habit" box |
| F3 | low | 3 | Figure 2 | Flow runs bottom to top | Declined: low and not a one-line change |
| F4 | low | 3 | Figure 1 | Value labels far from bars | Moved to the bar ends |
| F5 | low | 4 | Figure 1 | Accent meaning only in the caption | Added an in-figure key |
| F6 | low | 8 | Context window | Dense paragraph | Split with notes |
| F7 | low | 6 | Header | Builds-on not a link | Declined: no earlier lesson file; wording simplified |
| F8 | low | 9 | Go further | Later reading marked; no community | Marked "optional and for later" |
