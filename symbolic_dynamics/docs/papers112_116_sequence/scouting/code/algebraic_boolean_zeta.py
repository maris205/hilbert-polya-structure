#!/usr/bin/env python3
"""Exact spike for the Boolean-lattice zeta transform in characteristic p.

For f : 2^[n] -> F_q, the update is

    (Z f)(S) = sum_{T subseteq S} f(T).

The script works over prime fields for literal controls.  The formulas depend
only on the characteristic and therefore extend unchanged to q=p^a.
"""

from itertools import product
from math import comb


class Audit:
    def __init__(self):
        self.assertions = 0

    def check(self, condition, message="assertion failed"):
        self.assertions += 1
        if not condition:
            raise AssertionError(message)


AUDIT = Audit()


def zeta_vector(vector, n, p):
    out = list(vector)
    for bit in range(n):
        step = 1 << bit
        for mask in range(1 << n):
            if mask & step:
                out[mask] = (out[mask] + out[mask ^ step]) % p
    return tuple(out)


def iterate(vector, n, p, times):
    for _ in range(times):
        vector = zeta_vector(vector, n, p)
    return vector


def zeta_matrix(n, p):
    size = 1 << n
    matrix = [[0] * size for _ in range(size)]
    for row in range(size):
        sub = row
        while True:
            matrix[row][sub] = 1 % p
            if sub == 0:
                break
            sub = (sub - 1) & row
    return matrix


def rank_mod(matrix, p):
    a = [row[:] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    rank = 0
    for col in range(cols):
        pivot = next((i for i in range(rank, rows) if a[i][col] % p), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col] % p, -1, p)
        a[rank] = [(inv * x) % p for x in a[rank]]
        for i in range(rows):
            if i != rank and a[i][col] % p:
                factor = a[i][col] % p
                a[i] = [(x - factor * y) % p for x, y in zip(a[i], a[rank])]
        rank += 1
        if rank == rows:
            break
    return rank


def fixed_dimension_direct(n, p):
    z = zeta_matrix(n, p)
    size = 1 << n
    difference = [
        [(z[i][j] - (1 if i == j else 0)) % p for j in range(size)]
        for i in range(size)
    ]
    return size - rank_mod(difference, p)


def module_multiplicities(n, p):
    """Multiplicity of V_1,...,V_(p-1),V_p in V_2^(tensor n).

    V_r denotes the r-dimensional indecomposable F_p[C_p]-module.  The last
    return value is the multiplicity of the projective block V_p.
    """
    if n < 1:
        raise ValueError("n must be positive")
    if p == 2:
        return [0, 2 ** (n - 1)]
    nonprojective = [0] * p
    nonprojective[2] = 1
    projective = 0
    for _ in range(1, n):
        nxt = [0] * p
        for r in range(1, p):
            if r > 1:
                nxt[r - 1] += nonprojective[r]
            if r + 1 < p:
                nxt[r + 1] += nonprojective[r]
            # The r=p-1 contribution to V_p is stored after this loop.
        new_projective = 2 * projective + nonprojective[p - 1]
        nonprojective = nxt
        projective = new_projective
    return nonprojective[1:] + [projective]


def fixed_dimension_formula(n, p):
    if p == 2:
        return 2 ** (n - 1)
    multiplicities = module_multiplicities(n, p)
    return sum(multiplicities)


def matrix_power_entry_formula(row, col, m, p):
    r"""Entry (row,col) of Z^m: m^|row\col| when col subseteq row."""
    if col & ~row:
        return 0
    return pow(m % p, (row ^ col).bit_count(), p)


def audit_iterate_identity(n, p):
    size = 1 << n
    for col in range(size):
        basis = tuple(1 if i == col else 0 for i in range(size))
        for m in range(p + 1):
            literal = iterate(basis, n, p, m)
            formula = tuple(
                matrix_power_entry_formula(row, col, m, p)
                for row in range(size)
            )
            AUDIT.check(
                literal == formula,
                f"iterate-entry mismatch at n={n}, p={p}, m={m}, col={col}",
            )
    zero = (0,) * size
    probe = tuple(1 if i == 0 else 0 for i in range(size))
    AUDIT.check(iterate(probe, n, p, p) == probe)
    for m in range(1, p):
        AUDIT.check(iterate(probe, n, p, m) != probe)
    AUDIT.check(zeta_vector(zero, n, p) == zero)


def exhaustive_orbits(n, p):
    size = 1 << n
    fixed = 0
    period_p_points = 0
    for vector in product(range(p), repeat=size):
        image = zeta_vector(vector, n, p)
        if image == vector:
            fixed += 1
        else:
            AUDIT.check(iterate(vector, n, p, p) == vector)
            period_p_points += 1
    kappa = fixed_dimension_formula(n, p)
    AUDIT.check(fixed == p**kappa, f"fixed count mismatch n={n}, p={p}")
    AUDIT.check((period_p_points % p) == 0)
    cycles = (period_p_points // p) + fixed
    return fixed, cycles


def run_characteristic(p, max_rank_n):
    sequence = []
    first_anomaly = None
    for n in range(1, max_rank_n + 1):
        multiplicities = module_multiplicities(n, p)
        kappa = fixed_dimension_formula(n, p)
        sequence.append(kappa)
        if p == 2:
            weighted_dimension = 2 * multiplicities[-1]
        else:
            weighted_dimension = sum(
                r * multiplicities[r - 1] for r in range(1, p)
            ) + p * multiplicities[-1]
        AUDIT.check(weighted_dimension == 2**n, "module dimension mismatch")
        if n <= 7:
            direct = fixed_dimension_direct(n, p)
            AUDIT.check(
                direct == kappa,
                f"rank/module mismatch at n={n}, p={p}: {direct}!={kappa}",
            )
        char_zero_blocks = comb(n, n // 2)
        if first_anomaly is None and kappa != char_zero_blocks:
            first_anomaly = n

    for n in range(1, min(5, max_rank_n) + 1):
        audit_iterate_identity(n, p)

    exhaustive_lanes = []
    if p == 2:
        ns = range(1, 5)
    elif p == 3:
        ns = range(1, 4)
    else:
        ns = range(1, 3)
    for n in ns:
        fixed, cycles = exhaustive_orbits(n, p)
        exhaustive_lanes.append((n, fixed, cycles))

    print(
        f"p={p}: fixed dimensions n=1..{max_rank_n}: {sequence}; "
        f"first departure from C(n,floor(n/2))={first_anomaly}; "
        f"exhaustive (n,fixed,total cycles)={exhaustive_lanes}"
    )


def main():
    for p in (2, 3, 5, 7):
        run_characteristic(p, 12)
    # Adversarially probe the proposed sharp modular-anomaly threshold well
    # beyond the direct matrix-rank lanes.
    for p in (2, 3, 5, 7, 11, 13, 17, 19):
        for n in range(1, 2 * p - 1):
            AUDIT.check(
                fixed_dimension_formula(n, p) == comb(n, n // 2),
                f"premature modular anomaly at p={p}, n={n}",
            )
        n = 2 * p - 1
        AUDIT.check(
            fixed_dimension_formula(n, p) == comb(n, n // 2) + 1,
            f"first-anomaly formula failed at p={p}",
        )
    print(f"PASS: {AUDIT.assertions:,} exact assertions")


if __name__ == "__main__":
    main()
