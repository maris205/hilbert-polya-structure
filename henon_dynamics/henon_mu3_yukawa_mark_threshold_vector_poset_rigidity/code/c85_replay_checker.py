#!/usr/bin/env python3
"""Clean-process replay for C85."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from hashlib import sha256
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c85_threshold_vector_poset_rigidity_evidence.json"
CHECKER = PROJECT / "code/c85_threshold_vector_poset_rigidity_checker.py"
EXPECTED = "22bdaf9fa2fe08532b45eae51cf7704a1509764b5a09f10eebb98012224be152"


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
    assert payload["status"] == "C85_INDEPENDENT_CHECK_PASS"
    assert payload["distinct_vector_count"] == 20
    print(json.dumps({
        "status": "C85_REPLAY_PASS",
        "evidence_sha256": after,
        "distinct_vector_count": payload["distinct_vector_count"],
        "fibre_spectrum": payload["fibre_spectrum"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
