#!/usr/bin/env python3
"""Exact deterministic controls for cyclic shift--join partition dynamics."""

from collections import Counter
from math import comb, gcd


ASSERTIONS = 0
PARTITIONS_ENUMERATED = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def partitions(n):
    """Generate every partition of [0,n) as a restricted-growth string."""
    word = [0] * n

    def rec(index, maximum):
        if index == n:
            yield tuple(word)
            return
        for value in range(maximum + 2):
            word[index] = value
            yield from rec(index + 1, max(maximum, value))

    if n == 0:
        yield ()
    else:
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
    """Partition join via union--find."""
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
    return canonical(tuple(root(vertex) for vertex in range(n)))


def update(partition):
    return join(partition, rotate(partition))


def orbit_join(partition, time):
    out = partition
    for shift in range(1, time + 1):
        out = join(out, rotate(partition, shift))
    return out


def translated_components(partition, time):
    """Independent graph-components realization of the consecutive joins."""
    n = len(partition)
    adjacency = [set() for _ in range(n)]
    blocks = {}
    for vertex, label in enumerate(partition):
        blocks.setdefault(label, []).append(vertex)
    for shift in range(time + 1):
        for block in blocks.values():
            shifted = [(vertex + shift) % n for vertex in block]
            for left_index, left in enumerate(shifted):
                for right in shifted[left_index + 1 :]:
                    adjacency[left].add(right)
                    adjacency[right].add(left)

    labels = [-1] * n
    component = 0
    for start in range(n):
        if labels[start] != -1:
            continue
        labels[start] = component
        stack = [start]
        while stack:
            vertex = stack.pop()
            for neighbor in adjacency[vertex]:
                if labels[neighbor] == -1:
                    labels[neighbor] = component
                    stack.append(neighbor)
        component += 1
    return canonical(tuple(labels))


def refines(fine, coarse):
    n = len(fine)
    return all(
        fine[left] != fine[right] or coarse[left] == coarse[right]
        for left in range(n)
        for right in range(n)
    )


def divisors(n):
    return [divisor for divisor in range(1, n + 1) if n % divisor == 0]


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


def bell_numbers(limit):
    bell = [0] * (limit + 1)
    bell[0] = 1
    for n in range(limit):
        choose = 1
        total = 0
        for k in range(n + 1):
            total += choose * bell[k]
            if k < n:
                choose = choose * (n - k) // (k + 1)
        bell[n + 1] = total
    return bell


def core_size(partition):
    n = len(partition)
    generated_gcd = n
    blocks = {}
    for vertex, label in enumerate(partition):
        blocks.setdefault(label, []).append(vertex)
    for block in blocks.values():
        base = block[0]
        for vertex in block[1:]:
            generated_gcd = gcd(generated_gcd, (vertex - base) % n)
    return n // generated_gcd


def core_partition(n, subgroup_size):
    index = n // subgroup_size
    return canonical(tuple(vertex % index for vertex in range(n)))


