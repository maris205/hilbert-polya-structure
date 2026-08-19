#!/usr/bin/env python3
"""Clean-process replay and semantic compatibility check for C66."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c66_mark_snf_evidence.json"
CHECKER = Path(__file__).resolve().parent / "c66_mark_snf_checker.py"


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def main() -> None:
    raw = EVIDENCE.read_bytes()
    doc = json.loads(raw)
    assert raw == canonical(doc)
    run = subprocess.run([sys.executable, str(CHECKER)], cwd=PROJECT, capture_output=True, text=True)
    assert run.returncode == 0, run.stderr
    result = json.loads(run.stdout)
    expected = {
        "status": "PASS",
        "smith_invariants": [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 24, 144],
        "determinant": 226492416,
        "primary_2": [2] * 10 + [4] * 3 + [8, 16],
        "primary_3": [3, 9],
    }
    assert result == expected
    assert doc["c65_compatibility"] == {"old_snf": [2, 8], "all_snf": [2, 2, 8], "relative_quotient": "Z/2"}
    assert doc["claims"]["restricted_16_type_mark_cokernel_only"] is True
    print(json.dumps({"status": "REPLAY_PASS", "smith_invariants": expected["smith_invariants"],
                      "determinant": expected["determinant"], "primary_2": expected["primary_2"],
                      "primary_3": expected["primary_3"]}, sort_keys=True))


if __name__ == "__main__":
    main()
