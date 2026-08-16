#!/usr/bin/env python3
"""Exact producer-side surface discriminant and ODP witness replay for C58."""

from __future__ import annotations

import argparse
import hashlib
from itertools import product
import math
from pathlib import Path
from typing import Any

from c58_exact import (
    StrictDataError,
    atomic_write,
    canonical_json_bytes,
    canonical_leaf_bytes,
    deep_exact,
    reject_optimized_python,
    require_canonical_compact_json,
    strict_gzip_json,
)


CUBIC_TERMS = (
    (75081586157, (3, 0, 0, 0)),
    (-28576620789, (2, 1, 0, 0)),
    (-122000922135, (2, 0, 1, 0)),
    (-5364921951, (2, 0, 0, 1)),
    (164150208636, (1, 2, 0, 0)),
    (-415458334296, (1, 1, 1, 0)),
    (151070718312, (1, 1, 0, 1)),
    (1158143874300, (1, 0, 2, 0)),
    (114691988016, (1, 0, 1, 1)),
    (113572676646, (1, 0, 0, 2)),
    (6898957820, (0, 3, 0, 0)),
    (1132596902196, (0, 2, 1, 0)),
    (-30413540316, (0, 2, 0, 1)),
    (-2054867641020, (0, 1, 2, 0)),
    (151980984216, (0, 1, 1, 1)),
    (36794420832, (0, 1, 0, 2)),
    (2646295985484, (0, 0, 3, 0)),
    (560186573940, (0, 0, 2, 1)),
    (706181383584, (0, 0, 1, 2)),
    (1884468968, (0, 0, 0, 3)),
)

LARGE_PRIME = 14932047182473291995860108491583652133938007263719
FACTORIZATION = (
    (2, 64),
    (3, 43),
    (5, 7),
    (181, 24),
    (283, 1),
    (997, 24),
    (1801, 1),
    (2346241, 24),
    (LARGE_PRIME, 1),
)
WITNESSES = {
    283: {
        "hessian": 228,
        "point": [1, 66, 155, 125],
        "quotient": 212,
    },
    1801: {
        "hessian": 1387,
        "point": [1, 1437, 538, 511],
        "quotient": 818,
    },
    LARGE_PRIME: {
        "hessian": 6136116089260018682592250996037036352166217747437,
        "point": [
            1,
            13510103813129040670509336985505882430772547129082,
            9804662502886869685787960537224283370301790578288,
            2060004063224680714367389988490103248145804244874,
        ],
        "quotient": 11651769163508833344099877335703302197941640200357,
    },
}


def sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def compositions(total: int, length: int):
    return tuple(
        row for row in product(range(total + 1), repeat=length) if sum(row) == total
    )


def macaulay_rows():
    monomials = tuple(sorted(compositions(5, 4), reverse=True))
    column_index = {monomial: column for column, monomial in enumerate(monomials)}
    gradients = []
    for variable in range(4):
        gradient: dict[tuple[int, ...], int] = {}
        for coefficient, exponent in CUBIC_TERMS:
            if exponent[variable]:
                target = list(exponent)
                target[variable] -= 1
                key = tuple(target)
                gradient[key] = gradient.get(key, 0) + coefficient * exponent[variable]
        gradients.append(gradient)
    rows = []
    for alpha in monomials:
        variable = next(index for index, value in enumerate(alpha) if value >= 2)
        multiplier = list(alpha)
        multiplier[variable] -= 2
        row = [0] * len(monomials)
        for exponent, coefficient in gradients[variable].items():
            target = tuple(multiplier[index] + exponent[index] for index in range(4))
            row[column_index[target]] += coefficient
        rows.append(row)
    nonreduced = tuple(
        index
        for index, monomial in enumerate(monomials)
        if sum(value >= 2 for value in monomial) >= 2
    )
    if len(rows) != 56 or len(nonreduced) != 24:
        raise StrictDataError("Macaulay matrix dimensions changed")
    minor = [[rows[row][column] for column in nonreduced] for row in nonreduced]
    return rows, nonreduced, minor


