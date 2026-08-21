#!/usr/bin/env python3
from __future__ import annotations

from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c98_conditional_kernel_evidence.json"
CHECKER = PROJECT / "code/c98_conditional_kernel_checker.py"
EXPECTED = "49179ea34f6f10b7e20c68914cdd7aa5bb5df775cefade69f1a40163f2e933cb"


def main() -> None:
    before = sha256(EVIDENCE.read_bytes()).hexdigest()
    assert before == EXPECTED
    env = {**os.environ, "PYTHONHASHSEED": "0", "PYTHONDONTWRITEBYTECODE": "1", "LC_ALL": "C", "TZ": "UTC"}
    run = subprocess.run([sys.executable, str(CHECKER)], cwd=PROJECT, capture_output=True, text=True, check=True, env=env)
    after = sha256(EVIDENCE.read_bytes()).hexdigest()
    assert before == after
    report = json.loads(run.stdout.strip().splitlines()[-1])
    print(json.dumps({"status": "C98_REPLAY_PASS", "ordered_pair_count": report["ordered_pair_count"], "evidence_sha256": after}, sort_keys=True))


if __name__ == "__main__":
    main()
