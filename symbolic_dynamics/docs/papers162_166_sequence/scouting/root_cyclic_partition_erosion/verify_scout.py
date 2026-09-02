#!/usr/bin/env python3
"""Independent exact checks for cyclic partition erosion.

The program uses only exhaustive finite objects and integer arithmetic.  It
checks the literal dynamics separately from the partition-lattice inversion
formula; it is falsification evidence, not a proof for arbitrary n.
"""

from collections import Counter, defaultdict
from functools import lru_cache
from hashlib import sha256
from math import factorial


ASSERTIONS = 0


def check(condition, message="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


@lru_cache(None)
def partitions(n):
    if n == 0:
        return ((),)
    out = []

    def rec(word, maximum):
        if len(word) == n:
            out.append(tuple(word))
            return
        for value in range(maximum + 2):
            rec(word + [value], max(maximum, value))

    rec([0], 0)
    return tuple(out)


def canonical(labels):
    rename = {}
    out = []
    for value in labels:
        if value not in rename:
            rename[value] = len(rename)
        out.append(rename[value])
    return tuple(out)


def rotate(partition, amount=1):
    n = len(partition)
    if n == 0:
        return partition
    return canonical([partition[(i - amount) % n] for i in range(n)])


def meet(left, right):
    return canonical([(left[i], right[i]) for i in range(len(left))])


def update(partition):
    return meet(partition, rotate(partition))


def literal_iterate(partition, time):
    value = partition
    for _ in range(time):
        value = update(value)
    return value


def window_iterate(partition, time):
    value = partition
    for shift in range(1, time + 1):
        value = meet(value, rotate(partition, shift))
    return value


def stable_core(partition):
    value = partition
    for shift in range(1, len(partition)):
        value = meet(value, rotate(partition, shift))
    return value


def actual_depth(partition):
    value = partition
    depth = 0
    while update(value) != value:
        value = update(value)
        depth += 1
    return depth


def longest_cyclic_true(bits):
    n = len(bits)
    if all(bits):
        return n
    if not any(bits):
        return 0
    best = run = 0
    for bit in bits + bits:
        run = run + 1 if bit else 0
        best = max(best, run)
    return min(best, n)


def run_depth(partition):
    n = len(partition)
    if n <= 1:
        return 0
    answer = 0
    for delta in range(1, n):
        good = [partition[x] == partition[(x + delta) % n] for x in range(n)]
        if not all(good):
            answer = max(answer, longest_cyclic_true(good))
    return answer


def refines(fine, coarse):
    n = len(fine)
    for i in range(n):
        for j in range(i + 1, n):
            if fine[i] == fine[j] and coarse[i] != coarse[j]:
                return False
    return True


def join(partition_list):
    n = len(partition_list[0])
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        x, y = find(x), find(y)
        if x != y:
            parent[y] = x

    for partition in partition_list:
        first = {}
        for i, label in enumerate(partition):
            if label in first:
                union(first[label], i)
            else:
                first[label] = i
    return canonical([find(i) for i in range(n)])


@lru_cache(None)
def coarsenings(fine):
    block_count = len(set(fine))
    out = []
    for quotient in partitions(block_count):
        out.append(canonical([quotient[label] for label in fine]))
    return tuple(out)


def partition_mobius(fine, coarse):
    check(refines(fine, coarse), "mobius interval order")
    fine_blocks_by_coarse = defaultdict(set)
    for f, c in zip(fine, coarse):
        fine_blocks_by_coarse[c].add(f)
    answer = 1
    for blocks in fine_blocks_by_coarse.values():
        size = len(blocks)
        answer *= (-1) ** (size - 1) * factorial(size - 1)
    return answer


@lru_cache(None)
def touchard(n):
    # coefficient k is S(n,k)
    stirling = [[0] * (n + 1) for _ in range(n + 1)]
    stirling[0][0] = 1
    for m in range(1, n + 1):
        for k in range(1, m + 1):
            stirling[m][k] = stirling[m - 1][k - 1] + k * stirling[m - 1][k]
    return tuple(stirling[n])


def poly_add_scaled(accumulator, polynomial, scalar):
    if len(accumulator) < len(polynomial):
        accumulator.extend([0] * (len(polynomial) - len(accumulator)))
    for i, coefficient in enumerate(polynomial):
        accumulator[i] += scalar * coefficient


def fibre_formula(target, time):
    answer = []
    for coarse in coarsenings(target):
        orbit_join = join([rotate(coarse, -j) for j in range(time + 1)])
        m = len(set(orbit_join))
        poly_add_scaled(answer, touchard(m), partition_mobius(target, coarse))
    while answer and answer[-1] == 0:
        answer.pop()
    return tuple(answer or [0])


def polynomial_from_sources(sources):
    counts = Counter(len(set(source)) for source in sources)
    if not counts:
        return (0,)
    return tuple(counts.get(k, 0) for k in range(max(counts) + 1))


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def number_theoretic_mobius(n):
    value = n
    primes = 0
    p = 2
    while p * p <= value:
        if value % p == 0:
            value //= p
            primes += 1
            if value % p == 0:
                return 0
            while value % p == 0:
                value //= p
        p += 1
    if value > 1:
        primes += 1
    return -1 if primes % 2 else 1


def primitive_touchard(d):
    answer = []
    for e in divisors(d):
        poly_add_scaled(answer, touchard(e), number_theoretic_mobius(d // e))
    while answer and answer[-1] == 0:
        answer.pop()
    return tuple(answer or [0])


def congruence_partition(n, block_count):
    return canonical([i % block_count for i in range(n)])


def main():
    rows = []

    # Literal temporal law, pointwise run clock, recurrence, and sharp height.
    for n in range(1, 9):
        depth_histogram = Counter()
        fixed = []
        core_histogram = Counter()
        for partition in partitions(n):
            depth = actual_depth(partition)
            depth_histogram[depth] += 1
            check(depth == run_depth(partition), f"run clock n={n}, p={partition}")
            core = stable_core(partition)
            core_histogram[len(set(core))] += 1
            check(literal_iterate(partition, max(0, n - 2)) == core,
                  f"stable time n={n}")
            for time in range(n + 1):
                check(literal_iterate(partition, time) == window_iterate(partition, time),
                      f"window iterate n={n}, t={time}")
            if update(partition) == partition:
                fixed.append(partition)
                check(rotate(partition) == partition, "fixed implies invariant")
            else:
                check(refines(update(partition), partition), "strict refinement direction")
                check(update(partition) != partition, "nonfixed strictness")
        expected_height = 0 if n <= 2 else n - 2
        check(max(depth_histogram) == expected_height, f"sharp height n={n}")
        check(len(fixed) == len(divisors(n)), f"fixed count n={n}")
        expected_fixed = {congruence_partition(n, d) for d in divisors(n)}
        check(set(fixed) == expected_fixed, f"fixed atlas n={n}")
        if n >= 3:
            witness = canonical([1 if i == 0 else 0 for i in range(n)])
            check(actual_depth(witness) == n - 2, f"sharp witness n={n}")
        rows.append(("temporal", n, len(partitions(n)), tuple(sorted(depth_histogram.items())),
                     tuple(sorted(core_histogram.items()))))

    # Independent all-time, every-target, source-block polynomial inversion.
    for n in range(1, 8):
        phase = partitions(n)
        for time in range(0, max(1, n - 1)):
            actual = defaultdict(list)
            for source in phase:
                actual[literal_iterate(source, time)].append(source)
            nonempty_targets = 0
            for target in phase:
                direct = polynomial_from_sources(actual.get(target, ()))
                formula = fibre_formula(target, time)
                check(direct == formula,
                      f"fibre polynomial n={n}, t={time}, target={target}: {direct}!={formula}")
                for coefficient in formula:
                    check(coefficient >= 0, "fibre polynomial nonnegative")
                nonempty_targets += direct != (0,)
            rows.append(("fibre", n, time, nonempty_targets,
                         sum(len(v) for v in actual.values())))

    # Stable basins, including block-marked fibres at each invariant target.
    for n in range(1, 9):
        actual = defaultdict(list)
        for source in partitions(n):
            actual[stable_core(source)].append(source)
        total = 0
        for d in divisors(n):
            target = congruence_partition(n, d)
            direct = polynomial_from_sources(actual[target])
            formula = primitive_touchard(d)
            check(direct == formula, f"terminal basin n={n}, d={d}")
            check(sum(formula) > 0, "positive terminal basin")
            check(len(formula) - 1 == d, "terminal fibre degree recovers block count")
            total += sum(formula)
        check(total == len(partitions(n)), f"basin partition n={n}")
        rows.append(("basin", n, tuple((d, sum(primitive_touchard(d))) for d in divisors(n))))

    payload = "\n".join(repr(row) for row in rows)
    print("CYCLIC_PARTITION_EROSION_SCOUT_V1")
    print(f"temporal_boxes=8")
    print(f"fibre_boxes={sum(max(1, n - 1) for n in range(1, 8))}")
    print(f"basin_boxes=8")
    print(f"row_sha256={sha256(payload.encode()).hexdigest()}")
    print(f"assertions={ASSERTIONS}")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