def bareiss(values: list[list[int]]) -> int:
    matrix = [row[:] for row in values]
    size = len(matrix)
    if size == 0 or any(len(row) != size for row in matrix):
        raise StrictDataError("Bareiss input is not square")
    sign = 1
    previous = 1
    for pivot_index in range(size - 1):
        if matrix[pivot_index][pivot_index] == 0:
            swap = next(
                (
                    row
                    for row in range(pivot_index + 1, size)
                    if matrix[row][pivot_index]
                ),
                None,
            )
            if swap is None:
                return 0
            matrix[pivot_index], matrix[swap] = matrix[swap], matrix[pivot_index]
            sign = -sign
        pivot = matrix[pivot_index][pivot_index]
        for row in range(pivot_index + 1, size):
            for column in range(pivot_index + 1, size):
                numerator = (
                    matrix[row][column] * pivot
                    - matrix[row][pivot_index] * matrix[pivot_index][column]
                )
                if numerator % previous:
                    raise StrictDataError("Bareiss division was not exact")
                matrix[row][column] = numerator // previous
        previous = pivot
        for row in range(pivot_index + 1, size):
            matrix[row][pivot_index] = 0
    return sign * matrix[-1][-1]


def determinant(values: list[list[int]], engine: str) -> int:
    if engine == "bareiss":
        return bareiss(values)
    if engine == "flint":
        try:
            from flint import fmpz_mat
        except ImportError as exc:
            raise StrictDataError("python-flint is required for the FLINT engine") from exc
        return int(fmpz_mat(values).det())
    raise StrictDataError("unknown determinant engine")


def build_macaulay(engine: str) -> dict[str, Any]:
    rows, nonreduced, minor = macaulay_rows()
    numerator = determinant(rows, engine)
    denominator = determinant(minor, engine)
    if denominator == 0 or numerator % denominator:
        raise StrictDataError("extraneous determinant does not divide Macaulay determinant")
    resultant = numerator // denominator
    if resultant % (3**5):
        raise StrictDataError("resultant is not divisible by the cubic normalization 3^5")
    divided = resultant // (3**5)
    if divided != math.prod(prime**exponent for prime, exponent in FACTORIZATION):
        raise StrictDataError("divided discriminant factorization changed")
    return {
        "denominator_decimal_newline_sha256": sha256(
            (str(denominator) + "\n").encode("ascii")
        ),
        "divided_discriminant": divided,
        "divided_discriminant_decimal_newline_sha256": sha256(
            (str(divided) + "\n").encode("ascii")
        ),
        "extraneous_shape": [24, 24],
        "factorization": [[prime, exponent] for prime, exponent in FACTORIZATION],
        "matrix_shape": [56, 56],
        "nonreduced_indices": list(nonreduced),
        "numerator_decimal_newline_sha256": sha256(
            (str(numerator) + "\n").encode("ascii")
        ),
        "resultant_decimal_newline_sha256": sha256(
            (str(resultant) + "\n").encode("ascii")
        ),
    }


def evaluate(point: list[int], derivative_variables: tuple[int, ...] = ()) -> int:
    total = 0
    for coefficient, exponent in CUBIC_TERMS:
        factor = coefficient
        remaining = list(exponent)
        for variable in derivative_variables:
            if remaining[variable] == 0:
                factor = 0
                break
            factor *= remaining[variable]
            remaining[variable] -= 1
        if factor:
            factor *= math.prod(
                point[index] ** remaining[index] for index in range(4)
            )
            total += factor
    return total


def determinant3(matrix: list[list[int]], modulus: int) -> int:
    return (
        matrix[0][0]
        * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1]
        * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2]
        * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    ) % modulus


