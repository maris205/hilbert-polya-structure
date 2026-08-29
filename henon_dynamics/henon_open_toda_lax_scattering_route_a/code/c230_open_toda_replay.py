#!/usr/bin/env python3
"""Clean-process canonical byte replay for C230."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c230_open_toda_producer.py"
EVIDENCE = ROOT / "results/c230_open_toda_evidence.json"


def main() -> None:
    parser = argparse.ArgumentParser(); parser.add_argument("--evidence", type=Path, default=EVIDENCE)
    target = parser.parse_args().evidence
    env = dict(os.environ); env["PYTHONDONTWRITEBYTECODE"] = "1"
    with tempfile.TemporaryDirectory() as folder:
        replay = Path(folder) / "evidence.json"
        subprocess.run([sys.executable, "-B", str(PRODUCER), "--output", str(replay)], check=True, capture_output=True, env=env)
        if replay.read_bytes() != target.read_bytes():
            raise AssertionError("canonical replay mismatch")
    data = json.loads(target.read_text())
    print(json.dumps({"status": "C230_REPLAY_PASS", "bytes": target.stat().st_size, "payload_sha256": data["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
