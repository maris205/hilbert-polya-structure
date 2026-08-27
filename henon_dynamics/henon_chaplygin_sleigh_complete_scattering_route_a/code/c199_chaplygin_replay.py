#!/usr/bin/env python3
"""Require byte-exact replay of the C199 evidence."""
import json, subprocess, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; EVIDENCE=ROOT/"results/c199_chaplygin_evidence.json"; PRODUCER=Path(__file__).with_name("c199_chaplygin_producer.py")
def main():
    with tempfile.TemporaryDirectory() as d:
        out=Path(d)/"evidence.json"; subprocess.run([sys.executable,str(PRODUCER),"--output",str(out)],check=True,capture_output=True)
        if out.read_bytes()!=EVIDENCE.read_bytes(): raise AssertionError("canonical replay mismatch")
    print(json.dumps({"status":"C199_REPLAY_PASS","bytes":EVIDENCE.stat().st_size},sort_keys=True))
if __name__=="__main__": main()
