# Context and memory: where does it live?

| Place | Holds | Survives the call? | Survives the session? | Use for |
|---|---|---|---|---|
| Context window | Everything in one request, answer included | No | No | What the model needs right now |
| Accumulating history | The list your program resends each step | Yes, by resending | No | The current task |
| Saved notes | Files the application stores for the model | Yes | Yes | Preferences, progress |
| Retrieval store | Long reference text, fetched on demand | Yes | Yes | Manuals |
| Official record | Facts that grant permissions | Yes | Yes | Training status, checked by code |

## Rules of thumb
- Hard limit: input over the window returns a 400 error. Soft limit: answers get worse before that (context rot).
- Cost: every call is billed for the whole history, so a page added at step 2 of 6 costs its size 5 times.
- Compaction: summarize and continue fresh. Tell the summarizer to keep bookings, constraints and open questions.
- Notes are hints written by the model. Permissions come from the official record, checked in code.
- Preload what is small and always needed. Retrieve what is long and rarely needed.

Sources: [context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows), [memory tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool), [Effective context engineering](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents).
