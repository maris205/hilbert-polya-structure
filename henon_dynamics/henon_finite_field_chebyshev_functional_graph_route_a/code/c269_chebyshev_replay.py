#!/usr/bin/env python3
"""Fresh byte replay for HCS-C269."""
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "results/c269_chebyshev_evidence.json"
with tempfile.TemporaryDirectory(prefix="c269-replay-") as td:
    out = Path(td) / "evidence.json"
    text = subprocess.check_output(
        [sys.executable, "-B", str(ROOT / "code/c269_chebyshev_producer.py"), "--output", str(out)], text=True
    )
    assert "C269_PRODUCER_PASS" in text
    assert out.read_bytes() == EXPECTED.read_bytes()
print("C269 byte replay: PASS")
