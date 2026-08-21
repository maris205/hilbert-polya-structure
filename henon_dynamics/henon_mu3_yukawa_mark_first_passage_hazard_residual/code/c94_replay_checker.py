#!/usr/bin/env python3
"""Clean-process deterministic replay for the C94 checker."""

from __future__ import annotations

from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c94_first_passage_hazard_residual_evidence.json"
CHECKER = PROJECT / "code/c94_first_passage_hazard_residual_checker.py"
EXPECTED = "e185462629459a7d6602e3d1e3f49977a82d3fdee86007c3f906b224f028d1b3"


def main() -> None:
    before = sha256(EVIDENCE.read_bytes()).hexdigest()
    assert before == EXPECTED
    env = {**os.environ, "PYTHONHASHSEED": "0", "PYTHONDONTWRITEBYTECODE": "1", "LC_ALL": "C", "TZ": "UTC"}
    run = subprocess.run([sys.executable, "-B", str(CHECKER)], cwd=PROJECT, capture_output=True, text=True, check=True, env=env)
    after = sha256(EVIDENCE.read_bytes()).hexdigest()
    assert before == after
    payload = json.loads(run.stdout.strip().splitlines()[-1])
    assert payload["status"] == "C94_INDEPENDENT_CHECK_PASS"
    print(json.dumps({"status": "C94_REPLAY_PASS", "evidence_sha256": after, "target_count": payload["target_count"]}, sort_keys=True))


if __name__ == "__main__":
    main()
