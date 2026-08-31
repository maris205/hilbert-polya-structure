#!/usr/bin/env python3
"""Canonical byte replay for HCS-C263."""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c263_polya_evidence.json"


def main():
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "evidence.json"
        subprocess.check_call([sys.executable, "-B", str(ROOT / "code/c263_polya_producer.py"), "--output", str(out)])
        assert out.read_bytes() == EVIDENCE.read_bytes()
    print(f"C263 byte replay: PASS ({EVIDENCE.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
