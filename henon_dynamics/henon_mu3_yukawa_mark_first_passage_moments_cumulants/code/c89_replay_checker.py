#!/usr/bin/env python3
"""Clean-process deterministic replay for C89."""
from __future__ import annotations
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c89_first_passage_moments_evidence.json"
CHECKER = PROJECT / "code/c89_first_passage_moments_checker.py"
EXPECTED = "86a589505280721590674235626ddc21e37d57c891c726c7e6fbba98b2bd3af9"


def main() -> None:
    before = sha256(EVIDENCE.read_bytes()).hexdigest()
    assert before == EXPECTED
    env = {**os.environ, "PYTHONHASHSEED": "0", "PYTHONDONTWRITEBYTECODE": "1", "LC_ALL": "C", "TZ": "UTC"}
    run = subprocess.run([sys.executable, str(CHECKER)], cwd=PROJECT, capture_output=True, text=True, check=True, env=env)
    after = sha256(EVIDENCE.read_bytes()).hexdigest()
    assert after == before
    payload = json.loads(run.stdout.strip().splitlines()[-1])
    assert payload["status"] == "C89_INDEPENDENT_CHECK_PASS"
    print(json.dumps({"status": "C89_REPLAY_PASS", "evidence_sha256": after, "target_count": payload["target_count"]}, sort_keys=True))


if __name__ == "__main__":
    main()
