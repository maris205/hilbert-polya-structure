#!/usr/bin/env python3
"""Exact verifier for the second, nondivisor algebraic replacement lane.

Every displayed finite carrier is completely enumerated.  The program uses
only Python integers and tuples: no random sampling, floating point, network
access, third-party package, or wall-clock input is present.
"""

from collections import Counter, deque
from dataclasses import dataclass
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


@dataclass(frozen=True)
class Summary:
    states: int
    image: int
    fixed: int
    max_fibre: int
    periods: tuple
    max_tail: int
    recurrent: int


def functional_summary(states, update):
    states = tuple(states)
    universe = set(states)
    AUDIT.check(len(universe) == len(states), "carrier has duplicates")
    nxt = {}
    for state in states:
        image = update(state)
        AUDIT.check(image in universe, (state, image, "not a self-map"))
        nxt[state] = image

    fibres = Counter(nxt.values())
    periods = set()
    recurrent = set()
    max_tail = 0
    for start in states:
        seen = {}
        state = start
        while state not in seen:
            AUDIT.check(state in universe)
            seen[state] = len(seen)
            state = nxt[state]
            AUDIT.check(len(seen) <= len(states) + 1)
        tail = seen[state]
        period = len(seen) - tail
        AUDIT.check(period >= 1)
        max_tail = max(max_tail, tail)
        periods.add(period)
        point = state
        for _ in range(period):
            recurrent.add(point)
            point = nxt[point]
        AUDIT.check(point == state)

    fixed = sum(nxt[state] == state for state in states)
    AUDIT.check(sum(fibres.values()) == len(states))
    AUDIT.check(fixed == sum(nxt[state] == state for state in recurrent))
    return Summary(
        states=len(states),
        image=len(fibres),
        fixed=fixed,
        max_fibre=max(fibres.values()),
        periods=tuple(sorted(periods)),
        max_tail=max_tail,
        recurrent=len(recurrent),
    )


def summary_line(handle, carrier, summaries, decision):
    periods = sorted({period for row in summaries for period in row.periods})
    fixed = [row.fixed for row in summaries]
    recurrent = [row.recurrent for row in summaries]
    images = [row.image for row in summaries]
    return (
        f"{handle}|{carrier}|params={len(summaries)}"
        f"|states={sum(row.states for row in summaries)}"
        f"|periods={','.join(map(str, periods))}"
        f"|max_tail={max(row.max_tail for row in summaries)}"
        f"|fixed={min(fixed)}..{max(fixed)}"
        f"|recurrent={min(recurrent)}..{max(recurrent)}"
        f"|image={min(images)}..{max(images)}"
        f"|max_fibre={max(row.max_fibre for row in summaries)}"
        f"|{decision}"
    )


# ---------------------------------------------------------------------------
# Conjugacy/type transforms from characteristic subgroups


@lru_cache(maxsize=None)
def integer_partitions(total, ceiling):
    if total == 0:
        return ((),)
    out = []
    for part in range(min(total, ceiling), 0, -1):
        for suffix in integer_partitions(total - part, part):
            out.append((part,) + suffix)
    return tuple(out)


def partition_map(partition, kind):
    multiplicities = Counter(partition)
    out = []
    for size, multiplicity in multiplicities.items():
        if kind == "derived_centralizer":
            if multiplicity == 1:
                out.extend([1] * size)
            elif multiplicity == 2:
                out.extend([size, size])
            else:
                out.append(size * multiplicity)
        elif kind == "second_derived_centralizer":
            if multiplicity >= 4:
                out.append(size * multiplicity)
            elif multiplicity == 3:
                out.extend([size] * 3)
            else:
                out.extend([1] * (size * multiplicity))
        elif kind == "solvable_radical_centralizer":
            if multiplicity <= 4:
                out.append(size * multiplicity)
            else:
                out.extend([size] * multiplicity)
        elif kind == "center_centralizer":
            if size == 1 and multiplicity == 2:
                out.append(2)
            else:
                out.extend([size] * multiplicity)
        elif kind == "derived_young":
            if size == 2:
                out.extend([1] * (2 * multiplicity))
            else:
                out.extend([size] * multiplicity)
        elif kind == "second_derived_young":
            if size in (2, 3):
                out.extend([1] * (size * multiplicity))
            else:
                out.extend([size] * multiplicity)
        elif kind == "solvable_radical_young":
            if size >= 5:
                out.extend([1] * (size * multiplicity))
            else:
                out.extend([size] * multiplicity)
        elif kind == "center_young":
            if size >= 3:
                out.extend([1] * (size * multiplicity))
            else:
                out.extend([size] * multiplicity)
        else:
            raise ValueError(kind)
    result = tuple(sorted(out, reverse=True))
    AUDIT.check(sum(result) == sum(partition), (kind, partition, result))
    return result


