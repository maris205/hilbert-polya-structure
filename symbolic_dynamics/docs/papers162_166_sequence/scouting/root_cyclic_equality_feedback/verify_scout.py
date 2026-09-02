#!/usr/bin/env python3
"""Exact scout for cyclic q-ary equality feedback at dyadic lengths."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import product
from math import comb


ASSERTIONS = 0


def require(condition: bool, witness: object) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(witness)


def equality_step(word: tuple[int, ...]) -> tuple[int, ...]:
    n = len(word)
    return tuple(int(word[i] == word[(i + 1) % n]) for i in range(n))


def difference(mask: tuple[int, ...]) -> tuple[int, ...]:
    n = len(mask)
    return tuple(mask[i] ^ mask[(i + 1) % n] for i in range(n))


def power_difference(mask: tuple[int, ...], exponent: int) -> tuple[int, ...]:
    out = mask
    for _ in range(exponent):
        out = difference(out)
    return out


def change_mask(word: tuple[int, ...]) -> tuple[int, ...]:
    n = len(word)
    return tuple(int(word[i] != word[(i + 1) % n]) for i in range(n))


def closed(word: tuple[int, ...], t: int) -> tuple[int, ...]:
    if t == 0:
        return word
    c = power_difference(change_mask(word), t - 1)
    return tuple(1 ^ bit for bit in c)


def iterate(word: tuple[int, ...], t: int) -> tuple[int, ...]:
    out = word
    for _ in range(t):
        out = equality_step(out)
    return out


def nil_index(mask: tuple[int, ...]) -> int:
    zero = (0,) * len(mask)
    cur = mask
    for j in range(len(mask) + 1):
        if cur == zero:
            return j
        cur = difference(cur)
    raise AssertionError(("not nilpotent", mask))


def depth(word: tuple[int, ...]) -> int:
    one = (1,) * len(word)
    if word == one:
        return 0
    c = change_mask(word)
    if not any(c):
        return 1
    return 1 + nil_index(c)


def colourings_of_mask(mask: tuple[int, ...], q: int) -> int:
    r = sum(mask)
    return (q - 1) ** r + ((-1) ** r) * (q - 1)


def in_image_of_difference_power(mask: tuple[int, ...], j: int) -> bool:
    n = len(mask)
    j = min(j, n)
    return power_difference(mask, n - j) == (0,) * n


def predicted_fibre(target: tuple[int, ...], t: int, q: int) -> int:
    n = len(target)
    if t == 0:
        return 1
    if any(bit not in (0, 1) for bit in target):
        return 0
    d = tuple(bit ^ 1 for bit in target)
    j = min(t - 1, n)
    total = 0
    for mask in product((0, 1), repeat=n):
        if power_difference(mask, j) == d:
            total += colourings_of_mask(mask, q)
    return total


def exact_cdf(n: int, q: int, j: int) -> int:
    total = 0
    for mask in product((0, 1), repeat=n):
        if power_difference(mask, j) == (0,) * n:
            total += colourings_of_mask(mask, q)
    return total


def integrated_radius(d: tuple[int, ...]) -> int:
    """Weight, modulo complement, of the two solutions to D c=d."""
    require(sum(d) % 2 == 0, ("integrable target", d))
    current = 0
    weight = 0
    for bit in d:
        weight += current
        current ^= bit
    require(current == 0, ("cyclic integration closes", d))
    return min(weight, len(d) - weight)


def second_time_fibre(n: int, q: int, radius: int) -> int:
    a = q - 1
    return a ** radius + a ** (n - radius) + 2 * a * ((-1) ** radius)


def midpoint_fibre(n: int, q: int, half_weight: int) -> int:
    half = n // 2
    a = q - 1
    return ((1 + a * a) ** (half - half_weight)
            * (2 * a) ** half_weight
            + a * (2 ** half) * ((-1) ** half_weight))


def main() -> None:
    rows: list[str] = []
    total_words = 0
    boxes = [(4, 3), (4, 4), (4, 5), (4, 6), (8, 3), (8, 4)]

    for n, q in boxes:
        words = tuple(product(range(q), repeat=n))
        total_words += len(words)
        one = (1,) * n
        masks = tuple(product((0, 1), repeat=n))

        require((n & (n - 1)) == 0 and n >= 4, ("dyadic", n))
        for mask in masks:
            require(power_difference(mask, n) == (0,) * n,
                    ("D^n zero", n, mask))
            require(nil_index(mask) <= n, ("nil index", n, mask))
        for j in range(n + 1):
            kernel = sum(power_difference(mask, j) == (0,) * n for mask in masks)
            require(kernel == 2 ** j, ("kernel dimension", n, j, kernel))

        actual_depths: Counter[int] = Counter()
        mask_multiplicity: Counter[tuple[int, ...]] = Counter()
        for word in words:
            c = change_mask(word)
            mask_multiplicity[c] += 1
            d = depth(word)
            actual_depths[d] += 1
            require(iterate(word, d) == one, ("depth hits", n, q, word))
            if d:
                require(iterate(word, d - 1) != one, ("depth sharp", n, q, word))
            for t in range(n + 2):
                require(iterate(word, t) == closed(word, t),
                        ("closed iterate", n, q, t, word))

        for mask in masks:
            require(mask_multiplicity[mask] == colourings_of_mask(mask, q),
                    ("fixed change mask", n, q, mask,
                     mask_multiplicity[mask]))

        predicted_depths: Counter[int] = Counter({0: 1, 1: q - 1})
        previous = q
        for j in range(1, n + 1):
            current = exact_cdf(n, q, j)
            predicted_depths[j + 1] = current - previous
            previous = current
        require(actual_depths == predicted_depths,
                ("depth census", n, q, actual_depths, predicted_depths))

        for j in (1, 2, 4, 8):
            if j >= n:
                continue
            dyadic = (1 + (q - 1) ** (n // j)) ** j + (q - 1) * (2 ** j)
            require(exact_cdf(n, q, j) == dyadic,
                    ("dyadic CDF", n, q, j))

        last_layer = (
            (q ** n - (q - 2) ** n) // 2
            - (q - 1) * 2 ** (n - 1)
        )
        require(actual_depths[n + 1] == last_layer,
                ("sharp last layer", n, q, actual_depths[n + 1], last_layer))
        require(last_layer > 0, ("sharp witness exists", n, q))

        image_sizes: list[int] = []
        max_fibre = 0
        recorded_fibres: dict[int, Counter[tuple[int, ...]]] = {}
        for t in range(n + 2):
            fibres: Counter[tuple[int, ...]] = Counter(iterate(word, t) for word in words)
            recorded_fibres[t] = fibres
            image_sizes.append(len(fibres))
            if t == 0:
                require(len(fibres) == q ** n and set(fibres.values()) == {1},
                        ("identity image", n, q))
                continue
            if t == 1:
                require(len(fibres) == 2 ** n - n, ("first image", n, q))
            else:
                j = min(t - 1, n)
                require(len(fibres) == 2 ** (n - j),
                        ("positive image", n, q, t, len(fibres)))
            for target in product(range(q), repeat=n):
                predicted = predicted_fibre(target, t, q)
                observed = fibres[target]
                require(observed == predicted,
                        ("every target fibre", n, q, t, target,
                         observed, predicted))
                if observed:
                    dmask = tuple((bit ^ 1) for bit in target)
                    if t == 1:
                        require(sum(dmask) != 1, ("first support hole", target))
                    else:
                        require(in_image_of_difference_power(dmask, t - 1),
                                ("linear image support", n, q, t, target))
                    max_fibre = max(max_fibre, observed)

        # Complete target-sensitive fibre spectrum at t=2.  The two
        # solutions of D c=d are complements.
        second_class: Counter[int] = Counter()
        for target, value in recorded_fibres[2].items():
            dmask = tuple(bit ^ 1 for bit in target)
            radius = integrated_radius(dmask)
            expected = second_time_fibre(n, q, radius)
            require(value == expected, ("second spectrum value", n, q, target))
            second_class[radius] += 1
        for radius in range(n // 2 + 1):
            multiplicity = (comb(n, radius) if radius < n // 2
                            else comb(n, radius) // 2)
            require(second_class[radius] == multiplicity,
                    ("second spectrum multiplicity", n, q, radius,
                     second_class[radius], multiplicity))
        require(sum(second_class.values()) == 2 ** (n - 1),
                ("second spectrum mass", n, q))

        # At j=n/2, D^j=I+S^(n/2).  Feasible deviations are duplicated
        # half-words, and each pair contributes either 1+a^2 or 2a.
        midpoint_time = n // 2 + 1
        midpoint_class: Counter[int] = Counter()
        for target, value in recorded_fibres[midpoint_time].items():
            dmask = tuple(bit ^ 1 for bit in target)
            half = dmask[: n // 2]
            require(dmask[n // 2 :] == half,
                    ("midpoint duplicated support", n, q, target))
            half_weight = sum(half)
            expected = midpoint_fibre(n, q, half_weight)
            require(value == expected,
                    ("midpoint spectrum value", n, q, target, value, expected))
            midpoint_class[half_weight] += 1
        for half_weight in range(n // 2 + 1):
            require(midpoint_class[half_weight] == comb(n // 2, half_weight),
                    ("midpoint spectrum multiplicity", n, q, half_weight))
        require(sum(midpoint_class.values()) == 2 ** (n // 2),
                ("midpoint spectrum mass", n, q))

        require(predicted_fibre(one, 1, q) == q,
                ("alphabet recovery", n, q))
        rows.append(
            f"n={n},q={q}|states={q**n}|height={max(actual_depths)}|"
            f"last={actual_depths[n+1]}|"
            f"images={','.join(map(str,image_sizes))}|max_fibre={max_fibre}"
        )

    print("CYCLIC_EQUALITY_FEEDBACK_SCOUT_V2")
    print(f"boxes={len(boxes)} words={total_words}")
    for row in rows:
        print(row)
    print(f"assertions={ASSERTIONS}")
    print("REPAIR complete_t2_and_midpoint_target_fibre_spectra")
    print("DECISION GREEN_REENTRY_PENDING_INDEPENDENT_HOSTILE_GATE")
    print("EXTERNAL HOLD_EXTERNAL")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
