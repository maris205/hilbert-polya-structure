#!/usr/bin/env python3
"""Cheap exact spikes for four bad-characteristic algebraic updates.

Only prime fields are used.  Matrices act on column vectors, and every
calculation is performed with Python integers reduced modulo ``p``.
"""

from math import comb


class Audit:
    def __init__(self):
        self.assertions = 0

    def check(self, condition, message):
        self.assertions += 1
        if not condition:
            raise AssertionError(message)


AUDIT = Audit()


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def matmul(a, b, p):
    if not a or not b:
        return []
    bt = list(zip(*b))
    return [
        [sum(x * y for x, y in zip(row, col)) % p for col in bt]
        for row in a
    ]


def matpow(a, exponent, p):
    out = identity(len(a))
    base = [row[:] for row in a]
    while exponent:
        if exponent & 1:
            out = matmul(out, base, p)
        base = matmul(base, base, p)
        exponent //= 2
    return out


def rank_mod(a, p):
    work = [[x % p for x in row] for row in a]
    rows = len(work)
    cols = len(work[0]) if rows else 0
    pivot_row = 0
    for col in range(cols):
        pivot = next(
            (row for row in range(pivot_row, rows) if work[row][col]), None
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        inverse = pow(work[pivot_row][col], -1, p)
        work[pivot_row] = [(inverse * x) % p for x in work[pivot_row]]
        for row in range(rows):
            if row != pivot_row and work[row][col]:
                factor = work[row][col]
                work[row] = [
                    (x - factor * y) % p
                    for x, y in zip(work[row], work[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def subtract_identity(a, p):
    out = [row[:] for row in a]
    for i in range(len(out)):
        out[i][i] = (out[i][i] - 1) % p
    return out


def nilpotency_index(a, p):
    power = [row[:] for row in a]
    for exponent in range(1, len(a) + 2):
        if rank_mod(power, p) == 0:
            return exponent
        power = matmul(power, a, p)
    raise AssertionError("operator did not become zero within its dimension")


def boolean_zeta(n):
    size = 1 << n
    return [
        [int((subset & state) == subset) for subset in range(size)]
        for state in range(size)
    ]


def boolean_kappa_recurrence(n, p):
    if n == 0:
        return 1
    if p == 2:
        return 1 << (n - 1)
    multiplicities = [0] * (p + 1)
    multiplicities[2] = 1
    projective = 0
    if n == 1:
        return 1
    for _ in range(1, n):
        new = [0] * (p + 1)
        for r in range(1, p):
            new[r] = multiplicities[r - 1] + multiplicities[r + 1]
        projective = 2 * projective + multiplicities[p - 1]
        multiplicities = new
    return sum(multiplicities[1:p]) + projective


def run_boolean_zeta():
    for p, max_n in ((2, 7), (3, 6), (5, 5)):
        for n in range(max_n + 1):
            zeta = boolean_zeta(n)
            size = 1 << n
            fixed_dimension = size - rank_mod(subtract_identity(zeta, p), p)
            AUDIT.check(
                fixed_dimension == boolean_kappa_recurrence(n, p),
                f"Boolean fixed dimension mismatch at {(p, n)}",
            )
            AUDIT.check(
                matpow(zeta, p, p) == identity(size),
                f"Boolean zeta does not have p-power identity at {(p, n)}",
            )

    for p in (3, 5, 7, 11):
        for n in range(1, 2 * p - 1):
            AUDIT.check(
                boolean_kappa_recurrence(n, p) == comb(n, n // 2),
                f"premature Boolean modular anomaly at {(p, n)}",
            )
        AUDIT.check(
            boolean_kappa_recurrence(2 * p - 1, p)
            == comb(2 * p - 1, p - 1) + 1,
            f"missing first Boolean modular excess at p={p}",
        )


def hasse_matrix(n, p, level):
    step = p**level
    out = [[0] * (n + 1) for _ in range(n + 1)]
    for degree in range(step, n + 1):
        out[degree - step][degree] = comb(degree, step) % p
    return out


def base_p_digit(number, p, level):
    return (number // (p**level)) % p


def run_hasse_digit_filter():
    for p in (2, 3, 5, 7):
        for level in (0, 1, 2):
            step = p**level
            n = min(3 * step + p + 2, 70)
            hasse = hasse_matrix(n, p, level)
            AUDIT.check(
                matpow(hasse, p, p) == [[0] * (n + 1) for _ in range(n + 1)],
                f"Hasse p-nilpotence failed at {(p, level, n)}",
            )
            for t in range(1, p + 1):
                power = matpow(hasse, t, p)
                literal_nullity = n + 1 - rank_mod(power, p)
                digit_nullity = sum(
                    base_p_digit(k, p, level) < t for k in range(n + 1)
                )
                AUDIT.check(
                    literal_nullity == digit_nullity,
                    f"Hasse digit CDF mismatch at {(p, level, n, t)}",
                )

            for degree in range(n + 1):
                vector = [0] * (n + 1)
                vector[degree] = 1
                state = vector
                depth = 0
                while any(state):
                    state = [
                        sum(hasse[i][j] * state[j] for j in range(n + 1)) % p
                        for i in range(n + 1)
                    ]
                    depth += 1
                AUDIT.check(
                    depth == base_p_digit(degree, p, level) + 1,
                    f"Hasse monomial depth mismatch at {(p, level, degree)}",
                )


def finite_difference_matrix(n, p):
    out = [[0] * (n + 1) for _ in range(n + 1)]
    for degree in range(n + 1):
        for target in range(degree + 1):
            out[target][degree] = comb(degree, target) % p
        out[degree][degree] = (out[degree][degree] - 1) % p
    return out


def run_finite_difference():
    for p in (2, 3, 5, 7):
        for n in range(0, 2 * p + 4):
            delta = finite_difference_matrix(n, p)
            zero = [[0] * (n + 1) for _ in range(n + 1)]
            AUDIT.check(
                matpow(delta, p, p) == zero,
                f"finite difference p-nilpotence failed at {(p, n)}",
            )
            kernel_dimension = n + 1 - rank_mod(delta, p)
            AUDIT.check(
                kernel_dimension == n // p + 1,
                f"translation-invariant kernel mismatch at {(p, n)}",
            )
            AUDIT.check(
                nilpotency_index(delta, p) == min(n + 1, p),
                f"finite-difference depth mismatch at {(p, n)}",
            )


def jordan_commutator(d, p):
    size = d * d
    out = [[0] * size for _ in range(size)]

    def index(i, j):
        return i * d + j

    for i in range(d):
        for j in range(d):
            source = index(i, j)
            if i > 0:
                out[index(i - 1, j)][source] += 1
            if j + 1 < d:
                out[index(i, j + 1)][source] -= 1
    return [[entry % p for entry in row] for row in out]


def least_p_power_at_least(d, p):
    out = 1
    while out < d:
        out *= p
    return out


def run_jordan_commutator():
    for p in (2, 3, 5, 7):
        for d in range(1, 9):
            operator = jordan_commutator(d, p)
            expected = min(2 * d - 1, least_p_power_at_least(d, p))
            AUDIT.check(
                nilpotency_index(operator, p) == expected,
                f"commutator modular threshold mismatch at {(p, d)}",
            )
            power_p = matpow(operator, p, p)
            if d <= p:
                AUDIT.check(
                    power_p == [[0] * (d * d) for _ in range(d * d)],
                    f"restricted p-map identity failed at {(p, d)}",
                )

    actual = nilpotency_index(jordan_commutator(9, 5), 5)
    naive = min(17, least_p_power_at_least(9, 5))
    AUDIT.check(actual == 15 and naive == 17, "missing commutator carry counterexample")


def main():
    run_boolean_zeta()
    run_hasse_digit_filter()
    run_finite_difference()
    run_jordan_commutator()
    print("FALSE CONJECTURE A: characteristic-zero Boolean fixed dimensions persist "
          "past n=2p-2; first counterexample is n=2p-1.")
    print("FALSE CONJECTURE B: Hasse depth grows like degree/order; it is only "
          "the selected base-p digit plus one.")
    print("FALSE CONJECTURE C: a least-p-power shortcut controls every "
          "commutator depth; (p,d)=(5,9) has index 15, not 17, so the full "
          "Lucas carry pattern is needed.")
    print(f"PASS: {AUDIT.assertions:,} exact assertions")


if __name__ == "__main__":
    main()
