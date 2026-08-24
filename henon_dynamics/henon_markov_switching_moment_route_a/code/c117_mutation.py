#!/usr/bin/env python3
"""Hostile semantic mutations for the independent C117 checker."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import tempfile

from c117_markov_checker import validate

ROOT = Path(__file__).resolve().parents[1]
D = json.loads((ROOT / "results/c117_markov_evidence.json").read_text())


def cases():
    def one(fn):
        x = copy.deepcopy(D); fn(x); return x
    return [
        one(lambda x: x.__setitem__("scope_literal", "BROKEN")),
        one(lambda x: x["source_model"]["stationary_distribution"].__setitem__(0, "4/7")),
        one(lambda x: x["source_model"]["transition_matrix_rows_old_columns_new"][0].__setitem__(0, "1/2")),
        one(lambda x: x["tangent_cocycle"]["jacobian_determinants"].__setitem__(1, "1")),
        one(lambda x: x["tangent_cocycle"]["first_moment_operator"][0].__setitem__(0, "0")),
        one(lambda x: x["tangent_cocycle"]["first_moment_traces"].__setitem__("3", "0")),
        one(lambda x: x["tangent_cocycle"]["first_moment_det_I_minus_z"].__setitem__(2, "0")),
        one(lambda x: x["symmetric_second_moment_cocycle"]["operator"][0].__setitem__(0, "0")),
        one(lambda x: x["symmetric_second_moment_cocycle"]["det_I_minus_z"].__setitem__(6, "0")),
        one(lambda x: x["stationary_averaging_control"].__setitem__("intermittency_gap_rank", 0)),
        one(lambda x: x["route_a_verdict"].__setitem__("A2", "A2_GLOBAL_FREDHOLM")),
        one(lambda x: x["claims"].__setitem__("route_b_authorized", True)),
    ]


rejected = 0
for value in cases():
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump(value, f, sort_keys=True, separators=(",", ":")); f.write("\n"); name = f.name
    try:
        validate(Path(name))
    except (AssertionError, KeyError, ValueError):
        rejected += 1
    Path(name).unlink()
assert rejected == len(cases())
print(f"C117_MUTATION_PASS {rejected}/{len(cases())}")
