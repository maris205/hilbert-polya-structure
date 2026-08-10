#!/usr/bin/env python3
"""Produce the exact HCS-C27 finite-Weil chronology certificate.

The program starts from the released C24 and C26 JSON certificates.  It
never replaces a chronological product by an average.  For every odd prime
``p`` it evaluates the genuine genus-two finite Weil character by Thomas's
formula

    Tr rho_p(g) = p^(k/2) gamma_p(1)^(4-k) Legendre(det sigma_g),

and records it in the exact quadratic basis ``1,G_p``, where

    G_p = sum_x exp(2*pi*i*(x^2/2)/p),  G_p^2 = Legendre(-1,p)*p.

The release has four logically different outputs:

* a finite-dimensional tensor argument upgrading the C26 scalar Bergman
  operator to an ordinary trace-class finite-Weil twist;
* exact local polynomials det(I-T rho_p(g)) for the frozen three-return
  chronology witness at p=3,5,7;
* a power-character scan, including a complete p=43 blind period;
* an integral symplectic conjugacy proving an all-prime/all-power collapse
  for the distinct C24-P076/P082 symbolic cycles.

Finite scans are labelled as such.  The Fredholm and conjugacy statements
are theorem-level consequences of the stated exact identities.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import platform
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Iterable

import sympy as sp


PROJECT = Path(__file__).resolve().parents[1]
HENON_ROOT = PROJECT.parent
C24_PATH = HENON_ROOT / "rauzy_metaplectic_obstruction" / "results" / "c24_certificate.json"
C25_PATH = HENON_ROOT / "agy_metaplectic_transfer_obstruction" / "results" / "c25_certificate.json"
C26_PATH = HENON_ROOT / "agy_holomorphic_slice_obstruction" / "results" / "c26_certificate.json"
DEFAULT_OUTPUT = PROJECT / "results" / "c27_certificate.json"

EXPECTED_SOURCE_HASHES = {
    "C24": "4b4fe5943262137eeeb3eda4de887725a0663402a1f39f8cc43e089bcc91e778",
    "C25": "a35cee22714abbb9dc9aadcc165720d1ff77aff3b7f29071f53a1b451760bd12",
    "C26": "1c0289b9b47e65e0603ea001be7cce263aea13d58c66e4609eac88edf8f7ce4a",
}

J_C26 = sp.Matrix(
    [[0, -1, 0, 0], [1, 0, -1, 1], [0, 1, 0, -1], [0, -1, 1, 0]]
)
J_STANDARD = sp.Matrix(
    [[0, 0, 1, 0], [0, 0, 0, 1], [-1, 0, 0, 0], [0, -1, 0, 0]]
)
DARBOUX_T = sp.Matrix(
    [[1, 1, 0, 1], [0, 0, -1, 0], [0, 1, 0, 0], [0, 0, 0, -1]]
)
C24_CONJUGATOR = sp.Matrix(
    [[0, 0, -1, 1], [-1, 0, 0, -1], [0, -2, 0, -1], [0, -1, 0, -1]]
)

GAMMA_STAR = "t" * 64 + "tbttbtbb" * 8
ODD_PRIMES_97 = tuple(int(value) for value in list(sp.primerange(3, 98)))
IDENTITY4 = sp.eye(4)

Pair = tuple[Fraction, Fraction]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--bridge-max-length", type=int, default=12)
    parser.add_argument("--power-window", type=int, default=24)
    return parser.parse_args()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_sha256(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def matrix_json(matrix: sp.MatrixBase) -> list[list[int]]:
    return [[int(matrix[row, column]) for column in range(matrix.cols)] for row in range(matrix.rows)]


def matrix_mod(matrix: sp.MatrixBase, p: int) -> sp.Matrix:
    return matrix.applyfunc(lambda value: int(value) % p)


def matmul_mod(left: sp.MatrixBase, right: sp.MatrixBase, p: int) -> sp.Matrix:
    return matrix_mod(left * right, p)


def legendre(value: int, p: int) -> int:
    if p == 2 or not sp.isprime(p):
        raise ValueError("finite Weil release supports odd prime moduli only")
    value %= p
    if value == 0:
        return 0
    residue = pow(value, (p - 1) // 2, p)
    if residue == 1:
        return 1
    if residue == p - 1:
        return -1
    raise AssertionError("Euler criterion failed")


def pivot_columns_mod(matrix: sp.MatrixBase, p: int) -> list[int]:
    rows = [[int(matrix[row, column]) % p for column in range(matrix.cols)] for row in range(matrix.rows)]
    pivot_row = 0
    pivots: list[int] = []
    for column in range(matrix.cols):
        pivot = next((row for row in range(pivot_row, matrix.rows) if rows[row][column]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        inverse = pow(rows[pivot_row][column], -1, p)
        rows[pivot_row] = [(value * inverse) % p for value in rows[pivot_row]]
        for row in range(matrix.rows):
            if row == pivot_row or rows[row][column] == 0:
                continue
            multiplier = rows[row][column]
            rows[row] = [
                (rows[row][index] - multiplier * rows[pivot_row][index]) % p
                for index in range(matrix.cols)
            ]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == matrix.rows:
            break
    return pivots


def determinant_mod(matrix: sp.MatrixBase, p: int) -> int:
    if matrix.rows == 0:
        return 1
    rows = [[int(matrix[row, column]) % p for column in range(matrix.cols)] for row in range(matrix.rows)]
    answer = 1
    for column in range(matrix.cols):
        pivot = next((row for row in range(column, matrix.rows) if rows[row][column]), None)
        if pivot is None:
            return 0
        if pivot != column:
            rows[column], rows[pivot] = rows[pivot], rows[column]
            answer = -answer
        pivot_value = rows[column][column] % p
        answer = answer * pivot_value % p
        inverse = pow(pivot_value, -1, p)
        for row in range(column + 1, matrix.rows):
            multiplier = rows[row][column] * inverse % p
            rows[row] = [
                (rows[row][index] - multiplier * rows[column][index]) % p
                for index in range(matrix.cols)
            ]
    return answer % p


def sigma_data(matrix: sp.MatrixBase, form: sp.MatrixBase, p: int) -> tuple[int, int, list[int]]:
    """Return k, det(sigma_g), and a quotient-basis column choice."""

    g = matrix_mod(matrix, p)
    h = matrix_mod(g - sp.eye(4), p)
    pivots = pivot_columns_mod(h, p)
    rank = len(pivots)
    kernel_dimension = 4 - rank
    if rank == 0:
        return kernel_dimension, 1, []
    complement = sp.eye(4)[:, pivots]
    quotient_form = matrix_mod(complement.T * h.T * form * complement, p)
    discriminant = determinant_mod(quotient_form, p)
    if discriminant == 0:
        raise AssertionError("Thomas quotient form is unexpectedly degenerate")
    return kernel_dimension, discriminant, pivots


def character_pair_from_invariants(kernel_dimension: int, eta_d: int, p: int) -> tuple[int, int]:
    eta_minus_one = legendre(-1, p)
    table = {
        0: (eta_d, 0),
        1: (0, eta_d * eta_minus_one),
        2: (eta_d * eta_minus_one * p, 0),
        3: (0, eta_d * p),
        4: (p * p, 0),
    }
    return table[kernel_dimension]


def thomas_character(matrix: sp.MatrixBase, form: sp.MatrixBase, p: int) -> dict[str, object]:
    if p == 2 or not sp.isprime(p):
        raise ValueError("Thomas character requires an odd prime in this release")
    kernel_dimension, discriminant, pivots = sigma_data(matrix, form, p)
    eta_d = legendre(discriminant, p)
    one, gauss = character_pair_from_invariants(kernel_dimension, eta_d, p)
    return {
        "p": p,
        "kernel_dimension": kernel_dimension,
        "sigma_discriminant_mod_p": discriminant,
        "sigma_quotient_pivot_columns": pivots,
        "legendre_sigma_discriminant": eta_d,
        "basis": f"1,G_{p}",
        "gauss_relation": f"G_{p}^2={legendre(-1, p) * p}",
        "exact_pair_one_gauss": [one, gauss],
        "absolute_value_squared": p**kernel_dimension,
    }


def character_key(matrix: sp.MatrixBase, form: sp.MatrixBase, p: int) -> tuple[int, int]:
    record = thomas_character(matrix, form, p)
    pair = record["exact_pair_one_gauss"]
    assert isinstance(pair, list)
    return int(pair[0]), int(pair[1])


def pair_add(left: Pair, right: Pair) -> Pair:
    return left[0] + right[0], left[1] + right[1]


def pair_multiply(left: Pair, right: Pair, p: int) -> Pair:
    gauss_square = legendre(-1, p) * p
    return (
        left[0] * right[0] + left[1] * right[1] * gauss_square,
        left[0] * right[1] + left[1] * right[0],
    )


def pair_conjugate(value: Pair, p: int) -> Pair:
    return value[0], legendre(-1, p) * value[1]


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def serialize_pair(value: Pair) -> list[str]:
    return [fraction_text(value[0]), fraction_text(value[1])]


def local_weil_polynomial(matrix: sp.MatrixBase, form: sp.MatrixBase, p: int) -> dict[str, object]:
    """Recover det(I-T rho_p(g)) from exact power characters by Newton sums."""

    degree = p * p
    reduced = matrix_mod(matrix, p)
    current = sp.eye(4)
    traces: list[Pair] = []
    for _ in range(degree):
        current = matmul_mod(current, reduced, p)
        one, gauss = character_key(current, form, p)
        traces.append((Fraction(one), Fraction(gauss)))

    coefficients: list[Pair] = [(Fraction(1), Fraction(0))]
    for index in range(1, degree + 1):
        total: Pair = (Fraction(0), Fraction(0))
        for power in range(1, index + 1):
            total = pair_add(total, pair_multiply(coefficients[index - power], traces[power - 1], p))
        coefficients.append((-total[0] / index, -total[1] / index))

    reciprocal = all(
        coefficients[index] == tuple(-value for value in pair_conjugate(coefficients[degree - index], p))
        for index in range(degree + 1)
    )
    if coefficients[-1] != (Fraction(-1), Fraction(0)) or not reciprocal:
        raise AssertionError("finite Weil local polynomial failed determinant-one reciprocity")
    serialized_coefficients = [serialize_pair(value) for value in coefficients]
    return {
        "p": p,
        "degree": degree,
        "basis": f"1,G_{p}",
        "gauss_relation": f"G_{p}^2={legendre(-1, p) * p}",
        "coefficient_order": "ascending powers of T",
        "coefficients_one_gauss": serialized_coefficients,
        "power_traces_one_gauss": [serialize_pair(value) for value in traces],
        "constant_coefficient": serialized_coefficients[0],
        "leading_coefficient": serialized_coefficients[-1],
        "conjugate_reciprocity_verified": reciprocal,
        "coefficient_sha256": canonical_sha256(serialized_coefficients),
    }


def characteristic_coefficients(matrix: sp.MatrixBase) -> list[int]:
    return [int(value) for value in matrix.charpoly().all_coeffs()]


def discriminant_at_one(matrix: sp.MatrixBase) -> int:
    return int((sp.eye(4) - matrix).det())


def factor_record(value: int) -> dict[str, object]:
    factors = {int(prime): int(exponent) for prime, exponent in sp.factorint(abs(value)).items()}
    squarefree = (-1 if value < 0 else 1) * math.prod(
        prime for prime, exponent in factors.items() if exponent % 2
    )
    return {
        "value": value,
        "factorization": {str(prime): exponent for prime, exponent in factors.items()},
        "squarefree_kernel": squarefree,
    }


def load_sources() -> tuple[dict[str, object], dict[str, object], dict[str, object], dict[str, object]]:
    paths = {"C24": C24_PATH, "C25": C25_PATH, "C26": C26_PATH}
    observed = {name: sha256(path) for name, path in paths.items()}
    if observed != EXPECTED_SOURCE_HASHES:
        raise AssertionError(f"source lock changed: {observed}")
    c24 = json.loads(C24_PATH.read_text(encoding="utf-8"))
    c25 = json.loads(C25_PATH.read_text(encoding="utf-8"))
    c26 = json.loads(C26_PATH.read_text(encoding="utf-8"))
    source_lock = {
        "files": {
            name: {"path": str(paths[name].relative_to(HENON_ROOT.parent)), "sha256": observed[name]}
            for name in paths
        },
        "chronology": "B_(e1...en)=B_en...B_e1; no chronological averaging",
        "finite_field_scope": "odd primes only",
        "additive_character": "psi_p(a)=exp(2*pi*i*a/p)",
        "full_fibre": "the full p^2-dimensional finite Weil representation",
    }
    return c24, c25, c26, source_lock


def c26_matrices(c26: dict[str, object]) -> dict[str, sp.Matrix]:
    source_branch = c26["source_locked_branch"]
    periodic = c26["scalar_periodic_trace_gate"]
    two = periodic["chronological_two_return_witness"]
    three = periodic["three_return_spectral_chronology_witness"]
    return {
        "gamma_star": sp.Matrix(source_branch["chronological_matrix_B"]),
        "second_branch": sp.Matrix(two["second_branch_chronological_matrix_B"]),
        "two_forward": sp.Matrix(two["two_return_chronological_matrix_B"]),
        "two_reverse": sp.Matrix(two["reversed_order_matrix_B"]),
        "third_branch": sp.Matrix(three["third_branch_chronological_matrix_B"]),
        "three_forward": sp.Matrix(three["forward_chronological_matrix_B"]),
        "three_reverse": sp.Matrix(three["reversed_chronological_matrix_B"]),
    }


def verify_c26_chronology(matrices: dict[str, sp.Matrix]) -> dict[str, object]:
    checks = {
        "two_forward_equals_second_times_gamma": matrices["two_forward"]
        == matrices["second_branch"] * matrices["gamma_star"],
        "two_reverse_equals_gamma_times_second": matrices["two_reverse"]
        == matrices["gamma_star"] * matrices["second_branch"],
        "three_forward_equals_third_second_gamma": matrices["three_forward"]
        == matrices["third_branch"] * matrices["second_branch"] * matrices["gamma_star"],
        "three_reverse_equals_gamma_second_third": matrices["three_reverse"]
        == matrices["gamma_star"] * matrices["second_branch"] * matrices["third_branch"],
    }
    symplectic = {
        name: matrix.T * J_C26 * matrix == J_C26 for name, matrix in matrices.items()
    }
    if not all(checks.values()) or not all(symplectic.values()):
        raise AssertionError("frozen C26 chronology or symplectic form failed")
    forward_coefficients = characteristic_coefficients(matrices["three_forward"])
    reverse_coefficients = characteristic_coefficients(matrices["three_reverse"])
    differences = [abs(left - right) for left, right in zip(forward_coefficients, reverse_coefficients)]
    nonzero = [value for value in differences if value]
    coefficient_difference_gcd = math.gcd(*nonzero)
    if coefficient_difference_gcd != 64:
        raise AssertionError("universal odd-prime chronology sentinel changed")
    return {
        "composition_checks": checks,
        "symplectic_checks": symplectic,
        "two_return_null_control": {
            "integer_matrices_different": matrices["two_forward"] != matrices["two_reverse"],
            "characteristic_polynomials_equal": characteristic_coefficients(matrices["two_forward"])
            == characteristic_coefficients(matrices["two_reverse"]),
            "all_representation_characters_equal": True,
            "reason": "Tr rho(AB)=Tr rho(BA) by trace cyclicity",
        },
        "three_return_positive_sentinel": {
            "integer_matrices_different": matrices["three_forward"] != matrices["three_reverse"],
            "forward_characteristic_coefficients": forward_coefficients,
            "reverse_characteristic_coefficients": reverse_coefficients,
            "nonzero_coefficient_difference_gcd": coefficient_difference_gcd,
            "characteristic_polynomials_different_mod_every_odd_prime": True,
        },
    }


def c24_control(c24: dict[str, object]) -> dict[str, object]:
    cycles = {row["id"]: row for row in c24["eventually_positive_cycles"]}
    form = sp.Matrix(c24["source_lock"]["J0"])
    left = sp.Matrix(cycles["C24-P076"]["base_trivialized_symplectic_matrix"])
    right = sp.Matrix(cycles["C24-P082"]["base_trivialized_symplectic_matrix"])
    conjugacy_checks = {
        "det_X_is_one": int(C24_CONJUGATOR.det()) == 1,
        "X_preserves_J0": C24_CONJUGATOR.T * form * C24_CONJUGATOR == form,
        "P082_X_equals_X_P076": right * C24_CONJUGATOR == C24_CONJUGATOR * left,
        "P076_symplectic": left.T * form * left == form,
        "P082_symplectic": right.T * form * right == form,
    }
    if not all(conjugacy_checks.values()):
        raise AssertionError("C24 integral symplectic conjugacy failed")

    left_order = list(cycles["C24-P076"]["central_first_return_branches"])
    right_order = list(cycles["C24-P082"]["central_first_return_branches"])
    same_branch_multiset = sorted(left_order) == sorted(right_order)
    cyclic_rotations = [left_order[offset:] + left_order[:offset] for offset in range(len(left_order))]
    not_cyclic_rotations = right_order not in cyclic_rotations
    if not same_branch_multiset or not not_cyclic_rotations:
        raise AssertionError("C24 symbolic noncyclic-order control failed")

    singular_left = sp.Matrix(cycles["C24-P014"]["base_trivialized_symplectic_matrix"])
    singular_right = sp.Matrix(cycles["C24-P016"]["base_trivialized_symplectic_matrix"])
    p3_left = thomas_character(singular_left, form, 3)
    p3_right = thomas_character(singular_right, form, 3)
    if p3_left["exact_pair_one_gauss"] == p3_right["exact_pair_one_gauss"]:
        raise AssertionError("singular-prime chronology refinement disappeared")

    groups: dict[tuple[int, ...], list[dict[str, object]]] = defaultdict(list)
    for row in c24["eventually_positive_cycles"]:
        groups[tuple(int(value) for value in row["characteristic_coefficients_descending"])].append(row)
    split_by_prime: dict[str, int] = {}
    split_classes: set[tuple[int, ...]] = set()
    singular_only = True
    for p in ODD_PRIMES_97:
        split_count = 0
        for characteristic, rows in groups.items():
            if len(rows) < 2:
                continue
            keys = {
                character_key(sp.Matrix(row["base_trivialized_symplectic_matrix"]), form, p)
                for row in rows
            }
            if len(keys) > 1:
                split_count += 1
                split_classes.add(characteristic)
                determinant_at_one = sum(characteristic)
                singular_only &= determinant_at_one == 0 or determinant_at_one % p == 0
        split_by_prime[str(p)] = split_count

    regular_discriminants = [
        int(row["det_I_minus_power"]["1"])
        for row in c24["eventually_positive_cycles"]
        if int(row["det_I_minus_power"]["1"]) != 0
    ]
    regular_squarefree = [factor_record(value)["squarefree_kernel"] for value in regular_discriminants]
    return {
        "source_form_J0": matrix_json(form),
        "integral_symplectic_conjugacy_collapse": {
            "left_id": "C24-P076",
            "right_id": "C24-P082",
            "left_central_first_return_order": left_order,
            "right_central_first_return_order": right_order,
            "same_branch_multiset": same_branch_multiset,
            "not_cyclic_rotations": not_cyclic_rotations,
            "left_matrix": matrix_json(left),
            "right_matrix": matrix_json(right),
            "conjugator_X": matrix_json(C24_CONJUGATOR),
            "checks": conjugacy_checks,
            "characteristic_coefficients": characteristic_coefficients(left),
            "consequence": "Theta_p(P076^r)=Theta_p(P082^r) for every odd p and every integer r",
            "scope": "all class-function fibres collapse this complete repetition tower",
        },
        "singular_prime_positive_control": {
            "left_id": "C24-P014",
            "right_id": "C24-P016",
            "common_characteristic_coefficients": characteristic_coefficients(singular_left),
            "common_det_I_minus_g": discriminant_at_one(singular_left),
            "p": 3,
            "left_character": p3_left,
            "right_character": p3_right,
            "characters_different": p3_left["exact_pair_one_gauss"] != p3_right["exact_pair_one_gauss"],
        },
        "census": {
            "cycle_count": len(c24["eventually_positive_cycles"]),
            "singular_cycle_count": sum(
                int(row["det_I_minus_power"]["1"]) == 0 for row in c24["eventually_positive_cycles"]
            ),
            "regular_cycle_count": len(regular_discriminants),
            "regular_distinct_discriminants": len(set(regular_discriminants)),
            "regular_distinct_squarefree_kernels": len(set(regular_squarefree)),
            "same_charpoly_classes_split_by_prime": split_by_prime,
            "split_class_union_count": len(split_classes),
            "all_observed_same_charpoly_splits_on_singular_mod_p_loci_only": singular_only,
        },
    }


def power_scan(
    left: sp.MatrixBase,
    right: sp.MatrixBase,
    form: sp.MatrixBase,
    primes: Iterable[int],
    maximum_power: int,
) -> dict[str, object]:
    rows: dict[str, object] = {}
    differences = 0
    equalities = 0
    first_difference: list[int] | None = None
    for p in primes:
        left_power = sp.eye(4)
        right_power = sp.eye(4)
        left_mod = matrix_mod(left, p)
        right_mod = matrix_mod(right, p)
        equal_powers: list[int] = []
        different_powers: list[int] = []
        for exponent in range(1, maximum_power + 1):
            left_power = matmul_mod(left_power, left_mod, p)
            right_power = matmul_mod(right_power, right_mod, p)
            equal = character_key(left_power, form, p) == character_key(right_power, form, p)
            if equal:
                equalities += 1
                equal_powers.append(exponent)
            else:
                differences += 1
                different_powers.append(exponent)
                candidate = [p, exponent]
                if first_difference is None or candidate < first_difference:
                    first_difference = candidate
        rows[str(p)] = {
            "equal_powers": equal_powers,
            "different_powers": different_powers,
            "first_different_power": different_powers[0] if different_powers else None,
        }
    patterns: dict[tuple[int, ...], list[int]] = defaultdict(list)
    for prime, record in rows.items():
        patterns[tuple(record["different_powers"])].append(int(prime))
    return {
        "maximum_power": maximum_power,
        "prime_count": len(tuple(primes)),
        "total_comparisons": maximum_power * len(tuple(primes)),
        "equal_comparisons": equalities,
        "different_comparisons": differences,
        "first_difference_lexicographic_p_then_r": first_difference,
        "per_prime": rows,
        "pattern_classes": [
            {"different_powers": list(pattern), "primes": sorted(prime_list)}
            for pattern, prime_list in sorted(patterns.items(), key=lambda item: (len(item[0]), item[0]))
        ],
    }


def first_character_difference(
    left: sp.MatrixBase,
    right: sp.MatrixBase,
    form: sp.MatrixBase,
    p: int,
    search_cap: int,
) -> int | None:
    """Return the first exact Weil-character difference through ``search_cap``."""

    left_power = sp.eye(4)
    right_power = sp.eye(4)
    left_mod = matrix_mod(left, p)
    right_mod = matrix_mod(right, p)
    for exponent in range(1, search_cap + 1):
        left_power = matmul_mod(left_power, left_mod, p)
        right_power = matmul_mod(right_power, right_mod, p)
        if character_key(left_power, form, p) != character_key(right_power, form, p):
            return exponent
    return None


def post_window_controls(
    left: sp.MatrixBase, right: sp.MatrixBase, form: sp.MatrixBase
) -> dict[str, object]:
    """Certify that the p=83 and p=89 24-power null windows end later."""

    expected = {83: 41, 89: 30}
    records: dict[str, object] = {}
    for p, search_cap in expected.items():
        first_difference = first_character_difference(left, right, form, p, search_cap)
        if first_difference != search_cap:
            raise AssertionError(f"late chronology control changed at p={p}: {first_difference}")
        records[str(p)] = {
            "short_window_maximum_power": 24,
            "characters_equal_through_short_window": first_character_difference(
                left, right, form, p, 24
            )
            is None,
            "search_cap": search_cap,
            "first_different_power": first_difference,
        }
    return records


def complete_period_collision(
    left: sp.MatrixBase,
    right: sp.MatrixBase,
    form: sp.MatrixBase,
    p: int,
    cap: int,
) -> dict[str, object]:
    identity = sp.eye(4)
    left_mod = matrix_mod(left, p)
    right_mod = matrix_mod(right, p)
    left_power = identity
    right_power = identity
    left_order = None
    right_order = None
    first_difference = None
    common_identity = None
    for exponent in range(1, cap + 1):
        left_power = matmul_mod(left_power, left_mod, p)
        right_power = matmul_mod(right_power, right_mod, p)
        if left_order is None and left_power == identity:
            left_order = exponent
        if right_order is None and right_power == identity:
            right_order = exponent
        if first_difference is None and character_key(left_power, form, p) != character_key(right_power, form, p):
            first_difference = exponent
        if left_power == identity and right_power == identity:
            common_identity = exponent
            break
    if common_identity is None:
        raise AssertionError("declared complete-period cap was too small")
    all_equal = first_difference is None
    return {
        "p": p,
        "left_matrix_order": left_order,
        "right_matrix_order": right_order,
        "first_common_identity_power": common_identity,
        "all_power_characters_equal": all_equal,
        "first_different_power": first_difference,
        "complete_period_proof": all_equal,
        "consequence": (
            "the finite-fibre polynomials det(I-T rho_p(left)) and det(I-T rho_p(right)) are equal; "
            "this does not identify the scalar Perron trace atoms"
            if all_equal
            else None
        ),
        "left_base_characteristic_coefficients_mod_p": [value % p for value in characteristic_coefficients(left)],
        "right_base_characteristic_coefficients_mod_p": [value % p for value in characteristic_coefficients(right)],
        "base_characteristic_polynomials_different_mod_p": [
            value % p for value in characteristic_coefficients(left)
        ]
        != [value % p for value in characteristic_coefficients(right)],
    }


def graph_edges(c26: dict[str, object]) -> dict[tuple[int, str], tuple[int, sp.Matrix]]:
    result: dict[tuple[int, str], tuple[int, sp.Matrix]] = {}
    for edge in c26["graph"]["edges"]:
        result[(int(edge["source"]), str(edge["type"]))] = (
            int(edge["target"]),
            sp.Matrix(edge["chronological_matrix"]),
        )
    if len(result) != 14:
        raise AssertionError("C26 graph is not the frozen seven-state graph")
    return result


def follow_graph_word(
    start_state: int,
    word: str,
    edges: dict[tuple[int, str], tuple[int, sp.Matrix]],
) -> tuple[int, sp.Matrix]:
    state = start_state
    product = sp.eye(4)
    for token in word:
        target, edge_matrix = edges[(state, token)]
        product = edge_matrix * product
        state = target
    return state, product


def first_returns(
    base_state: int,
    edges: dict[tuple[int, str], tuple[int, sp.Matrix]],
    maximum_length: int,
) -> list[str]:
    frontier = [(base_state, "")]
    returns: list[str] = []
    for _ in range(maximum_length):
        next_frontier: list[tuple[int, str]] = []
        for state, word in frontier:
            for token in ("t", "b"):
                target, _ = edges[(state, token)]
                extended = word + token
                if target == base_state:
                    returns.append(extended)
                else:
                    next_frontier.append((target, extended))
        frontier = next_frontier
    return returns


def agy_arithmetic_scan(
    c26: dict[str, object], matrices: dict[str, sp.Matrix], maximum_length: int
) -> dict[str, object]:
    edges = graph_edges(c26)
    end, gamma_matrix = follow_graph_word(4, GAMMA_STAR, edges)
    if end != 4 or gamma_matrix != matrices["gamma_star"]:
        raise AssertionError("gamma_star graph replay failed")
    returns = first_returns(4, edges, maximum_length)
    rows: list[dict[str, object]] = []
    for word in returns:
        bridge_end, bridge_matrix = follow_graph_word(4, word, edges)
        if bridge_end != 4:
            raise AssertionError("non-return entered the arithmetic scan")
        branch_matrix = gamma_matrix * bridge_matrix * gamma_matrix
        discriminant = discriminant_at_one(branch_matrix)
        signature = [
            0 if discriminant % p == 0 else legendre(discriminant, p) for p in ODD_PRIMES_97
        ]
        rows.append(
            {
                "bridge_word": word,
                "bridge_length": len(word),
                "det_I_minus_branch": discriminant,
                "legendre_signature_primes_3_to_97": signature,
                "characteristic_coefficients": characteristic_coefficients(branch_matrix),
            }
        )
    signature_keys = {tuple(row["legendre_signature_primes_3_to_97"]) for row in rows}
    discriminants = {int(row["det_I_minus_branch"]) for row in rows}
    characteristics = {tuple(row["characteristic_coefficients"]) for row in rows}
    sample_factorizations = {
        row["bridge_word"]: factor_record(int(row["det_I_minus_branch"]))
        for row in rows[:10]
    }
    return {
        "scope": {
            "base_state": 4,
            "branch_form": "gamma_star + first_return_bridge + gamma_star",
            "bridge_max_length": maximum_length,
            "finite_scan_is_all_length_theorem": False,
        },
        "odd_signature_primes": list(ODD_PRIMES_97),
        "branch_count": len(rows),
        "count_by_bridge_length": dict(sorted(Counter(row["bridge_length"] for row in rows).items())),
        "distinct_discriminants": len(discriminants),
        "distinct_characteristic_polynomials": len(characteristics),
        "distinct_legendre_signatures": len(signature_keys),
        "all_150_signatures_distinct": len(rows) == 150 and len(signature_keys) == 150,
        "sample_factorizations": sample_factorizations,
        "rows": rows,
        "interpretation": (
            "Finite evidence favours orbit-dependent quadratic fields rather than a small common conductor; "
            "this is not an all-length theorem."
        ),
    }


def published_discriminants(matrices: dict[str, sp.Matrix]) -> dict[str, object]:
    selected = {
        "gamma_star": matrices["gamma_star"],
        "two_return_forward": matrices["two_forward"],
        "three_return_forward": matrices["three_forward"],
        "three_return_reverse": matrices["three_reverse"],
    }
    records = {name: factor_record(discriminant_at_one(matrix)) for name, matrix in selected.items()}
    return {
        "records": records,
        "distinct_squarefree_kernels": len(
            {int(record["squarefree_kernel"]) for record in records.values()}
        ),
        "common_conductor_observed": False,
        "warning": "four examples cannot prove all-length conductor fragmentation",
    }


def finite_twist_theorem() -> dict[str, object]:
    return {
        "status": "PROVED_BY_FINITE_TENSOR_EXTENSION_OF_C26_THEOREM_3_2",
        "source_half_plane": "Re(s)>-sigma_0",
        "space": "H_p=A^2(Omega) tensor C^(p^2), for each fixed odd prime p",
        "operator": (
            "(L_(s,p)F)(z)=sum_gamma w_(s,gamma)(z) "
            "rho_p(g_gamma mod p) F(h_gamma z), with column fibres and left matrix action"
        ),
        "order_firewall": (
            "for forward Rauzy order beta_1,...,beta_n the transfer-operator factor order is "
            "beta_n,...,beta_1, hence the fibre is rho(g_beta_n)...rho(g_beta_1)="
            "rho(g_beta_n...g_beta_1)"
        ),
        "chronological_fibre": (
            "g_fwd=g_(beta_n)...g_(beta_1); evaluate Theta_p only after forming this product"
        ),
        "trace_class_argument": (
            "rho_p(gamma) is unitary on a p^2-dimensional fibre, so each branch trace norm is "
            "multiplied by p^2; the C26 locally uniform trace-norm sum remains finite for fixed p"
        ),
        "singular_values": "the C26 exponential singular-value bound persists with finite multiplicity p^2",
        "determinant": "D_p(s,u)=det_(H_p)(I-u L_(s,p))",
        "joint_holomorphy": "D_p is holomorphic on {Re(s)>-sigma_0} x C for each fixed odd p",
        "word_trace_atom": (
            "Tr T_(s,p,word)=Theta_p(g_word) * lambda_word^(-(s+1)) / "
            "chi_word'(lambda_word)"
        ),
        "repetition_warning": "use Theta_p(g_word^r), never Theta_p(g_word)^r",
        "character_nonzero": True,
        "character_modulus": "|Theta_p(g)|^2=|ker(g-I)|=p^k",
        "not_claimed": [
            "no p-to-infinity limit",
            "no unregularized product over primes",
            "no adelic Hilbert space",
            "no self-adjoint Hilbert-Polya operator",
            "no Riemann-zero correspondence",
        ],
    }


def generic_character_theorem() -> dict[str, object]:
    return {
        "status": "PROVED",
        "statement": (
            "For integral symplectic g with D_g=det(g-I) nonzero and every odd p not dividing D_g, "
            "Theta_p(g mod p)=Legendre(D_g,p)."
        ),
        "proof": (
            "p not dividing D_g implies ker(g-I)=0; Thomas's genus-two formula then reduces to "
            "the square class of det sigma_g=det(g-I)."
        ),
        "arithmetic_interpretation": (
            "good-prime traces form the quadratic character of the squarefree kernel of D_g; "
            "primes dividing D_g carry the singular Gauss corrections"
        ),
        "coarseness": "at every good prime the full p^2-dimensional trace is only +1 or -1",
    }


def scope_firewall() -> dict[str, object]:
    flags = {
        "chronology_averaged": False,
        "characters_multiplied_branchwise": False,
        "B_transpose_substituted_for_forward_homology_cocycle": False,
        "p_equals_2_included": False,
        "finite_power_window_promoted_to_all_power_theorem": False,
        "finite_bridge_scan_promoted_to_all_length_theorem": False,
        "metaplectic_edge_signs_added_over_finite_fields": False,
        "full_fibre_silently_replaced_by_parity_sector": False,
        "prime_family_called_one_intrinsic_operator": False,
        "Riemann_zero_match_claimed": False,
        "Route_B_used": False,
    }
    if any(flags.values()):
        raise AssertionError("scope firewall failed")
    return {
        "flags": flags,
        "positive_claim": (
            "a fixed-prime family of genuine finite-Weil Fredholm determinants with exact arithmetic traces"
        ),
        "negative_claim": (
            "class-function fibres cannot recover all symbolic chronology, and the bounded census exhibits arithmetic fragmentation"
        ),
    }


def run(bridge_max_length: int, power_window: int) -> dict[str, object]:
    c24, _c25, c26, source_lock = load_sources()
    if DARBOUX_T.det() != -1 or DARBOUX_T.T * J_C26 * DARBOUX_T != J_STANDARD:
        raise AssertionError("integral Darboux basis failed")
    matrices = c26_matrices(c26)
    chronology = verify_c26_chronology(matrices)

    small_prime_characters: dict[str, object] = {}
    local_polynomials: dict[str, object] = {}
    for p in (3, 5, 7):
        characters = {
            name: thomas_character(matrix, J_C26, p)
            for name, matrix in matrices.items()
        }
        small_prime_characters[str(p)] = {
            "fibre_dimension": p * p,
            "characters": characters,
            "two_forward_equals_reverse": characters["two_forward"]["exact_pair_one_gauss"]
            == characters["two_reverse"]["exact_pair_one_gauss"],
            "three_forward_differs_from_reverse": characters["three_forward"]["exact_pair_one_gauss"]
            != characters["three_reverse"]["exact_pair_one_gauss"],
        }
        forward_polynomial = local_weil_polynomial(matrices["three_forward"], J_C26, p)
        reverse_polynomial = local_weil_polynomial(matrices["three_reverse"], J_C26, p)
        local_polynomials[str(p)] = {
            "three_forward": forward_polynomial,
            "three_reverse": reverse_polynomial,
            "polynomials_different": forward_polynomial["coefficients_one_gauss"]
            != reverse_polynomial["coefficients_one_gauss"],
        }

    scan = power_scan(
        matrices["three_forward"],
        matrices["three_reverse"],
        J_C26,
        ODD_PRIMES_97,
        power_window,
    )
    late_controls = post_window_controls(
        matrices["three_forward"], matrices["three_reverse"], J_C26
    )
    collision_43 = complete_period_collision(
        matrices["three_forward"], matrices["three_reverse"], J_C26, 43, 925
    )
    if scan["different_comparisons"] != 328 or scan["equal_comparisons"] != 248:
        raise AssertionError("frozen p<=97, r<=24 power census changed")
    if not collision_43["complete_period_proof"]:
        raise AssertionError("p=43 full local-factor collision disappeared")

    return {
        "schema": "HCS-C27-FINITE-WEIL-DETERMINANT-V1",
        "candidate_id": "HCS-C27",
        "candidate_name": "AGY finite-Weil chronology determinant",
        "source_lock": source_lock,
        "conventions": {
            "symplectic_form_J0": matrix_json(J_C26),
            "darboux_basis_T": matrix_json(DARBOUX_T),
            "darboux_identity": "T^T J0 T = [[0,I2],[-I2,0]]",
            "additive_character": "psi_p(a)=exp(2*pi*i*a/p)",
            "gauss_sum": "G_p=sum_(x in F_p) psi_p(x^2/2)",
            "gauss_relation": "G_p^2=Legendre(-1,p)*p",
            "finite_group": "Sp(4,F_p), not PSp and not a metaplectic double cover",
            "chronology": "later forward returns multiply on the left",
        },
        "finite_twist_theorem": finite_twist_theorem(),
        "generic_good_prime_theorem": generic_character_theorem(),
        "c26_chronology_controls": chronology,
        "small_prime_exact_characters": small_prime_characters,
        "exact_local_weil_polynomials": local_polynomials,
        "c26_power_character_scan": scan,
        "c26_post_window_separation_controls": late_controls,
        "p43_complete_weil_fibre_polynomial_collision": collision_43,
        "c24_controls": c24_control(c24),
        "published_orbit_discriminants": published_discriminants(matrices),
        "agy_branch_arithmetic_scan": agy_arithmetic_scan(c26, matrices, bridge_max_length),
        "decisions": {
            "finite_weil_fredholm_gate": "PASS_FOR_EACH_FIXED_ODD_PRIME",
            "chronology_sensitivity_gate": "PASS_BUT_NOT_SEPARATING",
            "common_arithmetic_conductor_gate": "FAIL_IN_150_BRANCH_FINITE_SCAN",
            "intrinsic_global_Hilbert_Polya_gate": "FAIL_MODULUS_P_REMAINS_EXTERNAL",
            "next_action": "PIVOT_TO_GLOBAL_PRIME_ASSEMBLY_ONLY_IF_AN_INTRINSIC_ADELIC_MEASURE_IS_DERIVED",
            "route_B_authorized": False,
        },
        "scope_firewall": scope_firewall(),
        "runtime": {
            "python": platform.python_version(),
            "sympy": sp.__version__,
            "bridge_max_length": bridge_max_length,
            "power_window": power_window,
            "producer_sha256": sha256(Path(__file__)),
        },
        "material_passport": {
            "origin": "C27 independent finite-Weil gate",
            "origin_date": "2026-08-10",
            "origin_mode": "exact theorem plus source-locked finite computation",
            "verification_status": "PRODUCER_COMPLETE; INDEPENDENT_REPLAY_RECORDED_SEPARATELY",
            "version_label": "HCS-C27-v1",
        },
    }


def main() -> None:
    args = parse_args()
    report = run(args.bridge_max_length, args.power_window)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "output": str(args.output),
                "fixed_prime_fredholm": report["decisions"]["finite_weil_fredholm_gate"],
                "power_differences": report["c26_power_character_scan"]["different_comparisons"],
                "p43_full_collision": report["p43_complete_weil_fibre_polynomial_collision"]["complete_period_proof"],
                "c24_all_tower_collapse": report["c24_controls"]["integral_symplectic_conjugacy_collapse"]["checks"][
                    "P082_X_equals_X_P076"
                ],
                "agy_signature_count": report["agy_branch_arithmetic_scan"]["distinct_legendre_signatures"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
