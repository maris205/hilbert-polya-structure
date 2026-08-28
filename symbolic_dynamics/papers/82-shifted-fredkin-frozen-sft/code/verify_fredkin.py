#!/usr/bin/env python3
"""Exact controls for the two-layer shifted Fredkin ring.

The script implements the literal three-bit controlled-swap rule, exhausts
every state for m=1,...,6, and independently checks the frozen-set transfer
matrix.  It uses only the Python standard library.  The finite computation is
a regression control, not a proof of the all-m theorems in main.tex.
"""

from collections import Counter
from fractions import Fraction


MATRIX = (
    (1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1),
    (1, 0, 1, 0, 1, 0, 1, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (1, 1, 1, 1, 1, 1, 1, 1),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 1, 0, 1, 0, 1, 0, 1),
    (0, 1, 0, 1, 0, 1, 0, 1),
)


EXPECTED_CYCLE_TYPES = {
    1: {1: 5, 3: 1},
    2: {1: 19, 2: 9, 3: 5, 4: 3},
    3: {1: 80, 2: 75, 3: 46, 4: 15, 6: 6, 8: 6},
    4: {
        1: 343,
        2: 537,
        3: 321,
        4: 149,
        6: 108,
        8: 24,
        10: 2,
        12: 2,
        14: 2,
        16: 4,
        18: 8,
    },
    5: {
        1: 1475,
        2: 3600,
        3: 2101,
        4: 1200,
        6: 1240,
        8: 230,
        10: 5,
        12: 75,
        16: 35,
        18: 105,
        30: 5,
        32: 5,
    },
    6: {
        1: 6346,
        2: 23433,
        3: 13432,
        4: 9273,
        6: 12078,
        8: 1872,
        10: 3,
        12: 1314,
        16: 336,
        18: 966,
        24: 96,
        30: 6,
        32: 48,
        54: 24,
        74: 3,
    },
}


CHECK_COUNT = 0


def check(condition, message):
    """Count and execute one explicit control assertion."""

    global CHECK_COUNT
    CHECK_COUNT += 1
    if not condition:
        raise AssertionError(message)


def bit(state, site):
    return (state >> site) & 1


def fredkin(state, control, target_left, target_right):
    """Apply the paper's explicitly defined control-on-one conditional swap."""

    if bit(state, control) and bit(state, target_left) != bit(state, target_right):
        state ^= (1 << target_left) | (1 << target_right)
    return state


def layer_a(state, m):
    for block in range(m):
        state = fredkin(state, 3 * block, 3 * block + 1, 3 * block + 2)
    return state


def layer_b(state, m):
    sites = 3 * m
    for block in range(m):
        state = fredkin(
            state,
            3 * block + 1,
            3 * block + 2,
            (3 * block + 3) % sites,
        )
    return state


def update(state, m):
    return layer_b(layer_a(state, m), m)


def inverse_update(state, m):
    return layer_a(layer_b(state, m), m)


def block_tuple(state, block):
    return tuple(bit(state, 3 * block + offset) for offset in range(3))


def block_index(block):
    a, b, c = block
    return a + 2 * b + 4 * c


def local_allowed(left, right):
    """Literal fixed condition for the shifted gate across one boundary."""

    a, b, c = left
    d, _, _ = right
    beta, gamma = (b, c) if a == 0 else (c, b)
    if beta == 0:
        return (beta, gamma, d) == (b, c, d)
    return (beta, d, gamma) == (b, c, d)


def accepted_by_sft(state, m):
    indices = [block_index(block_tuple(state, block)) for block in range(m)]
    return all(MATRIX[indices[block]][indices[(block + 1) % m]] for block in range(m))


def matrix_product(left, right):
    rows = len(left)
    middle = len(right)
    columns = len(right[0])
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(middle)) for j in range(columns))
        for i in range(rows)
    )


def matrix_power(matrix, exponent):
    size = len(matrix)
    result = tuple(tuple(int(i == j) for j in range(size)) for i in range(size))
    base = matrix
    while exponent:
        if exponent & 1:
            result = matrix_product(result, base)
        base = matrix_product(base, base)
        exponent >>= 1
    return result


def trace_power(exponent):
    powered = matrix_power(MATRIX, exponent)
    return sum(powered[i][i] for i in range(len(MATRIX)))


