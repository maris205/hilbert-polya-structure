#!/usr/bin/env python3
"""Finite controls for the weighted Heisenberg congruence-nullity theorem.

The computations are regression checks.  The manuscript proof uses the
irreducible decomposition of the finite Heisenberg regular representation.
The non-split character fixture below works explicitly in F_4 and compares
an enumerated root-pair count with a gcd degree computed over F_2.
"""

from __future__ import annotations

from itertools import product


def rank_mod(matrix: list[list[int]], p: int) -> int:
    a = [[entry % p for entry in row] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        inv = pow(a[pivot_row][col], -1, p)
        a[pivot_row] = [(inv * value) % p for value in a[pivot_row]]
        for r in range(rows):
            if r == pivot_row or not a[r][col]:
                continue
            scale = a[r][col]
            a[r] = [
                (left - scale * right) % p
                for left, right in zip(a[r], a[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def determinant_mod(matrix: list[list[int]], p: int) -> int:
    a = [[entry % p for entry in row] for row in matrix]
    size = len(a)
    determinant = 1
    for col in range(size):
        pivot = next((r for r in range(col, size) if a[r][col]), None)
        if pivot is None:
            return 0
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            determinant = -determinant
        pivot_value = a[col][col]
        determinant = determinant * pivot_value % p
        inverse = pow(pivot_value, -1, p)
        for row in range(col + 1, size):
            if not a[row][col]:
                continue
            scale = a[row][col] * inverse % p
            for j in range(col, size):
                a[row][j] = (a[row][j] - scale * a[col][j]) % p
    return determinant % p


def primitive_ell_root(ell: int, p: int) -> int:
    root = next(
        value
        for value in range(2, p)
        if pow(value, ell, p) == 1 and value != 1
    )
    assert all(pow(root, j, p) != 1 for j in range(1, ell))
    return root


def clock_shift_block(
    ell: int, p: int, coefficients: tuple[int, int, int]
) -> list[list[int]]:
    alpha, beta, gamma = (value % p for value in coefficients)
    zeta = primitive_ell_root(ell, p)
    matrix = [[0] * ell for _ in range(ell)]
    for j in range(ell):
        matrix[j][j] = (alpha + beta * pow(zeta, j, p)) % p
        matrix[(j + 1) % ell][j] = (
            matrix[(j + 1) % ell][j] + gamma
        ) % p
    return matrix


def check_clock_shift_blocks() -> None:
    cases = [
        (3, 19, (1, 1, 1)),
        (3, 19, (1, 4, 5)),
        (5, 31, (1, 1, 1)),
        (5, 31, (1, 5, 7)),
    ]
    for ell, p, coefficients in cases:
        matrix = clock_shift_block(ell, p, coefficients)
        delta = sum(pow(value, ell, p) for value in coefficients) % p
        assert determinant_mod(matrix, p) == delta
        assert ell - rank_mod(matrix, p) == int(delta == 0)
    print("clock-shift determinant and exact nullity: PASS (four direct blocks)")


def trim(poly: list[int], p: int) -> list[int]:
    poly = [coefficient % p for coefficient in poly]
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def divmod_poly(a: list[int], b: list[int], p: int) -> tuple[list[int], list[int]]:
    remainder = trim(a[:], p)
    divisor = trim(b[:], p)
    quotient = [0] * max(1, len(remainder) - len(divisor) + 1)
    inv_lead = pow(divisor[-1], -1, p)
    while len(remainder) >= len(divisor) and remainder != [0]:
        shift = len(remainder) - len(divisor)
        scale = remainder[-1] * inv_lead % p
        quotient[shift] = scale
        for j, coefficient in enumerate(divisor):
            remainder[shift + j] = (remainder[shift + j] - scale * coefficient) % p
        remainder = trim(remainder, p)
    return trim(quotient, p), remainder


def gcd_degree(a: list[int], b: list[int], p: int) -> int:
    a = trim(a, p)
    b = trim(b, p)
    while b != [0]:
        _, remainder = divmod_poly(a, b, p)
        a, b = b, remainder
    return len(a) - 1


def heisenberg_product(
    left: tuple[int, int, int], right: tuple[int, int, int], ell: int
) -> tuple[int, int, int]:
    x, y, z = left
    u, v, w = right
    return ((x + u) % ell, (y + v) % ell, (z + w + x * v) % ell)


def full_matrix_nullity(
    ell: int, p: int, coefficients: tuple[int, int, int]
) -> int:
    alpha, beta, gamma = (value % p for value in coefficients)
    elements = list(product(range(ell), repeat=3))
    index = {element: i for i, element in enumerate(elements)}
    identity = (0, 0, 0)
    a = (1, 0, 0)
    b = (0, 1, 0)
    matrix: list[list[int]] = []
    for g in elements:
        row = [0] * len(elements)
        for coefficient, step in ((alpha, identity), (beta, a), (gamma, b)):
            h = heisenberg_product(g, step, ell)
            row[index[h]] = (row[index[h]] + coefficient) % p
        matrix.append(row)
    return len(elements) - rank_mod(matrix, p)


def polynomial_power_linear(alpha: int, beta: int, ell: int, p: int) -> list[int]:
    # Coefficients of (alpha + beta*t)^ell over F_p.
    from math import comb

    return [
        comb(ell, j) * pow(alpha, ell - j, p) * pow(beta, j, p) % p
        for j in range(ell + 1)
    ]


def f4_mul(left: int, right: int) -> int:
    """Multiply bit-polynomials modulo x^2+x+1 over F_2."""

    raw = 0
    for shift in range(2):
        if (right >> shift) & 1:
            raw ^= left << shift
    if raw & 0b100:
        raw ^= 0b111
    return raw


def f4_pow(value: int, exponent: int) -> int:
    out = 1
    while exponent:
        if exponent & 1:
            out = f4_mul(out, value)
        value = f4_mul(value, value)
        exponent //= 2
    return out


def check_nonsplit_character_enumeration() -> None:
    """Enumerate the ell=3 character equation over F_4, not F_2."""

    ell, p = 3, 2
    roots = [value for value in range(4) if f4_pow(value, ell) == 1]
    assert roots == [1, 2, 3]
    # In characteristic two, 1+u+v=0 is represented by XOR.
    solution_pairs = [(u, v) for u, v in product(roots, repeat=2) if 1 ^ u ^ v == 0]
    assert solution_pairs == [(2, 3), (3, 2)]

    torsion = [1, 0, 0, 1]  # t^3-1 = t^3+1 over F_2
    fermat_slice = polynomial_power_linear(1, 1, ell, p)
    fermat_slice[0] = (fermat_slice[0] + 1) % p
    ground_field_degree = gcd_degree(torsion, fermat_slice, p)
    assert ground_field_degree == len(solution_pairs) == 2
    print(
        "non-split character enumeration F4/F2: "
        "mu_3=[1,a,1+a] pairs=[(a,1+a),(1+a,a)] gcd_degree=2 PASS"
    )


def formula_nullity(
    ell: int, p: int, coefficients: tuple[int, int, int]
) -> int:
    alpha, beta, gamma = (value % p for value in coefficients)
    torsion = [(-1) % p] + [0] * (ell - 1) + [1]
    fermat_slice = polynomial_power_linear(alpha, beta, ell, p)
    fermat_slice[0] = (fermat_slice[0] + pow(gamma, ell, p)) % p
    one_dimensional = gcd_degree(torsion, fermat_slice, p)
    nonlinear_singular = (
        pow(alpha, ell, p) + pow(beta, ell, p) + pow(gamma, ell, p)
    ) % p == 0
    return one_dimensional + ell * (ell - 1) * int(nonlinear_singular)


def main() -> None:
    check_clock_shift_blocks()
    check_nonsplit_character_enumeration()

    # All coefficient triples have nonzero entries, and ell and p are distinct
    # odd/prime parameters as required by the theorem (p=2 is also allowed).
    cases = [
        (3, 2, (1, 1, 1)),
        (3, 5, (1, 1, 1)),
        (3, 5, (1, 1, 2)),
        (3, 5, (1, 2, 3)),
        (3, 7, (2, 3, 4)),
        (5, 2, (1, 1, 1)),
        (5, 3, (1, 1, 1)),
        (5, 7, (1, 2, 3)),
        (5, 11, (1, 1, 1)),
        (5, 11, (2, 3, 5)),
    ]
    for ell, p, coefficients in cases:
        observed = full_matrix_nullity(ell, p, coefficients)
        expected = formula_nullity(ell, p, coefficients)
        assert observed == expected, (ell, p, coefficients, observed, expected)
        print(
            f"PASS ell={ell} p={p} coefficients={coefficients} "
            f"nullity={observed}"
        )
    print("ALL WEIGHTED HEISENBERG CONTROLS PASS")


if __name__ == "__main__":
    main()
