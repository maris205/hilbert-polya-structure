#!/usr/bin/env python3
"""Byte-for-byte evidence replay for HCS-C258."""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c258_lcg_producer.py"
EVIDENCE = ROOT / "results/c258_lcg_evidence.json"

with tempfile.TemporaryDirectory(prefix="c258-replay-") as tmp:
    target = Path(tmp) / "evidence.json"
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    output = subprocess.check_output(
        [sys.executable, "-B", str(PRODUCER), "--output", str(target)],
        env=env,
        text=True,
    )
    assert "C258_PRODUCER_PASS" in output
    assert target.read_bytes() == EVIDENCE.read_bytes()

print("C258 byte replay: PASS")
