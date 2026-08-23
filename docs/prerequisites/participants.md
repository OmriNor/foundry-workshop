# Participant and Client Prerequisites

Complete this setup before the workshop. The workshop host provides the Foundry
configuration values and project access.

## What You Need

- Visual Studio Code with the **Python** and **Jupyter** extensions.
- Python 3.11 with `venv` and `pip` (run `python3 -m venv --help` and `python -m pip --help` without errors to validate).
- Azure CLI and Git.
- A Microsoft Entra account assigned **Foundry Project Manager** on the workshop
  Foundry resource (should be taken care of by the host).

## What the Workshop Host Provides

- The workshop repository or folder.
- Confirmation that your chosen participant ID is not already in use.
- The non-secret `.env` values: `AZURE_SUBSCRIPTION_ID`, `AZURE_RESOURCE_GROUP`,
  `FOUNDRY_RESOURCE_NAME`, `FOUNDRY_PROJECT_NAME`, `FOUNDRY_PROJECT_ENDPOINT`,
  `MODEL_DEPLOYMENT_NAME`, and `PUBLIC_MCP_ENDPOINT`.
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
- Confirmation that your Entra account has Foundry Project Manager access at the
  workshop Foundry resource scope.
