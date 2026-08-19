#!/usr/bin/env python3
"""Clean-process replay for the C69 evidence checker."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c69_defect_splitting_evidence.json"
CHECKER = Path(__file__).resolve().parent / "c69_defect_splitting_checker.py"


def main() -> None:
    expected = json.loads(EVIDENCE.read_text())
    run = subprocess.run([sys.executable, str(CHECKER)], cwd=PROJECT,
                         capture_output=True, text=True)
    assert run.returncode == 0, run.stderr
    result = json.loads(run.stdout)
    assert result["status"] == "PASS"
    assert result["retraction"] == "VERIFIED"
    assert result["complement_lattice_index"] == 32
    assert result["complement_smith_invariants"] == expected["complement_smith_invariants"]
    assert result["complement_count"] == 2 ** 41
    print(json.dumps({**result, "status": "REPLAY_PASS"}, sort_keys=True))


if __name__ == "__main__":
    main()
