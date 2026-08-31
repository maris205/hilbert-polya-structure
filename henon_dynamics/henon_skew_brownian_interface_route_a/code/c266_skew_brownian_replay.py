#!/usr/bin/env python3
"""Fresh-path byte replay for HCS-C266."""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "results/c266_skew_brownian_evidence.json"
PRODUCER = ROOT / "code/c266_skew_brownian_producer.py"


def main():
    with tempfile.TemporaryDirectory(prefix="c266-replay-") as tmp:
        fresh = Path(tmp) / "fresh.json"
        out = subprocess.check_output([sys.executable, "-B", str(PRODUCER), "--output", str(fresh)], text=True)
        assert "C266_PRODUCER_PASS" in out
        assert fresh.read_bytes() == EXPECTED.read_bytes()
    print(f"C266 byte replay: PASS ({EXPECTED.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
