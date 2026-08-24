#!/usr/bin/env python3
"""Hostile in-memory mutation audit against the independent C125 checker."""
from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path

from c125_anosov_checker import validate


ROOT = Path(__file__).resolve().parents[1]
baseline = json.loads((ROOT / "results/c125_anosov_evidence.json").read_text())
validate(baseline)


def corrupt_wrap(candidate: dict) -> None:
    candidate["negative_controls"]["wraparound_fourier_aliasing"]["rows"][1]["wraparound_traces"][0] += 1


def corrupt_basis(candidate: dict) -> None:
    candidate["koopman_obstruction"]["orthonormal_test_sources_and_images"][4]["image_A_transpose_k"] = [10, 4]


mutations = [
    ("scope", lambda d: d.update(scope_literal="ARITHMETIC_ALLOWED")),
    ("matrix", lambda d: d["frozen_system"].update(matrix_A=[[3, 1], [1, 1]])),
    ("fixed_count", lambda d: d["all_order_fixed_point_theorem"]["rows"][5].update(fixed_point_count=319)),
    ("primitive_count", lambda d: d["all_order_fixed_point_theorem"]["rows"][7].update(primitive_orbit_count=271)),
    ("zeta_formula", lambda d: d["artin_mazur_zeta"].update(exact_rational_function="1/(1-3*z+z^2)")),
    ("zeta_coefficient", lambda d: d["artin_mazur_zeta"]["series_coefficients_z_0_to_12"].__setitem__(8, 988)),
    ("basis_action", corrupt_basis),
    ("unitarity", lambda d: d["koopman_obstruction"].update(unitary=False)),
    ("compactness", lambda d: d["koopman_obstruction"].update(noncompact=False)),
    ("trace_class", lambda d: d["koopman_obstruction"].update(trace_class=True)),
    ("ordinary_determinant", lambda d: d["koopman_obstruction"].update(ordinary_trace_class_fredholm_determinant_defined=True)),
    ("parabolic_determinant", lambda d: d["negative_controls"]["parabolic_shear"].update(det_B_power_minus_I=1)),
    ("parabolic_finite", lambda d: d["negative_controls"]["parabolic_shear"].update(standard_finite_fixed_point_count_available=True)),
    ("signed_as_count", lambda d: d["negative_controls"]["drop_absolute_value"].update(valid_as_fixed_point_counts=True)),
    ("wrap_trace", corrupt_wrap),
    ("cutoff_claim", lambda d: d["negative_controls"]["wraparound_fourier_aliasing"].update(cutoff_independent=True)),
    ("A1_overclaim", lambda d: d["route_a_verdict"].update(A1="A1_PASS_ANALYTIC")),
    ("A2_overclaim", lambda d: d["route_a_verdict"].update(A2="A2_ANALYTIC_DETERMINANT")),
    ("A3_softening", lambda d: d["route_a_verdict"].update(A3="A3_NOT_ADDRESSED")),
    ("A4_overclaim", lambda d: d["route_a_verdict"].update(A4="A4_NATURAL_QUANTIZATION")),
    ("route_b", lambda d: d["route_a_verdict"].update(route_b_invocation_allowed=True)),
    ("drop_progress", lambda d: d.pop("progress_over_prior_gate")),
    ("drop_nonclaim", lambda d: d["nonclaims"].pop()),
]

rejected = 0
for name, mutate in mutations:
    candidate = deepcopy(baseline)
    mutate(candidate)
    assert candidate != baseline, name
    try:
        validate(candidate)
    except (AssertionError, KeyError, TypeError, ValueError):
        rejected += 1
    else:
        raise AssertionError(f"mutation escaped checker: {name}")

assert rejected == len(mutations)
print("C125_MUTATION_PASS", rejected, "/", len(mutations))
