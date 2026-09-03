#!/usr/bin/env python3
"""Two-isolated-directory byte replay for HCS-C350."""
import hashlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT=Path(__file__).resolve().parents[1]
PRODUCER=ROOT/"code/c350_schnakenberg_producer.py"
EVALUATION=ROOT/"evaluations/route_a/HCS-C350/2026-09-03.yaml"
EVIDENCE=ROOT/"results/c350_schnakenberg_evidence.json"


def run(directory):
    output=Path(directory)/"evidence.json"
    result=subprocess.run([sys.executable,"-B",str(PRODUCER),"--output",str(output),
        "--evaluation",str(EVALUATION)],check=True,stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,text=True,
        env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1",TZ="UTC"))
    if "C350_PRODUCER_PASS" not in result.stdout:
        raise AssertionError("producer sentinel")
    return output.read_bytes()


def main():
    if sys.flags.optimize:
        raise RuntimeError("C350 replay refuses optimized Python")
    with tempfile.TemporaryDirectory(prefix="c350-replay-a-") as a, tempfile.TemporaryDirectory(prefix="c350-replay-b-") as b:
        one,two=run(a),run(b)
    expected=EVIDENCE.read_bytes()
    if one!=two or one!=expected:
        raise AssertionError("isolated replay mismatch")
    print(f"C350 byte replay: PASS 2 copies ({hashlib.sha256(one).hexdigest()})")


if __name__=="__main__":
    main()
