#!/usr/bin/env python3
"""Clean-process replay for the C67 coordinate profile."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c67_coordinate_profile_evidence.json"
CHECKER = Path(__file__).resolve().parent / "c67_coordinate_profile_checker.py"


def main() -> None:
    doc = json.loads(EVIDENCE.read_text())
    run = subprocess.run(
        [sys.executable, str(CHECKER)],
        cwd=PROJECT,
        capture_output=True,
        text=True,
    )
    assert run.returncode == 0, run.stderr
    result = json.loads(run.stdout)
    expected = {
        "status": "PASS",
        "coordinate_orders": [36, 12, 6, 6, 2, 2, 36, 6, 16, 8, 6, 12, 2, 2, 36, 36],
        "dual_coordinate_orders": [1, 4, 2, 2, 2, 2, 36, 6, 16, 8, 2, 4, 2, 2, 2, 2],
        "global_denominator": 144,
        "inverse_nonzero_count": 43,
    }
    assert result == expected
    assert doc["coordinate_lcm"] == doc["dual_coordinate_lcm"] == 144
    print(json.dumps({"status": "REPLAY_PASS", **expected}, sort_keys=True))


if __name__ == "__main__":
    main()
