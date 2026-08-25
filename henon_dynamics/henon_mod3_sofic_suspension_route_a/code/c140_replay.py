#!/usr/bin/env python3
"""Replay C140 production in isolation and require byte identity."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c140_sofic_producer.py"
CHECKER = ROOT / "code/c140_sofic_checker.py"
CANONICAL = ROOT / "results/c140_sofic_evidence.json"


def main():
    with tempfile.TemporaryDirectory(prefix="c140-replay-") as temporary:
        candidate = Path(temporary) / "evidence.json"
        subprocess.run([sys.executable, str(PRODUCER), "--output", str(candidate)], check=True, capture_output=True, text=True)
        if candidate.read_bytes() != CANONICAL.read_bytes():
            raise AssertionError("producer replay is not byte-identical")
        subprocess.run([sys.executable, str(CHECKER), str(candidate)], check=True, capture_output=True, text=True)
    raw = CANONICAL.read_bytes()
    print(json.dumps({"status": "C140_REPLAY_PASS", "bytes": len(raw), "sha256": sha256(raw).hexdigest()}, sort_keys=True))


if __name__ == "__main__":
    main()
