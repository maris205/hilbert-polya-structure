#!/usr/bin/env python3
"""Exact paper-local audit for derived-centralizer orbit partitions.

The program is self-contained and uses only Python integers, tuples, sets,
and dictionaries.  Its finite enumerations are falsification controls, not
proofs of the all-weight theorems or evidence of novelty.
"""

from collections import Counter
from functools import lru_cache
from itertools import permutations, product


class Audit:
    def __init__(self):
        self.assertions = 0

    def check(self, condition, message="assertion failed"):
        self.assertions += 1
        if not condition:
            raise AssertionError(message)


AUDIT = Audit()


@lru_cache(maxsize=None)
def integer_partitions(total, ceiling):
    if total == 0:
        return ((),)
    answer = []
    for part in range(min(total, ceiling), 0, -1):
        for suffix in integer_partitions(total - part, part):
            answer.append((part,) + suffix)
    return tuple(answer)


def ct1_update(partition):
    multiplicities = Counter(partition)
    answer = []
    for size, multiplicity in multiplicities.items():
        if multiplicity == 1:
            answer.extend([1] * size)
        elif multiplicity == 2:
            answer.extend([size, size])
        else:
            answer.append(size * multiplicity)
    answer = tuple(sorted(answer, reverse=True))
    AUDIT.check(sum(answer) == sum(partition), (partition, answer))
    return answer


def recurrent_class(partition):
    multiplicities = Counter(partition)
    ones = multiplicities.get(1, 0)
    exceptional = [
        size
        for size, multiplicity in multiplicities.items()
        if size >= 2 and multiplicity != 2
    ]
    if ones in (0, 1, 2) and not exceptional:
        return "B"
    if ones == 0 and len(exceptional) == 1:
        amplitude = exceptional[0]
        if amplitude >= 3 and multiplicities[amplitude] == 1:
            return "O1_WHOLE"
    if ones >= 3 and not exceptional:
        if multiplicities.get(ones, 0) == 0:
            return "O1_SPLIT"
    if ones >= 3 and len(exceptional) == 1:
        whole = exceptional[0]
        if (
            whole >= 3
            and multiplicities[whole] == 1
            and (whole == ones or multiplicities.get(ones, 0) == 0)
        ):
            return "O2_EQUAL" if whole == ones else "O2_UNEQUAL"
    return None


def orbit_profile(states):
    maximum_tail = 0
    periods = set()
    fixed = 0
    recurrent = 0
    for start in states:
        seen = {}
        state = start
        while state not in seen:
            seen[state] = len(seen)
            state = ct1_update(state)
            AUDIT.check(sum(state) == sum(start), "weight escaped")
        tail = seen[state]
        period = len(seen) - tail
        AUDIT.check(period >= 1)
        periods.add(period)
        maximum_tail = max(maximum_tail, tail)

        successor = ct1_update(start)
        second = ct1_update(successor)
        decoded = recurrent_class(start)
        AUDIT.check((decoded is not None) == (second == start),
                    (start, successor, second, decoded))
        if decoded is not None:
            recurrent += 1
            is_fixed_class = decoded in {"B", "O2_EQUAL"}
            AUDIT.check(is_fixed_class == (successor == start), start)
        fixed += successor == start
    AUDIT.check(recurrent >= fixed)
    AUDIT.check((recurrent - fixed) % 2 == 0)
    return maximum_tail, tuple(sorted(periods)), fixed, recurrent


def local_contribution(size, multiplicity):
    if multiplicity == 0:
        return ()
    if multiplicity == 1:
        return (1,) * size
    if multiplicity == 2:
        return (size, size)
    return (size * multiplicity,)


def coefficient_fibres(maximum_weight):
    coefficients = {(0, ()): 1}
    for size in range(1, maximum_weight + 1):
        updated = Counter()
        for (weight, target), coefficient in coefficients.items():
            maximum_multiplicity = (maximum_weight - weight) // size
            for multiplicity in range(maximum_multiplicity + 1):
                contribution = local_contribution(size, multiplicity)
                merged = tuple(sorted(target + contribution, reverse=True))
                updated[(weight + size * multiplicity, merged)] += coefficient
        coefficients = dict(updated)
    answer = {weight: Counter() for weight in range(maximum_weight + 1)}
    for (weight, target), coefficient in coefficients.items():
        answer[weight][target] += coefficient
    return answer


