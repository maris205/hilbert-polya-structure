#!/usr/bin/env python3
"""Independent exact checker for C95; it rebuilds the finite-difference atlas."""

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
C90 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_first_passage_joint_coupling"
EVIDENCE = PROJECT / "results/c95_comparable_delay_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
N = 16
M = 17
TARGETS = 20
TOTAL = factorial(N)
AUTHORITY = {
    "c88": "4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b",
    "c88_manifest": "aab137987b45be54d401b5a021212412de25097b149a73ee65c8e0daaced56c5",
    "c90": "c457a267b2621c71f7f5ad810ce9dec41aacfe25de3e843fab1398be75571978",
    "c90_manifest": "4233c3b8e60a09729ce1befdb68e28566bde87042fef3059f8ff98cac6ebb737",
}


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def rational(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def read_sources() -> tuple[dict[str, Any], dict[str, Any]]:
    paths = {
        "c88": C88 / "results/c88_subgroup_first_passage_atlas_evidence.json",
        "c88_manifest": C88 / "C88_PREFREEZE_MANIFEST.json",
        "c90": C90 / "results/c90_joint_first_passage_evidence.json",
        "c90_manifest": C90 / "C90_PREFREEZE_MANIFEST.json",
    }
    raw = {key: path.read_bytes() for key, path in paths.items()}
    assert {key: digest(value) for key, value in raw.items()} == AUTHORITY
    c88, c90 = json.loads(raw["c88"]), json.loads(raw["c90"])
    assert raw["c88"] == canonical(c88)
    assert raw["c90"] == canonical(c90)
    assert c88["scope_literal"] == c90["scope_literal"] == FIREWALL
    assert c88["status"] == c90["status"] == "PREFREEZE_G3_PASS"
    return c88, c90


def build_expected() -> tuple[dict[str, Any], dict[str, int]]:
    c88, c90 = read_sources()
    rows = c88["first_passage_atlas"]["target_rows"]
    assert len(rows) == TARGETS
    inclusion = c88["target_poset"]["inclusion_matrix"]
    pairs = [(i, j) for i in range(TARGETS) for j in range(TARGETS) if inclusion[i][j]]
    assert len(pairs) == 102
    source_pairs = {(row["lower_target_index"], row["upper_target_index"]): row for row in c90["joint_atlas"]["pair_rows"]}
    assert len(source_pairs) == 400

    def s(i: int, j: int, k: int, ell: int) -> int:
        if k < 0 and ell < 0:
            return TOTAL
        if k < 0:
            return int(rows[j]["survival_permutation_count_after_time"][str(ell)])
        if ell < 0:
            return int(rows[i]["survival_permutation_count_after_time"][str(k)])
        return int(source_pairs[(i, j)]["joint_survival_permutation_counts"][str(k)][str(ell)])

    pair_rows: list[dict[str, Any]] = []
    for i, j in pairs:
        pmf = [[s(i, j, a - 1, b - 1) - s(i, j, a, b - 1) - s(i, j, a - 1, b) + s(i, j, a, b) for b in range(M)] for a in range(M)]
        assert all(v >= 0 for row in pmf for v in row)
        assert sum(map(sum, pmf)) == TOTAL
        assert all(pmf[a][b] == 0 for a in range(M) for b in range(M) if a > b)
        left = [sum(pmf[a]) for a in range(M)]
        right = [sum(pmf[a][b] for a in range(M)) for b in range(M)]
        left_expected = [int(rows[i]["permutation_count_by_first_passage_time"][str(a)]) for a in range(M)]
        right_expected = [int(rows[j]["permutation_count_by_first_passage_time"][str(b)]) for b in range(M)]
        assert left == left_expected and right == right_expected
        for k in range(M):
            for ell in range(M):
                assert sum(pmf[a][b] for a in range(k + 1, M) for b in range(ell + 1, M)) == s(i, j, k, ell)
        delays = [sum(pmf[a][a + d] for a in range(M - d)) for d in range(M)]
        mean = Fraction(sum(d * x for d, x in enumerate(delays)), TOTAL)
        second = Fraction(sum(d * d * x for d, x in enumerate(delays)), TOTAL)
        cond: list[dict[str, Any]] = []
        for t in range(M):
            denominator = left[t]
            counts = [pmf[t][t + d] if t + d < M else 0 for d in range(M)]
            assert sum(counts) == denominator
            cm = Fraction(sum(d * x for d, x in enumerate(counts)), denominator) if denominator else Fraction(0)
            cs = Fraction(sum(d * d * x for d, x in enumerate(counts)), denominator) if denominator else Fraction(0)
            cond.append({
                "lower_first_passage_time": t,
                "conditioning_permutation_count": denominator,
                "conditioning_probability": rational(Fraction(denominator, TOTAL)),
                "delay_permutation_count_by_delta": {str(d): counts[d] for d in range(M)},
                "conditional_delay_probability_by_delta": {str(d): rational(Fraction(counts[d], denominator)) if denominator else rational(Fraction(0)) for d in range(M)},
                "conditional_mean_delay": rational(cm),
                "conditional_second_moment_delay": rational(cs),
                "conditional_variance_delay": rational(cs - cm * cm),
            })
        pair_rows.append({
            "lower_target_index": i,
            "upper_target_index": j,
            "lower_target_order": rows[i]["target_subgroup_order"],
            "upper_target_order": rows[j]["target_subgroup_order"],
            "comparable_relation_certified": True,
            "joint_pmf_permutation_counts": {str(a): {str(b): pmf[a][b] for b in range(M)} for a in range(M)},
            "joint_pmf_probabilities": {str(a): {str(b): rational(Fraction(pmf[a][b], TOTAL)) for b in range(M)} for a in range(M)},
            "target_time_order": {"pointwise": True, "violation_permutation_count": 0},
            "delay_definition": "D_ij=T_j-T_i, conditionally indexed by T_i=t",
            "delay_permutation_count_by_delta": {str(d): delays[d] for d in range(M)},
            "delay_probability_by_delta": {str(d): rational(Fraction(delays[d], TOTAL)) for d in range(M)},
            "delay_mean": rational(mean),
            "delay_second_moment": rational(second),
            "delay_variance": rational(second - mean * mean),
            "conditional_delay_rows_given_lower_time": cond,
            "marginal_identity": {
                "left_pmf_matches_c88": True,
                "right_pmf_matches_c88": True,
                "left_survival_matches_c88": True,
                "right_survival_matches_c88": True,
            },
        })
    expected = {
        "schema_id": "hcs-c95-comparable-first-passage-delay-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "authority": AUTHORITY,
        "definition": {
            "random_object": "uniform permutation of the sixteen frozen C88 labels",
            "target_time": "T_i=min{k:H_i is hit by the first k labels}",
            "joint_survival": "S_ij(k,l)=# {T_i>k and T_j>l} from C90, with C88 marginal boundaries at -1",
            "finite_difference": "N_ij(a,b)=S(a-1,b-1)-S(a,b-1)-S(a-1,b)+S(a,b)",
            "comparable_scope": "all C88 inclusion-matrix ordered pairs, including reflexive pairs",
            "delay": "D_ij=T_j-T_i, with conditional law P(D=d | T_i=t)",
            "conditional_variance": "E[D^2|T_i=t]-E[D|T_i=t]^2",
            "trivial_target": "C88 target 0 has T_0=0 for every permutation",
        },
        "source_model": {"group": "Z/9 + Z/3 + Z/2", "label_count": N, "target_subgroup_count": TARGETS, "total_permutations": TOTAL, "comparable_ordered_pair_count_including_reflexive": 102, "threshold_grid": [0, N]},
        "delay_atlas": {"ordered_pair_count": len(pair_rows), "delay_support": list(range(M)), "pair_rows": pair_rows},
        "checks": {
            "all_102_comparable_ordered_pairs_including_reflexive": True,
            "all_102_finite_difference_pmfs_nonnegative_and_normalized": True,
            "all_102_target_time_orders_certified": True,
            "all_102_delay_conditional_rows": True,
            "all_102_c90_survival_cells_recovered": True,
            "all_204_c88_marginal_pmf_identities": True,
        },
        "claims": {"exact_finite_comparable_delay_laws": True, "arithmetic_local_claimed": False, "euler_factors_claimed": False, "root_numbers_claimed": False, "automorphy_claimed": False, "full_burnside_ring_claimed": False, "full_table_of_marks_claimed": False, "hilbert_polya_operator_claimed": False},
    }
    return expected, {"pair_count": len(pair_rows), "pmf_cells": len(pair_rows) * M * M}


def validate_evidence_path(path: Path = EVIDENCE, built: dict[str, Any] | None = None) -> dict[str, int | str]:
    expected, diagnostics = build_expected() if built is None else (built, {})
    raw = path.read_bytes()
    observed = json.loads(raw)
    assert raw == canonical(observed)
    assert observed == expected
    return {"status": "C95_INDEPENDENT_CHECK_PASS", **diagnostics, "evidence_sha256": digest(raw)}


def main() -> None:
    print(json.dumps(validate_evidence_path(), sort_keys=True))


if __name__ == "__main__":
    main()
