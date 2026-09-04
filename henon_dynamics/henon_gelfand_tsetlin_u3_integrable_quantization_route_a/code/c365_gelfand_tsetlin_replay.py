#!/usr/bin/env python3
"""Two-isolated-directory byte replay for HCS-C365."""
from __future__ import annotations
if not __debug__: raise RuntimeError("c365 replay refuses optimized Python")
import argparse, subprocess, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];PROD=ROOT/"code/c365_gelfand_tsetlin_producer.py";EVID=ROOT/"results/c365_gelfand_tsetlin_evidence.json"
def main():
    argparse.ArgumentParser().parse_args();blobs=[]
    for _ in range(2):
        with tempfile.TemporaryDirectory(prefix="c365-replay-") as td:
            out=Path(td)/"evidence.json";p=subprocess.run([sys.executable,str(PROD),"--output",str(out)],capture_output=True,text=True)
            assert p.returncode==0,p.stderr;blobs.append(out.read_bytes())
    assert blobs[0]==blobs[1]==EVID.read_bytes()
    print(f"C365 replay PASS: bytes={len(blobs[0])} isolated_runs=2")
if __name__=="__main__": main()
