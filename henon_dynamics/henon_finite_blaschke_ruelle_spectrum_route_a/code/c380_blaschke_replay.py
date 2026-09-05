#!/usr/bin/env python3
"""Run the producer from two unrelated working directories."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c380 replay refuses optimized Python")
import argparse
import hashlib
import subprocess
import sys
import tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
    argparse.ArgumentParser().parse_args();blobs=[]
    for i in range(2):
        with tempfile.TemporaryDirectory(prefix=f"c380-isolated-{i}-") as directory:
            out=Path(directory)/"evidence.json"
            subprocess.run([sys.executable,"-B",str(ROOT/"code/c380_blaschke_producer.py"),"--output",str(out)],cwd=directory,check=True,capture_output=True)
            blobs.append(out.read_bytes())
    assert blobs[0]==blobs[1]==(ROOT/"results/c380_blaschke_evidence.json").read_bytes()
    print("C380 two-directory replay PASS: sha256="+hashlib.sha256(blobs[0]).hexdigest())
if __name__=="__main__":main()
