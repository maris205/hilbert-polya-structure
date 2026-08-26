#!/usr/bin/env python3
"""Byte-for-byte producer replay for HCS-C171."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c171_ehrenfest_evidence.json"
PRODUCER = ROOT / "code/c171_ehrenfest_producer.py"


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="c171-replay-") as temporary:
        output = Path(temporary) / "evidence.json"
        subprocess.run([sys.executable, str(PRODUCER), "--output", str(output)], check=True,
                       capture_output=True, text=True)
        if output.read_bytes() != EVIDENCE.read_bytes():
            raise AssertionError("producer replay differs byte-for-byte")
    print(json.dumps({"status": "C171_REPLAY_PASS", "sha256": sha256(EVIDENCE.read_bytes()).hexdigest()}, sort_keys=True))


if __name__ == "__main__":
    main()
