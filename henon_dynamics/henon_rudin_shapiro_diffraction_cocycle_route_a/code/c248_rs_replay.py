#!/usr/bin/env python3
"""Clean byte replay of the C248 producer."""
from __future__ import annotations

from hashlib import sha256
import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c248_rs_evidence.json"
PRODUCER = ROOT / "code/c248_rs_producer.py"


def main() -> None:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    with tempfile.TemporaryDirectory(prefix="c248-rs-replay-") as td:
        out = Path(td) / "replayed.json"
        subprocess.check_call([sys.executable, "-B", str(PRODUCER), "--output", str(out)], env=env, stdout=subprocess.DEVNULL)
        original = EVIDENCE.read_bytes()
        replayed = out.read_bytes()
        assert original == replayed, "producer replay bytes differ"
    print(f"C248 byte replay: PASS sha256={sha256(original).hexdigest()}")


if __name__ == "__main__":
    main()
