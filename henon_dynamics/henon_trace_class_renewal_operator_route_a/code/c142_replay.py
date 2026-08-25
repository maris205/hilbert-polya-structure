#!/usr/bin/env python3
"""Byte-for-byte replay of the canonical C142 evidence receipt."""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    expected = ROOT / "results/c142_renewal_evidence.json"
    with tempfile.TemporaryDirectory(prefix="c142-replay-") as tmp:
        replay = Path(tmp) / "evidence.json"
        subprocess.run([sys.executable, str(ROOT / "code/c142_renewal_producer.py"), "--output", str(replay)], check=True, capture_output=True, text=True)
        if replay.read_bytes() != expected.read_bytes():
            raise SystemExit("C142 replay mismatch")
    print(json.dumps({"status": "PASS", "byte_replay": True}, sort_keys=True))


if __name__ == "__main__":
    main()
