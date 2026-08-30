#!/usr/bin/env python3
"""Exact pilot for a two-coordinate shifted-Cartier sum.

The full coefficient box is checked for small prime fields.  A separate
maximal-chain model checks the sharp modular nilpotency threshold farther
than full coefficient enumeration would be sensible.
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


def zero(n):
    return [[0] * n for _ in range(n)]


def add(a, b, p):
    return [[(x + y) % p for x, y in zip(arow, brow)] for arow, brow in zip(a, b)]


def scalar(c, a, p):
    return [[c * x % p for x in row] for row in a]


def matmul(a, b, p):
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


def nilpotency_index(operator, p):
    power = [row[:] for row in operator]
    for exponent in range(1, len(operator) + 2):
        if rank_mod(power, p) == 0:
            return exponent
        power = matmul(power, operator, p)
    raise AssertionError("operator did not become nilpotent")


def coefficient_operators(p, height):
    width = p**height
    size = width * width
    cx = zero(size)
    cy = zero(size)

    def index(i, j):
        return i * width + j

    for i in range(width):
        for j in range(width):
            source = index(i, j)
            if i % p == p - 1:
                cx[index((i - (p - 1)) // p, j)][source] = 1
            if j % p == p - 1:
                cy[index(i, (j - (p - 1)) // p)][source] = 1
    return cx, cy


def shift_chain(size):
    out = zero(size)
    for source in range(1, size):
        out[source - 1][source] = 1
    return out


def kronecker_sum_chain(size, p):
    shift = shift_chain(size)
    dimension = size * size
    out = zero(dimension)

    def index(i, j):
        return i * size + j

    for i in range(size):
        for j in range(size):
            source = index(i, j)
            if i > 0:
                out[index(i - 1, j)][source] += 1
            if j > 0:
                out[index(i, j - 1)][source] += 1
    return [[entry % p for entry in row] for row in out]


def least_p_power_at_least(number, p):
    out = 1
    while out < number:
        out *= p
    return out


def lucas_index(height, p):
    """Index from the last carry-free binomial coefficient in the box."""
    chain_size = height + 1
    last_nonzero = 0
    for exponent in range(2 * chain_size - 1):
        lower = max(0, exponent - height)
        upper = min(height, exponent)
        if any(comb(exponent, k) % p for k in range(lower, upper + 1)):
            last_nonzero = exponent
    return last_nonzero + 1


def first_window_index(height, p):
    if height >= p:
        raise ValueError("the first-window formula assumes h < p")
    return min(2 * height + 1, p)


def binomial_expansion(cx, cy, exponent, p):
    size = len(cx)
    out = zero(size)
    for k in range(exponent + 1):
        left = matpow(cx, k, p)
        right = matpow(cy, exponent - k, p)
        term = matmul(left, right, p)
        out = add(out, scalar(comb(exponent, k) % p, term, p), p)
    return out


def run_full_boxes():
    lanes = ((2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (5, 1))
    for p, height in lanes:
        cx, cy = coefficient_operators(p, height)
        operator = add(cx, cy, p)
        AUDIT.check(
            matmul(cx, cy, p) == matmul(cy, cx, p),
            f"coordinate Cartier operators do not commute at {(p, height)}",
        )
        for exponent in range(0, 2 * height + 2):
            AUDIT.check(
                matpow(operator, exponent, p)
                == binomial_expansion(cx, cy, exponent, p),
                f"binomial iterate identity failed at {(p, height, exponent)}",
            )
        actual = nilpotency_index(operator, p)
        AUDIT.check(
            actual == lucas_index(height, p),
            f"full-box nilpotency threshold mismatch at {(p, height)}",
        )
        print(
            f"full box p={p}, h={height}, dimension={p ** (2 * height):>3}: "
            f"nilpotency index={actual}"
        )


def run_maximal_chains():
    for p in (2, 3, 5, 7):
        for height in range(0, 9):
            operator = kronecker_sum_chain(height + 1, p)
            actual = nilpotency_index(operator, p)
            AUDIT.check(
            actual == lucas_index(height, p),
                f"maximal-chain threshold mismatch at {(p, height)}",
            )
            if height < p:
                AUDIT.check(
                    actual == first_window_index(height, p),
                    f"first modular window mismatch at {(p, height)}",
                )
                AUDIT.check(
                    matpow(operator, p, p) == zero((height + 1) ** 2),
                    f"freshman's-dream collapse failed at {(p, height)}",
                )

    actual = nilpotency_index(kronecker_sum_chain(9, 5), 5)
    naive = min(17, least_p_power_at_least(9, 5))
    AUDIT.check(actual == 15 and naive == 17, "missing second-window counterexample")


def main():
    run_full_boxes()
    run_maximal_chains()
    print(
        "FALSE CONJECTURE: two independent height-h coefficient chains always "
        "give depth 2h+1; binomial cancellation gives the last carry-free "
        "coefficient inside the h by h box.  Even the tempting least-p-power "
        "shortcut fails: (p,h)=(5,8) has index 15, not 17."
    )
    print(f"PASS: {AUDIT.assertions:,} exact assertions")


if __name__ == "__main__":
    main()
