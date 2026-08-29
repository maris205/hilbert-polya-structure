#!/usr/bin/env python3
"""Exact controls for the max-plus switching-induced-growth paper.

The verifier is standard-library only.  It uses integer and Fraction
arithmetic; it performs no random sampling and uses no floating point.

The main lanes are deliberately redundant:

* literal 2-by-2 max-plus products and literal vector actions;
* minimal tropical-rank-one reset words and their constant output gaps;
* the five-gap projective recursion and its three-state strong lumping;
* exhaustive word histograms, exact height support, and independent dynamic
  programs;
* biased exact laws and the Laurent-PGF transfer matrix;
* stationary, Poisson/martingale, and implicit-Perron formula checks;
* deterministic endpoints, generator powers, and rare extremal words.
"""

from collections import defaultdict
from fractions import Fraction
from itertools import product


NEG_INF = None
A = ((-2, -1), (1, -1))
B = ((-1, 1), (-1, -2))
GENERATORS = (A, B)
IDENTITY = ((0, NEG_INF), (NEG_INF, 0))

N, Z, P = range(3)
LUMP_TRANSITION = {
    (N, 0): (Z, -1),
    (N, 1): (P, 1),
    (Z, 0): (N, 1),
    (Z, 1): (P, 1),
    (P, 0): (N, 1),
    (P, 1): (Z, -1),
}

GAP_TRANSITION = {
    (0, 0): (-2, 1),
    (0, 1): (2, 1),
    (-2, 0): (0, -1),
    (-3, 0): (0, -1),
    (-2, 1): (3, 1),
    (-3, 1): (3, 1),
    (2, 0): (-3, 1),
    (3, 0): (-3, 1),
    (2, 1): (0, -1),
    (3, 1): (0, -1),
}

ASSERTIONS = 0
LANES = defaultdict(int)


def check(condition, message, lane):
    global ASSERTIONS
    ASSERTIONS += 1
    LANES[lane] += 1
    if not condition:
        raise AssertionError((lane, message))


def tropical_plus(left, right):
    if left is NEG_INF or right is NEG_INF:
        return NEG_INF
    return left + right


def finite_maximum(values):
    finite = [value for value in values if value is not NEG_INF]
    return max(finite) if finite else NEG_INF


def tropical_matmul(left, right):
    return tuple(
        tuple(
            finite_maximum(
                tropical_plus(left[row][middle], right[middle][column])
                for middle in range(2)
            )
            for column in range(2)
        )
        for row in range(2)
    )


def literal_product(word):
    """Chronological convention: word[0] acts first."""
    matrix = IDENTITY
    for letter in word:
        matrix = tropical_matmul(GENERATORS[letter], matrix)
    return matrix


def tropical_matvec(matrix, vector):
    return tuple(
        finite_maximum(
            tropical_plus(matrix[row][column], vector[column])
            for column in range(2)
        )
        for row in range(2)
    )


def literal_vector(word):
    vector = (0, 0)
    for letter in word:
        vector = tropical_matvec(GENERATORS[letter], vector)
    return vector


def matrix_height(matrix):
    return finite_maximum(entry for row in matrix for entry in row)


def tropical_rank_one(matrix):
    return (matrix[0][0] + matrix[1][1]
            == matrix[0][1] + matrix[1][0])


def five_gap_word(word):
    gap = 0
    height = 0
    for letter in word:
        gap, reward = GAP_TRANSITION[gap, letter]
        height += reward
    return gap, height


def lump(gap):
    if gap < 0:
        return N
    if gap > 0:
        return P
    return Z


def lump_word(word):
    state = Z
    height = 0
    for letter in word:
        state, reward = LUMP_TRANSITION[state, letter]
        height += reward
    return state, height


def count_dp(n):
    law = {(Z, 0): 1}
    for _ in range(n):
        new = defaultdict(int)
        for (state, height), multiplicity in law.items():
            for letter in (0, 1):
                next_state, reward = LUMP_TRANSITION[state, letter]
                new[next_state, height + reward] += multiplicity
        law = dict(new)
    histogram = defaultdict(int)
    for (_, height), multiplicity in law.items():
        histogram[height] += multiplicity
    return law, dict(histogram)


