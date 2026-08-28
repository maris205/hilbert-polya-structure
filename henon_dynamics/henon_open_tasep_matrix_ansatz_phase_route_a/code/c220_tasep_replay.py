#!/usr/bin/env python3
"""Byte-for-byte clean-process replay of the C220 producer."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = Path(__file__).with_name("c220_tasep_producer.py")
DEFAULT_EVIDENCE = ROOT / "results/c220_tasep_evidence.json"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    target = parser.parse_args().evidence
    with tempfile.TemporaryDirectory() as folder:
        replay = Path(folder) / "evidence.json"
        subprocess.run([sys.executable, "-B", str(PRODUCER), "--output", str(replay)], check=True, capture_output=True)
        if replay.read_bytes() != target.read_bytes():
            raise AssertionError("canonical replay mismatch")
    obj = json.loads(target.read_text())
    print(json.dumps({"status": "C220_REPLAY_PASS", "bytes": target.stat().st_size, "payload_sha256": obj["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
