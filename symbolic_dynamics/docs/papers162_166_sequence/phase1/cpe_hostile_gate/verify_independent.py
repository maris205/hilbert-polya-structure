#!/usr/bin/env python3
"""Hostile, representation-independent checks for cyclic partition erosion.

Partitions are tuples of bit masks, not restricted-growth strings.  The
partition-lattice Mobius function is reconstructed recursively from the
incidence relation rather than inserted in factorial closed form.  Touchard
polynomials are counted directly from set partitions.  This is finite
counterexample pressure and not a proof for arbitrary n.
"""

from collections import Counter, defaultdict
from functools import lru_cache
from hashlib import sha256
from math import factorial


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def low_bit_index(mask):
    return (mask & -mask).bit_length() - 1


def canon(blocks):
    blocks = tuple(block for block in blocks if block)
    return tuple(sorted(blocks, key=lambda block: (low_bit_index(block), block)))


@lru_cache(None)
def partitions(n):
    if n == 0:
        return ((),)
    bit = 1 << (n - 1)
    out = []
    for old in partitions(n - 1):
        for index in range(len(old)):
            blocks = list(old)
            blocks[index] |= bit
            out.append(canon(blocks))
        out.append(canon(old + (bit,)))
    return tuple(out)


def block_count(partition):
    return len(partition)


def block_at(partition, point):
    bit = 1 << point
    for block in partition:
        if block & bit:
            return block
    raise AssertionError("point omitted from partition")


def related(partition, left, right):
    return bool(block_at(partition, left) & (1 << right))


def shift_mask(mask, amount, n):
    amount %= n
    answer = 0
    for point in range(n):
        if mask & (1 << point):
            answer |= 1 << ((point + amount) % n)
    return answer


def shift(partition, amount, n):
    return canon(shift_mask(block, amount, n) for block in partition)


def meet(left, right):
    return canon(a & b for a in left for b in right if a & b)


def join(partition_list, n):
    parent = list(range(n))

    def find(point):
        while parent[point] != point:
            parent[point] = parent[parent[point]]
            point = parent[point]
        return point

    def union(left, right):
        left, right = find(left), find(right)
        if left != right:
            parent[right] = left

    for partition in partition_list:
        for block in partition:
            points = [point for point in range(n) if block & (1 << point)]
            for point in points[1:]:
                union(points[0], point)
    blocks = defaultdict(int)
    for point in range(n):
        blocks[find(point)] |= 1 << point
    return canon(blocks.values())


def refines(fine, coarse):
    return all(any(block & ~container == 0 for container in coarse)
               for block in fine)


def update(partition, n):
    return meet(partition, shift(partition, 1, n))


def iterate(partition, time, n):
    value = partition
    for _ in range(time):
        value = update(value, n)
    return value


def window(partition, time, n):
    value = partition
    for amount in range(1, time + 1):
        value = meet(value, shift(partition, amount, n))
    return value


def stable_core(partition, n):
    return window(partition, n - 1, n)


def depth(partition, n):
    value = partition
    time = 0
    while True:
        successor = update(value, n)
        if successor == value:
            return time
        value = successor
        time += 1
        if time > n:
            raise AssertionError("monotone orbit failed to stabilize")


def longest_cyclic_run(bits):
    n = len(bits)
    if all(bits):
        return n
    best = run = 0
    for bit in bits + bits:
        run = run + 1 if bit else 0
        best = max(best, run)
    return min(best, n)


def clock(partition, n):
    answer = 0
    for delta in range(1, n):
        good = [related(partition, x, (x + delta) % n) for x in range(n)]
        if not all(good):
            answer = max(answer, longest_cyclic_run(good))
    return answer


def congruence(n, number_of_blocks):
    blocks = [0] * number_of_blocks
    for point in range(n):
        blocks[point % number_of_blocks] |= 1 << point
    return canon(blocks)


def divisors(n):
    return tuple(d for d in range(1, n + 1) if n % d == 0)


@lru_cache(None)
def coarsenings(fine):
    count = len(fine)
    answer = []
    for quotient in partitions(count):
        blocks = []
        for quotient_block in quotient:
            block = 0
            for index in range(count):
                if quotient_block & (1 << index):
                    block |= fine[index]
            blocks.append(block)
        answer.append(canon(blocks))
    return tuple(answer)


