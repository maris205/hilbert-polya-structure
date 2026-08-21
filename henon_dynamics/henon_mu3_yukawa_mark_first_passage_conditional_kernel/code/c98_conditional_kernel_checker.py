#!/usr/bin/env python3
"""Independent exact checker for C98 conditional first-passage kernels."""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
from hashlib import sha256
import json
from math import factorial
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c98_conditional_kernel_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
N, TIMES, TARGETS, TOTAL = 16, 17, 20, factorial(16)
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
    base = ROOT / "henon_dynamics"
    paths = {
        "c88": base / "henon_mu3_yukawa_mark_subgroup_first_passage_atlas/results/c88_subgroup_first_passage_atlas_evidence.json",
        "c88_manifest": base / "henon_mu3_yukawa_mark_subgroup_first_passage_atlas/C88_PREFREEZE_MANIFEST.json",
        "c90": base / "henon_mu3_yukawa_mark_first_passage_joint_coupling/results/c90_joint_first_passage_evidence.json",
        "c90_manifest": base / "henon_mu3_yukawa_mark_first_passage_joint_coupling/C90_PREFREEZE_MANIFEST.json",
    }
    raw = {name: path.read_bytes() for name, path in paths.items()}
    assert {name: digest(value) for name, value in raw.items()} == AUTHORITY
    c88, c90 = json.loads(raw["c88"]), json.loads(raw["c90"])
    assert raw["c88"] == canonical(c88) and raw["c90"] == canonical(c90)
    assert c88["scope_literal"] == c90["scope_literal"] == FIREWALL
    return c88, c90


