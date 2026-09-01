#!/usr/bin/env python3
"""Exact audit for rank-feedback splitting of finite abelian p-groups.

The carrier is the set of integer partitions: a partition
``lambda=(a_1,...,a_r)`` represents ``direct_sum_i C_(p^a_i)``.  The
rank-feedback update is the type of ``p^r G direct_sum G[p^r]``.  All
arithmetic in this file is exact and the program has no dependencies beyond
the Python standard library.

Finite enumeration is a falsification control.  It is not an all-weight
proof and it is not novelty, priority, or ownership evidence.
"""

from collections import Counter
from functools import lru_cache


MAX_WEIGHT = 50
FIBRE_MAX_WEIGHT = 35
REPORT_WEIGHTS = frozenset((1, 2, 3, 4, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50))


class Audit:
    def __init__(self):
        self.assertions = 0

    def check(self, condition, message="assertion failed"):
        self.assertions += 1
        if not condition:
            raise AssertionError(message)


AUDIT = Audit()


@lru_cache(maxsize=None)
def partitions(n, cap):
    """All decreasing partitions of n with largest part at most cap."""
    if n == 0:
        return ((),)
    cap = min(n, cap)
    answer = []
    for first in range(cap, 0, -1):
        for tail in partitions(n - first, first):
            answer.append((first,) + tail)
    return tuple(answer)


def partitions_of(n):
    return partitions(n, n)


def split_count(partition):
    rank = len(partition)
    return sum(part > rank for part in partition)


def rank_feedback_step(partition):
    """Type-coordinate form of G -> p^d(G)G direct_sum G[p^d(G)]."""
    rank = len(partition)
    output = []
    for exponent in partition:
        if exponent <= rank:
            output.append(exponent)
        else:
            output.extend((rank, exponent - rank))
    return tuple(sorted(output, reverse=True))


def factorwise_group_type(partition):
    """Independently collect image and kernel cyclic exponents."""
    rank = len(partition)
    image_exponents = []
    torsion_exponents = []
    for exponent in partition:
        image_exponent = max(exponent - rank, 0)
        torsion_exponent = min(exponent, rank)
        if image_exponent:
            image_exponents.append(image_exponent)
        if torsion_exponent:
            torsion_exponents.append(torsion_exponent)
    return tuple(sorted(image_exponents + torsion_exponents, reverse=True))


def is_fixed(partition):
    return not partition or partition[0] <= len(partition)


def triangular(index):
    return index * (index + 1) // 2


def sharp_clock(weight):
    """Largest d with T_d < weight."""
    depth = 0
    while triangular(depth + 1) < weight:
        depth += 1
    return depth


def trace_to_fixed(partition):
    """Return depth together with the ranks and split counts used en route."""
    state = partition
    seen = set()
    ranks = []
    split_counts = []
    while not is_fixed(state):
        AUDIT.check(state not in seen, (partition, state, "nonfixed cycle"))
        seen.add(state)
        rank = len(state)
        count = split_count(state)
        target = rank_feedback_step(state)
        AUDIT.check(count > 0, (state, "nonfixed state has no split"))
        AUDIT.check(len(target) == rank + count, (state, target, "rank increment"))
        AUDIT.check(sum(target) == sum(state), (state, target, "weight drift"))
        AUDIT.check(len(target) > rank, (state, target, "rank did not rise"))
        ranks.append(rank)
        split_counts.append(count)
        state = target
    AUDIT.check(is_fixed(state), (partition, state, "failed to terminate"))
    return len(ranks), tuple(ranks), tuple(split_counts), state


def bounded_choice_coefficient(multiplicities, maximum_part, degree):
    """Coefficient of u^degree in product_j (1+...+u^m_j)."""
    coefficients = [1] + [0] * degree
    for part in range(1, maximum_part + 1):
        next_coefficients = [0] * (degree + 1)
        bound = multiplicities.get(part, 0)
        for old_degree, value in enumerate(coefficients):
            if value == 0:
                continue
            for take in range(min(bound, degree - old_degree) + 1):
                next_coefficients[old_degree + take] += value
        coefficients = next_coefficients
    return coefficients[degree]


