#!/usr/bin/env python3
"""Replay C150 production in isolation and require byte identity."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c150_mersenne_producer.py"
CHECKER = ROOT / "code/c150_mersenne_checker.py"
CANONICAL = ROOT / "results/c150_rule90_mersenne_evidence.json"


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="c150-replay-") as temporary:
        candidate = Path(temporary) / "evidence.json"
        subprocess.run([sys.executable, str(PRODUCER), "--output", str(candidate)], check=True, capture_output=True, text=True)
        if candidate.read_bytes() != CANONICAL.read_bytes():
            raise AssertionError("producer replay is not byte-identical")
        subprocess.run([sys.executable, str(CHECKER), str(candidate)], check=True, capture_output=True, text=True)
    raw = CANONICAL.read_bytes()
    print(json.dumps({"status": "C150_REPLAY_PASS", "bytes": len(raw), "sha256": sha256(raw).hexdigest()}, sort_keys=True))


if __name__ == "__main__":
    main()
