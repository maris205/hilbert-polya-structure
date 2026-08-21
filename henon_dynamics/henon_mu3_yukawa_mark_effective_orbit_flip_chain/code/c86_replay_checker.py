#!/usr/bin/env python3
"""Clean-process replay wrapper for C86."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from hashlib import sha256
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c86_effective_orbit_flip_chain_evidence.json"
CHECKER = PROJECT / "code/c86_effective_orbit_flip_chain_checker.py"


def main() -> None:
    before = sha256(EVIDENCE.read_bytes()).hexdigest()
    result = subprocess.run(
        [sys.executable, str(CHECKER)],
        cwd=PROJECT,
        capture_output=True,
        text=True,
        check=True,
        env={**os.environ, "PYTHONHASHSEED": "0", "LC_ALL": "C"},
    )
    after = sha256(EVIDENCE.read_bytes()).hexdigest()
    assert before == after
    payload = json.loads(result.stdout.strip().splitlines()[-1])
    assert payload["status"] == "C86_INDEPENDENT_CHECK_PASS"
    print(json.dumps({
        "status": "C86_REPLAY_PASS",
        "evidence_sha256": after,
        "orbit_count": payload["orbit_count"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