@lru_cache(None)
def incidence_mobius(fine, coarse):
    check(refines(fine, coarse), "Mobius requested outside an interval")
    if fine == coarse:
        return 1
    total = 0
    for middle in coarsenings(fine):
        if middle != coarse and refines(middle, coarse):
            total += incidence_mobius(fine, middle)
    return -total


def factorial_mobius(fine, coarse):
    answer = 1
    for container in coarse:
        r = sum(1 for block in fine if block & ~container == 0)
        answer *= (-1) ** (r - 1) * factorial(r - 1)
    return answer


@lru_cache(None)
def touchard_direct(n):
    counts = Counter(len(partition) for partition in partitions(n))
    return tuple(counts.get(k, 0) for k in range(n + 1))


def add_scaled(accumulator, polynomial, scale):
    while len(accumulator) < len(polynomial):
        accumulator.append(0)
    for degree, coefficient in enumerate(polynomial):
        accumulator[degree] += scale * coefficient


def trim(polynomial):
    polynomial = list(polynomial)
    while len(polynomial) > 1 and polynomial[-1] == 0:
        polynomial.pop()
    return tuple(polynomial)


def fibre_formula(target, time, n):
    answer = []
    for theta in coarsenings(target):
        orbit_join = join([shift(theta, -j, n) for j in range(time + 1)], n)
        add_scaled(answer, touchard_direct(len(orbit_join)),
                   incidence_mobius(target, theta))
    return trim(answer or [0])


def source_polynomial(sources):
    counts = Counter(len(source) for source in sources)
    if not counts:
        return (0,)
    return tuple(counts.get(k, 0) for k in range(max(counts) + 1))


@lru_cache(None)
def divisor_mobius(number):
    if number == 1:
        return 1
    return -sum(divisor_mobius(divisor) for divisor in divisors(number)
                if divisor < number)


