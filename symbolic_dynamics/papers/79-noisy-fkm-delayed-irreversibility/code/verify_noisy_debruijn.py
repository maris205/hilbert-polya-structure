#!/usr/bin/env python3
"""Exact finite controls for noisy FKM delayed irreversibility.

The script uses only Python's standard library.  Probability calculations for
the reversal inequalities are exact Fractions; floating point is used only
for the optional Shannon-entropy sandwich.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from math import log, log2


def divisors(number):
    return [candidate for candidate in range(1, number + 1) if number % candidate == 0]


def rotations(word):
    return [word[offset:] + word[:offset] for offset in range(1, len(word))]


def is_lyndon(word):
    return all(word < rotation for rotation in rotations(word))


def explicit_lyndon_concatenation(order):
    """Definition-level construction, used as an independent FKM check."""
    words = []
    for length in divisors(order):
        for word in product((0, 1), repeat=length):
            if is_lyndon(word):
                words.append(word)
    words.sort()
    return tuple(symbol for word in words for symbol in word)


def fkm_binary_cycle(order):
    """Standard FKM recursion for the binary lexicographically least cycle."""
    alphabet_size = 2
    work = [0] * (alphabet_size * order + 1)
    sequence = []

    def visit(position, period):
        if position > order:
            if order % period == 0:
                sequence.extend(work[1 : period + 1])
            return
        work[position] = work[position - period]
        visit(position + 1, period)
        for digit in range(work[position - period] + 1, alphabet_size):
            work[position] = digit
            visit(position + 1, position)

    visit(1, 1)
    return tuple(sequence)


def cyclic_block(sequence, start, length):
    size = len(sequence)
    return tuple(sequence[(start + offset) % size] for offset in range(length))


def cyclic_blocks(sequence, length):
    return [cyclic_block(sequence, start, length) for start in range(len(sequence))]


def noisy_law(sequence, length, epsilon):
    """Observed length-law after independent BSC emissions, exactly."""
    clean_blocks = cyclic_blocks(sequence, length)
    phase_count = len(sequence)
    law = {}
    for output in product((0, 1), repeat=length):
        probability = Fraction(0)
        for clean in clean_blocks:
            distance = sum(source != target for source, target in zip(clean, output))
            probability += epsilon**distance * (1 - epsilon) ** (length - distance)
        law[output] = probability / phase_count
    assert sum(law.values(), Fraction(0)) == 1
    return law


def reversal_differences(law):
    return {word: probability - law[word[::-1]] for word, probability in law.items()}


def squared_l2_gap(law):
    return sum(value * value for value in reversal_differences(law).values())


def total_variation_gap(law):
    return sum(abs(value) for value in reversal_differences(law).values()) / 2


def binary_entropy(epsilon):
    value = float(epsilon)
    if value in (0.0, 1.0):
        return 0.0
    return -value * log2(value) - (1.0 - value) * log2(1.0 - value)


def shannon_entropy(law):
    return -sum(float(probability) * log2(float(probability))
                for probability in law.values() if probability)


def is_rotation(word, candidate):
    if len(word) != len(candidate):
        return False
    doubled = word + word
    return any(tuple(doubled[start : start + len(word)]) == candidate
               for start in range(len(word)))


def check_fkm_definition_and_debruijn():
    checks = 0
    minimum_shift_distances = {}
    for order in range(1, 11):
        cycle = fkm_binary_cycle(order)
        assert cycle == explicit_lyndon_concatenation(order)
        assert len(cycle) == 2**order
        order_counts = Counter(cyclic_blocks(cycle, order))
        assert len(order_counts) == 2**order
        assert set(order_counts.values()) == {1}

        for length in range(1, order + 1):
            counts = Counter(cyclic_blocks(cycle, length))
            assert len(counts) == 2**length
            assert set(counts.values()) == {2 ** (order - length)}
            checks += 1

        distances = [
            sum(cycle[index] != cycle[(index + shift) % len(cycle)]
                for index in range(len(cycle)))
            for shift in range(1, len(cycle))
        ]
        assert distances and min(distances) > 0
        minimum_shift_distances[order] = min(distances)

    return checks, minimum_shift_distances


def check_fkm_witness():
    checks = 0
    samples = []
    for order in range(3, 13):
        cycle = fkm_binary_cycle(order)
        prefix = (0,) * order + (1,) + (0,) * (order - 2) + (1, 1)
        assert cycle[: len(prefix)] == prefix

        witness = (0,) * (order - 1) + (1, 0)
        reverse = witness[::-1]
        support = set(cyclic_blocks(cycle, order + 1))
        assert witness in support
        assert reverse not in support

        clean_law = Counter(cyclic_blocks(cycle, order + 1))
        assert clean_law[witness] == 1
        assert clean_law[reverse] == 0
        checks += 1
        if order <= 6:
            samples.append((order, "".join(map(str, witness)), "".join(map(str, reverse))))
    return checks, samples


def check_noisy_local_uniformity():
    checks = 0
    for order in range(3, 7):
        cycle = fkm_binary_cycle(order)
        for epsilon in (Fraction(1, 5), Fraction(1, 2), Fraction(4, 5)):
            for length in range(1, order + 1):
                law = noisy_law(cycle, length, epsilon)
                assert set(law.values()) == {Fraction(1, 2**length)}
                checks += 1
    return checks


def check_reversal_bounds():
    checks = 0
    samples = []
    epsilon_values = (
        Fraction(0),
        Fraction(1, 5),
        Fraction(1, 3),
        Fraction(1, 2),
        Fraction(4, 5),
        Fraction(1),
    )
    for order in range(3, 9):
        cycle = fkm_binary_cycle(order)
        length = order + 1
        for epsilon in epsilon_values:
            law = noisy_law(cycle, length, epsilon)
            gap2 = squared_l2_gap(law)
            tv_gap = total_variation_gap(law)
            channel_factor = abs(1 - 2 * epsilon) ** length
            l2_lower_squared = Fraction(2, 2 ** (2 * order)) * channel_factor**2
            tv_lower = Fraction(1, 2**order) * channel_factor

            if epsilon == Fraction(1, 2):
                assert gap2 == 0
                assert tv_gap == 0
                assert set(law.values()) == {Fraction(1, 2**length)}
            else:
                assert gap2 >= l2_lower_squared > 0
                assert tv_gap >= tv_lower > 0
            checks += 1

            if order in (3, 5, 8) and epsilon in (Fraction(1, 5), Fraction(4, 5)):
                samples.append(
                    (order, epsilon, gap2, l2_lower_squared, tv_gap, tv_lower)
                )
    return checks, samples


def check_full_support_and_periodic_covariance():
    checks = 0
    samples = []
    for order in range(3, 9):
        cycle = fkm_binary_cycle(order)
        size = len(cycle)
        signs = [1 if bit == 0 else -1 for bit in cycle]
        assert sum(signs) == 0
        assert sum(signs[index] * signs[(index + size) % size]
                   for index in range(size)) == size

        for epsilon in (Fraction(1, 5), Fraction(1, 3), Fraction(4, 5)):
            law = noisy_law(cycle, order + 1, epsilon)
            assert all(probability > 0 for probability in law.values())
            covariance = (1 - 2 * epsilon) ** 2
            assert covariance > 0
            checks += 1
            if order == 5:
                samples.append((epsilon, covariance))
    return checks, samples


def check_phase_separation_and_drift():
    checks = 0
    samples = []
    for order in range(3, 11):
        cycle = fkm_binary_cycle(order)
        size = len(cycle)
        distances = []
        for shift in range(1, size):
            distance = sum(cycle[index] != cycle[(index + shift) % size]
                           for index in range(size))
            assert distance > 0
            distances.append(distance)

        minimum_distance = min(distances)
        for epsilon in (Fraction(1, 5), Fraction(1, 3), Fraction(4, 5)):
            value = float(epsilon)
            per_symbol_drift_lower = (
                minimum_distance
                * (1.0 - 2.0 * value)
                * log((1.0 - value) / value)
                / size
            )
            assert per_symbol_drift_lower > 0.0
            checks += 1
            if order in (3, 6, 10) and epsilon == Fraction(1, 5):
                samples.append((order, minimum_distance, per_symbol_drift_lower))
    return checks, samples


def check_endpoint_markov_and_small_order_reversibility():
    checks = 0
    for order in range(1, 9):
        cycle = fkm_binary_cycle(order)
        next_symbols = defaultdict(set)
        for start in range(len(cycle)):
            context = cyclic_block(cycle, start, max(0, order - 1))
            following = cycle[(start + max(0, order - 1)) % len(cycle)]
            next_symbols[context].add(following)
        if order >= 2:
            assert all(symbols == {0, 1} for symbols in next_symbols.values())
        checks += 1

    for order in (1, 2):
        cycle = fkm_binary_cycle(order)
        assert is_rotation(cycle, cycle[::-1])
        for epsilon in (Fraction(0), Fraction(1, 5), Fraction(1, 2), Fraction(1)):
            for length in range(1, 2 * len(cycle) + 3):
                law = noisy_law(cycle, length, epsilon)
                assert squared_l2_gap(law) == 0
                checks += 1
    return checks


def check_entropy_sandwich():
    checks = 0
    samples = []
    tolerance = 1e-10
    for order in (3, 4):
        cycle = fkm_binary_cycle(order)
        for epsilon in (Fraction(1, 5), Fraction(4, 5)):
            rate = binary_entropy(epsilon)
            for length in range(1, 11):
                law = noisy_law(cycle, length, epsilon)
                entropy = shannon_entropy(law)
                lower = length * rate
                upper = lower + order
                assert entropy + tolerance >= lower
                assert entropy <= upper + tolerance
                if length <= order:
                    assert abs(entropy - length) < tolerance
                checks += 1
            final_law = noisy_law(cycle, 10, epsilon)
            residual = shannon_entropy(final_law) - 10 * rate
            samples.append((order, epsilon, residual))
    return checks, samples


def main():
    definition_checks, shift_distances = check_fkm_definition_and_debruijn()
    witness_checks, witness_samples = check_fkm_witness()
    uniformity_checks = check_noisy_local_uniformity()
    reversal_checks, reversal_samples = check_reversal_bounds()
    covariance_checks, covariance_samples = check_full_support_and_periodic_covariance()
    phase_checks, phase_samples = check_phase_separation_and_drift()
    endpoint_checks = check_endpoint_markov_and_small_order_reversibility()
    entropy_checks, entropy_samples = check_entropy_sandwich()

    total = sum(
        (
            definition_checks,
            witness_checks,
            uniformity_checks,
            reversal_checks,
            covariance_checks,
            phase_checks,
            endpoint_checks,
            entropy_checks,
        )
    )
    print("PASS noisy FKM delayed-irreversibility controls")
    print(f"total grouped assertions: {total}")
    print(f"definition/de Bruijn groups: {definition_checks}")
    print(f"FKM witness groups: {witness_checks}")
    print(f"noisy local-uniformity groups: {uniformity_checks}")
    print(f"exact reversal-bound groups: {reversal_checks}")
    print(f"support/covariance groups: {covariance_checks}")
    print(f"phase-separation/drift groups: {phase_checks}")
    print(f"endpoint/small-order groups: {endpoint_checks}")
    print(f"entropy-sandwich groups: {entropy_checks}")
    print("minimum nontrivial cyclic-shift Hamming distances:")
    print(shift_distances)
    print("witness samples (k, word, reverse):")
    for row in witness_samples:
        print(row)
    print("reversal samples")
    print("(k, epsilon, exact l2^2, theorem l2^2 lower, exact TV, theorem TV lower):")
    for row in reversal_samples:
        print(row)
    print("periodic covariance samples (epsilon, covariance):")
    for row in covariance_samples:
        print(row)
    print("phase drift samples (k, min Hamming distance, drift per symbol):")
    for row in phase_samples:
        print(row)
    print("finite entropy residual samples H_10 - 10 h_b(epsilon):")
    for row in entropy_samples:
        print(row)


if __name__ == "__main__":
    main()
