#!/usr/bin/env python3
"""Fresh-process byte replay for the HCS-C274 evidence payload."""
from __future__ import annotations

import hashlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c274_penning_evidence.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="c274_replay_") as tmp:
        out = Path(tmp) / "evidence.json"
        env = dict(os.environ)
        env["C274_EVIDENCE_OUT"] = str(out)
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        subprocess.check_call([sys.executable, "-B", str(ROOT / "code/c274_penning_producer.py")], env=env)
        assert out.read_bytes() == EVIDENCE.read_bytes()
        print(f"C274 byte replay: PASS sha256={digest(out)} bytes={out.stat().st_size}")


if __name__ == "__main__":
    main()
