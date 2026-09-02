#!/usr/bin/env python3
"""Two-run isolated byte replay for HCS-C316."""
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c316_elephant_producer.py"
EVIDENCE = ROOT / "results/c316_elephant_evidence.json"


def duplicate(items):
    out = {}
    for key, value in items:
        if key in out: raise ValueError("duplicate JSON key")
        out[key] = value
    return out


def main():
    if sys.flags.optimize:
        raise RuntimeError("C316 replay refuses optimized Python")
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    with tempfile.TemporaryDirectory(prefix="c316-replay-") as tmp:
        paths = [Path(tmp) / "a.json", Path(tmp) / "b.json"]
        for path in paths:
            out = subprocess.check_output([sys.executable, "-B", str(PRODUCER), "--output", str(path)], env=env, text=True)
            if "C316_PRODUCER_PASS" not in out: raise AssertionError("producer sentinel absent")
            json.loads(path.read_text(), object_pairs_hook=duplicate,
                       parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))
        if paths[0].read_bytes() != paths[1].read_bytes() or paths[0].read_bytes() != EVIDENCE.read_bytes():
            raise AssertionError("byte replay mismatch")
        print(f"C316 byte replay: PASS ({hashlib.sha256(paths[0].read_bytes()).hexdigest()})")


if __name__ == "__main__": main()
