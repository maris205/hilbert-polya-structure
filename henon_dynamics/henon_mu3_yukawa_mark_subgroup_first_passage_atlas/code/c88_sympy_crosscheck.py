#!/usr/bin/env python3
"""Symbolic and finite probability cross-check for the C88 atlas."""

from __future__ import annotations

from hashlib import sha256
import json
from math import comb, factorial
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c88_subgroup_first_passage_atlas_evidence.json"
C83 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_random_order_assembly_stopping_time/results/c83_random_order_stopping_time_evidence.json"
C83_HASH = "033f42f0eea2518f7cb269dd465d82d4871a729d2b93679fcd9f3af38cf9ca28"


def q(value: dict[str, int]) -> sp.Rational:
    return sp.Rational(value["numerator"], value["denominator"])


def main() -> None:
    evidence = json.loads(EVIDENCE.read_text())
    assert evidence["schema_id"] == "hcs-c88-subgroup-first-passage-atlas-prefreeze-v1"
    assert evidence["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
    rows = evidence["first_passage_atlas"]["target_rows"]
    assert len(rows) == 20
    z = sp.symbols("z")
    total = factorial(16)
    expectations = []
    for target, row in enumerate(rows):
        assert row["target_subgroup_index"] == target
        counts = row["permutation_count_by_first_passage_time"]
        pgf = sp.expand(sum(value * z ** int(time) for time, value in counts.items()) / total)
        assert sp.simplify(pgf.subs(z, 1) - 1) == 0
        stored_expectation = q(row["expected_first_passage_time"])
        assert sp.diff(pgf, z).subs(z, 1) == stored_expectation
        expectations.append(stored_expectation)
        nonzero = [int(time) for time, count in counts.items() if count]
        assert min(nonzero) == row["minimum_first_passage_time"]
        assert max(nonzero) == row["maximum_first_passage_time"]

        survival_sum = 0
        previous_cdf = sp.Rational(0)
        for time in range(17):
            hit = row["subset_hit_count_by_cardinality"][str(time)]
            nonhit = row["subset_nonhit_count_by_cardinality"][str(time)]
            assert hit + nonhit == comb(16, time)
            cdf = sp.Rational(hit, comb(16, time))
            survival = sp.Rational(nonhit, comb(16, time))
            assert q(row["subset_hit_probability_by_cardinality"][str(time)]) == cdf
            assert q(row["subset_survival_probability_by_cardinality"][str(time)]) == survival
            assert q(row["probability_by_first_passage_time"][str(time)]) == cdf - previous_cdf
            assert row["survival_permutation_count_after_time"][str(time)] == survival * total
            if time:
                pivotal = row["pivotal_edge_count_by_cardinality"][str(time)]
                assert counts[str(time)] == pivotal * factorial(time - 1) * factorial(16 - time)
            if time < 16:
                survival_sum += survival
            previous_cdf = cdf
        assert sp.simplify(survival_sum - stored_expectation) == 0

        pivotal_poly = sum(
            multiplicity * int(key.split(",")[1]) * z ** int(key.split(",")[0])
            for key, multiplicity in row["pivotal_pattern_counts"].items()
        )
        for time in range(17):
            assert sp.expand(pivotal_poly).coeff(z, time) == row["pivotal_edge_count_by_cardinality"][str(time)]

    inclusion = evidence["target_poset"]["inclusion_matrix"]
    assert sum(map(sum, inclusion)) == 102
    for lower in range(20):
        for upper in range(20):
            if not inclusion[lower][upper]:
                continue
            assert expectations[lower] <= expectations[upper]
            for time in range(17):
                assert rows[lower]["subset_hit_count_by_cardinality"][str(time)] >= rows[upper]["subset_hit_count_by_cardinality"][str(time)]
                assert rows[lower]["survival_permutation_count_after_time"][str(time)] <= rows[upper]["survival_permutation_count_after_time"][str(time)]

    c83_raw = C83.read_bytes()
    assert sha256(c83_raw).hexdigest() == C83_HASH
    c83 = json.loads(c83_raw)["assembly_atlas"]
    top = rows[19]
    assert top["permutation_count_by_first_passage_time"] == c83["permutation_count_by_stopping_time"]
    assert top["probability_by_first_passage_time"] == c83["probability_by_stopping_time"]
    assert top["survival_permutation_count_after_time"] == c83["survival_permutation_counts"]
    assert top["expected_first_passage_time"] == c83["expected_stopping_time"]
    print(json.dumps({
        "status": "C88_SYMPY_CROSSCHECK_PASS",
        "target_count": len(rows),
        "normalized_pgf_count": len(rows),
        "monotone_pair_count": 102,
        "top_expectation": str(expectations[19]),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
