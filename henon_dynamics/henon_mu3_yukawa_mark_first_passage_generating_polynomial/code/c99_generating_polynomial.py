#!/usr/bin/env python3
"""Produce the exact first-passage probability generating-polynomial atlas."""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from math import factorial, gcd
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
C88 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_subgroup_first_passage_atlas"
C89 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_first_passage_moments_cumulants"
OUT = PROJECT / "results/c99_generating_polynomial_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
N = 16
M = N + 1
TOTAL = factorial(N)
ORDERS = tuple(range(7))
AUTHORITY = {
    "c88": "4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b",
    "c88_manifest": "aab137987b45be54d401b5a021212412de25097b149a73ee65c8e0daaced56c5",
    "c89": "86a589505280721590674235626ddc21e37d57c891c726c7e6fbba98b2bd3af9",
}


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def rational(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def falling(value: int, order: int) -> int:
    out = 1
    for offset in range(order):
        out *= value - offset
    return out


def stirling_second(n: int, k: int) -> int:
    table = [[0] * (n + 1) for _ in range(n + 1)]
    table[0][0] = 1
    for row in range(1, n + 1):
        for col in range(1, row + 1):
            table[row][col] = table[row - 1][col - 1] + col * table[row - 1][col]
    return table[n][k]


def load_sources() -> tuple[dict[str, Any], dict[str, Any]]:
    paths = {
        "c88": C88 / "results/c88_subgroup_first_passage_atlas_evidence.json",
        "c88_manifest": C88 / "C88_PREFREEZE_MANIFEST.json",
        "c89": C89 / "results/c89_first_passage_moments_evidence.json",
    }
    raw = {key: path.read_bytes() for key, path in paths.items()}
    assert {key: digest(value) for key, value in raw.items()} == AUTHORITY
    c88, c89 = json.loads(raw["c88"]), json.loads(raw["c89"])
    assert raw["c88"] == canonical(c88)
    assert raw["c89"] == canonical(c89)
    assert c88["status"] == c89["status"] == "PREFREEZE_G3_PASS"
    assert c88["scope_literal"] == c89["scope_literal"] == FIREWALL
    return c88, c89


def row_for(counts: list[int], index: int, source: dict[str, Any], c89_row: dict[str, Any]) -> dict[str, Any]:
    assert len(counts) == M and sum(counts) == TOTAL
    support = [time for time, value in enumerate(counts) if value]
    support_gcd = 0
    for time in support:
        support_gcd = gcd(support_gcd, time)
    derivatives = {
        str(order): rational(Fraction(sum(falling(time, order) * counts[time] for time in range(M)), TOTAL))
        for order in ORDERS
    }
    recovered_raw = {}
    recovery_terms: dict[str, dict[str, dict[str, int]]] = {}
    for order in ORDERS:
        terms: dict[str, dict[str, int]] = {}
        value = Fraction(0)
        for falling_order in range(order + 1):
            coefficient = stirling_second(order, falling_order)
            term = coefficient * Fraction(derivatives[str(falling_order)]["numerator"], derivatives[str(falling_order)]["denominator"])
            terms[str(falling_order)] = rational(term)
            value += term
        recovery_terms[str(order)] = terms
        recovered_raw[str(order)] = rational(value)
    source_raw = c89_row["raw_moments"]
    assert recovered_raw == source_raw
    terms = [
        {"time": time, "permutation_count": counts[time], "probability": rational(Fraction(counts[time], TOTAL))}
        for time in range(M)
    ]
    return {
        "target_subgroup_index": index,
        "target_subgroup_order": source["target_subgroup_order"],
        "source_c88_row_sha256": digest(canonical(source)),
        "generating_polynomial": {"variable": "z", "terms": terms},
        "permutation_count_by_time": {str(time): counts[time] for time in range(M)},
        "probability_coefficient_by_time": {str(time): rational(Fraction(counts[time], TOTAL)) for time in range(M)},
        "support_times": support,
        "support_minimum": min(support),
        "support_maximum": max(support),
        "degree": max(support),
        "support_gcd": support_gcd,
        "derivative_at_one_orders_0_to_6": derivatives,
        "raw_moment_recovery_from_derivatives": recovered_raw,
        "stirling_recovery_terms": recovery_terms,
        "c89_raw_moments": source_raw,
        "identity_checks": {
            "distribution_normalized": sum(counts) == TOTAL,
            "degree_equals_support_maximum": max(support) == max(support),
            "derivatives_recover_c89_raw_orders_0_to_6": recovered_raw == source_raw,
            "probability_coefficients_sum_to_one": sum(Fraction(counts[time], TOTAL) for time in range(M)) == 1,
        },
    }


def main() -> None:
    c88, c89 = load_sources()
    c88_rows = c88["first_passage_atlas"]["target_rows"]
    c89_rows = c89["moment_atlas"]["target_rows"]
    assert len(c88_rows) == len(c89_rows) == 20
    target_rows = []
    for index, (source, c89_row) in enumerate(zip(c88_rows, c89_rows)):
        counts = [int(source["permutation_count_by_first_passage_time"][str(time)]) for time in range(M)]
        target_rows.append(row_for(counts, index, source, c89_row))
    result = {
        "schema_id": "hcs-c99-first-passage-generating-polynomial-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "authority": AUTHORITY,
        "definition": {
            "random_variable": "T_i=min{k:H_i is hit by the first k labels}",
            "generating_polynomial": "G_i(z)=sum_{t=0}^{16} N_i(t) z^t",
            "probability_generating_function": "P_i(z)=G_i(z)/16!",
            "derivative_identity": "P_i^(m)(1)=E[(T_i)_m]",
            "ordinary_recovery": "E[T_i^r]=sum_{m=0}^r {r\\brace m} P_i^(m)(1)",
            "support_gcd": "gcd of the nonzero-support time indices, with gcd({0})=0",
        },
        "source_model": {"group": "Z/9 + Z/3 + Z/2", "label_count": N, "target_subgroup_count": 20, "total_permutations": TOTAL, "orders": list(ORDERS)},
        "polynomial_atlas": {"target_rows": target_rows},
        "checks": {
            "all_20_polynomials": True,
            "all_340_coefficient_cells": True,
            "all_support_degree_gcd_spectra": True,
            "all_derivatives_orders_0_to_6": True,
            "all_c89_raw_moment_recoveries_orders_0_to_6": True,
            "all_probability_polynomials_normalized": True,
        },
        "claims": {
            "exact_finite_probability_generating_polynomials": True,
            "arithmetic_local_claimed": False,
            "euler_factors_claimed": False,
            "root_numbers_claimed": False,
            "automorphy_claimed": False,
            "full_burnside_ring_claimed": False,
            "full_table_of_marks_claimed": False,
            "hilbert_polya_operator_claimed": False,
        },
    }
    OUT.write_bytes(canonical(result))
    print(json.dumps({"status": result["status"], "target_count": 20, "coefficient_cells": 20 * M, "evidence_sha256": digest(OUT.read_bytes())}, sort_keys=True))


if __name__ == "__main__":
    main()
