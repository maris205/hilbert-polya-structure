#!/usr/bin/env python3
"""Fresh-path byte replay for HCS-C278."""
from __future__ import annotations

import hashlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c278_camassa_holm_producer.py"
CANONICAL = ROOT / "results/c278_camassa_holm_evidence.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    environment = dict(os.environ)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    with tempfile.TemporaryDirectory(prefix="c278-replay-") as directory:
        first = Path(directory) / "first.json"
        second = Path(directory) / "nested" / "second.json"
        subprocess.run([sys.executable, "-B", str(PRODUCER), "--output", str(first)], check=True, env=environment, stdout=subprocess.DEVNULL)
        subprocess.run([sys.executable, "-B", str(PRODUCER), "--output", str(second)], check=True, env=environment, stdout=subprocess.DEVNULL)
        assert first.read_bytes() == second.read_bytes() == CANONICAL.read_bytes()
        print(f"C278 byte replay: PASS ({digest(first)})")


if __name__ == "__main__":
    main()
