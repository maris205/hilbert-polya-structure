#!/usr/bin/env python3
"""Byte-exact replay of HCS-C207 evidence."""
import subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; EVIDENCE=ROOT/"results/c207_barenblatt_evidence.json"; PRODUCER=Path(__file__).with_name("c207_barenblatt_producer.py")
with tempfile.TemporaryDirectory() as d:
    p=Path(d)/"evidence.json"; subprocess.run([sys.executable,str(PRODUCER),"--output",str(p)],check=True,capture_output=True)
    if p.read_bytes()!=EVIDENCE.read_bytes(): raise AssertionError("C207 replay mismatch")
print('{"status":"C207_REPLAY_PASS","byte_exact":true}')
