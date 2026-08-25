#!/usr/bin/env python3
"""Canonical byte replay for HCS-C167 evidence."""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path,
                        default=root / "results/c167_rectangle_evidence.json")
    args = parser.parse_args()
    with tempfile.TemporaryDirectory(prefix="c167-replay-") as temp:
        replay = Path(temp) / "evidence.json"
        process = subprocess.run(
            [sys.executable, str(root / "code/c167_rectangle_producer.py"),
             "--output", str(replay)],
            check=True, capture_output=True, text=True,
        )
        assert replay.read_bytes() == args.evidence.read_bytes()
        assert digest(replay) == digest(args.evidence)
    print(json.dumps({
        "status": "C167_REPLAY_PASS",
        "evidence_sha256": digest(args.evidence),
        "producer_receipt": json.loads(process.stdout),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
