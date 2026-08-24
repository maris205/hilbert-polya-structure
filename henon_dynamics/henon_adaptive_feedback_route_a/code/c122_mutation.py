#!/usr/bin/env python3
"""Hostile mutations that the independent C122 validator must reject."""
from copy import deepcopy
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))
from c122_adaptive_checker import CheckFailure, validate  # noqa: E402

base = json.loads((ROOT / "results" / "c122_adaptive_evidence.json").read_text())


def change(path, value):
    def mutate(data):
        node = data
        for key in path[:-1]:
            node = node[key]
        node[path[-1]] = value
    return mutate


mutations = [
    change(["schema_id"], "wrong"),
    change(["scope_literal"], "ROUTE_B"),
    change(["source_model", "parameters", "feedback_gain"], "5/2"),
    change(["structural_checks", "constant_jacobian_determinant"], "1"),
    change(["certified_orbit_ledger", "fixed_rows", 0, "state", 0], "0"),
    change(["certified_orbit_ledger", "period_two_rows", 0, "states", 0, 0], "2"),
    change(["certified_orbit_ledger", "period_two_rows", 0, "monodromy_trace"], "0"),
    change(["certified_orbit_ledger", "period_two_rows", 0, "monodromy_determinant"], "1/2"),
    change(["certified_orbit_ledger", "period_two_rows", 0, "det_I_minus_z_monodromy", 2], "2"),
    change(["feedback_controls", "gain_zero_parameter_residual_against_target"], "0"),
    change(["structural_checks", "degree_prefix", 5, "coordinate_total_degrees", 0], 63),
    change(["route_a_verdict", "A1"], "A1_PASS_CERTIFIED"),
    change(["route_a_verdict", "A2"], "A2_ANALYTIC_DETERMINANT"),
    change(["route_a_verdict", "A3"], "A3_PARTIAL_ANALYTIC_STRUCTURE"),
    change(["route_a_verdict", "A4"], "A4_NATURAL_QUANTIZATION"),
    change(["claims", "route_b_authorized"], True),
]

rejected = 0
for mutate in mutations:
    candidate = deepcopy(base)
    mutate(candidate)
    try:
        validate(candidate)
    except (CheckFailure, KeyError, TypeError, ValueError, IndexError):
        rejected += 1
if rejected != len(mutations):
    raise SystemExit(f"C122_MUTATION_FAIL {rejected}/{len(mutations)}")
print(f"C122_MUTATION_PASS {rejected}/{len(mutations)}")
