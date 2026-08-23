from dotenv import load_dotenv

from workshop_core.config import ConfigurationError, WorkshopConfig
from workshop_core.preflight import PreflightError, run_local_preflight


def main() -> int:
    load_dotenv()
    try:
        config = WorkshopConfig.load()
        for check in run_local_preflight(config):
            print(f"[OK] {check}")
    except (ConfigurationError, PreflightError, ValueError) as error:
        print(f"[ERROR] {error}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
