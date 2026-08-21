#!/usr/bin/env python3
"""SymPy and exact-array checks for C90."""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from math import factorial
from pathlib import Path
import sympy as sp

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c90_joint_first_passage_evidence.json"
C89 = PROJECT.parent / "henon_mu3_yukawa_mark_first_passage_moments_cumulants" / "results/c89_first_passage_moments_evidence.json"
TOTAL = factorial(16)


def q(value: dict[str, int]) -> sp.Rational:
    return sp.Rational(value["numerator"], value["denominator"])


def main() -> None:
    raw = EVIDENCE.read_bytes()
    evidence = json.loads(raw)
    c89 = json.loads(C89.read_bytes())
    assert evidence["schema_id"] == "hcs-c90-joint-first-passage-coupling-prefreeze-v1"
    assert evidence["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
    rows = evidence["joint_atlas"]["pair_rows"]
    assert len(rows) == 400
    z, w = sp.symbols("z w")
    for index, row in enumerate(rows):
        i, j = divmod(index, 20)
        assert (row["lower_target_index"], row["upper_target_index"]) == (i, j)
        cells = row["joint_survival_permutation_counts"]
        assert q(row["joint_survival_probabilities"]["0"]["0"]) == sp.Rational(cells["0"]["0"], TOTAL)
        for k in range(17):
            for l in range(17):
                value = int(cells[str(k)][str(l)])
                assert value >= 0
                if k < 16:
                    assert value >= int(cells[str(k + 1)][str(l)])
                if l < 16:
                    assert value >= int(cells[str(k)][str(l + 1)])
                assert q(row["joint_survival_probabilities"][str(k)][str(l)]) == sp.Rational(value, TOTAL)
                assert value == int(rows[j * 20 + i]["joint_survival_permutation_counts"][str(l)][str(k)])
        for a in range(1, 7):
            for b in range(1, 7):
                expected = sp.Rational(
                    sum(((k + 1) ** a - k ** a) * ((l + 1) ** b - l ** b) * int(cells[str(k)][str(l)]) for k in range(16) for l in range(16)),
                    TOTAL,
                )
                assert q(row["mixed_raw_moments"][str(a)][str(b)]) == expected
        for order in range(7):
            assert q(row["mixed_raw_moments"][str(order)]["0"]) == q(c89["moment_atlas"]["target_rows"][i]["raw_moments"][str(order)])
            assert q(row["mixed_raw_moments"]["0"][str(order)]) == q(c89["moment_atlas"]["target_rows"][j]["raw_moments"][str(order)])
        ei = q(c89["moment_atlas"]["target_rows"][i]["mean"])
        ej = q(c89["moment_atlas"]["target_rows"][j]["mean"])
        assert q(row["covariance"]) == q(row["mixed_raw_moments"]["1"]["1"]) - ei * ej
    print(json.dumps({"status": "C90_SYMPY_CROSSCHECK_PASS", "ordered_pair_count": 400, "joint_cells": 400 * 289, "evidence_sha256": sha256(raw).hexdigest()}, sort_keys=True))


if __name__ == "__main__":
    main()
