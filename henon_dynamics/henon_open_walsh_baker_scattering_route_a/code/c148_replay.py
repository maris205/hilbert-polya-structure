#!/usr/bin/env python3
"""Replay C148 evidence in isolation and demand canonical byte identity."""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]


def main():
    with tempfile.TemporaryDirectory(prefix="c148-replay-") as temporary:
        output = Path(temporary) / "evidence.json"
        subprocess.run(
            [sys.executable, str(ROOT / "code/c148_walsh_baker_producer.py"), "--output", str(output)],
            check=True,
            capture_output=True,
            text=True,
        )
        frozen = ROOT / "results/c148_walsh_baker_evidence.json"
        if output.read_bytes() != frozen.read_bytes():
            raise SystemExit("C148 canonical replay mismatch")
    print(json.dumps({"status": "PASS", "byte_replay": True}, sort_keys=True))


if __name__ == "__main__":
    main()
