#!/usr/bin/env python3
"""Exact spike for rotating the first Chen--Fox--Lyndon factor.

For a nonempty word w=l_1...l_r in nonincreasing CFL factorization, set
F(w)=l_2...l_r l_1 (and F(w)=w when r=1).  Equal factors may make the
concatenation unchanged.  The map stays in the cyclic-conjugacy class.
"""

from itertools import product
from math import gcd


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def cfl(word):
    """Duval's linear-time nonincreasing Lyndon factorization."""
    n = len(word)
    factors = []
    i = 0
    while i < n:
        j = i + 1
        k = i
        while j < n and word[k] <= word[j]:
            if word[k] < word[j]:
                k = i
            else:
                k += 1
            j += 1
        length = j - k
        while i <= k:
            factors.append(word[i : i + length])
            i += length
    return tuple(factors)


def rotations(word):
    if not word:
        return (word,)
    return tuple(word[i:] + word[:i] for i in range(len(word)))


def is_lyndon(word):
    return bool(word) and all(word < rotation for rotation in rotations(word)[1:])


def step(word):
    factors = cfl(word)
    if len(factors) <= 1:
        return word
    return sum(factors[1:] + factors[:1], ())


def orbit(word):
    seen = {}
    path = []
    x = word
    while x not in seen:
        seen[x] = len(path)
        path.append(x)
        x = step(x)
    return tuple(path), seen[x], len(path) - seen[x]


def phi(n):
    return sum(1 for a in range(1, n + 1) if gcd(a, n) == 1)


def necklace_count(q, n):
    if n == 0:
        return 1
    return sum(phi(d) * q ** (n // d) for d in range(1, n + 1) if n % d == 0) // n


def word_string(word):
    return "".join(str(x) for x in word)


def first_rotation_index(word, target):
    return next(i for i, rotation in enumerate(rotations(word)) if rotation == target)


def statistics(q, n):
    fixed = 0
    max_depth = 0
    depth_histogram = {}
    first_not_one_step = None
    first_factor_count_failure = None
    first_depth_not_rotation_index = None

    for word in product(range(q), repeat=n):
        factors = cfl(word)
        check(sum(factors, ()) == word, f"CFL reconstruction failed: {word}")
        check(all(is_lyndon(factor) for factor in factors), f"non-Lyndon factor: {word}, {factors}")
        check(
            all(factors[i] >= factors[i + 1] for i in range(len(factors) - 1)),
            f"CFL order failed: {word}, {factors}",
        )
        image = step(word)
        check(image in rotations(word), f"map left conjugacy class: {word}->{image}")
        check(image <= word, f"lexicographic descent failed: {word}->{image}")
        check((image == word) == (len(set(factors)) <= 1), f"fixed criterion failed: {word}, {factors}")

        path, mu, period = orbit(word)
        check(period == 1, f"nontrivial cycle: {word}, {path[mu:]}")
        endpoint = path[-1]
        minimum = min(rotations(word))
        check(endpoint == minimum, f"wrong conjugacy representative: {word}->{endpoint}, want {minimum}")
        depth = len(path) - 1
        max_depth = max(max_depth, depth)
        depth_histogram[depth] = depth_histogram.get(depth, 0) + 1
        fixed += depth == 0

        if depth > 1 and first_not_one_step is None:
            first_not_one_step = (word_string(word), depth, tuple(map(word_string, path)))
        guessed_depth = max(0, len(factors) - 1)
        if depth > 0 and depth != guessed_depth and first_factor_count_failure is None:
            first_factor_count_failure = (
                word_string(word),
                tuple(map(word_string, factors)),
                guessed_depth,
                depth,
            )
        rotation_index = first_rotation_index(word, minimum)
        if depth != rotation_index and first_depth_not_rotation_index is None:
            first_depth_not_rotation_index = (
                word_string(word),
                rotation_index,
                depth,
            )

    expected_fixed = necklace_count(q, n)
    check(fixed == expected_fixed, f"necklace fixed count failed at q={q}, n={n}: {fixed}!={expected_fixed}")
    return {
        "q": q,
        "n": n,
        "states": q**n,
        "fixed": fixed,
        "max_depth": max_depth,
        "depth_histogram": dict(sorted(depth_histogram.items())),
        "first_not_one_step": first_not_one_step,
        "first_factor_count_failure": first_factor_count_failure,
        "first_depth_not_rotation_index": first_depth_not_rotation_index,
    }


def main():
    stats = []
    for q, max_n in ((2, 12), (3, 9)):
        for n in range(1, max_n + 1):
            stats.append(statistics(q, n))

    print("CFL FIRST-FACTOR ROTATION")
    for data in stats:
        print(
            "q={q} n={n} states={states} fixed={fixed} max_depth={max_depth} "
            "depth_histogram={depth_histogram}".format(**data)
        )

    first_not_one_step = next(
        (data["q"], data["n"], data["first_not_one_step"])
        for data in stats
        if data["first_not_one_step"] is not None
    )
    first_factor_failure = next(
        (data["q"], data["n"], data["first_factor_count_failure"])
        for data in stats
        if data["first_factor_count_failure"] is not None
    )
    first_rotation_failure = next(
        (data["q"], data["n"], data["first_depth_not_rotation_index"])
        for data in stats
        if data["first_depth_not_rotation_index"] is not None
    )
    first_depth_over_n_minus_one = next(
        ((data["q"], data["n"], data["max_depth"]) for data in stats if data["max_depth"] > data["n"] - 1),
        None,
    )
    print(f"first_not_one_step={first_not_one_step}")
    print(f"first_depth_not_factor_count_minus_one={first_factor_failure}")
    print(f"first_depth_not_min_rotation_index={first_rotation_failure}")
    print(f"first_depth_over_n_minus_one={first_depth_over_n_minus_one}")
    print(f"assertions={ASSERTIONS}")


if __name__ == "__main__":
    main()
