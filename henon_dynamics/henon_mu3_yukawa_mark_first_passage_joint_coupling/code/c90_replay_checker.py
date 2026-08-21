#!/usr/bin/env python3
"""Clean deterministic replay for C90."""
from __future__ import annotations
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c90_joint_first_passage_evidence.json"
CHECKER = PROJECT / "code/c90_joint_first_passage_checker.py"
EXPECTED = "c457a267b2621c71f7f5ad810ce9dec41aacfe25de3e843fab1398be75571978"


def main() -> None:
    before = sha256(EVIDENCE.read_bytes()).hexdigest()
    assert before == EXPECTED
    env = {**os.environ, "PYTHONHASHSEED": "0", "PYTHONDONTWRITEBYTECODE": "1", "LC_ALL": "C", "TZ": "UTC"}
    run = subprocess.run([sys.executable, str(CHECKER)], cwd=PROJECT, capture_output=True, text=True, check=True, env=env)
    after = sha256(EVIDENCE.read_bytes()).hexdigest()
    assert after == before
    payload = json.loads(run.stdout.strip().splitlines()[-1])
    assert payload["status"] == "C90_INDEPENDENT_CHECK_PASS"
    print(json.dumps({"status": "C90_REPLAY_PASS", "ordered_pair_count": payload["ordered_pair_count"], "evidence_sha256": after}, sort_keys=True))


if __name__ == "__main__":
    main()
