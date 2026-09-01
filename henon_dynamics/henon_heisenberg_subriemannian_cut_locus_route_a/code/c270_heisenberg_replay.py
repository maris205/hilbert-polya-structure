#!/usr/bin/env python3
"""Byte-for-byte producer replay in a temporary directory."""
from __future__ import annotations

import hashlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c270_heisenberg_evidence.json"


def digest(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main() -> None:
    with tempfile.TemporaryDirectory() as td:
        out = Path(td) / "evidence.json"
        env = dict(os.environ)
        env["C270_EVIDENCE_OUT"] = str(out)
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        subprocess.check_call([sys.executable, "-B", str(ROOT / "code/c270_heisenberg_producer.py")], env=env)
        assert out.read_bytes() == EVIDENCE.read_bytes()
        print(f"C270 byte replay: PASS sha256={digest(out)} bytes={out.stat().st_size}")


if __name__ == "__main__":
    main()
