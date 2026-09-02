#!/usr/bin/env python3
"""Two isolated byte replays for the deterministic C292 evidence."""
from __future__ import annotations

import hashlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c292_sticky_producer.py"
EVIDENCE = ROOT / "results/c292_sticky_evidence.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    hashes = []
    blobs = []
    env = dict(os.environ)
    env.update({"PYTHONDONTWRITEBYTECODE": "1", "TZ": "UTC"})
    for _ in range(2):
        with tempfile.TemporaryDirectory(prefix="c292-replay-") as temporary:
            output = Path(temporary) / "evidence.json"
            text = subprocess.check_output([sys.executable, "-B", str(PRODUCER), "--output", str(output)], env=env, text=True)
            if "C292_PRODUCER_PASS" not in text:
                raise AssertionError(text)
            hashes.append(digest(output))
            blobs.append(output.read_bytes())
    if blobs[0] != blobs[1] or blobs[0] != EVIDENCE.read_bytes():
        raise AssertionError("byte replay mismatch")
    print(f"C292 byte replay: PASS (2/2 isolated outputs; sha256={hashes[0]})")


if __name__ == "__main__":
    main()