TYPE_SYSTEMS = (
    (
        "CT1",
        "partition types; orbits of the derived subgroup of a permutation centralizer",
        "derived_centralizer",
        "PROMOTE_INTERNAL_THEOREM_READY_OWNER_HOLD",
    ),
    (
        "CT2",
        "partition types; second-derived-centralizer orbit type",
        "second_derived_centralizer",
        "KILL_ADJACENT_DERIVED_SERIES_SIBLING",
    ),
    (
        "CT3",
        "partition types; solvable-radical-centralizer orbit type",
        "solvable_radical_centralizer",
        "KILL_BOUNDED_GLAISHER_COAGULATION",
    ),
    (
        "CT4",
        "partition types; center-of-centralizer orbit type",
        "center_centralizer",
        "KILL_ONE_STEP_CENTER_EXCEPTION",
    ),
    (
        "YT1",
        "partition types; derived Young-subgroup orbit type",
        "derived_young",
        "KILL_ONE_STEP_DERIVED_BLOCK_EROSION",
    ),
    (
        "YT2",
        "partition types; second-derived Young-subgroup orbit type",
        "second_derived_young",
        "KILL_ONE_STEP_SECOND_DERIVED_EROSION",
    ),
    (
        "YT3",
        "partition types; solvable-radical Young-subgroup orbit type",
        "solvable_radical_young",
        "KILL_ONE_STEP_SOLVABLE_BLOCK_SPLIT",
    ),
    (
        "YT4",
        "partition types; center-of-Young-subgroup orbit type",
        "center_young",
        "KILL_ONE_STEP_CENTER_BLOCK_SPLIT",
    ),
)


def ct1_local_contribution(size, multiplicity):
    if multiplicity == 0:
        return ()
    if multiplicity == 1:
        return (1,) * size
    if multiplicity == 2:
        return (size, size)
    return (size * multiplicity,)


