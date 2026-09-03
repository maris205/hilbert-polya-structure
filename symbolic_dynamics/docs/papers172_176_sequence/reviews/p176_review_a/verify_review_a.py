#!/usr/bin/env python3
"""Independent hostile-review control for P176.

This program deliberately does not import the author verifier or any scouting
module.  Words are represented by integers (bit i is the symbol at pointed
coordinate i), whereas the author program uses tuples.  The literal map,
functional graphs, necklace decomposition, inverse branches, and arithmetic
censuses are reconstructed here from scratch using only the Python standard
library.

Finite enumeration is a falsifier and regression control, not an
all-parameter proof.
"""

from __future__ import annotations

from collections import Counter
from math import comb, gcd


ASSERTIONS = 0


def require(condition: bool, label: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def divisors(value: int) -> tuple[int, ...]:
    return tuple(candidate for candidate in range(1, value + 1) if value % candidate == 0)


def rotate_left(mask: int, length: int, amount: int) -> int:
    """Rotate pointed coordinates left; bit i stores the symbol at position i."""
    amount %= length
    if amount == 0:
        return mask
    lower = mask & ((1 << amount) - 1)
    return (mask >> amount) | (lower << (length - amount))


def literal_step(mask: int, length: int) -> int:
    ones = mask.bit_count()
    first = mask & 1
    frequency = ones if first else length - ones
    return rotate_left(mask, length, frequency)


def bit(mask: int, position: int) -> int:
    return (mask >> position) & 1


def least_rotational_period(mask: int, length: int) -> int:
    for candidate in divisors(length):
        if all(bit(mask, position) == bit(mask, position % candidate) for position in range(length)):
            return candidate
    raise AssertionError("positive word length has no rotational period")


def map_metrics(successor: list[int]) -> tuple[list[int], list[int], tuple[frozenset[int], ...]]:
    """Return pointwise tails, periods, and the literal cycle vertex sets."""
    size = len(successor)
    tails = [-1] * size
    periods = [0] * size
    cycles: list[frozenset[int]] = []
    for start in range(size):
        if tails[start] >= 0:
            continue
        trail: list[int] = []
        first_visit: dict[int, int] = {}
        cursor = start
        while tails[cursor] < 0 and cursor not in first_visit:
            first_visit[cursor] = len(trail)
            trail.append(cursor)
            cursor = successor[cursor]
        if cursor in first_visit:
            entry = first_visit[cursor]
            cycle = trail[entry:]
            cycle_length = len(cycle)
            cycles.append(frozenset(cycle))
            for vertex in cycle:
                tails[vertex] = 0
                periods[vertex] = cycle_length
            trail = trail[:entry]
        for vertex in reversed(trail):
            next_vertex = successor[vertex]
            tails[vertex] = tails[next_vertex] + 1
            periods[vertex] = periods[next_vertex]
    require(all(value >= 0 for value in tails), "functional graph tail coverage")
    require(all(value >= 1 for value in periods), "functional graph period coverage")
    return tails, periods, tuple(cycles)


def expected_oriented_cycle(bits: tuple[int, ...]) -> tuple[list[int], list[int], set[frozenset[int]]]:
    """Closed prediction for a cycle whose 1-arrows go right and 0-arrows left."""
    length = len(bits)
    if length == 1:
        return [0], [1], {frozenset({0})}
    if length == 2:
        return [0, 0], [2, 2], {frozenset({0, 1})}
    if len(set(bits)) == 1:
        return [0] * length, [length] * length, {frozenset(range(length))}

    cycle_edges = {
        frozenset({q, (q + 1) % length})
        for q in range(length)
        if bits[q] == 1 and bits[(q + 1) % length] == 0
    }
    tails: list[int] = []
    for q in range(length):
        if bits[q] == 1:
            distance = next(
                offset
                for offset in range(length)
                if bits[(q + offset) % length] == 1
                and bits[(q + offset + 1) % length] == 0
            )
        else:
            distance = next(
                offset
                for offset in range(length)
                if bits[(q - offset - 1) % length] == 1
                and bits[(q - offset) % length] == 0
            )
        tails.append(distance)
    return tails, [2] * length, cycle_edges


def longest_cyclic_constant_run(bits: tuple[int, ...]) -> int:
    if len(set(bits)) == 1:
        return len(bits)
    length = len(bits)
    best = 0
    for start in range(length):
        run = 1
        while run < length and bits[(start + run) % length] == bits[start]:
            run += 1
        best = max(best, run)
    return best


def audit_abstract_orientations(max_length: int) -> int:
    """Check the component theorem on every binary orientation, independently of words."""
    profile_count = 0
    for length in range(1, max_length + 1):
        for mask in range(1 << length):
            profile_count += 1
            bits = tuple(bit(mask, q) for q in range(length))
            successor = [
                (q + 1) % length if bits[q] else (q - 1) % length
                for q in range(length)
            ]
            tails, periods, cycles = map_metrics(successor)
            expected_tails, expected_periods, expected_cycles = expected_oriented_cycle(bits)
            require(tails == expected_tails, f"oriented-cycle point tails L={length} mask={mask}")
            require(periods == expected_periods, f"oriented-cycle point periods L={length} mask={mask}")
            require(set(cycles) == expected_cycles, f"oriented-cycle recurrent edges L={length} mask={mask}")
            if length >= 3 and len(set(bits)) > 1:
                require(
                    max(tails) == longest_cyclic_constant_run(bits) - 1,
                    f"oriented-cycle longest-run law L={length} mask={mask}",
                )
    return profile_count


def predicted_predecessors(target: int, length: int) -> set[int]:
    ones = target.bit_count()
    if ones in (0, length):
        return {target}
    answer: set[int] = set()
    source_one = rotate_left(target, length, -ones)
    if bit(source_one, 0) == 1:
        answer.add(source_one)
    source_zero = rotate_left(target, length, ones)
    if bit(source_zero, 0) == 0:
        answer.add(source_zero)
    return answer


def mobius(value: int) -> int:
    residual = value
    distinct_primes = 0
    prime = 2
    while prime * prime <= residual:
        if residual % prime == 0:
            residual //= prime
            distinct_primes += 1
            if residual % prime == 0:
                return 0
            while residual % prime == 0:
                residual //= prime
        prime += 1
    if residual > 1:
        distinct_primes += 1
    return -1 if distinct_primes % 2 else 1


def primitive_formula(length: int, weight: int) -> int:
    return sum(
        mobius(repetition) * comb(length // repetition, weight // repetition)
        for repetition in divisors(gcd(length, weight))
    )


def fixed_formula(length: int) -> int:
    total = 0
    for block_length in divisors(length):
        repetitions = length // block_length
        for block_weight in range(block_length + 1):
            if (repetitions * block_weight) % block_length == 0:
                total += primitive_formula(block_length, block_weight)
    return total


def expected_period_inventory(length: int) -> set[int]:
    if length == 1:
        return {1}
    return {1, 2} | {period for period in divisors(length) if 3 <= period < length}


def audit_necklaces(
    length: int,
    successor: list[int],
    global_tails: list[int],
    global_periods: list[int],
    least_periods: list[int],
) -> tuple[int, int]:
    state_count = 1 << length
    seen = bytearray(state_count)
    necklace_count = 0
    component_count = 0
    for representative in range(state_count):
        if seen[representative]:
            continue
        necklace_count += 1
        period_length = least_periods[representative]
        rotations = tuple(
            rotate_left(representative, length, phase)
            for phase in range(period_length)
        )
        require(len(set(rotations)) == period_length, "distinct phases in least-period necklace")
        phase_of = {word: phase for phase, word in enumerate(rotations)}
        for word in rotations:
            seen[word] = 1

        ones = representative.bit_count()
        phase_successor: list[int] = []
        for phase, word in enumerate(rotations):
            actual_phase = phase_of[successor[word]]
            expected_phase = (phase + (ones if bit(word, 0) else -ones)) % period_length
            require(actual_phase == expected_phase, "literal-to-plus-minus-k phase conjugacy")
            phase_successor.append(actual_phase)

        subgroup_index = gcd(ones, period_length)
        component_length = period_length // subgroup_index
        covered_phases: set[int] = set()
        for residue in range(subgroup_index):
            component_count += 1
            positions = tuple(
                (residue + q * ones) % period_length
                for q in range(component_length)
            )
            require(len(set(positions)) == component_length, "generator coset size")
            covered_phases.update(positions)
            q_of = {phase: q for q, phase in enumerate(positions)}
            bits = tuple(bit(representative, phase) for phase in positions)
            local_successor = [q_of[phase_successor[phase]] for phase in positions]
            for q in range(component_length):
                expected_q = (q + 1) % component_length if bits[q] else (q - 1) % component_length
                require(local_successor[q] == expected_q, "generator-coordinate nearest-neighbour arrow")

            local_tails, local_periods, local_cycles = map_metrics(local_successor)
            expected_tails, expected_periods, expected_cycles = expected_oriented_cycle(bits)
            require(local_tails == expected_tails, "necklace component exact tails")
            require(local_periods == expected_periods, "necklace component exact periods")
            require(set(local_cycles) == expected_cycles, "necklace component exact recurrent sets")
            for q, phase in enumerate(positions):
                word = rotations[phase]
                require(global_tails[word] == local_tails[q], "component/global tail agreement")
                require(global_periods[word] == local_periods[q], "component/global period agreement")
        require(covered_phases == set(range(period_length)), "generator cosets partition phase space")
    require(all(seen), "necklace partition covers binary carrier")
    return necklace_count, component_count


def audit_order(length: int) -> str:
    state_count = 1 << length
    full_mask = state_count - 1
    successor = [literal_step(mask, length) for mask in range(state_count)]
    weights = [mask.bit_count() for mask in range(state_count)]
    least_periods = [least_rotational_period(mask, length) for mask in range(state_count)]
    indegree = [0] * state_count
    for source, target in enumerate(successor):
        require(0 <= target < state_count, "literal carrier closure")
        require(weights[source] == weights[target], "literal weight preservation")
        indegree[target] += 1

    for target in range(state_count):
        predicted = predicted_predecessors(target, length)
        require(indegree[target] == len(predicted), "every-target predecessor completeness")
        for source in predicted:
            require(successor[source] == target, "every labelled predecessor is sufficient")
        require(indegree[target] in (0, 1, 2), "global fibre support is 0/1/2")

    layer_histograms = [Counter() for _ in range(length + 1)]
    for target, fibre_size in enumerate(indegree):
        layer_histograms[weights[target]][fibre_size] += 1
    require(layer_histograms[0] == Counter({1: 1}), "all-zero target boundary fibre")
    require(layer_histograms[length] == Counter({1: 1}), "all-one target boundary fibre")
    for weight in range(1, length):
        if (2 * weight) % length == 0:
            expected = Counter({1: comb(length, weight)})
        else:
            corner = comb(length - 2, weight - 1)
            expected = Counter(
                {
                    0: corner,
                    1: comb(length, weight) - 2 * corner,
                    2: corner,
                }
            )
            expected += Counter()  # discard any formal zero entries
        require(layer_histograms[weight] == expected, "weight-layer fibre histogram")

    global_fibres = Counter(indegree)
    image_size = sum(value > 0 for value in indegree)
    image_formula = 2 + sum(
        comb(length, weight)
        - (0 if (2 * weight) % length == 0 else comb(length - 2, weight - 1))
        for weight in range(1, length)
    )
    require(image_size == image_formula, "closed image formula")
    require(sum(size * count for size, count in global_fibres.items()) == state_count, "fibre mass conservation")

    tails, periods, cycles = map_metrics(successor)
    inventory = set(periods)
    require(inventory == expected_period_inventory(length), "complete possible-period inventory")
    maximum_tail = max(tails)
    require(maximum_tail == max(0, length - 2), "sharp global preperiod")
    deepest = {mask for mask, value in enumerate(tails) if value == maximum_tail}
    if length == 1:
        expected_deepest = {0, 1}
    elif length == 2:
        expected_deepest = set(range(4))
    else:
        expected_deepest = {2, full_mask ^ 2}
    require(deepest == expected_deepest, "exact deepest-state set")

    primitive_by_weight = Counter(
        weights[mask]
        for mask in range(state_count)
        if least_periods[mask] == length
    )
    for weight in range(length + 1):
        require(
            primitive_by_weight[weight] == primitive_formula(length, weight),
            "primitive fixed-density Mobius formula",
        )
    for mask in range(state_count):
        require(
            (successor[mask] == mask) == (weights[mask] % least_periods[mask] == 0),
            "least-period fixed criterion",
        )
    fixed_count = sum(source == target for source, target in enumerate(successor))
    require(fixed_count == fixed_formula(length), "Mobius fixed census")

    for long_period in sorted(expected_period_inventory(length) - {1, 2}):
        quotient = length // long_period
        support = set(range(max(0, quotient - 1))) | {quotient}
        witness = sum(1 << position for position in support)
        require(weights[witness] == quotient, "long-period witness weight")
        require(least_periods[witness] == length, "long-period witness aperiodicity")
        pointed_witness = rotate_left(witness, length, quotient - 1)
        require(tails[pointed_witness] == 0, "long-period witness recurrence")
        require(periods[pointed_witness] == long_period, "long-period witness exact period")

    necklace_count, component_count = audit_necklaces(
        length, successor, tails, periods, least_periods
    )
    cycle_histogram = Counter(len(cycle) for cycle in cycles)
    return (
        f"n={length} states={state_count} necklaces={necklace_count} "
        f"components={component_count} image={image_size} fixed={fixed_count} "
        f"tail={maximum_tail} deepest={len(deepest)} periods={sorted(inventory)} "
        f"cycles={dict(sorted(cycle_histogram.items()))} "
        f"fibres={dict(sorted(global_fibres.items()))}"
    )


def main() -> None:
    print("P176 HOSTILE REVIEW A -- INDEPENDENT BITMASK CONTROL")
    print("STATUS AMBER_INTERNAL_NEAR_P166 / HOLD_EXTERNAL")
    orientation_profiles = audit_abstract_orientations(18)
    print(f"ABSTRACT_ORIENTATIONS lengths=1..18 profiles={orientation_profiles} PASS")
    for length in range(1, 20):
        print(audit_order(length))
    print("THEOREM +/-k pointed-necklace components PASS")
    print("THEOREM possible-period inventory PASS")
    print("THEOREM sharp n-2 clock and exact deepest set PASS")
    print("THEOREM every-target 0/1/2 fibres and histogram PASS")
    print("THEOREM primitive-block Mobius fixed census PASS")
    print(f"ASSERTIONS {ASSERTIONS}")
    print("HOSTILE_REVIEW_A EXACT_CONTROL_PASS")


if __name__ == "__main__":
    main()
