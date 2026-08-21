#!/usr/bin/env python3
"""Clean-process replay wrapper for C82."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from hashlib import sha256
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c82_bitflip_noise_fourier_evidence.json"
CHECKER = PROJECT / "code/c82_bitflip_noise_fourier_checker.py"


def main():
    before = sha256(EVIDENCE.read_bytes()).hexdigest()
    result = subprocess.run([sys.executable, str(CHECKER)], cwd=PROJECT,
                            capture_output=True, text=True, check=True,
                            env={**os.environ, "PYTHONHASHSEED": "0", "LC_ALL": "C"})
    after = sha256(EVIDENCE.read_bytes()).hexdigest()
    assert after == before
    payload = json.loads(result.stdout.strip().splitlines()[-1])
    assert payload["status"] == "C82_INDEPENDENT_CHECK_PASS"
    print(json.dumps({"status": "C82_REPLAY_PASS", "evidence_sha256": after,
                      "one_count": payload["one_count"]}, sort_keys=True))


if __name__ == "__main__":
    main()
