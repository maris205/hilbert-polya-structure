#!/usr/bin/env python3
"""Exact pilot for parity support of exterior squares of cyclic characters."""

from collections import Counter
from itertools import combinations
import json
import math


class Checker:
    def __init__(self):
        self.assertions = 0

    def check(self, condition, message):
        self.assertions += 1
        if not condition:
            raise AssertionError(message)


def elements(mask, modulus):
    return [value for value in range(modulus) if (mask >> value) & 1]


def from_elements(values, modulus):
    mask = 0
    for value in values:
        mask |= 1 << (value % modulus)
    return mask


def update(mask, modulus):
    values = elements(mask, modulus)
    out = 0
    for i, left in enumerate(values):
        for right in values[i + 1 :]:
            out ^= 1 << ((left + right) % modulus)
    return out


def translate(mask, shift, modulus):
    return from_elements((value + shift for value in elements(mask, modulus)), modulus)


def affine_reflect(mask, center_sum, modulus):
    return from_elements((center_sum - value for value in elements(mask, modulus)), modulus)


def orbit_type(start, modulus):
    seen = {}
    current = start
    while current not in seen:
        seen[current] = len(seen)
        current = update(current, modulus)
    return seen[current], len(seen) - seen[current]


def full_graph_lane(checker):
    summaries = {}
    period_support = {}
    for modulus in range(1, 13):
        types = Counter()
        for mask in range(1 << modulus):
            image = update(mask, modulus)
            size = mask.bit_count()
            checker.check(
                image.bit_count() % 2 == (size * (size - 1) // 2) % 2,
                f"cardinality parity failed at m={modulus}",
            )
            preperiod, period = orbit_type(mask, modulus)
            checker.check(preperiod <= (1 << modulus), "orbit bound failed")
            types[(preperiod, period)] += 1
        checker.check(sum(types.values()) == (1 << modulus), "phase census failed")
        periods = sorted({period for (_preperiod, period) in types})
        period_support[str(modulus)] = periods
        summaries[str(modulus)] = {
            "states": 1 << modulus,
            "max_preperiod": max(preperiod for preperiod, _period in types),
            "periods": periods,
            "orbit_type_counts": {
                f"{preperiod}:{period}": count
                for (preperiod, period), count in sorted(types.items())
            },
        }

    checker.check(18 in period_support["9"], "period-18 witness disappeared")
    checker.check(30 in period_support["11"], "period-30 witness disappeared")
    return summaries


def equivariance_lane(checker):
    checked = 0
    for modulus in range(1, 10):
        for mask in range(1 << modulus):
            for shift in range(modulus):
                checker.check(
                    update(translate(mask, shift, modulus), modulus)
                    == translate(update(mask, modulus), 2 * shift, modulus),
                    f"translation-doubling cocycle failed at m={modulus}",
                )
                checked += 1
    return checked


def small_support_lane(checker):
    summaries = {}
    for modulus in range(3, 16):
        triple_count = 0
        for triple in combinations(range(modulus), 3):
            mask = from_elements(triple, modulus)
            sigma = sum(triple) % modulus
            image = update(mask, modulus)
            checker.check(
                image == affine_reflect(mask, sigma, modulus),
                f"three-support reflection failed at m={modulus}",
            )
            checker.check(
                update(image, modulus) == translate(mask, sigma, modulus),
                f"three-support second iterate failed at m={modulus}",
            )
            if math.gcd(3, modulus) == 1:
                centroid = pow(3, -1, modulus) * sigma % modulus
                centered = translate(mask, -centroid, modulus)
                next_sigma = sum(elements(image, modulus)) % modulus
                next_centroid = pow(3, -1, modulus) * next_sigma % modulus
                centered_image = translate(image, -next_centroid, modulus)
                checker.check(
                    centered_image == affine_reflect(centered, 0, modulus),
                    f"centroid-shape split failed at m={modulus}",
                )
            triple_count += 1

        for size in range(3):
            for support in combinations(range(modulus), size):
                mask = from_elements(support, modulus)
                if size == 0:
                    checker.check(update(mask, modulus) == 0, "empty state not fixed")
                elif size == 1:
                    checker.check(update(mask, modulus) == 0, "singleton did not die")
                else:
                    first = update(mask, modulus)
                    checker.check(first.bit_count() == 1, "pair did not become singleton")
                    checker.check(update(first, modulus) == 0, "pair did not die in two steps")
        summaries[str(modulus)] = {
            "three_supports": triple_count,
            "centroid_split": math.gcd(3, modulus) == 1,
        }
    return summaries


def main():
    checker = Checker()
    result = {
        "full_graphs": full_graph_lane(checker),
        "translation_equivariance_checks": equivariance_lane(checker),
        "small_supports": small_support_lane(checker),
    }
    result["assertions"] = checker.assertions
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
