#!/usr/bin/env python3
"""Independent odd-branch finite complement in original integer coordinates.

Uses full bounding rectangles and Boolean transitive closure, not the
author's doubled-coordinate filtering/pruning or expected output tables.
"""

from math import isqrt
from root_integer_henon_check import canonical


def check(parameter):
    doubled_bound = 2 + isqrt(1 - 4 * parameter)
    lower = (-doubled_bound) // 2
    upper = (doubled_bound - 1) // 2
    vertices = [(x, y) for x in range(lower, upper + 1)
                for y in range(lower, upper + 1)]
    position = {point: j for j, point in enumerate(vertices)}
    reach = [0] * len(vertices)
    for j, (x, y) in enumerate(vertices):
        target = position.get((y, y * y + y + parameter - x))
        if target is not None:
            reach[j] = 1 << target
    for k in range(len(vertices)):
        for j in range(len(vertices)):
            if reach[j] & (1 << k):
                reach[j] |= reach[k]
    actual = {point for j, point in enumerate(vertices)
              if reach[j] & (1 << j)}
    expected_words = set()
    for k in range(isqrt(-parameter + 4) + 2):
        pronic = k * (k + 1)
        if parameter == -pronic:
            expected_words.update({(-k,), (k + 1,)})
        if parameter == -pronic - 4:
            expected_words.add(canonical((-k - 2, k - 1)))
        if parameter == -pronic - 2:
            expected_words.add(canonical((-k - 2, k, k)))
            if k >= 1:
                expected_words.add(canonical((k - 1, -k - 1, -k - 1)))
        if parameter == -pronic - 1:
            expected_words.add(canonical((-k - 1, -k - 1, k, k)))
    expected_points = {(word[j], word[(j + 1) % len(word)])
                       for word in expected_words for j in range(len(word))}
    assert actual == expected_points, (parameter, actual, expected_points)
    print(f"A={parameter}: full_rectangle={len(vertices)} "
          f"periodic={len(actual)} words={sorted(expected_words)}")


if __name__ == "__main__":
    for parameter in range(0, -17, -1):
        check(parameter)
    print("PASS: all 17 odd-branch finite complements, exact full vertex sets")
