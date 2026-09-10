#!/usr/bin/env python3
"""Clean-process deterministic replay for C100."""
from __future__ import annotations
from hashlib import sha256
import json, os, subprocess, sys
from pathlib import Path
PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c100_pair_dependence_geometry_evidence.json"
CHECKER = PROJECT / "code/c100_pair_dependence_geometry_checker.py"


def main() -> None:
    before = sha256(EVIDENCE.read_bytes()).hexdigest()
    env = {**os.environ, "PYTHONHASHSEED": "0", "PYTHONDONTWRITEBYTECODE": "1", "LC_ALL": "C", "TZ": "UTC"}
    run = subprocess.run([sys.executable, "-B", str(CHECKER)], cwd=PROJECT, capture_output=True, text=True, check=True, env=env)
    after = sha256(EVIDENCE.read_bytes()).hexdigest()
    assert after == before
    payload = json.loads(run.stdout.strip().splitlines()[-1])
    assert payload["status"] == "C100_INDEPENDENT_CHECK_PASS"
    print(json.dumps({"status": "C100_REPLAY_PASS", "evidence_sha256": after, "ordered_pair_count": payload["ordered_pair_count"], "joint_pmf_cells": payload["joint_pmf_cells"]}, sort_keys=True))


if __name__ == "__main__":
    main()
