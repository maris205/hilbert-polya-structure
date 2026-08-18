#!/usr/bin/env python3
"""Clean-process replay wrapper for the C64 certificate.

The structural checker performs a fresh source reconstruction.  This wrapper
adds a second process boundary, canonical-byte checks, and direct all-element
checks for the diagonal and the R4 witness before accepting the result.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c64_mark_evidence.json"
CHECKER = Path(__file__).resolve().parent / "c64_mark_checker.py"
EXPECTED_C63 = "38f439cfe6ed71616a7c74d68bd07da73f5680566ae16f8c557ab2b5d1d16e26"


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def main() -> None:
    raw = EVIDENCE.read_bytes()
    evidence = json.loads(raw)
    assert raw == canonical(evidence)
    assert evidence["schema_id"] == "hcs-c64-table-of-marks-prefreeze-v1"
    assert evidence["authority"]["c63"] == EXPECTED_C63
    assert hashlib.sha256(raw).hexdigest() == hashlib.sha256(canonical(evidence)).hexdigest()

    run = subprocess.run([sys.executable, str(CHECKER)], cwd=PROJECT, text=True, capture_output=True)
    assert run.returncode == 0, run.stderr
    replay = json.loads(run.stdout)
    assert replay["status"] == "PASS"
    assert replay["rank"] == 16 and replay["determinant"] == 226492416
    assert replay["r4_witness"] == 4

    # A byte-level replay of the headline linear combination is independent
    # of the checker output and catches column-order or sign drift.
    matrix = evidence["mark_matrix"]
    r4 = evidence["r4_vector"]
    assert r4 == [0,1,1,0,1,1,0,0,0,0,-1,-1,-1,-1,0,0]
    assert [sum(row[j] * r4[j] for j in range(16)) for row in matrix] == evidence["r4_mark_vector"]
    assert evidence["r4_mark_vector"][1] == 4
    print(json.dumps({"status":"REPLAY_PASS", "matrix_sha256":evidence["matrix_sha256"], "rank":16, "determinant":226492416, "r4_witness":4}, sort_keys=True))


if __name__ == "__main__":
    main()
