#!/usr/bin/env python3
"""Exact controls for the critical-Jordan block substitution."""

from collections import Counter


SUBSTITUTION = {
    "A": (("A", "A"), ("B", "C")),
    "B": (("B", "B"), ("B", "C")),
    "C": (("A", "C"), ("C", "C")),
}
INCIDENCE = ((2, 0, 1), (1, 3, 0), (1, 1, 3))


def matmul(left, right):
    rows = len(left)
    middle = len(right)
    columns = len(right[0])
    return tuple(
        tuple(
            sum(left[row][inner] * right[inner][column] for inner in range(middle))
            for column in range(columns)
        )
        for row in range(rows)
    )


def matrix_power(matrix, exponent):
    size = len(matrix)
    answer = tuple(
        tuple(int(row == column) for column in range(size)) for row in range(size)
    )
    for _ in range(exponent):
        answer = matmul(answer, matrix)
    return answer


def substitute(grid):
    height, width = len(grid), len(grid[0])
    output = [[None] * (2 * width) for _ in range(2 * height)]
    for row in range(height):
        for column in range(width):
            block = SUBSTITUTION[grid[row][column]]
            for delta_row in range(2):
                for delta_column in range(2):
                    output[2 * row + delta_row][2 * column + delta_column] = block[
                        delta_row
                    ][delta_column]
    return tuple(tuple(row) for row in output)


def iterate(letter, level):
    grid = ((letter,),)
    for _ in range(level):
        grid = substitute(grid)
    return grid


def patches(grid, size):
    return {
        tuple(
            tuple(grid[row + delta][column : column + size])
            for delta in range(size)
        )
        for row in range(len(grid) - size + 1)
        for column in range(len(grid[0]) - size + 1)
    }


def counts(grid):
    counter = Counter(symbol for row in grid for symbol in row)
    return tuple(counter[symbol] for symbol in "ABC")


def discrepancy(grid):
    counter = Counter(symbol for row in grid for symbol in row)
    return counter["A"] - counter["B"]


def field(grid):
    weight = {"A": 1, "B": -1, "C": 0}
    return tuple(tuple(weight[symbol] for symbol in row) for row in grid)


def characteristic_coefficients_3(matrix):
    """Return trace, sum of principal 2-minors, and determinant."""
    trace = sum(matrix[index][index] for index in range(3))
    principal_two = (
        matrix[0][0] * matrix[1][1]
        - matrix[0][1] * matrix[1][0]
        + matrix[0][0] * matrix[2][2]
        - matrix[0][2] * matrix[2][0]
        + matrix[1][1] * matrix[2][2]
        - matrix[1][2] * matrix[2][1]
    )
    determinant = (
        matrix[0][0]
        * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1]
        * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2]
        * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )
    return trace, principal_two, determinant


def main():
    # Direct matrix identities: characteristic polynomial is
    # (x-4)(x-2)^2, f M = 2 f + g, and g M = 2 g.
    computed_incidence = tuple(
        tuple(counts(SUBSTITUTION[parent])[row] for parent in "ABC")
        for row in range(3)
    )
    assert computed_incidence == INCIDENCE
    f = ((1, -1, 0),)
    g = ((-1, -1, 1),)
    assert matmul(f, INCIDENCE) == ((1, -3, 1),)
    assert matmul(g, INCIDENCE) == ((-2, -2, 2),)
    assert matrix_power(INCIDENCE, 2) == ((5, 1, 5), (5, 9, 1), (6, 6, 10))
    assert characteristic_coefficients_3(INCIDENCE) == (8, 20, 16)
    assert matmul(INCIDENCE, ((1,), (1,), (2,))) == ((4,), (4,), (8,))

    for level in range(33):
        jordan_term = level * (2 ** (level - 1)) if level else 0
        expected = (
            2**level - jordan_term,
            -(2**level) - jordan_term,
            jordan_term,
        )
        observed = matmul(f, matrix_power(INCIDENCE, level))[0]
        assert observed == expected

    for level in range(9):
        jordan_term = level * (2 ** (level - 1)) if level else 0
        expected = (
            2**level - jordan_term,
            -(2**level) - jordan_term,
            jordan_term,
        )
        assert tuple(discrepancy(iterate(letter, level)) for letter in "ABC") == expected
        a_field = field(iterate("A", level))
        b_field = field(iterate("B", level))
        c_field = field(iterate("C", level))
        side = 2**level
        exceptional = (0, side - 1)
        for row in range(side):
            for column in range(side):
                assert b_field[row][column] <= a_field[row][column]
                assert b_field[row][column] <= c_field[row][column]
                difference = a_field[row][column] - c_field[row][column]
                if (row, column) == exceptional:
                    assert difference == 1
                else:
                    assert difference <= 0

    # A finite, exhaustive recognizability certificate.  Legal 2x2 patches
    # form a substitution-closed set of size 20.  Every legal 3x3 patch is
    # obtained inside the substituted image of one of those patches.
    legal_two = set(SUBSTITUTION.values())
    closure_sizes = [len(legal_two)]
    while True:
        next_legal_two = legal_two | set().union(
            *(patches(substitute(patch), 2) for patch in legal_two)
        )
        closure_sizes.append(len(next_legal_two))
        if next_legal_two == legal_two:
            break
        legal_two = next_legal_two
    assert closure_sizes == [3, 13, 20, 20]

    by_phase = {(row, column): set() for row in range(2) for column in range(2)}
    for patch in legal_two:
        image = substitute(patch)
        for row in range(2):
            for column in range(2):
                by_phase[(row, column)].add(
                    tuple(
                        tuple(image[row + delta][column : column + 3])
                        for delta in range(3)
                    )
                )
    for phase, phase_patches in by_phase.items():
        for other, other_patches in by_phase.items():
            if phase != other:
                assert phase_patches.isdisjoint(other_patches)
    phase_counts = {phase: len(phase_patches) for phase, phase_patches in by_phase.items()}
    assert phase_counts == {(0, 0): 18, (0, 1): 20, (1, 0): 15, (1, 1): 10}
    assert len(set().union(*by_phase.values())) == 63

    print("PASS: incidence primitivity and Jordan-chain identities")
    print("PASS: exact supertile discrepancy through level 32")
    print("PASS: pointwise periodic-envelope identity through level 8")
    print("legal 2x2 closure sizes:", closure_sizes)
    print("legal 3x3 patches by phase:", phase_counts)
    print("PASS: four phase languages are pairwise disjoint")


if __name__ == "__main__":
    main()
