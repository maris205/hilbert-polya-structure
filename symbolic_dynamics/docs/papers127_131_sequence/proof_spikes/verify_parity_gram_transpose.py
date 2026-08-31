#!/usr/bin/env python3
"""Exact verifier for the binary parity--Gram transpose map.

For A in M_n(F_2), put r=A1 and

    Phi(A) = A^T + r r^T.

The script exhausts n<=4 and checks the proposed quotient, image, fibres,
depth layers, periods, and component census using integer bit arithmetic.
"""

from __future__ import annotations

from collections import Counter


ASSERTIONS = 0


def check(condition: bool, message: str = "") -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message or f"assertion {ASSERTIONS} failed")


def bit(mask: int, n: int, i: int, j: int) -> int:
    return mask >> (i * n + j) & 1


def margins(mask: int, n: int):
    row = tuple(sum(bit(mask, n, i, j) for j in range(n)) & 1 for i in range(n))
    col = tuple(sum(bit(mask, n, i, j) for i in range(n)) & 1 for j in range(n))
    total = sum(row) & 1
    check(total == (sum(col) & 1))
    return row, col, total


def transpose(mask: int, n: int) -> int:
    answer = 0
    for i in range(n):
        for j in range(n):
            answer |= bit(mask, n, j, i) << (i * n + j)
    return answer


def outer(vector, n: int) -> int:
    answer = 0
    for i in range(n):
        for j in range(n):
            answer |= (vector[i] & vector[j]) << (i * n + j)
    return answer


def phi(mask: int, n: int) -> int:
    row, _col, _total = margins(mask, n)
    return transpose(mask, n) ^ outer(row, n)


def orbit(mask: int, n: int):
    seen = {}
    x = mask
    while x not in seen:
        seen[x] = len(seen)
        x = phi(x, n)
    return seen[x], len(seen) - seen[x]


def vector_xor(a, b):
    return tuple(x ^ y for x, y in zip(a, b))


def main() -> None:
    for n in range(1, 5):
        states = range(1 << (n * n))
        fibres = Counter()
        orbit_census = Counter()
        margin_census = Counter()
        fixed = 0

        for matrix in states:
            row, col, total = margins(matrix, n)
            image = phi(matrix, n)
            image_row, image_col, image_total = margins(image, n)

            # Quotient law: total parity falls to zero; on the even slice,
            # row and column parities swap.
            check(image_total == 0)
            predicted_row = vector_xor(col, row) if total else col
            predicted_col = (0,) * n if total else row
            # For total one, c' = r + total*r = 0.
            check(image_row == predicted_row)
            check(image_col == predicted_col)

            second = phi(image, n)
            if total == 0:
                check(second == (matrix ^ outer(row, n) ^ outer(col, n)))
                check(phi(phi(second, n), n) == matrix)

            tail, period = orbit(matrix, n)
            check(tail == total)
            check(period in (1, 2, 4))
            if total == 0 and row != col:
                check(period == 4)
            if total == 0 and row == col:
                check(period in (1, 2))

            fibres[image] += 1
            orbit_census[tail, period] += 1
            if total == 0:
                margin_census[row, col] += 1
            fixed += image == matrix

        all_states = 1 << (n * n)
        recurrent = 1 << (n * n - 1)
        equal_margin = 1 << (n * (n - 1))
        fixed_formula = 1 << (n * (n - 1) // 2)
        two_cycles = (equal_margin - fixed_formula) // 2
        four_cycles = (recurrent - equal_margin) // 4

        check(len(fibres) == recurrent)
        check(sum(fibres.values()) == all_states)
        check(fixed == fixed_formula)
        check(orbit_census[0, 1] == fixed_formula)
        check(orbit_census[0, 2] == 2 * two_cycles)
        check(orbit_census[0, 4] == 4 * four_cycles)
        check(sum(count for (tail, _period), count in orbit_census.items() if tail == 1) == recurrent)

        # Every feasible even row/column margin pair has the standard affine
        # dimension (n-1)^2.
        expected_per_margin = 1 << ((n - 1) * (n - 1))
        check(len(margin_census) == 1 << (2 * n - 2))
        check(set(margin_census.values()) == {expected_per_margin})

        # Exact one-step fibre law.  A target with zero column parity has one
        # even preimage and 2^(n-1) odd preimages; every other image target has
        # its unique even preimage.
        large_fibre_targets = 0
        for target, count in fibres.items():
            _row, col, total = margins(target, n)
            check(total == 0)
            expected = (1 << (n - 1)) + 1 if not any(col) else 1
            check(count == expected)
            large_fibre_targets += not any(col)
        check(large_fibre_targets == 1 << (n * (n - 1)))

        print(
            f"n={n} states={all_states} image={recurrent} depth1={recurrent} "
            f"fixed={fixed_formula} two_cycles={two_cycles} "
            f"four_cycles={four_cycles} large_fibre_targets={large_fibre_targets} "
            f"large_fibre={(1 << (n - 1)) + 1}"
        )

    print(f"ASSERTIONS={ASSERTIONS}")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
