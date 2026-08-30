#!/usr/bin/env python3
"""Clean-process byte replay for the C251 producer."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c251_majority_producer.py"
EVIDENCE = ROOT / "results/c251_majority_evidence.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    with tempfile.TemporaryDirectory(prefix="c251-replay-") as td:
        output = Path(td) / "replayed.json"
        subprocess.run([sys.executable, "-B", str(PRODUCER), "--output", str(output)], check=True, env=env, stdout=subprocess.PIPE, text=True)
        assert output.read_bytes() == EVIDENCE.read_bytes()
        assert json.loads(output.read_text())["payload_sha256"] == json.loads(EVIDENCE.read_text())["payload_sha256"]
        print(f"C251 byte replay: PASS ({digest(EVIDENCE)})")


if __name__ == "__main__":
    main()
