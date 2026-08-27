#!/usr/bin/env python3
"""Produce the exact C194 Holte carries ledger."""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
import math
import os
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = Path(os.environ.get("C194_OUTPUT", ROOT / "results/c194_holte_evidence.json"))
SOURCE_COMMIT = "c3a5b9bbb3b6d0881f395abe4a01accd322f69cb"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
N_MAX = 8
BASES = tuple(range(2, 11))
SEMIGROUP_BASES = tuple(range(2, 9))


def qtext(value: Fraction | int) -> str:
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def digit_sum_counts(n: int, base: int) -> list[int]:
    """Coefficient list of (1+x+...+x^(base-1))^n by convolution."""
    counts = [1]
    for _ in range(n):
        prefix = [0]
        for value in counts:
            prefix.append(prefix[-1] + value)
        updated = []
        for total in range(len(counts) + base - 1):
            right = min(total + 1, len(counts))
            left = max(0, total - base + 1)
            updated.append(prefix[right] - prefix[left])
        counts = updated
    return counts


def transition_numerators(n: int, base: int) -> list[list[int]]:
    counts = digit_sum_counts(n, base)
    matrix: list[list[int]] = []
    for carry_in in range(n):
        row = []
        for carry_out in range(n):
            lower = carry_out * base - carry_in
            upper = (carry_out + 1) * base - carry_in - 1
            start = max(0, lower)
            stop = min(len(counts), upper + 1)
            row.append(sum(counts[start:stop]) if start < stop else 0)
        if sum(row) != base**n:
            raise AssertionError((n, base, carry_in, row))
        matrix.append(row)
    return matrix


def transition(n: int, base: int) -> list[list[Fraction]]:
    denominator = base**n
    return [[Fraction(value, denominator) for value in row] for row in transition_numerators(n, base)]


def identity(size: int) -> list[list[Fraction]]:
    return [[Fraction(int(i == j)) for j in range(size)] for i in range(size)]


