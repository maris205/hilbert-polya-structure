#!/usr/bin/env python3
"""Independent finite-complement check; no author module or data is imported.

For c=0,...,12 reconstruct the entire proved bounding square, not the
author's filtered vertex set. Boolean transitive closure identifies every
vertex with a nonempty return path. No period cutoff is used.
"""

from math import isqrt


def canonical(word):
    return min(word[j:] + word[:j] for j in range(len(word)))


def check(c):
    bound = 1 + isqrt(c + 1)
    vertices = [(x, y) for x in range(-bound, bound + 1)
                for y in range(-bound, bound + 1)]
    position = {point: j for j, point in enumerate(vertices)}
    reach = [0] * len(vertices)
    for j, (x, y) in enumerate(vertices):
        target = position.get((y, y * y - c - x))
        if target is not None:
            reach[j] = 1 << target
    for k in range(len(vertices)):
        for j in range(len(vertices)):
            if reach[j] & (1 << k):
                reach[j] |= reach[k]
    actual = {point for j, point in enumerate(vertices)
              if reach[j] & (1 << j)}
    words = set()
    for start in actual:
        current = start
        word = []
        while True:
            x, y = current
            word.append(x)
            current = (y, y * y - c - x)
            assert current in actual
            if current == start:
                break
            assert len(word) <= len(actual)
        words.add(canonical(tuple(word)))
    expected = set()
    for k in range(isqrt(c + 3) + 2):
        if c == k * k - 1:
            expected.update({(1 - k,), (1 + k,)})
        if k >= 1 and c == k * k + 3:
            expected.add(canonical((-k - 1, k - 1)))
        if c == k * k + 1:
            expected.update({canonical((-k - 1, k, k)),
                             canonical((k - 1, -k, -k))})
        if k >= 1 and c == k * k:
            expected.add(canonical((-k, -k, k, k)))
    expected_points = {(word[j], word[(j + 1) % len(word)])
                       for word in expected for j in range(len(word))}
    assert words == expected, (c, words, expected)
    assert actual == expected_points, (c, actual, expected_points)
    print(f"c={c}: full_square={len(vertices)} periodic={len(actual)} "
          f"words={sorted(words)}")


if __name__ == "__main__":
    for parameter in range(13):
        check(parameter)
    print("PASS: all 13 finite complements, exact full vertex sets")
