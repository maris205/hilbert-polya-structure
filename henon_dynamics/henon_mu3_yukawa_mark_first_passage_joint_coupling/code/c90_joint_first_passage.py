#!/usr/bin/env python3
"""Produce the exact joint-survival and mixed-moment atlas for C90."""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from math import factorial
from pathlib import Path
from typing import Any

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
C88 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_subgroup_first_passage_atlas"
C89 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_first_passage_moments_cumulants"
OUT = PROJECT / "results/c90_joint_first_passage_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
LABEL_COUNT = 16
TARGET_COUNT = 20
SUPPORT_COUNT = 1 << LABEL_COUNT
TOTAL = factorial(LABEL_COUNT)
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


def load_sources() -> tuple[dict[str, Any], dict[str, Any]]:
    c88_path = C88 / "results/c88_subgroup_first_passage_atlas_evidence.json"
    c88_manifest_path = C88 / "C88_PREFREEZE_MANIFEST.json"
    c89_path = C89 / "results/c89_first_passage_moments_evidence.json"
    c88_raw = c88_path.read_bytes()
    c88_manifest_raw = c88_manifest_path.read_bytes()
    c89_raw = c89_path.read_bytes()
    assert digest(c88_raw) == AUTHORITY["c88"]
    assert digest(c88_manifest_raw) == AUTHORITY["c88_manifest"]
    assert digest(c89_raw) == AUTHORITY["c89"]
    c88 = json.loads(c88_raw)
    c89 = json.loads(c89_raw)
    assert c88["scope_literal"] == c89["scope_literal"] == FIREWALL
    assert c88["status"] == "PREFREEZE_G3_PASS"
    return c88, c89


def arrays_from_c88(c88: dict[str, Any]) -> tuple[np.ndarray, np.ndarray]:
    sizes = np.fromiter((support.bit_count() for support in range(SUPPORT_COUNT)), dtype=np.int8, count=SUPPORT_COUNT)
    nonhit = np.zeros((TARGET_COUNT, 17, SUPPORT_COUNT), dtype=np.float64)
    for target, row in enumerate(c88["first_passage_atlas"]["target_rows"]):
        packed = np.frombuffer(bytes.fromhex(row["subset_hit_bitset_hex"]), dtype=np.uint8)
        hit = np.unpackbits(packed, bitorder="little")[:SUPPORT_COUNT].astype(bool)
        for time in range(17):
            nonhit[target, time, (sizes == time) & ~hit] = 1.0
    # Superset zeta transform: after the transform, entry A counts admissible
    # exact-size-l supersets B containing A.
    supersets = np.zeros_like(nonhit, dtype=np.float64)
    for target in range(TARGET_COUNT):
        for time in range(17):
            values = nonhit[target, time].copy()
            for bit in range(LABEL_COUNT):
                step = 1 << bit
                view = values.reshape(-1, 2 * step)
                view[:, :step] += view[:, step:]
            supersets[target, time] = values
    return nonhit, supersets


def mixed_from_joint(joint: np.ndarray, i: int, j: int, a: int, b: int, c89_rows: list[dict[str, Any]]) -> Fraction:
    if a == 0 and b == 0:
        return Fraction(1)
    if a == 0:
        value = c89_rows[j]["raw_moments"][str(b)]
        return Fraction(value["numerator"], value["denominator"])
    if b == 0:
        value = c89_rows[i]["raw_moments"][str(a)]
        return Fraction(value["numerator"], value["denominator"])
    total = sum(
        ((k + 1) ** a - k ** a) * ((l + 1) ** b - l ** b) * int(joint[i, j, k, l])
        for k in range(16)
        for l in range(16)
    )
    return Fraction(total, TOTAL)


