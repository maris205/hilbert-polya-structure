#!/usr/bin/env python3
"""Canonical evidence replay for C116."""
import json
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "results/c116_lozi_evidence.json"
raw = PATH.read_bytes()
data = json.loads(raw)
assert data["schema"] == "hcs-c116-lozi-nonsmooth-route-a-v1"
assert data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
assert len(data["word_status_rows"]) == sum(2**n for n in range(1, 9)) == 510
assert len(data["primitive_rows"]) == 37
assert data["finite_cycle_atlas_operator"]["dimension"] == 240
canonical = (json.dumps(data, sort_keys=True, indent=2) + "\n").encode()
assert canonical == raw
print("C116_REPLAY_PASS", sha256(raw).hexdigest())
