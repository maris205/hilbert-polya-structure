#!/usr/bin/env python3
"""Byte-level clean replay for the C241 Lüroth certificate."""
from __future__ import annotations

from hashlib import sha256
import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c241_luroth_evidence.json"
PRODUCER = ROOT / "code/c241_luroth_producer.py"


def main() -> None:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["SOURCE_DATE_EPOCH"] = "1788048000"
    with tempfile.TemporaryDirectory(prefix="c241-luroth-replay-") as td:
        out = Path(td) / "replayed.json"
        subprocess.check_call(
            [sys.executable, "-B", str(PRODUCER), "--output", str(out)],
            env=env,
            stdout=subprocess.DEVNULL,
        )
        original = EVIDENCE.read_bytes()
        replayed = out.read_bytes()
        assert original == replayed, "producer replay bytes differ"
    print(f"C241 byte replay: PASS sha256={sha256(original).hexdigest()}")


if __name__ == "__main__":
    main()
