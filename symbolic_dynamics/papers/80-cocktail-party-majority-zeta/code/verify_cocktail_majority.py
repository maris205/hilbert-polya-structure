#!/usr/bin/env python3
"""Exhaust the literal majority rule on cocktail-party graphs.

Vertices are consecutive deleted-matching pairs.  Exact theorem formulas are
checked for every state through n=8 and for the first twelve iterate counts.
"""

from math import comb


def bit(state, vertex):
    return (state >> vertex) & 1


def update(state, n):
    """One synchronous strict-majority step, with inertia on a tie."""

    out = 0
    degree = 2 * n - 2
    for vertex in range(2 * n):
        mate = vertex ^ 1
        neighbor_ones = sum(
            bit(state, other)
            for other in range(2 * n)
            if other not in (vertex, mate)
        )
        old = bit(state, vertex)
        if 2 * neighbor_ones > degree:
            new = 1
        elif 2 * neighbor_ones < degree:
            new = 0
        else:
            new = old
        out |= new << vertex
    return out


def is_pairwise_mixed(state, n):
    return all(bit(state, 2 * pair) != bit(state, 2 * pair + 1) for pair in range(n))


def audit(n):
    size = 1 << (2 * n)
    zero = 0
    one = size - 1
    images = [update(state, n) for state in range(size)]
    fixed = []
    two_periodic = []
    basin_zero = []
    basin_one = []

    for state in range(size):
        image = images[state]
        second = images[image]
        assert images[second] == image

        weight = state.bit_count()
        if weight < n:
            assert image == zero
            basin_zero.append(state)
        elif weight > n:
            assert image == one
            basin_one.append(state)
        else:
            for pair in range(n):
                left = bit(state, 2 * pair)
                right = bit(state, 2 * pair + 1)
                expected = (left, right) if left != right else (1 - left, 1 - right)
                assert (bit(image, 2 * pair), bit(image, 2 * pair + 1)) == expected
            assert second == state

        if image == state:
            fixed.append(state)
        elif second == state:
            two_periodic.append(state)

    expected_fixed = 2 + 2**n
    expected_two_points = comb(2 * n, n) - 2**n
    expected_basin = (4**n - comb(2 * n, n)) // 2
    assert len(fixed) == expected_fixed
    assert len(two_periodic) == expected_two_points
    assert len(basin_zero) == expected_basin
    assert len(basin_one) == expected_basin
    assert sum(is_pairwise_mixed(state, n) for state in fixed) == 2**n

    for exponent in range(1, 13):
        current = list(range(size))
        for _ in range(exponent):
            current = [images[state] for state in current]
        actual = sum(image == state for state, image in enumerate(current))
        expected = expected_fixed if exponent % 2 else 2 + comb(2 * n, n)
        assert actual == expected

    return expected_fixed, expected_two_points // 2, expected_basin


def main():
    rows = [(n, *audit(n)) for n in range(1, 9)]
    print("PASS exhaustive local-update/state-partition checks: n=1,...,8")
    print("PASS Artin--Mazur fixed-count checks: k=1,...,12")
    print("rows (n, fixed points, genuine 2-cycles, each consensus basin):")
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
