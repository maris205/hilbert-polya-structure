#!/usr/bin/env python3
"""Hostile in-memory mutation gate for C116."""
import copy
import json
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "results/c116_lozi_evidence.json").read_text())


def validate(data):
    assert data["schema"] == "hcs-c116-lozi-nonsmooth-route-a-v1"
    assert data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
    source = data["source_model"]
    assert source["parameters"] == {"a": "2", "b": "1/2"}
    assert source["branch_domains"] == {"0": "x<0", "1": "x>0"}
    assert source["border"] == "x=0 excluded before enumeration"
    assert source["diagnostic_branch_weights"] == ["1/2", "2/3"]
    expected_rooted = {"1": 2, "2": 4, "3": 2, "4": 8, "5": 22, "6": 40, "7": 58, "8": 128}
    expected_primitive = {"1": 2, "2": 1, "3": 0, "4": 1, "5": 4, "6": 6, "7": 8, "8": 15}
    assert data["rooted_admissible_counts"] == expected_rooted
    assert data["primitive_necklace_counts"] == expected_primitive
    assert sum(data["primitive_necklace_counts"].values()) == len(data["primitive_rows"]) == 37
    for n in range(1, 9):
        record = data["word_classification_counts"][str(n)]
        assert record["total_words"] == 2**n
        assert record["admissible_strict"] == expected_rooted[str(n)]
        assert sum(record[key] for key in ("admissible_strict", "sign_mismatch", "border_hit", "singular_return")) == 2**n
    weights = (Q(1, 2), Q(2, 3))
    dimension = 0
    for row in data["primitive_rows"]:
        n = row["length"]
        assert len(row["symbols"]) == n and row["word"] == "".join(map(str, row["symbols"]))
        assert row["strict_x_margin"] != "0" and Q(row["strict_x_margin"]) > 0
        weight = Q(1)
        for symbol in row["symbols"]:
            weight *= weights[symbol]
        assert row["branch_weight"] == str(weight)
        dimension += n
    operator = data["finite_cycle_atlas_operator"]
    assert operator["dimension"] == dimension == 240
    assert operator["block_count"] == 37 and len(operator["sparse_edges"]) == 240
    for power in range(1, 9):
        trace = sum(
            row["length"] * Q(row["branch_weight"]) ** (power // row["length"])
            for row in data["primitive_rows"]
            if power % row["length"] == 0
        )
        assert operator["weighted_trace_prefix"][str(power)] == str(trace)
        assert operator["unweighted_trace_prefix"][str(power)] == expected_rooted[str(power)]
    assert data["verdict"]["A1"] == "A1_PARTIAL_CERTIFIED"
    assert data["verdict"]["A2"] == "A2_CERTIFIED_PREFIX"
    assert data["verdict"]["A3"] == "A3_NOT_ADDRESSED"
    assert data["verdict"]["A4"] == "A4_FAIL"


mutations = [
    ("parameter", lambda d: d["source_model"]["parameters"].update({"a": "3"})),
    ("border", lambda d: d["source_model"].update({"border": "x=0 assigned to branch 1"})),
    ("domain", lambda d: d["source_model"]["branch_domains"].update({"0": "x<=0"})),
    ("weight", lambda d: d["source_model"].update({"diagnostic_branch_weights": ["1", "1"]})),
    ("rooted_count", lambda d: d["rooted_admissible_counts"].update({"8": 256})),
    ("primitive_count", lambda d: d["primitive_necklace_counts"].update({"5": 5})),
    ("classification", lambda d: d["word_classification_counts"]["3"].update({"sign_mismatch": 5})),
    ("margin", lambda d: d["primitive_rows"][0].update({"strict_x_margin": "0"})),
    ("trace", lambda d: d["finite_cycle_atlas_operator"]["weighted_trace_prefix"].update({"8": "0"})),
    ("dimension", lambda d: d["finite_cycle_atlas_operator"].update({"dimension": 239})),
    ("scope", lambda d: d.update({"scope_literal": "ARITHMETIC_ROUTE"})),
    ("verdict", lambda d: d["verdict"].update({"A2": "A2_ANALYTIC_DETERMINANT"})),
]

validate(DATA)
rejected = 0
for name, mutate in mutations:
    candidate = copy.deepcopy(DATA)
    mutate(candidate)
    try:
        validate(candidate)
    except (AssertionError, KeyError, ValueError, ZeroDivisionError):
        rejected += 1
    else:
        raise AssertionError(f"mutation escaped: {name}")
assert rejected == len(mutations)
print("C116_MUTATION_PASS", rejected, "/", len(mutations))
