#!/usr/bin/env python3
"""Byte-exact replay for the deterministic C185 evidence artifact."""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c185_brockett_evidence.json"
PRODUCER = ROOT / "code/c185_brockett_producer.py"
CHECKER = ROOT / "code/c185_brockett_checker.py"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence", nargs="?", type=Path, default=DEFAULT_EVIDENCE)
    args = parser.parse_args()
    with tempfile.TemporaryDirectory(prefix="c185-replay-") as tmp:
        replay = Path(tmp) / "evidence.json"
        subprocess.run([sys.executable, str(PRODUCER), "--output", str(replay)], check=True, capture_output=True, text=True)
        if replay.read_bytes() != args.evidence.read_bytes():
            raise AssertionError("replayed evidence differs byte-for-byte")
        checked = subprocess.run([sys.executable, str(CHECKER), str(replay)], check=True, capture_output=True, text=True)
        checker_status = json.loads(checked.stdout.strip().splitlines()[-1])
        if checker_status["status"] != "C185_CHECKER_PASS":
            raise AssertionError("checker did not pass on replayed bytes")
    print(json.dumps({
        "status": "C185_REPLAY_PASS",
        "bytes": args.evidence.stat().st_size,
        "file_sha256": digest(args.evidence),
        "checker_assertions": checker_status["assertions"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
