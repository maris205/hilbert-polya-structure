#!/usr/bin/env python3
"""Exact finite controls for the commutation-transfer theorem.

Three counters are compared.  The torus-edge counter is deliberately
independent of the boundary-word and transfer-matrix implementations.
"""

from collections import Counter
from itertools import permutations, product


DOMAIN = [(0, 0), (0, 1), (1, 0), (1, 1)]
CODOMAIN = [(0, 0), (0, 1), (1, 0), (1, 1)]


def commute_one(theta, blue_word, red_letter):
    output_blue = [None] * len(blue_word)
    output_red = red_letter
    for position in range(len(blue_word) - 1, -1, -1):
        output_red, output_blue[position] = theta[
            (blue_word[position], output_red)
        ]
    return output_red, tuple(output_blue)


def commute_block(theta, blue_word, red_word):
    output_red = []
    for red_letter in red_word:
        red_letter_out, blue_word = commute_one(
            theta, blue_word, red_letter
        )
        output_red.append(red_letter_out)
    return tuple(output_red), blue_word


def boundary_pair_count(theta, width, height):
    return sum(
        commute_block(theta, blue_word, red_word)
        == (red_word, blue_word)
        for blue_word in product(range(2), repeat=width)
        for red_word in product(range(2), repeat=height)
    )


def transfer_matrix(theta, width):
    words = list(product(range(2), repeat=width))
    position = {word: row for row, word in enumerate(words)}
    matrix = [[0] * len(words) for _ in words]
    for word in words:
        for red_letter in range(2):
            output_red, output_word = commute_one(theta, word, red_letter)
            if output_red == red_letter:
                matrix[position[word]][position[output_word]] += 1
    return matrix


def multiply(left, right):
    size = len(left)
    return [
        [
            sum(left[row][mid] * right[mid][column] for mid in range(size))
            for column in range(size)
        ]
        for row in range(size)
    ]


def trace_power(matrix, exponent):
    size = len(matrix)
    power = [[int(row == column) for column in range(size)] for row in range(size)]
    for _ in range(exponent):
        power = multiply(power, matrix)
    return sum(power[row][row] for row in range(size))


def direct_torus_count(theta, width, height):
    """Enumerate edge labels and check only the local square relations."""

    cells = [(column, row) for row in range(height) for column in range(width)]
    answer = 0
    for labels in product(range(2), repeat=2 * width * height):
        horizontal = dict(zip(cells, labels[: width * height]))
        vertical = dict(zip(cells, labels[width * height :]))
        valid = all(
            theta[
                (
                    horizontal[(column, row)],
                    vertical[((column + 1) % width, row)],
                )
            ]
            == (
                vertical[(column, row)],
                horizontal[(column, (row + 1) % height)],
            )
            for column, row in cells
        )
        answer += valid
    return answer


def main():
    profiles = []
    checks = 0
    all_permutations = list(permutations(CODOMAIN))
    for permutation in all_permutations:
        theta = dict(zip(DOMAIN, permutation))
        profile = []
        for width in range(1, 4):
            matrix = transfer_matrix(theta, width)
            for height in range(1, 4):
                boundary = boundary_pair_count(theta, width, height)
                transfer = trace_power(matrix, height)
                torus = direct_torus_count(theta, width, height)
                assert boundary == transfer == torus
                profile.append(boundary)
                checks += 1
        profiles.append(tuple(profile))

    identity = ((0, 0), (1, 0), (0, 1), (1, 1))
    chosen_cycle = ((0, 1), (1, 1), (1, 0), (0, 0))
    identity_profile = profiles[all_permutations.index(identity)]
    cycle_profile = profiles[all_permutations.index(chosen_cycle)]
    assert identity_profile == (4, 8, 16, 8, 16, 32, 16, 32, 64)
    assert cycle_profile == (0, 0, 0, 0, 8, 0, 0, 0, 0)

    print(f"PASS: {checks}/216 theta-size triples")
    print("distinct truncated profiles:", len(set(profiles)))
    print("profile-class multiplicities:", sorted(Counter(profiles).values()))
    print("identity profile:", identity_profile)
    print("chosen 4-cycle profile:", cycle_profile)


if __name__ == "__main__":
    main()
