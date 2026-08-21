#!/usr/bin/env python3
"""Clean-process deterministic replay for C92."""

from __future__ import annotations

from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c92_first_passage_label_sensitivity_evidence.json"
CHECKER = PROJECT / "code/c92_first_passage_label_sensitivity_checker.py"
EXPECTED = "902d6b2fd688abc525d2fab187559bfc9904c7f3c97dc51af62050586d145812"


def main() -> None:
    before = sha256(EVIDENCE.read_bytes()).hexdigest()
    assert before == EXPECTED
    env = {**os.environ, "PYTHONHASHSEED": "0", "PYTHONDONTWRITEBYTECODE": "1", "LC_ALL": "C", "TZ": "UTC"}
    run = subprocess.run([sys.executable, str(CHECKER)], cwd=PROJECT, capture_output=True, text=True, check=True, env=env)
    after = sha256(EVIDENCE.read_bytes()).hexdigest()
    assert after == before
    payload = json.loads(run.stdout.strip().splitlines()[-1])
    assert payload["status"] == "C92_INDEPENDENT_CHECK_PASS"
    print(json.dumps({"status": "C92_REPLAY_PASS", "evidence_sha256": after, "target_count": payload["target_count"]}, sort_keys=True))


if __name__ == "__main__":
    main()
