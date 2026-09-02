#!/usr/bin/env python3
"""Fresh independent verifier for the repaired CEF V2 theorem package.

The scout module is never imported.  Literal q-ary trajectories, packed
cyclic binary operators, affine profiles, and Walsh sums are reconstructed
here from the definition of the map.
"""

from collections import Counter, defaultdict
from itertools import product
from math import comb


ASSERTIONS = 0
WALSH_EVALUATIONS = 0
SPECTRAL_TARGETS = 0


def check(statement, receipt):
    global ASSERTIONS
    ASSERTIONS += 1
    if not statement:
        raise AssertionError(receipt)


def cyclic_next_xor(bits, n):
    """Bit i becomes old bit i XOR old bit i+1 (indices modulo n)."""
    neighbor = (bits >> 1) | ((bits & 1) << (n - 1))
    return bits ^ neighbor


def cyclic_previous_xor(bits, n):
    """Transpose operator: bit i becomes old bit i XOR old bit i-1."""
    cap = (1 << n) - 1
    neighbor = ((bits << 1) & cap) | (bits >> (n - 1))
    return bits ^ neighbor


def operator_power(bits, exponent, n, transpose=False):
    update = cyclic_previous_xor if transpose else cyclic_next_xor
    for _ in range(exponent):
        bits = update(bits, n)
    return bits


def literal_step(word):
    n = len(word)
    return tuple(int(word[i] == word[(i + 1) % n]) for i in range(n))


def literal_trajectory(word, horizon):
    history = [word]
    for _ in range(horizon):
        history.append(literal_step(history[-1]))
    return history


def change_mask(word):
    n = len(word)
    mask = 0
    for i in range(n):
        if word[i] != word[(i + 1) % n]:
            mask |= 1 << i
    return mask


def bits_to_word(bits, n):
    return tuple((bits >> i) & 1 for i in range(n))


def word_to_bits(word):
    return sum((int(bit) & 1) << i for i, bit in enumerate(word))


def mask_source_count(weight, q):
    a = q - 1
    return a ** weight + ((-1) ** weight) * a


def affine_profiles(n):
    """profiles[j][d] is the weight distribution on {c:D^j c=d}."""
    profiles = []
    current = list(range(1 << n))
    for j in range(n + 1):
        by_target = defaultdict(Counter)
        for c, d in enumerate(current):
            by_target[d][c.bit_count()] += 1
        profiles.append(dict(by_target))
        current = [cyclic_next_xor(d, n) for d in current]
    return profiles


def evaluate_change_weight_profile(profile, q):
    return sum(count * mask_source_count(weight, q)
               for weight, count in profile.items())


def evaluate_power_profile(profile, a):
    return sum(count * a ** weight for weight, count in profile.items())


def walsh_affine_enumerator(n, exponent, target, a):
    global WALSH_EVALUATIONS
    numerator = 0
    for character in range(1 << n):
        dual = operator_power(character, exponent, n, transpose=True)
        sign = -1 if ((character & target).bit_count() & 1) else 1
        k = dual.bit_count()
        numerator += sign * (1 + a) ** (n - k) * (1 - a) ** k
    check(numerator % (1 << n) == 0,
          ("Walsh divisibility", n, exponent, target, a, numerator))
    WALSH_EVALUATIONS += 1
    return numerator // (1 << n)


