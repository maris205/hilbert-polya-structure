#!/usr/bin/env python3
"""Hostile in-memory mutation audit against the independent C121 checker."""
from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path

from c121_projective_checker import validate


ROOT = Path(__file__).resolve().parents[1]
baseline = json.loads((ROOT / "results/c121_projective_evidence.json").read_text())
validate(baseline)


def alter_cycle(candidate: dict) -> None:
    candidate["primitive_real_two_cycle"]["q"] = [-1, 0]


def alter_dag(candidate: dict) -> None:
    candidate["degree_growth"]["rows"][3]["recurrence_dag_sha256"] = "0" * 64


mutations = [
    ("scope", lambda d: d.update(scope_literal="ARITHMETIC_ALLOWED")),
    ("parameter", lambda d: d["frozen_map"].update(parameter_c=-3)),
    ("affine_formula", lambda d: d["frozen_map"].update(affine_formula="H(x,y)=(x^2-3-y,x)")),
    ("inverse", lambda d: d["frozen_map"].update(inverse_formula="H^{-1}(x,y)=(y,y^2-3-x)")),
    ("I_plus", lambda d: d["birational_certificate"].update(forward_indeterminacy_I_plus=[1, 0, 0])),
    ("stability", lambda d: d["birational_certificate"].update(algebraically_stable_on_P2=False)),
    ("degree_8", lambda d: d["degree_growth"]["rows"][7].update(projective_degree=255)),
    ("dag_hash", alter_dag),
    ("cycle", alter_cycle),
    ("monodromy", lambda d: d["primitive_real_two_cycle"]["monodromy"][0].__setitem__(1, 3)),
    ("control", lambda d: d["parameter_controls"][0].update(frozen_two_cycle_preserved=True)),
    ("entropy_overclaim", lambda d: d["degree_growth"].update(entropy_claimed=True)),
    ("A1_overclaim", lambda d: d["route_a_verdict"].update(A1="A1_PASS_CERTIFIED")),
    ("A2_overclaim", lambda d: d["route_a_verdict"].update(A2="A2_CERTIFIED_PREFIX")),
    ("A3_softening", lambda d: d["route_a_verdict"].update(A3="A3_NOT_ADDRESSED")),
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
print("C121_MUTATION_PASS", rejected, "/", len(mutations))
