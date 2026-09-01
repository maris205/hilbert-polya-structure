#!/usr/bin/env python3
"""Two-fresh-path byte replay for HCS-C279."""
from __future__ import annotations

import hashlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c279_path_tv_producer.py"
CANONICAL = ROOT / "results/c279_path_tv_evidence.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    environment = dict(os.environ)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    environment["TZ"] = "UTC"
    with tempfile.TemporaryDirectory(prefix="c279-replay-a-") as first_directory, tempfile.TemporaryDirectory(prefix="c279-replay-b-") as second_directory:
        first = Path(first_directory) / "evidence-a.json"
        second = Path(second_directory) / "nested" / "evidence-b.json"
        subprocess.run(
            [sys.executable, "-B", str(PRODUCER), "--output", str(first)],
            check=True, env=environment, stdout=subprocess.DEVNULL,
        )
        subprocess.run(
            [sys.executable, "-B", str(PRODUCER), "--output", str(second)],
            check=True, env=environment, stdout=subprocess.DEVNULL,
        )
        assert first.read_bytes() == second.read_bytes() == CANONICAL.read_bytes()
        print(f"C279 byte replay: PASS ({digest(first)}; two fresh trees)")


if __name__ == "__main__":
    main()
