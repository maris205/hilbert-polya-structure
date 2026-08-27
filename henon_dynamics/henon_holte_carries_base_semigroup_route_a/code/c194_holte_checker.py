#!/usr/bin/env python3
"""Independent inclusion--exclusion and linear-algebra checker for C194."""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import itertools
import json
import math
from pathlib import Path
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c194_holte_evidence.json"
SOURCE_COMMIT = "c3a5b9bbb3b6d0881f395abe4a01accd322f69cb"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
CHECKS = 0
_EULERIAN_CACHE: dict[int, list[int]] = {}
_TRANSITION_CACHE: dict[tuple[int, int], tuple[list[list[int]], list[list[Fraction]]]] = {}
_CHARACTERISTIC_CACHE: dict[tuple[int, int], list[Fraction]] = {}


def check(condition: bool, message: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def q(value: str | int) -> Fraction:
    return Fraction(value)


def qtext(value: Fraction | int) -> str:
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def identity(size: int) -> list[list[Fraction]]:
    return [[Fraction(int(i == j)) for j in range(size)] for i in range(size)]


def multiply(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    size = len(left)
    return [[sum((left[i][k] * right[k][j] for k in range(size)), Fraction()) for j in range(size)] for i in range(size)]


def matrix_power(matrix: list[list[Fraction]], exponent: int) -> list[list[Fraction]]:
    result = identity(len(matrix))
    for _ in range(exponent):
        result = multiply(result, matrix)
    return result


def matrix_trace(matrix: list[list[Fraction]]) -> Fraction:
    return sum((matrix[i][i] for i in range(len(matrix))), Fraction())


def transition_by_slack_inclusion(n: int, base: int) -> tuple[list[list[int]], list[list[Fraction]]]:
    """Use Holte's n+1-variable slack coefficient, not digit convolution."""
    if (n, base) in _TRANSITION_CACHE:
        return _TRANSITION_CACHE[(n, base)]
    numerators = []
    for carry_in in range(n):
        row = []
        for carry_out in range(n):
            degree = (carry_out + 1) * base - 1 - carry_in
            coefficient = 0
            if degree >= 0:
                for excluded in range(degree // base + 1):
                    top = degree - excluded * base + n
                    if top >= n:
                        coefficient += (-1) ** excluded * math.comb(n + 1, excluded) * math.comb(top, n)
            row.append(coefficient)
        numerators.append(row)
    denominator = base**n
    matrix = [[Fraction(value, denominator) for value in row] for row in numerators]
    _TRANSITION_CACHE[(n, base)] = (numerators, matrix)
    return numerators, matrix


def eulerian_by_permutations(n: int) -> list[int]:
    if n not in _EULERIAN_CACHE:
        row = [0] * n
        for permutation in itertools.permutations(range(n)):
            descents = sum(permutation[i] > permutation[i + 1] for i in range(n - 1))
            row[descents] += 1
        _EULERIAN_CACHE[n] = row
    return _EULERIAN_CACHE[n]


def characteristic_descending(matrix: list[list[Fraction]]) -> list[Fraction]:
    """Faddeev--LeVerrier coefficients [1,c1,...,cn]."""
    size = len(matrix)
    auxiliary = identity(size)
    coefficients = [Fraction(1)]
    for index in range(1, size + 1):
        product = multiply(matrix, auxiliary)
        coefficient = -matrix_trace(product) / index
        coefficients.append(coefficient)
        auxiliary = product
        for diagonal in range(size):
            auxiliary[diagonal][diagonal] += coefficient
    return coefficients


def total_variation(row: list[Fraction], stationary: list[Fraction]) -> Fraction:
    return sum((abs(left - right) for left, right in zip(row, stationary)), Fraction()) / 2


EXPECTED_SOURCE_LOCK = {
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
}

EXPECTED_SOURCES = [
    {
        "source_id": "H97", "authors": ["John M. Holte"],
        "title": "Carries, Combinatorics, and an Amazing Matrix",
        "journal": "The American Mathematical Monthly 104(2), 138--149", "year": 1997,
        "doi": "10.1080/00029890.1997.11990612", "stable_doi": "10.2307/2974981",
        "theorem_locators": ["Theorem 1", "Theorem 3", "Theorem 4"],
        "role": "transition formula, base-independent diagonalization, simple spectrum, Eulerian stationary law and semigroup",
    },
    {
        "source_id": "DF09", "authors": ["Persi Diaconis", "Jason Fulman"],
        "title": "Carries, shuffling, and symmetric functions",
        "journal": "Advances in Applied Mathematics 43(2), 176--196", "year": 2009,
        "doi": "10.1016/j.aam.2009.02.002",
        "theorem_locators": ["Theorem 1.1", "Theorem 3.1", "Theorem 3.3"],
        "role": "descent marginal interpretation and quantitative convergence bounds",
    },
]

EXPECTED_ATTRIBUTION = {
    "status": "CLASSICAL_THEOREM_REPRODUCED_WITH_EXACT_CERTIFICATE",
    "holte_owned": "the all-(n,b) transition formula, common eigenvectors, eigenvalues, stationary Eulerian row and P_a P_b=P_ab",
    "diaconis_fulman_owned": "the shuffle/descent interpretation and sharp convergence analysis",
    "package_derived": "finite trace/determinant corollaries, exact spectral-projector convergence identity and executable regression ledger",
    "all_family_proof_owner": "Holte 1997, with convergence statements sourced to Diaconis--Fulman 2009",
    "code_role": "finite regression and release verification only; never the proof of the all-parameter theorem",
    "novelty_claimed": False,
    "external_review_claimed": False,
}

EXPECTED_THEOREM = {
    "transition_window": "P_b(i,j)=b^{-n} times the number of digit vectors whose sum lies in [jb-i,(j+1)b-i-1]",
    "semigroup": "P_a P_b=P_ab for every a,b>=2; hence P_b^r=P_(b^r) for every r>=0",
    "spectrum": "P_b is diagonalizable with the n distinct eigenvalues 1,b^{-1},...,b^{-(n-1)} and base-independent left and right eigenvectors",
    "stationarity": "the unique stationary row is pi_n(j)=A(n,j)/n!, independent of b",
    "operator_corollaries": "tr(P_b^r)=sum_{k=0}^{n-1}b^{-rk}, det(I-zP_b)=product_{k=0}^{n-1}(1-zb^{-k}), and the characteristic polynomial is the matching product",
    "convergence": "the common spectral projectors give exact geometric convergence; Diaconis--Fulman Theorem 3.3 supplies the stated all-start total-variation upper bound for n>=3",
    "boundary": "n=1 is the one-state identity; prime and composite bases obey the identical semigroup and spectral theorem",
}

EXPECTED_ROUTE = {
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
}

EXPECTED_FORBIDDEN = {
    "target_zero_table_used": False, "target_prime_table_used": False,
    "arithmetic_local_data_used": False, "euler_factor_claimed": False,
    "root_number_claimed": False, "automorphy_claimed": False,
    "target_divisor_claimed": False, "target_functional_equation_claimed": False,
    "hilbert_polya_operator_claimed": False, "route_b_invoked": False,
    "global_novelty_claimed": False, "external_peer_review_claimed": False,
}

EXPECTED_NONCLAIMS = [
    "priority or novelty for the carries matrix, its spectrum, eigenvectors, stationary law, semigroup or convergence theory",
    "a deterministic primitive-orbit interpretation of the stochastic matrix",
    "a special theorem for prime bases or any rational-prime orbit semantics",
    "an Euler product, arithmetic local factor, root number or automorphy statement",
    "a target divisor, target functional equation, target counting law or Hilbert--Polya operator",
    "an all-parameter proof inferred from the finite regression census",
    "Route-B authorization, global literature priority, external peer review or an acceptance score",
]


def verify(document: dict[str, Any]) -> int:
    global CHECKS
    CHECKS = 0
    expected_top = {
        "schema", "candidate_id", "evaluation_date", "source_commit", "evaluator", "scope_literal",
        "source_lock", "source_registry", "attribution", "theorem_lock", "route_a", "forbidden_claims",
        "finite_regression", "cases", "nonclaims", "payload_sha256",
    }
    check(set(document) == expected_top, "top-level exact map")
    check(document["schema"] == "hcs-c194-holte-carries-evidence-v1", "schema")
    check(document["candidate_id"] == "HCS-C194", "candidate")
    check(document["evaluation_date"] == "2026-08-27", "date")
    check(document["source_commit"] == SOURCE_COMMIT, "commit")
    check(document["evaluator"] == {"version": "0.2.0", "path": "flow_systems/skills/route-a-evaluator.md", "sha256": EVALUATOR_SHA256}, "evaluator exact map")
    check(document["scope_literal"] == SCOPE, "scope")
    check(document["source_lock"] == EXPECTED_SOURCE_LOCK, "source lock exact map")
    check(document["source_registry"] == EXPECTED_SOURCES, "source registry exact population")
    check(document["attribution"] == EXPECTED_ATTRIBUTION, "attribution exact map")
    check(document["theorem_lock"] == EXPECTED_THEOREM, "theorem exact map")
    check(document["route_a"] == EXPECTED_ROUTE, "route exact map")
    check(document["forbidden_claims"] == EXPECTED_FORBIDDEN, "forbidden exact map")
    check(document["nonclaims"] == EXPECTED_NONCLAIMS, "nonclaims exact population")

    payload = dict(document)
    claimed_digest = payload.pop("payload_sha256")
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    check(claimed_digest == sha256(canonical).hexdigest(), "canonical payload hash")

    cases = document["cases"]
    check(len(cases) == 72, "case population")
    transition_cells = 0
    power_rows = 0
    convergence_rows = 0
    prime_cases = 0
    composite_cases = 0
    for case_index, case in enumerate(cases):
        expected_keys = {
            "n", "base", "base_class", "denominator", "transition_numerators", "transition_matrix",
            "eulerian_numbers", "stationary_distribution", "eigenvalues", "charpoly_ascending",
            "det_I_minus_zP_ascending", "trace", "power_traces", "convergence",
        }
        check(set(case) == expected_keys, f"case {case_index} exact map")
        n = case_index // 9 + 1
        base = case_index % 9 + 2
        check(case["n"] == n and case["base"] == base, f"case {case_index} ordering")
        classification = "prime" if base in {2, 3, 5, 7} else "composite"
        check(case["base_class"] == classification, f"case {case_index} base class")
        prime_cases += classification == "prime"
        composite_cases += classification == "composite"
        check(case["denominator"] == str(base**n), f"case {case_index} denominator")

        numerators, matrix = transition_by_slack_inclusion(n, base)
        check(len(case["transition_numerators"]) == n, f"case {case_index} numerator rows")
        check(len(case["transition_matrix"]) == n, f"case {case_index} matrix rows")
        for i in range(n):
            check(len(case["transition_numerators"][i]) == n, f"case {case_index} numerator columns")
            check(len(case["transition_matrix"][i]) == n, f"case {case_index} matrix columns")
            for j in range(n):
                check(case["transition_numerators"][i][j] == numerators[i][j], f"case {case_index} numerator {i},{j}")
                check(q(case["transition_matrix"][i][j]) == matrix[i][j], f"case {case_index} matrix {i},{j}")
                transition_cells += 1
            check(sum(matrix[i], Fraction()) == 1, f"case {case_index} stochastic row {i}")

        eulerian = eulerian_by_permutations(n)
        stationary = [Fraction(value, math.factorial(n)) for value in eulerian]
        check(case["eulerian_numbers"] == [str(value) for value in eulerian], f"case {case_index} Eulerian")
        check([q(value) for value in case["stationary_distribution"]] == stationary, f"case {case_index} stationary serialization")
        check(sum(stationary, Fraction()) == 1, f"case {case_index} stationary mass")
        product = [sum((stationary[i] * matrix[i][j] for i in range(n)), Fraction()) for j in range(n)]
        for j in range(n):
            check(product[j] == stationary[j], f"case {case_index} stationary equation {j}")

        eigenvalues = [Fraction(1, base**index) for index in range(n)]
        check([q(value) for value in case["eigenvalues"]] == eigenvalues, f"case {case_index} spectrum")
        check(len(set(eigenvalues)) == n, f"case {case_index} simple spectrum")
        if (n, base) not in _CHARACTERISTIC_CACHE:
            _CHARACTERISTIC_CACHE[(n, base)] = characteristic_descending(matrix)
        coefficients = _CHARACTERISTIC_CACHE[(n, base)]
        check([q(value) for value in case["charpoly_ascending"]] == list(reversed(coefficients)), f"case {case_index} charpoly")
        check([q(value) for value in case["det_I_minus_zP_ascending"]] == coefficients, f"case {case_index} determinant")
        check(q(case["trace"]) == matrix_trace(matrix) == sum(eigenvalues, Fraction()), f"case {case_index} trace")

        check(len(case["power_traces"]) == 7, f"case {case_index} power row population")
        current = identity(n)
        for exponent, row in enumerate(case["power_traces"]):
            check(set(row) == {"power", "direct", "spectral"}, f"case {case_index} power map")
            check(row["power"] == exponent, f"case {case_index} power index")
            if exponent:
                current = multiply(current, matrix)
            direct = matrix_trace(current)
            spectral = sum((value**exponent for value in eigenvalues), Fraction())
            check(q(row["direct"]) == direct, f"case {case_index} direct power trace")
            check(q(row["spectral"]) == spectral == direct, f"case {case_index} spectral power trace")
            power_rows += 1

        check(len(case["convergence"]) == 5, f"case {case_index} convergence population")
        for exponent, row in enumerate(case["convergence"], start=1):
            check(set(row) == {"power", "from_zero_distribution", "from_last_distribution", "state_total_variation", "worst_total_variation", "theorem_3_3_bounds"}, f"case {case_index} convergence map")
            check(row["power"] == exponent, f"case {case_index} convergence power")
            current = matrix_power(matrix, exponent)
            distances = [total_variation(state_row, stationary) for state_row in current]
            check([q(value) for value in row["from_zero_distribution"]] == current[0], f"case {case_index} zero distribution")
            check([q(value) for value in row["from_last_distribution"]] == current[-1], f"case {case_index} last distribution")
            check([q(value) for value in row["state_total_variation"]] == distances, f"case {case_index} TV vector")
            check(q(row["worst_total_variation"]) == max(distances), f"case {case_index} worst TV")
            if n >= 3:
                bounds = [Fraction(n - 1, 2 * base**exponent) + Fraction(i, base**exponent) for i in range(n)]
                check([q(value) for value in row["theorem_3_3_bounds"]] == bounds, f"case {case_index} convergence bounds")
                for state in range(n):
                    check(distances[state] <= bounds[state], f"case {case_index} convergence inequality {state}")
            else:
                check(row["theorem_3_3_bounds"] == [], f"case {case_index} small-n bound boundary")
            convergence_rows += 1

    semigroup_tuples = 0
    semigroup_cells = 0
    for n in range(1, 9):
        for a in range(2, 9):
            _, left = transition_by_slack_inclusion(n, a)
            for b in range(2, 9):
                _, right = transition_by_slack_inclusion(n, b)
                _, combined = transition_by_slack_inclusion(n, a * b)
                observed = multiply(left, right)
                for i in range(n):
                    for j in range(n):
                        check(observed[i][j] == combined[i][j], f"semigroup {n},{a},{b},{i},{j}")
                        semigroup_cells += 1
                semigroup_tuples += 1

    power_tuples = 0
    power_cells = 0
    for n in range(1, 9):
        for base, exponent in ([(base, 2) for base in range(2, 11)] + [(base, 3) for base in range(2, 5)]):
            _, matrix = transition_by_slack_inclusion(n, base)
            _, expected = transition_by_slack_inclusion(n, base**exponent)
            observed = matrix_power(matrix, exponent)
            for i in range(n):
                for j in range(n):
                    check(observed[i][j] == expected[i][j], f"power identity {n},{base},{exponent},{i},{j}")
                    power_cells += 1
            power_tuples += 1

    expected_finite = {
        "n_min": 1, "n_max": 8, "base_min": 2, "base_max": 10,
        "case_count": 72, "transition_cell_count": transition_cells,
        "power_trace_row_count": power_rows, "convergence_row_count": convergence_rows,
        "prime_base_case_count": prime_cases, "composite_base_case_count": composite_cases,
        "semigroup_base_min": 2, "semigroup_base_max": 8,
        "semigroup_tuple_count": semigroup_tuples, "semigroup_cell_count": semigroup_cells,
        "power_identity_tuple_count": power_tuples, "power_identity_cell_count": power_cells,
        "proof_boundary": "all finite matrices are regression sentinels; Holte's theorem carries the infinite quantifiers",
    }
    check(document["finite_regression"] == expected_finite, "finite aggregate exact map")
    return CHECKS


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else EVIDENCE
    document = json.loads(path.read_text())
    assertions = verify(document)
    print(json.dumps({
        "status": "C194_CHECKER_PASS",
        "assertions": assertions,
        "cases": len(document["cases"]),
        "transition_cells": document["finite_regression"]["transition_cell_count"],
        "semigroup_tuples": document["finite_regression"]["semigroup_tuple_count"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
