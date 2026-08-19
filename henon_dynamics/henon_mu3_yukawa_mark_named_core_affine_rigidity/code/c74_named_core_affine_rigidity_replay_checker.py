#!/usr/bin/env python3
"""Clean-process replay for the C74 independent checker."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys

PROJECT = Path(__file__).resolve().parents[1]
CHECKER = Path(__file__).resolve().parent / "c74_named_core_affine_rigidity_checker.py"


def main() -> None:
    run = subprocess.run([sys.executable, str(CHECKER)], cwd=PROJECT,
                         capture_output=True, text=True, check=True)
    print(run.stdout.strip().replace('"status": "PASS"', '"status": "REPLAY_PASS"'))


if __name__ == "__main__":
    main()
