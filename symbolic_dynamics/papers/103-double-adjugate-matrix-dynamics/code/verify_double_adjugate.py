#!/usr/bin/env python3
"""Exact controls for double-adjugate dynamics over prime fields."""

from itertools import product
from math import gcd


ASSERTIONS = 0


def check(condition, message="exact assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def det(matrix, prime):
    n = len(matrix)
    work = [list(row) for row in matrix]
    out = 1
    for col in range(n):
        pivot = next((row for row in range(col, n)
                      if work[row][col] % prime), None)
        if pivot is None:
            return 0
        if pivot != col:
            work[col], work[pivot] = work[pivot], work[col]
            out = -out
        value = work[col][col] % prime
        out = out * value % prime
        inverse = pow(value, -1, prime)
        for row in range(col + 1, n):
            factor = work[row][col] * inverse % prime
            for j in range(col, n):
                work[row][j] = (work[row][j]
                                - factor * work[col][j]) % prime
    return out % prime


def minor(matrix, deleted_row, deleted_column):
    return tuple(
        tuple(matrix[row][column] for column in range(len(matrix))
              if column != deleted_column)
        for row in range(len(matrix)) if row != deleted_row
    )


def adjugate(matrix, prime):
    n = len(matrix)
    return tuple(
        tuple(((-1) ** (i + j)
               * det(minor(matrix, j, i), prime)) % prime
              for j in range(n))
        for i in range(n)
    )


def scalar(value, matrix, prime):
    return tuple(tuple(value * entry % prime for entry in row)
                 for row in matrix)


def psi_closed(matrix, prime):
    return scalar(pow(det(matrix, prime), len(matrix) - 2, prime),
                  matrix, prime)


def matrices(prime, dimension):
    for flat in product(range(prime), repeat=dimension * dimension):
        yield tuple(tuple(flat[dimension * i + j]
                          for j in range(dimension))
                    for i in range(dimension))


def gl_size(q, dimension):
    out = 1
    for j in range(dimension):
        out *= q ** dimension - q ** j
    return out


def sl_size(q, dimension):
    return gl_size(q, dimension) // (q - 1)


def fixed_formula(q, dimension, iterate):
    alpha = (dimension - 1) ** 2
    exponent = (alpha ** iterate - 1) // dimension
    return 1 + sl_size(q, dimension) * gcd(exponent, q - 1)


def prime_divisors(value):
    factors = []
    prime = 2
    while prime * prime <= value:
        if value % prime == 0:
            factors.append(prime)
            while value % prime == 0:
                value //= prime
        prime += 1
    if value > 1:
        factors.append(value)
    return factors


def valuation(value, prime):
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def stabilization_time(alpha, modulus):
    common = [prime for prime in prime_divisors(alpha)
              if modulus % prime == 0]
    if not common:
        return 0
    return max(
        (valuation(modulus, prime) + valuation(alpha, prime) - 1)
        // valuation(alpha, prime)
        for prime in common
    )


def exhaustive_lane():
    rows = []
    for prime, dimension in ((2, 3), (3, 3), (2, 4)):
        fixed = [0] * 6
        images = [set() for _ in range(6)]
        total = 0
        for matrix in matrices(prime, dimension):
            total += 1
            direct = adjugate(adjugate(matrix, prime), prime)
            closed = psi_closed(matrix, prime)
            check(direct == closed, "literal and closed double adjugates differ")
            if det(matrix, prime) == 0:
                check(all(entry == 0 for row in direct for entry in row),
                      "singular matrix did not collapse")
            value = matrix
            for iterate in range(1, 7):
                value = psi_closed(value, prime)
                fixed[iterate - 1] += value == matrix
                images[iterate - 1].add(value)
        predicted_fixed = [fixed_formula(prime, dimension, iterate)
                           for iterate in range(1, 7)]
        check(fixed == predicted_fixed, "fixed sequence formula failed")
        alpha = (dimension - 1) ** 2
        predicted_images = [
            1 + gl_size(prime, dimension)
            // gcd(alpha ** iterate, prime - 1)
            for iterate in range(1, 7)
        ]
        check([len(image) for image in images] == predicted_images,
              "image staircase formula failed")
        rows.append((prime, dimension, total, fixed,
                     [len(image) for image in images]))
    return rows


def diagonal(determinant, dimension):
    return tuple(
        tuple(determinant if i == j == 0 else 1 if i == j else 0
              for j in range(dimension))
        for i in range(dimension)
    )


def signal_lane():
    rows = []
    for q, dimension in ((5, 4), (7, 3), (11, 4), (13, 5)):
        alpha = (dimension - 1) ** 2
        determinant_counts = []
        matrix_counts = []
        for iterate in range(1, 13):
            exponent = (alpha ** iterate - 1) // dimension
            good = []
            for delta in range(1, q):
                matrix = diagonal(delta, dimension)
                value = matrix
                for _ in range(iterate):
                    value = psi_closed(value, q)
                check(
                    value == scalar(pow(delta, exponent, q), matrix, q),
                    "iterate exponent normal form failed",
                )
                check(
                    det(value, q) == pow(delta, alpha ** iterate, q),
                    "determinant exponent normal form failed",
                )
                check((value == matrix) == (pow(delta, exponent, q) == 1),
                      "determinant representative criterion failed")
                if value == matrix:
                    good.append(delta)
            check(len(good) == gcd(exponent, q - 1),
                  "determinant gcd count failed")
            determinant_counts.append(len(good))
            matrix_counts.append(fixed_formula(q, dimension, iterate))
        rows.append((q, dimension, determinant_counts, matrix_counts))
    return rows


def staircase_lane():
    """Independent scalar-line images, including multi-step stabilization."""
    rows = []
    for q, dimension in ((5, 4), (7, 3), (17, 3), (257, 3), (19, 4)):
        alpha = (dimension - 1) ** 2
        modulus = q - 1
        time = stabilization_time(alpha, modulus)
        horizon = max(6, time + 3)
        base = diagonal(1, dimension)
        actual_sizes = []
        predicted_sizes = []
        gcds = []
        for iterate in range(horizon + 1):
            line_image = set()
            for coefficient in range(1, q):
                value = scalar(coefficient, base, q)
                for _ in range(iterate):
                    value = psi_closed(value, q)
                line_image.add(value)
            predicted = modulus // gcd(alpha ** iterate, modulus)
            check(len(line_image) == predicted,
                  "literal projective-line image size failed")
            actual_sizes.append(len(line_image))
            predicted_sizes.append(predicted)
            gcds.append(gcd(alpha ** iterate, modulus))

        check(actual_sizes == predicted_sizes,
              "line-image staircase disagrees with gcd staircase")
        for iterate in range(time):
            check(actual_sizes[iterate] > actual_sizes[iterate + 1],
                  "image chain did not lose strictly before t_star")
        for iterate in range(time, horizon):
            check(actual_sizes[iterate] == actual_sizes[iterate + 1],
                  "image chain did not stabilize at t_star")

        saturated = 1
        for prime in prime_divisors(alpha):
            saturated *= prime ** valuation(modulus, prime)
        check(gcds[time] == saturated,
              "saturated prime-power divisor failed")
        if time > 0:
            check(gcds[time - 1] < saturated,
                  "claimed first stabilization was not first")
        else:
            check(saturated == 1,
                  "zero stabilization time requires coprimality")
        rows.append((q, dimension, time, actual_sizes))
    return rows


def main():
    exhaustive = exhaustive_lane()
    signals = signal_lane()
    staircases = staircase_lane()
    print("double-adjugate exact controls: PASS")
    print(f"assertions: {ASSERTIONS}")
    for row in exhaustive:
        print("exhaustive", row)
    for row in signals:
        print("signal", row)
    for row in staircases:
        print("staircase", row)


if __name__ == "__main__":
    main()