def build_expected() -> tuple[dict[str, Any], dict[str, int]]:
    c88, c90 = read_sources()
    rows88 = c88["first_passage_atlas"]["target_rows"]
    inclusion = c88["target_poset"]["inclusion_matrix"]
    source_pairs = {(row["lower_target_index"], row["upper_target_index"]): row for row in c90["joint_atlas"]["pair_rows"]}
    assert len(rows88) == TARGETS and len(source_pairs) == 400
    marginals = [[int(row["permutation_count_by_first_passage_time"][str(time)]) for time in range(TIMES)] for row in rows88]
    survivals = [[int(row["survival_permutation_count_after_time"][str(time)]) for time in range(TIMES)] for row in rows88]

    # Source-level cross-check independent of the C90 finite-difference use:
    # at equal thresholds k, both nonhit events concern the same size-k prefix.
    # Rebuild all 20*20*17 such cells directly from C88 packed support bits.
    layer_masks = [0] * TIMES
    for support in range(1 << N):
        layer_masks[support.bit_count()] |= 1 << support
    hit_integers = [int.from_bytes(bytes.fromhex(row["subset_hit_bitset_hex"]), "little") for row in rows88]
    factorials = [factorial(value) for value in range(TIMES)]
    for left in range(TARGETS):
        for right in range(TARGETS):
            source = source_pairs[(left, right)]["joint_survival_permutation_counts"]
            for time in range(TIMES):
                subset_count = ((~hit_integers[left]) & (~hit_integers[right]) & layer_masks[time]).bit_count()
                direct = subset_count * factorials[time] * factorials[N - time]
                assert direct == int(source[str(time)][str(time)])

    def s(left: int, right: int, a: int, b: int) -> int:
        if a < 0 and b < 0:
            return TOTAL
        if a < 0:
            return survivals[right][b]
        if b < 0:
            return survivals[left][a]
        return int(source_pairs[(left, right)]["joint_survival_permutation_counts"][str(a)][str(b)])

    def relation(left: int, right: int) -> str:
        if left == right:
            return "diagonal"
        if inclusion[left][right]:
            return "forward_comparable"
        if inclusion[right][left]:
            return "reverse_comparable"
        return "incomparable"

    pmfs: dict[tuple[int, int], list[list[int]]] = {}
    for left in range(TARGETS):
        for right in range(TARGETS):
            pmf = [[s(left, right, a - 1, b - 1) - s(left, right, a, b - 1) - s(left, right, a - 1, b) + s(left, right, a, b) for b in range(TIMES)] for a in range(TIMES)]
            assert all(v >= 0 for row in pmf for v in row) and sum(map(sum, pmf)) == TOTAL
            assert [sum(row) for row in pmf] == marginals[left]
            assert [sum(pmf[a][b] for a in range(TIMES)) for b in range(TIMES)] == marginals[right]
            pmfs[(left, right)] = pmf

    rows: list[dict[str, Any]] = []
    attainable = empty = 0
    for left in range(TARGETS):
        for right in range(TARGETS):
            pmf = pmfs[(left, right)]
            reverse = pmfs[(right, left)]
            assert all(pmf[a][b] == reverse[b][a] for a in range(TIMES) for b in range(TIMES))
            conditional: list[dict[str, Any]] = []
            means: list[Fraction | None] = []
            variances: list[Fraction | None] = []
            for a in range(TIMES):
                denominator = marginals[left][a]
                counts = pmf[a]
                assert sum(counts) == denominator
                if denominator:
                    probabilities = {str(b): rational(Fraction(counts[b], denominator)) for b in range(TIMES)}
                    mean = Fraction(sum(b * counts[b] for b in range(TIMES)), denominator)
                    second = Fraction(sum(b * b * counts[b] for b in range(TIMES)), denominator)
                    variance = second - mean * mean
                    attainable += 1
                else:
                    probabilities = None
                    mean = second = variance = None
                    empty += 1
                means.append(mean)
                variances.append(variance)
                conditional.append({
                    "conditioning_first_passage_time": a,
                    "conditioning_permutation_count": denominator,
                    "joint_permutation_count_by_response_time": {str(b): counts[b] for b in range(TIMES)},
                    "conditional_probability_by_response_time": probabilities,
                    "conditional_mean_response_time": rational(mean) if mean is not None else None,
                    "conditional_second_moment_response_time": rational(second) if second is not None else None,
                    "conditional_variance_response_time": rational(variance) if variance is not None else None,
                })
            response_mean = Fraction(sum(b * marginals[right][b] for b in range(TIMES)), TOTAL)
            response_second = Fraction(sum(b * b * marginals[right][b] for b in range(TIMES)), TOTAL)
            response_variance = response_second - response_mean * response_mean
            tower_mean = sum((Fraction(marginals[left][a], TOTAL) * means[a] for a in range(TIMES) if means[a] is not None), Fraction(0))
            expected_variance = sum((Fraction(marginals[left][a], TOTAL) * variances[a] for a in range(TIMES) if variances[a] is not None), Fraction(0))
            variance_mean = sum((Fraction(marginals[left][a], TOTAL) * (means[a] - response_mean) ** 2 for a in range(TIMES) if means[a] is not None), Fraction(0))
            assert tower_mean == response_mean
            assert expected_variance + variance_mean == response_variance
            diagonal = None
            if left == right:
                diagonal = all(pmf[a][b] == (marginals[left][a] if a == b else 0) for a in range(TIMES) for b in range(TIMES))
                assert diagonal
            rows.append({
                "conditioning_target_index": left,
                "response_target_index": right,
                "relation_type": relation(left, right),
                "joint_first_passage_permutation_counts": {str(a): {str(b): pmf[a][b] for b in range(TIMES)} for a in range(TIMES)},
                "conditioning_marginal_permutation_counts": {str(a): marginals[left][a] for a in range(TIMES)},
                "response_marginal_permutation_counts": {str(b): marginals[right][b] for b in range(TIMES)},
                "conditional_rows": conditional,
                "tower_identities": {
                    "kernel_recovered_response_expectation": rational(tower_mean),
                    "c88_response_expectation": rational(response_mean),
                    "expected_conditional_variance": rational(expected_variance),
                    "variance_of_conditional_mean": rational(variance_mean),
                    "c88_response_variance": rational(response_variance),
                    "total_expectation_verified": True,
                    "total_variance_verified": True,
                },
                "bayes_reverse_identity": {"reverse_ordered_pair": [right, left], "joint_transpose_verified": True, "all_289_cell_balances_verified": True},
                "diagonal_kernel_is_identity": diagonal,
            })

    expected = {
        "schema_id": "hcs-c98-first-passage-conditional-kernel-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "authority": AUTHORITY,
        "definition": {
            "conditional_kernel": "K_ij(a,b)=P(T_j=b | T_i=a) for every nonempty conditioning row",
            "empty_row_convention": "if P(T_i=a)=0, the conditional probabilities and moments are null rather than assigned a law",
            "joint_recovery": "N_ij(a,b)=S(a-1,b-1)-S(a,b-1)-S(a-1,b)+S(a,b), with C88 marginal boundaries",
            "bayes_cell_balance": "P(T_i=a)K_ij(a,b)=P(T_j=b)K_ji(b,a)=N_ij(a,b)/16!",
            "total_expectation": "E[E(T_j|T_i)]=E(T_j)",
            "total_variance": "E[Var(T_j|T_i)]+Var(E[T_j|T_i])=Var(T_j)",
        },
        "source_model": {"group": "Z/9 + Z/3 + Z/2", "label_count": N, "target_subgroup_count": TARGETS, "total_permutations": TOTAL, "ordered_target_pair_count": 400, "time_grid": [0, N]},
        "conditional_kernel_atlas": {
            "ordered_pair_count": len(rows),
            "candidate_conditioning_row_count": len(rows) * TIMES,
            "attainable_conditioning_row_count": attainable,
            "empty_conditioning_row_count": empty,
            "relation_type_spectrum": dict(sorted(Counter(row["relation_type"] for row in rows).items())),
            "pair_rows": rows,
        },
        "checks": {
            "all_400_joint_pmfs_nonnegative_and_normalized": True,
            "all_800_c88_marginals_recovered": True,
            "all_attainable_conditional_rows_normalized": True,
            "all_empty_conditional_rows_are_null": True,
            "all_400_total_expectation_identities": True,
            "all_400_total_variance_identities": True,
            "all_115600_bayes_cell_balances": True,
            "all_20_diagonal_kernels_are_identity": True,
        },
        "claims": {
            "exact_finite_conditional_first_passage_kernels": True,
            "arithmetic_local_claimed": False,
            "euler_factors_claimed": False,
            "root_numbers_claimed": False,
            "automorphy_claimed": False,
            "full_burnside_ring_claimed": False,
            "full_table_of_marks_claimed": False,
            "hilbert_polya_operator_claimed": False,
        },
    }
    return expected, {"ordered_pair_count": len(rows), "attainable_conditioning_rows": attainable, "empty_conditioning_rows": empty, "c88_synchronous_cells_rebuilt": TARGETS * TARGETS * TIMES}


def validate_evidence_path(path: Path = EVIDENCE, built: dict[str, Any] | None = None) -> dict[str, Any]:
    expected, diagnostics = build_expected() if built is None else (built, {})
    raw = path.read_bytes()
    observed = json.loads(raw)
    assert raw == canonical(observed)
    assert observed == expected
    return {"status": "C98_INDEPENDENT_CHECK_PASS", **diagnostics, "evidence_sha256": digest(raw)}


def main() -> None:
    print(json.dumps(validate_evidence_path(), sort_keys=True))


if __name__ == "__main__":
    main()
