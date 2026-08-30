#!/usr/bin/env python3
"""Exact controls for synchronous b-fold merging on integer partitions."""

from collections import Counter, defaultdict
from functools import lru_cache


ASSERTIONS = 0


def check(condition, message="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


@lru_cache(maxsize=None)
def partitions(n, cap=None):
    if cap is None or cap > n:
        cap = n
    if n == 0:
        return ((),)
    out = []
    for first in range(cap, 0, -1):
        for tail in partitions(n - first, first):
            out.append((first,) + tail)
    return tuple(out)


def step(part, base):
    source = Counter(part)
    target = Counter()
    for value, multiplicity in source.items():
        target[value] += multiplicity % base
        target[base * value] += multiplicity // base
    return tuple(sorted(target.elements(), reverse=True))


def iterate(part, base, times):
    for _ in range(times):
        part = step(part, base)
    return part


def depth(part, base):
    seen = set()
    d = 0
    while True:
        check(part not in seen, "nontrivial cycle")
        seen.add(part)
        nxt = step(part, base)
        check(sum(part) == sum(nxt), "weight not preserved")
        if nxt == part:
            return d
        check(len(nxt) < len(part), "part-count Lyapunov failed")
        part = nxt
        d += 1


def in_image_t(part, base, times):
    modulus = base ** times
    counts = Counter(part)
    return all(value % modulus == 0 or multiplicity < base
               for value, multiplicity in counts.items())


def fibre_formula(part, base):
    counts = Counter(part)
    if any(value % base != 0 and multiplicity >= base
           for value, multiplicity in counts.items()):
        return 0
    answer = 1
    for value, multiplicity in counts.items():
        if value % base == 0:
            answer *= min(base, multiplicity + 1)
    return answer


def sharp_witness(n, base):
    power = 1
    exponent = 0
    while power * base <= n:
        power *= base
        exponent += 1
    if exponent == 0:
        return (n,), 0
    slack = n - power
    parts = [1] * (base + slack)
    for level in range(1, exponent):
        parts.extend([base ** level] * (base - 1))
    return tuple(sorted(parts, reverse=True)), exponent


def restricted_product_coefficients(limit, base, times):
    coeff = [0] * (limit + 1)
    coeff[0] = 1
    modulus = base ** times
    for value in range(1, limit + 1):
        bound = limit // value if value % modulus == 0 else base - 1
        new = [0] * (limit + 1)
        for total, count in enumerate(coeff):
            if not count:
                continue
            for multiplicity in range(min(bound, (limit - total) // value) + 1):
                new[total + multiplicity * value] += count
        coeff = new
    return coeff


def regular_part_coefficients(limit, base):
    coeff = [0] * (limit + 1)
    coeff[0] = 1
    for value in range(1, limit + 1):
        if value % base == 0:
            continue
        for total in range(value, limit + 1):
            coeff[total] += coeff[total - value]
    return coeff


def direct_lane():
    image_sentinels = {}
    max_depth_sentinels = {}
    for base in range(2, 7):
        for n in range(0, 31):
            states = partitions(n)
            fibres = defaultdict(int)
            depth_hist = Counter()
            for part in states:
                target = step(part, base)
                check(target in states, "partition closure")
                check(sum(target) == n, "weight changed")
                check((target == part) == all(v < base for v in Counter(part).values()),
                      "fixed criterion")
                check((target == part) or len(target) < len(part),
                      "strict part-count descent")
                fibres[target] += 1
                d = depth(part, base)
                depth_hist[d] += 1
                check(d <= (0 if n == 0 else floor_log(n, base)),
                      "clock upper bound")
            check(sum(fibres.values()) == len(states), "fibre mass")
            image_count = len(fibres)
            for target in states:
                check(fibres[target] == fibre_formula(target, base),
                      f"fibre formula base={base} n={n} target={target}")
            witness, exponent = sharp_witness(n, base) if n else ((), 0)
            check(sum(witness) == n, "witness weight")
            check(witness in states, "witness is not a partition")
            check(depth(witness, base) == exponent, "sharp witness failed")
            check(max(depth_hist, default=0) == exponent, "maximum depth failed")
            image_sentinels[(base, n)] = image_count
            max_depth_sentinels[(base, n)] = exponent
    return image_sentinels, max_depth_sentinels


def floor_log(n, base):
    exponent = 0
    while n >= base:
        n //= base
        exponent += 1
    return exponent


def iterate_image_lane(image_sentinels):
    for base in range(2, 7):
        for n in range(0, 27):
            states = partitions(n)
            for times in range(1, 6):
                literal = {iterate(part, base, times) for part in states}
                predicted = {part for part in states if in_image_t(part, base, times)}
                check(literal == predicted,
                      f"iterated image base={base} n={n} t={times}")
                for part in states:
                    check((part in literal) == in_image_t(part, base, times),
                          "pointwise iterated image mismatch")
                if times == 1:
                    check(len(literal) == image_sentinels[(base, n)],
                          "one-step image sentinel mismatch")


def generating_function_lane(image_sentinels):
    limit = 120
    for base in range(2, 7):
        regular = regular_part_coefficients(limit, base)
        stabilized = restricted_product_coefficients(limit, base, limit)
        for n in range(limit + 1):
            check(regular[n] == stabilized[n], "Glaisher control mismatch")
        for times in range(1, 7):
            coeff = restricted_product_coefficients(limit, base, times)
            for n in range(0, 31):
                literal = sum(in_image_t(part, base, times) for part in partitions(n))
                check(coeff[n] == literal, "image product mismatch")
                if times == 1:
                    check(coeff[n] == image_sentinels[(base, n)],
                          "one-step product mismatch")


def boundary_and_formula_lane():
    for base in range(2, 11):
        for n in range(0, 37):
            for part in partitions(n):
                orbit = [part]
                for _ in range(max(4, floor_log(max(1, n), base) + 1)):
                    orbit.append(step(orbit[-1], base))
                fixed = orbit[-1]
                check(step(fixed, base) == fixed, "normal form did not settle")
                check(all(v < base for v in Counter(fixed).values()),
                      "normal multiplicities")
                check(sum(fixed) == n, "normal weight")
                for times in range(1, 5):
                    image = orbit[times]
                    modulus = base ** times
                    for value, multiplicity in Counter(image).items():
                        if value % modulus:
                            check(multiplicity < base,
                                  "low tower level did not stabilize")


def main():
    images, depths = direct_lane()
    iterate_image_lane(images)
    generating_function_lane(images)
    boundary_and_formula_lane()
    print("parallel Glaisher compression verifier: PASS")
    print(f"exact assertions: {ASSERTIONS:,}")
    print("bases: 2..10; exhaustive boundary partitions: n<=36")
    print("literal fibres/depths: bases 2..6, n<=30")
    print("iterated images: bases 2..6, n<=26, t<=5")
    print("image products: bases 2..6, coefficients n<=120, t<=6")
    print("base-2 image n=0..15:", [images[(2, n)] for n in range(16)])
    print("base-3 image n=0..15:", [images[(3, n)] for n in range(16)])
    print("base-2 max depth n=0..30:", [depths[(2, n)] for n in range(31)])
    print("scope sentinel: Glaisher terminal bijection is classical and zero-credit")
    print("scope sentinel: all-size image/fibre/clock claims are proved symbolically, not by this run")


if __name__ == "__main__":
    main()
