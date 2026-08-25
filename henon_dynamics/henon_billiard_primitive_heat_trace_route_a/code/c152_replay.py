#!/usr/bin/env python3
"""Byte-for-byte producer replay for HCS-C152."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess,sys,tempfile
ROOT=Path(__file__).resolve().parents[1]; PRODUCER=ROOT/"code/c152_heat_producer.py"; EVIDENCE=ROOT/"results/c152_heat_evidence.json"
def main():
    with tempfile.TemporaryDirectory(prefix="c152-replay-") as temporary:
        output=Path(temporary)/"evidence.json"
        subprocess.run([sys.executable,str(PRODUCER),"--output",str(output)],check=True,capture_output=True,text=True)
        if output.read_bytes()!=EVIDENCE.read_bytes(): raise AssertionError("producer replay differs from frozen evidence")
    print(json.dumps({"status":"C152_REPLAY_PASS","sha256":sha256(EVIDENCE.read_bytes()).hexdigest()},sort_keys=True))
if __name__ == "__main__": main()
