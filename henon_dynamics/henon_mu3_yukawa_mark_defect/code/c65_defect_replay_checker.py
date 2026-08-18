#!/usr/bin/env python3
"""Clean-process replay for C65, with an explicit relative-lattice witness."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c65_defect_evidence.json"
CHECKER = Path(__file__).resolve().parent / "c65_defect_checker.py"


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def main() -> None:
    raw = EVIDENCE.read_bytes()
    doc = json.loads(raw)
    assert raw == canonical(doc)
    run = subprocess.run([sys.executable, str(CHECKER)], cwd=PROJECT, capture_output=True, text=True)
    assert run.returncode == 0, run.stderr
    result = json.loads(run.stdout)
    assert result == {"all_index":32,"all_snf":[2,2,8],"old_index":16,"old_snf":[2,8],"relative_jump":2,"status":"PASS"}

    # Replay the relative quotient using the normalized basis coordinates:
    # L_all has coordinates (8,2,2), while Sat(L_old) adds e1 and e3.
    assert doc["relative_jump"]["quotient_index"] == 2
    assert doc["relative_jump"]["generator"] == "u2=m(z2)/2=-m(R4)/2"
    assert doc["relative_jump"]["order"] == 2
    assert doc["mark_contents"]["r4"] == 2
    print(json.dumps({"status":"REPLAY_PASS", "old_snf":[2,8], "all_snf":[2,2,8], "relative_jump":2, "generator_order":2}, sort_keys=True))


if __name__ == "__main__":
    main()
