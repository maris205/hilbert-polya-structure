#!/usr/bin/env python3
"""Hostile Review A exact control for P184.

This control solves the predecessor congruence separately on every valuation
class and reconstructs functional graphs directly.  It does not import or
invoke the author-side verifier.
"""

from collections import Counter, defaultdict
from math import gcd


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def vp(x, p, a):
    if x == 0:
        return a
    value = 0
    while x % p == 0:
        value += 1
        x //= p
    return value


def transition(x, p, a):
    n = p ** a
    return (x + n // gcd(x, n)) % n


def direct_predecessors(y, p, a):
    """Solve x+p^(a-v)=y mod p^a on each possible valuation v."""
    n = p ** a
    answers = set()
    for v in range(a + 1):
        candidate = (y - p ** (a - v)) % n
        if vp(candidate, p, a) == v:
            answers.add(candidate)
    return answers


def predicted_point(x, p, a):
    v = vp(x, p, a)
    if 2 * v < a:
        return 0, p ** v
    if 2 * v > a:
        return 1, p ** (a - v)
    h = a // 2
    u = x // (p ** h)
    r = p - (u % p)
    s = vp(u + r, p, h)
    return r + 1, p ** (h - s)


def orbit_signature(x, image):
    seen = {}
    orbit = []
    while x not in seen:
        seen[x] = len(orbit)
        orbit.append(x)
        x = image[x]
    mu = seen[x]
    lam = len(orbit) - seen[x]
    return mu, lam


def canonical_cycle(start, image):
    cycle = []
    x = start
    while not cycle or x != start:
        cycle.append(x)
        x = image[x]
    rotations = [tuple(cycle[q:] + cycle[:q]) for q in range(len(cycle))]
    return min(rotations)


def expected_double_set(p, a):
    result = {1}
    for w in range(1, a):
        if 2 * w >= a:
            break
        for u in range(1, p ** w):
            if u % p:
                result.add(p ** w * (1 + p ** (a - 2 * w) * u))
    return result


def expected_empty_set(p, a):
    if a % 2:
        h = a // 2
        return {y for y in range(p ** a) if vp(y, p, a) > h}
    h = a // 2
    return {p ** h * z for z in range(p ** h) if z % p == 1}


def audit_carrier(p, a):
    n = p ** a
    image = [transition(x, p, a) for x in range(n)]
    reverse = defaultdict(set)
    for x, y in enumerate(image):
        reverse[y].add(x)

    actual_mu = []
    actual_lam = []
    for x in range(n):
        mu, lam = orbit_signature(x, image)
        exp_mu, exp_lam = predicted_point(x, p, a)
        check((mu, lam) == (exp_mu, exp_lam),
              ("pointwise tail/period", p, a, x, (mu, lam),
               (exp_mu, exp_lam)))
        actual_mu.append(mu)
        actual_lam.append(lam)

        v = vp(x, p, a)
        y = image[x]
        if 2 * v < a:
            check(vp(y, p, a) == v, ("low stratum invariance", p, a, x))
        elif 2 * v > a:
            check(vp(y, p, a) == a - v,
                  ("high complementary fall", p, a, x))
        else:
            h = a // 2
            u = x // p ** h
            check(y == (p ** h * ((u + 1) % p ** h)) % n,
                  ("middle unit increment", p, a, x))

    expected_cycles = Counter()
    for v in range(a):
        if 2 * v < a:
            expected_cycles[p ** v] += (p - 1) * p ** (a - 2 * v - 1)
    cycles = set()
    for x in range(n):
        if actual_mu[x] == 0:
            cycles.add(canonical_cycle(x, image))
    actual_cycles = Counter(map(len, cycles))
    check(actual_cycles == expected_cycles,
          ("cycle census", p, a, actual_cycles, expected_cycles))

    tails = Counter(actual_mu)
    expected_tails = Counter({0: n - p ** (a // 2)})
    if a % 2:
        expected_tails[1] = p ** (a // 2)
    else:
        h = a // 2
        for depth in range(1, p + 1):
            expected_tails[depth] = p ** (h - 1)
    check(tails == expected_tails,
          ("tail census", p, a, tails, expected_tails))

    double_set = expected_double_set(p, a)
    empty_set = expected_empty_set(p, a)
    defect = p ** ((a - 1) // 2)
    check(double_set.isdisjoint(empty_set), ("D/Z disjoint", p, a))
    check(len(double_set) == defect, ("double-set size", p, a))
    check(len(empty_set) == defect, ("empty-set size", p, a))

    fibre_hist = Counter()
    for y in range(n):
        solved = direct_predecessors(y, p, a)
        brute = reverse[y]
        check(solved == brute, ("modular predecessor solve", p, a, y))
        expected_size = 0 if y in empty_set else 2 if y in double_set else 1
        check(len(solved) == expected_size,
              ("explicit fibre atlas", p, a, y, solved))
        check(len(solved) <= 2, ("maximum indegree", p, a, y))
        fibre_hist[len(solved)] += 1

    expected_hist = Counter({0: defect, 1: n - 2 * defect, 2: defect})
    check(fibre_hist == expected_hist,
          ("fibre census", p, a, fibre_hist, expected_hist))
    check(sum(size * count for size, count in fibre_hist.items()) == n,
          ("fibre mass", p, a))
    image_size = len(set(image))
    check(image_size == n - defect, ("image defect", p, a))

    return (p, a, n, tails[0], image_size,
            fibre_hist[0], fibre_hist[1], fibre_hist[2], max(tails))


def main():
    carriers = []
    carriers.extend((2, a) for a in range(1, 13))
    carriers.extend((3, a) for a in range(1, 9))
    carriers.extend((5, a) for a in range(1, 7))
    carriers.extend((7, a) for a in range(1, 6))
    carriers.extend((11, a) for a in range(1, 5))
    carriers.extend((13, a) for a in range(1, 5))

    rows = [audit_carrier(p, a) for p, a in carriers]
    print("P184_HOSTILE_REVIEW_A_EXACT_CONTROL")
    print("REPRESENTATION=valuation-class modular predecessor solver; direct functional graphs")
    print(f"CARRIERS={len(rows)}")
    for row in rows:
        p, a, n, recurrent, image, z, o, d, max_tail = row
        if (p, a) in {(2, 1), (2, 2), (2, 12), (3, 4), (5, 4),
                      (7, 4), (11, 3), (13, 4)}:
            print(f"p={p} a={a} N={n} recurrent={recurrent} image={image} "
                  f"fibres_0_1_2={z}/{o}/{d} max_tail={max_tail}")
    print(f"ASSERTIONS={ASSERTIONS}")
    print("CRITICAL_FINDINGS=0")
    print("MAJOR_FINDINGS=0")
    print("MINOR_FINDINGS=0")
    print("VERDICT=PROVABLE_AS_STATED")
    print("STATUS=HOLD_EXTERNAL")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