def dimer_coefficients(maximum_weight, excluded=()):
    excluded = set(excluded)
    coefficients = [0] * (maximum_weight + 1)
    coefficients[0] = 1
    for size in range(2, maximum_weight // 2 + 1):
        if size in excluded:
            continue
        contribution = 2 * size
        for weight in range(maximum_weight, contribution - 1, -1):
            coefficients[weight] += coefficients[weight - contribution]
    return coefficients


def recurrent_generating_counts(maximum_weight):
    fixed = [0] * (maximum_weight + 1)
    cycles = [0] * (maximum_weight + 1)
    base = dimer_coefficients(maximum_weight)
    for weight in range(maximum_weight + 1):
        fixed[weight] += sum(
            base[weight - residue]
            for residue in (0, 1, 2)
            if weight >= residue
        )
    for amplitude in range(3, maximum_weight + 1):
        dimers = dimer_coefficients(maximum_weight, (amplitude,))
        for weight in range(amplitude, maximum_weight + 1):
            cycles[weight] += dimers[weight - amplitude]
        for weight in range(2 * amplitude, maximum_weight + 1):
            fixed[weight] += dimers[weight - 2 * amplitude]
        for other in range(amplitude + 1, maximum_weight + 1):
            if amplitude + other > maximum_weight:
                break
            pair_dimers = dimer_coefficients(
                maximum_weight, (amplitude, other)
            )
            for weight in range(amplitude + other, maximum_weight + 1):
                cycles[weight] += pair_dimers[weight - amplitude - other]
    return fixed, cycles


def colored_initial(partition):
    return tuple(
        sorted(((size, (tag,)) for tag, size in enumerate(partition)),
               reverse=True)
    )


def colored_update(state):
    by_size = {}
    for size, tag in state:
        by_size.setdefault(size, []).append(tag)
    answer = []
    crossing = False
    for size, tags in by_size.items():
        multiplicity = len(tags)
        if multiplicity == 1:
            answer.extend((1, tags[0]) for _ in range(size))
        elif multiplicity == 2:
            answer.extend((size, tag) for tag in tags)
        else:
            distinct = set(tags)
            crossing |= len(distinct) > 1
            union = tuple(sorted({atom for tag in distinct for atom in tag}))
            answer.append((size * multiplicity, union))
    return tuple(sorted(answer, reverse=True)), crossing


def verify_colored(maximum_weight):
    initial_count = 0
    reachable_count = 0
    clean_pairs = 0
    for total in range(1, maximum_weight + 1):
        for partition in integer_partitions(total, total):
            initial_count += 1
            initial_sizes = dict(enumerate(partition))
            state = colored_initial(partition)
            seen = set()
            while state not in seen:
                seen.add(state)
                reachable_count += 1
                pieces_by_tag = {}
                for size, tag in state:
                    pieces_by_tag.setdefault(tag, []).append(size)
                tags = set(pieces_by_tag)
                atoms = [atom for tag in tags for atom in tag]
                AUDIT.check(
                    len(atoms) == len(set(atoms))
                    and set(atoms) == set(initial_sizes),
                    (partition, state),
                )
                for tag, sizes in pieces_by_tag.items():
                    mass = sum(initial_sizes[atom] for atom in tag)
                    AUDIT.check(
                        sizes == [mass]
                        or (len(sizes) == mass and set(sizes) == {1}),
                        (partition, tag, sizes, mass),
                    )

                successor, first_cross = colored_update(state)
                uncolored_successor = tuple(
                    sorted((size for size, _tag in successor), reverse=True)
                )
                uncolored_state = tuple(
                    sorted((size for size, _tag in state), reverse=True)
                )
                AUDIT.check(uncolored_successor == ct1_update(uncolored_state))
                old_count = len(tags)
                new_count = len({tag for _size, tag in successor})
                AUDIT.check(new_count <= old_count)
                AUDIT.check(first_cross == (new_count < old_count))

                second, second_cross = colored_update(successor)
                third, _ = colored_update(second)
                if not first_cross and not second_cross:
                    clean_pairs += 1
                    AUDIT.check(third == successor,
                                (partition, state, successor, second, third))
                state = successor
    return initial_count, reachable_count, clean_pairs


def compose(left, right):
    return tuple(left[right[index]] for index in range(len(left)))


def inverse(permutation):
    answer = [0] * len(permutation)
    for index, image in enumerate(permutation):
        answer[image] = index
    return tuple(answer)


def commutator(left, right):
    return compose(compose(compose(left, right), inverse(left)), inverse(right))


def generated_group(generators, degree):
    identity = tuple(range(degree))
    generators = tuple(set(generators))
    group = {identity}
    frontier = [identity]
    while frontier:
        element = frontier.pop()
        for generator in generators:
            candidate = compose(element, generator)
            if candidate not in group:
                group.add(candidate)
                frontier.append(candidate)
    return group


def derived_group(group, degree):
    group = tuple(group)
    commutators = {
        commutator(left, right) for left in group for right in group
    }
    return generated_group(commutators, degree)


def wreath_group(cycle_size, block_count):
    degree = cycle_size * block_count
    answer = []
    for shifts in product(range(cycle_size), repeat=block_count):
        for block_permutation in permutations(range(block_count)):
            element = []
            for block in range(block_count):
                for coordinate in range(cycle_size):
                    element.append(
                        block_permutation[block] * cycle_size
                        + (coordinate + shifts[block]) % cycle_size
                    )
            answer.append(tuple(element))
    AUDIT.check(len(answer) == len(set(answer)))
    return tuple(answer)


def orbit_sizes(group, degree):
    remaining = set(range(degree))
    answer = []
    while remaining:
        point = min(remaining)
        orbit = {element[point] for element in group}
        AUDIT.check(orbit <= remaining)
        remaining -= orbit
        answer.append(len(orbit))
    return tuple(sorted(answer, reverse=True))


def expected_wreath_orbits(cycle_size, block_count):
    if block_count == 1:
        return (1,) * cycle_size
    if block_count == 2:
        return (cycle_size, cycle_size)
    return (cycle_size * block_count,)


def verify_wreath_rule():
    cases = (
        (1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
        (2, 1), (3, 1), (4, 1), (5, 1), (6, 1),
        (2, 2), (3, 2), (4, 2), (5, 2),
        (2, 3), (3, 3), (4, 3), (2, 4),
    )
    element_count = 0
    for cycle_size, block_count in cases:
        degree = cycle_size * block_count
        group = wreath_group(cycle_size, block_count)
        derived = derived_group(group, degree)
        AUDIT.check(
            orbit_sizes(derived, degree)
            == expected_wreath_orbits(cycle_size, block_count),
            (cycle_size, block_count),
        )
        element_count += len(group)
    return len(cases), element_count


def main():
    predicted_fixed, predicted_cycles = recurrent_generating_counts(30)
    total_states = 0
    all_periods = set()
    global_max_tail = 0
    first_tail_weights = {}
    n30 = None
    for total in range(1, 46):
        states = integer_partitions(total, total)
        maximum_tail, periods, fixed, recurrent = orbit_profile(states)
        total_states += len(states)
        all_periods.update(periods)
        global_max_tail = max(global_max_tail, maximum_tail)
        first_tail_weights.setdefault(maximum_tail, total)
        AUDIT.check(set(periods) <= {1, 2})
        AUDIT.check(maximum_tail <= 2 * total)
        cycles = (recurrent - fixed) // 2
        if total <= 30:
            AUDIT.check(fixed == predicted_fixed[total], (total, fixed))
            AUDIT.check(cycles == predicted_cycles[total], (total, cycles))
        if total == 30:
            n30 = (fixed, cycles, recurrent)

    predicted_fibres = coefficient_fibres(30)
    all_target_cells = 0
    nonzero_target_cells = 0
    for total in range(1, 31):
        states = integer_partitions(total, total)
        actual = Counter(ct1_update(state) for state in states)
        AUDIT.check(sum(actual.values()) == len(states))
        for target in states:
            AUDIT.check(actual[target] == predicted_fibres[total][target],
                        (total, target, actual[target],
                         predicted_fibres[total][target]))
            all_target_cells += 1
            nonzero_target_cells += actual[target] > 0

    wreath_cases, wreath_elements = verify_wreath_rule()
    tag_initial, tag_reachable, clean_pairs = verify_colored(30)
    AUDIT.check(total_states == 540634)
    AUDIT.check(n30 == (59, 139, 337))
    AUDIT.check((tag_initial, tag_reachable, clean_pairs)
                == (28628, 118634, 56961))
    AUDIT.check((wreath_cases, wreath_elements) == (18, 1259))

    first_tail_text = ",".join(
        f"{tail}:{first_tail_weights[tail]}"
        for tail in sorted(first_tail_weights)
    )
    print("DERIVED_CENTRALIZER_ORBIT_PARTITIONS_V1")
    print(f"PARTITIONS_N_LE_45={total_states}")
    print(f"PERIODS={','.join(map(str, sorted(all_periods)))}")
    print(f"MAX_TAIL={global_max_tail}")
    print(f"FIRST_TAIL_WEIGHTS={first_tail_text}")
    print(f"N30_FIXED_CYCLES_RECURRENT={n30[0]},{n30[1]},{n30[2]}")
    print(f"ALL_TARGET_CELLS_N_LE_30={all_target_cells}")
    print(f"NONZERO_TARGET_CELLS_N_LE_30={nonzero_target_cells}")
    print(f"WREATH_CASES={wreath_cases}")
    print(f"WREATH_ELEMENTS={wreath_elements}")
    print(f"TAG_INITIAL_N_LE_30={tag_initial}")
    print(f"TAG_REACHABLE={tag_reachable}")
    print(f"TWO_CLEAN_PAIRS={clean_pairs}")
    print(f"TOTAL_ASSERTIONS={AUDIT.assertions}")
    print("EXACT_ARITHMETIC=python_integers_and_tuples")
    print("FLOATING_POINT=none")
    print("SAMPLING=none")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
