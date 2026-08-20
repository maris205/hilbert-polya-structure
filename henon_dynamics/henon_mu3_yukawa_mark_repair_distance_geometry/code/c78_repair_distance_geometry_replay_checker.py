#!/usr/bin/env python3
"""Clean-process replay of the C78 independent checker."""

from __future__ import annotations

import json
import os
from hashlib import sha256
from pathlib import Path
import subprocess
import sys

PROJECT = Path(__file__).resolve().parents[1]
CHECKER = Path(__file__).resolve().parent / "c78_repair_distance_geometry_checker.py"
EVIDENCE = PROJECT / "results/c78_repair_distance_geometry_evidence.json"
EXPECTED = "728d6462b337e3b22fe267ae9388da476a0f6409cc64a17ca659f53f1a8126ae"


def main() -> None:
    before = sha256(EVIDENCE.read_bytes()).hexdigest()
    assert before == EXPECTED, before
    run = subprocess.run(
        [sys.executable, str(CHECKER)], cwd=PROJECT,
        capture_output=True, text=True, check=True,
        env={**os.environ, "PYTHONHASHSEED": "0", "LC_ALL": "C"},
    )
    after = sha256(EVIDENCE.read_bytes()).hexdigest()
    assert after == before
    payload = json.loads(run.stdout.strip().splitlines()[-1])
    assert payload["status"] == "SYMPY_CROSSCHECK_PASS"
    assert payload["support_count"] == 65536
    assert payload["distance_distribution"] == {"0": 30400, "1": 32704, "2": 2368, "3": 64}
    print(json.dumps({
        "status": "REPLAY_PASS",
        "checker_status": payload["status"],
        "evidence_sha256": after,
        "support_count": payload["support_count"],
        "distance_distribution": payload["distance_distribution"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
