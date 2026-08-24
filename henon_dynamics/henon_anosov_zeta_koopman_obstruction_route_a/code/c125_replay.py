#!/usr/bin/env python3
"""Replay canonical C125 evidence bytes and headline sequences."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "results/c125_anosov_evidence.json"
raw = PATH.read_bytes()
data = json.loads(raw)
canonical = (json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode()
assert raw == canonical
assert data["schema"] == "hcs-c125-anosov-zeta-koopman-obstruction-v1"
assert data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
assert data["all_order_fixed_point_theorem"]["fixed_point_counts_n_1_to_12"] == [
    1, 5, 16, 45, 121, 320, 841, 2205, 5776, 15125, 39601, 103680
]
assert data["all_order_fixed_point_theorem"]["primitive_orbit_counts_n_1_to_12"] == [
    1, 2, 5, 10, 24, 50, 120, 270, 640, 1500, 3600, 8610
]
assert data["artin_mazur_zeta"]["exact_rational_function"] == "(1-z)^2/(1-3*z+z^2)"
assert data["koopman_obstruction"]["unitary"] is True
assert data["koopman_obstruction"]["noncompact"] is True
assert data["route_a_verdict"]["canonical_tuple"] == ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
assert data["route_a_verdict"]["route_b_invocation_allowed"] is False
print("C125_REPLAY_PASS", sha256(raw).hexdigest(), "n=1..12")
