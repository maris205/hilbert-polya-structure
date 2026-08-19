#!/usr/bin/env python3
"""Run the C76 independent checker in a fresh Python process."""

from __future__ import annotations

import json
from hashlib import sha256
import os
from pathlib import Path
import subprocess
import sys

PROJECT = Path(__file__).resolve().parents[1]
CHECKER = Path(__file__).resolve().parent / "c76_closure_orbit_atlas_checker.py"
EVIDENCE = PROJECT / "results/c76_closure_orbit_atlas_evidence.json"
EXPECTED_EVIDENCE_SHA256 = "42e7783b2652666b84ea7f82b65d2421d98064ee5d5011ab94033aa18c051a94"


def main() -> None:
    before = sha256(EVIDENCE.read_bytes()).hexdigest()
    assert before == EXPECTED_EVIDENCE_SHA256
    run = subprocess.run(
        [sys.executable, str(CHECKER)],
        cwd=PROJECT,
        capture_output=True,
        text=True,
        check=True,
        env={**os.environ, "PYTHONHASHSEED": "0", "LC_ALL": "C"},
    )
    after = sha256(EVIDENCE.read_bytes()).hexdigest()
    assert after == before
    payload = json.loads(run.stdout.strip().splitlines()[-1])
    assert payload == {
        "closure_minimal_orbit_count": 34,
        "closure_minimal_support_count": 98,
        "effective_group_order": 1920,
        "full_core_minimal_orbit_count": 7,
        "full_core_minimal_support_count": 25,
        "orbit_count": 3024,
        "status": "PASS",
    }
    print(json.dumps({
        "status": "REPLAY_PASS",
        "checker_status": payload["status"],
        "evidence_sha256": after,
        "orbit_count": payload["orbit_count"],
        "closure_minimal_support_count": payload["closure_minimal_support_count"],
        "full_core_minimal_support_count": payload["full_core_minimal_support_count"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
