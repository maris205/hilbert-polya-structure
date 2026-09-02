#!/usr/bin/env python3
"""Independent threshold checks for AA01/USP.

This verifier does not import either scout implementation.  It checks the
stratumwise formulas, the pooled empty/failure fibres, identifiability, two
nonisomorphic order-four local rings, and ring-agnostic boundary controls.
"""

from collections import Counter
from itertools import product
from math import isqrt


ASSERTIONS = 0
FAIL = "FAIL"


def check(condition, label):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(f"{label} [assertion {ASSERTIONS}]")


class Ring:
    def __init__(self, name, elements, zero, one, add, mul):
        self.name = name
        self.elements = tuple(elements)
        self.zero = zero
        self.one = one
        self.add = add
        self.mul = mul
        self.neg = {a: next(b for b in self.elements if add(a, b) == zero)
                    for a in self.elements}
        self.inverse = {}
        for a in self.elements:
            for b in self.elements:
                if mul(a, b) == one and mul(b, a) == one:
                    self.inverse[a] = b
                    break
        self.units = frozenset(self.inverse)

    def sub(self, a, b):
        return self.add(a, self.neg[b])


def zmod(m):
    return Ring(f"Z{m}", range(m), 0, 1,
                lambda a, b: (a + b) % m,
                lambda a, b: (a * b) % m)


def dual_f2():
    def mul(x, y):
        a, b = x & 1, (x >> 1) & 1
        c, d = y & 1, (y >> 1) & 1
        return (a * c) | (((a * d + b * c) & 1) << 1)
    return Ring("F2eps", range(4), 0, 1, lambda a, b: a ^ b, mul)


def matrix2_f2():
    def mul(x, y):
        a, b, c, d = ((x >> i) & 1 for i in range(4))
        e, f, g, h = ((y >> i) & 1 for i in range(4))
        vals = (a * e + b * g, a * f + b * h,
                c * e + d * g, c * f + d * h)
        return sum((v & 1) << i for i, v in enumerate(vals))
    return Ring("M2F2", range(16), 0, 9, lambda a, b: a ^ b, mul)


def matrices(ring, n):
    if n == 0:
        yield ()
        return
    for entries in product(ring.elements, repeat=n * n):
        yield tuple(tuple(entries[i * n:(i + 1) * n]) for i in range(n))


def schur(matrix, ring):
    if matrix == FAIL or matrix == ():
        return matrix
    a = matrix[0][0]
    if a not in ring.units:
        return FAIL
    if len(matrix) == 1:
        return ()
    ai = ring.inverse[a]
    return tuple(tuple(ring.sub(
        matrix[i][j], ring.mul(ring.mul(matrix[i][0], ai), matrix[0][j]))
        for j in range(1, len(matrix))) for i in range(1, len(matrix)))


def iterate(x, t, ring):
    for _ in range(t):
        x = schur(x, ring)
    return x


def audit_strata(ring, max_n):
    Q, U = len(ring.elements), len(ring.units)
    carriers = {n: tuple(matrices(ring, n)) for n in range(max_n + 1)}
    for n, carrier in carriers.items():
        for A in carrier:
            y = schur(A, ring)
            check(y == FAIL or isinstance(y, tuple), f"{ring.name} closure n={n}")
        for t in range(n + 1):
            survived = sum(iterate(A, t, ring) != FAIL for A in carrier)
            check(survived == U ** t * Q ** (n * n - t),
                  f"{ring.name} survival n={n} t={t}")
        if n:
            shells = []
            for t in range(n):
                count = sum(iterate(A, t, ring) != FAIL and
                            iterate(A, t + 1, ring) == FAIL for A in carrier)
                expected = U ** t * (Q - U) * Q ** (n * n - t - 1)
                check(count == expected, f"{ring.name} first-fail n={n} t={t+1}")
                shells.append(count)
            success = U ** n * Q ** (n * n - n)
            check(sum(shells) + success == Q ** (n * n),
                  f"{ring.name} shell mass n={n}")
    for k in range(max_n + 1):
        for t in range(max_n - k + 1):
            fibres = Counter(iterate(A, t, ring) for A in carriers[k + t])
            expected = U ** t * Q ** (2 * k * t + t * (t - 1))
            for B in carriers[k]:
                check(fibres[B] == expected,
                      f"{ring.name} target k={k} t={t}")
    return carriers


def audit_pooled(ring, carriers, cap):
    Q, U = len(ring.elements), len(ring.units)
    for t in range(cap + 2):
        empty_actual = 1  # the empty matrix itself
        fail_actual = 1   # the fixed failure sink itself
        for n in range(1, cap + 1):
            outputs = Counter(iterate(A, t, ring) for A in carriers[n])
            empty_actual += outputs[()]
            fail_actual += outputs[FAIL]
        empty_expected = 1 + sum(
            U ** j * Q ** (j * j - j) for j in range(1, min(t, cap) + 1))
        fail_expected = 1 + sum(
            Q ** (n * n) - U ** min(t, n) * Q ** (n * n - min(t, n))
            for n in range(1, cap + 1))
        check(empty_actual == empty_expected, f"{ring.name} pooled empty t={t}")
        check(fail_actual == fail_expected, f"{ring.name} pooled fail t={t}")


def audit_identifiability(ring):
    Q, U = len(ring.elements), len(ring.units)
    F0 = U
    F1 = U * Q * Q
    ratio = F1 // F0
    recovered_q = isqrt(ratio)
    check(F1 % F0 == 0 and recovered_q ** 2 == ratio,
          f"{ring.name} square-ratio")
    check((recovered_q, F0) == (Q, U), f"{ring.name} recover Q,U")
    return F0, F1


def characteristic(ring):
    x = ring.zero
    for n in range(1, 100):
        x = ring.add(x, ring.one)
        if x == ring.zero:
            return n
    raise AssertionError("characteristic search failed")


def main():
    z4, dual, z6, matrix = zmod(4), dual_f2(), zmod(6), matrix2_f2()
    rows = []
    for ring, max_n in ((z4, 3), (dual, 3), (z6, 2), (matrix, 2)):
        carriers = audit_strata(ring, max_n)
        if ring in (z4, dual):
            audit_pooled(ring, carriers, 3)
        F0, F1 = audit_identifiability(ring)
        rows.append((ring.name, len(ring.elements), len(ring.units), max_n, F0, F1))
    check(characteristic(z4) == 4 and characteristic(dual) == 2,
          "order-four rings are nonisomorphic")
    check(rows[0][1:3] == rows[1][1:3] == (4, 2),
          "nonisomorphic rings share Q,U")
    check(matrix.mul(1, 2) != matrix.mul(2, 1), "noncommutative boundary")
    print("AA01_USP_SPECIALIST_GATE")
    print(f"RINGS {rows}")
    print("POOLED cap=3 empty/failure formulas PASS on Z4 and F2eps")
    print("BOUNDARY Z6(nonlocal) and M2F2(noncommutative) PASS")
    print("NONISOMORPHIC char(Z4)=4 char(F2eps)=2 same(Q,U)=(4,2)")
    print(f"ASSERTIONS {ASSERTIONS}")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
