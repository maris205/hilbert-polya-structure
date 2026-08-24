#!/usr/bin/env python3
"""Canonical byte replay for C114 evidence."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "results/c114_jet_evidence.json"
raw = path.read_bytes()
data = json.loads(raw)
canonical = (json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode()
assert raw == canonical
assert data["schema"] == "hcs-c114-local-jet-koopman-v1"
assert data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
assert data["local_algebra"]["dimension"] == 15
assert len(data["operator"]["matrix"]) == 15
assert all(len(row) == 15 for row in data["operator"]["matrix"])
print("C114_REPLAY_PASS", sha256(raw).hexdigest())
