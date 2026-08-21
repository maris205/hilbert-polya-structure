#!/usr/bin/env python3
"""Clean-process replay for C80."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from hashlib import sha256
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c80_threshold_repair_atlas_evidence.json"
CHECKER = PROJECT / "code/c80_threshold_repair_atlas_checker.py"
EXPECTED = "8d27428b14dbd7354e9c8308ad76b1108e3f551702165833301509cd52de7df5"


def main():
    before = sha256(EVIDENCE.read_bytes()).hexdigest()
    assert before == EXPECTED
    result = subprocess.run([sys.executable, str(CHECKER)], cwd=PROJECT,
                            capture_output=True, text=True, check=True,
                            env={**os.environ, "PYTHONHASHSEED": "0", "LC_ALL": "C"})
    after = sha256(EVIDENCE.read_bytes()).hexdigest()
    assert after == before
    payload = json.loads(result.stdout.strip().splitlines()[-1])
    assert payload["status"] == "C80_INDEPENDENT_CHECK_PASS"
    print(json.dumps({"status": "C80_REPLAY_PASS", "evidence_sha256": after,
                      "q_distribution": payload["q_distribution"]}, sort_keys=True))


if __name__ == "__main__":
    main()
