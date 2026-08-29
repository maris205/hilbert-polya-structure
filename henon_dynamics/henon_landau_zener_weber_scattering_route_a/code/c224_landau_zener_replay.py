#!/usr/bin/env python3
"""Clean-process canonical byte replay for C224."""
from __future__ import annotations
import argparse, json, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = Path(__file__).with_name("c224_landau_zener_producer.py")
EVIDENCE = ROOT / "results/c224_landau_zener_evidence.json"

def main() -> None:
    parser = argparse.ArgumentParser(); parser.add_argument("--evidence", type=Path, default=EVIDENCE)
    target = parser.parse_args().evidence
    with tempfile.TemporaryDirectory() as folder:
        replay = Path(folder) / "evidence.json"
        subprocess.run([sys.executable, "-B", str(PRODUCER), "--output", str(replay)], check=True, capture_output=True)
        if replay.read_bytes() != target.read_bytes(): raise AssertionError("canonical replay mismatch")
    data = json.loads(target.read_text())
    print(json.dumps({"status": "C224_REPLAY_PASS", "bytes": target.stat().st_size, "payload_sha256": data["payload_sha256"]}, sort_keys=True))

if __name__ == "__main__": main()
