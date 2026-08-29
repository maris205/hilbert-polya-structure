#!/usr/bin/env python3
"""Exact control for Drazin-inverse dynamics on small matrix algebras.

This is a deliberately hostile comparison spike: the formulas are clean, but
the scouting report still subjects the system to owner and internal-collision
gates.
"""

from collections import Counter, defaultdict
from itertools import product


class Audit:
    def __init__(self):
        self.assertions = 0

    def check(self, condition, message="assertion failed"):
        self.assertions += 1
        if not condition:
            raise AssertionError(message)


AUDIT = Audit()


def eye(d):
    return tuple(1 if i == j else 0 for i in range(d) for j in range(d))


def zero(d):
    return (0,) * (d * d)


def matmul(a, b, d, q):
    return tuple(
        sum(a[i * d + k] * b[k * d + j] for k in range(d)) % q
        for i in range(d)
        for j in range(d)
    )


def matpow(a, n, d, q):
    out = eye(d)
    base = a
    while n:
        if n & 1:
            out = matmul(out, base, d, q)
        base = matmul(base, base, d, q)
        n //= 2
    return out


def rank(a, d, q):
    rows = [[a[i * d + j] % q for j in range(d)] for i in range(d)]
    r = 0
    for col in range(d):
        pivot = next((i for i in range(r, d) if rows[i][col]), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        scale = pow(rows[r][col], -1, q)
        rows[r] = [(scale * x) % q for x in rows[r]]
        for i in range(d):
            if i != r and rows[i][col]:
                scale = rows[i][col]
                rows[i] = [(x - scale * y) % q for x, y in zip(rows[i], rows[r])]
        r += 1
    return r


def drazin_from_powers(a, d, q):
    """Return (A^D, power-index, eventual period) from the monogenic semigroup."""
    seen = {a: 1}
    x = a
    exponent = 1
    while True:
        x = matmul(x, a, d, q)
        exponent += 1
        if x in seen:
            index = seen[x]
            period = exponent - index
            break
        seen[x] = exponent
    e = index
    while e % period != (period - 1) % period:
        e += 1
    return matpow(a, e, d, q), index, period


def gl_order(d, q):
    ans = 1
    for i in range(d):
        ans *= q**d - q**i
    return ans


def qbinom(n, k, q):
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator *= q ** (n - i) - 1
        denominator *= q ** (k - i) - 1
    return numerator // denominator


def involution_count(d, q):
    if q % 2:
        return sum(qbinom(d, a, q) * q ** (a * (d - a)) for a in range(d + 1))
    return sum(
        qbinom(d, s, q) * qbinom(d - s, s, q) * gl_order(s, q)
        for s in range(d // 2 + 1)
    )


def core_count(d, q):
    return sum(
        qbinom(d, r, q) * q ** (r * (d - r)) * gl_order(r, q)
        for r in range(d + 1)
    )


def fixed_count(d, q):
    return sum(
        qbinom(d, r, q) * q ** (r * (d - r)) * involution_count(r, q)
        for r in range(d + 1)
    )


def run_lane(q, d):
    matrices = list(product(range(q), repeat=d * d))
    step = {}
    indices = {}
    fibres = defaultdict(int)
    for a in matrices:
        b, index, period = drazin_from_powers(a, d, q)
        step[a] = b
        indices[a] = index
        fibres[b] += 1
        AUDIT.check(matmul(a, b, d, q) == matmul(b, a, d, q), "AB != BA")
        AUDIT.check(matmul(matmul(b, a, d, q), b, d, q) == b, "BAB != B")
        lhs = matmul(matpow(a, index + 1, d, q), b, d, q)
        AUDIT.check(lhs == matpow(a, index, d, q), "Drazin power identity failed")
        AUDIT.check(period >= 1 and index >= 1)

    core = [a for a in matrices if rank(a, d, q) == rank(matmul(a, a, d, q), d, q)]
    core_set = set(core)
    fixed = 0
    cycles = Counter()
    seen = set()
    for a in matrices:
        b = step[a]
        AUDIT.check(b in core_set, "Drazin image is not group-invertible")
        AUDIT.check(step[step[step[a]]] == step[a], "T^3 != T")
        fixed += b == a
    for a in core:
        AUDIT.check(step[step[a]] == a, "core action is not an involution")
        if a not in seen:
            b = step[a]
            length = 1 if b == a else 2
            cycles[length] += 1
            seen.add(a)
            seen.add(b)

    AUDIT.check(len(core) == core_count(d, q), "core formula mismatch")
    AUDIT.check(fixed == fixed_count(d, q), "fixed formula mismatch")
    AUDIT.check(cycles[1] == fixed)
    AUDIT.check(cycles[2] == (len(core) - fixed) // 2)
    for b in core:
        r = rank(b, d, q)
        expected = q ** ((d - r) * (d - r - 1))
        AUDIT.check(fibres[b] == expected, "rank-uniform fibre formula mismatch")
    AUDIT.check(sum(fibres.values()) == q ** (d * d))

    index_hist = Counter(indices.values())
    print(
        f"q={q}, d={d}: all={len(matrices)}, core={len(core)}, fixed={fixed}, "
        f"2-cycles={cycles[2]}, power-index={dict(sorted(index_hist.items()))}"
    )


def main():
    for q, d in [(2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3), (5, 1), (5, 2)]:
        run_lane(q, d)
    print(f"PASS: {AUDIT.assertions:,} exact assertions")


if __name__ == "__main__":
    main()
