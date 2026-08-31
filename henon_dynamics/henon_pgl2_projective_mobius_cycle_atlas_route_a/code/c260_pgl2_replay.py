#!/usr/bin/env python3
"""Byte-for-byte evidence replay for HCS-C260."""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c260_pgl2_producer.py"
EVIDENCE = ROOT / "results/c260_pgl2_evidence.json"

with tempfile.TemporaryDirectory(prefix="c260-replay-") as tmp:
    target = Path(tmp) / "evidence.json"
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    output = subprocess.check_output(
        [sys.executable, "-B", str(PRODUCER), "--output", str(target)],
        env=env,
        text=True,
    )
    assert "C260_PRODUCER_PASS" in output
    assert target.read_bytes() == EVIDENCE.read_bytes()

print("C260 byte replay: PASS")
