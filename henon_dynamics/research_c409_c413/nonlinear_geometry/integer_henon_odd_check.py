"""Exact finite certificate for the b=1 integral Hénon branch.

The all-parameter proof is in ADDENDUM_INTEGER_HENON_ODD.md; finite
parameter screens, if requested, are supplemental and are not that proof.
"""

from math import isqrt

from integer_henon_check import canonical, points_from_words, prune


EXPECTED_SIZES = {
    0: [16, 8, 5, 3, 2],
    -1: [16, 12, 9, 8, 7, 6, 5, 4],
    -2: [36, 22, 17, 13, 10, 8, 7, 6, 5],
    -3: [36, 24, 17, 14, 12, 10, 8, 6, 5, 4],
    -4: [36, 22, 14, 8],
    -5: [36, 20, 12, 8, 5, 2, 1, 0],
    -6: [64, 32, 18, 11, 8, 5, 4],
    -7: [64, 32, 18, 14, 10, 8, 6, 4],
    -8: [64, 28, 14, 7, 6],
    -9: [64, 24, 10, 4, 2, 0],
    -10: [36, 6, 2],
    -11: [36, 8, 2, 0],
    -12: [64, 22, 10, 4, 2],
    -13: [36, 20, 14, 12, 10, 8, 6, 4],
    -14: [36, 20, 12, 6],
    -15: [36, 12, 6, 4, 2, 0],
    -16: [36, 4, 2],
}

EXPECTED_WORDS = {
    0: [(0,), (1,)],
    -1: [(-1, -1, 0, 0)],
    -2: [(-1,), (2,), (-2, 0, 0)],
    -3: [(-2, -2, 1, 1)],
    -4: [(-2, -1), (-3, 1, 1), (-2, -2, 0)],
    -5: [],
    -6: [(-2,), (3,), (-3, 0)],
    -7: [(-3, -3, 2, 2)],
    -8: [(-4, 2, 2), (-3, -3, 1)],
    -9: [],
    -10: [(-4, 1)],
    -11: [],
    -12: [(-3,), (4,)],
    -13: [(-4, -4, 3, 3)],
    -14: [(-5, 3, 3), (-4, -4, 2)],
    -15: [],
    -16: [(-5, 2)],
}


def initial_vertices(parameter):
    if parameter > 0:
        return set()
    bound = 2 + isqrt(1-4*parameter)
    symbols = [z for z in range(-bound, bound+1)
               if z % 2 and abs(z*z+4*parameter+3) <= 4*bound]
    return {(x, y) for x in symbols for y in symbols}


def successor(pair, parameter):
    x, y = pair
    numerator = y*y+4*parameter+3
    assert numerator % 2 == 0
    return (y, numerator//2-x)


def path_cycles(parameter):
    vertices = initial_vertices(parameter)
    visited = set()
    words = set()
    for initial in sorted(vertices):
        current = initial
        path = []
        path_index = {}
        while current in vertices and current not in visited and current not in path_index:
            path_index[current] = len(path)
            path.append(current)
            current = successor(current, parameter)
        if current in path_index:
            words.add(canonical((p[0]-1)//2 for p in path[path_index[current]:]))
        visited.update(path)
    return sorted(words, key=lambda w: (len(w), w))


def pronic_index(value):
    if value < 0:
        return None
    root = isqrt(1+4*value)
    if root*root != 1+4*value or root % 2 != 1:
        return None
    return (root-1)//2


def predicted_cycles(parameter):
    words = set()
    k = pronic_index(-parameter)
    if k is not None:
        words.update([(-k,), (k+1,)])
    k = pronic_index(-parameter-4)
    if k is not None:
        words.add(canonical((-k-2, k-1)))
    k = pronic_index(-parameter-2)
    if k is not None:
        words.add(canonical((-k-2, k, k)))
        if k >= 1:
            words.add(canonical((k-1, -k-1, -k-1)))
    k = pronic_index(-parameter-1)
    if k is not None:
        words.add(canonical((-k-1, -k-1, k, k)))
    return sorted(words, key=lambda w: (len(w), w))


def verify_certificate():
    for parameter in range(0, -17, -1):
        core, sizes = prune(initial_vertices(parameter), lambda p: successor(p, parameter))
        actual_integer_points = {((x-1)//2, (y-1)//2) for x, y in core}
        assert sizes == EXPECTED_SIZES[parameter], (parameter, sizes)
        assert actual_integer_points == points_from_words(EXPECTED_WORDS[parameter])
        assert path_cycles(parameter) == EXPECTED_WORDS[parameter]
        assert predicted_cycles(parameter) == EXPECTED_WORDS[parameter]
        print("A =", parameter, "sizes =", sizes, "cycles =", EXPECTED_WORDS[parameter])


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--screen-minimum", type=int)
    args = parser.parse_args()
    verify_certificate()
    print("All 17 exact small-parameter certificates PASS.")
    if args.screen_minimum is not None:
        for parameter in range(args.screen_minimum, 2):
            assert path_cycles(parameter) == predicted_cycles(parameter), parameter
        print("Supplemental finite formula screen:", args.screen_minimum,
              "through 1 PASS; not the all-parameter proof.")
