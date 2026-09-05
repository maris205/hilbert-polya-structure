#!/usr/bin/env python3
"""Replay canonical producer from two unrelated working directories."""
if not __debug__: raise RuntimeError("c396 replay refuses optimized Python")
import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile
ROOT=Path(__file__).resolve().parents[1]
def run():
    blobs=[]
    for prefix in ("c396-replay-a-","c396-replay-b-"):
      with tempfile.TemporaryDirectory(prefix=prefix) as directory:
        out=Path(directory)/"receipt.json"
        subprocess.run([sys.executable,"-B",str(ROOT/"code/c396_producer.py"),"--output",str(out)],cwd=directory,check=True,capture_output=True)
        subprocess.run([sys.executable,"-B",str(ROOT/"code/c396_checker.py"),str(out)],cwd=directory,check=True,capture_output=True)
        blobs.append(out.read_bytes())
    assert blobs[0]==blobs[1]==(ROOT/"results/c396_evidence.json").read_bytes()
    print("C396 two-directory replay PASS",hashlib.sha256(blobs[0]).hexdigest())
if __name__=="__main__":run()
