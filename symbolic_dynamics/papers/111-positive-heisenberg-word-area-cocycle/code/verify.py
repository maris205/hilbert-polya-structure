#!/usr/bin/env python3
"""Exact controls for positive Heisenberg word-area cocycles.

The program has two deliberately separate lanes.

Lane A literally multiplies the two 3-by-3 integer generators and compares
the result with independently scanned word counts.  It then compares the
exhaustive area histograms with a Gaussian-binomial recurrence.

Lane B expands the area into centered iid Bernoulli variables, checks that
identity word by word, and evaluates biased moments with exact Fraction
arithmetic.  Extremal-area probabilities and rational exponential-moment
bounds provide a separate control for the pressure proof.

No random sampling, floating-point arithmetic, or network access is used.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from math import comb


X = ((1, 1, 0), (0, 1, 0), (0, 0, 1))
Y = ((1, 0, 0), (0, 1, 1), (0, 0, 1))
IDENTITY = ((1, 0, 0), (0, 1, 0), (0, 0, 1))

ASSERTIONS = 0
LANES = defaultdict(int)


def check(condition, message, lane):
    global ASSERTIONS
    ASSERTIONS += 1
    LANES[lane] += 1
    if not condition:
        raise AssertionError((lane, message))


def matmul(left, right):
    return tuple(
        tuple(
            sum(left[row][middle] * right[middle][column]
                for middle in range(3))
            for column in range(3)
        )
        for row in range(3)
    )


def literal_product(word):
    matrix = IDENTITY
    for letter in word:
        matrix = matmul(X if letter else Y, matrix)
    return matrix


def scan_word(word):
    """Return (#X,#Y,#(Y before X)) without matrix arithmetic."""
    x_count = 0
    y_count = 0
    area = 0
    for letter in word:
        if letter:
            x_count += 1
            area += y_count
        else:
            y_count += 1
    return x_count, y_count, area


def poly_add(left, right, shift=0):
    out = list(left)
    needed = len(right) + shift
    if len(out) < needed:
        out.extend([0] * (needed - len(out)))
    for degree, coefficient in enumerate(right):
        out[degree + shift] += coefficient
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def gaussian_rows(max_n):
    """Build [n choose j]_z from the last-letter recurrence."""
    rows = [[(1,)]]
    for n in range(1, max_n + 1):
        row = []
        for j in range(n + 1):
            final_y = rows[n - 1][j] if j < n else (0,)
            final_x = rows[n - 1][j - 1] if j else (0,)
            row.append(poly_add(final_y, final_x, n - j))
        rows.append(row)
    return rows


def histogram_polynomial(histogram):
    if not histogram:
        return (0,)
    return tuple(histogram.get(area, 0)
                 for area in range(max(histogram) + 1))


def conditional_moments(coefficients):
    mass = sum(coefficients)
    first = sum(area * count
                for area, count in enumerate(coefficients))
    second = sum(area * area * count
                 for area, count in enumerate(coefficients))
    mean = Fraction(first, mass)
    variance = Fraction(second, mass) - mean * mean
    return mean, variance


def biased_moments(row, p):
    n = len(row) - 1
    q = 1 - p
    mass = Fraction(0)
    first = Fraction(0)
    second = Fraction(0)
    for j, coefficients in enumerate(row):
        word_weight = p**j * q**(n - j)
        for area, count in enumerate(coefficients):
            probability = count * word_weight
            mass += probability
            first += probability * area
            second += probability * area * area
    return mass, first, second - first * first


def biased_transform(row, p, tilt):
    n = len(row) - 1
    q = 1 - p
    return sum(
        count * p**j * q**(n - j) * tilt**area
        for j, coefficients in enumerate(row)
        for area, count in enumerate(coefficients)
    )


def zero_area_probability(n, p):
    q = 1 - p
    return sum(p**j * q**(n - j) for j in range(n + 1))


def run():
    enum_horizon = 16
    moment_horizon = 32
    rows = gaussian_rows(moment_horizon)
    literal_words = 0
    histogram_slices = 0

    # Lane A1: raw integer matrices versus independently scanned words.
    for n in range(enum_horizon + 1):
        histograms = {j: Counter() for j in range(n + 1)}
        for word in product((0, 1), repeat=n):
            literal_words += 1
            matrix = literal_product(word)
            j, k, area = scan_word(word)
            predicted = ((1, j, area), (0, 1, k), (0, 0, 1))
            check(matrix == predicted,
                  ("normal form", n, word, matrix, predicted),
                  "literal_normal_form")
            frobenius_squared = sum(entry * entry for row in matrix
                                    for entry in row)
            check(frobenius_squared == 3 + j * j + k * k + area * area,
                  ("Frobenius formula", n, word),
                  "literal_norm")
            check(matrix[0][1] + matrix[1][2] == n,
                  ("first-superdiagonal count", n, word),
                  "literal_normal_form")
            histograms[j][area] += 1

        for j, histogram in histograms.items():
            histogram_slices += 1
            coefficients = histogram_polynomial(histogram)
            check(coefficients == rows[n][j],
                  ("Gaussian slice", n, j, coefficients, rows[n][j]),
                  "gaussian_slice")
            check(sum(coefficients) == comb(n, j),
                  ("slice mass", n, j), "gaussian_slice")
            mean, variance = conditional_moments(coefficients)
            expected_mean = Fraction(j * (n - j), 2)
            expected_variance = Fraction(j * (n - j) * (n + 1), 12)
            check(mean == expected_mean,
                  ("conditional mean", n, j, mean, expected_mean),
                  "conditional_moments")
            check(variance == expected_variance,
                  ("conditional variance", n, j, variance,
                   expected_variance), "conditional_moments")

        maximum = (n * n) // 4
        maximum_words = sum(histogram.get(maximum, 0)
                            for histogram in histograms.values())
        zero_words = sum(histogram.get(0, 0)
                         for histogram in histograms.values())
        check(maximum_words == (1 if n % 2 == 0 else 2),
              ("maximizers", n, maximum_words), "extrema")
        check(zero_words == n + 1,
              ("zero words", n, zero_words), "extrema")

    # Lane A2: conditional Gaussian slices imply the full biased moments.
    probabilities = (
        Fraction(0), Fraction(1, 7), Fraction(1, 3), Fraction(1, 2),
        Fraction(2, 3), Fraction(6, 7), Fraction(1),
    )
    biased_cases = 0
    for n in range(moment_horizon + 1):
        for p in probabilities:
            biased_cases += 1
            q = 1 - p
            mass, mean, variance = biased_moments(rows[n], p)
            expected_mean = Fraction(n * (n - 1), 2) * p * q
            expected_variance = (
                Fraction(n * (n - 1), 6) * p * q
                * (6 * n * p * p - 6 * n * p + 2 * n
                   - 9 * p * p + 9 * p - 1)
            )
            check(mass == 1, ("biased mass", n, p, mass),
                  "biased_moments")
            check(mean == expected_mean,
                  ("biased mean", n, p, mean, expected_mean),
                  "biased_moments")
            check(variance == expected_variance,
                  ("biased variance", n, p, variance,
                   expected_variance), "biased_moments")
            pair_variance = (
                comb(n, 2) * p * q * (1 - p * q)
                + 2 * comb(n, 3) * p * q * (1 - 3 * p * q)
            )
            check(pair_variance == expected_variance,
                  ("pair covariance variance", n, p,
                   pair_variance, expected_variance), "pair_covariance")

            zero_probability = sum(
                coefficients[0] * p**j * q**(n - j)
                for j, coefficients in enumerate(rows[n])
            )
            check(zero_probability == zero_area_probability(n, p),
                  ("zero-area probability", n, p), "extrema")
            if 0 < p < 1:
                maximum = (n * n) // 4
                maximum_probability = sum(
                    coefficients[maximum] * p**j * q**(n - j)
                    if maximum < len(coefficients) else Fraction(0)
                    for j, coefficients in enumerate(rows[n])
                )
                check(maximum_probability == (p * q)**(n // 2),
                      ("max-area probability", n, p,
                       maximum_probability), "extrema")

    # Lane B1: the centered-pair decomposition, independent of q-binomials.
    decomposition_words = 0
    for n in range(13):
        for p in (Fraction(1, 7), Fraction(1, 2), Fraction(5, 6)):
            q = 1 - p
            weights = [Fraction(k) - p * (n - 1) for k in range(n)]
            weight_square_sum = sum(weight * weight for weight in weights)
            closed_weight_square_sum = (
                Fraction(n * (n - 1), 6)
                * (2 * n - 1 - 6 * p * (n - 1)
                   + 6 * p * p * (n - 1))
            )
            check(weight_square_sum == closed_weight_square_sum,
                  ("weight variance", n, p), "centered_decomposition")
            for word in product((0, 1), repeat=n):
                decomposition_words += 1
                _, _, area = scan_word(word)
                eta = [Fraction(letter) - p for letter in word]
                centered = (Fraction(area)
                            - Fraction(n * (n - 1), 2) * p * q)
                linear = sum(weight * value
                             for weight, value in zip(weights, eta))
                quadratic = -sum(
                    eta[i] * eta[j]
                    for i in range(n) for j in range(i + 1, n)
                )
                check(centered == linear + quadratic,
                      ("centered identity", n, p, word),
                      "centered_decomposition")

    # Lane B2: exact exponential-moment bounds used by the pressure proof.
    pressure_cases = 0
    for n in range(moment_horizon + 1):
        maximum = (n * n) // 4
        for p in (Fraction(1, 7), Fraction(1, 2), Fraction(5, 6)):
            q = 1 - p
            max_probability = (p * q)**(n // 2)
            zero_probability = zero_area_probability(n, p)
            for tilt in (Fraction(2), Fraction(3), Fraction(1, 2)):
                pressure_cases += 1
                transform = biased_transform(rows[n], p, tilt)
                if tilt > 1:
                    check(max_probability * tilt**maximum <= transform,
                          ("positive lower bound", n, p, tilt),
                          "pressure_bounds")
                    check(transform <= tilt**maximum,
                          ("positive upper bound", n, p, tilt),
                          "pressure_bounds")
                else:
                    check(zero_probability <= transform,
                          ("negative lower bound", n, p, tilt),
                          "pressure_bounds")
                    check(transform <= 1,
                          ("negative upper bound", n, p, tilt),
                          "pressure_bounds")

    # Endpoint and asymptotic-algebra sentinels.
    for n in range(1, 101):
        for endpoint_word in ((1,) * n, (0,) * n):
            matrix = literal_product(endpoint_word)
            j, k, area = scan_word(endpoint_word)
            check(area == 0, ("endpoint area", n, endpoint_word[0]),
                  "endpoints")
            check(sum(entry * entry for row in matrix for entry in row)
                  == n * n + 3,
                  ("endpoint norm", n, endpoint_word[0]), "endpoints")
            check((j, k) in ((n, 0), (0, n)),
                  ("endpoint counts", n, endpoint_word[0]), "endpoints")

        for p in (Fraction(1, 7), Fraction(1, 2), Fraction(5, 6)):
            q = 1 - p
            sigma_squared = p * q * (3 * p * p - 3 * p + 1) / 3
            leading_coefficient = (
                Fraction(n * (n - 1), 6) * p * q
                * (6 * n * p * p - 6 * n * p + 2 * n
                   - 9 * p * p + 9 * p - 1)
            )
            cubic_factor = 6 * p * p - 6 * p + 2
            lower_factor = -9 * p * p + 9 * p - 1
            residual = leading_coefficient - sigma_squared * n**3
            expected_residual = (
                p * q * ((lower_factor - cubic_factor) * n * n
                         - lower_factor * n) / 6
            )
            check(residual == expected_residual,
                  ("CLT variance coefficient", n, p, residual),
                  "asymptotic_algebra")

    lane_summary = ",".join(
        f"{name}:{LANES[name]}" for name in sorted(LANES)
    )
    print("positive-Heisenberg exact control: PASS")
    print(f"assertions={ASSERTIONS}")
    print(f"literal_words={literal_words}")
    print(f"histogram_slices={histogram_slices}")
    print(f"biased_cases={biased_cases}")
    print(f"decomposition_words={decomposition_words}")
    print(f"pressure_cases={pressure_cases}")
    print(f"lane_assertions={lane_summary}")


if __name__ == "__main__":
    run()
