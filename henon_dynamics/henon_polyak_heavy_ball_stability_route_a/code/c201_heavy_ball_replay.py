#!/usr/bin/env python3
"""Reproduce C201 evidence and require byte identity."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
PRODUCER = Path(__file__).with_name("c201_heavy_ball_producer.py")
EVIDENCE = ROOT / "results/c201_heavy_ball_evidence.json"


def main() -> None:
    with tempfile.TemporaryDirectory() as folder:
        candidate = Path(folder) / "evidence.json"
        subprocess.run([sys.executable, str(PRODUCER), "--output", str(candidate)], check=True, capture_output=True)
        if candidate.read_bytes() != EVIDENCE.read_bytes():
            raise AssertionError("canonical replay mismatch")
    print(json.dumps({"status": "C201_REPLAY_PASS", "bytes": EVIDENCE.stat().st_size}, sort_keys=True))


if __name__ == "__main__":
    main()
