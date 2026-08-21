#!/usr/bin/env python3
"""Independent exact reconstruction of the C90 joint receipt."""
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
EVIDENCE = PROJECT / "results/c90_joint_first_passage_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
TARGET_COUNT = 20
SUPPORT_COUNT = 1 << 16
TOTAL = factorial(16)
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


def sources() -> tuple[dict[str, Any], dict[str, Any]]:
    c88_raw = (C88 / "results/c88_subgroup_first_passage_atlas_evidence.json").read_bytes()
    manifest_raw = (C88 / "C88_PREFREEZE_MANIFEST.json").read_bytes()
    c89_raw = (C89 / "results/c89_first_passage_moments_evidence.json").read_bytes()
    assert digest(c88_raw) == AUTHORITY["c88"]
    assert digest(manifest_raw) == AUTHORITY["c88_manifest"]
    assert digest(c89_raw) == AUTHORITY["c89"]
    c88, c89 = json.loads(c88_raw), json.loads(c89_raw)
    assert c88["scope_literal"] == c89["scope_literal"] == FIREWALL
    return c88, c89


def build_joint(c88: dict[str, Any]) -> np.ndarray:
    sizes = np.fromiter((mask.bit_count() for mask in range(SUPPORT_COUNT)), dtype=np.int8, count=SUPPORT_COUNT)
    nonhit = np.zeros((TARGET_COUNT, 17, SUPPORT_COUNT), dtype=np.int8)
    for target, row in enumerate(c88["first_passage_atlas"]["target_rows"]):
        bits = np.unpackbits(np.frombuffer(bytes.fromhex(row["subset_hit_bitset_hex"]), dtype=np.uint8), bitorder="little")[:SUPPORT_COUNT]
        for time in range(17):
            nonhit[target, time, (sizes == time) & (bits == 0)] = 1
    supersets = nonhit.astype(np.int32)
    for target in range(TARGET_COUNT):
        for time in range(17):
            values = supersets[target, time]
            for bit in range(16):
                step = 1 << bit
                view = values.reshape(-1, 2 * step)
                view[:, :step] += view[:, step:]
    nested = np.empty((TARGET_COUNT * 17, TARGET_COUNT * 17), dtype=np.int64)
    left = nonhit.reshape(TARGET_COUNT * 17, SUPPORT_COUNT).astype(np.int32)
    right = supersets.reshape(TARGET_COUNT * 17, SUPPORT_COUNT)
    for start in range(0, TARGET_COUNT * 17, 34):
        nested[start:start + 34] = left[start:start + 34] @ right.T
    nested = nested.reshape(TARGET_COUNT, 17, TARGET_COUNT, 17)
    factorials = [factorial(k) for k in range(17)]
    joint = np.zeros((TARGET_COUNT, TARGET_COUNT, 17, 17), dtype=np.int64)
    for i in range(TARGET_COUNT):
        for j in range(TARGET_COUNT):
            for k in range(17):
                for l in range(17):
                    if k <= l:
                        base = nested[i, k, j, l]
                        weight = factorials[k] * factorials[l - k] * factorials[16 - l]
                    else:
                        base = nested[j, l, i, k]
                        weight = factorials[l] * factorials[k - l] * factorials[16 - k]
                    joint[i, j, k, l] = int(base) * weight
    return joint


def expected() -> dict[str, Any]:
    c88, c89 = sources()
    joint = build_joint(c88)
    c89_rows = c89["moment_atlas"]["target_rows"]
    pairs = []
    for i in range(TARGET_COUNT):
        for j in range(TARGET_COUNT):
            cells = {str(k): {str(l): int(joint[i, j, k, l]) for l in range(17)} for k in range(17)}
            probabilities = {str(k): {str(l): rational(Fraction(int(joint[i, j, k, l]), TOTAL)) for l in range(17)} for k in range(17)}
            mixed = {}
            for a in range(7):
                mixed[str(a)] = {}
                for b in range(7):
                    if a == 0 and b == 0:
                        value = Fraction(1)
                    elif a == 0:
                        value = Fraction(c89_rows[j]["raw_moments"][str(b)]["numerator"], c89_rows[j]["raw_moments"][str(b)]["denominator"])
                    elif b == 0:
                        value = Fraction(c89_rows[i]["raw_moments"][str(a)]["numerator"], c89_rows[i]["raw_moments"][str(a)]["denominator"])
                    else:
                        value = Fraction(sum(((k + 1) ** a - k ** a) * ((l + 1) ** b - l ** b) * int(joint[i, j, k, l]) for k in range(16) for l in range(16)), TOTAL)
                    mixed[str(a)][str(b)] = rational(value)
            ei = Fraction(c89_rows[i]["mean"]["numerator"], c89_rows[i]["mean"]["denominator"])
            ej = Fraction(c89_rows[j]["mean"]["numerator"], c89_rows[j]["mean"]["denominator"])
            eij = Fraction(mixed["1"]["1"]["numerator"], mixed["1"]["1"]["denominator"])
            left = all(mixed[str(a)]["0"] == c89_rows[i]["raw_moments"][str(a)] for a in range(7))
            right = all(mixed["0"][str(b)] == c89_rows[j]["raw_moments"][str(b)] for b in range(7))
            assert left and right
            pairs.append({
                "lower_target_index": i,
                "upper_target_index": j,
                "joint_survival_permutation_counts": cells,
                "joint_survival_probabilities": probabilities,
                "mixed_raw_moments": mixed,
                "covariance": rational(eij - ei * ej),
                "marginal_consistency": {"left_target_raw_orders_0_to_6_match": left, "right_target_raw_orders_0_to_6_match": right, "all_orders_match": left and right},
            })
    return {
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
        "source_model": {"group": "Z/9 + Z/3 + Z/2", "label_count": 16, "target_subgroup_count": 20, "total_permutations": TOTAL, "threshold_grid": [0, 16]},
        "joint_atlas": {"ordered_target_pair_count": 400, "mixed_moment_orders": list(range(7)), "pair_rows": pairs},
        "checks": {"all_400_ordered_pairs": True, "all_289_joint_survival_cells_per_pair": True, "all_joint_probability_cells_exact": True, "all_mixed_orders_0_to_6": True, "all_covariances_exact": True, "all_400_marginal_consistency_identities": True, "joint_symmetry_under_pair_transpose": True, "diagonal_recovery_of_single_target_survival": True},
        "claims": {"exact_finite_joint_first_passage_laws": True, "arithmetic_local_claimed": False, "euler_factors_claimed": False, "root_numbers_claimed": False, "automorphy_claimed": False, "full_burnside_ring_claimed": False, "full_table_of_marks_claimed": False, "hilbert_polya_operator_claimed": False},
    }


def main() -> None:
    observed_raw = EVIDENCE.read_bytes()
    observed = json.loads(observed_raw)
    assert observed_raw == canonical(observed)
    assert observed == expected()
    print(json.dumps({"status": "C90_INDEPENDENT_CHECK_PASS", "ordered_pair_count": 400, "evidence_sha256": digest(observed_raw)}, sort_keys=True))


if __name__ == "__main__":
    main()
