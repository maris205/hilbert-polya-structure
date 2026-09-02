#!/usr/bin/env python3
"""Produce canonical exact evidence for the HCS-C302 Quicksort cost law."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c302_quicksort_evidence.json"
SOURCE = "83c058259c02707d004fca2d6b1a4ebaf5036094"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788307200


def canonical_hash(data: dict) -> str:
    body = dict(data); body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def rat(value: Fraction | int) -> str:
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def harmonic(n: int, power: int = 1) -> Fraction:
    return sum((Fraction(1, k**power) for k in range(1, n + 1)), Fraction())


def mean_formula(n: int) -> Fraction:
    return 2 * (n + 1) * harmonic(n) - 4 * n


def variance_formula(n: int) -> Fraction:
    return 7*n*n - 4*(n+1)**2*harmonic(n, 2) - 2*(n+1)*harmonic(n) + 13*n


def convolve(left: dict[int, Fraction], right: dict[int, Fraction]) -> dict[int, Fraction]:
    out: dict[int, Fraction] = {}
    for a, pa in left.items():
        for b, pb in right.items():
            out[a+b] = out.get(a+b, Fraction()) + pa*pb
    return out


def pgfs(n_max: int) -> list[dict[int, Fraction]]:
    laws: list[dict[int, Fraction]] = [{0: Fraction(1)}, {0: Fraction(1)}]
    for n in range(2, n_max + 1):
        law: dict[int, Fraction] = {}
        for j in range(n):
            for cost, probability in convolve(laws[j], laws[n-1-j]).items():
                shifted = cost + n - 1
                law[shifted] = law.get(shifted, Fraction()) + probability / n
        assert sum(law.values()) == 1
        laws.append(dict(sorted(law.items())))
    return laws[:n_max+1]


def raw_moment(law: dict[int, Fraction], order: int) -> Fraction:
    return sum((Fraction(cost**order) * probability for cost, probability in law.items()), Fraction())


def finite_rows(n_max: int = 12) -> tuple[list[dict], int]:
    laws = pgfs(n_max)
    rows = []
    coefficient_cells = 0
    for n, law in enumerate(laws):
        mean = raw_moment(law, 1)
        second = raw_moment(law, 2)
        third = raw_moment(law, 3)
        variance = second - mean*mean
        centered_third = third - 3*mean*second + 2*mean**3
        entries = []
        for cost, probability in law.items():
            permutation_count = probability * math.factorial(n)
            assert permutation_count.denominator == 1
            entries.append({
                "comparisons": cost,
                "numerator": probability.numerator,
                "denominator": probability.denominator,
                "permutation_count": permutation_count.numerator,
            })
        rows.append({
            "n": n,
            "coefficient_count": len(entries),
            "support_min": min(law),
            "support_max": max(law),
            "coefficients": entries,
            "probability_sum": rat(sum(law.values())),
            "permutation_count_sum": sum(item["permutation_count"] for item in entries),
            "raw_moment_1": rat(mean),
            "raw_moment_2": rat(second),
            "raw_moment_3": rat(third),
            "variance_from_coefficients": rat(variance),
            "third_centered_moment": rat(centered_third),
            "mean_formula": rat(mean_formula(n)),
            "variance_formula": rat(variance_formula(n)),
            "normalized_variance_n_plus_1": rat(variance / (n+1)**2),
            "normalized_third_centered_n_plus_1": rat(centered_third / (n+1)**3),
        })
        coefficient_cells += len(entries)
    return rows, coefficient_cells


def centered_recursion(n_max: int = 32) -> tuple[list[dict], int]:
    groups = []
    cells = 0
    for n in range(2, n_max + 1):
        rows = []
        for j in range(n):
            left = Fraction(j+1, n+1)
            right = Fraction(n-j, n+1)
            toll = Fraction(n-1) + mean_formula(j) + mean_formula(n-1-j) - mean_formula(n)
            toll /= n+1
            rows.append({
                "pivot_left_size": j,
                "left_coefficient": rat(left),
                "right_coefficient": rat(right),
                "coefficient_sum": rat(left+right),
                "centered_toll": rat(toll),
            })
            cells += 1
        mean_toll = sum(Fraction(row["centered_toll"]) for row in rows) / n
        square_average = sum(
            Fraction(row["left_coefficient"])**2 + Fraction(row["right_coefficient"])**2
            for row in rows
        ) / n
        toll_square_average = sum(Fraction(row["centered_toll"])**2 for row in rows) / n
        groups.append({
            "n": n,
            "pivot_count": n,
            "mean_centered_toll": rat(mean_toll),
            "coefficient_square_average": rat(square_average),
            "toll_square_average": rat(toll_square_average),
            "rows": rows,
        })
    return groups, cells


def asymptotic_diagnostics() -> list[dict]:
    limit = 7 - 2*math.pi**2/3
    rows = []
    for n in (8, 16, 32, 64, 128, 256):
        normalized = variance_formula(n) / (n+1)**2
        rows.append({
            "n": n,
            "normalized_variance_exact": rat(normalized),
            "normalized_variance_decimal_12": f"{float(normalized):.12f}",
            "limit_variance_decimal_12": f"{limit:.12f}",
            "absolute_error_decimal_12": f"{abs(float(normalized)-limit):.12f}",
        })
    return rows


def build_payload() -> dict:
    finite, coefficient_cells = finite_rows()
    centered, centered_cells = centered_recursion()
    payload = {
        "schema": "hcs-c302-quicksort-comparison-evidence-v1",
        "candidate_id": "HCS-C302",
        "obstruction_id": "HEN-O286",
        "title": "Exact Quicksort comparison costs and contraction limit",
        "evaluation_date": "2026-09-02",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator_authority_sha256": EVALUATOR,
        "model": {
            "input": "uniform random permutation of n distinct keys",
            "pivot": "first key, equivalently a pivot rule independent of values with uniform rank",
            "partition_cost": "exactly n-1 key comparisons",
            "total_cost": "key comparisons only",
            "base_cases": "X_0=X_1=0",
            "distributional_recurrence": "X_n =d X_{I_n}+X'_{n-1-I_n}+n-1 with I_n uniform on {0,...,n-1}",
        },
        "theorem": {
            "pgf": "G_n(z)=z^{n-1}/n sum_{j=0}^{n-1}G_j(z)G_{n-1-j}(z), G_0=G_1=1",
            "mean": "mu_n=2(n+1)H_n-4n",
            "variance": "v_n=7n^2-4(n+1)^2H_n^(2)-2(n+1)H_n+13n",
            "normalization": "Y_n=(X_n-mu_n)/(n+1)",
            "fixed_point": "Y =d UY_1+(1-U)Y_2+C(U)",
            "toll": "C(u)=1+2u log u+2(1-u)log(1-u), with 0 log 0=0",
            "convergence": "Y_n converges in quadratic Wasserstein distance, and under a recursive coupling in L^2, to the unique centered finite-variance fixed law",
            "limit_variance": "E[Y^2]=7-2*pi^2/3",
            "limit_third_moment": "E[Y^3]=16*zeta(3)-19>0",
            "non_gaussian": "the centered limit is nondegenerate and non-Gaussian",
        },
        "proof_certificates": {
            "recursive_independence": "conditional on pivot rank, the two relative subarray orders are independent uniform permutations",
            "variance_lane": "law of total variance plus the exact mean gives the all-n variance formula",
            "contraction": "E[U^2+(1-U)^2]=2/3, so the centered transform contracts squared d_2 by 2/3",
            "endogenous_l2": "orthogonal binary-tree toll levels satisfy E[Delta_r^2]=E[C(U)^2](2/3)^r, so their series realizes the unique fixed law in L2",
            "mixed_subproblem_closure": "on one iid-uniform binary tree, e_n<=sqrt(Q_n)+delta_n with Q_n=(2/n)sum_j((j+1)/(n+1))^2e_j^2, delta_n->0, and the cutoff limsup gives D<=sqrt(2/3)D",
            "third_moment_license": "the binary-tree toll series converges in L3 by conditional Rosenthal bounds using level sums (2/3)^r and (1/2)^r",
            "third_moment": "m3=(1/2)m3+3m2 integral C(u)(u^2+(1-u)^2)du+integral C(u)^3du",
            "positivity": "zeta(3)>sum_{k=1}^6 k^{-3}=28567/24000 gives 16*zeta(3)-19>67/1500>0",
        },
        "finite_pgf_regression": {
            "n_max": 12,
            "row_count": len(finite),
            "coefficient_cells": coefficient_cells,
            "rows": finite,
        },
        "centered_recursion_regression": {
            "n_min": 2,
            "n_max": 32,
            "group_count": len(centered),
            "pivot_rows": centered_cells,
            "groups": centered,
        },
        "limit_integrals": {
            "integral_C": "0",
            "integral_C_squared": "7/3-2*pi^2/9",
            "integral_C_times_branch_square": "1/18",
            "integral_C_cubed": "-32/3+pi^2/9+8*zeta(3)",
            "branch_square_integral": "2/3",
            "fixed_point_variance": "7-2*pi^2/3",
            "fixed_point_third_moment": "16*zeta(3)-19",
            "strict_positive_lower_bound": "67/1500",
        },
        "variance_limit_diagnostics": asymptotic_diagnostics(),
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall_verdict": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "obstruction": "recursive comparison-cost distributions have no arithmetic local carrier, primitive orbit ledger, intrinsic logarithmic prime clock, target determinant, divisor law, or same-clock self-adjoint zero lift",
        },
        "scope_flags": {
            "claims_target_arithmetic_local_data": False,
            "claims_target_euler_factors": False,
            "claims_root_number": False,
            "claims_automorphy": False,
            "claims_target_divisor_or_counting_law": False,
            "claims_target_functional_equation": False,
            "claims_target_zero_match": False,
            "claims_hilbert_polya_operator": False,
            "invokes_route_b": False,
        },
        "nonclaims": [
            "No priority is claimed for Quicksort, its comparison recurrence, limiting law, or contraction method.",
            "Finite PGFs are source probability polynomials, not target arithmetic determinants.",
            "No target arithmetic local datum, Euler factor, root number, automorphy, divisor law, functional equation, zero match, or Hilbert--Polya operator is asserted.",
        ],
        "collision_boundary": {
            "C291": "C291 owns random greedy dimer adsorption; C302 owns recursive permutation splitting and a non-Gaussian contraction fixed point.",
            "cost_warning": "swaps, assignments, recursion depth, wall-clock time, repeated keys, three-way partitioning, and sampled pivots are different models",
            "normalization_warning": "division by n has the same limit for n>=1 but is not the frozen finite recurrence, which divides by n+1",
        },
        "source_owner_tokens": [
            "doi:10.1093/comjnl/5.1.10",
            "NUMDAM:ITA_1989__23_3_335_0",
            "NUMDAM:ITA_1991__25_1_85_0",
        ],
        "regression_summary": {
            "finite_pgf_rows": len(finite),
            "pgf_coefficient_cells": coefficient_cells,
            "centered_pivot_rows": centered_cells,
            "variance_diagnostic_rows": 6,
            "all_probability_rows_normalized": True,
            "normalization_denominator": "n+1",
        },
    }
    payload["payload_sha256"] = canonical_hash(payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    data = build_payload()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {args.output}")
    print(f"payload_sha256={data['payload_sha256']}")
    print(f"pgf_rows={data['regression_summary']['finite_pgf_rows']}")
    print(f"pgf_coefficient_cells={data['regression_summary']['pgf_coefficient_cells']}")
    print(f"centered_pivot_rows={data['regression_summary']['centered_pivot_rows']}")


if __name__ == "__main__":
    main()
