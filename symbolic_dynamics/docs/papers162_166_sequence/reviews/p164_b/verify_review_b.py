#!/usr/bin/env python3
"""Independent Hostile Review B verifier for P164.

The program constructs the q-ary equality-feedback map literally and derives
the binary linear tail locally.  It imports neither the author verifier nor
Review-A code or data.
"""

from collections import Counter, defaultdict
from itertools import product
from math import comb


ASSERTIONS = 0


def check(condition, label):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def all_one(n):
    return (1 << n) - 1


def tuple_to_mask(word):
    value = 0
    for i, bit in enumerate(word):
        check(bit in (0, 1), "binary tuple encoding")
        value |= bit << i
    return value


def mask_to_tuple(mask, n):
    return tuple((mask >> i) & 1 for i in range(n))


def literal_step(word):
    n = len(word)
    return tuple(int(word[i] == word[(i + 1) % n]) for i in range(n))


def change_mask(word):
    n = len(word)
    value = 0
    for i in range(n):
        if word[i] != word[(i + 1) % n]:
            value |= 1 << i
    return value


def shift_next(mask, n):
    """S with (Sx)_i=x_(i+1), using bit i for coordinate i."""
    return (mask >> 1) | ((mask & 1) << (n - 1))


def d_step(mask, n):
    return mask ^ shift_next(mask, n)


def d_power(mask, exponent, n):
    for _ in range(exponent):
        mask = d_step(mask, n)
    return mask


def chi(q, mask):
    r = mask.bit_count()
    return (q - 1) ** r + ((-1) ** r) * (q - 1)


def nil_index(mask, n):
    for j in range(n + 1):
        if mask == 0:
            return j
        mask = d_step(mask, n)
    raise AssertionError("dyadic D failed to vanish")


def weighted_kernel_mass(n, q, j):
    return sum(chi(q, c) for c in range(1 << n) if d_power(c, j, n) == 0)


def affine_components(n, q, j):
    """Return W_(j,d)(q-1), W_(j,d)(-1), and chi-weighted fibres."""
    x = q - 1
    positive = defaultdict(int)
    signed = defaultdict(int)
    fibres = defaultdict(int)
    for c in range(1 << n):
        d = d_power(c, j, n)
        r = c.bit_count()
        positive[d] += x**r
        signed[d] += (-1) ** r
        fibres[d] += chi(q, c)
    return dict(positive), dict(signed), dict(fibres)


def linear_image(n, j):
    return {d_power(c, j, n) for c in range(1 << n)}


