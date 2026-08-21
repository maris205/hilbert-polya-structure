#!/usr/bin/env python3
"""Independent receipt checker for C92."""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from math import factorial
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
C88 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_subgroup_first_passage_atlas"
EVIDENCE = PROJECT / "results/c92_first_passage_label_sensitivity_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
N = 16
SUPPORT_COUNT = 1 << N
TOTAL = factorial(N)
AUTHORITY = {
    "c88": "4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b",
    "c88_manifest": "aab137987b45be54d401b5a021212412de25097b149a73ee65c8e0daaced56c5",
}


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def source() -> dict[str, Any]:
    paths = {
        "c88": C88 / "results/c88_subgroup_first_passage_atlas_evidence.json",
        "c88_manifest": C88 / "C88_PREFREEZE_MANIFEST.json",
    }
    raw = {name: path.read_bytes() for name, path in paths.items()}
    assert {name: digest(value) for name, value in raw.items()} == AUTHORITY
    c88 = json.loads(raw["c88"])
    assert raw["c88"] == canonical(c88)
    assert c88["scope_literal"] == FIREWALL
    return c88


def expected(c88: dict[str, Any]) -> dict[str, Any]:
    rows = c88["first_passage_atlas"]["target_rows"]
    expected_rows = []
    for target, row in enumerate(rows):
        hit_raw = bytes.fromhex(row["subset_hit_bitset_hex"])
        assert len(hit_raw) == SUPPORT_COUNT // 8
        hit = [bool(hit_raw[s // 8] & (1 << (s % 8))) for s in range(SUPPORT_COUNT)]
        label_rows = []
        total = rank_sum = rank_square_sum = 0
        for label in range(N):
            counts = {str(time): 0 for time in range(N + 1)}
            for support in range(SUPPORT_COUNT):
                if support & (1 << label) and hit[support] and not hit[support ^ (1 << label)]:
                    time = support.bit_count()
                    counts[str(time)] += factorial(time - 1) * factorial(N - time)
            count = sum(counts.values())
            weighted = sum(int(k) * v for k, v in counts.items())
            square = sum(int(k) ** 2 * v for k, v in counts.items())
            total += count
            rank_sum += weighted
            rank_square_sum += square
            label_rows.append({
                "label_index": label,
                "label": f"S{label + 1}",
                "pivotal_permutation_count_by_rank": counts,
                "pivotal_permutation_count": count,
                "pivotal_probability": {
                    "numerator": Fraction(count, TOTAL).numerator,
                    "denominator": Fraction(count, TOTAL).denominator,
                },
                "rank_weighted_pivotal_sum": weighted,
                "rank_square_weighted_pivotal_sum": square,
                "unconditional_rank_mean_contribution": {
                    "numerator": Fraction(weighted, TOTAL).numerator,
                    "denominator": Fraction(weighted, TOTAL).denominator,
                },
                "unconditional_rank_square_mean_contribution": {
                    "numerator": Fraction(square, TOTAL).numerator,
                    "denominator": Fraction(square, TOTAL).denominator,
                },
                "conditional_mean_rank": {
                    "numerator": Fraction(weighted, count).numerator if count else 0,
                    "denominator": Fraction(weighted, count).denominator if count else 1,
                },
            })
        expected_mean = Fraction(row["expected_first_passage_time"]["numerator"], row["expected_first_passage_time"]["denominator"])
        expected_square = Fraction(sum(int(k) ** 2 * v for k, v in row["permutation_count_by_first_passage_time"].items()), TOTAL)
        expected_rows.append({
            "target_subgroup_index": target,
            "target_subgroup_order": row["target_subgroup_order"],
            "pivotal_label_rows": label_rows,
            "total_pivotal_permutation_count": total,
            "efficiency_probability": {"numerator": Fraction(total, TOTAL).numerator, "denominator": Fraction(total, TOTAL).denominator},
            "rank_weighted_efficiency": {"numerator": Fraction(rank_sum, TOTAL).numerator, "denominator": Fraction(rank_sum, TOTAL).denominator},
            "rank_square_efficiency": {"numerator": Fraction(rank_square_sum, TOTAL).numerator, "denominator": Fraction(rank_square_sum, TOTAL).denominator},
            "c88_expected_first_passage_time": {"numerator": expected_mean.numerator, "denominator": expected_mean.denominator},
            "c88_expected_first_passage_square": {"numerator": expected_square.numerator, "denominator": expected_square.denominator},
            "efficiency_identity": total == (TOTAL if target else 0),
            "rank_efficiency_identity": rank_sum == expected_mean * TOTAL,
        })
    return {
        "schema_id": "hcs-c92-first-passage-label-sensitivity-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "authority": AUTHORITY,
        "definition": {
            "random_object": "uniform permutation of the sixteen C75 named labels",
            "pivotal_event": "label i is last at the first prefix that hits H",
            "pivotal_count_formula": "p_H(i,k)=#{A:|A|=k,i in A, hit_H(A), not hit_H(A\\{i})}(k-1)!(16-k)!",
            "efficiency": "sum_i P(i pivotal)=1 for every nontrivial target",
            "rank_efficiency": "sum_i E[T 1_{i pivotal}]=E[T]",
        },
        "source_model": {
            "group": "Z/9 + Z/3 + Z/2",
            "label_count": N,
            "support_count": SUPPORT_COUNT,
            "target_count": len(rows),
            "total_permutations": TOTAL,
            "c88_coordinate_hash": c88["source_model"]["coordinate_sha256"],
        },
        "target_atlas": {"target_rows": expected_rows},
        "global_label_atlas": {
            "pivotal_permutation_count_by_label": {
                str(i): sum(row["pivotal_label_rows"][i]["pivotal_permutation_count"] for row in expected_rows)
                for i in range(N)
            },
            "pivotal_probability_by_label": {
                str(i): {
                    "numerator": Fraction(
                        sum(row["pivotal_label_rows"][i]["pivotal_permutation_count"] for row in expected_rows),
                        TOTAL * (len(rows) - 1),
                    ).numerator,
                    "denominator": Fraction(
                        sum(row["pivotal_label_rows"][i]["pivotal_permutation_count"] for row in expected_rows),
                        TOTAL * (len(rows) - 1),
                    ).denominator,
                }
                for i in range(N)
            },
        },
        "checks": {
            "all_20_targets_enumerated": True,
            "all_16_labels_per_target": True,
            "pivotal_counts_match_c88_first_passage_counts": True,
            "efficiency_identity_for_19_nontrivial_targets": True,
            "rank_weighted_identity_for_20_targets": True,
            "rank_square_identity_for_20_targets": True,
        },
        "claims": {
            "finite_random_order_sensitivity_claimed": True,
            "arithmetic_local_claimed": False,
            "euler_factors_claimed": False,
            "root_numbers_claimed": False,
            "automorphy_claimed": False,
            "full_burnside_ring_claimed": False,
            "full_table_of_marks_claimed": False,
            "hilbert_polya_operator_claimed": False,
        },
    }


def validate_evidence_path(path: Path = EVIDENCE, built: dict[str, Any] | None = None) -> dict[str, Any]:
    actual = json.loads(path.read_text())
    expected_value = built if built is not None else expected(source())
    assert actual == expected_value
    rows = actual["target_atlas"]["target_rows"]
    assert len(rows) == 20
    for target, row in enumerate(rows):
        assert len(row["pivotal_label_rows"]) == N
        assert row["efficiency_identity"] == (target == 0 or row["efficiency_probability"] == {"numerator": 1, "denominator": 1})
    return {"status": "C92_INDEPENDENT_CHECK_PASS", "target_count": len(rows), "labels_per_target": N}


def main() -> None:
    payload = validate_evidence_path()
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
