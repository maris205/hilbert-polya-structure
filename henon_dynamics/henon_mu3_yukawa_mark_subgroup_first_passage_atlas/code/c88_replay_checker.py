#!/usr/bin/env python3
"""Clean-process deterministic replay for C88."""

from __future__ import annotations

from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c88_subgroup_first_passage_atlas_evidence.json"
CHECKER = PROJECT / "code/c88_subgroup_first_passage_atlas_checker.py"
EXPECTED = "4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b"


def main() -> None:
    before = sha256(EVIDENCE.read_bytes()).hexdigest()
    assert before == EXPECTED
    environment = {
        **os.environ,
        "PYTHONHASHSEED": "0",
        "PYTHONDONTWRITEBYTECODE": "1",
        "LC_ALL": "C",
        "TZ": "UTC",
    }
    run = subprocess.run(
        [sys.executable, str(CHECKER)],
        cwd=PROJECT,
        capture_output=True,
        text=True,
        check=True,
        env=environment,
    )
    after = sha256(EVIDENCE.read_bytes()).hexdigest()
    assert after == before
    payload = json.loads(run.stdout.strip().splitlines()[-1])
    assert payload["status"] == "C88_INDEPENDENT_CHECK_PASS"
    assert payload["target_count"] == 20
    print(json.dumps({
        "status": "C88_REPLAY_PASS",
        "evidence_sha256": after,
        "target_count": payload["target_count"],
        "minimal_support_counts": payload["minimal_support_counts"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