def checkpoint_value(n, q, j):
    x = q - 1
    return (1 + x ** (n // j)) ** j + x * (2**j)


def last_shell_value(n, q):
    return (q**n - (q - 2) ** n) // 2 - (q - 1) * 2 ** (n - 1)


def full_box(n, q):
    one_tuple = (1,) * n
    one_mask = all_one(n)
    mask_counts = Counter()
    depth_counts = Counter()
    target_counts = [Counter() for _ in range(n + 3)]
    word_count = 0

    for word in product(range(q), repeat=n):
        word_count += 1
        c = change_mask(word)
        mask_counts[c] += 1

        if word == one_tuple:
            predicted_depth = 0
        elif c == 0:
            predicted_depth = 1
        else:
            predicted_depth = 1 + nil_index(c, n)

        state = word
        observed_depth = 0 if state == one_tuple else None
        for t in range(1, n + 3):
            state = literal_step(state)
            check(all(bit in (0, 1) for bit in state), "positive iterate is binary")
            state_mask = tuple_to_mask(state)
            target_counts[t][state_mask] += 1
            expected_mask = one_mask ^ d_power(c, min(t - 1, n), n)
            check(state_mask == expected_mask, "literal all-time iterate")
            if observed_depth is None and state == one_tuple:
                observed_depth = t
        check(observed_depth == predicted_depth, "pointwise depth")
        check(state == one_tuple, "absorption by dyadic nilpotence")
        depth_counts[observed_depth] += 1

    check(word_count == q**n, "full word census")
    for c in range(1 << n):
        check(mask_counts[c] == chi(q, c), "change-mask multiplicity")
        check((mask_counts[c] == 0) == (c.bit_count() == 1), "q>=3 feasibility boundary")

    check(target_counts[1] == Counter({one_mask ^ c: chi(q, c) for c in range(1 << n) if chi(q, c)}),
          "first target fibres")
    check(len(target_counts[1]) == 2**n - n, "first image cardinality")

    c_values = [weighted_kernel_mass(n, q, j) for j in range(n + 1)]
    check(c_values[0] == q, "constant-word cumulative boundary")
    check(c_values[n] == q**n, "full-kernel cumulative boundary")
    expected_depths = Counter({0: 1, 1: q - 1})
    for j in range(1, n + 1):
        expected_depths[j + 1] = c_values[j] - c_values[j - 1]
    check(depth_counts == expected_depths, "all depth shells")
    check(max(depth_counts) == n + 1, "sharp height")

    j = 1
    while j < n:
        check(c_values[j] == checkpoint_value(n, q, j), "dyadic checkpoint formula")
        j *= 2
    check(expected_depths[n + 1] == last_shell_value(n, q), "last shell formula")
    check(last_shell_value(n, q) > 0, "last shell positivity")

    for t in range(2, n + 3):
        j = min(t - 1, n)
        wx, wm, predicted_d = affine_components(n, q, j)
        expected_targets = Counter()
        for d in range(1 << n):
            predicted = wx.get(d, 0) + (q - 1) * wm.get(d, 0)
            check(predicted == predicted_d.get(d, 0), "affine enumerator evaluation")
            if predicted:
                expected_targets[one_mask ^ d] = predicted
            check(target_counts[t].get(one_mask ^ d, 0) == predicted, "every binary target fibre")
        check(target_counts[t] == expected_targets, "no nonbinary positive-time targets")
        check(set(predicted_d) == linear_image(n, j), "complete image staircase")
        check(len(target_counts[t]) == 2 ** (n - j), "image staircase cardinality")
        check(sum(target_counts[t].values()) == q**n, "all-time fibre mass")

    check(set(target_counts[n]) == {0, one_mask}, "time-n two-target boundary")
    check(target_counts[n][0] == last_shell_value(n, q), "last shell is time-n zero fibre")
    check(target_counts[n + 1] == Counter({one_mask: q**n}), "j=n collapse")
    check(target_counts[n + 2] == target_counts[n + 1], "post-collapse stability")
    check(literal_step(one_tuple) == one_tuple, "unique endpoint fixed")

    return {
        "n": n,
        "q": q,
        "words": word_count,
        "height": max(depth_counts),
        "image1": len(target_counts[1]),
        "last": depth_counts[n + 1],
    }


def verify_time_two(n, q):
    x = q - 1
    _, _, fibres = affine_components(n, q, 1)
    rho = {}
    for c in range(1 << n):
        d = d_step(c, n)
        candidate = min(c.bit_count(), n - c.bit_count())
        rho[d] = min(rho.get(d, n + 1), candidate)

    check(set(fibres) == {d for d in range(1 << n) if d.bit_count() % 2 == 0},
          "time-two support is even-weight")
    parameter_counts = Counter()
    actual_numerical = Counter()
    predicted_numerical = Counter()
    for d, value in fibres.items():
        r = rho[d]
        predicted = x**r + x ** (n - r) + 2 * x * ((-1) ** r)
        check(value == predicted, "time-two complementary-pair formula")
        check(value > 0, "time-two supported target positive")
        parameter_counts[r] += 1
        actual_numerical[value] += 1
    for r in range(n // 2 + 1):
        multiplicity = comb(n, r) if r < n // 2 else comb(n, r) // 2
        check(parameter_counts[r] == multiplicity, "time-two parameter multiplicity")
        value = x**r + x ** (n - r) + 2 * x * ((-1) ** r)
        predicted_numerical[value] += multiplicity
    check(actual_numerical == predicted_numerical, "time-two collision aggregation")
    check(sum(value * count for value, count in actual_numerical.items()) == q**n,
          "time-two mass")
    if (n, q) == (4, 4):
        v1 = x + x ** (n - 1) - 2 * x
        v2 = 2 * x ** (n // 2) + 2 * x
        check(v1 == v2 == 24, "advertised n=4 q=4 collision")
        check(actual_numerical[24] == 7, "collision classes merge to seven targets")
    return len(fibres), len(actual_numerical)


def verify_midpoint(n, q):
    half = n // 2
    x = q - 1
    _, _, fibres = affine_components(n, q, half)
    expected_support = {u | (u << half) for u in range(1 << half)}
    check(set(fibres) == expected_support, "midpoint duplicated-half support")
    parameter_counts = Counter()
    actual_numerical = Counter()
    predicted_numerical = Counter()
    for d, value in fibres.items():
        low = d & ((1 << half) - 1)
        high = d >> half
        check(low == high, "midpoint target has two equal halves")
        h = low.bit_count()
        predicted = (1 + x*x) ** (half - h) * (2*x) ** h + x * 2**half * ((-1) ** h)
        check(value == predicted, "midpoint half-weight formula")
        check(value > 0, "midpoint supported target positive")
        parameter_counts[h] += 1
        actual_numerical[value] += 1
    for h in range(half + 1):
        multiplicity = comb(half, h)
        check(parameter_counts[h] == multiplicity, "midpoint parameter multiplicity")
        value = (1 + x*x) ** (half - h) * (2*x) ** h + x * 2**half * ((-1) ** h)
        predicted_numerical[value] += multiplicity
    check(actual_numerical == predicted_numerical, "midpoint collision aggregation")
    check(sum(value * count for value, count in actual_numerical.items()) == q**n,
          "midpoint mass")
    return len(fibres), len(actual_numerical)


def verify_symbolic_dyadic_boundaries():
    for n in (4, 8, 16, 32):
        check(d_power(all_one(n), 1, n) == 0, "D kills constants")
        if n <= 12:
            for c in range(1 << n):
                check(d_power(c, n, n) == 0, "D^n vanishes")
        # Basis-vector rank test: im D^j has exactly 2^(n-j) elements.
        if n <= 16:
            for j in range(n + 1):
                check(len(linear_image(n, j)) == 2 ** (n - j), "single-block image rank")
        for q in (3, 4, 5, 7):
            value = last_shell_value(n, q)
            check(value > 0, "symbolic last-shell positivity")
            if n <= 16:
                check(value == q**n - weighted_kernel_mass(n, q, n - 1),
                      "symbolic last-shell difference")


def verify_excluded_boundaries():
    # q=2: feasible change masks are even-weight, not merely non-units.
    n = 4
    binary_counts = Counter(change_mask(word) for word in product(range(2), repeat=n))
    for c in range(1 << n):
        check(binary_counts[c] == (2 if c.bit_count() % 2 == 0 else 0), "q=2 mask boundary")
    check(len(binary_counts) == 2 ** (n - 1), "q=2 first image differs")
    check(len(binary_counts) != 2**n - n, "q=2 excludes first-image formula")

    # n=2: adding the all-one kernel vector maps a unit to the other unit, so
    # the every-coset support repair used for n>=4 fails.
    n = 2
    q = 3
    t2 = Counter()
    for word in product(range(q), repeat=n):
        state = literal_step(literal_step(word))
        t2[tuple_to_mask(state)] += 1
    check(len(t2) == 1, "n=2 second image singleton")
    check(len(t2) != 2 ** (n - 1), "n=2 image staircase excluded")

    # Nondyadic length: D need not be nilpotent.
    n = 6
    check(d_power(1, n, n) != 0, "nondyadic D^n is nonzero")
    feasible = all_one(n) ^ 1
    check(chi(3, feasible) > 0, "nondyadic witness is feasible")
    check(all(d_power(feasible, j, n) != 0 for j in range(13)),
          "nondyadic witness does not absorb in claimed window")

    # Only dyadic checkpoints use D^j=I+S^j.
    n = 8
    witness = 1
    check(d_power(witness, 3, n) != (witness ^ shift_by(witness, 3, n)),
          "nondyadic checkpoint exponent excluded")


def shift_by(mask, amount, n):
    amount %= n
    if amount == 0:
        return mask
    low = mask & ((1 << amount) - 1)
    return (mask >> amount) | (low << (n - amount))


def main():
    full_rows = []
    for n, q in ((4, 3), (4, 4), (4, 5), (4, 6), (8, 3), (8, 4)):
        row = full_box(n, q)
        full_rows.append(
            f"n={n},q={q},words={row['words']},height={row['height']},"
            f"image1={row['image1']},last={row['last']}"
        )

    spectrum_rows = []
    for n in (4, 8, 16):
        for q in (3, 4, 5, 7):
            t2_targets, t2_values = verify_time_two(n, q)
            mid_targets, mid_values = verify_midpoint(n, q)
            spectrum_rows.append(
                f"n={n},q={q},t2={t2_targets}/{t2_values},"
                f"mid={mid_targets}/{mid_values}"
            )

    verify_symbolic_dyadic_boundaries()
    verify_excluded_boundaries()

    print("P164_HOSTILE_REVIEW_B_INDEPENDENT")
    print("FULL=" + ";".join(full_rows))
    print("SPECTRA=" + ";".join(spectrum_rows))
    print("BOUNDARIES=q2,n2,nondyadic,j=n,time_n,last_shell,collision_merge")
    print("CHECKS=literal,mask,iterate,depth,image,fibre,t2,midpoint,excluded")
    print(f"ASSERTIONS={ASSERTIONS}")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
