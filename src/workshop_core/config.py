from dataclasses import dataclass
import os


class ConfigurationError(ValueError):
    pass


@dataclass(frozen=True)
class WorkshopConfig:
    subscription_id: str
    resource_group: str
    foundry_resource_name: str
    foundry_project_name: str
    foundry_project_endpoint: str
    model_deployment_name: str
    participant_id: str
    public_mcp_endpoint: str

    @classmethod
    def load(cls) -> "WorkshopConfig":
        keys = {
            "subscription_id": "AZURE_SUBSCRIPTION_ID",
            "resource_group": "AZURE_RESOURCE_GROUP",
            "foundry_resource_name": "FOUNDRY_RESOURCE_NAME",
            "foundry_project_name": "FOUNDRY_PROJECT_NAME",
            "foundry_project_endpoint": "FOUNDRY_PROJECT_ENDPOINT",
            "model_deployment_name": "MODEL_DEPLOYMENT_NAME",
            "participant_id": "PARTICIPANT_ID",
            "public_mcp_endpoint": "PUBLIC_MCP_ENDPOINT",
        }
        missing = [env_name for env_name in keys.values() if not os.getenv(env_name)]
        if missing:
            raise ConfigurationError(
                "Missing required environment variables: " + ", ".join(sorted(missing))
            )
        values = {field: os.environ[env_name] for field, env_name in keys.items()}
        return cls(**values)