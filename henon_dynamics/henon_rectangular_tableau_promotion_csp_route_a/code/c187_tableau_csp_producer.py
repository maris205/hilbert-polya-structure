#!/usr/bin/env python3
"""Produce the exact HCS-C187 rectangular-tableau CSP certificate."""
from __future__ import annotations

import argparse
from collections import Counter
from functools import lru_cache
from hashlib import sha256
import json
from math import factorial, gcd, lcm, prod
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c187_tableau_csp_evidence.json"
SOURCE_COMMIT = "908a6818caedb0c46195a591873a2ac9c685b55e"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
A_MAX = B_MAX = 6
ENUMERATION_N_MAX = 16
ENUMERATION_TABLEAU_MAX = 50_000


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n: int) -> int:
    if n == 1:
        return 1
    primes = 0
    p = 2
    remaining = n
    while p * p <= remaining:
        if remaining % p == 0:
            remaining //= p
            primes += 1
            if remaining % p == 0:
                return 0
            while remaining % p == 0:
                remaining //= p
        p += 1
    if remaining > 1:
        primes += 1
    return -1 if primes % 2 else 1


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def poly_mul(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] += a * b
    return trim(answer)


def poly_div_exact(numerator: list[int], denominator: list[int]) -> list[int]:
    """Exact division in Z[q], with ascending coefficient lists."""
    work = numerator[:]
    denominator = trim(denominator[:])
    if denominator[-1] not in (1, -1):
        raise AssertionError("division expects a unit leading coefficient")
    if len(work) < len(denominator):
        raise AssertionError("nonzero numerator has smaller degree")
    quotient = [0] * (len(work) - len(denominator) + 1)
    while len(work) >= len(denominator):
        shift = len(work) - len(denominator)
        leading = work[-1] // denominator[-1]
        quotient[shift] = leading
        for index, value in enumerate(denominator):
            work[index + shift] -= leading * value
        trim(work)
        if work == [0]:
            break
    if any(work):
        raise AssertionError("polynomial division left a remainder")
    return trim(quotient)


def poly_mod(numerator: list[int], denominator: list[int]) -> list[int]:
    work = trim(numerator[:])
    denominator = trim(denominator[:])
    if denominator[-1] != 1:
        raise AssertionError("modulus must be monic")
    while len(work) >= len(denominator):
        shift = len(work) - len(denominator)
        leading = work[-1]
        for index, value in enumerate(denominator):
            work[index + shift] -= leading * value
        trim(work)
    return trim(work)


def poly_pow(base: list[int], exponent: int) -> list[int]:
    answer = [1]
    factor = base[:]
    power = exponent
    while power:
        if power & 1:
            answer = poly_mul(answer, factor)
        power >>= 1
        if power:
            factor = poly_mul(factor, factor)
    return answer


@lru_cache(maxsize=None)
def cyclotomic(n: int) -> tuple[int, ...]:
    polynomial = [-1] + [0] * (n - 1) + [1]
    for d in divisors(n):
        if d == n:
            continue
        polynomial = poly_div_exact(polynomial, list(cyclotomic(d)))
    return tuple(polynomial)


def hook_lengths(a: int, b: int) -> list[int]:
    return [a - row + b - column - 1 for row in range(a) for column in range(b)]


def q_hook_polynomial(a: int, b: int) -> tuple[list[int], dict[int, int]]:
    n = a * b
    hooks = hook_lengths(a, b)
    exponents: dict[int, int] = {}
    polynomial = [1]
    for order in range(2, n + 1):
        exponent = n // order - sum(hook % order == 0 for hook in hooks)
        if exponent < 0:
            raise AssertionError("negative cyclotomic exponent")
        if exponent:
            exponents[order] = exponent
            polynomial = poly_mul(polynomial, poly_pow(list(cyclotomic(order)), exponent))
    return polynomial, exponents


def root_evaluation(coefficients: list[int], order: int) -> int:
    if order == 1:
        return sum(coefficients)
    remainder = poly_mod(coefficients, list(cyclotomic(order)))
    if len(remainder) != 1:
        raise AssertionError(f"root-of-unity remainder for order {order} is not constant")
    return remainder[0]


