#!/usr/bin/env python3
from __future__ import annotations

from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c97_pair_orbit_quotient_evidence.json"
CHECKER = PROJECT / "code/c97_pair_orbit_quotient_checker.py"
EXPECTED = "099d8f32794d6967b3f2653f92dcaa0b096c711b67ed070330d7763a146bc696"


def main() -> None:
    before = sha256(EVIDENCE.read_bytes()).hexdigest()
    assert before == EXPECTED
    env = {**os.environ, "PYTHONHASHSEED": "0", "PYTHONDONTWRITEBYTECODE": "1", "LC_ALL": "C", "TZ": "UTC"}
    run = subprocess.run([sys.executable, str(CHECKER)], cwd=PROJECT, capture_output=True, text=True, check=True, env=env)
    after = sha256(EVIDENCE.read_bytes()).hexdigest()
    assert before == after
    report = json.loads(run.stdout.strip().splitlines()[-1])
    print(json.dumps({"status": "C97_REPLAY_PASS", "pair_orbit_count": report["pair_orbit_count"], "evidence_sha256": after}, sort_keys=True))


if __name__ == "__main__":
    main()
