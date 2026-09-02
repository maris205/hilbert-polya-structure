#!/usr/bin/env python3
"""Regenerate C308 evidence twice in isolation and demand byte identity."""
from __future__ import annotations

import hashlib
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c308_hatano_nelson_producer.py"
CANONICAL = ROOT / "results/c308_hatano_nelson_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C308/2026-09-03.yaml"


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="c308-replay-") as tmp:
        first, second = Path(tmp) / "first.json", Path(tmp) / "second.json"
        for target in (first, second):
            subprocess.run([sys.executable, str(PRODUCER), "--output", str(target), "--evaluation", str(EVALUATION)], check=True, capture_output=True, text=True)
        assert first.read_bytes() == second.read_bytes() == CANONICAL.read_bytes()
        digest = hashlib.sha256(first.read_bytes()).hexdigest()
    print(f"C308 isolated replay: PASS (two regenerations byte-identical; evidence_sha256={digest})")


if __name__ == "__main__":
    main()
