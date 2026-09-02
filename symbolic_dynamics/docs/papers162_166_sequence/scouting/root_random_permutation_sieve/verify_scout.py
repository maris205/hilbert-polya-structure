#!/usr/bin/env python3
"""Exact checks for the random-permutation fixed-point sieve."""

from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import permutations
from math import comb, factorial


ASSERTIONS = 0


def check(condition, message="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def subsets(n):
    return range(1 << n)


def popcount(mask):
    return mask.bit_count()


def fixed_mask(permutation):
    mask = 0
    for i, value in enumerate(permutation):
        if i == value:
            mask |= 1 << i
    return mask


def cycle_count(permutation):
    n = len(permutation)
    seen = [False] * n
    cycles = 0
    for start in range(n):
        if not seen[start]:
            cycles += 1
            value = start
            while not seen[value]:
                seen[value] = True
                value = permutation[value]
    return cycles


def one_step_matrix(n):
    size = 1 << n
    matrix = [[0] * size for _ in range(size)]
    marked = [[defaultdict(int) for _ in range(size)] for _ in range(size)]
    permutation_data = []
    for permutation in permutations(range(n)):
        permutation_data.append((fixed_mask(permutation), cycle_count(permutation)))
    for source in subsets(n):
        for fixed, cycles in permutation_data:
            target = source & fixed
            matrix[source][target] += 1
            marked[source][target][cycles] += 1
    return matrix, marked


def matrix_multiply(left, right):
    n = len(left)
    answer = [[0] * n for _ in range(n)]
    for i in range(n):
        for k, value in enumerate(left[i]):
            if value:
                for j, other in enumerate(right[k]):
                    if other:
                        answer[i][j] += value * other
    return answer


def identity_matrix(n):
    answer = [[0] * n for _ in range(n)]
    for i in range(n):
        answer[i][i] = 1
    return answer


def history_formula(n, source, target, time):
    if target & ~source:
        return 0
    a = popcount(source)
    b = popcount(target)
    return sum(
        (-1) ** j * comb(a - b, j) * factorial(n - b - j) ** time
        for j in range(a - b + 1)
    )


def poly_add_scaled(accumulator, polynomial, scalar=1):
    if len(accumulator) < len(polynomial):
        accumulator.extend([0] * (len(polynomial) - len(accumulator)))
    for degree, coefficient in enumerate(polynomial):
        accumulator[degree] += scalar * coefficient


def poly_multiply(left, right):
    if not left or not right:
        return []
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] += a * b
    return answer


def poly_power(polynomial, exponent):
    answer = [1]
    base = polynomial
    while exponent:
        if exponent & 1:
            answer = poly_multiply(answer, base)
        base = poly_multiply(base, base)
        exponent //= 2
    return answer


def required_fixed_cycle_polynomial(n, required):
    # u^required times u(u+1)...(u+n-required-1)
    polynomial = [0] * required + [1]
    for shift in range(n - required):
        polynomial = poly_multiply(polynomial, [shift, 1])
    return polynomial


def marked_formula(n, source, target, time):
    if target & ~source:
        return [0]
    a = popcount(source)
    b = popcount(target)
    answer = []
    for j in range(a - b + 1):
        term = poly_power(required_fixed_cycle_polynomial(n, b + j), time)
        poly_add_scaled(answer, term, (-1) ** j * comb(a - b, j))
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return answer or [0]


def marked_step(distribution, marked_matrix):
    size = len(marked_matrix)
    answer = [[0] for _ in range(size)]
    for intermediate, polynomial in enumerate(distribution):
        if not any(polynomial):
            continue
        for target in range(size):
            edge = marked_matrix[intermediate][target]
            if not edge:
                continue
            edge_poly = [0] * (max(edge) + 1)
            for degree, coefficient in edge.items():
                edge_poly[degree] = coefficient
            product = poly_multiply(polynomial, edge_poly)
            poly_add_scaled(answer[target], product)
    for polynomial in answer:
        while len(polynomial) > 1 and polynomial[-1] == 0:
            polynomial.pop()
    return answer


def lambda_value(n, size):
    return Fraction(factorial(n - size), factorial(n))


def absorption_cdf(n, initial_size, time):
    return sum(
        Fraction((-1) ** j * comb(initial_size, j), 1) * lambda_value(n, j) ** time
        for j in range(initial_size + 1)
    )


def expected_time_formula(n, initial_size):
    return sum(
        Fraction((-1) ** (j + 1) * comb(initial_size, j), 1)
        / (1 - lambda_value(n, j))
        for j in range(1, initial_size + 1)
    )


def second_moment_formula(n, initial_size):
    return sum(
        Fraction((-1) ** (j + 1) * comb(initial_size, j), 1)
        * (1 + lambda_value(n, j)) / (1 - lambda_value(n, j)) ** 2
        for j in range(1, initial_size + 1)
    )


