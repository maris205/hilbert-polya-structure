#!/usr/bin/env python3
"""Canonical byte replay for the C186 evidence."""
from hashlib import sha256
import json
from pathlib import Path

from c186_euler_top_producer import build_evidence, serialize

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c186_euler_top_evidence.json"


def main() -> None:
    expected = EVIDENCE.read_bytes()
    replayed = serialize(build_evidence())
    if expected != replayed:
        raise AssertionError("canonical evidence replay differs")
    print(json.dumps({"status": "C186_REPLAY_PASS", "bytes": len(expected), "evidence_sha256": sha256(expected).hexdigest()}, sort_keys=True))


if __name__ == "__main__":
    main()
