# Writer notes: What the makerspace assistant sees, forgets and remembers

## Departures from the plan
| Plan item | What the plan said | What the draft does | Why |
|---|---|---|---|
| S2 check wording | "8,000-token page at step 2 of a 6-step run", cost across steps 2 to 6 | Says the page arrives after call 1 of a run of 6 model calls, so it is resent on calls 2 to 6 | The plan's wording was ambiguous about which call first carries the page; the answer (8,000 x 5 = 40,000) is unchanged |
| S4 handler and notes path | Per-student folder; note at `/memories/students/s123.md` | Per-student base folder `ROOT/s123`; note at `/memories/profile.md` | Keeps the 12-line handler simple and consistent with "map /memories to a per-student folder" |
| S5 token tally | "about 2,300 in the third call" | The answering call (the second model call, after the tool result) carries about 2,300; total about 3,300 for two calls | The plan's three steps contain two model calls; arithmetic made consistent |
| S3 new-window size | About 1,100 tokens | 1,100 for prompt, summary and last message, plus a line saying tool definitions make it about 1,700 | Plan's figure omitted the 600 tokens of tool definitions used elsewhere |
| Go further | Primary source only; template also has a community link | No "Test it with others" line | The plan gives no community URL, and links must come only from the plan |
| Worked example table | Not specified beyond "filled table" | Table includes a "who verifies" column as planned; the faded task hints are given inline in one paragraph | Space |
| Misconception boxes | Plan did not place them | Three boxes, once each: S1 (more context is better), S2 (model remembers earlier steps), S4 (a note is a verified fact) | LESSONS.md asks for misconceptions where they bite |

## Sections against their budgets
| Section | Planned words | Paragraphs written | Check present |
|---|---|---|---|
| Opening and warm-up | 300 | about 3 plus figure and 2 recalls | 2 recall questions |
| S1 The context window | 700 | about 7 plus table | Yes |
| S2 What carries from step to step | 700 | about 6 plus code and figure | Yes, plus second check (which lever) |
| S3 When the window fills | 700 | about 6 | Yes, plus second check (what must survive) |
| S4 Between sessions | 750 | about 7 plus two code blocks | Yes, plus second check (what belongs in notes) |
| S5 Finding the right page | 750 | about 6 | Yes, plus second check (hybrid split) |
| Worked example and practice | 350 | table and faded task | Faded task with solution on demand |
| Summary and go further | 250 | summary box and sources | n/a |

The draft likely lands somewhat under 4,500 words (my estimate is 4,000 to 4,300); S3 and S5 are the likeliest to be short.

Side points: none added beyond the plan; the aside in S3 carries the planned one-line mention of context editing.
