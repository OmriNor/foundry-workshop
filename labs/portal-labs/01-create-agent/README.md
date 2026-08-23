# Lab 1: Create the Support Agent

**Learning objective:** Create the initial Contoso SupportHub X1 support agent in
the Microsoft Foundry portal. You will enhance this same agent in Labs 2 and 3.

**Required access:** **Foundry Project Manager** at the workshop Foundry scope.

## Create the Baseline Agent

1. In Microsoft Foundry, turn on **New Foundry**, then select **Build** > **Agents** >
	**New Agent** > **Build an agent**.
2. Set the agent name to `<PARTICIPANT_ID>-agent-baseline` and create it.
3. Select the workshop's shared GPT-5.4-mini deployment in the **Model** list.
4. Enter these instructions:

	```text
	You are the Contoso SupportHub X1 support assistant. Answer only from
	connected sources when they are available. If a source does not contain the
	answer, say so. Never invent customer or private information.
	```

5. Send this prompt:

	```text
	What is the warranty period for SupportHub X1?
	```

At this stage the answer is not reliably grounded because the agent has no workshop
files yet. Keep this agent open: Lab 2 adds its knowledge source and Lab 3 adds its
MCP tool.

## Checkpoint

The agent has the expected name, model, and instructions, and responds in the
playground.

## Next Step

Continue to [Lab 2](../02-file-grounding/README.md) to attach the support files to
this agent.