def multiply(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    size = len(left)
    return [
        [sum((left[i][k] * right[k][j] for k in range(size)), Fraction()) for j in range(size)]
        for i in range(size)
    ]


def power(matrix: list[list[Fraction]], exponent: int) -> list[list[Fraction]]:
    result = identity(len(matrix))
    factor = matrix
    while exponent:
        if exponent & 1:
            result = multiply(result, factor)
        exponent //= 2
        if exponent:
            factor = multiply(factor, factor)
    return result


def trace(matrix: list[list[Fraction]]) -> Fraction:
    return sum((matrix[i][i] for i in range(len(matrix))), Fraction())


def eulerian_row(n: int) -> list[int]:
    row = [1]
    for size in range(2, n + 1):
        previous = row
        row = []
        for descents in range(size):
            first = (descents + 1) * previous[descents] if descents < len(previous) else 0
            second = (size - descents) * previous[descents - 1] if descents else 0
            row.append(first + second)
    return row


def polynomial_product(left: list[Fraction], right: Iterable[Fraction]) -> list[Fraction]:
    right = list(right)
    result = [Fraction() for _ in range(len(left) + len(right) - 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return result


def spectral_polynomials(n: int, base: int) -> tuple[list[Fraction], list[Fraction]]:
    charpoly = [Fraction(1)]
    determinant = [Fraction(1)]
    for index in range(n):
        eigenvalue = Fraction(1, base**index)
        charpoly = polynomial_product(charpoly, [-eigenvalue, Fraction(1)])
        determinant = polynomial_product(determinant, [Fraction(1), -eigenvalue])
    return charpoly, determinant


def total_variation(row: list[Fraction], stationary: list[Fraction]) -> Fraction:
    return sum((abs(left - right) for left, right in zip(row, stationary)), Fraction()) / 2


def serialize_matrix(matrix: list[list[Fraction]]) -> list[list[str]]:
    return [[qtext(value) for value in row] for row in matrix]


def payload_digest(document: dict[str, object]) -> str:
    raw = json.dumps(document, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def build_case(n: int, base: int) -> dict[str, object]:
    numerators = transition_numerators(n, base)
    matrix = [[Fraction(value, base**n) for value in row] for row in numerators]
    eulerian = eulerian_row(n)
    stationary = [Fraction(value, math.factorial(n)) for value in eulerian]
    charpoly, determinant = spectral_polynomials(n, base)
    eigenvalues = [Fraction(1, base**index) for index in range(n)]
    power_traces = []
    current = identity(n)
    for exponent in range(7):
        if exponent:
            current = multiply(current, matrix)
        direct = trace(current)
        spectral = sum((value**exponent for value in eigenvalues), Fraction())
        if direct != spectral:
            raise AssertionError((n, base, exponent, direct, spectral))
        power_traces.append({"power": exponent, "direct": qtext(direct), "spectral": qtext(spectral)})

    convergence = []
    for exponent in range(1, 6):
        current = power(matrix, exponent)
        distances = [total_variation(row, stationary) for row in current]
        if n >= 3:
            bounds = [Fraction(n - 1, 2 * base**exponent) + Fraction(i, base**exponent) for i in range(n)]
            if any(distance > bound for distance, bound in zip(distances, bounds)):
                raise AssertionError((n, base, exponent, distances, bounds))
        else:
            bounds = []
        convergence.append({
            "power": exponent,
            "from_zero_distribution": [qtext(value) for value in current[0]],
            "from_last_distribution": [qtext(value) for value in current[-1]],
            "state_total_variation": [qtext(value) for value in distances],
            "worst_total_variation": qtext(max(distances)),
            "theorem_3_3_bounds": [qtext(value) for value in bounds],
        })

    return {
        "n": n,
        "base": base,
        "base_class": "prime" if base in {2, 3, 5, 7} else "composite",
        "denominator": str(base**n),
        "transition_numerators": numerators,
        "transition_matrix": serialize_matrix(matrix),
        "eulerian_numbers": [str(value) for value in eulerian],
        "stationary_distribution": [qtext(value) for value in stationary],
        "eigenvalues": [qtext(value) for value in eigenvalues],
        "charpoly_ascending": [qtext(value) for value in charpoly],
        "det_I_minus_zP_ascending": [qtext(value) for value in determinant],
        "trace": qtext(trace(matrix)),
        "power_traces": power_traces,
        "convergence": convergence,
    }


def main() -> None:
    cases = [build_case(n, base) for n in range(1, N_MAX + 1) for base in BASES]

    semigroup_tuple_count = 0
    semigroup_cell_count = 0
    for n in range(1, N_MAX + 1):
        for left_base in SEMIGROUP_BASES:
            left = transition(n, left_base)
            for right_base in SEMIGROUP_BASES:
                observed = multiply(left, transition(n, right_base))
                expected = transition(n, left_base * right_base)
                if observed != expected:
                    raise AssertionError((n, left_base, right_base))
                semigroup_tuple_count += 1
                semigroup_cell_count += n * n

    power_specs = [(base, 2) for base in BASES] + [(base, 3) for base in range(2, 5)]
    power_tuple_count = 0
    power_cell_count = 0
    for n in range(1, N_MAX + 1):
        for base, exponent in power_specs:
            if power(transition(n, base), exponent) != transition(n, base**exponent):
                raise AssertionError((n, base, exponent))
            power_tuple_count += 1
            power_cell_count += n * n

    document: dict[str, object] = {
        "schema": "hcs-c194-holte-carries-evidence-v1",
        "candidate_id": "HCS-C194",
        "evaluation_date": "2026-08-27",
        "source_commit": SOURCE_COMMIT,
        "evaluator": {
            "version": "0.2.0",
            "path": "flow_systems/skills/route-a-evaluator.md",
            "sha256": EVALUATOR_SHA256,
        },
        "scope_literal": SCOPE,
        "source_lock": {
            "phase_space": "for each n>=1, the carry states X_n={0,...,n-1}",
            "clock": "one independent base-b digit column from each of n addends",
            "transition": "j is the unique output carry with jb <= i + sum(digits) < (j+1)b",
            "parameters": "all integers n>=1 and b>=2; n=1 is the one-state identity boundary",
            "normalization": "row-stochastic matrices acting on row distributions",
            "arithmetic_origin": "ordinary positional integer addition in base b, not a rational-prime orbit model",
            "determinant_convention": "det(I-z P_b), a finite Markov determinant rather than an Artin--Mazur zeta",
            "precision": "exact integer counts and rational arithmetic",
            "allowed_data": "digit counts, carries, Eulerian numbers, exact finite matrices and prime/composite base controls",
            "forbidden_data": "target tables, arithmetic local data, Euler factors, root numbers, automorphy, Hilbert--Polya and Route B",
        },
        "source_registry": [
            {
                "source_id": "H97",
                "authors": ["John M. Holte"],
                "title": "Carries, Combinatorics, and an Amazing Matrix",
                "journal": "The American Mathematical Monthly 104(2), 138--149",
                "year": 1997,
                "doi": "10.1080/00029890.1997.11990612",
                "stable_doi": "10.2307/2974981",
                "theorem_locators": ["Theorem 1", "Theorem 3", "Theorem 4"],
                "role": "transition formula, base-independent diagonalization, simple spectrum, Eulerian stationary law and semigroup",
            },
            {
                "source_id": "DF09",
                "authors": ["Persi Diaconis", "Jason Fulman"],
                "title": "Carries, shuffling, and symmetric functions",
                "journal": "Advances in Applied Mathematics 43(2), 176--196",
                "year": 2009,
                "doi": "10.1016/j.aam.2009.02.002",
                "theorem_locators": ["Theorem 1.1", "Theorem 3.1", "Theorem 3.3"],
                "role": "descent marginal interpretation and quantitative convergence bounds",
            },
        ],
        "attribution": {
            "status": "CLASSICAL_THEOREM_REPRODUCED_WITH_EXACT_CERTIFICATE",
            "holte_owned": "the all-(n,b) transition formula, common eigenvectors, eigenvalues, stationary Eulerian row and P_a P_b=P_ab",
            "diaconis_fulman_owned": "the shuffle/descent interpretation and sharp convergence analysis",
            "package_derived": "finite trace/determinant corollaries, exact spectral-projector convergence identity and executable regression ledger",
            "all_family_proof_owner": "Holte 1997, with convergence statements sourced to Diaconis--Fulman 2009",
            "code_role": "finite regression and release verification only; never the proof of the all-parameter theorem",
            "novelty_claimed": False,
            "external_review_claimed": False,
        },
        "theorem_lock": {
            "transition_window": "P_b(i,j)=b^{-n} times the number of digit vectors whose sum lies in [jb-i,(j+1)b-i-1]",
            "semigroup": "P_a P_b=P_ab for every a,b>=2; hence P_b^r=P_(b^r) for every r>=0",
            "spectrum": "P_b is diagonalizable with the n distinct eigenvalues 1,b^{-1},...,b^{-(n-1)} and base-independent left and right eigenvectors",
            "stationarity": "the unique stationary row is pi_n(j)=A(n,j)/n!, independent of b",
            "operator_corollaries": "tr(P_b^r)=sum_{k=0}^{n-1}b^{-rk}, det(I-zP_b)=product_{k=0}^{n-1}(1-zb^{-k}), and the characteristic polynomial is the matching product",
            "convergence": "the common spectral projectors give exact geometric convergence; Diaconis--Fulman Theorem 3.3 supplies the stated all-start total-variation upper bound for n>=3",
            "boundary": "n=1 is the one-state identity; prime and composite bases obey the identical semigroup and spectral theorem",
        },
        "route_a": {
            "tuple": ["A0_WEAK_ARITHMETIC_RELATION", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "qualifications": {
                "A0": "positional integer addition is intrinsic arithmetic, but its base-power semigroup is not a rational-prime primitive-orbit repetition law and supplies no log-p clock or arithmetic weights",
                "A1": "a stochastic transition matrix is not a deterministic primitive-orbit owner and supplies no target arithmetic weights",
                "A2": "the finite Markov determinant has no identified target divisor or source-native Euler product",
                "A3": "no target continuation, functional equation, counting law or Weil compression follows",
                "A4": "real simple spectrum permits formal similarity to a self-adjoint matrix after choosing an inner product, but no natural target quantization is selected",
            },
            "route_b_invocation_allowed": False,
        },
        "forbidden_claims": {
            "target_zero_table_used": False,
            "target_prime_table_used": False,
            "arithmetic_local_data_used": False,
            "euler_factor_claimed": False,
            "root_number_claimed": False,
            "automorphy_claimed": False,
            "target_divisor_claimed": False,
            "target_functional_equation_claimed": False,
            "hilbert_polya_operator_claimed": False,
            "route_b_invoked": False,
            "global_novelty_claimed": False,
            "external_peer_review_claimed": False,
        },
        "finite_regression": {
            "n_min": 1,
            "n_max": N_MAX,
            "base_min": min(BASES),
            "base_max": max(BASES),
            "case_count": len(cases),
            "transition_cell_count": sum(case["n"] ** 2 for case in cases),
            "power_trace_row_count": 7 * len(cases),
            "convergence_row_count": 5 * len(cases),
            "prime_base_case_count": sum(case["base_class"] == "prime" for case in cases),
            "composite_base_case_count": sum(case["base_class"] == "composite" for case in cases),
            "semigroup_base_min": min(SEMIGROUP_BASES),
            "semigroup_base_max": max(SEMIGROUP_BASES),
            "semigroup_tuple_count": semigroup_tuple_count,
            "semigroup_cell_count": semigroup_cell_count,
            "power_identity_tuple_count": power_tuple_count,
            "power_identity_cell_count": power_cell_count,
            "proof_boundary": "all finite matrices are regression sentinels; Holte's theorem carries the infinite quantifiers",
        },
        "cases": cases,
        "nonclaims": [
            "priority or novelty for the carries matrix, its spectrum, eigenvectors, stationary law, semigroup or convergence theory",
            "a deterministic primitive-orbit interpretation of the stochastic matrix",
            "a special theorem for prime bases or any rational-prime orbit semantics",
            "an Euler product, arithmetic local factor, root number or automorphy statement",
            "a target divisor, target functional equation, target counting law or Hilbert--Polya operator",
            "an all-parameter proof inferred from the finite regression census",
            "Route-B authorization, global literature priority, external peer review or an acceptance score",
        ],
    }
    document["payload_sha256"] = payload_digest(document)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(document, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C194_PRODUCER_PASS",
        "cases": len(cases),
        "transition_cells": document["finite_regression"]["transition_cell_count"],
        "semigroup_tuples": semigroup_tuple_count,
        "power_identity_tuples": power_tuple_count,
        "payload_sha256": document["payload_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
