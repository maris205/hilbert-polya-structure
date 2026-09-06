#!/usr/bin/env python3
"""Small exact diagnostics for the new census proof; writes no files.

No parameter census, old-result re-test, analytic inference, or numeric tolerance.
"""

from functools import reduce
from math import gcd


def mul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def content(a):
    return reduce(gcd, (abs(x) for row in a for x in row))


def det(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def invariants(a):
    t = a[0][0] + a[1][1]
    k = content(((a[0][0] - 1, a[0][1]),
                 (a[1][0], a[1][1] - 1)))
    h = content(((2 * a[0][0] - t, 2 * a[0][1]),
                 (2 * a[1][0], 2 * a[1][1] - t)))
    g = gcd(gcd(abs(a[0][1]), abs(a[1][0])), abs(a[1][1] - a[0][0]))
    return t, k, h, g


def smith(a):
    s1 = content(a)
    return s1, abs(det(a)) // s1


def diagnostic(a):
    assert det(a) == 1
    t, k, h, g = invariants(a)
    assert abs(t) > 2
    assert k == (gcd(h, t - 2) if t % 2 else gcd(h // 2, t // 2 - 1))
    u = [0, 1]
    for _ in range(12):
        u.append(t * u[-1] - u[-2])
    power = ((1, 0), (0, 1))
    rows = []
    for n in range(1, 13):
        power = mul(power, a)
        difference = ((power[0][0] - 1, power[0][1]),
                      (power[1][0], power[1][1] - 1))
        actual_smith = smith(difference)
        expected_s1 = (k * abs(u[n // 2 + 1] + u[n // 2]) if n % 2
                       else h * abs(u[n // 2]))
        assert actual_smith[0] == expected_s1
        row = []
        for q in range(2, 17):
            direct = sum((difference[0][0] * x + difference[0][1] * y) % q == 0
                         and (difference[1][0] * x + difference[1][1] * y) % q == 0
                         for x in range(q) for y in range(q))
            predicted = gcd(q, actual_smith[0]) * gcd(q, actual_smith[1])
            assert direct == predicted
            row.append(direct)
        rows.append(tuple(row))
    return tuple(rows)


def negate(a):
    return tuple(tuple(-x for x in row) for row in a)


def main():
    a = ((1, 4), (4, 17))
    b = ((5, 8), (8, 13))
    odd = ((2, 1), (1, 1))
    cases = (a, b, negate(a), negate(b), odd, negate(odd))
    results = [diagnostic(matrix) for matrix in cases]
    assert results[0] == results[1]
    assert results[2] == results[3]
    assert invariants(a) == (18, 4, 8, 4)
    assert invariants(b) == (18, 4, 8, 8)
    assert all(b[i][j] % 8 == (5 if i == j else 0)
               for i in range(2) for j in range(2))
    assert a[0][1] % 8 != 0 or a[1][0] % 8 != 0

    for t_half, r in ((9, 4), (-9, 4), (23, 4), (33, 8), (7, 4), (2, 1)):
        d, remainder = divmod(t_half * t_half - 1, r * r)
        assert remainder == 0
        a0 = ((t_half, r), (r * d, t_half))
        assert det(a0) == 1
        assert invariants(a0) == (2 * t_half, gcd(t_half - 1, r), 2 * r, r)
        if d % 4 == 1:
            a1 = ((t_half + r, 2 * r), (r * (d - 1) // 2, t_half - r))
            assert det(a1) == 1
            assert invariants(a1) == (2 * t_half, gcd(t_half - 1, r), 2 * r, 2 * r)

    print("PASS: 72 exact Smith-content identities on 6 fixed signed matrices.")
    print("PASS: 1080 direct finite-kernel counts (n=1..12, q=2..16).")
    print("PASS: paired positive/negative trace-18 diagnostic arrays agree.")
    print("PASS: non-conjugacy modulo 8 certified by scalar versus nonscalar.")
    print("PASS: 6 chosen admissibility/representative cases, including singleton cases.")
    print("Universal quantifiers and fibre completeness are proved in the Markdown proof,")
    print("not by these finite diagnostics; source ownership remains separate.")


if __name__ == "__main__":
    main()
