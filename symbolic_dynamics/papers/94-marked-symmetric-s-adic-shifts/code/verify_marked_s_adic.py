#!/usr/bin/env python3
"""Exact finite controls for P94: marked symmetric S-adic shifts.

The script has two independent evidence-bearing lanes.

1. Literal words: it enumerates binary preimages, constructs their images,
   and checks that ``10`` occurs exactly across constant-length image cuts.
   A cyclic version checks the marker phase without assuming a chosen origin.
2. Incidence arithmetic: it uses ``fractions.Fraction`` to verify the
   symmetric incidence matrices, their bias contraction, products, and the
   finite inverse-limit interval.  The examples a_n=n and a_n=n^2 receive
   separate exact partial-product checks.

The one floating-point comparison is explicitly labelled as a numerical
sanity check for Euler's already-proved sinh product; no finite theorem rests
on that comparison.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import pi, prod, sinh


ASSERTIONS = 0


def check(condition: bool, message: str = "") -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message or f"assertion {ASSERTIONS} failed")


def image(letter: int, a: int) -> str:
    check(letter in (0, 1), "binary letter required")
    check(a >= 1, "a must be positive")
    if letter == 0:
        return "0" * (a + 1) + "1"
    return "0" + "1" * (a + 1)


def apply(word: tuple[int, ...], a: int) -> str:
    return "".join(image(letter, a) for letter in word)


def linear_ten_positions(word: str) -> list[int]:
    return [i for i in range(len(word) - 1) if word[i : i + 2] == "10"]


def cyclic_ten_positions(word: str) -> list[int]:
    return [
        i
        for i in range(len(word))
        if word[i] == "1" and word[(i + 1) % len(word)] == "0"
    ]


def decode_blocks(word: str, a: int) -> tuple[int, ...]:
    length = a + 2
    check(len(word) % length == 0, "whole blocks required")
    dictionary = {image(0, a): 0, image(1, a): 1}
    blocks = [word[i : i + length] for i in range(0, len(word), length)]
    check(all(block in dictionary for block in blocks), "unknown image block")
    return tuple(dictionary[block] for block in blocks)


def marker_probe() -> tuple[int, int]:
    literal_words = 0
    cyclic_words = 0
    for a in range(1, 10):
        length = a + 2
        check("10" not in image(0, a), "internal marker in sigma(0)")
        check("10" not in image(1, a), "internal marker in sigma(1)")
        check(image(0, a)[0] == image(1, a)[0] == "0")
        check(image(0, a)[-1] == image(1, a)[-1] == "1")
        for width in range(1, 8):
            for bits in product((0, 1), repeat=width):
                out = apply(bits, a)
                expected_linear = [k * length - 1 for k in range(1, width)]
                check(linear_ten_positions(out) == expected_linear)
                check(decode_blocks(out, a) == bits)
                literal_words += 1

                expected_cyclic = [k * length - 1 for k in range(1, width + 1)]
                check(cyclic_ten_positions(out) == expected_cyclic)
                marker_positions = cyclic_ten_positions(out)
                gaps = []
                for j in range(width):
                    gap = (
                        marker_positions[(j + 1) % width] - marker_positions[j]
                    ) % len(out)
                    gaps.append(gap or len(out))
                check(gaps == [length] * width)
                cyclic_words += 1
    return literal_words, cyclic_words


def mat_vec(matrix: tuple[tuple[Fraction, Fraction], ...], vector):
    return tuple(sum(row[j] * vector[j] for j in range(2)) for row in matrix)


def mat_mul(left, right):
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )


def normalized_matrix(a: int):
    length = a + 2
    return (
        (Fraction(a + 1, length), Fraction(1, length)),
        (Fraction(1, length), Fraction(a + 1, length)),
    )


def bias_vector(t: Fraction):
    return (Fraction(1, 2) * (1 + t), Fraction(1, 2) * (1 - t))


def rho(a: int) -> Fraction:
    return Fraction(a, a + 2)


def incidence_probe() -> int:
    cases = 0
    test_biases = [Fraction(k, 12) for k in range(-12, 13)]
    for a in range(1, 31):
        matrix = normalized_matrix(a)
        check(sum(matrix[0]) == 1 and sum(matrix[1]) == 1)
        check(matrix[0][0] == matrix[1][1])
        check(matrix[0][1] == matrix[1][0])
        for t in test_biases:
            check(mat_vec(matrix, bias_vector(t)) == bias_vector(rho(a) * t))
            cases += 1

    # Independent composition lane.  The second eigen-direction must contract
    # by the product of the individual rho factors, regardless of order.
    identity = (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(1)),
    )
    for depth in range(1, 7):
        for directive in product(range(1, 5), repeat=depth):
            matrix = identity
            contraction = Fraction(1)
            for a in directive:
                matrix = mat_mul(matrix, normalized_matrix(a))
                contraction *= rho(a)
            for t in (Fraction(-1), Fraction(-2, 5), Fraction(0), Fraction(3, 7), Fraction(1)):
                check(mat_vec(matrix, bias_vector(t)) == bias_vector(contraction * t))
                cases += 1
            check(sum(matrix[0]) == 1 and sum(matrix[1]) == 1)
            check(matrix[0][0] - matrix[0][1] == contraction)
    return cases


def inverse_limit_probe() -> int:
    cases = 0
    directives = [
        tuple(range(1, 13)),
        tuple(n * n for n in range(1, 13)),
        (1, 4, 2, 9, 3, 16, 5, 25, 6, 36),
    ]
    for directive in directives:
        partial = [Fraction(1)]
        for a in directive:
            partial.append(partial[-1] * rho(a))
        radius = partial[-1]
        for scale in (Fraction(-1), Fraction(-1, 3), Fraction(0), Fraction(2, 5), Fraction(1)):
            bottom_bias = scale * radius
            biases = [bottom_bias / partial[n] for n in range(len(directive) + 1)]
            check(all(-1 <= t <= 1 for t in biases))
            for n, a in enumerate(directive):
                check(biases[n] == rho(a) * biases[n + 1])
                check(
                    mat_vec(normalized_matrix(a), bias_vector(biases[n + 1]))
                    == bias_vector(biases[n])
                )
                cases += 1

        # Any level-zero bias outside the finite radius forces a terminal
        # bias outside [-1,1], exactly as in the interval proof.
        outside = radius + Fraction(1, 10) * radius
        check(abs(outside / radius) > 1)
    return cases


def example_probe() -> tuple[Fraction, float, float]:
    # Telescoping example a_n=n, all exact.
    running = Fraction(1)
    for n in range(1, 201):
        running *= Fraction(n, n + 2)
        check(running == Fraction(2, (n + 1) * (n + 2)))

    # Square example: exact rational partial products and recurrence.
    square = Fraction(1)
    square_20 = None
    for n in range(1, 101):
        previous = square
        square *= Fraction(n * n, n * n + 2)
        check(square * (n * n + 2) == previous * n * n)
        check(square > 0)
        if n == 20:
            square_20 = square

    # Numerical-only sanity check of Euler's sinh product.  A long direct
    # product approaches the closed form from above with O(1/N) tail error.
    numerical_partial = prod(
        (n * n) / (n * n + 2.0) for n in range(1, 250_001)
    )
    closed_form = pi * (2.0**0.5) / sinh(pi * (2.0**0.5))
    check(numerical_partial > closed_form)
    check(abs(numerical_partial - closed_form) < 1.0e-6)
    check(square_20 is not None)
    return square_20, numerical_partial, closed_form


def main() -> None:
    literal_words, cyclic_words = marker_probe()
    incidence_cases = incidence_probe()
    inverse_cases = inverse_limit_probe()
    square_20, numerical_partial, closed_form = example_probe()
    print("marked symmetric S-adic exact control: PASS")
    print(f"assertions={ASSERTIONS}")
    print(f"literal_marker_words={literal_words}")
    print(f"cyclic_phase_words={cyclic_words}")
    print(f"incidence_bias_cases={incidence_cases}")
    print(f"inverse_limit_cases={inverse_cases}")
    print("a_n=n: R_N=2/((N+1)(N+2)) verified exactly for N<=200")
    print(f"a_n=n^2: R_20={square_20.numerator}/{square_20.denominator}")
    print("a_n=n^2: exact partial-product recurrence verified for N<=100")
    print(f"a_n=n^2: R_250000={numerical_partial:.15f}")
    print(f"a_n=n^2: pi*sqrt(2)/sinh(pi*sqrt(2))={closed_form:.15f}")


if __name__ == "__main__":
    main()
