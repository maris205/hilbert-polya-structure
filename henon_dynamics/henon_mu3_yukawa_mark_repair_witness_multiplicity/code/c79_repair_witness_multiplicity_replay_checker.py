#!/usr/bin/env python3
"""Clean-process replay wrapper for the independent C79 checker."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
CHECKER = PROJECT / "code/c79_repair_witness_multiplicity_checker.py"


def main() -> None:
    result = subprocess.run(
        [sys.executable, str(CHECKER)],
        cwd=PROJECT,
        check=False,
        capture_output=True,
        text=True,
        env={"PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin", "PYTHONHASHSEED": "0"},
    )
    if result.returncode != 0:
        print(result.stdout, end="")
        print(result.stderr, end="", file=sys.stderr)
        raise SystemExit(result.returncode)
    print(result.stdout, end="")
    print("C79_REPLAY_PASS")


if __name__ == "__main__":
    main()
