#!/usr/bin/env python3
"""Clean-process deterministic replay for C91."""

from __future__ import annotations

from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c91_first_passage_race_atlas_evidence.json"
CHECKER = PROJECT / "code/c91_first_passage_race_atlas_checker.py"
EXPECTED = "36b0fffda585ea483ba5603101c83c361b85ca4ba9a49c878f1e366d3c13ff0f"


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
    run = subprocess.run([sys.executable, str(CHECKER)], cwd=PROJECT, capture_output=True, text=True, check=True, env=environment)
    after = sha256(EVIDENCE.read_bytes()).hexdigest()
    assert after == before
    payload = json.loads(run.stdout.strip().splitlines()[-1])
    assert payload["status"] == "C91_INDEPENDENT_CHECK_PASS"
    assert payload["pair_count"] == 108
    print(json.dumps({"status": "C91_REPLAY_PASS", "evidence_sha256": after, "pair_count": payload["pair_count"], "pairs_with_nonzero_ties": payload["pairs_with_nonzero_ties"]}, sort_keys=True))


if __name__ == "__main__":
    main()
