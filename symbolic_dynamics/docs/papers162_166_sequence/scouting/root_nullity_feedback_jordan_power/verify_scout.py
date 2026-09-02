#!/usr/bin/env python3
"""Exact audit for nullity-feedback powers of nilpotent Jordan types.

The partition model and literal finite-field matrix model are implemented
separately.  Only the Python standard library is used.
"""

from collections import Counter
from functools import lru_cache
from math import prod


ASSERTIONS = 0


def check(condition, message="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


@lru_cache(None)
def partitions(n, maximum=None):
    if n == 0:
        return ((),)
    if maximum is None or maximum > n:
        maximum = n
    output = []
    for first in range(maximum, 0, -1):
        for tail in partitions(n - first, first):
            output.append((first,) + tail)
    return tuple(output)


def block_power_type(size, exponent):
    quotient, remainder = divmod(size, exponent)
    if quotient == 0:
        return (1,) * remainder
    return (quotient + 1,) * remainder + (quotient,) * (exponent - remainder)


def power_type(partition, exponent):
    pieces = []
    for size in partition:
        pieces.extend(block_power_type(size, exponent))
    return tuple(sorted(pieces, reverse=True))


def feedback_step(partition):
    return power_type(partition, 1 + len(partition))


def feedback_iterate(partition, time):
    for _ in range(time):
        partition = feedback_step(partition)
    return partition


def exponent_sequence(partition, steps):
    values = [1]
    for _ in range(steps):
        current = values[-1]
        nullity = sum(min(current, size) for size in partition)
        values.append(current * (1 + nullity))
    return tuple(values)


def point_clock(partition):
    time = 0
    exponent = 1
    while exponent < partition[0]:
        exponent *= 1 + sum(min(exponent, size) for size in partition)
        time += 1
    return time


def sylvester_exponents(steps):
    values = [1]
    for _ in range(steps):
        values.append(values[-1] * (values[-1] + 1))
    return tuple(values)


def global_clock(n):
    time = 0
    exponent = 1
    while exponent < n:
        exponent *= exponent + 1
        time += 1
    return time


def tail_threshold(tail, time):
    value = 1
    for _ in range(time):
        value *= 1 + value + sum(min(value, size) for size in tail)
    return value


def conjugate_partition(partition):
    if not partition:
        return ()
    return tuple(sum(size >= column for size in partition) for column in range(1, partition[0] + 1))


# ---------------------------------------------------------------------------
# A target-resolved fixed-r flow formula.


@lru_cache(None)
def multiset_count(count, maximum_value, total):
    """Multisets of `count` elements in [0,maximum_value] with given sum."""
    if count < 0 or maximum_value < 0 or total < 0:
        return 0
    table = {(0, 0): 1}
    for value in range(maximum_value + 1):
        new = {}
        for (used, subtotal), ways in table.items():
            for multiplicity in range(count - used + 1):
                next_total = subtotal + multiplicity * value
                if next_total <= total:
                    key = (used + multiplicity, next_total)
                    new[key] = new.get(key, 0) + ways
        table = new
    return table.get((count, total), 0)


def fixed_r_flow_fibre(target, r):
    """Evaluate the quotient/residue flow formula for sources of length r-1."""
    counts = Counter(target)
    maximum = target[0]
    answer = 0

    def descend(level, residue_sum, used_large, weight):
        nonlocal answer
        if level == 1:
            b_one = residue_sum
            for a_one in range(r - used_large):
                residue_ways = multiset_count(a_one, r - 1, b_one)
                if residue_ways == 0:
                    continue
                small_count = r - 1 - used_large - a_one
                small_weight = counts[1] - r * a_one + b_one
                small_ways = multiset_count(
                    small_count, r - 2, small_weight - small_count
                )
                answer += weight * residue_ways * small_ways
            return

        for a_level in range(r - used_large):
            residue_ways = multiset_count(a_level, r - 1, residue_sum)
            if residue_ways == 0:
                continue
            previous_residue = counts[level] - r * a_level + residue_sum
            if previous_residue < 0:
                continue
            descend(
                level - 1,
                previous_residue,
                used_large + a_level,
                weight * residue_ways,
            )

    # No target block above `maximum` forces B_maximum=0.
    descend(maximum, 0, 0, 1)
    return answer


@lru_cache(None)
def bounded_partition_count(total, maximum_part, maximum_length):
    if total == 0:
        return 1
    if total < 0 or maximum_part == 0 or maximum_length == 0:
        return 0
    return bounded_partition_count(total, maximum_part - 1, maximum_length) + bounded_partition_count(
        total - maximum_part, maximum_part, maximum_length - 1
    )


def zero_fibre_gaussian_count(n):
    # For source length ell, subtract one from every part.  The remaining
    # Ferrers diagram lies in an ell by ell rectangle.
    return sum(
        bounded_partition_count(n - length, length, length)
        for length in range(1, n + 1)
    )


# ---------------------------------------------------------------------------
# Literal matrix arithmetic over F_p.


def zero_matrix(n):
    return tuple(tuple(0 for _ in range(n)) for _ in range(n))


def identity_matrix(n):
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))


