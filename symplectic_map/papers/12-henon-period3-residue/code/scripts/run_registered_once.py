"""Sole R100 entry point; requires a hash-bound independent deployment PASS."""

from __future__ import annotations

import sys
from pathlib import Path


def main() -> None:
    if len(sys.argv) != 1:
        raise RuntimeError("registered audit accepts no arguments")
    sys.dont_write_bytecode = True
    project_root = Path(__file__).absolute().parents[2]
    sys.path.insert(0, str(project_root / "code/candidate_v1"))
    from bootstrap.runner import run_registered_audit

    run_registered_audit(project_root)


if __name__ == "__main__":
    main()
