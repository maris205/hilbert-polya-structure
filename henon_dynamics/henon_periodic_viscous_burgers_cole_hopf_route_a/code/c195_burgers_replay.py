#!/usr/bin/env python3
"""Byte-for-byte deterministic replay of the C195 evidence artifact."""
from __future__ import annotations

from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c195_burgers_producer.py"
EVIDENCE = ROOT / "results/c195_burgers_evidence.json"


def load_producer():
    spec = importlib.util.spec_from_file_location("c195_replay_producer", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load producer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    producer = load_producer()
    generated = producer.serialize(producer.build_evidence())
    stored = EVIDENCE.read_bytes()
    with tempfile.TemporaryDirectory(prefix="c195-replay-") as temp:
        replay = Path(temp) / "evidence.json"
        replay.write_bytes(generated)
        if replay.read_bytes() != stored:
            raise AssertionError("C195 replay bytes differ")
    print(json.dumps({
        "status": "C195_REPLAY_PASS",
        "bytes": len(stored),
        "evidence_sha256": sha256(stored).hexdigest(),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
