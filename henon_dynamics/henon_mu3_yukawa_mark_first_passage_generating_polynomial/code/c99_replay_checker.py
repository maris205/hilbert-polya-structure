#!/usr/bin/env python3
"""Clean-process deterministic replay for C99."""
from __future__ import annotations
from hashlib import sha256
import json, os, subprocess, sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c99_generating_polynomial_evidence.json"
CHECKER = PROJECT / "code/c99_generating_polynomial_checker.py"
EXPECTED = "6ef947aeba00ca89fc03b96be877402e55ed7e72451711796a0b44d51ce467ad"


def main() -> None:
    before = sha256(EVIDENCE.read_bytes()).hexdigest()
    assert before == EXPECTED
    env = {**os.environ, "PYTHONHASHSEED": "0", "PYTHONDONTWRITEBYTECODE": "1", "LC_ALL": "C", "TZ": "UTC"}
    run = subprocess.run([sys.executable, str(CHECKER)], cwd=PROJECT, capture_output=True, text=True, check=True, env=env)
    after = sha256(EVIDENCE.read_bytes()).hexdigest()
    assert after == before
    payload = json.loads(run.stdout.strip().splitlines()[-1])
    assert payload["status"] == "C99_INDEPENDENT_CHECK_PASS"
    print(json.dumps({"status": "C99_REPLAY_PASS", "target_count": payload["target_count"], "coefficient_cells": payload["coefficient_cells"], "evidence_sha256": after}, sort_keys=True))


if __name__ == "__main__":
    main()