def fibre_formula(target):
    """The theorem's sum over every possible source rank."""
    length = len(target)
    multiplicities = Counter(target)
    answer = 0
    for rank in range((length + 1) // 2, length + 1):
        split_parts = length - rank
        if multiplicities[rank] < split_parts:
            continue
        residual = multiplicities.copy()
        residual[rank] -= split_parts
        forced_high = sum(
            count for part, count in residual.items() if part > rank
        )
        if forced_high > split_parts:
            continue
        degree = split_parts - forced_high
        answer += bounded_choice_coefficient(residual, rank, degree)
    return answer


def image_criterion(target):
    """Existential marker/large-remainder criterion from the theorem."""
    length = len(target)
    multiplicities = Counter(target)
    for rank in range((length + 1) // 2, length + 1):
        split_parts = length - rank
        if multiplicities[rank] < split_parts:
            continue
        if sum(count for part, count in multiplicities.items() if part > rank) <= split_parts:
            return True
    return False


@lru_cache(maxsize=None)
def gaussian_binomial(n, k):
    """Coefficients through MAX_WEIGHT using the q-Pascal recurrence."""
    if k < 0 or k > n:
        return (0,) * (MAX_WEIGHT + 1)
    if k == 0 or k == n:
        return (1,) + (0,) * MAX_WEIGHT
    left = gaussian_binomial(n - 1, k)
    right = gaussian_binomial(n - 1, k - 1)
    shift = n - k
    output = list(left)
    for degree in range(shift, MAX_WEIGHT + 1):
        output[degree] += right[degree - shift]
    return tuple(output)


def audit_literal_cyclic_factors():
    """Construct kernels and images in small literal cyclic p-groups."""
    cells = 0
    elements = 0
    for prime in (2, 3):
        for exponent in range(1, 9):
            modulus = prime ** exponent
            elements += modulus
            universe = range(modulus)
            for rank in range(0, 11):
                cells += 1
                multiplier = prime ** rank
                image = {multiplier * value % modulus for value in universe}
                torsion = {
                    value for value in universe if multiplier * value % modulus == 0
                }
                truncated_rank = min(rank, exponent)
                expected_image_generator = prime ** truncated_rank
                expected_torsion_generator = prime ** (exponent - truncated_rank)
                expected_image = {
                    expected_image_generator * value
                    for value in range(prime ** (exponent - truncated_rank))
                }
                expected_torsion = {
                    expected_torsion_generator * value
                    for value in range(prime ** truncated_rank)
                }
                AUDIT.check(image == expected_image, (prime, exponent, rank, "image"))
                AUDIT.check(torsion == expected_torsion, (prime, exponent, rank, "kernel"))
                AUDIT.check(
                    len(image) == prime ** max(exponent - rank, 0),
                    (prime, exponent, rank, "image order"),
                )
                AUDIT.check(
                    len(torsion) == prime ** min(exponent, rank),
                    (prime, exponent, rank, "kernel order"),
                )
                AUDIT.check(len(image) * len(torsion) == modulus, "exact sequence")
    return cells, elements


def fixed_ogf_coefficients():
    coefficients = [0] * (MAX_WEIGHT + 1)
    coefficients[0] = 1
    for rank in range(1, MAX_WEIGHT + 1):
        rectangle = gaussian_binomial(2 * rank - 1, rank)
        for degree in range(0, MAX_WEIGHT - rank + 1):
            coefficients[degree + rank] += rectangle[degree]
    return tuple(coefficients)


def main():
    print("RANK_FEEDBACK_PGROUP_SPLIT_V1")
    cyclic_cells, cyclic_elements = audit_literal_cyclic_factors()
    print(
        f"literal_cyclic_cells={cyclic_cells}|base_group_elements={cyclic_elements}"
        "|primes=2,3|exponents=1..8|feedback_ranks=0..10"
    )

    total_states = 0
    fixed_counts = [1] + [0] * MAX_WEIGHT
    fibres_by_weight = {}
    statistics = {}

    AUDIT.check(rank_feedback_step(()) == (), "empty convention")
    AUDIT.check(is_fixed(()), "empty convention is not fixed")

    for weight in range(1, MAX_WEIGHT + 1):
        states = partitions_of(weight)
        total_states += len(states)
        fibres = Counter()
        depth_histogram = Counter()
        deepest_count = 0
        deepest_witness = None
        maximum_depth = -1

        for partition in states:
            rank = len(partition)
            count = split_count(partition)
            target = rank_feedback_step(partition)
            fibres[target] += 1

            AUDIT.check(sum(target) == weight, (partition, target, "weight"))
            AUDIT.check(target == factorwise_group_type(partition), "group/type identity")
            AUDIT.check(len(target) == rank + count, "rank formula")
            AUDIT.check((target == partition) == is_fixed(partition), "fixed criterion")
            AUDIT.check((count == 0) == is_fixed(partition), "split criterion")

            depth, ranks, split_counts, terminal = trace_to_fixed(partition)
            depth_histogram[depth] += 1
            AUDIT.check(is_fixed(terminal), "terminal is not fixed")
            AUDIT.check(len(ranks) == len(split_counts) == depth, "trace lengths")
            AUDIT.check(
                all(ranks[index + 1] == ranks[index] + split_counts[index]
                    for index in range(max(0, depth - 1))),
                "rank recurrence",
            )
            marker_budget = rank + sum(
                count_at_time * rank_at_time
                for rank_at_time, count_at_time in zip(ranks, split_counts)
            )
            AUDIT.check(weight >= marker_budget, (partition, "marker budget"))
            AUDIT.check(
                weight >= rank * (depth + 1) + depth * (depth - 1) // 2,
                (partition, "pointwise triangular bound"),
            )

            if depth > maximum_depth:
                maximum_depth = depth
                deepest_count = 1
                deepest_witness = partition
            elif depth == maximum_depth:
                deepest_count += 1

        fixed_counts[weight] = depth_histogram[0]
        predicted = sharp_clock(weight)
        AUDIT.check(maximum_depth == predicted, (weight, maximum_depth, predicted))
        AUDIT.check(deepest_count == 1, (weight, deepest_count, "deepest count"))
        AUDIT.check(deepest_witness == (weight,), (weight, deepest_witness))

        source = (weight,)
        for time in range(predicted + 1):
            expected = tuple(
                sorted((weight - triangular(time),) + tuple(range(time, 0, -1)),
                       reverse=True)
            )
            AUDIT.check(source == expected, (weight, time, source, expected))
            if time < predicted:
                source = rank_feedback_step(source)
        AUDIT.check(is_fixed(source), (weight, source, "deepest source terminal"))

        if weight <= FIBRE_MAX_WEIGHT:
            fibres_by_weight[weight] = fibres

        statistics[weight] = (
            len(states),
            fixed_counts[weight],
            len(fibres),
            max(fibres.values()),
            maximum_depth,
            dict(sorted(depth_histogram.items())),
        )
        if weight in REPORT_WEIGHTS:
            state_count, fixed_count, image_count, maximum_fibre, depth, histogram = statistics[weight]
            print(
                f"n={weight}|states={state_count}|fixed={fixed_count}|image={image_count}"
                f"|max_fibre={maximum_fibre}|max_depth={depth}|deepest={(weight,)}"
                f"|depth_hist={histogram}"
            )

    ogf = fixed_ogf_coefficients()
    for weight in range(MAX_WEIGHT + 1):
        AUDIT.check(ogf[weight] == fixed_counts[weight], (weight, ogf[weight], fixed_counts[weight]))

    total_targets = 0
    zero_fibre_targets = 0
    for weight in range(1, FIBRE_MAX_WEIGHT + 1):
        actual = fibres_by_weight[weight]
        formula_sum = 0
        for target in partitions_of(weight):
            total_targets += 1
            predicted_fibre = fibre_formula(target)
            formula_sum += predicted_fibre
            actual_fibre = actual[target]
            zero_fibre_targets += actual_fibre == 0
            AUDIT.check(
                predicted_fibre == actual_fibre,
                (weight, target, predicted_fibre, actual_fibre, "fibre"),
            )
            AUDIT.check(
                image_criterion(target) == (actual_fibre > 0),
                (weight, target, actual_fibre, "image criterion"),
            )
            AUDIT.check(
                (predicted_fibre > 0) == image_criterion(target),
                (weight, target, predicted_fibre, "formula positivity"),
            )
        AUDIT.check(formula_sum == len(partitions_of(weight)), (weight, "fibre mass"))

    state_50, fixed_50, image_50, max_fibre_50, depth_50, hist_50 = statistics[50]
    AUDIT.check(
        (state_50, fixed_50, image_50, max_fibre_50, depth_50)
        == (204226, 106864, 120872, 31, 9),
        "frozen n=50 control changed",
    )
    AUDIT.check(
        hist_50
        == {0: 106864, 1: 74772, 2: 17910, 3: 3690, 4: 767,
            5: 170, 6: 40, 7: 10, 8: 2, 9: 1},
        "frozen n=50 depth histogram changed",
    )

    print(f"TOTAL_PARTITION_STATES={total_states}")
    print(f"TOTAL_FIBRE_TARGETS={total_targets}")
    print(f"ZERO_FIBRE_TARGETS={zero_fibre_targets}")
    print(f"FIXED_OGF_COEFFICIENTS_CHECKED={MAX_WEIGHT + 1}")
    print(f"MAX_WEIGHT={MAX_WEIGHT}")
    print(f"FIBRE_MAX_WEIGHT={FIBRE_MAX_WEIGHT}")
    print(f"TOTAL_ASSERTIONS={AUDIT.assertions}")
    print("EXACT_ARITHMETIC=python_integers")
    print("FLOATING_POINT=none")
    print("SAMPLING=none")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
