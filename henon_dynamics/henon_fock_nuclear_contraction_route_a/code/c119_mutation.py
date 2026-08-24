#!/usr/bin/env python3
"""Hostile in-memory mutation audit for the independent C119 checker."""
from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path

from c119_fock_checker import validate

ROOT = Path(__file__).resolve().parents[1]
baseline = json.loads((ROOT / "results/c119_fock_evidence.json").read_text())
validate(baseline)

mutations = [
    ("scope", lambda d: d.update(scope_literal="ARITHMETIC_ALLOWED")),
    ("map", lambda d: d["frozen_map"].update(formula="Phi(x,y)=(x-y,x)")),
    ("matrix", lambda d: d["frozen_map"]["matrix"][0].__setitem__(0, "1")),
    ("determinant", lambda d: d["frozen_map"].update(determinant="1/4")),
    ("periodic", lambda d: d["frozen_map"].update(fixed_points=[["0", "0"], ["1", "1"]])),
    ("gram", lambda d: d["euclidean_contraction"]["A_transpose_A"][0].__setitem__(0, "1")),
    ("singular", lambda d: d["euclidean_contraction"]["singular_value_squares_descending"].__setitem__(0, "1")),
    ("trace", lambda d: d["trace_and_fredholm_data"]["trace_powers_n1_to_8"].update({"3": "1"})),
    ("coefficient", lambda d: d["trace_and_fredholm_data"]["taylor_coefficients_ascending_z0_to_z8"].__setitem__(4, "0")),
    ("zero_mult", lambda d: d["zero_divisor"]["prefix_k0_to_8"][6].update(multiplicity=1)),
    ("overclaim", lambda d: d["verdict"].update(A2="A2_ANALYTIC_DETERMINANT")),
    ("drop_nonclaim", lambda d: d["nonclaims"].pop()),
]
rejected = 0
for name, mutate in mutations:
    candidate = deepcopy(baseline)
    mutate(candidate)
    assert candidate != baseline, name
    try:
        validate(candidate)
    except (AssertionError, KeyError, ValueError, TypeError):
        rejected += 1
    else:
        raise AssertionError(f"mutation escaped checker: {name}")
assert rejected == len(mutations)
print("C119_MUTATION_PASS", rejected, "/", len(mutations))
