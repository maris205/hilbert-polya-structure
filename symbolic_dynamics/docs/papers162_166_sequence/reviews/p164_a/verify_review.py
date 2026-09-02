#!/usr/bin/env python3
"""Independent hostile verifier for P164.

This file was derived from the theorem statements and literal map.  It does
not import or call the author verifier and uses only the Python standard
library, exact integers, and exhaustive finite enumeration.
"""

from collections import Counter, defaultdict
from functools import lru_cache
from itertools import product
from math import comb


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def popcount(mask):
    return mask.bit_count()


def tuple_to_mask(bits):
    return sum((bit & 1) << i for i, bit in enumerate(bits))


def mask_to_tuple(mask, n):
    return tuple((mask >> i) & 1 for i in range(n))


def all_one_mask(n):
    return (1 << n) - 1


def d_map(mask, n):
    """(Dc)_i=c_i+c_(i+1), with indices modulo n."""
    out = 0
    for i in range(n):
        bit = ((mask >> i) ^ (mask >> ((i + 1) % n))) & 1
        out |= bit << i
    return out


@lru_cache(maxsize=None)
def d_power(mask, n, exponent):
    out = mask
    for _ in range(exponent):
        out = d_map(out, n)
    return out


def literal_t(word):
    n = len(word)
    return tuple(int(word[i] == word[(i + 1) % n]) for i in range(n))


def change_mask(word):
    n = len(word)
    return tuple(int(word[i] != word[(i + 1) % n]) for i in range(n))


def chi(q, weight):
    x = q - 1
    return x ** weight + ((-1) ** weight) * x


def expected_depth(word):
    n = len(word)
    ones = tuple(1 for _ in range(n))
    if word == ones:
        return 0
    c = tuple_to_mask(change_mask(word))
    if c == 0:
        return 1
    for j in range(n + 1):
        if d_power(c, n, j) == 0:
            return j + 1
    raise AssertionError("dyadic nilpotence failed")


def literal_depth(word):
    n = len(word)
    ones = tuple(1 for _ in range(n))
    state = word
    for depth in range(n + 2):
        if state == ones:
            return depth
        state = literal_t(state)
    raise AssertionError("literal orbit exceeded claimed cap")


def weighted_pushforward(n, q, exponent):
    fibres = Counter()
    for mask in range(1 << n):
        fibres[d_power(mask, n, exponent)] += chi(q, popcount(mask))
    return fibres


def kernel_mass(n, q, exponent):
    return weighted_pushforward(n, q, exponent)[0]


def dyadic_divisors_below(n):
    j = 1
    ans = []
    while j < n:
        ans.append(j)
        j *= 2
    return ans