def solve_modular_linear(
    matrix: list[list[int]], right_hand_side: list[int], modulus: int
) -> list[int]:
    size = len(right_hand_side)
    if (
        size == 0
        or len(matrix) != size
        or any(len(row) != size for row in matrix)
    ):
        raise StrictDataError("modular linear system has wrong dimensions")
    augmented = [
        [value % modulus for value in matrix[row]]
        + [right_hand_side[row] % modulus]
        for row in range(size)
    ]
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if augmented[row][column]),
            None,
        )
        if pivot is None:
            raise StrictDataError("modular Hessian is singular")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        inverse_pivot = pow(augmented[column][column], -1, modulus)
        augmented[column] = [
            value * inverse_pivot % modulus for value in augmented[column]
        ]
        for row in range(size):
            if row == column:
                continue
            factor = augmented[row][column]
            augmented[row] = [
                (augmented[row][index] - factor * augmented[column][index])
                % modulus
                for index in range(size + 1)
            ]
    return [augmented[row][-1] for row in range(size)]


def normalized_groebner_basis(prime: int, chart: int):
    try:
        from sympy import groebner, symbols
    except ImportError as exc:
        raise StrictDataError("SymPy is required for the ODP replay") from exc
    variables = symbols("x0:4")
    polynomial = sum(
        coefficient
        * math.prod(variables[index] ** exponent[index] for index in range(4))
        for coefficient, exponent in CUBIC_TERMS
    )
    gradients = [polynomial.diff(variable) for variable in variables]
    substitutions = {variables[index]: 0 for index in range(chart)}
    substitutions[variables[chart]] = 1
    remaining = variables[chart + 1 :]
    equations = [gradient.subs(substitutions) for gradient in gradients]
    if not remaining:
        unit = any(int(equation) % prime for equation in equations)
        return ([[[1, []]]] if unit else []), unit
    basis_object = groebner(equations, *remaining, modulus=prime, order="grevlex")
    basis = [
        [
            [int(coefficient) % prime, list(exponents)]
            for exponents, coefficient in polynomial_object.terms()
        ]
        for polynomial_object in basis_object.polys
    ]
    unit = basis == [[[1, [0] * len(remaining)]]]
    return basis, unit


