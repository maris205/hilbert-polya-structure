#!/usr/bin/env python3
"""Two-isolated-directory byte replay for C361."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c361 replay refuses optimized Python")
import hashlib, subprocess, sys, tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PROD=ROOT/"code/c361_markov_entropy_producer.py";CHECK=ROOT/"code/c361_markov_entropy_checker.py"
EVAL=ROOT/"evaluations/route_a/HCS-C361/2026-09-04.yaml"; STORED=ROOT/"results/c361_markov_entropy_evidence.json"
blobs=[]
for _ in range(2):
    with tempfile.TemporaryDirectory(prefix="c361-replay-") as td:
        out=Path(td)/"evidence.json"
        subprocess.run([sys.executable,str(PROD),"--output",str(out),"--evaluation",str(EVAL)],check=True,capture_output=True,text=True)
        subprocess.run([sys.executable,str(CHECK),"--input",str(out),"--evaluation",str(EVAL)],check=True,capture_output=True,text=True)
        blobs.append(out.read_bytes())
assert blobs[0]==blobs[1]==STORED.read_bytes()
print(f"C361 replay PASS: isolated_runs=2 bytes={len(blobs[0])} sha256={hashlib.sha256(blobs[0]).hexdigest()}")
