#!/usr/bin/env python3
"""Clean-process byte replay for C210."""
import argparse
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = Path(__file__).with_name("c210_delay_producer.py")
EVIDENCE = ROOT / "results/c210_delay_evidence.json"


def main() -> None:
    ap = argparse.ArgumentParser(); ap.add_argument("--evidence", type=Path, default=EVIDENCE)
    target = ap.parse_args().evidence
    with tempfile.TemporaryDirectory() as folder:
        replay = Path(folder) / "evidence.json"
        subprocess.run([sys.executable, str(PRODUCER), "--output", str(replay)], check=True, capture_output=True)
        if replay.read_bytes() != target.read_bytes():
            raise AssertionError("canonical replay mismatch")
    print(json.dumps({"status": "C210_REPLAY_PASS", "bytes": target.stat().st_size}, sort_keys=True))


if __name__ == "__main__":
    main()
