#!/usr/bin/env python3
"""Exact rational and generating-function cross-check for C91."""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from math import factorial
from pathlib import Path

import sympy as sp

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c91_first_passage_race_atlas_evidence.json"
EXPECTED_C88 = "4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b"


def q(value: dict[str, int]) -> sp.Rational:
    return sp.Rational(value["numerator"], value["denominator"])


def main() -> None:
    evidence = json.loads(EVIDENCE.read_text())
    assert evidence["schema_id"] == "hcs-c91-first-passage-race-atlas-prefreeze-v1"
    assert evidence["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
    assert evidence["authority"]["c88"] == EXPECTED_C88
    pairs = evidence["race_atlas"]["pair_rows"]
    assert len(pairs) == 108
    total = factorial(16)
    z = sp.symbols("z")
    tie_pairs = 0
    for row in pairs:
        counts = row["outcome_permutation_count"]
        assert sum(counts.values()) == total
        probs = row["outcome_probability"]
        assert sum((q(probs[name]) for name in ("left_first", "tie", "right_first")), sp.Rational(0)) == 1
        by_time = row["outcome_permutation_count_by_first_passage_time"]
        edge_by_time = row["boundary_edge_count_by_first_passage_time"]
        for time in range(17):
            cell = by_time[str(time)]
            edge = edge_by_time[str(time)]
            weight = 0 if time == 0 else factorial(time - 1) * factorial(16 - time)
            for name in ("left_first", "tie", "right_first"):
                assert cell[name] == edge[name] * weight
        assert sum(sum(by_time[str(time)].values()) for time in range(17)) == total
        for name in ("left_first", "tie", "right_first"):
            pgf = sp.expand(sum(by_time[str(time)][name] * z**time for time in range(17)) / total)
            assert sp.simplify(pgf.subs(z, 1) - q(probs[name])) == 0
        tie_pairs += int(row["tie_nonzero"])
    aggregate = evidence["race_atlas"]["aggregate_outcome_permutation_count"]
    assert aggregate["left_first"] + aggregate["tie"] + aggregate["right_first"] == 108 * total
    assert tie_pairs == evidence["race_atlas"]["pairs_with_nonzero_ties"] == 99
    print(json.dumps({
        "status": "C91_SYMPY_CROSSCHECK_PASS",
        "pair_count": len(pairs),
        "normalized_outcome_pgf_count": 3 * len(pairs),
        "pairs_with_nonzero_ties": tie_pairs,
        "evidence_sha256": sha256(EVIDENCE.read_bytes()).hexdigest(),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