def primitive_touchard(d):
    answer = []
    for e in divisors(d):
        add_scaled(answer, touchard_direct(e), divisor_mobius(d // e))
    return trim(answer or [0])


def temporal_lane(rows):
    for n in range(1, 9):
        phase = partitions(n)
        depth_histogram = Counter()
        fixed = set()
        for partition in phase:
            actual_depth = depth(partition, n)
            depth_histogram[actual_depth] += 1
            check(actual_depth == clock(partition, n),
                  f"point clock n={n}, partition={partition}")
            core = stable_core(partition, n)
            check(iterate(partition, max(0, n - 2), n) == core,
                  f"n-2 bound n={n}, partition={partition}")
            for time in range(0, n + 3):
                check(iterate(partition, time, n) == window(partition, time, n),
                      f"window n={n}, t={time}, partition={partition}")
            if update(partition, n) == partition:
                fixed.add(partition)
                check(shift(partition, 1, n) == partition,
                      f"fixed but not invariant n={n}")
            else:
                check(refines(update(partition, n), partition),
                      f"wrong refinement direction n={n}")

            # Audit the point-clock orientation at every point and beyond the
            # stabilization time, not merely its maximized run statistic.
            for delta in range(1, n):
                good = [related(partition, x, (x + delta) % n)
                        for x in range(n)]
                if not all(good):
                    check(good.count(False) >= 2,
                          f"exactly one cyclic defect n={n}, delta={delta}")
                    check(longest_cyclic_run(good) <= max(0, n - 2),
                          f"run bound n={n}, delta={delta}")
                for time in range(0, n + 2):
                    evolved = iterate(partition, time, n)
                    for x in range(n):
                        predicted = all(good[(x - j) % n]
                                        for j in range(time + 1))
                        check(related(evolved, x, (x + delta) % n) == predicted,
                              f"pair survival n={n}, d={delta}, t={time}, x={x}")

        expected_fixed = {congruence(n, d) for d in divisors(n)}
        check(fixed == expected_fixed, f"fixed atlas n={n}")
        expected_height = 0 if n <= 2 else n - 2
        check(max(depth_histogram) == expected_height, f"sharp height n={n}")
        if n >= 3:
            witness = canon((1, ((1 << n) - 1) ^ 1))
            check(depth(witness, n) == n - 2, f"witness n={n}")
        rows.append(("temporal", n, len(phase),
                     tuple(sorted(depth_histogram.items())), len(fixed)))


def fibre_lane(rows):
    # All targets, including times strictly after the claimed universal cap.
    # This closes the most material finite-coverage hole in the scout verifier.
    for n in range(1, 7):
        phase = partitions(n)
        for time in range(0, n + 3):
            actual = defaultdict(list)
            for source in phase:
                actual[iterate(source, time, n)].append(source)
            nonempty = 0
            for target in phase:
                direct = source_polynomial(actual.get(target, ()))
                formula = fibre_formula(target, time, n)
                check(direct == formula,
                      f"fibre n={n}, t={time}, target={target}: {direct}!={formula}")
                check(all(coefficient >= 0 for coefficient in formula),
                      f"negative final coefficient n={n}, t={time}")
                nonempty += direct != (0,)

            fixed_targets = {congruence(n, d) for d in divisors(n)}
            predicted_shallow = sum(
                sum(fibre_formula(target, time, n)) for target in fixed_targets
            )
            actual_shallow = sum(depth(source, n) <= time for source in phase)
            check(predicted_shallow == actual_shallow,
                  f"depth census n={n}, t={time}")
            rows.append(("fibre", n, time, nonempty, actual_shallow))

    # A sparse n=7 lane uses literal enumeration at boundary and stable times.
    n = 7
    phase = partitions(n)
    for time in (0, n - 2, n - 1, n + 2):
        actual = defaultdict(list)
        for source in phase:
            actual[iterate(source, time, n)].append(source)
        for target in phase:
            check(source_polynomial(actual.get(target, ())) ==
                  fibre_formula(target, time, n),
                  f"sparse fibre n=7, t={time}, target={target}")
        rows.append(("fibre7", time, len(actual)))


def mobius_and_basin_lane(rows):
    # Reconstruct partition-lattice Mobius values from incidence and only then
    # compare them with the claimed sign/factorial orientation.
    for n in range(1, 8):
        intervals = 0
        for fine in partitions(n):
            for coarse in coarsenings(fine):
                check(incidence_mobius(fine, coarse) ==
                      factorial_mobius(fine, coarse),
                      f"partition Mobius sign n={n}, {fine}, {coarse}")
                intervals += 1
        rows.append(("mobius", n, intervals))

    for n in range(1, 10):
        actual = defaultdict(list)
        for source in partitions(n):
            actual[stable_core(source, n)].append(source)
        total = 0
        basin_row = []
        for d in divisors(n):
            target = congruence(n, d)
            direct = source_polynomial(actual[target])
            formula = primitive_touchard(d)
            check(direct == formula, f"terminal basin n={n}, d={d}")
            check(len(formula) - 1 == d and formula[-1] == 1,
                  f"terminal leading term n={n}, d={d}")
            size = sum(formula)
            check(size > 0, f"empty fixed basin n={n}, d={d}")
            total += size
            basin_row.append((d, size))
        check(total == len(partitions(n)), f"terminal basins do not partition n={n}")
        rows.append(("basin", n, tuple(basin_row)))


def main():
    rows = []
    temporal_lane(rows)
    fibre_lane(rows)
    mobius_and_basin_lane(rows)
    payload = "\n".join(repr(row) for row in rows)
    print("CPE_HOSTILE_GATE_INDEPENDENT_V1")
    print("representation=canonical_bitmask_blocks")
    print("temporal=all_partitions_n1..8_times0..n+2")
    print("pair_clock=all_points_all_deltas_n1..8_times0..n+1")
    print("fibres=all_targets_n1..6_times0..n+2_plus_n7_t0,5,6,9")
    print("partition_mobius=incidence_reconstruction_n1..7")
    print("terminal_basins=all_partitions_n1..9")
    print(f"row_sha256={sha256(payload.encode()).hexdigest()}")
    print(f"assertions={ASSERTIONS}")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