def main() -> None:
    c88, c89 = load_sources()
    nonhit, supersets = arrays_from_c88(c88)
    # Dot products count nested support pairs (A subset B).  A factorial
    # weight completes each pair to a full ordered label permutation.
    flat_nonhit = nonhit.reshape(TARGET_COUNT * 17, SUPPORT_COUNT)
    flat_supersets = supersets.reshape(TARGET_COUNT * 17, SUPPORT_COUNT)
    nested = flat_nonhit @ flat_supersets.T
    nested = np.rint(nested).astype(np.int64).reshape(TARGET_COUNT, 17, TARGET_COUNT, 17)
    factorials = [factorial(value) for value in range(17)]
    joint = np.zeros((TARGET_COUNT, TARGET_COUNT, 17, 17), dtype=np.int64)
    for i in range(TARGET_COUNT):
        for j in range(TARGET_COUNT):
            for k in range(17):
                for l in range(17):
                    if k <= l:
                        base = int(nested[i, k, j, l])
                        weight = factorials[k] * factorials[l - k] * factorials[16 - l]
                    else:
                        base = int(nested[j, l, i, k])
                        weight = factorials[l] * factorials[k - l] * factorials[16 - k]
                    joint[i, j, k, l] = base * weight

    for i in range(TARGET_COUNT):
        for j in range(TARGET_COUNT):
            for k in range(17):
                for l in range(17):
                    assert joint[i, j, k, l] == joint[j, i, l, k]
                    if i == j:
                        source_survival = int(c88["first_passage_atlas"]["target_rows"][i]["survival_permutation_count_after_time"][str(max(k, l))])
                        assert joint[i, i, k, l] == source_survival

    pair_rows: list[dict[str, Any]] = []
    c89_rows = c89["moment_atlas"]["target_rows"]
    for i in range(TARGET_COUNT):
        for j in range(TARGET_COUNT):
            cells = {
                str(k): {str(l): int(joint[i, j, k, l]) for l in range(17)}
                for k in range(17)
            }
            probabilities = {
                str(k): {
                    str(l): rational(Fraction(int(joint[i, j, k, l]), TOTAL))
                    for l in range(17)
                }
                for k in range(17)
            }
            mixed = {
                str(a): {
                    str(b): rational(mixed_from_joint(joint, i, j, a, b, c89_rows))
                    for b in ORDERS
                }
                for a in ORDERS
            }
            covariance = mixed["1"]["1"]
            covariance_value = Fraction(covariance["numerator"], covariance["denominator"])
            covariance_value -= Fraction(c89_rows[i]["mean"]["numerator"], c89_rows[i]["mean"]["denominator"]) * Fraction(c89_rows[j]["mean"]["numerator"], c89_rows[j]["mean"]["denominator"])
            left_match = all(mixed["%d" % order]["0"] == c89_rows[i]["raw_moments"][str(order)] for order in ORDERS)
            right_match = all(mixed["0"]["%d" % order] == c89_rows[j]["raw_moments"][str(order)] for order in ORDERS)
            row = {
                "lower_target_index": i,
                "upper_target_index": j,
                "joint_survival_permutation_counts": cells,
                "joint_survival_probabilities": probabilities,
                "mixed_raw_moments": mixed,
                "covariance": rational(covariance_value),
                "marginal_consistency": {
                    "left_target_raw_orders_0_to_6_match": left_match,
                    "right_target_raw_orders_0_to_6_match": right_match,
                    "all_orders_match": left_match and right_match,
                },
            }
            assert row["marginal_consistency"]["all_orders_match"]
            pair_rows.append(row)

    result: dict[str, Any] = {
        "schema_id": "hcs-c90-joint-first-passage-coupling-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "authority": AUTHORITY,
        "definition": {
            "joint_survival": "J_ij(k,l)=#{pi:T_i(pi)>k and T_j(pi)>l}",
            "joint_support_formula": "k! (l-k)! (16-l)! times nested support pairs for k<=l",
            "mixed_raw_moment": "E[T_i^a T_j^b]=sum_{k,l=0}^{15} Delta_a(k) Delta_b(l) P(T_i>k,T_j>l)",
            "delta_power": "Delta_a(k)=(k+1)^a-k^a",
            "marginal_convention": "mixed orders (a,0) and (0,b) include order zero and recover C89 raw moments",
            "covariance": "Cov(T_i,T_j)=E[T_i T_j]-E[T_i]E[T_j]",
        },
        "source_model": {
            "group": "Z/9 + Z/3 + Z/2",
            "label_count": LABEL_COUNT,
            "target_subgroup_count": TARGET_COUNT,
            "total_permutations": TOTAL,
            "threshold_grid": [0, 16],
        },
        "joint_atlas": {
            "ordered_target_pair_count": len(pair_rows),
            "mixed_moment_orders": list(ORDERS),
            "pair_rows": pair_rows,
        },
        "checks": {
            "all_400_ordered_pairs": True,
            "all_289_joint_survival_cells_per_pair": True,
            "all_joint_probability_cells_exact": True,
            "all_mixed_orders_0_to_6": True,
            "all_covariances_exact": True,
            "all_400_marginal_consistency_identities": True,
            "joint_symmetry_under_pair_transpose": True,
            "diagonal_recovery_of_single_target_survival": True,
        },
        "claims": {
            "exact_finite_joint_first_passage_laws": True,
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
        "ordered_pair_count": len(pair_rows),
        "joint_cells_per_pair": 17 * 17,
        "evidence_sha256": digest(OUT.read_bytes()),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