def ct1_coefficient_fibres(maximum_weight):
    """Expand the exact multivariate source product for CT1.

    The key `(weight,target)` has coefficient equal to the number of source
    multiplicity choices producing that target.  This route never calls the
    literal partition update.
    """
    coefficients = {(0, ()): 1}
    for size in range(1, maximum_weight + 1):
        updated = Counter()
        for (weight, target), coefficient in coefficients.items():
            for multiplicity in range((maximum_weight - weight) // size + 1):
                contribution = ct1_local_contribution(size, multiplicity)
                merged = tuple(sorted(target + contribution, reverse=True))
                updated[(weight + size * multiplicity, merged)] += coefficient
        coefficients = dict(updated)
    by_weight = {weight: Counter() for weight in range(1, maximum_weight + 1)}
    for (weight, target), coefficient in coefficients.items():
        if weight:
            by_weight[weight][target] += coefficient
    return by_weight


def ct1_recurrent_class(partition):
    """Decode the complete all-weight recurrent classification.

    `BASE_FIXED` consists only of persistent singleton multiplicity 0,1,2
    and dimers j,j.  `O1` has one whole/split oscillator.  `O2` has two
    antiphase oscillators; equal amplitudes project to an uncoloured fixed
    point, while unequal amplitudes project to a strict two-cycle.
    """
    multiplicities = Counter(partition)
    ones = multiplicities.get(1, 0)
    non_dimer_sizes = [
        size
        for size, multiplicity in multiplicities.items()
        if size >= 2 and multiplicity not in (0, 2)
    ]

    if ones in (0, 1, 2) and not non_dimer_sizes:
        return "BASE_FIXED"

    if ones == 0 and len(non_dimer_sizes) == 1:
        amplitude = non_dimer_sizes[0]
        if amplitude >= 3 and multiplicities[amplitude] == 1:
            return "O1_WHOLE"

    if ones >= 3 and not non_dimer_sizes:
        amplitude = ones
        if multiplicities.get(amplitude, 0) == 0:
            return "O1_SPLIT"

    if ones >= 3 and len(non_dimer_sizes) == 1:
        whole_amplitude = non_dimer_sizes[0]
        split_amplitude = ones
        if (
            whole_amplitude >= 3
            and multiplicities[whole_amplitude] == 1
            and (
                whole_amplitude == split_amplitude
                or multiplicities.get(split_amplitude, 0) == 0
            )
        ):
            if whole_amplitude == split_amplitude:
                return "O2_EQUAL_FIXED"
            return "O2_UNEQUAL_POINT"
    return None


def dimer_coefficients(maximum_weight, excluded=()):
    """Coefficients of product_{j>=2,j not excluded}(1+q^(2j))."""
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


def ct1_recurrent_generating_counts(maximum_weight):
    """Coefficient transfer for the all-weight fixed/cycle classification."""
    fixed = [0] * (maximum_weight + 1)
    cycles = [0] * (maximum_weight + 1)

    # Base fixed points: (1+q+q^2) product_{j>=2}(1+q^(2j)).
    base = dimer_coefficients(maximum_weight)
    for weight in range(maximum_weight + 1):
        fixed[weight] += sum(
            base[weight - singleton_count]
            for singleton_count in (0, 1, 2)
            if weight >= singleton_count
        )

    # One oscillator of amplitude a>=3.
    for amplitude in range(3, maximum_weight + 1):
        dimers = dimer_coefficients(maximum_weight, (amplitude,))
        for weight in range(amplitude, maximum_weight + 1):
            cycles[weight] += dimers[weight - amplitude]

    # Two antiphase oscillators.  Equal amplitudes project to a fixed
    # partition; unequal amplitudes give one unlabelled two-cycle.
    for left in range(3, maximum_weight + 1):
        equal_dimers = dimer_coefficients(maximum_weight, (left,))
        for weight in range(2 * left, maximum_weight + 1):
            fixed[weight] += equal_dimers[weight - 2 * left]
        for right in range(left + 1, maximum_weight + 1):
            if left + right > maximum_weight:
                break
            dimers = dimer_coefficients(maximum_weight, (left, right))
            for weight in range(left + right, maximum_weight + 1):
                cycles[weight] += dimers[weight - left - right]
    return fixed, cycles


def colored_state(partition):
    """Give each initial part its own permanent tag."""
    return tuple(
        sorted(
            ((size, (tag,)) for tag, size in enumerate(partition)),
            reverse=True,
        )
    )


def colored_ct1_update(state):
    """Lift CT1 to tagged parts and report whether distinct tags merge."""
    by_size = {}
    for size, tag in state:
        by_size.setdefault(size, []).append(tag)
    out = []
    cross_tag_merge = False
    for size, tags in by_size.items():
        multiplicity = len(tags)
        if multiplicity == 1:
            out.extend((1, tags[0]) for _ in range(size))
        elif multiplicity == 2:
            out.extend((size, tag) for tag in tags)
        else:
            distinct_tags = set(tags)
            cross_tag_merge |= len(distinct_tags) > 1
            union_tag = tuple(
                sorted({atom for tag in distinct_tags for atom in tag})
            )
            out.append((size * multiplicity, union_tag))
    return tuple(sorted(out, reverse=True)), cross_tag_merge


def verify_colored_tag_dynamics(maximum_weight):
    """Falsify the tag invariant and the two-clean-step lemma exactly."""
    initial_states = 0
    reachable_states = 0
    clean_pairs = 0
    for total in range(1, maximum_weight + 1):
        for partition in integer_partitions(total, total):
            initial_states += 1
            initial_sizes = dict(enumerate(partition))
            state = colored_state(partition)
            seen = set()
            while state not in seen:
                seen.add(state)
                reachable_states += 1

                # Every current tag is a block of initial tags.  Its mass is
                # represented either by one whole part or by that many ones.
                pieces_by_tag = {}
                for size, tag in state:
                    pieces_by_tag.setdefault(tag, []).append(size)
                tag_blocks = set(pieces_by_tag)
                tagged_atoms = [atom for tag in tag_blocks for atom in tag]
                AUDIT.check(
                    len(tagged_atoms) == len(set(tagged_atoms))
                    and set(tagged_atoms) == set(initial_sizes)
                )
                for tag, sizes in pieces_by_tag.items():
                    mass = sum(initial_sizes[atom] for atom in tag)
                    AUDIT.check(
                        sizes == [mass]
                        or (len(sizes) == mass and set(sizes) == {1}),
                        (partition, state, tag, sizes, mass),
                    )

                successor, first_cross = colored_ct1_update(state)
                AUDIT.check(
                    tuple(sorted((size for size, _tag in successor), reverse=True))
                    == partition_map(
                        tuple(sorted((size for size, _tag in state), reverse=True)),
                        "derived_centralizer",
                    )
                )
                old_tag_count = len(tag_blocks)
                new_tag_count = len({tag for _size, tag in successor})
                AUDIT.check(new_tag_count <= old_tag_count)
                AUDIT.check(first_cross == (new_tag_count < old_tag_count))

                second, second_cross = colored_ct1_update(successor)
                third, _third_cross = colored_ct1_update(second)
                if not first_cross and not second_cross:
                    clean_pairs += 1
                    # After two consecutive clean transitions, the first
                    # successor is already on a period-one or period-two orbit.
                    AUDIT.check(third == successor, (partition, state, successor))
                state = successor
    return initial_states, reachable_states, clean_pairs


def permutation_compose(left, right):
    return tuple(left[right[index]] for index in range(len(left)))


def permutation_inverse(permutation):
    inverse = [0] * len(permutation)
    for index, image in enumerate(permutation):
        inverse[image] = index
    return tuple(inverse)


def permutation_commutator(left, right):
    return permutation_compose(
        permutation_compose(
            permutation_compose(left, right), permutation_inverse(left)
        ),
        permutation_inverse(right),
    )


def generated_permutation_group(generators, degree):
    identity = tuple(range(degree))
    generators = tuple(set(generators))
    group = {identity}
    frontier = [identity]
    while frontier:
        element = frontier.pop()
        for generator in generators:
            product_element = permutation_compose(element, generator)
            if product_element not in group:
                group.add(product_element)
                frontier.append(product_element)
    return group


def derived_permutation_group(group, degree):
    group = tuple(group)
    commutators = {
        permutation_commutator(left, right)
        for left in group
        for right in group
    }
    return generated_permutation_group(commutators, degree)


def wreath_group(cycle_size, block_count):
    degree = cycle_size * block_count
    group = []
    for shifts in product(range(cycle_size), repeat=block_count):
        for block_permutation in permutations(range(block_count)):
            element = []
            for block in range(block_count):
                for coordinate in range(cycle_size):
                    element.append(
                        block_permutation[block] * cycle_size
                        + (coordinate + shifts[block]) % cycle_size
                    )
            AUDIT.check(len(element) == degree)
            group.append(tuple(element))
    AUDIT.check(len(set(group)) == len(group))
    return tuple(group)


def orbit_sizes(group, degree):
    remaining = set(range(degree))
    sizes = []
    while remaining:
        point = min(remaining)
        orbit = {element[point] for element in group}
        AUDIT.check(orbit <= remaining)
        remaining -= orbit
        sizes.append(len(orbit))
    return tuple(sorted(sizes, reverse=True))


def expected_wreath_orbits(cycle_size, block_count, level):
    if level == 1:
        if block_count == 1:
            return (1,) * cycle_size
        if block_count == 2:
            return (cycle_size, cycle_size)
        return (cycle_size * block_count,)
    if block_count >= 4:
        return (cycle_size * block_count,)
    if block_count == 3:
        return (cycle_size,) * 3
    return (1,) * (cycle_size * block_count)


def verify_wreath_factor_rules():
    cases = (
        (1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
        (2, 1), (3, 1), (4, 1), (5, 1), (6, 1),
        (2, 2), (3, 2), (4, 2), (5, 2),
        (2, 3), (3, 3), (4, 3), (2, 4),
    )
    checked_elements = 0
    for cycle_size, block_count in cases:
        degree = cycle_size * block_count
        group = wreath_group(cycle_size, block_count)
        first = derived_permutation_group(group, degree)
        second = derived_permutation_group(first, degree)
        AUDIT.check(
            orbit_sizes(first, degree)
            == expected_wreath_orbits(cycle_size, block_count, 1),
            (cycle_size, block_count, "first derived"),
        )
        AUDIT.check(
            orbit_sizes(second, degree)
            == expected_wreath_orbits(cycle_size, block_count, 2),
            (cycle_size, block_count, "second derived"),
        )
        checked_elements += len(group)
    return len(cases), checked_elements


def run_type_systems():
    lines = []
    total_states = 0
    summaries_by_handle = {}
    for handle, carrier, kind, decision in TYPE_SYSTEMS:
        summaries = []
        for total in range(1, 31):
            states = integer_partitions(total, total)
            summaries.append(
                functional_summary(
                    states, lambda state, kind=kind: partition_map(state, kind)
                )
            )
        summaries_by_handle[handle] = summaries
        total_states += sum(row.states for row in summaries)
        lines.append(summary_line(handle, carrier, summaries, decision))

    # Independent expansion of the every-target CT1 fibre coefficient.
    predicted = ct1_coefficient_fibres(30)
    fibre_cells = 0
    for total in range(1, 31):
        states = integer_partitions(total, total)
        actual = Counter(
            partition_map(state, "derived_centralizer") for state in states
        )
        AUDIT.check(sum(actual.values()) == len(states))
        AUDIT.check(actual == predicted[total], (total, actual, predicted[total]))
        for target in set(actual) | set(predicted[total]):
            AUDIT.check(actual[target] == predicted[total][target])
            fibre_cells += 1

    # A wider falsification box freezes the period/depth signal without
    # serving as the proof of the all-n theorem.
    predicted_fixed, predicted_cycles = ct1_recurrent_generating_counts(30)
    wide_states = 0
    wide_max_tail = 0
    wide_periods = set()
    first_weight_by_tail = {}
    weight_30_fixed = None
    weight_30_cycles = None
    weight_30_recurrent = None
    for total in range(1, 46):
        states = integer_partitions(total, total)
        row = functional_summary(
            states, lambda state: partition_map(state, "derived_centralizer")
        )
        wide_states += row.states
        wide_max_tail = max(wide_max_tail, row.max_tail)
        wide_periods.update(row.periods)
        first_weight_by_tail.setdefault(row.max_tail, total)
        AUDIT.check(set(row.periods) <= {1, 2})
        AUDIT.check(row.max_tail <= 2 * total)

        decoded_fixed = 0
        decoded_recurrent = 0
        decoded_classes = Counter()
        for state in states:
            successor = partition_map(state, "derived_centralizer")
            second = partition_map(successor, "derived_centralizer")
            recurrent_class = ct1_recurrent_class(state)
            AUDIT.check(
                (recurrent_class is not None) == (second == state),
                (total, state, successor, second, recurrent_class),
            )
            if recurrent_class is not None:
                decoded_recurrent += 1
                decoded_classes[recurrent_class] += 1
                fixed_class = recurrent_class in {
                    "BASE_FIXED", "O2_EQUAL_FIXED"
                }
                AUDIT.check(fixed_class == (successor == state))
                decoded_fixed += fixed_class
        AUDIT.check(decoded_fixed == row.fixed)
        AUDIT.check(decoded_recurrent == row.recurrent)
        decoded_cycles = (decoded_recurrent - decoded_fixed) // 2
        AUDIT.check(decoded_fixed + 2 * decoded_cycles == decoded_recurrent)
        if total <= 30:
            AUDIT.check(decoded_fixed == predicted_fixed[total])
            AUDIT.check(decoded_cycles == predicted_cycles[total])
        if total == 30:
            weight_30_fixed = decoded_fixed
            weight_30_cycles = decoded_cycles
            weight_30_recurrent = decoded_recurrent

    wreath_cases, wreath_elements = verify_wreath_factor_rules()
    tag_initial, tag_reachable, tag_clean_pairs = verify_colored_tag_dynamics(30)
    AUDIT.check((weight_30_fixed, weight_30_cycles, weight_30_recurrent) == (59, 139, 337))
    lines.append(
        "FOCUS_CT1|partitions=all_n<=45"
        f"|states={wide_states}|periods={','.join(map(str, sorted(wide_periods)))}"
        f"|max_tail={wide_max_tail}"
        f"|first_tail_weights={','.join(f'{key}:{first_weight_by_tail[key]}' for key in sorted(first_weight_by_tail))}"
        "|theorem=period_le_2,tail_le_2n,recurrent_decoder"
        f"|n30_fixed_cycles_recurrent={weight_30_fixed},{weight_30_cycles},{weight_30_recurrent}"
        f"|fibre_cells_n<=30={fibre_cells}|wreath_cases={wreath_cases}"
        f"|wreath_elements={wreath_elements}"
        f"|tag_initial_n<=30={tag_initial}|tag_reachable={tag_reachable}"
        f"|two_clean_pairs={tag_clean_pairs}|PASS"
    )
    return lines, total_states, len(TYPE_SYSTEMS)


# ---------------------------------------------------------------------------
# Boolean-relation semigroup maps


def relation_transpose(relation, order):
    out = 0
    for row in range(order):
        for column in range(order):
            if (relation >> (row * order + column)) & 1:
                out |= 1 << (column * order + row)
    return out


def relation_product(left, right, order):
    row_mask = (1 << order) - 1
    left_rows = [
        (left >> (row * order)) & row_mask for row in range(order)
    ]
    right_columns = [
        sum(
            ((right >> (row * order + column)) & 1) << row
            for row in range(order)
        )
        for column in range(order)
    ]
    out = 0
    for row in range(order):
        for column in range(order):
            if left_rows[row] & right_columns[column]:
                out |= 1 << (row * order + column)
    return out


def relation_update(relation, order, kind):
    converse = relation_transpose(relation, order)
    left_support = relation_product(relation, converse, order)
    right_support = relation_product(converse, relation, order)
    if kind == 1:
        return relation_product(left_support, relation, order)
    if kind == 2:
        return left_support & right_support
    if kind == 3:
        return left_support | right_support
    if kind == 4:
        return relation & left_support
    if kind == 5:
        return relation & (left_support | right_support)
    if kind == 6:
        return relation_product(left_support, right_support, order)
    raise ValueError(kind)


def bipartite_adjacency(relation, order):
    adjacency = [set() for _ in range(2 * order)]
    for left in range(order):
        for right in range(order):
            if (relation >> (left * order + right)) & 1:
                adjacency[left].add(order + right)
                adjacency[order + right].add(left)
    return adjacency


def difunctional_endpoint(relation, order):
    adjacency = bipartite_adjacency(relation, order)
    remaining = set(range(2 * order))
    out = 0
    while remaining:
        root = min(remaining)
        component = {root}
        queue = deque([root])
        while queue:
            vertex = queue.popleft()
            for neighbor in adjacency[vertex]:
                if neighbor not in component:
                    component.add(neighbor)
                    queue.append(neighbor)
        remaining -= component
        left = [vertex for vertex in component if vertex < order]
        right = [vertex - order for vertex in component if vertex >= order]
        if left and right:
            for row in left:
                for column in right:
                    out |= 1 << (row * order + column)
    return out


def maximum_cross_distance(relation, order):
    adjacency = bipartite_adjacency(relation, order)
    maximum = 0
    for source in range(order):
        distance = {source: 0}
        queue = deque([source])
        while queue:
            vertex = queue.popleft()
            for neighbor in adjacency[vertex]:
                if neighbor not in distance:
                    distance[neighbor] = distance[vertex] + 1
                    queue.append(neighbor)
        for target in range(order, 2 * order):
            if target in distance:
                maximum = max(maximum, distance[target])
    return maximum


RELATION_SYSTEMS = (
    (
        "SR1", "binary relations; R R^T R regularization", 1,
        "KILL_INTERNAL_ASYNC_BR1_AND_DIFUNCTIONAL_OWNER",
    ),
    (
        "SR2", "binary relations; meet of left/right Green supports", 2,
        "KILL_GREEN_SUPPORT_COLLAPSE",
    ),
    (
        "SR3", "binary relations; join of left/right Green supports", 3,
        "KILL_GREEN_SUPPORT_COLLAPSE",
    ),
    (
        "SR4", "binary relations; left-support erosion R intersect RR^T", 4,
        "KILL_SUPPORT_EROSION_SHALLOW",
    ),
    (
        "SR5", "binary relations; two-sided-support erosion", 5,
        "KILL_SUPPORT_EROSION_SHALLOW",
    ),
    (
        "SR6", "binary relations; product of left/right Green supports", 6,
        "KILL_GREEN_PRODUCT_COLLAPSE",
    ),
)


def run_relation_systems():
    lines = []
    total_states = 0
    for handle, carrier, kind, decision in RELATION_SYSTEMS:
        summaries = []
        for order in (2, 3, 4):
            states = range(1 << (order * order))
            summaries.append(
                functional_summary(
                    states,
                    lambda relation, order=order, kind=kind: relation_update(
                        relation, order, kind
                    ),
                )
            )
        total_states += sum(row.states for row in summaries)
        lines.append(summary_line(handle, carrier, summaries, decision))

    focus_states = 0
    depth_histogram = Counter()
    for order in (2, 3, 4):
        for relation in range(1 << (order * order)):
            focus_states += 1
            endpoint = difunctional_endpoint(relation, order)
            state = relation
            depth = 0
            while True:
                successor = relation_update(state, order, 1)
                if successor == state:
                    break
                AUDIT.check(depth <= order * order)
                state = successor
                depth += 1
            AUDIT.check(state == endpoint, (order, relation, state, endpoint))
            diameter = maximum_cross_distance(relation, order)
            predicted_depth = 0
            power = 1
            while power < diameter:
                power *= 3
                predicted_depth += 1
            AUDIT.check(depth == predicted_depth, (order, relation, depth, diameter))
            depth_histogram[depth] += 1
    lines.append(
        "FOCUS_SR1|all_square_relations_orders=2,3,4"
        f"|states={focus_states}"
        f"|depth_histogram={','.join(f'{key}:{depth_histogram[key]}' for key in sorted(depth_histogram))}"
        "|endpoint=bipartite_component_bicliques|depth=ceil_log3_cross_diameter|PASS"
    )
    return lines, total_states, len(RELATION_SYSTEMS)


# ---------------------------------------------------------------------------
# Full transformation monoids


def transformation_compose(left, right):
    return tuple(left[right[index]] for index in range(len(left)))


def transformation_update(state, kind):
    if kind == 1:
        left, right = state
        return (
            transformation_compose(
                transformation_compose(left, right), left
            ),
            transformation_compose(
                transformation_compose(right, left), right
            ),
        )
    left, middle, right = state
    if kind == 2:
        return (
            transformation_compose(left, middle),
            transformation_compose(middle, right),
            transformation_compose(right, left),
        )
    if kind == 3:
        return (
            transformation_compose(
                transformation_compose(left, middle), right
            ),
            transformation_compose(
                transformation_compose(middle, right), left
            ),
            transformation_compose(
                transformation_compose(right, left), middle
            ),
        )
    if kind == 4:
        return (
            transformation_compose(
                transformation_compose(left, middle), left
            ),
            transformation_compose(
                transformation_compose(middle, right), middle
            ),
            transformation_compose(
                transformation_compose(right, left), right
            ),
        )
    raise ValueError(kind)


TRANSFORMATION_SYSTEMS = (
    (
        "TM1", "full transformation monoid pairs; mutual sandwiches", 1,
        "KILL_SANDWICH_OWNER_NO_UNIFORM_SPINE",
    ),
    (
        "TM2", "full transformation monoid triples; cyclic adjacent products", 2,
        "KILL_LONG_PERIOD_PILOT_NO_THEOREM",
    ),
    (
        "TM3", "full transformation monoid triples; cyclic triple products", 3,
        "KILL_WORD_MAP_NO_FIBRE_LAW",
    ),
    (
        "TM4", "full transformation monoid triples; cyclic sandwiches", 4,
        "KILL_WORD_MAP_NO_FIBRE_LAW",
    ),
)


def all_transformations(order):
    return tuple(product(range(order), repeat=order))


def kernel_selector(transformation):
    order = len(transformation)
    return tuple(
        min(
            candidate
            for candidate in range(order)
            if transformation[candidate] == transformation[point]
        )
        for point in range(order)
    )


def run_transformation_systems():
    lines = []
    total_states = 0
    for handle, carrier, kind, decision in TRANSFORMATION_SYSTEMS:
        summaries = []
        for order in (2, 3):
            monoid = all_transformations(order)
            arity = 2 if kind == 1 else 3
            summaries.append(
                functional_summary(
                    product(monoid, repeat=arity),
                    lambda state, kind=kind: transformation_update(state, kind),
                )
            )
        total_states += sum(row.states for row in summaries)
        lines.append(summary_line(handle, carrier, summaries, decision))

    summaries = []
    for order in (2, 3, 4):
        monoid = all_transformations(order)
        summaries.append(functional_summary(monoid, kernel_selector))
        for transformation in monoid:
            image = kernel_selector(transformation)
            AUDIT.check(kernel_selector(image) == image)
            AUDIT.check(
                all(
                    (transformation[left] == transformation[right])
                    == (image[left] == image[right])
                    for left in range(order)
                    for right in range(order)
                )
            )
    total_states += sum(row.states for row in summaries)
    lines.append(
        summary_line(
            "TM5",
            "full transformation monoid; ordered kernel idempotent selector",
            summaries,
            "KILL_ORDER_DEPENDENT_ONE_STEP_NORMAL_FORM",
        )
    )
    return lines, total_states, len(TRANSFORMATION_SYSTEMS) + 1


# ---------------------------------------------------------------------------
# Two genuinely nonassociative Fano Steiner-quasigroup controls


def fano_product(left, right):
    # Nonzero vectors of F_2^3.  The diagonal is idempotent; off the diagonal
    # the third point on the Fano line is bitwise xor.
    return left if left == right else left ^ right


def fano_update(state, kind):
    left, middle, right = state
    if kind == 1:
        return (
            fano_product(left, middle),
            fano_product(middle, right),
            fano_product(right, left),
        )
    if kind == 2:
        return (
            fano_product(fano_product(left, middle), right),
            fano_product(fano_product(middle, right), left),
            fano_product(fano_product(right, left), middle),
        )
    raise ValueError(kind)


def run_fano_systems():
    lines = []
    total_states = 0
    specifications = (
        (
            "FQ1", "Fano Steiner quasigroup triples; cyclic edge products", 1,
            "KILL_FIXED_FANO_ACCIDENT",
        ),
        (
            "FQ2", "Fano Steiner quasigroup triples; cyclic associator products", 2,
            "KILL_FIXED_FANO_ACCIDENT",
        ),
    )
    for handle, carrier, kind, decision in specifications:
        states = tuple(product(range(1, 8), repeat=3))
        summary = functional_summary(
            states, lambda state, kind=kind: fano_update(state, kind)
        )
        total_states += summary.states
        lines.append(summary_line(handle, carrier, [summary], decision))

    # Check the literal quasigroup laws rather than merely trusting the table.
    for left in range(1, 8):
        row = [fano_product(left, right) for right in range(1, 8)]
        AUDIT.check(sorted(row) == list(range(1, 8)))
        AUDIT.check(fano_product(left, left) == left)
        for right in range(1, 8):
            AUDIT.check(fano_product(left, right) == fano_product(right, left))
            AUDIT.check(fano_product(left, fano_product(left, right)) == right)
    return lines, total_states, len(specifications)


def main():
    initial_assertions = AUDIT.assertions
    type_lines, type_states, type_count = run_type_systems()
    type_assertions = AUDIT.assertions - initial_assertions

    initial_assertions = AUDIT.assertions
    relation_lines, relation_states, relation_count = run_relation_systems()
    relation_assertions = AUDIT.assertions - initial_assertions

    initial_assertions = AUDIT.assertions
    transformation_lines, transformation_states, transformation_count = (
        run_transformation_systems()
    )
    transformation_assertions = AUDIT.assertions - initial_assertions

    initial_assertions = AUDIT.assertions
    fano_lines, fano_states, fano_count = run_fano_systems()
    fano_assertions = AUDIT.assertions - initial_assertions

    system_count = type_count + relation_count + transformation_count + fano_count
    state_count = type_states + relation_states + transformation_states + fano_states
    AUDIT.check(system_count >= 20)
    AUDIT.check(sum("PROMOTE_" in line for line in type_lines + relation_lines + transformation_lines + fano_lines) <= 2)

    print("NONDIVISOR_ALGEBRA_SCOUT_V1")
    for line in type_lines + relation_lines + transformation_lines + fano_lines:
        print(line)
    print(
        f"LEDGER|systems={system_count}|promotions=1|kills={system_count - 1}"
        f"|enumerated_parameter_states={state_count}"
        f"|type_assertions={type_assertions}"
        f"|relation_assertions={relation_assertions}"
        f"|transformation_assertions={transformation_assertions}"
        f"|fano_assertions={fano_assertions}"
        f"|assertions={AUDIT.assertions}|PASS"
    )
    print("EXACT_ARITHMETIC=python_integers_and_bitsets")
    print("FLOATING_POINT=none")
    print("SAMPLING=none")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
