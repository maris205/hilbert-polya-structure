#!/usr/bin/env python3
"""SymPy exact-rational cross-check for every C94 grid and moment identity."""

from __future__ import annotations

from hashlib import sha256
import json
from math import factorial
from pathlib import Path

import sympy as sp

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c94_first_passage_hazard_residual_evidence.json"
N = 16
TOTAL = factorial(N)


def q(value: dict[str, int]) -> sp.Rational:
    return sp.Rational(value["numerator"], value["denominator"])


def main() -> None:
    raw = EVIDENCE.read_bytes()
    evidence = json.loads(raw)
    assert evidence["schema_id"] == "hcs-c94-first-passage-hazard-residual-prefreeze-v1"
    assert evidence["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
    checked_hazards = checked_residual_cells = checked_defined_rows = 0
    z = sp.symbols("z")
    for row in evidence["hazard_residual_atlas"]["target_rows"]:
        counts = [int(row["permutation_count_by_first_passage_time"][str(k)]) for k in range(N + 1)]
        survival = [int(row["survival_permutation_count_after_time"][str(k)]) for k in range(N + 1)]
        pgf = sum(sp.Integer(counts[k]) * z**k for k in range(N + 1)) / TOTAL
        assert sp.simplify(pgf.subs(z, 1) - 1) == 0
        hazard = row["hazard_atlas"]
        for k in range(N + 1):
            risk = TOTAL if k == 0 else survival[k - 1]
            assert int(hazard["at_risk_permutation_count_before_step"][str(k)]) == risk
            if risk:
                expected = sp.Rational(counts[k], risk)
                assert q(hazard["hazard_probability"][str(k)]) == expected
                assert q(hazard["survival_transition_probability"][str(k)]) == 1 - expected
            else:
                assert hazard["hazard_probability"][str(k)] is None
                assert hazard["survival_transition_probability"][str(k)] is None
            checked_hazards += 1
        for entry in row["residual_life_atlas"]:
            k = int(entry["conditioning_step_k"])
            denominator = survival[k]
            assert entry["conditioning_survival_permutation_count"] == denominator
            for r in range(N + 1):
                s_cell = entry["conditional_residual_survival_probability_by_r"][str(r)]
                p_cell = entry["conditional_residual_probability_mass_by_r"][str(r)]
                if denominator == 0 or r > N - k:
                    assert s_cell is None and p_cell is None
                    continue
                assert q(s_cell) == sp.Rational(survival[k + r], denominator)
                assert q(p_cell) == sp.Rational(0 if r == 0 else counts[k + r], denominator)
                checked_residual_cells += 2
            if denominator:
                mean = sum(sp.Integer(t - k) * counts[t] for t in range(k + 1, N + 1)) / denominator
                second = sum(sp.Integer(t - k) ** 2 * counts[t] for t in range(k + 1, N + 1)) / denominator
                assert q(entry["mean_residual_life"]) == mean
                assert q(entry["second_residual_moment"]) == second
                assert q(entry["variance_residual_life"]) == second - mean**2
                checked_defined_rows += 1
    print(json.dumps({
        "status": "C94_SYMPY_CROSSCHECK_PASS",
        "target_count": 20,
        "hazard_steps": checked_hazards,
        "residual_probability_cells": checked_residual_cells,
        "defined_mean_variance_rows": checked_defined_rows,
        "evidence_sha256": sha256(raw).hexdigest(),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
