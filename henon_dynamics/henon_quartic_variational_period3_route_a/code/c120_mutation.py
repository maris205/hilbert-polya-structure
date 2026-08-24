#!/usr/bin/env python3
"""Hostile mutations that the independent C120 checker must reject."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import tempfile

from c120_variational_period3_checker import validate

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "results/c120_variational_period3_evidence.json").read_text())


def mutated(change):
    value = copy.deepcopy(DATA)
    change(value)
    return value


CASES = [
    mutated(lambda x: x.__setitem__("scope_literal", "BROKEN")),
    mutated(lambda x: x["source_model"].__setitem__("parameter_alpha", "3")),
    mutated(lambda x: x["structural_checks"].__setitem__("jacobian_determinant_symbolic", "-1")),
    mutated(lambda x: x["fixed_point_ledger"].__setitem__("count", 4)),
    mutated(lambda x: x["fixed_point_ledger"]["rows"][1]["state"].__setitem__(0, "1")),
    mutated(lambda x: x["primitive_period_three"].__setitem__("primitive_period", 1)),
    mutated(lambda x: x["primitive_period_three"]["monodromy"][1].__setitem__(0, "3")),
    mutated(lambda x: x["primitive_period_three"]["det_I_minus_z_monodromy"].__setitem__(1, "-2")),
    mutated(lambda x: x["discrete_action_certificate"].__setitem__("action", "-1/2")),
    mutated(lambda x: x["discrete_action_certificate"].__setitem__("morse_index", 1)),
    mutated(lambda x: x["controls"]["nearby_parameter"].__setitem__("frozen_cycle_survives", True)),
    mutated(lambda x: x["controls"]["deleted_cubic_term"]["residual_actual_minus_target"].__setitem__(0, "0")),
    mutated(lambda x: x["controls"]["noncyclic_word"].__setitem__("all_transitions_close", True)),
    mutated(lambda x: x["route_a_evaluator_audit"]["a1"].__setitem__("target_prime_correspondence", True)),
    mutated(lambda x: x["claims"].__setitem__("source_owned_dynamical_zeta_or_fredholm_object", True)),
    mutated(lambda x: x["claims"].__setitem__("target_divisor_match", True)),
    mutated(lambda x: x["route_a_verdict"].__setitem__("A1", "A1_PASS_CERTIFIED")),
    mutated(lambda x: x["route_a_verdict"].__setitem__("A2", "A2_CERTIFIED_GLOBAL")),
    mutated(lambda x: x["route_a_verdict"].__setitem__("A3", "A3_PARTIAL_ANALYTIC_STRUCTURE")),
    mutated(lambda x: x["route_a_verdict"].__setitem__("A4", "A4_ROUTE_B_READY")),
    mutated(lambda x: x["claims"].__setitem__("route_b_authorized", True)),
]

rejected = 0
for data in CASES:
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as handle:
        json.dump(data, handle, sort_keys=True, separators=(",", ":"))
        handle.write("\n")
        path = Path(handle.name)
    try:
        validate(path)
    except (AssertionError, KeyError, TypeError, ValueError):
        rejected += 1
    finally:
        path.unlink()

assert rejected == len(CASES)
print(f"C120_MUTATION_PASS {rejected}/{len(CASES)}")
