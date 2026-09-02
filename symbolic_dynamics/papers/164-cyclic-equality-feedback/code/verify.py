#!/usr/bin/env python3
"""Paper-local exact controls for cyclic equality feedback."""

from collections import Counter, defaultdict
from itertools import product
from math import comb


class Audit:
    def __init__(self):
        self.n = 0

    def check(self, ok, label):
        self.n += 1
        if not ok:
            raise AssertionError(label)


A = Audit()


def diff(c):
    n = len(c)
    return tuple(c[i] ^ c[(i + 1) % n] for i in range(n))


def power_diff(c, j):
    for _ in range(j):
        c = diff(c)
    return c


def change(w):
    n = len(w)
    return tuple(int(w[i] != w[(i + 1) % n]) for i in range(n))


def step(w):
    n = len(w)
    return tuple(int(w[i] == w[(i + 1) % n]) for i in range(n))


def chi(q, c):
    r = sum(c)
    return (q - 1) ** r + (-1) ** r * (q - 1)


def predicted(w, t):
    if t == 0:
        return w
    c = power_diff(change(w), t - 1)
    return tuple(1 ^ x for x in c)


def affine_fibre(n, q, j, y):
    d = tuple(1 ^ x for x in y)
    return sum(
        chi(q, c)
        for c in product((0, 1), repeat=n)
        if power_diff(c, j) == d
    )


def literal_box(n, q):
    words = list(product(range(q), repeat=n))
    masks = list(product((0, 1), repeat=n))
    mask_counts = Counter(change(w) for w in words)
    depths = Counter()
    images = []
    fibre_max = 0

    for c in masks:
        A.check(mask_counts[c] == chi(q, c), (n, q, c, "chi"))

    for w in words:
        x = w
        path = [x]
        for t in range(1, n + 3):
            x = step(x)
            path.append(x)
            A.check(x == predicted(w, t), (n, q, w, t, "iterate"))
        A.check(path[n + 1] == (1,) * n, (n, q, w, "absorption"))
        depth = next(t for t, x in enumerate(path) if x == (1,) * n)
        depths[depth] += 1
        if w != (1,) * n:
            A.check(path[depth - 1] != (1,) * n, (n, q, w, "minimal"))

    for t in range(1, n + 2):
        fibres = Counter(predicted(w, t) for w in words)
        images.append(len(fibres))
        j = min(t - 1, n)
        for y in masks:
            expected = affine_fibre(n, q, j, y)
            A.check(fibres[y] == expected, (n, q, t, y, "fibre"))
            fibre_max = max(fibre_max, fibres[y])
        A.check(sum(fibres.values()) == q**n, (n, q, t, "mass"))

    expected_images = [2**n - n] + [2 ** (n - j) for j in range(1, n + 1)]
    A.check(images == expected_images, (n, q, "images", images))
    last = (q**n - (q - 2) ** n) // 2 - (q - 1) * 2 ** (n - 1)
    A.check(depths[n + 1] == last, (n, q, "last", depths[n + 1], last))
    A.check(max(depths) == n + 1, (n, q, "height"))
    return len(words), last, images, fibre_max


def special_spectra():
    targets = 0
    for n in (4, 8, 16):
        masks = list(product((0, 1), repeat=n))
        half = n // 2
        for q in (3, 4, 5, 7):
            by_d_t2 = defaultdict(int)
            by_d_mid = defaultdict(int)
            solutions_t2 = defaultdict(list)
            for c in masks:
                weight = chi(q, c)
                dc = diff(c)
                by_d_t2[dc] += weight
                solutions_t2[dc].append(c)
                by_d_mid[power_diff(c, half)] += weight

            classes2 = Counter()
            values2 = Counter()
            for d, actual in by_d_t2.items():
                solutions = solutions_t2[d]
                A.check(len(solutions) == 2, (n, q, d, "pair"))
                rho = min(sum(solutions[0]), n - sum(solutions[0]))
                expected = ((q - 1) ** rho + (q - 1) ** (n - rho)
                            + 2 * (q - 1) * (-1) ** rho)
                A.check(actual == expected, (n, q, d, "t2"))
                classes2[rho] += 1
                values2[actual] += 1
                targets += 1
            for r in range(half + 1):
                expected_class = comb(n, r) if r < half else comb(n, half) // 2
                A.check(classes2[r] == expected_class, (n, q, r, "class2"))
            A.check(sum(v * values2[v] for v in values2) == q**n,
                    (n, q, "mass2"))

            classes_mid = Counter()
            values_mid = Counter()
            for d, actual in by_d_mid.items():
                A.check(d[:half] == d[half:], (n, q, d, "duplicated"))
                h = sum(d[:half])
                expected = ((1 + (q - 1) ** 2) ** (half - h)
                            * (2 * (q - 1)) ** h
                            + (q - 1) * 2**half * (-1) ** h)
                A.check(actual == expected, (n, q, d, "mid"))
                classes_mid[h] += 1
                values_mid[actual] += 1
                targets += 1
            for h in range(half + 1):
                A.check(classes_mid[h] == comb(half, h), (n, q, h, "classmid"))
            A.check(sum(v * values_mid[v] for v in values_mid) == q**n,
                    (n, q, "massmid"))

            if n == 4 and q == 4:
                A.check(len(values2) < len(classes2), "time-two collision sentinel")
                A.check(len(values_mid) < len(classes_mid), "midpoint collision sentinel")
    return targets


def boundaries():
    # q=2 fails the first-image formula; n=2 fails the later support repair.
    words = list(product(range(2), repeat=4))
    A.check(len({step(w) for w in words}) != 2**4 - 4, "q=2 support")
    words = list(product(range(3), repeat=2))
    A.check(len({step(step(w)) for w in words}) != 2 ** (2 - 1),
            "n=2 time-two support")
    c = (1, 0, 0, 0, 0, 0)
    A.check(power_diff(c, 6) != (0,) * 6, "nondyadic nonnilpotence")


def main():
    boxes = ((4, 3), (4, 4), (4, 5), (4, 6), (8, 3), (8, 4))
    print("CYCLIC_EQUALITY_FEEDBACK_PAPER_AUDIT_V1")
    total_words = 0
    for n, q in boxes:
        words, last, images, fibre_max = literal_box(n, q)
        total_words += words
        print(f"box n={n} q={q} words={words} last={last} "
              f"images={','.join(map(str, images))} max_fibre={fibre_max}")
    targets = special_spectra()
    boundaries()
    print(f"literal_words={total_words}")
    print(f"special_targets={targets}")
    print(f"assertions={A.n}")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
