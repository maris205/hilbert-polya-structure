#!/usr/bin/env python3
"""Clean deterministic replay for C101."""
from __future__ import annotations

from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c101_triple_coupling_evidence.json"
CHECKER = PROJECT / "code/c101_triple_coupling_checker.py"
EXPECTED = "43d71ab86e84def24b50563334f92a72efaf122a5760caab975e19b5ed46306d"


def main() -> None:
    before = sha256(EVIDENCE.read_bytes()).hexdigest()
    assert before == EXPECTED
    env = {**os.environ, "PYTHONHASHSEED": "0", "PYTHONDONTWRITEBYTECODE": "1", "LC_ALL": "C", "TZ": "UTC"}
    run = subprocess.run([sys.executable, "-B", str(CHECKER)], cwd=PROJECT, capture_output=True, text=True, check=True, env=env)
    after = sha256(EVIDENCE.read_bytes()).hexdigest()
    assert after == before
    payload = json.loads(run.stdout.strip().splitlines()[-1])
    print(json.dumps({"status": "C101_REPLAY_PASS", "triple_count": payload["triple_count"], "pmf_cells": payload["pmf_cells"], "evidence_sha256": after}, sort_keys=True))


if __name__ == "__main__":
    main()
