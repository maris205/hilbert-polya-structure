#!/usr/bin/env python3
"""Hostile in-memory mutation audit against the independent C114 checker."""
from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path

from c114_jet_checker import validate

ROOT = Path(__file__).resolve().parents[1]
baseline = json.loads((ROOT / "results/c114_jet_evidence.json").read_text())
validate(baseline)


def set_matrix_cell(data: dict) -> None:
    data["operator"]["matrix"][3][1] = "2"


def swap_basis(data: dict) -> None:
    data["local_algebra"]["basis_order"][1:3] = reversed(data["local_algebra"]["basis_order"][1:3])


mutations = [
    ("scope", lambda d: d.update(scope_literal="ARITHMETIC_ALLOWED")),
    ("formula", lambda d: d["frozen_germ"].update(formula="F(u,v)=(u^2+u-v,u)")),
    ("dimension", lambda d: d["local_algebra"].update(dimension=14)),
    ("basis_order", swap_basis),
    ("matrix_cell", set_matrix_cell),
    ("matrix_hash", lambda d: d["operator"].update(matrix_sha256="0" * 64)),
    ("trace", lambda d: d["operator"].update(trace="8")),
    ("determinant", lambda d: d["operator"].update(determinant="1/2")),
    ("characteristic", lambda d: d["operator"]["characteristic_polynomial_coefficients_descending"].__setitem__(1, "0")),
    ("graded_block", lambda d: d["graded_blocks"]["4"].update(trace="1")),
    ("correction_count", lambda d: d["nonlinear_vs_linearized_control"].update(correction_nonzero_entry_count=0)),
    ("overclaim", lambda d: d["verdict"].update(A2="A2_GLOBAL_FREDHOLM_CERTIFIED")),
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
print("C114_MUTATION_PASS", rejected, "/", len(mutations))
