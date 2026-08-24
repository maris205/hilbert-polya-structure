#!/usr/bin/env python3
"""Hostile evidence mutations that the independent C126 checker must reject."""
from __future__ import annotations

import copy
import json
from pathlib import Path

from c126_chebyshev_skew_checker import validate

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "results/c126_chebyshev_skew_evidence.json").read_text())


def changed(edit):
    value = copy.deepcopy(DATA)
    edit(value)
    return value


CASES = [
    changed(lambda x: x.__setitem__("scope_literal", "BROKEN")),
    changed(lambda x: x["source_model"].__setitem__("fiber_multiplier", "1")),
    changed(lambda x: x["source_model"].__setitem__("clock", "two applications of F")),
    changed(lambda x: x["all_period_theorem"]["finite_symbolic_replay"][2].__setitem__("degree", 26)),
    changed(lambda x: x["all_period_theorem"].__setitem__("base_fixed_root_count", "3^n roots with multiplicity")),
    changed(lambda x: x["all_period_theorem"].__setitem__("root_family_intersection", "empty")),
    changed(lambda x: x["primitive_orbits"]["prefix_n1_to_n12"][5].__setitem__("primitive_orbits", 115)),
    changed(lambda x: x["primitive_orbits"]["prefix_n1_to_n12"][7].__setitem__("negative_unstable_orientation_primitive_orbits", 409)),
    changed(lambda x: x["zeta"].__setitem__("closed_form", "zeta_F(z)=1/(1-2*z)")),
    changed(lambda x: x["stability"]["prefix_n1_to_n12"][3].__setitem__("negative_interior_count", 39)),
    changed(lambda x: x["stability"].__setitem__("orientation_counts", "positive=negative")),
    changed(lambda x: x["negative_controls"]["non_chebyshev_cubic"].__setitem__("distinct_base_fix_g2", 9)),
    changed(lambda x: x["negative_controls"]["unit_fiber_multiplier"].__setitem__("failure", "unique closure persists")),
    changed(lambda x: x["progress_over_prior_gate"].__setitem__("new_result", "finite period prefix")),
    changed(lambda x: x["route_a_evaluator"]["canonical_tuple"].__setitem__(0, "A1_PASS_ANALYTIC")),
    changed(lambda x: x["route_a_evaluator"]["canonical_tuple"].__setitem__(1, "A2_ANALYTIC_DETERMINANT")),
    changed(lambda x: x["route_a_evaluator"].__setitem__("route_b_invocation_allowed", True)),
    changed(lambda x: x["nonclaims"].__setitem__(0, "target divisor matched")),
]

rejected = 0
missed = []
for index, case in enumerate(CASES, 1):
    try:
        validate(case)
    except (AssertionError, KeyError, TypeError, ValueError):
        rejected += 1
    else:
        missed.append(index)

assert not missed, f"checker accepted hostile cases {missed}"
print(f"C126_MUTATION_PASS {rejected}/{len(CASES)}")
