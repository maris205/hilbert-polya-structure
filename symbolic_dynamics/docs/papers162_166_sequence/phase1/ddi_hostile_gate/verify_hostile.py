#!/usr/bin/env python3
"""Independent hostile verifier for divisor-imbalance dynamics (DDI).

No author module or transcript is imported.  Literal integer arithmetic,
finite-map cycle detection, quotient-residue lifting, and formula evaluation
are implemented here from scratch.
"""

from collections import Counter
from itertools import product
from math import gcd, lcm, prod


ASSERTIONS = 0


def demand(ok, tag):
    global ASSERTIONS
    ASSERTIONS += 1
    if not ok:
        raise AssertionError(tag)


def nu2_positive(x):
    demand(x > 0, ("nu2-domain", x))
    return (x & -x).bit_length() - 1


def step(e, a):
    return abs(2 * a - e)


def iterate(e, a, t):
    for _ in range(t):
        a = step(e, a)
    return a


def fold_residue(e, residue):
    residue %= 2 * e
    return min(residue, 2 * e - residue)


def predicted_iterate(e, a, t):
    return e - fold_residue(e, (1 << t) * (e - a))


def orbit_tail_period(e, a):
    first = {}
    path = []
    while a not in first:
        first[a] = len(path)
        path.append(a)
        a = step(e, a)
    return first[a], len(path) - first[a]


def L(e):
    return nu2_positive(2 * e)


def odd_part(e):
    return e >> nu2_positive(e)


def predicted_tail(e, a):
    x = e - a
    return 0 if x == 0 else max(0, L(e) - nu2_positive(x))


