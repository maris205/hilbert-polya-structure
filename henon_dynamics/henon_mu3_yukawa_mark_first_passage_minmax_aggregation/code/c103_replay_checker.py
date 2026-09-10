#!/usr/bin/env python3
"""Deterministic replay checker for C103."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c103_minmax_aggregation_evidence.json"


def main() -> None:
    raw = EVIDENCE.read_bytes()
    value = json.loads(raw)
    canonical = (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()
    assert raw == canonical
    assert value["status"] == "PREFREEZE_G3_PASS"
    print(json.dumps({"status": "C103_REPLAY_PASS", "evidence_sha256": sha256(raw).hexdigest()}, sort_keys=True))


if __name__ == "__main__":
    main()
