import shutil
import sys
from pathlib import Path
from urllib.parse import urlparse

from workshop_core.config import WorkshopConfig
from workshop_core.naming import validate_participant_id


class PreflightError(RuntimeError):
    pass


def _require_command(command: str, description: str) -> str:
    if command == "pip" and Path(sys.executable).with_name("pip").is_file():
        return description
    if shutil.which(command) is None:
        raise PreflightError(f"{description} executable was not found on PATH")
    return description


def _require_https(value: str, variable_name: str) -> str:
    parsed = urlparse(value)
    if parsed.scheme != "https" or not parsed.netloc:
        raise PreflightError(f"{variable_name} must use HTTPS")
    return variable_name


def run_local_preflight(config: WorkshopConfig) -> list[str]:
    if sys.version_info[:2] != (3, 11):
        raise PreflightError("Python 3.11.x is required")

    _require_command("pip", "pip")
    _require_command("az", "Azure CLI")
    _require_command("git", "Git")
    validate_participant_id(config.participant_id)
    _require_https(config.foundry_project_endpoint, "FOUNDRY_PROJECT_ENDPOINT")
    _require_https(config.public_mcp_endpoint, "PUBLIC_MCP_ENDPOINT")

    return [
        "Python 3.11 interpreter is active",
        "pip executable is available",
        "Azure CLI executable is available",
        "Git executable is available",
        f"Participant identifier {config.participant_id} is valid",
        "Foundry project endpoint uses HTTPS",
        "Public MCP endpoint uses HTTPS",
    ]
