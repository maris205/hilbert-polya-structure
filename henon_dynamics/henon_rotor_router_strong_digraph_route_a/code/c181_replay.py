#!/usr/bin/env python3
"""Byte-for-byte deterministic replay for C181 evidence."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c181_rotor_router_producer.py"
EVIDENCE = ROOT / "results/c181_rotor_router_evidence.json"


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="c181-replay-") as tmp:
        out = Path(tmp) / "evidence.json"
        subprocess.run([sys.executable, str(PRODUCER), "--output", str(out)], check=True, capture_output=True, text=True)
        expected, observed = EVIDENCE.read_bytes(), out.read_bytes()
        assert expected == observed, "producer replay is not byte-identical"
    print(json.dumps({"status": "C181_REPLAY_PASS", "bytes": len(expected), "sha256": sha256(expected).hexdigest()}, sort_keys=True))


if __name__ == "__main__":
    main()
