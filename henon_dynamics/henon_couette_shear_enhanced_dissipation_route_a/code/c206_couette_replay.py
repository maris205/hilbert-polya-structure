#!/usr/bin/env python3
"""Byte-exact replay of the HCS-C206 evidence."""
import subprocess, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; EVIDENCE=ROOT/"results/c206_couette_evidence.json"; PRODUCER=Path(__file__).with_name("c206_couette_producer.py")
with tempfile.TemporaryDirectory() as d:
    p=Path(d)/"evidence.json"
    subprocess.run([sys.executable,str(PRODUCER),"--output",str(p)],check=True,capture_output=True)
    if p.read_bytes()!=EVIDENCE.read_bytes(): raise AssertionError("C206 replay mismatch")
print('{"status":"C206_REPLAY_PASS","byte_exact":true}')
