#!/usr/bin/env python3
"""Clean-process replay for the C68 evidence checker."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c68_defect_duality_evidence.json"
CHECKER = Path(__file__).resolve().parent / "c68_defect_duality_checker.py"


def main() -> None:
    expected = json.loads(EVIDENCE.read_text())
    run = subprocess.run([sys.executable, str(CHECKER)], cwd=PROJECT,
                         capture_output=True, text=True)
    assert run.returncode == 0, run.stderr
    result = json.loads(run.stdout)
    assert result["status"] == "PASS"
    assert result["D_invariants"] == [2, 2, 8]
    assert result["quotient_smith_invariants"] == expected["quotient_smith_invariants"]
    assert result["dual_smith_invariants"] == expected["row_dual_map_smith_invariants"]
    print(json.dumps({"status": "REPLAY_PASS", **result}, sort_keys=True))


if __name__ == "__main__":
    main()
