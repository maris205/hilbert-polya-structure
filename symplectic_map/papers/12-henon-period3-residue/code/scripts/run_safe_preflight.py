"""Create the canonical pre-execution record; never imports a science engine."""

from __future__ import annotations

import sys
from pathlib import Path


def main() -> None:
    if len(sys.argv) != 1:
        raise RuntimeError("safe preflight accepts no arguments")
    sys.dont_write_bytecode = True
    project_root = Path(__file__).absolute().parents[2]
    sys.path.insert(0, str(project_root / "code/candidate_v1"))
    from bootstrap.preflight import collect_preflight
    from bootstrap.protocol import write_json_exclusive

    record = collect_preflight(project_root)
    if record["status"] != "PREEXECUTION_PASS_REGISTERED_COUNT_ZERO":
        raise RuntimeError("safe preflight rejected")
    write_json_exclusive(project_root / "preexecution/preflight.json", record)


if __name__ == "__main__":
    main()
