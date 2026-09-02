#!/usr/bin/env python3
"""Require byte-identical regeneration of the canonical C303 evidence."""
from __future__ import annotations

import hashlib
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c303_thermal_qubit_evidence.json"


def main() -> None:
    before = EVIDENCE.read_bytes()
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    out = subprocess.check_output([sys.executable, "-B", str(ROOT / "code/c303_thermal_qubit_producer.py")], env=env, text=True)
    after = EVIDENCE.read_bytes()
    assert "C303_PRODUCER_PASS" in out and before == after
    print(f"C303 byte replay: PASS ({len(after)} bytes; sha256={hashlib.sha256(after).hexdigest()})")


if __name__ == "__main__":
    main()
