#!/usr/bin/env python3
"""Fresh byte replay for HCS-C264."""
import subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "results/c264_power_map_evidence.json"
with tempfile.TemporaryDirectory(prefix="c264-replay-") as td:
    out = Path(td) / "evidence.json"
    result = subprocess.check_output([sys.executable, "-B", str(ROOT / "code/c264_power_map_producer.py"), "--output", str(out)], text=True)
    assert "C264_PRODUCER_PASS" in result
    assert out.read_bytes() == EXPECTED.read_bytes()
print("C264 byte replay: PASS")
