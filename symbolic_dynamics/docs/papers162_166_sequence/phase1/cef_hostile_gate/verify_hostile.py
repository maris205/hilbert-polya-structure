#!/usr/bin/env python3
"""Independent hostile verifier for cyclic equality feedback (CEF).

This implementation deliberately uses packed binary integers, direct word
iteration, and an independently derived character sum.  It imports no author
code and does not call any file from the scout directory.
"""

from collections import Counter, defaultdict
from itertools import product
from math import comb


ASSERTIONS = 0
FOURIER_CHECKS = 0


def verify(condition, label):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def right_rotation(bits, n):
    return (bits >> 1) | ((bits & 1) << (n - 1))


def left_rotation(bits, n):
    cap = (1 << n) - 1
    return ((bits << 1) & cap) | (bits >> (n - 1))


def delta(bits, n):
    """Packed form of (Dc)_i=c_i+c_(i+1) over F_2."""
    return bits ^ right_rotation(bits, n)


def delta_transpose(bits, n):
    return bits ^ left_rotation(bits, n)


def delta_power(bits, exponent, n):
    for _ in range(exponent):
        bits = delta(bits, n)
    return bits


def delta_transpose_power(bits, exponent, n):
    for _ in range(exponent):
        bits = delta_transpose(bits, n)
    return bits


def change_bits(word):
    n = len(word)
    ans = 0
    for i in range(n):
        if word[i] != word[(i + 1) % n]:
            ans |= 1 << i
    return ans


def equality_update(word):
    n = len(word)
    return tuple(int(word[i] == word[(i + 1) % n]) for i in range(n))


def literal_iterate(word, time):
    for _ in range(time):
        word = equality_update(word)
    return word


def packed_binary(word):
    ans = 0
    for i, x in enumerate(word):
        if x:
            ans |= 1 << i
    return ans


def binary_tuple(bits, n):
    return tuple((bits >> i) & 1 for i in range(n))


def closed_iterate(word, time):
    if time == 0:
        return word
    n = len(word)
    ones = (1 << n) - 1
    return binary_tuple(ones ^ delta_power(change_bits(word), time - 1, n), n)


def colouring_multiplicity(mask, n, q):
    changes = mask.bit_count()
    return (q - 1) ** changes + (-1) ** changes * (q - 1)


def absorption_depth(word):
    n = len(word)
    goal = (1,) * n
    if word == goal:
        return 0
    for time in range(1, n + 2):
        word = equality_update(word)
        if word == goal:
            return time
    raise AssertionError(("nonabsorbed", word))


def weight_profile_by_image(n, exponent):
    profiles = defaultdict(Counter)
    for c in range(1 << n):
        profiles[delta_power(c, exponent, n)][c.bit_count()] += 1
    return profiles


def evaluate_profile(profile, value):
    return sum(count * value ** weight for weight, count in profile.items())


def fourier_affine_weight(n, exponent, target, value):
    """Character-orthogonality evaluation of sum_(D^j c=d) value^wt(c)."""
    global FOURIER_CHECKS
    numerator = 0
    for character in range(1 << n):
        dual = delta_transpose_power(character, exponent, n)
        sign = -1 if (character & target).bit_count() & 1 else 1
        dual_weight = dual.bit_count()
        numerator += (
            sign
            * (1 + value) ** (n - dual_weight)
            * (1 - value) ** dual_weight
        )
    verify(numerator % (1 << n) == 0,
           ("Fourier integrality", n, exponent, target, value, numerator))
    FOURIER_CHECKS += 1
    return numerator // (1 << n)


