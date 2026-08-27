#!/usr/bin/env python3
"""Byte-for-byte replay test for the C192 producer."""
from hashlib import sha256
import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c192_hyperplane_evidence.json"
TEMP = ROOT / "results/.c192_replay.tmp.json"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    try:
        env = dict(os.environ)
        env["C192_OUTPUT"] = str(TEMP)
        subprocess.run([sys.executable, str(ROOT / "code/c192_hyperplane_producer.py")], check=True, env=env, stdout=subprocess.DEVNULL)
        assert TEMP.read_bytes() == EVIDENCE.read_bytes()
        print(f"C192_REPLAY_PASS bytes={EVIDENCE.stat().st_size} sha256={digest(EVIDENCE)}")
    finally:
        TEMP.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
