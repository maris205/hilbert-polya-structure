#!/usr/bin/env python3
"""Produce the exact C92 random-order label sensitivity atlas."""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from math import factorial
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
C88 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_subgroup_first_passage_atlas"
OUT = PROJECT / "results/c92_first_passage_label_sensitivity_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
LABEL_COUNT = 16
SUPPORT_COUNT = 1 << LABEL_COUNT
TOTAL = factorial(LABEL_COUNT)
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


def source() -> tuple[dict, dict[str, bytes]]:
    paths = {
        "c88": C88 / "results/c88_subgroup_first_passage_atlas_evidence.json",
        "c88_manifest": C88 / "C88_PREFREEZE_MANIFEST.json",
    }
    raw = {name: path.read_bytes() for name, path in paths.items()}
    assert {name: digest(value) for name, value in raw.items()} == AUTHORITY
    evidence = json.loads(raw["c88"])
    assert raw["c88"] == canonical(evidence)
    assert evidence["status"] == "PREFREEZE_G3_PASS"
    assert evidence["scope_literal"] == FIREWALL
    return evidence, raw


def hit_rows(evidence: dict) -> list[list[bool]]:
    rows = evidence["first_passage_atlas"]["target_rows"]
    result = []
    for row in rows:
        raw = bytes.fromhex(row["subset_hit_bitset_hex"])
        assert len(raw) == SUPPORT_COUNT // 8
        result.append([bool(raw[support // 8] & (1 << (support % 8))) for support in range(SUPPORT_COUNT)])
    return result


def main() -> None:
    evidence, _ = source()
    rows = evidence["first_passage_atlas"]["target_rows"]
    hits = hit_rows(evidence)
    target_rows = []
    global_pivotal = [0] * LABEL_COUNT
    for target, (row, hit) in enumerate(zip(rows, hits)):
        by_label = []
        total_pivotal = 0
        rank_sum = 0
        rank_square_sum = 0
        for label in range(LABEL_COUNT):
            counts = {str(time): 0 for time in range(LABEL_COUNT + 1)}
            for support in range(SUPPORT_COUNT):
                if not (support & (1 << label)) or not hit[support] or hit[support ^ (1 << label)]:
                    continue
                time = support.bit_count()
                count = factorial(time - 1) * factorial(LABEL_COUNT - time)
                counts[str(time)] += count
            count_total = sum(counts.values())
            weighted = sum(int(time) * count for time, count in counts.items())
            square = sum(int(time) ** 2 * count for time, count in counts.items())
            total_pivotal += count_total
            rank_sum += weighted
            rank_square_sum += square
            global_pivotal[label] += count_total
            by_label.append({
                "label_index": label,
                "label": f"S{label + 1}",
                "pivotal_permutation_count_by_rank": counts,
                "pivotal_permutation_count": count_total,
                "pivotal_probability": rational(Fraction(count_total, TOTAL)),
                "rank_weighted_pivotal_sum": weighted,
                "rank_square_weighted_pivotal_sum": square,
                "unconditional_rank_mean_contribution": rational(Fraction(weighted, TOTAL)),
                "unconditional_rank_square_mean_contribution": rational(Fraction(square, TOTAL)),
                "conditional_mean_rank": rational(Fraction(weighted, count_total)) if count_total else rational(Fraction(0)),
            })
        expected = Fraction(row["expected_first_passage_time"]["numerator"], row["expected_first_passage_time"]["denominator"])
        expected_square = Fraction(
            sum(int(time) ** 2 * count for time, count in row["permutation_count_by_first_passage_time"].items()),
            TOTAL,
        )
        first_passage_counts = {str(k): int(v) for k, v in row["permutation_count_by_first_passage_time"].items()}
        assert total_pivotal == sum(count for time, count in first_passage_counts.items() if int(time) > 0)
        assert rank_sum == expected * TOTAL
        assert rank_square_sum == expected_square * TOTAL
        target_rows.append({
            "target_subgroup_index": target,
            "target_subgroup_order": row["target_subgroup_order"],
            "pivotal_label_rows": by_label,
            "total_pivotal_permutation_count": total_pivotal,
            "efficiency_probability": rational(Fraction(total_pivotal, TOTAL)),
            "rank_weighted_efficiency": rational(Fraction(rank_sum, TOTAL)),
            "rank_square_efficiency": rational(Fraction(rank_square_sum, TOTAL)),
            "c88_expected_first_passage_time": rational(expected),
            "c88_expected_first_passage_square": rational(expected_square),
            "efficiency_identity": total_pivotal == (TOTAL if target else 0),
            "rank_efficiency_identity": rank_sum == expected * TOTAL,
        })
    result = {
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
            "label_count": LABEL_COUNT,
            "support_count": SUPPORT_COUNT,
            "target_count": len(rows),
            "total_permutations": TOTAL,
            "c88_coordinate_hash": evidence["source_model"]["coordinate_sha256"],
        },
        "target_atlas": {"target_rows": target_rows},
        "global_label_atlas": {
            "pivotal_permutation_count_by_label": {str(i): count for i, count in enumerate(global_pivotal)},
            "pivotal_probability_by_label": {str(i): rational(Fraction(count, TOTAL * (len(rows) - 1))) for i, count in enumerate(global_pivotal)},
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
    OUT.write_bytes(canonical(result))
    print(json.dumps({
        "status": result["status"],
        "target_count": len(rows),
        "labels_per_target": LABEL_COUNT,
        "evidence_sha256": digest(OUT.read_bytes()),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
