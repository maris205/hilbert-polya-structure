#!/usr/bin/env python3
"""Fresh-path canonical byte replay for C265."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c265_hawkes_producer.py"
EVIDENCE = ROOT / "results/c265_hawkes_evidence.json"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="c265_replay_a_") as first, tempfile.TemporaryDirectory(prefix="c265_replay_b_") as second:
        paths = [Path(first) / "evidence.json", Path(second) / "evidence.json"]
        for path in paths:
            subprocess.run([sys.executable, "-B", str(PRODUCER), "--output", str(path)], check=True, capture_output=True, text=True)
        assert paths[0].read_bytes() == paths[1].read_bytes() == EVIDENCE.read_bytes()
        payloads = [json.loads(path.read_text())["payload_sha256"] for path in paths]
        assert payloads[0] == payloads[1] == json.loads(EVIDENCE.read_text())["payload_sha256"]
        print(f"C265 byte replay: PASS (fresh-fresh-release sha256={digest(EVIDENCE)})")


if __name__ == "__main__":
    main()
