#!/usr/bin/env python3
"""Canonical byte replay for HCS-C166."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    root = Path(__file__).resolve().parents[1]
    released = root / "results/c166_pascal_tower_evidence.json"
    with tempfile.TemporaryDirectory(prefix="c166-replay-") as temp:
        first = Path(temp) / "first.json"
        second = Path(temp) / "second.json"
        for output in (first, second):
            subprocess.run([sys.executable, str(root / "code/c166_pascal_tower_producer.py"),
                            "--output", str(output)], check=True, capture_output=True, text=True)
        assert first.read_bytes() == second.read_bytes() == released.read_bytes()
        subprocess.run([sys.executable, str(root / "code/c166_pascal_tower_checker.py"),
                        "--evidence", str(first)], check=True, capture_output=True, text=True)
        value = digest(first)
    print(json.dumps({"status": "C166_REPLAY_PASS", "evidence_sha256": value}, sort_keys=True))


if __name__ == "__main__":
    main()
