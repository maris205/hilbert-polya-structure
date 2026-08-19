#!/usr/bin/env python3
"""Run the C77 independent checker in a clean deterministic process."""

from __future__ import annotations

import json
import os
from hashlib import sha256
from pathlib import Path
import subprocess
import sys

PROJECT = Path(__file__).resolve().parents[1]
CHECKER = Path(__file__).resolve().parent / "c77_subgroup_mobius_reliability_checker.py"
EVIDENCE = PROJECT / "results/c77_subgroup_mobius_reliability_evidence.json"
EXPECTED = "f7e2db84698ec61bf6283175368d2749d7f17ac77baeda37fd0a5cb8caf1c634"


def main() -> None:
    before = sha256(EVIDENCE.read_bytes()).hexdigest()
    assert before == EXPECTED, before
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
        "nonnegative_on_rational_grid": True,
        "status": "PASS",
        "subgroup_count": 20,
        "sum_polynomial": {"0": 1},
        "support_count": 65536,
        "top_polynomial_matches_c73": True,
    }, payload
    print(json.dumps({
        "status": "REPLAY_PASS",
        "checker_status": payload["status"],
        "evidence_sha256": after,
        "subgroup_count": payload["subgroup_count"],
        "support_count": payload["support_count"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