def probability_dp(n, p):
    q = 1 - p
    law = {(Z, 0): Fraction(1)}
    for _ in range(n):
        new = defaultdict(Fraction)
        for (state, height), mass in law.items():
            for letter, weight in ((0, p), (1, q)):
                next_state, reward = LUMP_TRANSITION[state, letter]
                new[next_state, height + reward] += mass * weight
        law = dict(new)
    return law


def tilted_kernel(p, y):
    q = 1 - p
    return (
        (0, p / y, q * y),
        (p * y, 0, q * y),
        (p * y, q / y, 0),
    )


def ordinary_matmul(left, right):
    rows = len(left)
    middle = len(right)
    columns = len(right[0])
    return tuple(
        tuple(
            sum(left[i][k] * right[k][j] for k in range(middle))
            for j in range(columns)
        )
        for i in range(rows)
    )


def matrix_power(matrix, exponent):
    size = len(matrix)
    result = tuple(
        tuple(Fraction(int(i == j)) for j in range(size))
        for i in range(size)
    )
    base = tuple(tuple(Fraction(value) for value in row) for row in matrix)
    while exponent:
        if exponent & 1:
            result = ordinary_matmul(base, result)
        base = ordinary_matmul(base, base)
        exponent //= 2
    return result


def kernel_pgf(n, p, y):
    power = matrix_power(tilted_kernel(p, y), n)
    return sum(power[Z])


