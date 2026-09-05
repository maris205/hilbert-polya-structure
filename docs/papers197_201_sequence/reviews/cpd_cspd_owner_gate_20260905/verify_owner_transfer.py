#!/usr/bin/env python3
"""Independent controls for the site-displacement owner transfer.

Enumerates free-site parking using lists, not the scout's occupancy code.
No author code imported. Entire translated source sets are compared with
the classical site-normalization equivalence classes.
"""
from collections import Counter, defaultdict
from itertools import product
from math import factorial

CHECKS = 0


def check(test, label):
    global CHECKS
    CHECKS += 1
    if not test:
        raise AssertionError(label)


def park(preferences):
    n = len(preferences)
    free = list(range(n))
    at_site = [None] * n
    displacement = [None] * n
    car_displacement = []
    wrapped = False
    for choice in preferences:
        eligible = [site for site in free if site >= choice]
        site = eligible[0] if eligible else free[0]
        free.remove(site)
        wrapped |= site < choice
        at_site[site] = choice
        displacement[site] = (site - choice) % n
        car_displacement.append((site - choice) % n)
    return tuple(displacement), tuple(at_site), wrapped, tuple(car_displacement)


def core(y):
    return all(value <= i for i, value in enumerate(y))


def rotated(y, cut):
    return y[cut:] + y[:cut]


def predecessor_poset(y):
    n = len(y)
    parents = [0] * n
    for site, distance in enumerate(y):
        for backward in range(1, distance + 1):
            parents[site] |= 1 << ((site - backward) % n)
    for pivot in range(n):
        for vertex in range(n):
            if parents[vertex] & (1 << pivot):
                parents[vertex] |= parents[pivot]
    if any(parents[v] & (1 << v) for v in range(n)):
        return 0, False
    ways = [0] * (1 << n)
    ways[0] = 1
    for chosen in range(1 << n):
        if ways[chosen]:
            for v in range(n):
                if not chosen & (1 << v) and not parents[v] & ~chosen:
                    ways[chosen | (1 << v)] += ways[chosen]
    hooks = 1
    for v in range(n):
        hooks *= parents[v].bit_count() + 1
        successors = [j for j in range(n) if parents[j] & (1 << v)]
        covers = [j for j in successors if not any(
            k != j and parents[j] & (1 << k) for k in successors
        )]
        check(len(covers) <= 1, "target poset Hasse forest")
    check(factorial(n) % hooks == 0, "integral forest hook count")
    check(ways[-1] == factorial(n) // hooks, "generic forest hook transfer")
    return ways[-1], True


def rank(n):
    buckets = defaultdict(set)
    normalization = defaultdict(set)
    depths = Counter()
    car_fibres = Counter()
    for a in product(range(n), repeat=n):
        y, normalized, wrapped, car_d = park(a)
        buckets[y].add(a)
        car_fibres[car_d] += 1
        if not wrapped:
            normalization[normalized].add(a)
        check(core(y) == (not wrapped), "intermediate class is classical PF")
        sy = park(y)[0]
        check(core(sy), "all outputs enter core after next epoch")
        if core(a):
            check(y == tuple(i - v for i, v in enumerate(a)), "complement on core")
        depths[0 if core(a) else (1 if not wrapped else 2)] += 1
    expected_image = set()
    for inv in product(*(range(i + 1) for i in range(n))):
        for cut in range(n):
            expected_image.add(rotated(inv, cut))
    check(set(buckets) == expected_image, "full image is rotations of inversion box")
    for y, sources in buckets.items():
        cut = next(k for k in range(n) if core(rotated(y, k)))
        yy = rotated(y, cut)
        translated = {tuple((v - cut) % n for v in a) for a in sources}
        classical_target = tuple(i - v for i, v in enumerate(yy))
        check(translated == normalization[classical_target], "entire circular fibre is an owned classical normalization class")
        count, acyclic = predecessor_poset(y)
        check(acyclic and count == len(sources), "complete target poset fibre")
    max_fibre = max(map(len, buckets.values()))
    check(max_fibre == factorial(n), "site-fibre maximum")
    check([y for y in buckets if len(buckets[y]) == max_fibre] == [(0,) * n], "unique site maximizer")
    check(depths[0] == factorial(n), "core count")
    check(depths[1] == (n + 1) ** (n - 1) - factorial(n), "depth one")
    check(depths[2] == n ** n - (n + 1) ** (n - 1), "depth two")
    print(f"n={n} source_states={n**n} site_image={len(buckets)} classical_normalization_classes={len(normalization)} translated_fibre_sets={len(buckets)} depths={tuple(depths[i] for i in range(3))} max_fibre={max_fibre} car_displacement_image={len(car_fibres)}")


if __name__ == "__main__":
    print("CPD_CSPD_INDEPENDENT_OWNER_TRANSFER_CONTROL")
    for n in range(1, 7):
        rank(n)
    print(f"assertions={CHECKS}")
    print("PASS_TRANSFER_NOT_ORIGINALITY_CLEARANCE")