def recursive_moments(n, matrix):
    denominator = factorial(n)
    size = len(matrix)
    means = [Fraction(0) for _ in range(size)]
    seconds = [Fraction(0) for _ in range(size)]
    for cardinality in range(1, n + 1):
        for source in subsets(n):
            if popcount(source) != cardinality:
                continue
            stay = Fraction(matrix[source][source], denominator)
            strict_mean = Fraction(0)
            strict_second = Fraction(0)
            for target in subsets(n):
                if target == source or not matrix[source][target]:
                    continue
                probability = Fraction(matrix[source][target], denominator)
                strict_mean += probability * means[target]
                strict_second += probability * seconds[target]
            means[source] = (1 + strict_mean) / (1 - stay)
            # E[(1+T')^2] with the self-loop term solved to the left.
            seconds[source] = (
                1 + 2 * (stay * means[source] + strict_mean) + strict_second
            ) / (1 - stay)
    return means, seconds


def main():
    rows = []

    for n in range(1, 8):
        matrix, _ = one_step_matrix(n)
        size = 1 << n
        denominator = factorial(n)

        # Literal transition counts and exact support, including the unique gap.
        for source in subsets(n):
            check(sum(matrix[source]) == denominator, "row mass")
            for target in subsets(n):
                literal = matrix[source][target]
                formula = history_formula(n, source, target, 1)
                check(literal == formula, f"one-step n={n}, A={source}, B={target}")
                expected_positive = (
                    not (target & ~source)
                    and not (source == size - 1 and popcount(target) == n - 1)
                )
                check((literal > 0) == expected_positive, "one-step support")

        # Integer matrix powers versus the independent inclusion-exclusion law.
        power = identity_matrix(size)
        for time in range(0, 6):
            if time:
                power = matrix_multiply(power, matrix)
            for source in subsets(n):
                check(sum(power[source]) == denominator ** time, "history mass")
                for target in subsets(n):
                    check(
                        power[source][target] == history_formula(n, source, target, time),
                        f"history n={n}, t={time}, A={source}, B={target}",
                    )

        # Subset-zeta eigenbasis: every containment indicator is an eigenvector.
        for witness in subsets(n):
            eigen_count = factorial(n - popcount(witness))
            for source in subsets(n):
                left = sum(
                    matrix[source][target]
                    for target in subsets(n)
                    if target & witness == witness
                )
                right = eigen_count if source & witness == witness else 0
                check(left == right, "zeta eigenbasis")

        # Exact CDF and rational first two moments for n>=2.
        if n >= 2:
            means, seconds = recursive_moments(n, matrix)
            for source in subsets(n):
                a = popcount(source)
                for time in range(0, 8):
                    direct = Fraction(matrix_power_entry(matrix, source, 0, time), denominator ** time)
                    check(direct == absorption_cdf(n, a, time), "absorption CDF")
                check(means[source] == expected_time_formula(n, a), "mean absorption")
                check(seconds[source] == second_moment_formula(n, a), "second moment")
        else:
            check(matrix[1][1] == 1 and matrix[1][0] == 0, "n=1 nonabsorbing boundary")

        rows.append(("unmarked", n, size, tuple(matrix[size - 1]),
                     tuple(expected_time_formula(n, a) if n >= 2 else None for a in range(n + 1))))

    # Cycle-marked histories are checked from literal permutation enumeration.
    for n in range(1, 6):
        _, marked = one_step_matrix(n)
        size = 1 << n
        for source in subsets(n):
            distribution = [[0] for _ in range(size)]
            distribution[source] = [1]
            for time in range(1, 4):
                distribution = marked_step(distribution, marked)
                for target in subsets(n):
                    direct = distribution[target]
                    formula = marked_formula(n, source, target, time)
                    check(direct == formula, f"marked n={n},t={time},A={source},B={target}")
                    for coefficient in formula:
                        check(coefficient >= 0, "marked coefficient nonnegative")
        rows.append(("marked", n, sum(len(p) for row in marked for p in row)))

    payload = "\n".join(repr(row) for row in rows)
    print("RANDOM_PERMUTATION_FIXED_POINT_SIEVE_SCOUT_V1")
    print("unmarked_boxes=7")
    print("marked_boxes=5")
    print(f"row_sha256={sha256(payload.encode()).hexdigest()}")
    print(f"assertions={ASSERTIONS}")
    print("STATUS PASS")


def matrix_power_entry(matrix, source, target, time):
    size = len(matrix)
    vector = [0] * size
    vector[source] = 1
    for _ in range(time):
        next_vector = [0] * size
        for intermediate, count in enumerate(vector):
            if count:
                for endpoint, edge in enumerate(matrix[intermediate]):
                    if edge:
                        next_vector[endpoint] += count * edge
        vector = next_vector
    return vector[target]


if __name__ == "__main__":
    main()
