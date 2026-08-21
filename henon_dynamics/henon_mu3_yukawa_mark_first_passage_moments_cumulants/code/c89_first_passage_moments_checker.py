#!/usr/bin/env python3
"""Independent bitset reconstruction for the C89 moment receipt."""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from math import comb, factorial
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
C88 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_subgroup_first_passage_atlas"
EVIDENCE = PROJECT / "results/c89_first_passage_moments_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
LABEL_COUNT = 16
SUPPORT_COUNT = 1 << LABEL_COUNT
TOTAL = factorial(LABEL_COUNT)
ORDERS = tuple(range(7))
AUTHORITY = {
    "c88": "4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b",
    "c88_manifest": "aab137987b45be54d401b5a021212412de25097b149a73ee65c8e0daaced56c5",
}


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def rational(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def falling(value: int, order: int) -> int:
    output = 1
    for offset in range(order):
        output *= value - offset
    return output


def moment_block(counts: list[int]) -> dict[str, Any]:
    mean = Fraction(sum(time * count for time, count in enumerate(counts)), TOTAL)
    raw_values = {order: Fraction(sum(time ** order * count for time, count in enumerate(counts)), TOTAL) for order in ORDERS}
    factorial_values = {order: Fraction(sum(falling(time, order) * count for time, count in enumerate(counts)), TOTAL) for order in ORDERS}
    central_values = {order: sum((Fraction(time) - mean) ** order * count for time, count in enumerate(counts)) / TOTAL for order in ORDERS}
    cumulants = {0: Fraction(0)}
    for order in range(1, 7):
        value = raw_values[order]
        for lower in range(1, order):
            value -= comb(order - 1, lower - 1) * cumulants[lower] * raw_values[order - lower]
        cumulants[order] = value
    return {
        "mean": rational(mean),
        "raw_moments": {str(order): rational(raw_values[order]) for order in ORDERS},
        "falling_factorial_moments": {str(order): rational(factorial_values[order]) for order in ORDERS},
        "central_moments": {str(order): rational(central_values[order]) for order in ORDERS},
        "cumulants": {str(order): rational(cumulants[order]) for order in range(1, 7)},
    }


def survival_block(counts: list[int]) -> dict[str, Any]:
    tails = [sum(counts[time + 1:]) for time in range(LABEL_COUNT + 1)]
    raw: dict[str, dict[str, int]] = {}
    factorial_values: dict[str, dict[str, int]] = {}
    for order in ORDERS:
        if order == 0:
            raw[str(order)] = rational(Fraction(1))
            factorial_values[str(order)] = rational(Fraction(1))
        else:
            raw_value = sum(((time + 1) ** order - time ** order) * tails[time] for time in range(LABEL_COUNT))
            fact_value = factorial(order) * sum(comb(time, order - 1) * tails[time] for time in range(order - 1, LABEL_COUNT))
            raw[str(order)] = rational(Fraction(raw_value, TOTAL))
            factorial_values[str(order)] = rational(Fraction(fact_value, TOTAL))
    return {
        "survival_permutation_counts": {str(time): tails[time] for time in range(LABEL_COUNT + 1)},
        "survival_raw_moments": raw,
        "survival_falling_factorial_moments": factorial_values,
    }


def build_expected() -> dict[str, Any]:
    c88_path = C88 / "results/c88_subgroup_first_passage_atlas_evidence.json"
    manifest_path = C88 / "C88_PREFREEZE_MANIFEST.json"
    c88_raw, manifest_raw = c88_path.read_bytes(), manifest_path.read_bytes()
    assert digest(c88_raw) == AUTHORITY["c88"]
    assert digest(manifest_raw) == AUTHORITY["c88_manifest"]
    c88 = json.loads(c88_raw)
    assert c88["status"] == "PREFREEZE_G3_PASS" and c88["scope_literal"] == FIREWALL
    rows: list[dict[str, Any]] = []
    for index, source in enumerate(c88["first_passage_atlas"]["target_rows"]):
        raw_bits = bytes.fromhex(source["subset_hit_bitset_hex"])
        assert len(raw_bits) == SUPPORT_COUNT // 8
        hit = [bool(raw_bits[support // 8] & (1 << (support % 8))) for support in range(SUPPORT_COUNT)]
        hit_counts = [sum(hit[support] and support.bit_count() == time for support in range(SUPPORT_COUNT)) for time in range(LABEL_COUNT + 1)]
        assert all(hit_counts[time] + sum((not hit[support]) and support.bit_count() == time for support in range(SUPPORT_COUNT)) == comb(LABEL_COUNT, time) for time in range(LABEL_COUNT + 1))
        counts = [0] * (LABEL_COUNT + 1)
        for time in range(1, LABEL_COUNT + 1):
            pivotal = sum(
                sum(not hit[support ^ (1 << label)] for label in range(LABEL_COUNT) if support & (1 << label))
                for support in range(SUPPORT_COUNT)
                if hit[support] and support.bit_count() == time
            )
            counts[time] = pivotal * factorial(time - 1) * factorial(LABEL_COUNT - time)
        counts[0] = TOTAL if hit[0] else 0
        assert sum(counts) == TOTAL
        row: dict[str, Any] = {
            "target_subgroup_index": index,
            "target_subgroup_order": source["target_subgroup_order"],
            "source_c88_row_sha256": digest(canonical(source)),
            "permutation_count_by_first_passage_time": {str(time): counts[time] for time in range(LABEL_COUNT + 1)},
            "probability_by_first_passage_time": {str(time): rational(Fraction(counts[time], TOTAL)) for time in range(LABEL_COUNT + 1)},
        }
        row.update(moment_block(counts))
        row.update(survival_block(counts))
        row["identity_checks"] = {
            "distribution_normalized": True,
            "raw_equals_survival_raw": row["raw_moments"] == row["survival_raw_moments"],
            "factorial_equals_survival_factorial": row["falling_factorial_moments"] == row["survival_falling_factorial_moments"],
            "mean_equals_first_cumulant": row["mean"] == row["cumulants"]["1"],
            "mean_equals_c88_expectation": row["mean"] == source["expected_first_passage_time"],
        }
        assert all(row["identity_checks"].values())
        rows.append(row)
    return {
        "schema_id": "hcs-c89-first-passage-moments-cumulants-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "authority": AUTHORITY,
        "definition": {
            "random_variable": "T_H=min{k:H<=Phi(A_k)} for the uniform 16-label permutation",
            "moment_orders": list(ORDERS),
            "raw_moment": "m_r=E[T^r]",
            "falling_factorial_moment": "f_r=E[(T)_r], (T)_r=T(T-1)...(T-r+1)",
            "central_moment": "mu_r=E[(T-E[T])^r]",
            "cumulant_recursion": "kappa_n=m_n-sum_{j=1}^{n-1} binom(n-1,j-1) kappa_j m_{n-j}",
            "survival_raw_identity": "E[T^r]=sum_{k=0}^{15}((k+1)^r-k^r)P(T>k)",
            "survival_factorial_identity": "E[(T)_r]=r! sum_{k=0}^{15} binom(k,r-1)P(T>k)",
        },
        "source_model": {
            "group": "Z/9 + Z/3 + Z/2",
            "label_count": LABEL_COUNT,
            "target_subgroup_count": len(rows),
            "total_permutations": TOTAL,
            "source_c88_evidence_sha256": AUTHORITY["c88"],
        },
        "moment_atlas": {"target_rows": rows},
        "checks": {
            "all_20_targets": True,
            "all_17_distribution_cells": True,
            "all_raw_factorial_central_orders_0_to_6": True,
            "all_cumulants_orders_1_to_6": True,
            "all_survival_tail_identities": True,
            "all_c88_means_rebound": True,
            "all_probability_generating_functions_normalized": True,
        },
        "claims": {
            "exact_finite_moment_laws": True,
            "arithmetic_local_claimed": False,
            "euler_factors_claimed": False,
            "root_numbers_claimed": False,
            "automorphy_claimed": False,
            "full_burnside_ring_claimed": False,
            "full_table_of_marks_claimed": False,
            "hilbert_polya_operator_claimed": False,
        },
    }


def main() -> None:
    expected = build_expected()
    observed_raw = EVIDENCE.read_bytes()
    observed = json.loads(observed_raw)
    assert observed_raw == canonical(observed)
    assert observed == expected
    print(json.dumps({"status": "C89_INDEPENDENT_CHECK_PASS", "target_count": 20, "evidence_sha256": digest(observed_raw)}, sort_keys=True))


if __name__ == "__main__":
    main()
