# Lab 4: Evaluate the Enhanced Agent

**Estimated time:** 15 minutes

**Learning objective:** Run a small, repeatable portal evaluation and turn every
result into a concrete improvement hypothesis.

This module is intentionally portal-only. The workshop mirrors agent creation,
grounding, and MCP in portal and SDK, while evaluation stays in the portal.

## Before You Start

The upload-ready dataset is [evaluation-dataset.jsonl](evaluation-dataset.jsonl), at
`labs/portal-labs/04-evaluation/evaluation-dataset.jsonl` in this workspace. It contains five
JSONL records with these fields:

- `query`: the prompt Foundry sends to the agent.
- `ground_truth`: an optional reference answer for evaluators that support
	reference-answer comparison.

This is an **Agent Target** evaluation. Foundry generates the response at run time;
do not add a precomputed `response` or a retrieval `context` field to this dataset.

### Preflight Checklist

- Confirm your participant-scoped enhanced agent has File Search and the approved
	Microsoft Learn MCP tool.
- Confirm the project has the required evaluation permissions and an approved judge
	model deployment for AI-assisted evaluators.
- Confirm the agent's Playground exposes the tool trace needed to inspect the
	MCP tool call separately from the evaluation run.

## Portal Procedure

1. In the Foundry portal, open your participant's enhanced agent, select its
	**Evaluation** tab, then select **Automatic Evaluation** > **Create**.
2. For the evaluation target, select **Agent**, choose your participant agent, select
	**Individual turns**, and choose **One Time** as the frequency.
3. For data, select **Existing Dataset**, then browse to
	`labs/portal-labs/04-evaluation/evaluation-dataset.jsonl`. Name the uploaded asset
	`<PARTICIPANT_ID>-evaluation-dataset.jsonl`, upload it, and confirm the preview
	contains all five records.
4. Map user input to `{{item.query}}` and ground truth to
	`{{item.ground_truth}}`. Continue and skip **Configure Agents**.
5. Remove suggested evaluators. Select **Task Adherence** and **Intent Resolution**;
	select groundedness and relevance when the portal makes them available.
6. On **Review and submit**, name the run
	`<PARTICIPANT_ID>-evaluation-run-<number>`, verify the dataset and mappings, then
	select **Submit**.
7. Open the completed run and inspect each query, generated response, evaluator
	 result, and explanation rather than relying only on the aggregate score.

## What to Inspect

- The warranty, return, troubleshooting, and Premium Support responses should match
	the workshop knowledge files.
- The Premium Support case should state that it is available 24x7.
- Confirm MCP behavior separately in the agent Playground: run the Lab 3 prompt and
	expand the trace to verify the Microsoft Learn MCP tool call and final answer. The
	portal evaluator can skip an intermediate tool-call item, so it is not used as the
	MCP verification signal.
- The out-of-scope case must not invent or disclose private information.
- Any failed case is an improvement hypothesis for the prompt, grounding, tool, or
	evaluation dataset.

After reviewing the evaluation, continue to the [Code and SDK Workshop](../../code-labs/README.md).