def predicted_hist(e):
    ell, m = L(e), odd_part(e)
    h = Counter({0: (m + 1) // 2, 1: (m + 1) // 2})
    for r in range(2, ell + 1):
        h[r] = (1 << (r - 2)) * m
    return h


def fixed_formula(e, k):
    m = odd_part(e)
    return (gcd((1 << k) - 1, m) + gcd((1 << k) + 1, m)) // 2


def mobius(n):
    answer = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            answer = -answer
            if n % p == 0:
                return 0
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        answer = -answer
    return answer


def divisors(k):
    return [d for d in range(1, k + 1) if k % d == 0]


def cycles_formula(exponents, ell):
    exact_points = sum(
        mobius(ell // k) * prod(fixed_formula(e, k) for e in exponents)
        for k in divisors(ell)
    )
    demand(exact_points % ell == 0, ("cycle-integrality", exponents, ell))
    return exact_points // ell


def image_size_formula(e, t):
    if t < L(e):
        return e // (1 << t) + 1
    return (odd_part(e) + 1) // 2


def fibre_formula(e, b, t):
    if t == 0:
        return 1
    g = 1 << min(t, L(e))
    y = e - b
    if y % g:
        return 0
    if y == 0:
        return g // 2 + 1
    if y == e:
        return g // 2
    return g


def lifted_fibre_profile(e, t):
    """Count quotient sources using representatives x=0,...,e."""
    return Counter(e - fold_residue(e, (1 << t) * x) for x in range(e + 1))


def vector_step(exponents, state):
    return tuple(step(e, a) for e, a in zip(exponents, state))


def vector_iterate(exponents, state, t):
    for _ in range(t):
        state = vector_step(exponents, state)
    return state


def vector_orbit(exponents, state):
    first = {}
    path = []
    while state not in first:
        first[state] = len(path)
        path.append(state)
        state = vector_step(exponents, state)
    return first[state], len(path) - first[state]


def direct_cycle_inventory(exponents):
    carrier = list(product(*(range(e + 1) for e in exponents)))
    recurrent = {x for x in carrier if vector_orbit(exponents, x)[0] == 0}
    cycles = Counter()
    unseen = set(recurrent)
    while unseen:
        start = min(unseen)
        orbit = []
        point = start
        while point not in orbit:
            orbit.append(point)
            point = vector_step(exponents, point)
        demand(point == start, ("recurrent-cycle-start", exponents, start))
        cycles[len(orbit)] += 1
        unseen.difference_update(orbit)
    return recurrent, cycles


def prime_factorization(n):
    answer = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            answer.append((p, e))
        p += 1
    if n > 1:
        answer.append((n, 1))
    return answer


def all_divisors(factors):
    return sorted(prod(p ** a for p, a in zip((p for p, _ in factors), exps))
                  for exps in product(*(range(e + 1) for _, e in factors)))


def exponent_tuple(factors, d):
    ans = []
    for p, _ in factors:
        a = 0
        while d % p == 0:
            d //= p
            a += 1
        ans.append(a)
    demand(d == 1, ("exponent-factor", d))
    return tuple(ans)


def literal_phi(n, d):
    partner = n // d
    return lcm(d, partner) // gcd(d, partner)


def local_suite():
    for e in range(1, 257):
        carrier = tuple(range(e + 1))
        hist = Counter()
        for a in carrier:
            tail, period = orbit_tail_period(e, a)
            hist[tail] += 1
            demand(tail == predicted_tail(e, a), ("tail", e, a, tail))
            demand(period >= 1, ("period", e, a))
            for t in range(20):
                demand(iterate(e, a, t) == predicted_iterate(e, a, t),
                       ("iterate", e, a, t))
        demand(hist == predicted_hist(e), ("hist", e, hist, predicted_hist(e)))
        demand(sum(hist.values()) == e + 1, ("hist-mass", e))
        demand(max(hist) == L(e), ("sharp-local", e))

        for t in range(20):
            counts = Counter(iterate(e, a, t) for a in carrier)
            lifted = lifted_fibre_profile(e, t)
            demand(len(counts) == image_size_formula(e, t), ("image", e, t))
            for b in carrier:
                expected = fibre_formula(e, b, t)
                demand(counts[b] == expected, ("fibre", e, b, t, counts[b], expected))
                demand(lifted[b] == expected,
                       ("lifted-fibre", e, b, t))
            demand(sum(counts.values()) == e + 1, ("fibre-mass", e, t))
            if t:
                observed_fix = sum(iterate(e, a, t) == a for a in carrier)
                demand(observed_fix == fixed_formula(e, t),
                       ("fixed", e, t, observed_fix, fixed_formula(e, t)))


def product_suite():
    boxes = ((1,), (2,), (3,), (4,), (5,), (6,), (8,), (10,), (12,),
             (1, 2), (2, 3), (3, 4), (2, 5), (4, 6), (1, 3, 5),
             (2, 4, 6), (2, 5, 8), (3, 6, 9))
    for exponents in boxes:
        carrier = list(product(*(range(e + 1) for e in exponents)))
        recurrent, direct_cycles = direct_cycle_inventory(exponents)
        demand(len(recurrent) == prod((odd_part(e) + 1) // 2 for e in exponents),
               ("recurrent-size", exponents))
        demand(sum(length * number for length, number in direct_cycles.items()) == len(recurrent),
               ("cycle-mass", exponents))
        for ell in range(1, 21):
            demand(direct_cycles[ell] == cycles_formula(exponents, ell),
                   ("cycles", exponents, ell, direct_cycles[ell], cycles_formula(exponents, ell)))

        depths = Counter()
        for state in carrier:
            tail, _ = vector_orbit(exponents, state)
            expected = max(predicted_tail(e, a) for e, a in zip(exponents, state))
            demand(tail == expected, ("product-tail", exponents, state))
            depths[tail] += 1
        for r in range(max(L(e) for e in exponents) + 1):
            cdf = prod(sum(v for level, v in predicted_hist(e).items() if level <= r)
                       for e in exponents)
            previous = (prod(sum(v for level, v in predicted_hist(e).items() if level <= r - 1)
                             for e in exponents) if r else 0)
            demand(depths[r] == cdf - previous, ("product-hist", exponents, r))

        for t in range(12):
            image = Counter(vector_iterate(exponents, state, t) for state in carrier)
            demand(len(image) == prod(image_size_formula(e, t) for e in exponents),
                   ("product-image", exponents, t))
            for target in carrier:
                expected = prod(fibre_formula(e, b, t) for e, b in zip(exponents, target))
                demand(image[target] == expected, ("product-fibre", exponents, t, target))
            if t:
                direct_fix = sum(vector_iterate(exponents, state, t) == state for state in carrier)
                expected_fix = prod(fixed_formula(e, t) for e in exponents)
                demand(direct_fix == expected_fix, ("product-fix", exponents, t))


def literal_suite():
    integers = (2, 4, 8, 12, 16, 18, 24, 36, 72, 96, 108, 144, 216,
                360, 720, 840, 1260, 2160, 5040, 7560, 83160)
    for n in integers:
        factors = prime_factorization(n)
        exponents = tuple(e for _, e in factors)
        ds = all_divisors(factors)
        demand(len(ds) == prod(e + 1 for e in exponents), ("divisor-mass", n))
        for d in ds:
            state = exponent_tuple(factors, d)
            target = literal_phi(n, d)
            demand(n % target == 0, ("closure", n, d, target))
            demand(exponent_tuple(factors, target) == vector_step(exponents, state),
                   ("literal-coordinate", n, d))
            common = gcd(d, n // d)
            demand(target == n // (common * common), ("literal-identity", n, d))


def main():
    local_suite()
    product_suite()
    literal_suite()
    print("DDI_INDEPENDENT_HOSTILE_GATE_V1")
    print("IMPLEMENTATION=DIRECT_INTEGER_MAP_AND_RESIDUE_QUOTIENT_NO_AUTHOR_IMPORT")
    print("LOCAL_EXPONENTS=1..256 TIMES=0..19")
    print("PRODUCT_BOXES=18 TIMES=0..11 CYCLE_LENGTHS=1..20")
    print("LITERAL_INTEGERS=21")
    print(f"ASSERTIONS={ASSERTIONS}")
    print("MATH_STATUS=PASS")
    print("EXTERNAL=HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
