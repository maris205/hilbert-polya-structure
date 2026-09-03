#!/usr/bin/env python3
"""Byte-for-byte evidence replay for HCS-C320."""
import subprocess,sys,tempfile
from pathlib import Path
if sys.flags.optimize:raise RuntimeError("C320 replay refuses optimized Python")
root=Path(__file__).resolve().parents[1]
with tempfile.TemporaryDirectory(prefix="c320-replay-") as tmp:
    out=Path(tmp)/"evidence.json"
    p=subprocess.run([sys.executable,"-B",str(root/"code/c320_darboux_halphen_producer.py"),"--output",str(out)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    if p.returncode or out.read_bytes()!=(root/"results/c320_darboux_halphen_evidence.json").read_bytes():raise AssertionError(p.stdout)
print("C320 byte replay: PASS")
