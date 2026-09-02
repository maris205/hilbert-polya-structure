#!/usr/bin/env python3
"""Two-run isolated byte replay for HCS-C314."""
import hashlib, os, subprocess, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];PRODUCER=ROOT/"code/c314_angenent_producer.py";EVIDENCE=ROOT/"results/c314_angenent_evidence.json"
def main():
    if sys.flags.optimize:raise RuntimeError("C314 replay refuses optimized Python")
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1",TZ="UTC")
    with tempfile.TemporaryDirectory(prefix="c314-replay-") as tmp:
        paths=[Path(tmp)/"a.json",Path(tmp)/"b.json"]
        for path in paths:
            out=subprocess.check_output([sys.executable,"-B",str(PRODUCER),"--output",str(path)],env=env,text=True)
            if "C314_PRODUCER_PASS" not in out:raise AssertionError("sentinel")
        if paths[0].read_bytes()!=paths[1].read_bytes() or paths[0].read_bytes()!=EVIDENCE.read_bytes():raise AssertionError("byte replay")
        print(f"C314 byte replay: PASS ({hashlib.sha256(paths[0].read_bytes()).hexdigest()})")
if __name__=="__main__":main()
