# Lab 2: Ground the Support Agent with Files

**Learning objective:** Attach the workshop support files to the Lab 1 agent so its
answers can cite the supplied knowledge.

**Required access:** **Foundry Project Manager** at the workshop Foundry scope.

## Attach Files

1. Open your `<PARTICIPANT_ID>-agent-baseline` agent in the Foundry portal.
2. Select **Upload files**.
3. In the file-attachment experience, create a new index named
	`<PARTICIPANT_ID>-grounding-vector-store`.
4. Add these four files to the index:

	- `assets/support-knowledge/product-overview.md`
	- `assets/support-knowledge/support-policy.md`
	- `assets/support-knowledge/troubleshooting.md`
	- `assets/support-knowledge/warranty-returns.md`

5. Finish the attachment flow and wait until the portal shows that the files are
	ready for use. Do not continue while indexing is still in progress. When finished,
	select **Attach**.
6. Save a new version of the same agent with the file attachment enabled.

## Verify Grounding

In the agent playground, send this prompt:

```text
What should I do when error E17 appears twice?
```

The answer should include the restart and enrollment-token steps, recommend
escalation after the second failed retry, and show source attribution for the workshop
files. Inspect the trace to see the File Search and retrieval steps.

## Checkpoint

The Lab 1 agent now has the four support files attached and returns a grounded E17
response with visible source attribution.

## Next Step

Continue to [Lab 3](../03-mcp-tools/README.md) to add a read-only MCP tool to this
same grounded agent.