def coefficient_sha256(coefficients: list[int]) -> str:
    return sha256(json.dumps(coefficients, separators=(",", ":")).encode()).hexdigest()


def canonical_bytes(data: dict) -> bytes:
    body = dict(data)
    body.pop("payload_sha256", None)
    return json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def build() -> dict:
    rectangles: list[dict] = []
    iterate_rows: list[dict] = []
    period_rows: list[dict] = []
    spectral_rows: list[dict] = []

    for a in range(1, A_MAX + 1):
        for b in range(1, B_MAX + 1):
            n = a * b
            hooks = hook_lengths(a, b)
            coefficients, exponents = q_hook_polynomial(a, b)
            tableau_count = factorial(n) // prod(hooks)
            assert sum(coefficients) == tableau_count
            expected_degree = n * (n - 1) // 2 - sum(hook - 1 for hook in hooks)
            assert len(coefficients) - 1 == expected_degree

            fixed_by_power: dict[int, int] = {}
            for power in range(n):
                root_order = n // gcd(n, power)
                fixed = root_evaluation(coefficients, root_order)
                assert fixed >= 0
                fixed_by_power[power] = fixed
                iterate_rows.append({
                    "a": a,
                    "b": b,
                    "n": n,
                    "iterate": power,
                    "gcd_n_iterate": gcd(n, power),
                    "root_order": root_order,
                    "fixed_count": fixed,
                })

            exact_period: dict[int, int] = {}
            cycles: dict[int, int] = {}
            for period in divisors(n):
                exact = 0
                for d in divisors(period):
                    fixed_d = tableau_count if d == n else fixed_by_power[d]
                    exact += mobius(period // d) * fixed_d
                assert exact >= 0 and exact % period == 0
                exact_period[period] = exact
                cycles[period] = exact // period
                period_rows.append({
                    "a": a,
                    "b": b,
                    "n": n,
                    "period": period,
                    "fixed_at_period": tableau_count if period == n else fixed_by_power[period],
                    "exact_period_count": exact,
                    "cycle_count": exact // period,
                })
            assert sum(exact_period.values()) == tableau_count

            actual_order = 1
            for period, count in exact_period.items():
                if count:
                    actual_order = lcm(actual_order, period)
            assert n % actual_order == 0

            spectral_multiplicities: list[int] = []
            for exponent in range(n):
                multiplicity = sum(
                    count for period, count in cycles.items()
                    if (exponent * period) % n == 0
                )
                spectral_multiplicities.append(multiplicity)
                spectral_rows.append({
                    "a": a,
                    "b": b,
                    "n": n,
                    "root_exponent_mod_n": exponent,
                    "multiplicity": multiplicity,
                })
            assert sum(spectral_multiplicities) == tableau_count

            hook_counter = Counter(hooks)
            rectangles.append({
                "a": a,
                "b": b,
                "n": n,
                "shape": [b] * a,
                "hook_multiset": {str(key): hook_counter[key] for key in sorted(hook_counter)},
                "tableau_count": tableau_count,
                "q_hook_convention": "F_ab(q)=[ab]_q!/product_(cells c)[h(c)]_q with no q-shift",
                "q_hook_cyclotomic_exponents": {str(key): exponents[key] for key in sorted(exponents)},
                "q_hook_degree": expected_degree,
                "q_hook_coefficients": coefficients,
                "q_hook_coefficients_sha256": coefficient_sha256(coefficients),
                "promotion_order_divides": n,
                "actual_promotion_order": actual_order,
                "identity_boundary": a == 1 or b == 1,
                "enumeration_regression_selected": n <= ENUMERATION_N_MAX and tableau_count <= ENUMERATION_TABLEAU_MAX,
                "nonzero_cycle_lengths": [period for period in divisors(n) if cycles[period]],
                "zeta_factors": [
                    {"period": period, "exponent": -cycles[period]}
                    for period in divisors(n) if cycles[period]
                ],
                "koopman_determinant_factors": [
                    {"period": period, "exponent": cycles[period]}
                    for period in divisors(n) if cycles[period]
                ],
            })

    data = {
        "schema": "HCS-C187-v1",
        "candidate_id": "HCS-C187",
        "date_utc": "2026-08-26",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "evaluator": {
            "path": "flow_systems/skills/route-a-evaluator.md",
            "version": "0.2.0",
            "sha256": EVALUATOR_SHA256,
        },
        "source_lock": {
            "object": "Schuetzenberger jeu-de-taquin promotion j on standard Young tableaux of rectangular shape b^a",
            "family": "all positive integers a,b with N=ab",
            "phase_space": "the finite set SYT(b^a)",
            "clock": "one application of Rhoades's convention: remove N, slide the hole northwest, increment retained entries, and insert 1",
            "measure": "counting probability on SYT(b^a)",
            "operator": "finite Koopman permutation U_ab f=f composed with j on ell2(SYT(b^a))",
            "q_hook_convention": "F_ab(q)=[N]_q!/product_(cells c)[h(c)]_q, exactly the unshifted standard-tableau polynomial in Rhoades Theorem 1.3",
            "determinant_convention": "Artin--Mazur zeta of the finite promotion permutation and the reciprocal finite Koopman determinant",
            "cutoff": "all-rectangle source theorem; exact formula regression uses 1<=a,b<=6 and direct tableau enumeration only on declared small rectangles",
            "allowed_data": "rectangular hook lengths, exact cyclotomic polynomials, source-derived CSP evaluations, and direct small-tableau promotion",
            "forbidden_data": "target zero or prime tables, arithmetic local data, Euler factors, root numbers, automorphy, Hilbert--Polya operators, and Route-B inputs",
        },
        "attribution": {
            "status": "SOURCE_DERIVED_SYNTHESIS_NOT_NEW_THEOREM_CLAIM",
            "all_rectangle_owner": "Rhoades 2010 owns the rectangular standard-tableau CSP and records the promotion order-divides-N theorem and dihedral promotion--evacuation action",
            "order_background": "Haiman 1992 is the classical source cited by Rhoades for the rectangular promotion-order result",
            "package_increment": "source-locked Route-A synthesis of every-iterate fixed counts, Mobius period/cycle recovery, finite zeta, Koopman determinant and spectral multiplicities, with executable regression and stopping boundaries",
            "finite_evidence_role": "finite enumeration and symbolic reconstruction are regression checks only and do not prove the all-rectangle CSP",
        },
        "theorem": {
            "order_bound": "j^N is the identity on SYT(b^a); the actual order divides N and need not equal N",
            "csp_fixed_count": "Fix(j^d)=F_ab(zeta_N^d) for every integer d, where F_ab(q) is the unshifted q-hook polynomial",
            "exact_period": "P_l=sum_(d|l) mu(l/d) Fix(j^d) for every l|N",
            "cycle_count": "C_l=P_l/l",
            "zeta": "zeta_j(z)=product_(l|N)(1-z^l)^(-C_l)",
            "koopman_determinant": "det(I-z U_ab)=product_(l|N)(1-z^l)^(C_l)=zeta_j(z)^(-1)",
            "spectral_multiplicity": "mult(zeta_N^k)=sum_(l|N and N divides k*l) C_l",
            "trace": "Tr(U_ab^d)=Fix(j^d)",
            "reversor": "evacuation e is an involution and e*j*e=j^(-1); e followed by complex conjugation is an antiunitary reversor",
            "identity_boundary": "if a=1 or b=1 then SYT(b^a) is a singleton and j has order one",
        },
        "finite_replay": {
            "a_min": 1,
            "a_max": A_MAX,
            "b_min": 1,
            "b_max": B_MAX,
            "enumeration_n_max": ENUMERATION_N_MAX,
            "enumeration_tableau_max": ENUMERATION_TABLEAU_MAX,
            "rectangles": rectangles,
            "iterate_rows": iterate_rows,
            "period_rows": period_rows,
            "spectral_rows": spectral_rows,
            "rectangle_row_count": len(rectangles),
            "iterate_row_count": len(iterate_rows),
            "period_row_count": len(period_rows),
            "spectral_row_count": len(spectral_rows),
            "enumeration_rectangle_count": sum(row["enumeration_regression_selected"] for row in rectangles),
        },
        "progress_and_boundary": {
            "progress": "one theorem package closes the all-rectangle fixed ledger, exact periods and cycles, zeta, finite Koopman determinant, spectrum, and evacuation reversal",
            "order_boundary": "j^N=id is uniform, but exact order N is false in general; one-row, one-column, and 2-by-2 rectangles are explicit controls",
            "proof_boundary": "the all-rectangle CSP is imported with attribution; finite rows and enumeration regression-test consequences rather than prove it",
            "arithmetic_boundary": "rectangle dimensions, hook lengths, and cyclotomic roots have no intrinsic rational-prime or prime-power semantics",
            "operator_boundary": "the natural finite unitary is the source Koopman permutation; it has only roots of unity and no target divisor or self-adjoint Hilbert--Polya conclusion",
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
            "overall": "ROUTE_A_REJECTED",
            "A0_qualification": "RECTANGLE_AND_HOOK_DATA_HAVE_NO_INTRINSIC_RATIONAL_PRIME_ORIGIN",
            "A1_qualification": "FINITE_PROMOTION_CYCLES_ARE_COMPLETE_BUT_CARRY_NO_A0_ARITHMETIC_PAYLOAD",
            "A2_qualification": "FINITE_SOURCE_ZETA_AND_KOOPMAN_DETERMINANT_HAVE_NO_TARGET_DIVISOR_MATCH",
            "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_CONTINUATION_OR_WEIL_COMPRESSION",
            "A4_qualification": "SOURCE_NATIVE_FINITE_UNITARY_AND_EVACUATION_ANTIUNITARY_REVERSOR_ONLY",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": {
            "used_target_zero_table": False,
            "used_target_prime_table": False,
            "used_arithmetic_local_data": False,
            "claimed_target_divisor_match": False,
            "claimed_target_functional_equation": False,
            "claimed_hilbert_polya": False,
            "claimed_exact_order_n_uniformly": False,
            "claimed_global_novelty": False,
            "route_b_invocation_allowed": False,
        },
        "source_registry": [
            {
                "key": "rhoades_2010_rectangular_promotion_csp",
                "title": "Cyclic sieving, promotion, and representation theory",
                "authors": "Brendon Rhoades",
                "year": 2010,
                "journal": "Journal of Combinatorial Theory, Series A 117(1), 38--76",
                "doi": "10.1016/j.jcta.2009.03.017",
                "arxiv": "1005.2568",
                "role": "primary ownership for the unshifted q-hook CSP, order-divides-N corollary, and promotion--evacuation dihedral relation",
            },
            {
                "key": "haiman_1992_dual_equivalence",
                "title": "Dual equivalence with applications, including a conjecture of Proctor",
                "authors": "Mark D. Haiman",
                "year": 1992,
                "journal": "Discrete Mathematics 99, 79--113",
                "doi": "10.1016/0012-365X(92)90368-P",
                "role": "classical promotion-order background cited by Rhoades",
            },
        ],
        "nonclaims": [
            "novelty or priority for the rectangular promotion CSP, q-hook formula, order bound, or evacuation relation",
            "uniform equality between the order of promotion and the number N of boxes",
            "use of finite enumeration as a proof of the all-rectangle theorem",
            "rational-prime semantics for rectangle dimensions, hook lengths, cyclotomic orders, or promotion cycles",
            "a target divisor, functional equation, counting law, continuation, or Weil compression",
            "a self-adjoint Hilbert--Polya operator, Route-B authorization, external peer review, or acceptance score",
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
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    finite = data["finite_replay"]
    print(json.dumps({
        "status": "C187_PRODUCER_PASS",
        "rectangle_rows": finite["rectangle_row_count"],
        "iterate_rows": finite["iterate_row_count"],
        "period_rows": finite["period_row_count"],
        "spectral_rows": finite["spectral_row_count"],
        "enumeration_rectangles": finite["enumeration_rectangle_count"],
        "payload_sha256": data["payload_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
