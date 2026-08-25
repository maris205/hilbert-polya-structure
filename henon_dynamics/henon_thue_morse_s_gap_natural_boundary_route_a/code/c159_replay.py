#!/usr/bin/env python3
"""Canonical byte replay for HCS-C159."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c159_s_gap_evidence.json"
PRODUCER = ROOT / "code/c159_s_gap_producer.py"


def main() -> None:
    released = EVIDENCE.read_bytes()
    with tempfile.TemporaryDirectory(prefix="c159-replay-") as temporary:
        target = Path(temporary) / "evidence.json"
        subprocess.run([sys.executable, str(PRODUCER), "--output", str(target)], check=True, capture_output=True, text=True)
        replayed = target.read_bytes()
    if replayed != released:
        raise AssertionError("canonical replay differs from released evidence")
    print(json.dumps({"status": "C159_REPLAY_PASS", "bytes": len(released), "file_sha256": sha256(released).hexdigest()}, sort_keys=True))


if __name__ == "__main__":
    main()
