# AI Agents and MCP Resources

## Knowledge

- [Article: "Code execution with MCP" (Anthropic Engineering)](https://www.anthropic.com/engineering/code-execution-with-mcp)
  Names the two token costs of MCP, tool definitions loaded upfront and intermediate tool results passing through the model, with the Drive-to-Salesforce transcript example. Use for: why MCP is expensive, and code execution as a fix.
- [Article: "Advanced tool use" (Anthropic Engineering)](https://www.anthropic.com/engineering/advanced-tool-use)
  Measured numbers: 58 tools across five servers at about 55K tokens, and what the Tool Search Tool saves. Use for: concrete token figures, tool search, programmatic tool calling.
- [Docs: "Scale to many tools with tool search" (Claude Code Agent SDK)](https://code.claude.com/docs/en/agent-sdk/tool-search)
  How deferred tool loading works and how `ENABLE_TOOL_SEARCH` configures it. Use for: a lesson on fixing the definition cost.

## Gaps

- No community listed yet; the learner has not been asked whether they want one.
