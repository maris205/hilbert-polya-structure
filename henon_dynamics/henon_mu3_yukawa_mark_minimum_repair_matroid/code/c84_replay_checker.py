#!/usr/bin/env python3
"""Clean-process replay wrapper for C84."""

from __future__ import annotations

from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c84_minimum_repair_matroid_evidence.json"
CHECKER = PROJECT / "code/c84_minimum_repair_matroid_checker.py"


def main() -> None:
    before = sha256(EVIDENCE.read_bytes()).hexdigest()
    result = subprocess.run(
        [sys.executable, str(CHECKER)],
        cwd=PROJECT,
        capture_output=True,
        text=True,
        check=True,
        env={**os.environ, "PYTHONHASHSEED": "0", "LC_ALL": "C"},
    )
    after = sha256(EVIDENCE.read_bytes()).hexdigest()
    assert before == after
    payload = json.loads(result.stdout.strip().splitlines()[-1])
    assert payload["status"] == "C84_INDEPENDENT_CHECK_PASS"
    print(json.dumps({
        "status": "C84_REPLAY_PASS",
        "evidence_sha256": after,
        "deletion_set_count": payload["deletion_set_count"],
        "all_deleted_basis_count": payload["all_deleted_basis_count"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
