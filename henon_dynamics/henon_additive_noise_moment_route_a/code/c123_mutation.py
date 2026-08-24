#!/usr/bin/env python3
"""Hostile evidence mutations for the independent C123 checker."""
from copy import deepcopy
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))
from c123_noise_checker import CheckFailure, validate  # noqa: E402

base = json.loads((ROOT / "results" / "c123_noise_evidence.json").read_text())


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
    change(["source_model", "linear_part", 0, 0], "2/3"),
    change(["source_model", "noise_probabilities", 0], "1/3"),
    change(["periodic_noise_word_atlas", "rooted_words_tested"], 62),
    change(["periodic_noise_word_atlas", "primitive_necklace_counts", "6"], 8),
    change(["periodic_noise_word_atlas", "row_probability_semantics"], "necklace total mass"),
    change(["periodic_noise_word_atlas", "rows", 0, "chosen_rooted_block_probability"], "1"),
    change(["periodic_noise_word_atlas", "rows", 0, "states", 0, 0], "0"),
    change(["degree_four_markov_operator", "matrix", 3, 0], "1"),
    change(["degree_four_markov_operator", "trace"], "1"),
    change(["degree_four_markov_operator", "det_I_minus_z", 2], "0"),
    change(["stationary_moments_through_degree_four", "covariance", 0, 0], "1"),
    change(["stationary_moments_through_degree_four", "x_fourth_cumulant"], "0"),
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
    raise SystemExit(f"C123_MUTATION_FAIL {rejected}/{len(mutations)}")
print(f"C123_MUTATION_PASS {rejected}/{len(mutations)}")
