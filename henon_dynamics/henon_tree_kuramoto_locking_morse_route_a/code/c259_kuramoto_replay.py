#!/usr/bin/env python3
"""Byte-for-byte producer replay for HCS-C259."""
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c259_kuramoto_producer.py"
EVIDENCE = ROOT / "results/c259_kuramoto_evidence.json"


def main():
    with tempfile.TemporaryDirectory() as directory:
        outputs = []
        for index in range(2):
            path = Path(directory) / f"evidence_{index}.json"
            env = dict(os.environ)
            env["PYTHONDONTWRITEBYTECODE"] = "1"
            subprocess.check_output([sys.executable, "-B", str(PRODUCER), "--output", str(path)], env=env, text=True)
            outputs.append(path)
        assert outputs[0].read_bytes() == outputs[1].read_bytes() == EVIDENCE.read_bytes()
        assert json.loads(outputs[0].read_text())["payload_sha256"] == json.loads(EVIDENCE.read_text())["payload_sha256"]
    print("C259 byte replay: PASS (two deterministic producer runs equal the released bytes)")


if __name__ == "__main__":
    main()