def direct_box(n, q, do_walsh):
    all_words = tuple(product(range(q), repeat=n))
    cap = (1 << n) - 1
    goal = (1,) * n
    profiles = affine_profiles(n)

    # The q-ary front is checked literally, not inferred from colouring.
    observed_masks = Counter(change_mask(word) for word in all_words)
    for mask in range(1 << n):
        predicted = mask_source_count(mask.bit_count(), q)
        check(observed_masks[mask] == predicted,
              ("fixed change mask", n, q, mask, observed_masks[mask], predicted))
    check(observed_masks[0] == q, ("constant front", n, q))
    check(all(observed_masks[1 << i] == 0 for i in range(n)),
          ("unit masks absent", n, q))
    check(all(observed_masks[c] > 0 for c in range(1 << n)
              if c.bit_count() != 1), ("all other masks occur", n, q))

    # Linear flag and the exact repeated-block checkpoints.
    kernels = []
    images = []
    for j in range(n + 1):
        kernel = {c for c in range(1 << n)
                  if operator_power(c, j, n) == 0}
        image = {operator_power(c, j, n) for c in range(1 << n)}
        kernels.append(kernel)
        images.append(image)
        check(len(kernel) == 1 << j, ("kernel size", n, j, len(kernel)))
        check(len(image) == 1 << (n - j), ("image size", n, j, len(image)))
        opposite_kernel = {d for d in range(1 << n)
                           if operator_power(d, n - j, n) == 0}
        check(image == opposite_kernel, ("image/kernel flag", n, j))
        check(set(profiles[j]) == image, ("profile support", n, j))
    check(kernels[n - 1] == {c for c in range(1 << n)
                             if c.bit_count() % 2 == 0},
          ("penultimate kernel", n))
    for j in range(1, n):
        if j & (j - 1):
            continue
        weights = Counter(c.bit_count() for c in kernels[j])
        repeated = Counter({k * (n // j): comb(j, k)
                            for k in range(j + 1)})
        check(weights == repeated, ("repeated block", n, j, weights, repeated))

    # One pass supplies every literal iterate, fibre, image, and exact depth.
    horizon = n + 2
    literal_fibres = [Counter() for _ in range(horizon + 1)]
    depths = Counter()
    for word in all_words:
        history = literal_trajectory(word, horizon)
        hit = None
        c = change_mask(word)
        for time, state in enumerate(history):
            literal_fibres[time][state] += 1
            if time == 0:
                predicted_state = word
            else:
                predicted_bits = cap ^ operator_power(c, time - 1, n)
                predicted_state = bits_to_word(predicted_bits, n)
            check(state == predicted_state,
                  ("closed iterate", n, q, word, time, state, predicted_state))
            if hit is None and state == goal:
                hit = time
        check(hit is not None, ("absorption", n, q, word))
        depths[hit] += 1

    check(depths[0] == 1, ("unique recurrent state", n, q, depths))
    check(depths[1] == q - 1, ("other constants depth one", n, q, depths))
    check(max(depths) == n + 1, ("sharp height", n, q, depths))

    previous_cdf = q
    for j in range(1, n + 1):
        cdf = sum(mask_source_count(c.bit_count(), q) for c in kernels[j])
        observed_cdf = sum(count for depth, count in depths.items()
                           if depth <= j + 1)
        check(cdf == observed_cdf, ("depth CDF", n, q, j, cdf, observed_cdf))
        check(depths[j + 1] == cdf - previous_cdf,
              ("depth shell", n, q, j, depths[j + 1], cdf - previous_cdf))
        if not (j & (j - 1)) and j < n:
            a = q - 1
            checkpoint = (1 + a ** (n // j)) ** j + a * (1 << j)
            check(cdf == checkpoint, ("checkpoint CDF", n, q, j, cdf, checkpoint))
        previous_cdf = cdf

    last = ((q ** n - (q - 2) ** n) // 2
            - (q - 1) * (1 << (n - 1)))
    check(depths[n + 1] == last and last > 0,
          ("last shell", n, q, depths[n + 1], last))

    image_sizes = []
    for time, observed in enumerate(literal_fibres):
        image_sizes.append(len(observed))
        if time == 0:
            check(len(observed) == q ** n and set(observed.values()) == {1},
                  ("time zero identity", n, q))
            continue
        exponent = min(time - 1, n)
        predicted = {}
        for deviation, profile in profiles[exponent].items():
            value = evaluate_change_weight_profile(profile, q)
            if value:
                predicted[bits_to_word(cap ^ deviation, n)] = value
        check(dict(observed) == predicted,
              ("all target fibres", n, q, time))
        check(observed[(2,) + (0,) * (n - 1)] == 0,
              ("nonbinary target", n, q, time))
        if time == 1:
            holes = {bits_to_word(cap ^ (1 << i), n) for i in range(n)}
            binary = set(product((0, 1), repeat=n))
            check(binary - set(observed) == holes, ("time-one holes", n, q))
            check(len(observed) == (1 << n) - n, ("time-one image", n, q))
        else:
            check(len(observed) == 1 << (n - exponent),
                  ("later image", n, q, time, len(observed)))
        if time >= n + 1:
            check(observed == Counter({goal: q ** n}),
                  ("stable sink", n, q, time, observed))

    check(literal_fibres[1][goal] == q, ("recover q", n, q))
    check(max(depths) - 1 == n, ("recover n", n, q))

    if do_walsh:
        for j, by_target in enumerate(profiles):
            for d in range(1 << n):
                profile = by_target.get(d, Counter())
                for a in (q - 1, -1):
                    direct = evaluate_power_profile(profile, a)
                    transformed = walsh_affine_enumerator(n, j, d, a)
                    check(direct == transformed,
                          ("Walsh affine formula", n, q, j, d, a,
                           direct, transformed))

    return (f"n={n},q={q}|states={q**n}|height={max(depths)}|last={last}|"
            f"images={','.join(map(str, image_sizes))}")


def second_time_value(n, q, radius):
    a = q - 1
    return a ** radius + a ** (n - radius) + 2 * a * ((-1) ** radius)


def midpoint_value(n, q, half_weight):
    a = q - 1
    half = n // 2
    return ((1 + a * a) ** (half - half_weight)
            * (2 * a) ** half_weight
            + a * (1 << half) * ((-1) ** half_weight))


def spectrum_box(n, q):
    global SPECTRAL_TARGETS
    profiles = affine_profiles(n)

    # t=2: solve D c=d by the profile itself; do not construct a preferred
    # antiderivative.  The radius must emerge as a complement-pair invariant.
    second_classes = Counter()
    second_values = Counter()
    for d, profile in profiles[1].items():
        SPECTRAL_TARGETS += 1
        check(d.bit_count() % 2 == 0, ("t2 support parity", n, q, d))
        check(sum(profile.values()) == 2, ("t2 two solutions", n, q, d, profile))
        weights = sorted(profile.elements())
        check(weights[0] + weights[-1] == n,
              ("t2 complementary weights", n, q, d, weights))
        radius = weights[0]
        check(0 <= radius <= n // 2, ("t2 radius", n, q, d, radius))
        actual = evaluate_change_weight_profile(profile, q)
        expected = second_time_value(n, q, radius)
        check(actual == expected, ("t2 value", n, q, d, actual, expected))
        check(actual > 0, ("t2 positive support", n, q, d, actual))
        second_classes[radius] += 1
        second_values[actual] += 1
    expected_classes = Counter({r: (comb(n, r) if r < n // 2
                                    else comb(n, r) // 2)
                                for r in range(n // 2 + 1)})
    check(second_classes == expected_classes,
          ("t2 class multiplicities", n, q, second_classes, expected_classes))
    expected_values = Counter()
    for r, multiplicity in expected_classes.items():
        expected_values[second_time_value(n, q, r)] += multiplicity
    check(second_values == expected_values,
          ("t2 aggregated numerical spectrum", n, q,
           second_values, expected_values))
    check(sum(second_values.values()) == 1 << (n - 1),
          ("t2 target mass", n, q))
    check(sum(value * multiplicity for value, multiplicity in second_values.items())
          == q ** n, ("t2 source mass", n, q))

    # Midpoint: again start from all solutions.  Support and local pair
    # factorization are inferred and then checked against the closed formula.
    half = n // 2
    mid_classes = Counter()
    mid_values = Counter()
    for d, profile in profiles[half].items():
        SPECTRAL_TARGETS += 1
        low = d & ((1 << half) - 1)
        high = d >> half
        check(low == high, ("midpoint duplicated target", n, q, d))
        h = low.bit_count()
        actual = evaluate_change_weight_profile(profile, q)
        expected = midpoint_value(n, q, h)
        check(actual == expected,
              ("midpoint value", n, q, d, h, actual, expected))
        check(actual > 0, ("midpoint positive support", n, q, d, actual))
        mid_classes[h] += 1
        mid_values[actual] += 1
    expected_mid_classes = Counter({h: comb(half, h)
                                    for h in range(half + 1)})
    check(mid_classes == expected_mid_classes,
          ("midpoint class multiplicities", n, q,
           mid_classes, expected_mid_classes))
    expected_mid_values = Counter()
    for h, multiplicity in expected_mid_classes.items():
        expected_mid_values[midpoint_value(n, q, h)] += multiplicity
    check(mid_values == expected_mid_values,
          ("midpoint aggregated numerical spectrum", n, q,
           mid_values, expected_mid_values))
    check(sum(mid_values.values()) == 1 << half,
          ("midpoint target mass", n, q))
    check(sum(value * multiplicity for value, multiplicity in mid_values.items())
          == q ** n, ("midpoint source mass", n, q))

    return (f"n={n},q={q}|t2_classes={len(second_classes)}|"
            f"t2_values={len(second_values)}|mid_classes={len(mid_classes)}|"
            f"mid_values={len(mid_values)}")


def excluded_boundaries():
    # n=2: both entries of an equality image agree, so the second image has
    # one state, contradicting the n>=4 affine-image repair.
    words2 = tuple(product(range(3), repeat=2))
    image2 = {literal_trajectory(word, 2)[2] for word in words2}
    check(image2 == {(1, 1)}, ("n=2 boundary", image2))
    check(len(image2) != 2, ("n=2 excluded image theorem", image2))

    # q=2: change masks are all even, not all masks except units.
    words_binary = tuple(product((0, 1), repeat=4))
    image_binary = {literal_step(word) for word in words_binary}
    check(len(image_binary) == 8, ("q=2 boundary", len(image_binary)))
    check(len(image_binary) != 12, ("q=2 excluded image theorem",))

    # A non-dyadic ring has a nonzero recurrent linear part.
    n = 6
    witness = 1
    check(operator_power(witness, n, n) != 0,
          ("nondyadic nilpotence boundary", n, witness))

    # t=0 is genuinely q-ary identity, not any positive-time binary formula.
    source = (2, 0, 1, 2)
    check(literal_trajectory(source, 0) == [source], ("t=0 boundary", source))

    return "n2_time2_image=1;q2_n4_time1_image=8;n6_D6_nonzero;t0_identity"


def main():
    print("CEF_REENTRY_INDEPENDENT_GATE_V1")
    print("IMPLEMENTATION=LITERAL_QARY_PLUS_FRESH_PACKED_PROFILES_NO_AUTHOR_IMPORT")

    direct_boxes = ((4, 3, True), (4, 4, True), (4, 5, False),
                    (4, 7, False), (8, 3, True), (8, 4, False))
    direct_rows = [direct_box(n, q, walsh) for n, q, walsh in direct_boxes]
    print(f"DIRECT_BOXES={len(direct_rows)}")
    for row in direct_rows:
        print(row)

    spectral_boxes = tuple((n, q) for n in (4, 8, 16)
                           for q in (3, 4, 5, 7))
    spectral_rows = [spectrum_box(n, q) for n, q in spectral_boxes]
    print(f"SPECTRAL_BOXES={len(spectral_rows)}")
    for row in spectral_rows:
        print(row)

    # Explicit hostile sentinels: class spectra need aggregation because
    # distinct radius/weight classes can share one numerical fibre value.
    check(second_time_value(4, 4, 1) == second_time_value(4, 4, 2) == 24,
          ("t2 collision sentinel",))
    check(midpoint_value(4, 4, 1) == midpoint_value(4, 4, 2) == 48,
          ("midpoint collision sentinel",))
    print("COLLISION_SENTINEL=n4,q4:t2[r1=r2=24];mid[h1=h2=48]")

    print("BOUNDARIES=" + excluded_boundaries())
    print(f"WALSH_EVALUATIONS={WALSH_EVALUATIONS}")
    print(f"SPECTRAL_TARGETS={SPECTRAL_TARGETS}")
    print(f"ASSERTIONS={ASSERTIONS}")
    print("MATH_STATUS=PASS")
    print("EXTERNAL=HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