def determinant3(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def direct_characteristic(r, y, p):
    kernel = tilted_kernel(p, y)
    matrix = tuple(
        tuple((r if i == j else 0) - kernel[i][j] for j in range(3))
        for i in range(3)
    )
    return determinant3(matrix)


def closed_characteristic(r, y, p):
    a = p * (1 - p)
    return r**3 + (2 * a - 1 - a * y**2) * r - a * y


def transition_matrix(p):
    q = 1 - p
    return ((0, p, q), (p, 0, q), (p, q, 0))


def stationary_data(p):
    q = 1 - p
    a = p * q
    pi = (p / (1 + p), (1 - a) / (2 + a), q / (1 + q))
    mu = 3 * a / (2 + a)
    variance = 4 * a * (1 - a) * (5 - 2 * a) / (2 + a) ** 3
    return pi, mu, variance


def exact_even_minimum_mass(n, p):
    check(n % 2 == 0, ("even minimum called at odd n", n), "internal")
    q = 1 - p
    return (p * p + q * q) ** (n // 2)


def exact_maximum_mass(n, p):
    check(n >= 1, ("maximum mass called at n=0",), "internal")
    q = 1 - p
    a = p * q
    if n % 2 == 0:
        return 2 * a ** (n // 2)
    return a ** ((n - 1) // 2)


def run_literal_lane():
    enum_horizon = 16
    total_words = 0

    orientation_word = (0, 0, 1)
    reverse_word = tuple(reversed(orientation_word))
    check(literal_product(orientation_word) == ((1, 1), (-1, -2)),
          ("orientation product", literal_product(orientation_word)),
          "orientation")
    check(literal_product(orientation_word) != literal_product(reverse_word),
          ("reversal must change literal product",), "orientation")
    check(matrix_height(literal_product(orientation_word))
          == matrix_height(literal_product(reverse_word)),
          ("height reversal sentinel",), "orientation")

    for n in range(enum_horizon + 1):
        histogram = defaultdict(int)
        maximum_words = 0
        minimum_words = 0
        for word in product((0, 1), repeat=n):
            total_words += 1
            matrix = literal_product(word)
            vector = literal_vector(word)
            row_maxima = tuple(finite_maximum(row) for row in matrix)
            gap, five_height = five_gap_word(word)
            state, lump_height_value = lump_word(word)
            height = max(vector)

            check(vector == row_maxima,
                  ("matrix/vector action", n, word, vector, row_maxima),
                  "literal_product")
            check(matrix_height(matrix) == height,
                  ("global height", n, word), "literal_product")
            check(vector[0] - vector[1] == gap,
                  ("literal gap", n, word, vector, gap), "five_gap")
            check(gap in {-3, -2, 0, 2, 3},
                  ("reachable gap", n, word, gap), "five_gap")
            check(five_height == height,
                  ("five-gap reward", n, word, five_height, height),
                  "five_gap")
            check(lump(gap) == state,
                  ("strong lump", n, word, gap, state), "strong_lumping")
            check(lump_height_value == height,
                  ("lumped reward", n, word, lump_height_value, height),
                  "strong_lumping")
            check(height % 2 == n % 2,
                  ("parity", n, word, height), "word_bounds")
            check((n % 2) <= height <= n,
                  ("bounds", n, word, height), "word_bounds")

            histogram[height] += 1
            maximum_words += height == n
            minimum_words += height == n % 2

        _, dynamic_histogram = count_dp(n)
        check(dict(histogram) == dynamic_histogram,
              ("histogram DP", n, dict(histogram), dynamic_histogram),
              "finite_law")
        check(sum(histogram.values()) == 2**n,
              ("histogram mass", n), "finite_law")
        expected_support = set(range(n % 2, n + 1, 2))
        check(set(histogram) == expected_support,
              ("exact height support", n, set(histogram), expected_support),
              "word_support")
        for negative_pairs in range(n // 2 + 1):
            suffix_length = n - 2 * negative_pairs
            witness = ((0, 0) * negative_pairs
                       + tuple(index % 2 for index in range(suffix_length)))
            check(len(witness) == n,
                  ("support witness length", n, negative_pairs, witness),
                  "word_support")
            check(five_gap_word(witness)[1] == suffix_length,
                  ("AA-block support witness", n, negative_pairs, witness,
                   five_gap_word(witness)), "word_support")
        if n == 0:
            check(maximum_words == 1 and minimum_words == 1,
                  ("empty word",), "empty_word")
            check(literal_product(()) == IDENTITY,
                  ("empty product",), "empty_word")
            check(matrix_height(IDENTITY) == 0,
                  ("H_0",), "empty_word")
        else:
            check(maximum_words == 2,
                  ("two alternating maximizers", n, maximum_words),
                  "rare_words")
            expected_minimum_count = (
                2 ** (n // 2) if n % 2 == 0
                else (n // 2 + 2) * 2 ** (n // 2)
            )
            check(minimum_words == expected_minimum_count,
                  ("minimum word count", n, minimum_words,
                   expected_minimum_count), "rare_words")
            alternating_a = tuple(i % 2 for i in range(n))
            alternating_b = tuple(1 - i % 2 for i in range(n))
            check(five_gap_word(alternating_a)[1] == n,
                  ("first alternating word", n), "rare_words")
            check(five_gap_word(alternating_b)[1] == n,
                  ("second alternating word", n), "rare_words")
            check(five_gap_word((0,) * n)[1] == n % 2,
                  ("A endpoint height", n), "endpoints")
            check(five_gap_word((1,) * n)[1] == n % 2,
                  ("B endpoint height", n), "endpoints")

    return enum_horizon, total_words


def run_reset_lane():
    expected = {
        (0, 1, 0): (((0, -2), (3, 1)), -3),
        (0, 1, 1): (((1, -1), (1, -1)), 0),
        (1, 0, 0): (((-1, 1), (-1, 1)), 0),
        (1, 0, 1): (((1, 3), (-2, 0)), 3),
    }

    rank_one_words = {}
    for n in (1, 2, 3):
        current = set()
        for word in product((0, 1), repeat=n):
            is_rank_one = tropical_rank_one(literal_product(word))
            should_be_rank_one = n == 3 and word in expected
            check(is_rank_one == should_be_rank_one,
                  ("reset classification", n, word, literal_product(word)),
                  "reset_words")
            if is_rank_one:
                current.add(word)
        rank_one_words[n] = current

    check(rank_one_words[1] == set(),
          ("no length-one reset", rank_one_words[1]), "reset_words")
    check(rank_one_words[2] == set(),
          ("no length-two reset", rank_one_words[2]), "reset_words")
    check(rank_one_words[3] == set(expected),
          ("exact length-three resets", rank_one_words[3], set(expected)),
          "reset_words")

    for word, (expected_matrix, expected_gap) in expected.items():
        matrix = literal_product(word)
        check(matrix == expected_matrix,
              ("reset product matrix", word, matrix, expected_matrix),
              "reset_words")
        check(tropical_rank_one(matrix),
              ("reset rank", word, matrix), "reset_words")
        check(matrix[0][0] - matrix[1][0] == expected_gap,
              ("reset first-column gap", word, matrix, expected_gap),
              "reset_words")
        check(matrix[0][1] - matrix[1][1] == expected_gap,
              ("reset second-column gap", word, matrix, expected_gap),
              "reset_words")
        for input_gap in (-64, -3, -2, -1, 0, 1, 2, 3, 64):
            image = tropical_matvec(matrix, (input_gap, 0))
            check(image[0] - image[1] == expected_gap,
                  ("constant reset gap", word, input_gap, image,
                   expected_gap), "reset_words")


def run_generator_lane():
    even_a = ((0, -2), (0, 0))
    odd_a = ((-1, -1), (1, -1))
    even_b = ((0, 0), (-2, 0))
    odd_b = ((-1, 1), (-1, -1))

    # Maximum cycle means and the 2-by-2 tropical-rank-one obstruction.
    for matrix, name in ((A, "A"), (B, "B")):
        cycle_means = (
            Fraction(matrix[0][0]),
            Fraction(matrix[1][1]),
            Fraction(matrix[0][1] + matrix[1][0], 2),
        )
        check(max(cycle_means) == 0,
              ("tropical spectral radius", name, cycle_means),
              "generators")
        check(matrix[0][0] + matrix[1][1]
              != matrix[0][1] + matrix[1][0],
              ("not tropical rank one", name), "generators")

    for n in range(1, 65):
        product_a = literal_product((0,) * n)
        product_b = literal_product((1,) * n)
        if n == 1:
            expected_a, expected_b = A, B
        elif n % 2 == 0:
            expected_a, expected_b = even_a, even_b
        else:
            expected_a, expected_b = odd_a, odd_b
        check(product_a == expected_a,
              ("bounded A power", n, product_a, expected_a), "generators")
        check(product_b == expected_b,
              ("bounded B power", n, product_b, expected_b), "generators")
        check(matrix_height(product_a) == n % 2,
              ("A height", n), "endpoints")
        check(matrix_height(product_b) == n % 2,
              ("B height", n), "endpoints")


def run_biased_lane():
    probabilities = (
        Fraction(0), Fraction(1, 7), Fraction(1, 5), Fraction(1, 2),
        Fraction(3, 4), Fraction(6, 7), Fraction(1),
    )
    tilts = (Fraction(1, 3), Fraction(1, 2), Fraction(1),
             Fraction(3, 2), Fraction(2))
    law_horizon = 32

    for p in probabilities:
        q = 1 - p
        for n in range(law_horizon + 1):
            law = probability_dp(n, p)
            check(sum(law.values()) == 1,
                  ("biased mass", n, p), "biased_law")

            histogram = defaultdict(Fraction)
            for (_, height), mass in law.items():
                if mass:
                    histogram[height] += mass
            check(set(histogram).issubset(set(range(n % 2, n + 1, 2))),
                  ("biased support", n, p, set(histogram)), "biased_law")
            if 0 < p < 1:
                check(set(histogram) == set(range(n % 2, n + 1, 2)),
                      ("interior exact support", n, p, set(histogram)),
                      "word_support")

            for y in tilts:
                dp_pgf = sum(mass * y**height
                             for height, mass in histogram.items())
                transfer_pgf = kernel_pgf(n, p, y)
                check(dp_pgf == transfer_pgf,
                      ("PGF transfer", n, p, y, dp_pgf, transfer_pgf),
                      "finite_pgf")

            if n <= 11:
                brute = defaultdict(Fraction)
                for word in product((0, 1), repeat=n):
                    weight = p ** word.count(0) * q ** word.count(1)
                    if weight:
                        brute[matrix_height(literal_product(word))] += weight
                check(dict(brute) == dict(histogram),
                      ("biased brute law", n, p), "biased_law")

            if n >= 1 and 0 < p < 1:
                check(histogram[n] == exact_maximum_mass(n, p),
                      ("alternating mass", n, p, histogram[n]),
                      "rare_words")
            if n % 2 == 0:
                check(histogram[0] == exact_even_minimum_mass(n, p),
                      ("minimum mass", n, p, histogram[0]),
                      "rare_words")

            if p in (0, 1):
                check(histogram == {n % 2: Fraction(1)},
                      ("deterministic endpoint law", n, p, histogram),
                      "endpoints")

    return law_horizon, probabilities


def run_spectral_lane():
    interior_probabilities = (
        Fraction(1, 11), Fraction(1, 7), Fraction(1, 5),
        Fraction(1, 2), Fraction(3, 4), Fraction(6, 7), Fraction(10, 11),
    )
    r_values = (Fraction(1, 4), Fraction(2, 3), Fraction(1),
                Fraction(7, 5), Fraction(3))
    y_values = (Fraction(1, 5), Fraction(1, 2), Fraction(1),
                Fraction(3, 2), Fraction(4))

    for p in interior_probabilities:
        q = 1 - p
        a = p * q
        pi, mu, variance = stationary_data(p)
        transition = transition_matrix(p)

        check(sum(pi) == 1, ("stationary mass", p, pi), "stationary")
        pushed = tuple(
            sum(pi[i] * transition[i][j] for i in range(3))
            for j in range(3)
        )
        check(pushed == pi, ("stationarity", p, pushed, pi), "stationary")
        check(pi[N] == p / (1 + p), ("pi_N", p), "stationary")
        check(pi[P] == q / (1 + q), ("pi_P", p), "stationary")
        check(pi[Z] == (1 - a) / (2 + a), ("pi_Z", p), "stationary")

        stationary_reward = Fraction(0)
        state_reward = []
        for state in (N, Z, P):
            mean = Fraction(0)
            for letter, weight in ((0, p), (1, q)):
                _, reward = LUMP_TRANSITION[state, letter]
                mean += weight * reward
                stationary_reward += pi[state] * weight * reward
            state_reward.append(mean)
        check(stationary_reward == mu,
              ("stationary drift", p, stationary_reward, mu), "drift")
        check(mu == 1 - 2 * (p * pi[N] + q * pi[P]),
              ("negative transition drift", p), "drift")
        check(mu > 0, ("positive interior drift", p, mu), "drift")

        # Explicit Poisson solution (I-P)h=f-mu and martingale variance.
        h = (-2 * p / (1 + p), Fraction(0), -2 * q / (1 + q))
        for state in (N, Z, P):
            poisson_left = h[state] - sum(
                transition[state][j] * h[j] for j in range(3)
            )
            check(poisson_left == state_reward[state] - mu,
                  ("Poisson equation", p, state, poisson_left,
                   state_reward[state] - mu), "poisson")

        martingale_variance = Fraction(0)
        for state in (N, Z, P):
            conditional_mean = Fraction(0)
            for letter, weight in ((0, p), (1, q)):
                next_state, reward = LUMP_TRANSITION[state, letter]
                difference = reward - mu + h[next_state] - h[state]
                conditional_mean += weight * difference
                martingale_variance += pi[state] * weight * difference**2
            check(conditional_mean == 0,
                  ("martingale difference", p, state, conditional_mean),
                  "poisson")
        check(martingale_variance == variance,
              ("martingale variance", p, martingale_variance, variance),
              "variance")
        check(variance > 0,
              ("positive variance", p, variance), "variance")

        # Independent implicit-Perron derivative calculation at t=0.
        rho_prime = 3 * a / (2 + a)
        rho_second = -(6 * rho_prime**2 - 4 * a * rho_prime - 5 * a) / (2 + a)
        check(rho_prime == mu,
              ("first Perron derivative", p), "perron_derivatives")
        check(rho_second - rho_prime**2 == variance,
              ("second Perron derivative", p, rho_second, variance),
              "perron_derivatives")

        for r in r_values:
            for y in y_values:
                check(direct_characteristic(r, y, p)
                      == closed_characteristic(r, y, p),
                      ("characteristic cubic", p, r, y), "cubic")

                # Similarity used at the negative-temperature edge.
                kernel = tilted_kernel(p, y)
                diagonal = (Fraction(1, 1) / y, Fraction(1),
                            Fraction(1, 1) / y)
                conjugated = tuple(
                    tuple(kernel[i][j] * diagonal[j] / diagonal[i]
                          for j in range(3))
                    for i in range(3)
                )
                expected_conjugated = (
                    (0, p, q * y),
                    (p, 0, q),
                    (p * y, q, 0),
                )
                check(conjugated == expected_conjugated,
                      ("negative-edge similarity", p, y, conjugated),
                      "zero_temperature")

        check(closed_characteristic(Fraction(1), Fraction(1), p) == 0,
              ("Perron root at zero tilt", p), "cubic")
        check(1 - 2 * a == p * p + q * q,
              ("negative edge radicand", p), "zero_temperature")
        check(1 - 2 * a > 0,
              ("positive negative-edge radicand", p),
              "zero_temperature")

        # Limiting characteristic polynomials after the two exact scalings.
        for r in r_values:
            negative_limit = r**3 + (2 * a - 1) * r
            check(negative_limit == r * (r**2 - (1 - 2 * a)),
                  ("negative-edge polynomial", p, r),
                  "zero_temperature")
            positive_limit = r**3 - a * r
            check(positive_limit == r * (r**2 - a),
                  ("positive-edge polynomial", p, r),
                  "zero_temperature")


def run_strong_lumping_local_lane():
    # Check the claimed common transition/reward for both representatives
    # in each nonzero lump directly from literal max-plus vector updates.
    representatives = {N: (-3, -2), Z: (0,), P: (2, 3)}
    for state, gaps in representatives.items():
        for letter in (0, 1):
            claimed_state, claimed_reward = LUMP_TRANSITION[state, letter]
            images = set()
            for gap in gaps:
                direct_vector = tropical_matvec(GENERATORS[letter], (gap, 0))
                new_gap = direct_vector[0] - direct_vector[1]
                reward = max(direct_vector) - max(gap, 0)
                check((new_gap, reward) == GAP_TRANSITION[gap, letter],
                      ("literal local gap", gap, letter,
                       (new_gap, reward), GAP_TRANSITION[gap, letter]),
                      "five_gap")
                images.add((lump(new_gap), reward))
            check(images == {(claimed_state, claimed_reward)},
                  ("local strong lumping", state, letter, images,
                   (claimed_state, claimed_reward)), "strong_lumping")


def run():
    run_strong_lumping_local_lane()
    run_reset_lane()
    enum_horizon, total_words = run_literal_lane()
    run_generator_lane()
    law_horizon, probabilities = run_biased_lane()
    run_spectral_lane()

    print("max-plus switching-induced-growth verifier: PASS")
    print(f"exact assertions: {ASSERTIONS:,}")
    print(f"literal words: {total_words:,} through n <= {enum_horizon}")
    print(f"biased law/PGF horizon: n <= {law_horizon}")
    print("probabilities: " + ", ".join(str(p) for p in probabilities))
    print("arithmetic: integers and fractions.Fraction only")
    print("orientation sentinel: A,A,B product differs from B,A,A")
    print("endpoint sentinel: H_n(A^n)=H_n(B^n)=n mod 2")
    print("reset sentinel: no reset through length 2; ABA/ABB/BAA/BAB only at length 3")
    print("support sentinel: every parity-compatible height is attained")
    print("rare-event sentinel: exactly two alternating maximizers for n >= 1")
    print("lane assertions:")
    for lane in sorted(LANES):
        print(f"  {lane}: {LANES[lane]:,}")


if __name__ == "__main__":
    run()
