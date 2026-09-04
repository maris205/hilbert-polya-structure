#!/usr/bin/env python3
"""Exact small-box regression checks for P187.

The finite checks are counterexample pressure only.  Uniform claims are
proved in the manuscript.
"""

from collections import Counter
from itertools import product
from math import gcd


ASSERTIONS = 0


def check(condition, label):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def matmul(a, b):
    n = len(a)
    return [
        [sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)]
        for i in range(n)
    ]


def trace_product(mats):
    n = len(mats[0])
    out = [[int(i == j) for j in range(n)] for i in range(n)]
    for mat in mats:
        out = matmul(out, mat)
    return sum(out[i][i] for i in range(n))


def difference(word):
    m = len(word)
    return tuple(max(word[i] - word[(i + 1) % m], 0) for i in range(m))


def tail_to_fixed(update, state):
    t = 0
    while True:
        nxt = update(state)
        if nxt == state:
            return t
        state = nxt
        t += 1
        check(t < 100, "orbit guard")


def local_matrix(a, b):
    return [
        [int(max(u - v, 0) == b) for v in range(a + 1)]
        for u in range(a + 1)
    ]


def exponent_boxes():
    signatures = []
    for a in range(1, 5):
        for m in range(1, 7):
            states = list(product(range(a + 1), repeat=m))
            fibres = Counter(difference(x) for x in states)
            maximum = 0
            fixed = 0
            for x in states:
                y = difference(x)
                t = tail_to_fixed(difference, x)
                maximum = max(maximum, t)
                check(difference(y) == y if m <= 2 else t <= a,
                      "height clock")
                support_condition = all(
                    x[i] == 0 or x[(i + 1) % m] == 0
                    for i in range(m)
                )
                check((difference(x) == x) == support_condition,
                      "fixed support")
                fixed += int(difference(x) == x)
            expected_height = 1 if m <= 2 else a
            check(maximum == expected_height, "sharp exponent height")
            transfer_mass = 0
            for target in states:
                predicted = trace_product(
                    [local_matrix(a, b) for b in target]
                )
                check(predicted == fibres[target], "every-target transfer")
                transfer_mass += predicted
            check(transfer_mass == (a + 1) ** m, "exponent mass")
            support_count = sum(
                a ** sum(bits)
                for bits in product((0, 1), repeat=m)
                if all(not (bits[i] and bits[(i + 1) % m])
                       for i in range(m))
            )
            check(fixed == support_count, "weighted cyclic support")
            signatures.append((a, m, len(states), maximum, fixed))
    return signatures


def factor(n):
    ans = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            a = 0
            while n % p == 0:
                n //= p
                a += 1
            ans.append((p, a))
        p += 1
    if n > 1:
        ans.append((n, 1))
    return ans


def divisors(n):
    out = [1]
    for p, a in factor(n):
        out = [d * p ** e for d in out for e in range(a + 1)]
    return tuple(sorted(out))


def valuation(x, p):
    e = 0
    while x % p == 0:
        x //= p
        e += 1
    return e


def divisor_update(word):
    m = len(word)
    return tuple(word[i] // gcd(word[i], word[(i + 1) % m])
                 for i in range(m))


def divisor_boxes():
    signatures = []
    for n in (1, 2, 4, 6, 12, 18, 36, 60):
        ds = divisors(n)
        fac = factor(n)
        for m in range(1, 5):
            states = list(product(ds, repeat=m))
            fibres = Counter(divisor_update(x) for x in states)
            fixed = 0
            maximum = 0
            for x in states:
                y = divisor_update(x)
                for p, _a in fac:
                    ex = tuple(valuation(v, p) for v in x)
                    ey = tuple(valuation(v, p) for v in y)
                    check(ey == difference(ex), "primewise conjugacy")
                t = tail_to_fixed(divisor_update, x)
                maximum = max(maximum, t)
                fixed += int(t == 0)
            if n == 1:
                expected_height = 0
            elif m <= 2:
                expected_height = 1
            else:
                expected_height = max(a for _, a in fac)
            check(maximum == expected_height, "composite sharp height")
            predicted_fixed = 1
            for _p, a in fac:
                predicted_fixed *= sum(
                    a ** sum(bits)
                    for bits in product((0, 1), repeat=m)
                    if all(not (bits[i] and bits[(i + 1) % m])
                           for i in range(m))
                )
            check(fixed == predicted_fixed, "composite fixed census")
            total = 0
            for target in states:
                predicted = 1
                for p, a in fac:
                    b = tuple(valuation(v, p) for v in target)
                    predicted *= trace_product(
                        [local_matrix(a, bi) for bi in b]
                    )
                check(predicted == fibres[target], "divisor target fibre")
                total += predicted
            check(total == len(states), "divisor fibre mass")
            signatures.append((n, m, len(states), maximum, fixed,
                               len(fibres)))
    return signatures


def main():
    exponent = exponent_boxes()
    composite = divisor_boxes()
    print("P187 exact author control")
    print("status=PASS")
    print(f"exponent_boxes={len(exponent)} last={exponent[-1]}")
    print(f"divisor_boxes={len(composite)} last={composite[-1]}")
    print(f"assertions={ASSERTIONS}")
    print("finite_checks_are_not_proof_or_novelty=true")


if __name__ == "__main__":
    main()
