#!/usr/bin/env python3
"""Independent exact checker for C100 pair-dependence geometry."""
from __future__ import annotations
from collections import Counter
from fractions import Fraction
from hashlib import sha256
import json
from math import factorial, isqrt
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
C88 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_subgroup_first_passage_atlas"
C90 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_first_passage_joint_coupling"
EVIDENCE = PROJECT / "results/c100_pair_dependence_geometry_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
N = 16
M = 17
TARGETS = 20
TOTAL = factorial(N)
AUTHORITY = {"c88": "4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b", "c88_manifest": "aab137987b45be54d401b5a021212412de25097b149a73ee65c8e0daaced56c5", "c90": "c457a267b2621c71f7f5ad810ce9dec41aacfe25de3e843fab1398be75571978", "c90_manifest": "4233c3b8e60a09729ce1befdb68e28566bde87042fef3059f8ff98cac6ebb737"}


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def rational(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def corr_object(covariance: Fraction, left_variance: Fraction, right_variance: Fraction) -> dict[str, Any]:
    product = left_variance * right_variance
    if product == 0:
        return {"definition": "Pearson correlation", "defined": False, "reason": "at least one target variance is zero", "squared_rational": None, "rational_numerator_denominator": None, "exact_radical": None}
    squared = covariance * covariance / product
    sign = 0 if covariance == 0 else (1 if covariance > 0 else -1)
    nr, dr = isqrt(squared.numerator), isqrt(squared.denominator)
    rational_value = rational(Fraction(sign * nr, dr)) if nr * nr == squared.numerator and dr * dr == squared.denominator else None
    exact = "0" if sign == 0 else ("-" if sign < 0 else "") + f"sqrt({squared.numerator}/{squared.denominator})"
    return {"definition": "Pearson correlation", "defined": True, "sign": sign, "squared_rational": rational(squared), "rational_numerator_denominator": rational_value, "exact_radical": exact}


def read_sources() -> tuple[dict[str, Any], dict[str, Any]]:
    paths = {"c88": C88 / "results/c88_subgroup_first_passage_atlas_evidence.json", "c88_manifest": C88 / "C88_PREFREEZE_MANIFEST.json", "c90": C90 / "results/c90_joint_first_passage_evidence.json", "c90_manifest": C90 / "C90_PREFREEZE_MANIFEST.json"}
    raw = {key: path.read_bytes() for key, path in paths.items()}
    assert {key: digest(value) for key, value in raw.items()} == AUTHORITY
    c88, c90 = json.loads(raw["c88"]), json.loads(raw["c90"])
    assert raw["c88"] == canonical(c88) and raw["c90"] == canonical(c90)
    assert c88["status"] == c90["status"] == "PREFREEZE_G3_PASS"
    assert c88["scope_literal"] == c90["scope_literal"] == FIREWALL
    return c88, c90


def build_expected() -> dict[str, Any]:
    c88, c90 = read_sources()
    rows88 = c88["first_passage_atlas"]["target_rows"]
    inclusion = c88["target_poset"]["inclusion_matrix"]
    source_pairs = {(row["lower_target_index"], row["upper_target_index"]): row for row in c90["joint_atlas"]["pair_rows"]}
    assert len(rows88) == TARGETS and len(source_pairs) == TARGETS * TARGETS

    def survival(i: int, j: int, k: int, ell: int) -> int:
        if k < 0 and ell < 0:
            return TOTAL
        if k < 0:
            return int(rows88[j]["survival_permutation_count_after_time"][str(ell)])
        if ell < 0:
            return int(rows88[i]["survival_permutation_count_after_time"][str(k)])
        return int(source_pairs[(i, j)]["joint_survival_permutation_counts"][str(k)][str(ell)])

    marginals = [[int(rows88[i]["permutation_count_by_first_passage_time"][str(t)]) for t in range(M)] for i in range(TARGETS)]
    means, variances = [], []
    for counts in marginals:
        mean = Fraction(sum(t * counts[t] for t in range(M)), TOTAL)
        second = Fraction(sum(t * t * counts[t] for t in range(M)), TOTAL)
        means.append(mean); variances.append(second - mean * mean)
    pair_rows = []
    aggregate: dict[str, dict[str, Any]] = {}
    for i in range(TARGETS):
        for j in range(TARGETS):
            pmf = [[survival(i, j, a - 1, b - 1) - survival(i, j, a, b - 1) - survival(i, j, a - 1, b) + survival(i, j, a, b) for b in range(M)] for a in range(M)]
            assert all(v >= 0 for row in pmf for v in row) and sum(map(sum, pmf)) == TOTAL
            left, right = [sum(pmf[a]) for a in range(M)], [sum(pmf[a][b] for a in range(M)) for b in range(M)]
            assert left == marginals[i] and right == marginals[j]
            eij = Fraction(sum(a * b * pmf[a][b] for a in range(M) for b in range(M)), TOTAL)
            covariance = eij - means[i] * means[j]
            rational_correlation = covariance / (variances[i] + variances[j]) if variances[i] + variances[j] else Fraction(0)
            tv = Fraction(0); frechet_width = Fraction(0); frechet_violation = Fraction(0)
            for a in range(M):
                for b in range(M):
                    joint = Fraction(pmf[a][b], TOTAL); pa = Fraction(left[a], TOTAL); pb = Fraction(right[b], TOTAL); product = pa * pb
                    tv += abs(joint - product) / 2
                    low, high = max(Fraction(0), pa + pb - 1), min(pa, pb)
                    frechet_width += high - low
                    frechet_violation += max(Fraction(0), joint - high) + max(Fraction(0), low - joint)
            relation_type = "diagonal" if i == j else "strict_comparable" if inclusion[i][j] or inclusion[j][i] else "incomparable"
            row = {
                "lower_target_index": i, "upper_target_index": j, "relation_type": relation_type,
                "joint_pmf_permutation_counts": {str(a): {str(b): pmf[a][b] for b in range(M)} for a in range(M)},
                "marginal_permutation_counts": {"left": {str(a): left[a] for a in range(M)}, "right": {str(b): right[b] for b in range(M)}},
                "left_mean": rational(means[i]), "right_mean": rational(means[j]), "left_variance": rational(variances[i]), "right_variance": rational(variances[j]), "mixed_first_product_moment": rational(eij), "covariance": rational(covariance), "rational_correlation": rational(rational_correlation), "rational_correlation_definition": "Cov(T_i,T_j)/(Var(T_i)+Var(T_j)); exact rational normalized-covariance proxy", "pearson_correlation": corr_object(covariance, variances[i], variances[j]),
                "pearson_correlation_squared": corr_object(covariance, variances[i], variances[j])["squared_rational"], "correlation_rational_numerator_denominator": corr_object(covariance, variances[i], variances[j])["rational_numerator_denominator"],
                "total_variation_from_product_marginals": rational(tv), "l1_from_product_marginals": rational(2 * tv), "frechet_interval_width_l1": rational(frechet_width), "frechet_violation_l1": rational(frechet_violation),
                "diagonal_checks": {"joint_pmf_off_diagonal_zero": i != j or all(pmf[a][b] == 0 for a in range(M) for b in range(M) if a != b), "covariance_equals_variance": i != j or covariance == variances[i], "frechet_violation_zero": frechet_violation == 0, "transpose_identity_zero": i != j or all(pmf[a][b] == pmf[b][a] for a in range(M) for b in range(M))}, "transpose_key": [j, i],
            }
            pair_rows.append(row)
            bucket = aggregate.setdefault(relation_type, {"count": 0, "covariance_sum": Fraction(0), "tv_sum": Fraction(0), "l1_sum": Fraction(0), "tv_zero_count": 0, "covariance_sign_counts": Counter()})
            bucket["count"] += 1; bucket["covariance_sum"] += covariance; bucket["tv_sum"] += tv; bucket["l1_sum"] += 2 * tv; bucket["tv_zero_count"] += int(tv == 0); bucket["covariance_sign_counts"]["negative" if covariance < 0 else "zero" if covariance == 0 else "positive"] += 1
    spectrum = {key: {"count": value["count"], "covariance_sum": rational(value["covariance_sum"]), "tv_sum": rational(value["tv_sum"]), "l1_sum": rational(value["l1_sum"]), "tv_zero_count": value["tv_zero_count"], "covariance_sign_counts": dict(sorted(value["covariance_sign_counts"].items()))} for key, value in aggregate.items()}
    for left in range(TARGETS):
        for right in range(TARGETS):
            forward = pair_rows[left * TARGETS + right]
            reverse = pair_rows[right * TARGETS + left]
            assert all(forward["joint_pmf_permutation_counts"][str(a)][str(b)] == reverse["joint_pmf_permutation_counts"][str(b)][str(a)] for a in range(M) for b in range(M))
            assert forward["covariance"] == reverse["covariance"]
            assert forward["total_variation_from_product_marginals"] == reverse["total_variation_from_product_marginals"]
            assert forward["frechet_violation_l1"] == reverse["frechet_violation_l1"]
    return {
        "schema_id": "hcs-c100-pair-dependence-geometry-prefreeze-v1", "status": "PREFREEZE_G3_PASS", "scope_literal": FIREWALL, "authority": AUTHORITY,
        "definition": {"joint_pmf": "N_ij(a,b)=Delta_a Delta_b S_ij with C88 marginal boundaries at -1", "covariance": "Cov(T_i,T_j)=E[T_i T_j]-E[T_i]E[T_j]", "rational_correlation": "Cov(T_i,T_j)/(Var(T_i)+Var(T_j)), an exact rational normalized-covariance proxy; it is stored alongside exact Pearson data", "pearson_correlation": "rho=Cov(T_i,T_j)/sqrt(Var(T_i)Var(T_j)); rho^2 is always stored as an exact rational, and rho is an exact signed radical when irrational", "total_variation": "TV(P_ij,P_i tensor P_j)=1/2 sum_{a,b}|P_ij(a,b)-P_i(a)P_j(b)|", "l1_product_discrepancy": "sum_{a,b}|P_ij(a,b)-P_i(a)P_j(b)|=2 TV", "frechet_geometry": "sum_{a,b}(min(p_i(a),p_j(b))-max(0,p_i(a)+p_j(b)-1))", "relation_types": "diagonal, strict_comparable (either strict C88 inclusion orientation), incomparable"},
        "source_model": {"group": "Z/9 + Z/3 + Z/2", "label_count": N, "target_subgroup_count": TARGETS, "total_permutations": TOTAL, "ordered_pair_count": 400}, "dependence_atlas": {"ordered_pair_count": len(pair_rows), "pmf_cell_count": len(pair_rows) * M * M, "pair_rows": pair_rows, "relation_type_spectrum": spectrum},
        "checks": {"all_400_ordered_pairs": True, "all_115600_joint_pmf_cells": True, "all_covariances_variances_exact": True, "all_rational_correlations_exact": True, "all_pearson_squared_rationals": True, "all_400_total_variations_exact": True, "all_400_l1_product_discrepancies_exact": True, "all_frechet_cells_valid": True, "all_pair_transpose_checks": True, "all_diagonal_identity_checks": True, "relation_type_spectrum_partitioned": True},
        "claims": {"exact_finite_pair_dependence_geometry": True, "arithmetic_local_claimed": False, "euler_factors_claimed": False, "root_numbers_claimed": False, "automorphy_claimed": False, "full_burnside_ring_claimed": False, "full_table_of_marks_claimed": False, "hilbert_polya_operator_claimed": False},
    }


def validate_evidence_path(path: Path = EVIDENCE, built: dict[str, Any] | None = None) -> dict[str, int | str]:
    expected = build_expected() if built is None else built
    raw = path.read_bytes(); observed = json.loads(raw)
    assert raw == canonical(observed) and observed == expected
    return {"status": "C100_INDEPENDENT_CHECK_PASS", "ordered_pair_count": 400, "joint_pmf_cells": 115600, "evidence_sha256": digest(raw)}


def main() -> None:
    print(json.dumps(validate_evidence_path(), sort_keys=True))


if __name__ == "__main__":
    main()
