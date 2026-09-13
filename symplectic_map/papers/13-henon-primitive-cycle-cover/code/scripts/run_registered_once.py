"""Unique registered entry.  Safe preflight and tests never invoke it."""

import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT / "code"))

from candidate_v1.bootstrap.constants import project_root_from_bootstrap
from candidate_v1.orchestrator.registered import run_registered_transaction


def main():
    if len(sys.argv) != 1:
        raise RuntimeError("registered entry takes no arguments")
    project_root = project_root_from_bootstrap()
    run_registered_transaction(project_root)


if __name__ == "__main__":
    main()