def matrix_multiply(left, right, p):
    n = len(left)
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(n)) % p for j in range(n))
        for i in range(n)
    )


def matrix_power(matrix, exponent, p):
    result = identity_matrix(len(matrix))
    base = matrix
    while exponent:
        if exponent & 1:
            result = matrix_multiply(result, base, p)
        base = matrix_multiply(base, base, p)
        exponent //= 2
    return result


def matrix_rank(matrix, p):
    work = [list(row) for row in matrix]
    rows = len(work)
    columns = len(work[0]) if rows else 0
    rank = 0
    for column in range(columns):
        pivot = next((i for i in range(rank, rows) if work[i][column] % p), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = pow(work[rank][column] % p, p - 2, p)
        work[rank] = [(inverse * value) % p for value in work[rank]]
        for row in range(rows):
            if row != rank and work[row][column] % p:
                factor = work[row][column] % p
                work[row] = [
                    (a - factor * b) % p for a, b in zip(work[row], work[rank])
                ]
        rank += 1
        if rank == rows:
            break
    return rank


def matrix_nullity(matrix, p):
    return len(matrix) - matrix_rank(matrix, p)


def jordan_matrix(partition):
    n = sum(partition)
    work = [[0] * n for _ in range(n)]
    offset = 0
    for size in partition:
        for i in range(size - 1):
            work[offset + i][offset + i + 1] = 1
        offset += size
    return tuple(tuple(row) for row in work)


def matrix_jordan_type(matrix, p):
    n = len(matrix)
    nullities = [0]
    for exponent in range(1, n + 1):
        nullities.append(matrix_nullity(matrix_power(matrix, exponent, p), p))
    blocks_at_least = [nullities[i] - nullities[i - 1] for i in range(1, n + 1)]
    blocks_at_least.append(0)
    parts = []
    for size in range(1, n + 1):
        exact = blocks_at_least[size - 1] - blocks_at_least[size]
        parts.extend([size] * exact)
    return tuple(sorted(parts, reverse=True))


def literal_matrix_step(matrix, p):
    exponent = 1 + matrix_nullity(matrix, p)
    return matrix_power(matrix, exponent, p)


# ---------------------------------------------------------------------------
# Audits.


def audit_block_formula_and_matrices():
    matrix_cells = 0
    for p in (2, 3):
        for n in range(1, 9):
            for partition in partitions(n):
                matrix = jordan_matrix(partition)
                check(matrix_jordan_type(matrix, p) == partition)
                check(matrix_nullity(matrix, p) == len(partition))
                for exponent in range(1, n + 2):
                    check(
                        matrix_jordan_type(matrix_power(matrix, exponent, p), p)
                        == power_type(partition, exponent),
                        (p, partition, exponent),
                    )
                    matrix_cells += 1
                current_matrix = matrix
                current_type = partition
                for _ in range(global_clock(n) + 2):
                    current_matrix = literal_matrix_step(current_matrix, p)
                    current_type = feedback_step(current_type)
                    check(matrix_jordan_type(current_matrix, p) == current_type)
    return matrix_cells


def audit_temporal():
    state_count = 0
    deepest_rows = []
    for n in range(1, 44):
        states = partitions(n)
        state_count += len(states)
        depths = Counter()
        for partition in states:
            clock = point_clock(partition)
            depths[clock] += 1
            sequence = exponent_sequence(partition, global_clock(n) + 2)
            for time, exponent in enumerate(sequence):
                check(
                    feedback_iterate(partition, time) == power_type(partition, exponent),
                    (partition, time, exponent),
                )
                check((time < clock) == (exponent < partition[0]))
            check(feedback_iterate(partition, clock) == (1,) * n)
            check((feedback_step(partition) == partition) == (partition == (1,) * n))

            tail = partition[1:]
            leading = partition[0]
            for time in range(global_clock(n) + 1):
                check((clock > time) == (leading > tail_threshold(tail, time)))

        expected_global = global_clock(n)
        check(max(depths) == expected_global)
        deepest = [partition for partition in states if point_clock(partition) == expected_global]
        if expected_global == 0:
            expected_unique = True
        else:
            expected_unique = n <= 2 ** (2 ** (expected_global - 1))
        check((len(deepest) == 1) == expected_unique, (n, deepest[:5]))
        if n in (1, 2, 3, 5, 6, 7, 16, 17, 21, 42, 43):
            deepest_rows.append(
                f"n={n}:states={len(states)},depth={expected_global},deepest={len(deepest)},"
                f"depths=" + ",".join(f"{d}:{depths[d]}" for d in sorted(depths))
            )

    # Boundary sentinels beyond feasible full partition enumeration.
    for depth in range(1, 6):
        threshold = 2 ** (2 ** (depth - 1))
        if global_clock(threshold) == depth:
            check(point_clock((threshold,)) == depth)
            check(point_clock((threshold - 1, 1)) < depth)
        next_n = threshold + 1
        if global_clock(next_n) == depth:
            check(point_clock((next_n,)) == depth)
            check(point_clock((next_n - 1, 1)) == depth)

    check(sylvester_exponents(6) == (1, 2, 6, 42, 1806, 3263442, 10650056950806))
    return state_count, deepest_rows


def audit_fibres():
    target_cells = 0
    flow_cells = 0
    signatures = []
    for n in range(1, 25):
        states = partitions(n)
        actual_by_r = {}
        total_fibres = Counter()
        for source in states:
            r = len(source) + 1
            target = feedback_step(source)
            actual_by_r.setdefault(r, Counter())[target] += 1
            total_fibres[target] += 1
        check(sum(total_fibres.values()) == len(states))

        for target in states:
            predicted_total = 0
            target_length = len(target)
            for r in range(2, n + 2):
                # A source of length r-1 yields between r-1 and r(r-1)
                # target blocks, so other r cannot contribute.
                if not (r - 1 <= target_length <= r * (r - 1)):
                    predicted = 0
                else:
                    predicted = fixed_r_flow_fibre(target, r)
                    flow_cells += 1
                actual = actual_by_r.get(r, Counter())[target]
                check(actual == predicted, (n, target, r, actual, predicted))
                predicted_total += predicted
                target_cells += 1
            check(predicted_total == total_fibres[target])

        zero = (1,) * n
        zero_count = total_fibres[zero]
        check(zero_count == zero_fibre_gaussian_count(n))
        terminal_sources = [source for source in states if source[0] <= len(source) + 1]
        nonterminal_sources = [source for source in states if source[0] > len(source) + 1]
        check(len(terminal_sources) == zero_count)
        check(len(nonterminal_sources) <= len(terminal_sources))
        check(
            all(
                conjugate_partition(source) in terminal_sources
                for source in nonterminal_sources
            )
        )
        check(zero_count == max(total_fibres.values()))

        if n in (1, 2, 3, 5, 6, 7, 10, 17, 24):
            images = []
            for time in range(global_clock(n) + 1):
                fibres_t = Counter(feedback_iterate(source, time) for source in states)
                images.append(len(fibres_t))
                check(sum(fibres_t.values()) == len(states))
            signatures.append(
                f"n={n}:states={len(states)},images=" + ",".join(map(str, images))
                + f",one-image={len(total_fibres)},zero-fibre={zero_count},max-fibre={max(total_fibres.values())}"
            )
    return target_cells, flow_cells, signatures


def main():
    print("NULLITY-FEEDBACK JORDAN POWER -- FOCUSED EXACT SCOUT")
    print("[Sylvester exponent thresholds]")
    print("K_0..K_6=" + ",".join(map(str, sylvester_exponents(6))))
    matrix_cells = audit_block_formula_and_matrices()
    print("[literal Jordan-matrix double control]")
    print(f"fields=2,3;n=1..8;power-type-cells={matrix_cells}")
    state_count, deepest_rows = audit_temporal()
    print("[temporal and deepest-type census]")
    for row in deepest_rows:
        print(row)
    print(f"partition-states-through-n43={state_count}")
    target_cells, flow_cells, signatures = audit_fibres()
    print("[every-target one-step flow atlas]")
    for row in signatures:
        print(row)
    print(f"target-r-cells={target_cells};flow-evaluations={flow_cells}")
    print(f"ASSERTIONS={ASSERTIONS}")
    print("RESULT=PASS")
    print("SCOUT_DECISION=KILL_INTERNAL_P137_PLUS_ROOT_OWNER")
    print("EXTERNAL_STATUS=HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
