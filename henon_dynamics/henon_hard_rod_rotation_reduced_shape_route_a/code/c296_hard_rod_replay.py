#!/usr/bin/env python3
"""Two isolated deterministic evidence replays for HCS-C296."""
from __future__ import annotations

import hashlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c296_hard_rod_producer.py"
EVIDENCE = ROOT / "results/c296_hard_rod_evidence.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    env = dict(os.environ)
    env.update({"PYTHONDONTWRITEBYTECODE": "1", "TZ": "UTC"})
    blobs = []
    hashes = []
    for _ in range(2):
        with tempfile.TemporaryDirectory(prefix="c296-replay-") as temporary:
            output = Path(temporary) / "evidence.json"
            text = subprocess.check_output([sys.executable, "-B", str(PRODUCER), "--output", str(output)], env=env, text=True)
            if "C296_PRODUCER_PASS" not in text:
                raise AssertionError(text)
            blobs.append(output.read_bytes())
            hashes.append(digest(output))
    if blobs[0] != blobs[1] or blobs[0] != EVIDENCE.read_bytes():
        raise AssertionError("byte replay mismatch")
    print(f"C296 byte replay: PASS (2/2 isolated outputs; sha256={hashes[0]})")


if __name__ == "__main__":
    main()
