#!/usr/bin/env python3
"""Produce the exact HCS-C182 periodic box--ball certificate.

The all-parameter statements are theorems.  The finite ledger is deliberately
labelled as a regression sentinel rather than as their proof.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from functools import reduce
from hashlib import sha256
from itertools import combinations, product
import json
from math import comb, gcd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c182_periodic_bbs_evidence.json"
SOURCE_COMMIT = "bbb809ee198bc9ad5f196383baab1e3d9de38e43"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
L_MAX = 14
FIXED_N_MAX = 12


def canonical_bytes(data: dict) -> bytes:
    body = dict(data)
    body.pop("payload_sha256", None)
    return json.dumps(
        body, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode()


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n: int) -> int:
    if n == 1:
        return 1
    sign = 1
    prime = 2
    remaining = n
    while prime * prime <= remaining:
        if remaining % prime == 0:
            remaining //= prime
            if remaining % prime == 0:
                return 0
            sign = -sign
            while remaining % prime == 0:
                remaining //= prime
        prime += 1
    if remaining > 1:
        sign = -sign
    return sign


def lcm(a: int, b: int) -> int:
    return abs(a // gcd(a, b) * b) if a and b else 0


def determinant(matrix: list[list[int]]) -> int:
    """Fraction-free Bareiss determinant, with the empty determinant equal to 1."""
    n = len(matrix)
    if n == 0:
        return 1
    a = [row[:] for row in matrix]
    sign = 1
    previous = 1
    for k in range(n - 1):
        pivot_row = next((r for r in range(k, n) if a[r][k]), None)
        if pivot_row is None:
            return 0
        if pivot_row != k:
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                if numerator % previous:
                    raise ArithmeticError("Bareiss non-exact division")
                a[i][j] = numerator // previous
        previous = pivot
    return sign * a[n - 1][n - 1]


def minor(matrix: list[list[int]], rows: tuple[int, ...], cols: tuple[int, ...]) -> int:
    return determinant([[matrix[i][j] for j in cols] for i in rows])


def smith_invariants(matrix: list[list[int]]) -> list[int]:
    """Return nonzero Smith factors via determinantal divisors."""
    row_count = len(matrix)
    col_count = len(matrix[0]) if row_count else 0
    rank_bound = min(row_count, col_count)
    previous = 1
    result: list[int] = []
    for size in range(1, rank_bound + 1):
        delta = 0
        for rows in combinations(range(row_count), size):
            for cols in combinations(range(col_count), size):
                delta = gcd(delta, abs(minor(matrix, rows, cols)))
        if delta == 0:
            break
        if delta % previous:
            raise ArithmeticError("invalid determinantal divisor chain")
        result.append(delta // previous)
        previous = delta
    return result


def partitions(total: int, ceiling: int | None = None) -> list[tuple[int, ...]]:
    if total == 0:
        return [()]
    if ceiling is None or ceiling > total:
        ceiling = total
    answer: list[tuple[int, ...]] = []
    for first in range(ceiling, 0, -1):
        for tail in partitions(total - first, first):
            answer.append((first,) + tail)
    return answer


def multiplicities(parts: tuple[int, ...]) -> dict[int, int]:
    result: dict[int, int] = {}
    for part in parts:
        result[part] = result.get(part, 0) + 1
    return dict(sorted(result.items()))


def vacancy(L: int, content: dict[int, int], j: int) -> int:
    return L - 2 * sum(min(j, k) * count for k, count in content.items())


def lambda_exact(m: int, p: int, alpha: int) -> int:
    common = gcd(m, p)
    value = 0
    for beta in divisors(common):
        if beta % alpha == 0:
            value += mobius(beta // alpha) * comb(
                (p + m) // beta - 1, m // beta - 1
            )
    return value


def f_matrix(
    support: list[int], content: dict[int, int], vacancies: dict[int, int], alpha: list[int]
) -> list[list[int]]:
    answer = []
    for j in support:
        row = []
        for position, k in enumerate(support):
            numerator = (vacancies[k] if j == k else 0) + 2 * min(j, k) * content[k]
            if numerator % alpha[position]:
                raise ArithmeticError("nonintegral KTT period matrix")
            row.append(numerator // alpha[position])
        answer.append(row)
    return answer


def translation_order(matrix: list[list[int]], h: list[int]) -> tuple[int, list[int]]:
    """Order of h in Z^s/FZ^s from augmented Smith determinantal divisors."""
    if not matrix:
        return 1, []
    det_f = abs(determinant(matrix))
    augmented = [row + [h[i]] for i, row in enumerate(matrix)]
    augmented_smith = smith_invariants(augmented)
    quotient_index = reduce(lambda x, y: x * y, augmented_smith, 1)
    if quotient_index <= 0 or det_f % quotient_index:
        raise ArithmeticError("invalid augmented Smith index")
    return det_f // quotient_index, augmented_smith


def cycle_rows(cycle_points: dict[int, int]) -> list[dict]:
    rows = []
    for order, points in sorted(cycle_points.items()):
        if points % order:
            raise ArithmeticError("periodic point count is not divisible by orbit length")
        rows.append({"order": order, "points": points, "cycles": points // order})
    return rows


def fixed_rows(cycle_points: dict[int, int]) -> list[dict]:
    return [
        {
            "n": n,
            "fixed_points": sum(points for order, points in cycle_points.items() if n % order == 0),
        }
        for n in range(1, FIXED_N_MAX + 1)
    ]


def evolution_record(l_value: int, cycle_points: dict[int, int]) -> dict:
    cycles = cycle_rows(cycle_points)
    return {
        "l": l_value,
        "cycle_spectrum": cycles,
        "fixed_point_prefix": fixed_rows(cycle_points),
        "artin_mazur_zeta_factors": [
            {"degree": row["order"], "exponent": -row["cycles"]} for row in cycles
        ],
        "koopman_determinant_factors": [
            {"degree": row["order"], "exponent": row["cycles"]} for row in cycles
        ],
    }


def build_level(L: int, parts: tuple[int, ...], l_values: list[int]) -> dict:
    M = sum(parts)
    content = multiplicities(parts)
    support = list(content)
    vacancies = {j: vacancy(L, content, j) for j in support}
    if any(value < 0 for value in vacancies.values()):
        raise ArithmeticError("negative vacancy in admissible regime")
    key = "+".join(f"{j}^{content[j]}" for j in support) if support else "vacuum"

    sector_records: list[dict] = []
    candidates = 1
    if support:
        alpha_ranges = [divisors(gcd(content[j], vacancies[j])) for j in support]
        candidates = reduce(lambda x, y: x * y, (len(values) for values in alpha_ranges), 1)
    else:
        alpha_ranges = []

    alpha_products = product(*alpha_ranges) if support else [()]
    level_cycles = {l_value: {} for l_value in l_values}
    for alpha_tuple in alpha_products:
        alpha = list(alpha_tuple)
        lambda_counts = [
            lambda_exact(content[j], vacancies[j], alpha[position])
            for position, j in enumerate(support)
        ]
        if any(value == 0 for value in lambda_counts):
            continue
        factors = [
            lambda_counts[position] // (content[j] // alpha[position])
            for position, j in enumerate(support)
        ]
        if any(
            lambda_counts[position] % (content[j] // alpha[position])
            for position, j in enumerate(support)
        ):
            raise ArithmeticError("nonintegral KTT sector multiplicity")
        component_multiplicity = reduce(lambda x, y: x * y, factors, 1)
        matrix = f_matrix(support, content, vacancies, alpha)
        det_f = abs(determinant(matrix))
        smith = smith_invariants(matrix)
        if reduce(lambda x, y: x * y, smith, 1) != det_f:
            raise ArithmeticError("Smith factors do not recover determinant")
        translations = []
        for l_value in l_values:
            h = [min(j, l_value) for j in support]
            order, augmented_smith = translation_order(matrix, h)
            points = component_multiplicity * det_f
            level_cycles[l_value][order] = level_cycles[l_value].get(order, 0) + points
            translations.append(
                {
                    "l": l_value,
                    "h": h,
                    "augmented_smith_invariants": augmented_smith,
                    "order": order,
                    "fixed_component_prefix": [
                        {
                            "n": n,
                            "fixed_points_per_component": det_f if n % order == 0 else 0,
                        }
                        for n in range(1, FIXED_N_MAX + 1)
                    ],
                }
            )
        sector_records.append(
            {
                "alpha": alpha,
                "lambda_exact_counts": lambda_counts,
                "component_multiplicity_factors": factors,
                "component_multiplicity": component_multiplicity,
                "F_alpha": matrix,
                "det_F_alpha": det_f,
                "smith_invariants": smith,
                "points_in_sector": component_multiplicity * det_f,
                "translations": translations,
            }
        )

    if support:
        base = f_matrix(support, content, vacancies, [1] * len(support))
        level_formula = Fraction(abs(determinant(base)), 1)
        for j in support:
            level_formula *= Fraction(comb(vacancies[j] + content[j] - 1, content[j] - 1), content[j])
        if level_formula.denominator != 1:
            raise ArithmeticError("nonintegral KTT level cardinality")
        expected_level = level_formula.numerator
    else:
        expected_level = 1
    sector_total = sum(row["points_in_sector"] for row in sector_records)
    if sector_total != expected_level:
        raise ArithmeticError("sector decomposition does not recover KTT level size")

    return {
        "L": L,
        "M": M,
        "content_key": key,
        "content": [
            {"j": j, "m_j": content[j], "p_j": vacancies[j]} for j in support
        ],
        "sector_candidate_count": candidates,
        "positive_sector_count": len(sector_records),
        "level_cardinality": sector_total,
        "ktt_level_cardinality": expected_level,
        "sectors": sector_records,
        "evolutions": [evolution_record(l_value, level_cycles[l_value]) for l_value in l_values],
    }


def build() -> dict:
    levels: list[dict] = []
    state_rows: list[dict] = []
    length_rows: list[dict] = []
    level_by_lm: dict[tuple[int, int], list[dict]] = {}

    for L in range(2, L_MAX + 1):
        l_values = list(range(1, L // 2 + 2))
        for M in range(0, L // 2 + 1):
            these_levels = [build_level(L, parts, l_values) for parts in partitions(M)]
            expected = comb(L, M)
            observed = sum(level["level_cardinality"] for level in these_levels)
            if observed != expected:
                raise ArithmeticError(f"KTT levels do not partition C({L},{M})")
            levels.extend(these_levels)
            level_by_lm[(L, M)] = these_levels
            for l_value in l_values:
                spectrum: dict[int, int] = {}
                for level in these_levels:
                    evolution = level["evolutions"][l_value - 1]
                    for row in evolution["cycle_spectrum"]:
                        spectrum[row["order"]] = spectrum.get(row["order"], 0) + row["points"]
                state_rows.append(
                    {
                        "L": L,
                        "M": M,
                        "l": l_value,
                        "state_count": expected,
                        **{key: value for key, value in evolution_record(l_value, spectrum).items() if key != "l"},
                    }
                )

        for l_value in l_values:
            spectrum: dict[int, int] = {}
            total = 0
            for M in range(0, L // 2 + 1):
                row = next(
                    item for item in state_rows
                    if item["L"] == L and item["M"] == M and item["l"] == l_value
                )
                total += row["state_count"]
                for cycle in row["cycle_spectrum"]:
                    spectrum[cycle["order"]] = spectrum.get(cycle["order"], 0) + cycle["points"]
            length_rows.append(
                {
                    "L": L,
                    "l": l_value,
                    "positive_weight_state_count": total,
                    **{key: value for key, value in evolution_record(l_value, spectrum).items() if key != "l"},
                }
            )

    sectors = [sector for level in levels for sector in level["sectors"]]
    translations = [translation for sector in sectors for translation in sector["translations"]]
    scan_totals = {
        "L_max": L_MAX,
        "fixed_n_max": FIXED_N_MAX,
        "level_count": len(levels),
        "sector_count": len(sectors),
        "translation_count": len(translations),
        "state_aggregate_count": len(state_rows),
        "length_aggregate_count": len(length_rows),
        "component_multiplicity_sum": sum(row["component_multiplicity"] for row in sectors),
        "sector_point_sum": sum(row["points_in_sector"] for row in sectors),
        "fixed_point_cells": FIXED_N_MAX * (
            len(translations) + len(state_rows) + len(length_rows)
        ),
    }

    data = {
        "schema": "hcs-c182-periodic-bbs-action-angle-v1",
        "candidate_id": "HCS-C182",
        "evaluation_date": "2026-08-26",
        "source_commit": SOURCE_COMMIT,
        "evaluator": {
            "skill": "route-a-evaluator",
            "version": "0.2.0",
            "path": "flow_systems/skills/route-a-evaluator.md",
            "sha256": EVALUATOR_SHA256,
        },
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "source_lock": {
            "object": "periodic A_1^(1) box--ball system on binary words of length L with M balls",
            "family": "all integers L>=1, 0<=M<=floor(L/2), every admissible soliton content m, every internal symmetry sector alpha, and every commuting T_l with l>=1",
            "phase_space": "P_(L,M)={binary words with exactly M balls}; the full positive-weight space is the disjoint union over 0<=M<=floor(L/2)",
            "dynamics": "the capacity-l periodic combinatorial-R carrier map T_l; the T_l commute and preserve soliton content",
            "parameters": "L,M,l, finitely supported m=(m_j), p_j=L-2*sum_k min(j,k)m_k, and alpha_j|gcd(m_j,p_j)",
            "parameter_provenance": "L,M,l are intrinsic lattice, mass, and carrier-capacity parameters; m,p,alpha are conserved-action and internal-symmetry data",
            "arithmetic_origin": "none: integer lattice combinatorics and Smith arithmetic are not an intrinsic rational-prime or prime-power source",
            "clock": "one application of T_l is one discrete physical update; n is the iterate count, with no log-prime roof or post-hoc time change",
            "normalization": "binary symbols 0=empty and 1=ball; source papers use 1=empty and 2=ball; no spectral unfolding or fitted scale",
            "determinant_convention": "Artin--Mazur zeta exp(sum_n #Fix(T_l^n) z^n/n) and the ordinary determinant of the finite counting-measure Koopman permutation",
            "orbit_cutoff": "none in the theorem; the finite regression ledger exhausts 2<=L<=14 and 0<=M<=floor(L/2), with fixed-point prefixes n<=12",
            "precision": "exact integers, binomial coefficients, Mobius inversion, determinants, determinantal divisors, and Smith normal form",
            "training_data": "none",
            "allowed_data": "KTT/Takagi action--angle theorems and exact finite regression states only",
            "forbidden_data": "target zero or prime tables, arithmetic local data, Euler factors, root numbers, automorphy, Hilbert--Polya claims, fitted clocks, and Route B",
        },
        "source_attribution": [
            {
                "authors": "A. Kuniba, T. Takagi, A. Takenouchi",
                "title": "Bethe ansatz and inverse scattering transform in a periodic box-ball system",
                "source": "Nuclear Physics B 747 (2006), 354--397; arXiv:math/0602481v2",
                "url": "https://arxiv.org/abs/math/0602481",
                "role": "source theorem for commuting time evolutions, conserved soliton content, action--angle bijection, and linearized T_l translations",
                "verified": True,
            },
            {
                "authors": "T. Takagi",
                "title": "Level Set Structure of an Integrable Cellular Automaton",
                "source": "SIGMA 6 (2010), 027; arXiv:0906.1410",
                "url": "https://sigma-journal.com/2010/027/",
                "role": "source theorem for internal-symmetry sector tori, F_alpha, exact multiplicities, and p_max=0 boundary",
                "verified": True,
            },
        ],
        "theorem": {
            "feasibility_triage": "PROVABLE AS STATED",
            "admissible_domain": "L>=2M>=0; sum_j j*m_j=M; H={j:m_j>0}; p_j=L-2*sum_k min(j,k)m_k>=0",
            "internal_symmetry": "for each j in H choose alpha_j dividing gcd(m_j,p_j), with gcd(m,0)=m",
            "sector_matrix": "F_alpha[j,k]=(delta_jk*p_k+2*min(j,k)*m_k)/alpha_k",
            "sector_torus": "each connected component of symmetry alpha is Z^H/F_alpha Z^H, and T_l is translation by h_l=(min(j,l))_(j in H)",
            "sector_multiplicity": "prod_j |Lambda^(alpha_j)(m_j,p_j)|/(m_j/alpha_j)",
            "mobius_count": "|Lambda^(alpha)(m,p)|=sum_(beta: alpha|beta|gcd(m,p)) mu(beta/alpha)*C((p+m)/beta-1,m/beta-1)",
            "snf_order": "ord_alpha,l is the least n>0 with n*h_l in F_alpha Z^H; equivalently det(F_alpha) divided by the product of the Smith factors of [F_alpha|h_l]",
            "component_fixed_points": "#Fix(T_l^n on one component)=det(F_alpha) if ord_alpha,l divides n, and 0 otherwise",
            "aggregate_fixed_points": "sum_alpha multiplicity(alpha)*det(F_alpha)*1_(ord_alpha,l divides n), with an additional sum over contents for P_(L,M) or the full positive-weight space",
            "primitive_cycles": "P_n=sum_(d|n) mu(n/d)#Fix(T_l^d), C_n=P_n/n; equivalently every component of order q contributes det(F_alpha)/q q-cycles",
            "zeta_koopman": "zeta_T(z)=prod_q(1-z^q)^(-C_q)=det(I-z U_T)^(-1) on the finite counting-measure Koopman space",
            "commutativity": "all T_l commute because their angle-variable representatives are translations on the same finite lattice quotient",
            "saturation": "h_l=(j)_(j in H) for l>=max(H), so every T_l beyond the longest soliton has the same action on that level",
            "vacuum_boundary": "M=0 gives the one-point zero-dimensional torus and every T_l is the identity",
            "half_filling_boundary": "when L=2M the largest vacancy p_max is zero; only alpha_max=m_max has nonzero Lambda count in that coordinate, and the torus theorem remains finite",
            "source_novelty_boundary": "the action--angle and internal-symmetry decomposition are prior KTT/Takagi results; this package derives and certifies their unified fixed-point, primitive-cycle, zeta, and finite-Koopman consequences",
        },
        "finite_regression_sentinels": {
            "sentinels_are_proof": False,
            "coverage": scan_totals,
            "level_rows": levels,
            "state_aggregate_rows": state_rows,
            "length_aggregate_rows": length_rows,
        },
        "progress_and_boundary": {
            "progress": "an all-L all-content all-internal-symmetry action--angle decomposition is converted into exact component and globally aggregated fixed-point, primitive-cycle, zeta, and Koopman determinant laws",
            "source_boundary": "KTT/Takagi own the action--angle and torus decomposition; the present contribution is the finite-dynamical synthesis, exact SNF certificate, and reproducible all-parameter derivation",
            "arithmetic_clock_obstruction": "the intrinsic clock is an unweighted integer iterate and the lengths L,l are freely chosen lattice parameters; no log p, prime-power repetition weight, or von Mangoldt amplitude emerges",
            "analytic_obstruction": "every fixed-(L,M,l) zeta is a finite rational cycle product, with no target functional equation, Riemann--von Mangoldt law, or canonical infinite-volume normalization supplied",
            "operator_progress": "the counting-measure Koopman operator is a canonical finite unitary permutation and its determinant is exactly the reciprocal zeta",
            "route_boundary": "exact integrability and exact Smith arithmetic do not repair A0 or imply a Hilbert--Polya operator",
        },
        "route_a": {
            "tuple": [
                "A0_FAIL",
                "A1_WEAK",
                "A2_FAIL",
                "A3_FAIL",
                "A4_NATURAL_QUANTIZATION",
            ],
            "overall": "ROUTE_A_REJECTED",
            "A0_qualification": "NO_INTRINSIC_RATIONAL_PRIME_OR_PRIME_POWER_ORIGIN_AND_NO_ARITHMETIC_CLOCK",
            "A1_qualification": "COMPLETE_INTRINSIC_PRIMITIVE_CYCLE_CLASSIFICATION_WITHOUT_ARITHMETIC_INFORMATION_OR_STABILITY_WEIGHTS",
            "A2_qualification": "EXACT_FINITE_SOURCE_ZETA_AND_KOOPMAN_DETERMINANT_WITH_NO_TARGET_DIVISOR_COMPARISON",
            "A3_qualification": "FINITE_RATIONAL_SOURCE_STRUCTURE_WITH_NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_CONTINUATION_OR_WEIL_COMPRESSION",
            "A4_qualification": "SAME_CLOCK_FINITE_COUNTING_MEASURE_KOOPMAN_PERMUTATION_UNITARY",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": {
            "used_target_zero_table": False,
            "used_target_prime_table": False,
            "used_arithmetic_local_data": False,
            "claimed_target_divisor_match": False,
            "claimed_target_functional_equation": False,
            "claimed_euler_factor": False,
            "claimed_root_number": False,
            "claimed_automorphy": False,
            "claimed_hilbert_polya": False,
            "claimed_action_angle_novelty": False,
            "route_b_invocation_allowed": False,
        },
        "integrity": {
            "finite_ledgers_are_proof": False,
            "citation_population": 2,
            "verified_reference_population": 2,
            "external_reviewer_simulated": False,
            "acceptance_score_claimed": False,
            "all_parameter_claims_have_proof_dependencies": True,
            "model_rejected_as_primary_route_a_candidate": True,
        },
        "nonclaims": [
            "novelty of the KTT/Takagi action--angle or invariant-torus theorem",
            "an arithmetic prime or prime-power origin for solitons, contents, or Smith factors",
            "stability or von Mangoldt weights for primitive cycles",
            "a target divisor, functional equation, counting law, or Weil compression",
            "arithmetic local data, Euler factors, root numbers, or automorphy",
            "a Hilbert--Polya operator or Route-B authorization",
            "external peer review, novelty priority, or an acceptance score",
        ],
    }
    data["payload_sha256"] = sha256(canonical_bytes(data)).hexdigest()
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    )
    coverage = data["finite_regression_sentinels"]["coverage"]
    print(
        json.dumps(
            {
                "status": "C182_PRODUCER_PASS",
                **coverage,
                "payload_sha256": data["payload_sha256"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
