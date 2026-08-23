# Lab 3: Add an MCP Tool

**Learning objective:** Add the approved Microsoft Learn MCP server to the grounded
Lab 1 agent and inspect one live tool call.

## Required Portal Access

The portal creates a project connection when you add this custom MCP server. Before
starting this lab, confirm that the workshop host assigned you **Foundry Project
Manager** at the workshop Foundry scope. If the portal reports that
`Microsoft.CognitiveServices/accounts/projects/connections/write` is unauthorized,
sign in again after the role assignment and retry this step.

## Add the Custom MCP Tool

1. Open your grounded `<PARTICIPANT_ID>-agent-baseline` agent in the Foundry portal.
2. Select **Tools** > **Add tools** > **Custom** > **MCP**.
3. Configure the custom MCP server:

	| Field | Value |
	| --- | --- |
	| Name | `MSLearn` |
	| Endpoint | `https://learn.microsoft.com/api/mcp` |
	| Authentication | Unauthenticated |

4. Retain the Lab 1 instructions and add this sentence:

	```text
	Use the connected documentation tool for current Microsoft Foundry documentation questions.
	```

5. Save a new version of the same grounded agent.

## Verify Tool Use

In the agent playground, send this prompt:

```text
Find current Microsoft Foundry guidance for remote MCP tools.
```

Inspect the run details and confirm that the Microsoft Learn MCP tool was called before
the final answer was produced.

You can configure the MCP tool from its **More options** menu to approve all tool calls
or restrict specific tools.

The workshop uses this server because its reviewed tool inventory is read-only. Do not
use this approval setting as a general rule for a different MCP server; require review
for any tool that could change data or access external systems.

## Checkpoint

The same agent now has both the support files and the Microsoft Learn MCP tool, and
one run shows a visible MCP tool call.

## Next Step

Continue to [Lab 4](../04-evaluation/README.md) to evaluate this enhanced agent.
