# Report

This file is written by `p3 report --write` (p3 0.2.0, 2026-11-24 20:03 UTC). Do not edit it by hand: it is written again whenever new runs are scored.

## Results on agent-architecture

Scored full runs (quick runs and --only runs left out); each cell is the mean over the runs, with the range in brackets.

### Quality

| config | runs | teach facts | teach misconc. | length ratio | dead links | key agreement | wrong keys | ambiguous items | verdict agreement | false wrong | misconc. hit | leaks | behavior met |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 1.00 | 0 | 0.74 (0.69-0.80) | 0 | 1.00 | 0 | 0 | 1.00 | 0.00 | 1.00 | 0 | 0.56 (0.50-0.67) |
| `c1-skills` | 1 | 0.83 | 0 | 0.66 | 0 | 1.00 | 0 | 0 | 1.00 | 0.00 | 1.00 | 0 | 0.83 |
| `c2-review` | 1 | 1.00 | 0 | 0.80 | 0 | 1.00 | 0 | 0 | 1.00 | 0.00 | 1.00 | 0 | 0.50 |
| `c3-split` | 1 | 1.00 | 0 | 0.90 | 0 | 1.00 | 0 | 0 | 1.00 | 0.00 | 1.00 | 0 | 0.50 |

Teach facts, key agreement, verdict agreement, false wrong, misconception hit and behavior met are shares (0 to 1); misconceptions, dead links, wrong keys, ambiguous items and leaks are counts per run.
A dash means no run could be scored on that check, and n= says how many of the runs could.
A job that failed counts against the config: no lesson scores 0 teach facts, no quiz and key 0 key agreement, a missing grades file disagrees on every item, and a tutor scenario with no reply is not met; leaks need a reply to check, so such a scenario is left out of them.
The length ratio is a rough reading-time estimate (visible words / 150) over the minutes requested; 0.6 to 1.5 counts as on length.

### Cost: teach

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 598.4k (569.9k-646.1k) | 31.2k (30.6k-31.9k) | 3.1 (3.0-3.4) | 0 | 0.62 (0.59-0.66) |
| `c1-skills` | 1 | 455.2k | 23.5k | 2.5 | 0 | 0.50 |
| `c2-review` | 1 | 3.87M | 156.5k | 12.1 | 8 | 3.10 |
| `c3-split` | 1 | 2.78M | 168.9k | 12.7 | 10 | 3.06 |

### Cost: quiz

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 148.5k (134.7k-171.8k) | 5.4k (5.0k-6.0k) | 0.7 (0.6-0.7) | 0 | 0.18 (0.18-0.19) |
| `c1-skills` | 1 | 126.9k | 5.8k | 0.8 | 0 | 0.18 |
| `c2-review` | 1 | 551.9k | 32.4k | 4.0 | 2 | 0.66 |
| `c3-split` | 1 | 592.0k | 38.2k | 4.7 | 2 | 0.67 |

### Cost: grade

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 285.3k (271.4k-312.1k) | 7.6k (7.5k-7.8k) | 1.0 (0.9-1.1) | 0 | 0.33 (0.33-0.34) |
| `c1-skills` | 1 | 244.8k | 6.6k | 0.9 | 0 | 0.29 |
| `c2-review` | 1 | 625.2k | 21.8k | 2.5 | 3 | 0.66 |
| `c3-split` | 1 | 631.4k | 23.2k | 2.5 | 3 | 0.60 |

### Cost: tutor

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 539.2k (454.1k-612.0k) | 10.9k (9.8k-11.7k) | 1.6 (1.5-1.6) | 0 | 0.67 (0.64-0.69) |
| `c1-skills` | 1 | 461.9k | 6.5k | 1.1 | 0 | 0.48 |
| `c2-review` | 1 | 468.1k | 6.4k | 1.1 | 0 | 0.48 |
| `c3-split` | 1 | 499.3k | 6.4k | 1.0 | 0 | 0.44 |

### Cost: all jobs

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 1.57M (1.44M-1.67M) | 55.1k (53.6k-56.5k) | 6.4 (6.1-6.7) | 0 | 1.82 (1.74-1.88) |
| `c1-skills` | 1 | 1.29M | 42.4k | 5.4 | 0 | 1.44 |
| `c2-review` | 1 | 5.52M | 217.1k | 19.6 | 13 | 4.90 |
| `c3-split` | 1 | 4.50M | 236.7k | 20.9 | 15 | 4.78 |

