#!/usr/bin/env python3
"""Clean-process byte replay for C232."""
from __future__ import annotations
import argparse, json, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = Path(__file__).with_name("c232_duffing_producer.py")
DEFAULT_EVIDENCE = ROOT / "results/c232_duffing_evidence.json"

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--evidence",type=Path,default=DEFAULT_EVIDENCE); target=ap.parse_args().evidence
    with tempfile.TemporaryDirectory() as td:
        out=Path(td)/"evidence.json"; subprocess.run([sys.executable,"-B",str(PRODUCER),"--output",str(out)],check=True,capture_output=True)
        if out.read_bytes()!=target.read_bytes(): raise AssertionError("canonical replay mismatch")
    obj=json.loads(target.read_text()); print(json.dumps({"status":"C232_REPLAY_PASS","bytes":target.stat().st_size,"payload_sha256":obj["payload_sha256"]},sort_keys=True))

if __name__=="__main__": main()
