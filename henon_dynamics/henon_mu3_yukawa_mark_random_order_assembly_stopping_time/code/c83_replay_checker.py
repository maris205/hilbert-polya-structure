#!/usr/bin/env python3
"""Clean-process replay wrapper for C83."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from hashlib import sha256
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c83_random_order_stopping_time_evidence.json"
CHECKER = PROJECT / "code/c83_random_order_stopping_time_checker.py"


def main():
    before = sha256(EVIDENCE.read_bytes()).hexdigest()
    result = subprocess.run([sys.executable, str(CHECKER)], cwd=PROJECT,
                            capture_output=True, text=True, check=True,
                            env={**os.environ, "PYTHONHASHSEED": "0", "LC_ALL": "C"})
    after = sha256(EVIDENCE.read_bytes()).hexdigest()
    assert before == after
    payload = json.loads(result.stdout.strip().splitlines()[-1])
    assert payload["status"] == "C83_INDEPENDENT_CHECK_PASS"
    print(json.dumps({"status": "C83_REPLAY_PASS", "evidence_sha256": after,
                      "total_permutations": payload["total_permutations"]}, sort_keys=True))


if __name__ == "__main__":
    main()
