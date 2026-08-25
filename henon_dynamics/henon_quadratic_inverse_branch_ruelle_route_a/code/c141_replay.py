#!/usr/bin/env python3
"""Byte-for-byte replay of the canonical C141 evidence."""
from __future__ import annotations

import hashlib
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c141_quadratic_ruelle_producer.py"
CANONICAL = ROOT / "results/c141_quadratic_ruelle_evidence.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="c141-replay-") as directory:
        output = Path(directory) / "evidence.json"
        subprocess.run([sys.executable, str(PRODUCER), "--output", str(output)], check=True, stdout=subprocess.DEVNULL)
        assert output.read_bytes() == CANONICAL.read_bytes(), "producer replay differs byte-for-byte"
        print(f"C141 replay: PASS (sha256={digest(output)})")


if __name__ == "__main__":
    main()
