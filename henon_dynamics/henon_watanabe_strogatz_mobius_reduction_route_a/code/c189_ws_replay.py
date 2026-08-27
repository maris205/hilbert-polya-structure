#!/usr/bin/env python3
"""Canonical byte replay for the C189 evidence payload."""
from hashlib import sha256
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
EVIDENCE = ROOT / "results/c189_ws_evidence.json"
sys.path.insert(0, str(HERE))

import c189_ws_producer as producer  # noqa: E402


def main() -> None:
    expected = EVIDENCE.read_bytes()
    replayed = producer.serialize(producer.build_evidence())
    if replayed != expected:
        raise AssertionError({
            "expected_sha256": sha256(expected).hexdigest(),
            "replayed_sha256": sha256(replayed).hexdigest(),
        })
    print(json.dumps({
        "status": "C189_REPLAY_PASS",
        "bytes": len(replayed),
        "evidence_sha256": sha256(replayed).hexdigest(),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