def exact_basin_formula(n, subgroup_size, bell):
    return sum(
        mobius(subgroup_size // divisor)
        * bell[divisor] ** (n // divisor)
        for divisor in divisors(subgroup_size)
    )


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


def binary_cut_lanes(limit=12):
    """Directly attack the two-defect and primitive-chord uniqueness lemma."""
    for n in range(3, limit + 1):
        for mask in range(1, (1 << n) - 1):
            bits = tuple((mask >> vertex) & 1 for vertex in range(n))
            admissible_primitive = []
            for left in range(n):
                for right in range(left + 1, n):
                    difference = (right - left) % n
                    admissible = all(
                        bits[(left + shift) % n]
                        == bits[(right + shift) % n]
                        for shift in range(n - 2)
                    )
                    if not admissible:
                        continue
                    defects = {
                        vertex
                        for vertex in range(n)
                        if bits[vertex]
                        != bits[(vertex + difference) % n]
                    }
                    if gcd(difference, n) > 1:
                        check(
                            not defects,
                            "an admissible nonprimitive chord had a cut defect",
                        )
                    else:
                        check(
                            defects == {(left - 2) % n, (left - 1) % n},
                            "a primitive chord did not have exactly two defects",
                        )
                        check(
                            all(
                                any(
                                    bits[vertex]
                                    != bits[(vertex + shift) % n]
                                    for vertex in range(n)
                                )
                                for shift in range(1, n)
                            ),
                            "primitive-chord cut had a nonzero stabilizer",
                        )
                        admissible_primitive.append((left, right))
            check(
                len(admissible_primitive) <= 1,
                "one binary cut admitted two distinct primitive chords",
            )


def lane(n, bell):
    global PARTITIONS_ENUMERATED
    depths = Counter()
    basins = Counter()
    fixed = 0
    expected_depth = max(0, n - 2)

    for partition in partitions(n):
        PARTITIONS_ENUMERATED += 1
        current = partition
        time = 0
        while True:
            check(
                current == orbit_join(partition, time),
                "semilattice orbit-join formula failed",
            )
            check(
                current == translated_components(partition, time),
                "independent translated-component formula failed",
            )
            following = update(current)
            check(refines(current, following), "join update was not monotone")
            if following == current:
                break
            current = following
            time += 1
            check(time <= n, "orbit did not stabilize by the finite bound")

        subgroup_size = core_size(partition)
        check(
            current == core_partition(n, subgroup_size),
            "endpoint is not the generated-subgroup coset partition",
        )
        check(
            current == translated_components(partition, n - 1),
            "endpoint disagrees with the full translate graph",
        )
        check(update(current) == current, "predicted endpoint is not fixed")
        if n >= 3:
            check(
                (time == expected_depth)
                == is_primitive_chord_atom(partition),
                "deepest shell is not exactly the primitive-chord atoms",
            )

        depths[time] += 1
        basins[subgroup_size] += 1
        fixed += time == 0

    check(sum(depths.values()) == bell[n], "Bell phase count failed")
    check(fixed == len(divisors(n)), "fixed points do not match subgroups")
    check(max(depths) == expected_depth, "sharp maximum depth failed")
    expected_deepest = bell[n] if n <= 2 else n * euler_phi(n) // 2
    check(
        depths[expected_depth] == expected_deepest,
        "primitive-chord deepest-shell count failed",
    )
    for subgroup_size in divisors(n):
        check(
            basins[subgroup_size]
            == exact_basin_formula(n, subgroup_size, bell),
            "Möbius--Bell basin formula failed",
        )
        check(
            update(core_partition(n, subgroup_size))
            == core_partition(n, subgroup_size),
            "a cyclic coset partition was not fixed",
        )
    check(sum(basins.values()) == bell[n], "basins do not partition the phase")

    return {
        "n": n,
        "bell": bell[n],
        "fixed": fixed,
        "max_depth": max(depths),
        "deepest": depths[expected_depth],
        "depths": dict(sorted(depths.items())),
        "basins": dict(sorted(basins.items())),
    }


def formula_lanes(bell, n_limit=50, period_limit=60):
    for n in range(1, n_limit + 1):
        basin_total = 0
        for subgroup_size in divisors(n):
            basin = exact_basin_formula(n, subgroup_size, bell)
            check(basin > 0, "closed basin formula was not positive")
            basin_total += basin
            refinement_total = sum(
                exact_basin_formula(n, divisor, bell)
                for divisor in divisors(subgroup_size)
            )
            check(
                refinement_total == bell[subgroup_size] ** (n // subgroup_size),
                "divisor convolution did not recover the refinement count",
            )
        check(basin_total == bell[n], "closed basins did not sum to Bell(n)")

        fixed_count = len(divisors(n))
        coefficients = [1]
        for degree in range(1, period_limit + 1):
            numerator = sum(
                fixed_count * coefficients[degree - step]
                for step in range(1, degree + 1)
            )
            check(numerator % degree == 0, "formal zeta recurrence not integral")
            coefficients.append(numerator // degree)
            check(
                coefficients[degree]
                == comb(fixed_count + degree - 1, degree),
                "formal zeta coefficient disagrees with (1-z)^(-tau(n))",
            )

        for period in range(1, period_limit + 1):
            least_period_points = sum(
                mobius(period // divisor) * fixed_count
                for divisor in divisors(period)
            )
            check(
                least_period_points == (fixed_count if period == 1 else 0),
                "temporal Möbius inversion found a nontrivial cycle",
            )


def main():
    bell = bell_numbers(50)
    rows = [lane(n, bell) for n in range(1, 11)]
    binary_cut_lanes()
    formula_lanes(bell)

    print("cyclic shift--join partition dynamics exact control: PASS")
    print(f"assertions={ASSERTIONS}")
    print(f"partitions_enumerated={PARTITIONS_ENUMERATED}")
    print("exhaustive_n=1..10")
    print("closed_formula_n=1..50")
    print("binary_cut_defect_n=3..12")
    print("temporal_mobius_and_zeta_period=1..60")
    for row in rows:
        print(
            "lane"
            f" n={row['n']} Bell={row['bell']} fixed={row['fixed']}"
            f" max_depth={row['max_depth']} deepest={row['deepest']}"
            f" depths={row['depths']} basins={row['basins']}"
        )


if __name__ == "__main__":
    main()
