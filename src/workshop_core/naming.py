import re


PARTICIPANT_ID_PATTERN = re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$")


def validate_participant_id(value: str) -> str:
    if not PARTICIPANT_ID_PATTERN.fullmatch(value):
        raise ValueError(
            "PARTICIPANT_ID must use lowercase kebab-case (for example omri or omri-2)"
        )
    return value


def sdk_participant_id(value: str) -> str:
    return f"{validate_participant_id(value)}-ws"


def build_resource_name(participant_id: str, lab: str, purpose: str) -> str:
    validate_participant_id(participant_id)
    for label, value in {"lab": lab, "purpose": purpose}.items():
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", value):
            raise ValueError(f"{label} must use lowercase kebab-case")
    return f"{participant_id}-{lab}-{purpose}"