Costs are per run, summed over the job's scenarios; list-price $ is the list-price equivalent, not what you pay on a subscription.

## Your ratings

Your ratings from 1 to 5 in the major reviews (reviews/<step>.md), which review full runs on the shared topic; a dash means no rating there yet, one that p3 check does not accept, or a job that step does not review (Tutor in c2-review; Quiz, Feedback and Tutor in c3-split).

| job | criterion | c1-skills | c2-review | c3-split | final |
|---|---|---:|---:|---:|---:|
| Lesson | Technical correctness and facts | 4 | 4 | 4 | - |
| Lesson | Pedagogy | 4 | 4 | 5 | - |
| Lesson | Alignment with the learning goal | 5 | 4 | 5 | - |
| Lesson | Overall quality | 4 | 4 | 4 | - |
| Quiz | Difficulty | 4 | 4 | - | - |
| Quiz | Coverage of the lesson's core | 5 | 4 | - | - |
| Quiz | Wording and possible misreadings | 4 | 3 | - | - |
| Quiz | Writing quality | 4 | 4 | - | - |
| Quiz | Alignment with the learning goal | 5 | 4 | - | - |
| Feedback | Useful | 4 | 4 | - | - |
| Feedback | Explains enough | 5 | 5 | - | - |
| Feedback | Personalized to how I like things explained | 4 | 3 | - | - |
| Tutor | Guardrails | 4 | - | - | - |
| Tutor | Personalization | 4 | - | - | - |

## Lesson length

Scored teach-only runs; each cell is the mean over the runs, with the range in brackets.

### Quality

| config | minutes | runs | teach facts | teach misconc. | length ratio | dead links |
|---|---:|---:|---:|---:|---:|---:|
| `c1-skills` | 10 | 3 | 0.72 (0.67-0.83) | 0 | 0.91 (0.82-0.96) | 0 |
| `c1-skills` | 30 | 3 | 0.89 (0.83-1.00) | 0 | 0.65 (0.62-0.68) | 0 |
| `c1-skills` | 60 | 3 | 1.00 | 0 | 0.49 (0.43-0.54) | 0 |

Teach facts, key agreement, verdict agreement, false wrong, misconception hit and behavior met are shares (0 to 1); misconceptions, dead links, wrong keys, ambiguous items and leaks are counts per run.
A dash means no run could be scored on that check, and n= says how many of the runs could.
A job that failed counts against the config: no lesson scores 0 teach facts, no quiz and key 0 key agreement, a missing grades file disagrees on every item, and a tutor scenario with no reply is not met; leaks need a reply to check, so such a scenario is left out of them.
The length ratio is a rough reading-time estimate (visible words / 150) over the minutes requested; 0.6 to 1.5 counts as on length.

### Cost: teach

| config | minutes | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|---:|
| `c1-skills` | 10 | 3 | 377.8k (355.8k-415.4k) | 14.6k (14.4k-14.8k) | 1.4 (1.4-1.5) | 0 | 0.37 (0.33-0.43) |
| `c1-skills` | 30 | 3 | 416.7k (396.5k-450.0k) | 21.5k (20.0k-22.4k) | 2.3 (2.1-2.4) | 0 | 0.48 (0.47-0.49) |
| `c1-skills` | 60 | 3 | 455.8k (395.0k-529.3k) | 30.2k (25.2k-34.3k) | 3.1 (2.6-3.6) | 0 | 0.60 (0.53-0.66) |

### Cost: all jobs

| config | minutes | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|---:|
| `c1-skills` | 10 | 3 | 377.8k (355.8k-415.4k) | 14.6k (14.4k-14.8k) | 1.4 (1.4-1.5) | 0 | 0.37 (0.33-0.43) |
| `c1-skills` | 30 | 3 | 416.7k (396.5k-450.0k) | 21.5k (20.0k-22.4k) | 2.3 (2.1-2.4) | 0 | 0.48 (0.47-0.49) |
| `c1-skills` | 60 | 3 | 455.8k (395.0k-529.3k) | 30.2k (25.2k-34.3k) | 3.1 (2.6-3.6) | 0 | 0.60 (0.53-0.66) |

Costs are per run, summed over the job's scenarios; list-price $ is the list-price equivalent, not what you pay on a subscription.