def prove_linear_boundaries():
    print("LINEAR n/kernel-sizes/image-sizes/unit-repair-at-j=n")
    for n in (4, 8, 16):
        universe = range(1 << n)
        images = []
        kernels = []
        feasible_images = []
        for j in range(n + 1):
            image = {d_power(mask, n, j) for mask in universe}
            kernel = {mask for mask in universe if d_power(mask, n, j) == 0}
            images.append(image)
            kernels.append(kernel)
            check(len(kernel) == 1 << j, f"kernel size n={n}, j={j}")
            check(len(image) == 1 << (n - j), f"image size n={n}, j={j}")
            check(image == {mask for mask in universe
                            if d_power(mask, n, n - j) == 0},
                  f"image/kernel flag n={n}, j={j}")
            if j >= 1:
                feasible = {
                    d_power(mask, n, j)
                    for mask in universe if popcount(mask) != 1
                }
                feasible_images.append(feasible)
                check(feasible == image, f"feasible image n={n}, j={j}")
                ones = all_one_mask(n)
                check(ones in kernel, f"all-one kernel n={n}, j={j}")
                for i in range(n):
                    unit = 1 << i
                    repair = unit ^ ones
                    check(popcount(repair) == n - 1 and popcount(repair) != 1,
                          f"unit repair weight n={n}, j={j}, i={i}")
                    check(d_power(repair, n, j) == d_power(unit, n, j),
                          f"unit repair coset n={n}, j={j}, i={i}")
        check(images[n] == {0}, f"nilpotence n={n}")
        check(kernels[n] == set(universe), f"terminal kernel n={n}")
        print("LINEAR", n,
              ",".join(str(len(kernels[j])) for j in (0, 1, n // 2, n)),
              ",".join(str(len(images[j])) for j in (0, 1, n // 2, n)),
              "PASS")

    # The stated n>=4 restriction is necessary for the proposed repair.
    n = 2
    ones = all_one_mask(n)
    check(popcount((1 << 0) ^ ones) == 1, "n=2 repair must remain forbidden")
    print("BOUNDARY n=2 unit-plus-one-has-weight=1 SUPPORT_REPAIR_FAILS_AS_STATED")


def check_last_shell_inequality():
    print("LAST_SHELL q/n/value/lower-bound-witness")
    for q in range(3, 11):
        x = q - 1
        for n in (4, 8, 16):
            last = (q ** n - (q - 2) ** n) // 2 - x * (1 << (n - 1))
            leading = x * (n * x ** (n - 2) - (1 << (n - 1)))
            check(n * x ** (n - 2) > (1 << (n - 1)),
                  f"strict elementary inequality q={q}, n={n}")
            check(last >= leading > 0, f"last shell positive q={q}, n={n}")
            if q in (3, 4) and n in (4, 8):
                print("LAST_SHELL", q, n, last, leading)


def check_change_mask_multiplicity(n, q, words):
    observed = Counter(tuple_to_mask(change_mask(word)) for word in words)
    check(sum(observed.values()) == q ** n, f"change mass n={n}, q={q}")
    for mask in range(1 << n):
        expected = chi(q, popcount(mask))
        check(observed[mask] == expected,
              f"change multiplicity n={n}, q={q}, mask={mask}")
        check((expected == 0) == (popcount(mask) == 1),
              f"support hole n={n}, q={q}, mask={mask}")


def check_literal_box(n, q):
    words = tuple(product(range(q), repeat=n))
    check_change_mask_multiplicity(n, q, words)
    ones = tuple(1 for _ in range(n))
    depth_hist = Counter()
    endpoint_counts = [Counter() for _ in range(n + 3)]

    for word in words:
        c = tuple_to_mask(change_mask(word))
        state = word
        endpoint_counts[0][state] += 1
        direct_depth = literal_depth(word)
        formula_depth = expected_depth(word)
        check(direct_depth == formula_depth,
              f"depth formula n={n}, q={q}, word={word}")
        depth_hist[direct_depth] += 1
        for t in range(1, n + 3):
            state = literal_t(state)
            endpoint_counts[t][state] += 1
            formula = all_one_mask(n) ^ d_power(c, n, min(t - 1, n))
            check(tuple_to_mask(state) == formula,
                  f"iterate identity n={n}, q={q}, t={t}, word={word}")

    check(len(endpoint_counts[0]) == q ** n,
          f"time-zero image n={n}, q={q}")
    check(all(multiplicity == 1 for multiplicity in endpoint_counts[0].values()),
          f"time-zero singleton fibres n={n}, q={q}")

    check(depth_hist[0] == 1, f"depth zero n={n}, q={q}")
    check(depth_hist[1] == q - 1, f"depth one n={n}, q={q}")
    check(max(depth_hist) == n + 1, f"sharp height n={n}, q={q}")
    c_masses = [kernel_mass(n, q, j) for j in range(n + 1)]
    check(c_masses[0] == q, f"C0 n={n}, q={q}")
    check(c_masses[n] == q ** n, f"Cn n={n}, q={q}")
    for j in range(1, n + 1):
        check(depth_hist[j + 1] == c_masses[j] - c_masses[j - 1],
              f"shell n={n}, q={q}, j={j}")
    for j in dyadic_divisors_below(n):
        checkpoint = (1 + (q - 1) ** (n // j)) ** j + (q - 1) * (1 << j)
        check(c_masses[j] == checkpoint,
              f"checkpoint n={n}, q={q}, j={j}")
    last_formula = (q ** n - (q - 2) ** n) // 2 - (q - 1) * (1 << (n - 1))
    check(depth_hist[n + 1] == last_formula > 0,
          f"last shell n={n}, q={q}")

    for t in range(1, n + 3):
        j = min(t - 1, n)
        predicted = weighted_pushforward(n, q, j)
        actual = endpoint_counts[t]
        check(all(set(target) <= {0, 1} for target in actual),
              f"positive endpoint binary n={n}, q={q}, t={t}")
        check(len(actual) == ((1 << n) - n if t == 1 else 1 << (n - j)),
              f"image size n={n}, q={q}, t={t}")
        for ymask in range(1 << n):
            y = mask_to_tuple(ymask, n)
            d = ymask ^ all_one_mask(n)
            check(actual[y] == predicted[d],
                  f"every-target fibre n={n}, q={q}, t={t}, y={ymask}")
        check(sum(actual.values()) == q ** n, f"fibre mass n={n}, q={q}, t={t}")

    check(endpoint_counts[n + 1] == Counter({ones: q ** n}),
          f"terminal cap n={n}, q={q}")
    check(endpoint_counts[n + 2] == endpoint_counts[n + 1],
          f"post-cap n={n}, q={q}")
    images = [len(endpoint_counts[t]) for t in range(1, n + 2)]
    print("LITERAL", n, q, len(words), max(depth_hist),
          ",".join(map(str, images)), depth_hist[n + 1])


def parameter_spectra(n, q):
    x = q - 1
    t2 = weighted_pushforward(n, q, 1)
    rep1 = {}
    for c in range(1 << n):
        rep1.setdefault(d_power(c, n, 1), c)
    class1 = Counter()
    by_value_actual1 = Counter()
    for d, fibre in t2.items():
        c = rep1[d]
        r = min(popcount(c), n - popcount(c))
        class1[r] += 1
        expected = x ** r + x ** (n - r) + 2 * x * ((-1) ** r)
        check(fibre == expected, f"time2 value n={n}, q={q}, r={r}")
        by_value_actual1[fibre] += 1
    by_value_class1 = Counter()
    for r in range(n // 2 + 1):
        multiplicity = comb(n, r) if r < n // 2 else comb(n, r) // 2
        check(class1[r] == multiplicity, f"time2 class n={n}, q={q}, r={r}")
        value = x ** r + x ** (n - r) + 2 * x * ((-1) ** r)
        by_value_class1[value] += multiplicity
    check(by_value_actual1 == by_value_class1,
          f"time2 collision aggregation n={n}, q={q}")

    half = n // 2
    mid = weighted_pushforward(n, q, half)
    classm = Counter()
    by_value_actualm = Counter()
    for d, fibre in mid.items():
        lower = d & ((1 << half) - 1)
        upper = d >> half
        check(lower == upper, f"midpoint duplicated target n={n}, q={q}")
        h = popcount(lower)
        classm[h] += 1
        expected = (1 + x * x) ** (half - h) * (2 * x) ** h \
            + x * (1 << half) * ((-1) ** h)
        check(fibre == expected, f"midpoint value n={n}, q={q}, h={h}")
        by_value_actualm[fibre] += 1
    by_value_classm = Counter()
    for h in range(half + 1):
        multiplicity = comb(half, h)
        check(classm[h] == multiplicity, f"midpoint class n={n}, q={q}, h={h}")
        value = (1 + x * x) ** (half - h) * (2 * x) ** h \
            + x * (1 << half) * ((-1) ** h)
        by_value_classm[value] += multiplicity
    check(by_value_actualm == by_value_classm,
          f"midpoint collision aggregation n={n}, q={q}")
    check(sum(value * count for value, count in by_value_actual1.items()) == q ** n,
          f"time2 mass n={n}, q={q}")
    check(sum(value * count for value, count in by_value_actualm.items()) == q ** n,
          f"midpoint mass n={n}, q={q}")

    collisions1 = []
    value_to_r = defaultdict(list)
    for r in range(n // 2 + 1):
        value = x ** r + x ** (n - r) + 2 * x * ((-1) ** r)
        value_to_r[value].append(r)
    collisions1 = [tuple(rs) for _, rs in sorted(value_to_r.items()) if len(rs) > 1]
    value_to_h = defaultdict(list)
    for h in range(half + 1):
        value = (1 + x * x) ** (half - h) * (2 * x) ** h \
            + x * (1 << half) * ((-1) ** h)
        value_to_h[value].append(h)
    collisionsm = [tuple(hs) for _, hs in sorted(value_to_h.items()) if len(hs) > 1]
    return collisions1, collisionsm


def check_spectra():
    print("SPECTRA n/q/time2-collisions/midpoint-collisions")
    collision_records = []
    for n in (4, 8, 16):
        for q in (3, 4, 5, 7):
            c1, cm = parameter_spectra(n, q)
            if c1 or cm:
                collision_records.append((n, q, c1, cm))
                print("SPECTRA", n, q, repr(c1), repr(cm))
    expected = [
        (4, 4, [(1, 2)], [(1, 2)]),
        (8, 3, [(3, 4)], [(3, 4)]),
    ]
    check(collision_records == expected, "registered collision list")
    print("SPECTRA collision-aggregation PASS")


def main():
    prove_linear_boundaries()
    check_last_shell_inequality()
    print("LITERAL n/q/words/height/image-sizes-t1..t(n+1)/last-shell")
    boxes = ((4, 3), (4, 4), (4, 5), (4, 6), (8, 3), (8, 4))
    check(sum(q ** n for n, q in boxes) == 74355, "literal box total")
    for n, q in boxes:
        check_literal_box(n, q)
    check_spectra()
    print("BOUNDARY t=0 identity; t=n+1 singleton cap; nonbinary positive-time fibres zero")
    print(f"ASSERTIONS {ASSERTIONS}")
    print("THEOREMS A-D PASS")
    print("FINDINGS 0_CRITICAL 0_MAJOR 2_MINOR")
    print("VERDICT REVISE_MINOR HOLD_EXTERNAL")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