def rational_rank(matrix):
    work = [[Fraction(entry) for entry in row] for row in matrix]
    rows = len(work)
    columns = len(work[0])
    pivot_row = 0
    for column in range(columns):
        pivot = next((row for row in range(pivot_row, rows) if work[row][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][column]
        work[pivot_row] = [entry / scale for entry in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [
                entry - factor * pivot_entry
                for entry, pivot_entry in zip(work[row], work[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def recurrence_count(m):
    if m == 1:
        return 5
    if m == 2:
        return 19
    previous_two, previous_one = 5, 19
    for _ in range(3, m + 1):
        previous_two, previous_one = previous_one, 5 * previous_one - 3 * previous_two
    return previous_one


def cycle_type(images):
    seen = [False] * len(images)
    cycles = Counter()
    for start in range(len(images)):
        if seen[start]:
            continue
        current = start
        length = 0
        while not seen[current]:
            seen[current] = True
            current = images[current]
            length += 1
        check(current == start, "a component of the alleged permutation did not close at its start")
        cycles[length] += 1
    return cycles


def audit_transfer_matrix():
    check(len(MATRIX) == 8, "transfer matrix must have eight rows")
    for row in MATRIX:
        check(len(row) == 8, "transfer matrix must have eight columns")
        for entry in row:
            check(entry in (0, 1), "transfer matrix must be binary")

    for left_index in range(8):
        left = (left_index & 1, (left_index >> 1) & 1, (left_index >> 2) & 1)
        for right_index in range(8):
            right = (
                right_index & 1,
                (right_index >> 1) & 1,
                (right_index >> 2) & 1,
            )
            check(
                MATRIX[left_index][right_index] == int(local_allowed(left, right)),
                "explicit matrix disagrees with the literal local boundary rule",
            )

    check(rational_rank(MATRIX) == 2, "transfer matrix rank is not two")
    check(trace_power(1) == 5, "trace M is not five")
    check(trace_power(2) == 19, "trace M^2 is not nineteen")
    for exponent in range(1, 13):
        check(
            trace_power(exponent) == recurrence_count(exponent),
            "matrix traces disagree with the claimed recurrence",
        )


def audit_ring(m):
    size = 1 << (3 * m)
    images = []
    for state in range(size):
        after_a = layer_a(state, m)
        after_b = layer_b(state, m)
        image = update(state, m)

        check(layer_a(after_a, m) == state, "aligned layer is not involutive")
        check(layer_b(after_b, m) == state, "shifted layer is not involutive")
        check(inverse_update(image, m) == state, "explicit inverse failed")
        check(
            layer_a(update(layer_a(state, m), m), m) == inverse_update(state, m),
            "A T A does not equal the inverse",
        )
        check(image.bit_count() == state.bit_count(), "Hamming weight was not conserved")
        check(
            (image == state) == accepted_by_sft(state, m),
            "literal fixed condition disagrees with the SFT",
        )
        images.append(image)

    check(len(set(images)) == size, "global update is not bijective")
    cycles = cycle_type(images)
    check(sum(period * count for period, count in cycles.items()) == size, "cycle census lost states")

    literal_fixed = sum(image == state for state, image in enumerate(images))
    expected_fixed = trace_power(m)
    check(literal_fixed == expected_fixed, "literal and transfer fixed counts disagree")
    check(cycles[1] == expected_fixed, "cycle census has the wrong fixed count")
    check(dict(sorted(cycles.items())) == EXPECTED_CYCLE_TYPES[m], "cycle-type regression changed")
    return size, expected_fixed, cycles


def main():
    audit_transfer_matrix()
    rows = []
    for m in range(1, 7):
        rows.append((m, *audit_ring(m)))

    total_states = sum(row[1] for row in rows)
    check(total_states == 299_592, "unexpected exhaustive state total")

    print("PASS transfer-matrix local-rule/rank/trace controls")
    print("PASS exhaustive shifted-Fredkin controls for m=1,...,6")
    for m, size, fixed, cycles in rows:
        cycle_text = ", ".join(f"{period}:{cycles[period]}" for period in sorted(cycles))
        print(
            f"m={m} states={size} fixed={fixed} "
            f"max_period={max(cycles)} cycles={{" + cycle_text + "}"
        )
    print(f"TOTAL_STATES={total_states}")
    print(f"ASSERTIONS={CHECK_COUNT}")


if __name__ == "__main__":
    main()
