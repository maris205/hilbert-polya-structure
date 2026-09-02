#!/usr/bin/env python3
"""Exact counterexample pressure for divisor-imbalance dynamics.

The program intentionally imports no project code.  Enumeration is evidence
against mistakes in the stated deductions, never a replacement for proof.
"""

from collections import Counter
from itertools import product
from math import gcd, isqrt, prod


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def v2(n):
    check(n > 0, "v2 positive input")
    return (n & -n).bit_length() - 1


def fold(modulus, residue):
    residue %= modulus
    return min(residue, modulus - residue)


def local_step(e, a):
    return abs(2 * a - e)


def local_iterate(e, a, time):
    for _ in range(time):
        a = local_step(e, a)
    return a


def local_closed(e, a, time):
    return e - fold(2 * e, (1 << time) * (e - a))


def local_depth(e, a):
    seen = {}
    time = 0
    while a not in seen:
        seen[a] = time
        time += 1
        a = local_step(e, a)
    return seen[a]


def local_depth_formula(e, a):
    x = e - a
    if x == 0:
        return 0
    return max(0, v2(2 * e) - v2(x))


def local_hist_formula(e):
    level = v2(2 * e)
    odd = e >> v2(e)
    answer = Counter({0: (odd + 1) // 2, 1: (odd + 1) // 2})
    for depth in range(2, level + 1):
        answer[depth] = (1 << (depth - 2)) * odd
    return answer


def local_fix_formula(e, time):
    odd = e >> v2(e)
    return (gcd((1 << time) - 1, odd) + gcd((1 << time) + 1, odd)) // 2


def local_image_size_formula(e, time):
    level = v2(2 * e)
    odd = e >> v2(e)
    if time < level:
        return e // (1 << time) + 1
    return (odd + 1) // 2


def local_fibre_formula(e, target, time):
    if time == 0:
        return 1
    level = v2(2 * e)
    kernel = 1 << min(time, level)
    y = e - target
    if y % kernel:
        return 0
    if y == 0:
        return kernel // 2 + 1
    if y == e:
        return kernel // 2
    return kernel


def vector_step(exponents, state):
    return tuple(local_step(e, a) for e, a in zip(exponents, state))


def vector_iterate(exponents, state, time):
    for _ in range(time):
        state = vector_step(exponents, state)
    return state


def vector_depth_formula(exponents, state):
    return max((local_depth_formula(e, a) for e, a in zip(exponents, state)), default=0)


def factor(n):
    result = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            result.append((p, e))
        p += 1 if p == 2 else 2
    if n > 1:
        result.append((n, 1))
    return result


def divisors(n):
    values = [1]
    for p, e in factor(n):
        values = [d * p ** a for d in values for a in range(e + 1)]
    return sorted(values)


def literal_step(n, d):
    other = n // d
    common = gcd(d, other)
    return (d * other // common) // common


def exponent_state(prime_exponents, d):
    answer = []
    for p, _ in prime_exponents:
        a = 0
        while d % p == 0:
            d //= p
            a += 1
        answer.append(a)
    check(d == 1, "exponent extraction")
    return tuple(answer)


def run_local():
    for e in range(1, 193):
        carrier = range(e + 1)
        observed_hist = Counter()
        for a in carrier:
            depth = local_depth(e, a)
            observed_hist[depth] += 1
            check(depth == local_depth_formula(e, a), f"local depth e={e} a={a}")
            for time in range(18):
                direct = local_iterate(e, a, time)
                closed = local_closed(e, a, time)
                check(direct == closed, f"closed iterate e={e} a={a} t={time}")
                check(0 <= direct <= e, f"closed carrier e={e} a={a} t={time}")
        check(observed_hist == local_hist_formula(e), f"depth histogram e={e}")
        check(sum(observed_hist.values()) == e + 1, f"depth mass e={e}")
        check(max(observed_hist) == v2(2 * e), f"sharp local height e={e}")
        for time in range(1, 18):
            images = Counter(local_iterate(e, a, time) for a in carrier)
            check(len(images) == local_image_size_formula(e, time),
                  f"local image e={e} t={time}")
            check(sum(value == key for key, value in
                      ((a, local_iterate(e, a, time)) for a in carrier)) ==
                  local_fix_formula(e, time), f"local fixed e={e} t={time}")
            for target in carrier:
                check(images[target] == local_fibre_formula(e, target, time),
                      f"local fibre e={e} t={time} b={target}")
            check(sum(local_fibre_formula(e, target, time) for target in carrier) == e + 1,
                  f"local fibre mass e={e} t={time}")


def run_products():
    boxes = [
        (1,), (2,), (3,), (4,), (6,), (8,), (12,),
        (1, 2), (2, 3), (3, 4), (4, 6), (2, 5, 8), (3, 6, 9),
    ]
    for exponents in boxes:
        carrier = list(product(*(range(e + 1) for e in exponents)))
        histories = Counter(vector_depth_formula(exponents, state) for state in carrier)
        check(sum(histories.values()) == prod(e + 1 for e in exponents),
              f"product depth mass E={exponents}")
        check(max(histories) == max(v2(2 * e) for e in exponents),
              f"product sharp height E={exponents}")
        for state in carrier:
            seen = {}
            point = state
            time = 0
            while point not in seen:
                seen[point] = time
                time += 1
                point = vector_step(exponents, point)
            check(seen[point] == vector_depth_formula(exponents, state),
                  f"product point depth E={exponents} x={state}")
        for time in range(10):
            images = Counter(vector_iterate(exponents, state, time) for state in carrier)
            expected_image = prod(local_image_size_formula(e, time) for e in exponents)
            check(len(images) == expected_image, f"product image E={exponents} t={time}")
            expected_fix = (prod(e + 1 for e in exponents) if time == 0 else
                            prod(local_fix_formula(e, time) for e in exponents))
            observed_fix = sum(vector_iterate(exponents, state, time) == state
                               for state in carrier)
            check(observed_fix == expected_fix, f"product fixed E={exponents} t={time}")
            for target in carrier:
                expected_fibre = prod(local_fibre_formula(e, b, time)
                                      for e, b in zip(exponents, target))
                check(images[target] == expected_fibre,
                      f"product fibre E={exponents} t={time} b={target}")
            check(sum(images.values()) == len(carrier), f"product mass E={exponents} t={time}")


def run_literal():
    integers = [2, 4, 8, 12, 16, 18, 24, 36, 72, 96, 108, 144,
                216, 360, 720, 840, 1260, 2160, 5040, 7560]
    for n in integers:
        pe = factor(n)
        exponents = tuple(e for _, e in pe)
        ds = divisors(n)
        check(len(ds) == prod(e + 1 for e in exponents), f"divisor count n={n}")
        for d in ds:
            state = exponent_state(pe, d)
            target = literal_step(n, d)
            target_state = exponent_state(pe, target)
            check(target_state == vector_step(exponents, state), f"literal n={n} d={d}")
            check(n % target == 0, f"literal divisor closure n={n} d={d}")
            common = gcd(d, n // d)
            check(target == n // (common * common), f"literal reduced product n={n} d={d}")


def main():
    run_local()
    run_products()
    run_literal()
    print("divisor imbalance verifier: PASS")
    print("local exponent boxes: e=1..192; times=0..17")
    print("product exponent boxes: 13; times=0..9")
    print("literal integer boxes: 20")
    print(f"assertions: {ASSERTIONS}")
    print("status: GREEN_PENDING_INDEPENDENT_HOSTILE_GATE")
    print("scope: exact enumeration is counterexample pressure, not proof")
    print("external: HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
