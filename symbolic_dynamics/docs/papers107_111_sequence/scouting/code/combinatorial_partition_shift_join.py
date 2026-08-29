#!/usr/bin/env python3
"""Exact spike for cyclic shift--join dynamics on the partition lattice."""

from collections import Counter
from math import gcd


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def partitions(n):
    if n == 0:
        yield ()
        return
    word = [0] * n

    def rec(index, maximum):
        if index == n:
            yield tuple(word)
            return
        for value in range(maximum + 2):
            word[index] = value
            yield from rec(index + 1, max(maximum, value))

    word[0] = 0
    yield from rec(1, 0)


def canonical(labels):
    rename = {}
    out = []
    for label in labels:
        if label not in rename:
            rename[label] = len(rename)
        out.append(rename[label])
    return tuple(out)


def rotate(partition, amount=1):
    n = len(partition)
    return canonical(tuple(partition[(i - amount) % n] for i in range(n)))


def join(left, right):
    n = len(left)
    parent = list(range(n))

    def root(vertex):
        while parent[vertex] != vertex:
            parent[vertex] = parent[parent[vertex]]
            vertex = parent[vertex]
        return vertex

    def union(a, b):
        a, b = root(a), root(b)
        if a != b:
            parent[b] = a

    for partition in (left, right):
        first = {}
        for vertex, label in enumerate(partition):
            if label in first:
                union(first[label], vertex)
            else:
                first[label] = vertex
    return canonical(tuple(root(i) for i in range(n)))


def update(partition):
    return join(partition, rotate(partition))


def orbit_join(partition, time):
    out = partition
    for shift in range(1, time + 1):
        out = join(out, rotate(partition, shift))
    return out


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def euler_phi(n):
    return sum(gcd(candidate, n) == 1 for candidate in range(1, n + 1))


def mobius(n):
    prime = 2
    sign = 1
    while prime * prime <= n:
        if n % prime == 0:
            n //= prime
            sign = -sign
            if n % prime == 0:
                return 0
            while n % prime == 0:
                n //= prime
        prime += 1
    return -sign if n > 1 else sign


def core_size(partition):
    n = len(partition)
    generator_gcd = n
    blocks = {}
    for vertex, label in enumerate(partition):
        blocks.setdefault(label, []).append(vertex)
    for block in blocks.values():
        base = block[0]
        for vertex in block[1:]:
            generator_gcd = gcd(generator_gcd, (vertex - base) % n)
    return n // generator_gcd


def core_partition(n, subgroup_size):
    index = n // subgroup_size
    return canonical(tuple(vertex % index for vertex in range(n)))


def is_primitive_chord_atom(partition):
    n = len(partition)
    blocks = {}
    for vertex, label in enumerate(partition):
        blocks.setdefault(label, []).append(vertex)
    nonsingletons = [block for block in blocks.values() if len(block) > 1]
    if len(nonsingletons) != 1 or len(nonsingletons[0]) != 2:
        return False
    left, right = nonsingletons[0]
    return gcd((right - left) % n, n) == 1


def bell_numbers(limit):
    bell = [0] * (limit + 1)
    bell[0] = 1
    for n in range(limit):
        # Bell recurrence B_(n+1)=sum_(k=0)^n binom(n,k)B_k.
        choose = 1
        total = 0
        for k in range(n + 1):
            total += choose * bell[k]
            choose = choose * (n - k) // (k + 1) if k < n else choose
        bell[n + 1] = total
    return bell


def exact_basin_formula(n, subgroup_size, bell):
    return sum(
        mobius(subgroup_size // d) * bell[d] ** (n // d)
        for d in divisors(subgroup_size)
    )


def lane(n, bell):
    depth_histogram = Counter()
    basins = Counter()
    fixed = 0
    total = 0
    expected_depth = max(0, n - 2)

    for partition in partitions(n):
        total += 1
        current = partition
        time = 0
        while update(current) != current:
            check(current == orbit_join(partition, time),
                  "iterate is not the consecutive orbit join")
            current = update(current)
            time += 1
            check(time <= n, "shift--join orbit did not stabilize")
        check(current == orbit_join(partition, time),
              "terminal iterate formula failed")
        subgroup_size = core_size(partition)
        check(current == core_partition(n, subgroup_size),
              "stable core is not the predicted cyclic coset partition")
        depth_histogram[time] += 1
        basins[subgroup_size] += 1
        fixed += time == 0
        if n >= 3:
            check(
                (time == expected_depth)
                == is_primitive_chord_atom(partition),
                "deepest state is not exactly a primitive-chord atom",
            )

    check(total == bell[n], "partition generator missed a Bell state")
    check(fixed == len(divisors(n)), "fixed partitions do not match divisors")
    check(max(depth_histogram) == expected_depth, "sharp depth failed")
    deepest = depth_histogram[expected_depth]
    expected_deepest = bell[n] if n <= 2 else n * euler_phi(n) // 2
    check(
        deepest == expected_deepest,
        "deepest shell is not the observed primitive-chord shell",
    )
    for subgroup_size in divisors(n):
        check(
            basins[subgroup_size]
            == exact_basin_formula(n, subgroup_size, bell),
            "Möbius--Bell basin formula failed",
        )
    check(sum(basins.values()) == bell[n], "basins do not partition phase")

    return {
        "n": n,
        "bell": bell[n],
        "fixed": fixed,
        "max_depth": max(depth_histogram),
        "deepest": deepest,
        "depths": dict(sorted(depth_histogram.items())),
        "basins": dict(sorted(basins.items())),
    }


def main():
    bell = bell_numbers(9)
    rows = [lane(n, bell) for n in range(1, 10)]
    print("cyclic partition shift--join exact spike: PASS")
    print(f"assertions={ASSERTIONS}")
    for row in rows:
        print(
            "lane"
            f" n={row['n']} Bell={row['bell']} fixed={row['fixed']}"
            f" max_depth={row['max_depth']} deepest={row['deepest']}"
            f" depths={row['depths']}"
            f" basins={row['basins']}"
        )


if __name__ == "__main__":
    main()
