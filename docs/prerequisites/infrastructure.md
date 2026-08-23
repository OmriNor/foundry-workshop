# Workshop Host Infrastructure Prerequisites

Use this checklist to prepare the Microsoft Foundry environment before distributing
the workshop repository. It is written for the workshop host or platform team, not
individual attendees.

## Required Foundry Environment

Provide one Microsoft Foundry project with public outbound access to the approved MCP
endpoint. The project must use **Basic Agent Setup**: Foundry manages the file storage,
vector stores, and File Search resources used in the labs.

The host supplies these non-secret values in each participant's `.env` file:

```dotenv
AZURE_SUBSCRIPTION_ID=
AZURE_RESOURCE_GROUP=
FOUNDRY_RESOURCE_NAME=
FOUNDRY_PROJECT_NAME=
FOUNDRY_PROJECT_ENDPOINT=
MODEL_DEPLOYMENT_NAME=
PARTICIPANT_ID=
PUBLIC_MCP_ENDPOINT=
```

Do not commit a populated `.env` file. Do not distribute credentials, client secrets,
shared access tokens, or Azure CLI caches.

## Model Deployment and Throughput

Provide a GPT-5.4-mini deployment, or a host-approved compatible deployment, in the
workshop project. Set `MODEL_DEPLOYMENT_NAME` to the deployment name used by the
notebooks.

The workshop host owns throughput planning. Provision sufficient RPM for the expected
cohort before delivery. You may deploy more than one model deployment for additional
RPM or operational fallback; each cohort's `.env` still names the one deployment it
uses.

## Participant Access

Assign every attendee **Foundry Project Manager** at the workshop **Foundry resource
scope**. This supports the full portal-first workflow: creating and running prompt
agents, attaching files, creating the custom MCP project connection in Lab 3, and
running the evaluation. Attendees must sign in again after a role assignment.

Before delivery, test with a non-administrator account that has this role. Confirm it
can create an agent in the portal and SDK, attach the workshop files, use File Search,
create the custom MCP connection, invoke the MCP tool, run the evaluation, and remove
its participant-prefixed resources.

## Public MCP Tool

The approved read-only MCP server is:

| Setting | Value |
| --- | --- |
| Endpoint | `https://learn.microsoft.com/api/mcp` |
| Authentication | None |
| Reviewed tools | `microsoft_docs_search`, `microsoft_docs_fetch`, `microsoft_code_sample_search` |

Do not reuse its approval settings for another MCP server without reviewing that
server's tools and side effects.
