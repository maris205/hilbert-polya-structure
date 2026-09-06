"""Exact scout only: all integral cycles of H_a in a proven finite box.

No finite period cutoff is used. For a <= 1 a periodic coordinate satisfies
|x| <= floor(1 + sqrt(1-a)) and |x*x+a| <= 2R. Enumerating the partial
functional graph on the resulting S x S therefore exhausts all periods.
This script is not, by itself, a theorem for infinitely many parameters.
"""

from math import isqrt


SMALL_SIZES = {
    0: [25, 15, 10, 8, 7, 6, 5, 4, 3, 2],
    1: [25, 18, 14, 12, 10, 9, 8, 7],
    2: [25, 17, 12, 8, 7, 6],
    3: [49, 28, 18, 11, 8, 6, 4, 2],
    4: [49, 29, 18, 14, 12, 10, 8, 6],
    5: [49, 26, 16, 9, 8, 7, 6],
    6: [49, 23, 12, 6, 2, 0],
    7: [36, 12, 6, 3, 2],
    8: [81, 33, 14, 6, 2],
    9: [64, 30, 14, 12, 10, 8, 6, 4],
    10: [36, 20, 12, 6],
    11: [36, 12, 6, 4, 2, 0],
    12: [36, 4, 2],
}

SMALL_WORDS = {
    0: [(0,), (2,)],
    1: [(-1, 0, 0), (-1, -1, 1, 1)],
    2: [(-2, 1, 1), (-1, -1, 0)],
    3: [(-1,), (3,)],
    4: [(-2, 0), (-2, -2, 2, 2)],
    5: [(-3, 2, 2), (-2, -2, 1)],
    6: [],
    7: [(-3, 1)],
    8: [(-2,), (4,)],
    9: [(-3, -3, 3, 3)],
    10: [(-4, 3, 3), (-3, -3, 2)],
    11: [],
    12: [(-4, 2)],
}


def canonical(word):
    word = tuple(word)
    return min(word[i:] + word[:i] for i in range(len(word)))


def cycles(a):
    if a > 1:
        return []
    radius = 1 + isqrt(1 - a)
    symbols = [x for x in range(-radius, radius + 1) if abs(x*x+a) <= 2*radius]
    states = {(x, y) for x in symbols for y in symbols}
    found = set()
    visited = set()
    for initial in sorted(states):
        current = initial
        path = []
        path_index = {}
        while current in states and current not in visited and current not in path_index:
            path_index[current] = len(path)
            path.append(current)
            x, y = current
            current = (y, y*y+a-x)
        if current in path_index:
            found.add(canonical(p[0] for p in path[path_index[current]:]))
        visited.update(path)
    return sorted(found, key=lambda w: (len(w), w))


def points_from_words(words):
    return {(word[i], word[(i+1) % len(word)])
            for word in words for i in range(len(word))}


def square_root_or_none(value):
    if value < 0:
        return None
    root = isqrt(value)
    return root if root*root == value else None


def predicted_cycles(a):
    """The theorem's asserted families, independently of graph enumeration."""
    words = set()
    root = square_root_or_none(1-a)
    if root is not None:
        words.update([(1-root,), (1+root,)])
    root = square_root_or_none(-a-3)
    if root is not None and root >= 1:
        words.add(canonical((-root-1, root-1)))
    root = square_root_or_none(-a-1)
    if root is not None:
        words.add(canonical((-root-1, root, root)))
        words.add(canonical((root-1, -root, -root)))
    root = square_root_or_none(-a)
    if root is not None and root >= 1:
        words.add(canonical((-root, -root, root, root)))
    return sorted(words, key=lambda w: (len(w), w))


def prune(vertices, successor):
    sizes = [len(vertices)]
    while True:
        new_vertices = {p for p in vertices if successor(p) in vertices}
        if new_vertices == vertices:
            return vertices, sizes
        vertices = new_vertices
        sizes.append(len(vertices))


def verify_small_certificate():
    for c in range(13):
        radius = 1 + isqrt(1+c)
        symbols = [x for x in range(-radius, radius+1) if abs(x*x-c) <= 2*radius]
        vertices = {(x, y) for x in symbols for y in symbols}
        core, sizes = prune(vertices, lambda p: (p[1], p[1]*p[1]-c-p[0]))
        assert sizes == SMALL_SIZES[c], (c, sizes)
        assert core == points_from_words(SMALL_WORDS[c]), (c, core)
        assert cycles(-c) == SMALL_WORDS[c], (c, cycles(-c))
        assert predicted_cycles(-c) == SMALL_WORDS[c], (c, predicted_cycles(-c))
        print("small c =", c, "sizes =", sizes, "cycles =", SMALL_WORDS[c])


def verify_local_symbols():
    symbols = [(epsilon, delta) for epsilon in (-1, 1) for delta in (-1, 0, 1)]
    vertices = {(left, center) for left in symbols for center in symbols}
    for s in range(-2, 4):
        def successor(pair):
            (el, dl), (ec, dc) = pair
            return ((ec, dc), (2*ec*dc-el, dc*dc-s-dl))
        core, sizes = prune(vertices, successor)
        # Any fixed r >= 4 embeds the six formal symbols injectively in Z.
        # This is a finite check of the local classification, not of the
        # infinite-parameter reduction in the proof.
        actual_pairs = {(17*el+dl, 17*ec+dc) for (el, dl), (ec, dc) in core}
        expected_pairs = points_from_words(predicted_cycles(-17*17-s))
        assert actual_pairs == expected_pairs, (s, actual_pairs, expected_pairs)
        print("symbol s =", s, "sizes =", sizes, "periodic vertices =", len(core))


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--minimum", type=int, default=-100)
    parser.add_argument("--maximum", type=int, default=2)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if args.verify:
        verify_small_certificate()
        verify_local_symbols()
        for parameter in range(args.minimum, args.maximum+1):
            assert cycles(parameter) == predicted_cycles(parameter), parameter
        print("Supplemental finite-parameter formula check:", args.minimum,
              "through", args.maximum, "PASS; not the all-parameter proof.")
        raise SystemExit(0)
    for parameter in range(args.minimum, args.maximum + 1):
        output = cycles(parameter)
        if output:
            print(parameter, output)
