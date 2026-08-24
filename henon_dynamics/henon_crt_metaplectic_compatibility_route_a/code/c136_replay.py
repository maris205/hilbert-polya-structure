#!/usr/bin/env python3
"""Byte-for-byte deterministic replay for HCS-C136."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
with tempfile.TemporaryDirectory(prefix="c136-replay-") as tmp:
    output = Path(tmp) / "evidence.json"
    subprocess.run(
        [sys.executable, str(ROOT / "code" / "c136_crt_metaplectic_producer.py"), "--output", str(output)],
        check=True,
        stdout=subprocess.DEVNULL,
    )
    assert output.read_bytes() == (ROOT / "results" / "c136_crt_metaplectic_evidence.json").read_bytes()
print("C136 deterministic replay: PASS")