def build_reflection_witnesses() -> list[dict[str, Any]]:
    rows = []
    for prime in (283, 1801, LARGE_PRIME):
        fixed = WITNESSES[prime]
        point = fixed["point"]
        value = evaluate(point)
        gradient = [evaluate(point, (variable,)) % prime for variable in range(4)]
        hessian = [
            [evaluate(point, (left, right)) % prime for right in range(1, 4)]
            for left in range(1, 4)
        ]
        hessian_determinant = determinant3(hessian, prime)
        quotient = (value // prime) % prime
        if value % prime or gradient != [0, 0, 0, 0]:
            raise StrictDataError(f"reflection point is not singular modulo {prime}")
        if (
            hessian_determinant != fixed["hessian"]
            or quotient != fixed["quotient"]
            or not hessian_determinant
            or not quotient
        ):
            raise StrictDataError(f"transverse ODP witness changed at {prime}")
        affine_gradient_divided_by_prime = []
        for variable in range(1, 4):
            derivative = evaluate(point, (variable,))
            if derivative % prime:
                raise StrictDataError(
                    f"affine critical gradient is not divisible by {prime}"
                )
            affine_gradient_divided_by_prime.append((derivative // prime) % prime)
        correction = solve_modular_linear(
            hessian,
            [(-value) % prime for value in affine_gradient_divided_by_prime],
            prime,
        )
        lifted_point = [1] + [
            point[index + 1] + prime * correction[index] for index in range(3)
        ]
        prime_squared = prime * prime
        lifted_affine_gradient = [
            evaluate(lifted_point, (variable,)) % prime_squared
            for variable in range(1, 4)
        ]
        lifted_value = evaluate(lifted_point)
        if lifted_affine_gradient != [0, 0, 0]:
            raise StrictDataError(
                f"critical-point Hensel lift failed modulo {prime}^2"
            )
        if lifted_value % prime_squared != value % prime_squared:
            raise StrictDataError(
                f"critical-value Hensel congruence failed modulo {prime}^2"
            )
        if lifted_value % prime or lifted_value % prime_squared == 0:
            raise StrictDataError(
                f"smoothing parameter does not have valuation one at {prime}"
            )
        basis_hashes = []
        basis_lengths = []
        unit_ideals = []
        chart_bases = []
        for chart in range(4):
            basis, unit = normalized_groebner_basis(prime, chart)
            chart_bases.append(basis)
            basis_hashes.append(sha256(canonical_leaf_bytes(basis)))
            basis_lengths.append(len(basis))
            unit_ideals.append(unit)
        if basis_lengths != [3, 1, 1, 1] or unit_ideals != [False, True, True, True]:
            raise StrictDataError(f"singular locus is not one reduced point at {prime}")
        expected_chart0 = [
            [
                [1, [1 if variable == index else 0 for variable in range(3)]],
                [(-point[index + 1]) % prime, [0, 0, 0]],
            ]
            for index in range(3)
        ]
        if chart_bases[0] != expected_chart0:
            raise StrictDataError(
                f"chart-0 reduced Groebner basis is not the recorded point at {prime}"
            )
        if sha256(canonical_leaf_bytes(expected_chart0)) != basis_hashes[0]:
            raise StrictDataError(f"chart-0 reduced-basis digest changed at {prime}")
        rows.append(
            {
                "affine_chart": 0,
                "chart0_reduced_groebner_basis": expected_chart0,
                "chart_groebner_basis_lengths": basis_lengths,
                "chart_groebner_basis_sha256": basis_hashes,
                "chart_unit_ideals": unit_ideals,
                "gradient_mod_prime": gradient,
                "hessian_determinant_mod_prime": hessian_determinant,
                "point_x0_to_x3": point,
                "prime": prime,
                "total_space_quotient_mod_prime": quotient,
            }
        )
    return rows


def build_fragment(engine: str) -> dict[str, Any]:
    return {
        "cubic_terms": [
            [coefficient, list(exponents)] for coefficient, exponents in CUBIC_TERMS
        ],
        "macaulay": build_macaulay(engine),
        "reflection_witnesses": build_reflection_witnesses(),
    }


def compact_report(engine: str, fragment: dict[str, Any], evidence_raw: bytes | None):
    return {
        "divided_discriminant_decimal_newline_sha256": fragment["macaulay"][
            "divided_discriminant_decimal_newline_sha256"
        ],
        "engine": engine,
        "evidence_decompressed_sha256": (
            sha256(evidence_raw) if evidence_raw is not None else None
        ),
        "macaulay_sha256": sha256(canonical_leaf_bytes(fragment["macaulay"])),
        "reflection_affine_hessian_units": True,
        "reflection_chart0_reduced_point_bases_verified": True,
        "reflection_critical_points_hensel_lift_uniquely": True,
        "reflection_critical_values_congruent_to_integer_witness_mod_p_squared": True,
        "reflection_residue_characteristics_odd": True,
        "reflection_smoothing_parameter_valuation_exactly_one": True,
        "reflection_unique_geometric_singular_point_each_prime": True,
        "reflection_witnesses_sha256": sha256(
            canonical_leaf_bytes(fragment["reflection_witnesses"])
        ),
        "status": "PASS",
        "support": [prime for prime, _ in FACTORIZATION],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--engine", choices=("flint", "bareiss"), required=True)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--evidence", type=Path)
    modes.add_argument("--build-fragment", type=Path)
    arguments = parser.parse_args()
    reject_optimized_python()
    fragment = build_fragment(arguments.engine)
    evidence_raw = None
    if arguments.evidence is not None:
        evidence, evidence_raw, _ = strict_gzip_json(
            arguments.evidence,
            max_compressed_bytes=4_000_000,
            max_decompressed_bytes=8_000_000,
        )
        require_canonical_compact_json(evidence_raw)
        observed = {
            "cubic_terms": evidence.get("cubic_terms"),
            "macaulay": evidence.get("macaulay"),
            "reflection_witnesses": evidence.get("reflection_witnesses"),
        }
        if not deep_exact(observed, fragment):
            raise StrictDataError("arithmetic evidence disagrees with surface replay")
    else:
        atomic_write(arguments.build_fragment, canonical_json_bytes(fragment))
    report = compact_report(arguments.engine, fragment, evidence_raw)
    raw = canonical_leaf_bytes(report)
    print(raw.decode("utf-8"))
    print("report_sha256", sha256(raw))


if __name__ == "__main__":
    main()
