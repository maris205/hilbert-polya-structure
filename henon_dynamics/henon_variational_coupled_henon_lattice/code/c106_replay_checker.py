#!/usr/bin/env python3
"""Canonical-byte replay check for the C106 evidence artifact."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c106_variational_lattice_evidence.json"


def main() -> None:
    raw = EVIDENCE.read_bytes()
    value = json.loads(raw)
    canonical = (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()
    assert raw == canonical
    assert value["status"] == "PREFREEZE_G3_PASS"
    assert value["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
    assert value["route_a_verdict"]["A1"] == "A1_WEAK"
    assert value["route_a_verdict"]["A2"] == "A2_FAIL"
    assert value["claims"]["fredholm_determinant_constructed"] is False
    print(json.dumps({"status": "C106_REPLAY_PASS", "evidence_sha256": sha256(raw).hexdigest()}, sort_keys=True))


if __name__ == "__main__":
    main()
