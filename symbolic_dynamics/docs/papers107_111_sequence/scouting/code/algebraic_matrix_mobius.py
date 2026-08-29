#!/usr/bin/env python3
"""Exact proof spike for A -> (I-A)^(-1) over small prime fields.

The program deliberately uses literal matrix arithmetic.  The closed counts
are evaluated independently from Gaussian-binomial and general-linear-group
formulas.
"""

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


def matmul(a, b, d, q):
    return tuple(
        sum(a[i * d + k] * b[k * d + j] for k in range(d)) % q
        for i in range(d)
        for j in range(d)
    )


def matsub(a, b, q):
    return tuple((x - y) % q for x, y in zip(a, b))


def matinv(a, d, q):
    rows = [
        [a[i * d + j] % q for j in range(d)]
        + [1 if i == j else 0 for j in range(d)]
        for i in range(d)
    ]
    for col in range(d):
        pivot = next((i for i in range(col, d) if rows[i][col] % q), None)
        if pivot is None:
            return None
        rows[col], rows[pivot] = rows[pivot], rows[col]
        scale = pow(rows[col][col], -1, q)
        rows[col] = [(scale * x) % q for x in rows[col]]
        for i in range(d):
            if i == col:
                continue
            scale = rows[i][col]
            if scale:
                rows[i] = [
                    (x - scale * y) % q for x, y in zip(rows[i], rows[col])
                ]
    return tuple(rows[i][d + j] for i in range(d) for j in range(d))


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


def derangement_formula(d, q):
    return sum(
        qbinom(d, k, q)
        * (-1) ** k
        * q ** (k * (k - 1) // 2)
        * q ** (k * (d - k))
        * gl_order(d - k, q)
        for k in range(d + 1)
    )


def fixed_formula(d, q):
    if q == 3:
        return sum(
            qbinom(d, r, q)
            * qbinom(d - r, r, q)
            * gl_order(r, q)
            for r in range(d // 2 + 1)
        )
    if q % 3 == 1:
        return sum(qbinom(d, r, q) * q ** (r * (d - r)) for r in range(d + 1))
    if d % 2:
        return 0
    return gl_order(d, q) // gl_order(d // 2, q * q)


def run_lane(q, d):
    identity = eye(d)
    phase = []
    for a in product(range(q), repeat=d * d):
        if matinv(a, d, q) is not None and matinv(matsub(identity, a, q), d, q) is not None:
            phase.append(a)

    def step(a):
        b = matinv(matsub(identity, a, q), d, q)
        AUDIT.check(b is not None, "phase is not invariant")
        return b

    phase_set = set(phase)
    fixed = 0
    seen = set()
    cycles = {1: 0, 3: 0}
    for a in phase:
        b = step(a)
        c = step(b)
        e = step(c)
        AUDIT.check(b in phase_set and c in phase_set, "image left phase")
        AUDIT.check(e == a, "T^3 is not the identity")
        quadratic = matsub(matmul(a, a, d, q), a, q)
        quadratic = tuple((x + y) % q for x, y in zip(quadratic, identity))
        AUDIT.check((b == a) == (quadratic == tuple(0 for _ in quadratic)))
        fixed += b == a
        if a not in seen:
            orbit = []
            x = a
            while x not in orbit:
                orbit.append(x)
                x = step(x)
            AUDIT.check(x == a and len(orbit) in (1, 3), "bad cycle")
            cycles[len(orbit)] += 1
            seen.update(orbit)

    closed_phase = derangement_formula(d, q)
    closed_fixed = fixed_formula(d, q)
    AUDIT.check(len(phase) == closed_phase, "q-derangement count mismatch")
    AUDIT.check(fixed == closed_fixed, "fixed count mismatch")
    AUDIT.check(cycles[1] == fixed)
    AUDIT.check(cycles[3] == (len(phase) - fixed) // 3)
    AUDIT.check(sum(k * v for k, v in cycles.items()) == len(phase))
    print(
        f"q={q:>2}, d={d}: phase={len(phase):>7}, fixed={fixed:>6}, "
        f"3-cycles={cycles[3]:>7}"
    )


def main():
    lanes = [(2, 1), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (3, 3),
             (5, 1), (5, 2), (7, 1), (7, 2)]
    for q, d in lanes:
        run_lane(q, d)
    print(f"PASS: {AUDIT.assertions:,} exact assertions")


if __name__ == "__main__":
    main()
