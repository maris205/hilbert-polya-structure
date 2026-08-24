#!/usr/bin/env python3
"""Replay the canonical C121 evidence bytes and recursive degree prefix."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "results/c121_projective_evidence.json"
raw = PATH.read_bytes()
data = json.loads(raw)
canonical = (json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode()
assert raw == canonical
assert data["schema"] == "hcs-c121-projective-algebraic-stability-v1"
assert data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
assert data["degree_growth"]["exact_projective_degree_sequence_n_1_to_8"] == [2, 4, 8, 16, 32, 64, 128, 256]
assert data["birational_certificate"]["algebraically_stable_on_P2"] is True
assert data["primitive_real_two_cycle"]["monodromy"] == [[-1, 4], [0, -1]]
assert data["route_a_verdict"]["canonical_tuple"] == ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"]
assert data["route_a_verdict"]["overall"] == "ROUTE_A_EXPLORATORY"
print("C121_REPLAY_PASS", sha256(raw).hexdigest(), "n=1..8")
