#!/usr/bin/env python3
"""Exact finite controls for noisy FKM delayed irreversibility."""

from collections import Counter
from fractions import Fraction
from itertools import product


def fkm_binary_cycle(order):
    alphabet_size = 2
    work = [0] * (alphabet_size * order + 1)
    sequence = []

    def visit(t, period):
        if t > order:
            if order % period == 0:
                sequence.extend(work[1 : period + 1])
            return
        work[t] = work[t - period]
        visit(t + 1, period)
        for digit in range(work[t - period] + 1, alphabet_size):
            work[t] = digit
            visit(t + 1, t)

    visit(1, 1)
    return tuple(sequence)


def cyclic_blocks(sequence, length):
    size = len(sequence)
    return [tuple(sequence[(start + offset) % size] for offset in range(length)) for start in range(size)]


def noisy_law(clean_blocks, epsilon):
    length = len(clean_blocks[0])
    denominator = len(clean_blocks)
    law = {}
    for output in product((0, 1), repeat=length):
        probability = Fraction(0)
        for clean in clean_blocks:
            distance = sum(a != b for a, b in zip(clean, output))
            probability += epsilon**distance * (1 - epsilon) ** (length - distance)
        law[output] = probability / denominator
    assert sum(law.values()) == 1
    return law


def squared_reversal_gap(law):
    return sum((probability - law[word[::-1]]) ** 2 for word, probability in law.items())


def main():
    structural_checks = 0
    exact_noise_checks = 0
    epsilon = Fraction(1, 5)
    sample = []
    for order in range(3, 13):
        cycle = fkm_binary_cycle(order)
        assert len(cycle) == 2**order
        for length in range(1, order + 1):
            counts = Counter(cyclic_blocks(cycle, length))
            assert len(counts) == 2**length
            assert set(counts.values()) == {2 ** (order - length)}
            structural_checks += 1
        witness = (0,) * (order - 1) + (1, 0)
        reverse = witness[::-1]
        support = set(cyclic_blocks(cycle, order + 1))
        assert witness in support
        assert reverse not in support
        structural_checks += 1

        if order <= 8:
            clean = cyclic_blocks(cycle, order + 1)
            law = noisy_law(clean, epsilon)
            gap2 = squared_reversal_gap(law)
            lower2 = Fraction(2, 2 ** (2 * order)) * (1 - 2 * epsilon) ** (2 * (order + 1))
            assert gap2 >= lower2 > 0
            exact_noise_checks += 1
            sample.append((order, gap2, lower2))

    assert fkm_binary_cycle(3) == (0, 0, 0, 1, 0, 1, 1, 1)
    print(f"PASS local-uniformity/FKM-witness checks: {structural_checks}")
    print(f"PASS exact BSC reversal-gap checks at epsilon=1/5: {exact_noise_checks}")
    print("sample (k, exact squared gap, theorem lower bound):")
    for row in sample[:4]:
        print(row)


if __name__ == "__main__":
    main()
