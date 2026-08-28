#!/usr/bin/env python3
"""Exact controls for the finite-field adjacent-product process.

Only the Python standard library is used.  Prime fields F_2, F_3, F_5 and
the nonprime field F_4 are checked.  Elements of F_4 are encoded as a+bx,
where x^2=x+1 over F_2.
"""

from collections import Counter
from fractions import Fraction
from itertools import product
import math


def field_mul(q, a, b):
    if q in (2, 3, 5):
        return (a * b) % q
    if q == 4:
        a0, a1 = a & 1, (a >> 1) & 1
        b0, b1 = b & 1, (b >> 1) & 1
        c0 = a0 & b0
        c1 = (a0 & b1) ^ (a1 & b0)
        c2 = a1 & b1
        # x^2=x+1 in F_4.
        c0 ^= c2
        c1 ^= c2
        return c0 | (c1 << 1)
    raise ValueError(f"unsupported control field q={q}")


def observed_word(q, hidden):
    return tuple(field_mul(q, hidden[i], hidden[i + 1])
                 for i in range(len(hidden) - 1))


def avoids_forbidden(word):
    return all(not (word[i - 1] != 0 and word[i] == 0
                    and word[i + 1] != 0)
               for i in range(1, len(word) - 1))


def fiber_matrix_count(q, word):
    m = q - 1
    zero, nonzero = 1, m
    for symbol in word:
        if symbol == 0:
            zero, nonzero = zero + nonzero, m * zero
        else:
            zero, nonzero = 0, nonzero
    return zero + nonzero


def brute_fibers(q, n):
    counts = Counter()
    for hidden in product(range(q), repeat=n + 1):
        counts[observed_word(q, hidden)] += 1
    return counts


def language_recurrence(q, maximum):
    m = q - 1
    values = [1, q, q * q]
    while len(values) <= maximum:
        values.append(q * values[-1] - m * values[-2] + m * values[-3])
    return values


def generalized_fibonacci(q, maximum):
    m = q - 1
    values = [0, 1]
    while len(values) <= maximum:
        values.append(values[-1] + m * values[-2])
    return values


def check_field(q):
    # Nonzero multiplication must be a permutation in each argument.
    expected = set(range(1, q))
    for a in range(1, q):
        assert {field_mul(q, a, b) for b in range(1, q)} == expected


def check_words(q, maximum):
    recurrence = language_recurrence(q, maximum)
    support_counts = [1]
    for n in range(1, maximum + 1):
        fibers = brute_fibers(q, n)
        supported = set(fibers)
        legal = {word for word in product(range(q), repeat=n)
                 if avoids_forbidden(word)}
        assert supported == legal
        assert len(supported) == recurrence[n]
        for word, count in fibers.items():
            assert count == fiber_matrix_count(q, word)
        support_counts.append(len(supported))
    return support_counts


def check_contexts(q, maximum):
    m = q - 1
    fib = generalized_fibonacci(q, maximum + 1)
    values = []
    for r in range(1, maximum + 1):
        claimed = Fraction(m * fib[r - 1], q * fib[r + 1])
        observed = set()
        for a in range(1, q):
            for b in range(1, q):
                context = (a,) + (0,) * r
                numerator = fiber_matrix_count(q, context + (b,))
                denominator = q * fiber_matrix_count(q, context)
                exact = Fraction(numerator, denominator)
                assert exact == claimed
                observed.add(exact)
        assert observed == {claimed}
        values.append(claimed)
    assert all(values[i] != values[i + 1]
               for i in range(len(values) - 1))
    return values


def binary_entropy(value):
    if value <= 0.0 or value >= 1.0:
        return 0.0
    return -value * math.log(value) - (1.0 - value) * math.log(1.0 - value)


def entropy_series(q, terms=250):
    m = q - 1
    fib = generalized_fibonacci(q, terms + 1)
    mass = 0.0
    entropy = 0.0
    for r in range(terms):
        weight = (m * m / (q * q)) * (fib[r + 1] / (q ** r))
        alpha = 1.0 if r == 0 else m * fib[r - 1] / fib[r + 1]
        nonzero_probability = (m / q) * alpha
        conditional_entropy = binary_entropy(nonzero_probability)
        if m > 1:
            conditional_entropy += nonzero_probability * math.log(m)
        mass += weight
        entropy += weight * conditional_entropy
    assert abs(mass - 1.0) < 1e-13
    return entropy, mass


def perron_root(q):
    m = q - 1
    lo, hi = 1.0, float(q)
    def polynomial(x):
        return x ** 3 - q * x ** 2 + m * x - m
    # The largest root lies between 1 and q.  Bisection is taken on the
    # final sign change nearest q, where the cubic is increasing.
    grid = [1.0 + (q - 1.0) * i / 10000 for i in range(10001)]
    brackets = []
    previous_x, previous_y = grid[0], polynomial(grid[0])
    for x in grid[1:]:
        y = polynomial(x)
        if previous_y == 0.0 or previous_y * y <= 0.0:
            brackets.append((previous_x, x))
        previous_x, previous_y = x, y
    lo, hi = brackets[-1]
    for _ in range(100):
        mid = (lo + hi) / 2.0
        if polynomial(lo) * polynomial(mid) <= 0.0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2.0


def main():
    settings = {2: 9, 3: 6, 4: 5, 5: 4}
    print("finite-field adjacent-product exact controls")
    for q, maximum in settings.items():
        check_field(q)
        counts = check_words(q, maximum)
        contexts = check_contexts(q, min(8, maximum + 2))
        entropy, mass = entropy_series(q)
        topological = math.log(perron_root(q))
        assert entropy < topological
        print(f"q={q}: L_0..L_{maximum}={counts}")
        print(f"q={q}: next fixed-nonzero probabilities="
              + ", ".join(str(value) for value in contexts))
        print(f"q={q}: age_mass={mass:.15f}, "
              f"h_mu={entropy:.15f}, h_top={topological:.15f}")
    print("ALL EXACT CONTROLS PASSED")


if __name__ == "__main__":
    main()
