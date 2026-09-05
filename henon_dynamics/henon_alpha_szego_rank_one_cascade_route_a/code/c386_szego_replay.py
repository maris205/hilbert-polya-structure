#!/usr/bin/env python3
"""Two isolated directory producer runs with copied locked YAML."""
if not __debug__:raise RuntimeError("c386 replay refuses optimized Python")
import argparse
import hashlib
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
ROOT=Path(__file__).resolve().parents[1]
def main():
    argparse.ArgumentParser().parse_args();blobs=[]
    for index in range(2):
        with tempfile.TemporaryDirectory(prefix=f"c386-replay-{index}-") as directory:
            p=Path(directory);(p/"code").mkdir();(p/"evaluations/route_a/HCS-C386").mkdir(parents=True)
            shutil.copy2(ROOT/"code/c386_szego_producer.py",p/"code/c386_szego_producer.py")
            shutil.copy2(ROOT/"evaluations/route_a/HCS-C386/2026-09-05.yaml",p/"evaluations/route_a/HCS-C386/2026-09-05.yaml")
            subprocess.run([sys.executable,"-B",str(p/"code/c386_szego_producer.py")],check=True,capture_output=True)
            blobs.append((p/"results/c386_szego_evidence.json").read_bytes())
    assert blobs[0]==blobs[1]==(ROOT/"results/c386_szego_evidence.json").read_bytes()
    print("C386 isolated replay PASS: directories=2 sha256="+hashlib.sha256(blobs[0]).hexdigest())
if __name__=="__main__":main()