def exact_box(n, q):
    all_words = tuple(product(range(q), repeat=n))
    all_masks = range(1 << n)
    ones = (1 << n) - 1

    # Literal nonlinear front and its cycle-colouring multiplicity.
    multiplicities = Counter(change_bits(w) for w in all_words)
    for c in all_masks:
        verify(multiplicities[c] == colouring_multiplicity(c, n, q),
               ("change multiplicity", n, q, c, multiplicities[c]))
    verify(multiplicities[0] == q, ("constant words", n, q))
    verify(all(multiplicities[1 << i] == 0 for i in range(n)),
           ("one-change hole", n, q))
    verify(all(multiplicities[c] > 0
               for c in all_masks if c.bit_count() != 1),
           ("all other masks occur", n, q))

    # Independent packed-operator audit: nilpotent single Jordan filtration,
    # image=opposite kernel, dyadic repetition profiles, last hyperplane.
    kernels = []
    image_sets = []
    for j in range(n + 1):
        kernel = {c for c in all_masks if delta_power(c, j, n) == 0}
        image = {delta_power(c, j, n) for c in all_masks}
        kernels.append(kernel)
        image_sets.append(image)
        verify(len(kernel) == 1 << j, ("kernel size", n, j, len(kernel)))
        verify(len(image) == 1 << (n - j), ("image size", n, j, len(image)))
        opposite = {d for d in all_masks if delta_power(d, n - j, n) == 0}
        verify(image == opposite, ("image-filter equality", n, j))
        if j:
            verify(kernels[j - 1] < kernel, ("strict kernel flag", n, j))
    verify(all(delta_power(c, n, n) == 0 for c in all_masks), ("D^n", n))
    verify(kernels[n - 1] == {c for c in all_masks if c.bit_count() % 2 == 0},
           ("last kernel even hyperplane", n))

    for j in (1, 2, 4, 8, 16):
        if j >= n:
            continue
        observed = Counter(c.bit_count() for c in kernels[j])
        expected = Counter({k * (n // j): comb(j, k) for k in range(j + 1)})
        verify(observed == expected, ("dyadic repeated-block kernel", n, j,
                                      observed, expected))

    # Literal iterates, unique recurrence, exact depth census and last layer.
    depths = Counter()
    for word in all_words:
        depth = absorption_depth(word)
        depths[depth] += 1
        for time in range(n + 3):
            verify(literal_iterate(word, time) == closed_iterate(word, time),
                   ("closed iterate", n, q, word, time))
    verify(depths[0] == 1, ("unique recurrent one", n, q, depths))
    verify(depths[1] == q - 1, ("other constants", n, q, depths))
    verify(max(depths) == n + 1, ("sharp height", n, q, depths))

    previous_cdf = q
    for j in range(1, n + 1):
        cdf = sum(colouring_multiplicity(c, n, q) for c in kernels[j])
        verify(sum(v for d, v in depths.items() if d <= j + 1) == cdf,
               ("kernel-filter CDF", n, q, j, cdf))
        verify(depths[j + 1] == cdf - previous_cdf,
               ("depth shell", n, q, j, depths[j + 1], cdf - previous_cdf))
        previous_cdf = cdf
        if j & (j - 1) == 0 and j < n:
            checkpoint = (1 + (q - 1) ** (n // j)) ** j + (q - 1) * 2 ** j
            verify(cdf == checkpoint, ("dyadic CDF", n, q, j, cdf, checkpoint))

    last = ((q ** n - (q - 2) ** n) // 2
            - (q - 1) * 2 ** (n - 1))
    verify(depths[n + 1] == last and last > 0,
           ("sharp last layer", n, q, depths[n + 1], last))

    # Every-target fibres.  Profiles are computed from packed masks, while
    # observed fibres are computed by literal q-ary iteration.
    image_sizes = []
    largest_fibre = 0
    for time in range(n + 3):
        observed = Counter(literal_iterate(w, time) for w in all_words)
        image_sizes.append(len(observed))
        if time == 0:
            verify(len(observed) == q ** n and set(observed.values()) == {1},
                   ("identity", n, q))
            continue

        exponent = min(time - 1, n)
        profiles = weight_profile_by_image(n, exponent)
        predicted_support = set()
        for target_bits in all_masks:
            target_word = binary_tuple(target_bits, n)
            d = target_bits ^ ones
            profile = profiles.get(d, Counter())
            weight_plus = evaluate_profile(profile, q - 1)
            weight_minus = evaluate_profile(profile, -1)
            predicted = weight_plus + (q - 1) * weight_minus
            verify(observed[target_word] == predicted,
                   ("every binary target", n, q, time, target_bits,
                    observed[target_word], predicted))

            fourier_plus = fourier_affine_weight(n, exponent, d, q - 1)
            fourier_minus = fourier_affine_weight(n, exponent, d, -1)
            verify(weight_plus == fourier_plus and weight_minus == fourier_minus,
                   ("affine Fourier", n, q, time, target_bits,
                    weight_plus, fourier_plus, weight_minus, fourier_minus))
            if predicted:
                predicted_support.add(target_word)
                largest_fibre = max(largest_fibre, predicted)

        verify(set(observed) == predicted_support,
               ("exact target support", n, q, time))
        # A genuinely q-ary target is impossible after one update.
        nonbinary = (2,) + (0,) * (n - 1)
        verify(observed[nonbinary] == 0, ("nonbinary target hole", n, q, time))

        if time == 1:
            forbidden = {binary_tuple(ones ^ (1 << i), n) for i in range(n)}
            verify(set(product((0, 1), repeat=n)) - set(observed) == forbidden,
                   ("exact time-one holes", n, q))
            verify(len(observed) == (1 << n) - n, ("time-one image", n, q))
        else:
            expected_image = 1 << (n - exponent)
            verify(len(observed) == expected_image,
                   ("later image size", n, q, time, len(observed), expected_image))
            for target in observed:
                d = packed_binary(target) ^ ones
                verify(delta_power(d, n - exponent, n) == 0,
                       ("later image filter", n, q, time, target))

        if time >= n + 1:
            verify(observed == Counter({(1,) * n: q ** n}),
                   ("post-cap", n, q, time, observed))

    # Labelled-graph recovery claims.
    first_fibres = Counter(equality_update(w) for w in all_words)
    verify(first_fibres[(1,) * n] == q, ("recover q", n, q))
    verify(max(depths) - 1 == n, ("recover n", n, q))
    return {
        "states": q ** n,
        "height": max(depths),
        "last": last,
        "images": image_sizes,
        "max_fibre": largest_fibre,
    }


def excluded_boundary_sentinels():
    # n=2 is excluded for a real reason: adding the all-one kernel vector to a
    # forbidden unit vector produces the other forbidden unit vector.
    n, q = 2, 3
    words = tuple(product(range(q), repeat=n))
    time_two_image = {literal_iterate(w, 2) for w in words}
    verify(len(time_two_image) == 1, ("n=2 sentinel", time_two_image))
    verify(len(time_two_image) != 1 << (n - 1), ("n=2 theorem must fail",))

    # q=2 is also essential: only even change masks occur, rather than every
    # mask except the unit vectors.
    n, q = 4, 2
    words = tuple(product(range(q), repeat=n))
    first_image = {literal_iterate(w, 1) for w in words}
    verify(len(first_image) == 8, ("q=2 sentinel", len(first_image)))
    verify(len(first_image) != (1 << n) - n, ("q=2 theorem must fail",))
    return "n2_time2_image=1 q2_n4_time1_image=8"


def main():
    print("CEF_INDEPENDENT_HOSTILE_GATE_V1")
    print("IMPLEMENTATION=PACKED_BITS_DIRECT_ITERATION_NO_AUTHOR_IMPORT")
    boxes = ((4, 3), (4, 4), (4, 5), (4, 7), (8, 3), (8, 4))
    rows = []
    for n, q in boxes:
        result = exact_box(n, q)
        rows.append(
            f"n={n},q={q}|states={result['states']}|height={result['height']}|"
            f"last={result['last']}|images={','.join(map(str, result['images']))}|"
            f"max_fibre={result['max_fibre']}"
        )
    sentinel = excluded_boundary_sentinels()
    print(f"BOXES={len(boxes)}")
    for row in rows:
        print(row)
    print("BOUNDARY_SENTINELS=" + sentinel)
    print(f"FOURIER_CHECKS={FOURIER_CHECKS}")
    print(f"ASSERTIONS={ASSERTIONS}")
    print("MATH_STATUS=PASS")
    print("EXTERNAL=HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
