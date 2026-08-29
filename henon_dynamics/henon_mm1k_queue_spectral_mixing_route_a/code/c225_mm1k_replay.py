#!/usr/bin/env python3
"""Clean-process byte replay of the canonical C225 producer."""
from __future__ import annotations
import argparse, json, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = Path(__file__).with_name("c225_mm1k_producer.py")
DEFAULT_EVIDENCE = ROOT / "results/c225_mm1k_evidence.json"

def main() -> None:
    p = argparse.ArgumentParser(); p.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE); target=p.parse_args().evidence
    with tempfile.TemporaryDirectory() as d:
        out=Path(d)/"evidence.json"
        subprocess.run([sys.executable,"-B",str(PRODUCER),"--output",str(out)],check=True,capture_output=True)
        if out.read_bytes()!=target.read_bytes(): raise AssertionError("canonical replay mismatch")
    obj=json.loads(target.read_text())
    print(json.dumps({"status":"C225_REPLAY_PASS","bytes":target.stat().st_size,"payload_sha256":obj["payload_sha256"]},sort_keys=True))

if __name__ == "__main__": main()
