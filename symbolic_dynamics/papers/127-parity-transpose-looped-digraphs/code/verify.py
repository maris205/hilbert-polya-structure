#!/usr/bin/env python3
"""Deterministic exact verifier for P127.

All calculations use integer bit masks.  The run exhausts every binary
matrix for 1 <= n <= 4 and every possible codomain target, and separately
checks the transvection/projection factorisation.
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
    return (mask >> (i * n + j)) & 1


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


def left_factor_form(mask: int, n: int) -> int:
    # (I + r 1^T) A^T: row i of A^T is toggled by r_i times the XOR
    # of every row of A^T, which is r^T.
    row, _col, _total = margins(mask, n)
    answer = transpose(mask, n)
    for i in range(n):
        if row[i]:
            for j in range(n):
                answer ^= row[j] << (i * n + j)
    return answer


def vector_xor(a, b):
    return tuple(x ^ y for x, y in zip(a, b))


def orbit(mask: int, n: int):
    seen = {}
    value = mask
    while value not in seen:
        seen[value] = len(seen)
        value = phi(value, n)
    return seen[value], len(seen) - seen[value]


def main() -> None:
    print("P127_PARITY_TRANSPOSE_EXACT_CONTROL")
    print("arithmetic=integer bit masks over F2; randomness=none")
    for n in range(1, 5):
        count = 1 << (n * n)
        fibres = Counter()
        orbit_census = Counter()
        margin_census = Counter()

        for matrix in range(count):
            row, col, total = margins(matrix, n)
            image = phi(matrix, n)
            check(image == left_factor_form(matrix, n))
            image_row, image_col, image_total = margins(image, n)
            check(image_total == 0)
            check(image_row == (vector_xor(col, row) if total else col))
            check(image_col == ((0,) * n if total else row))

            if total == 0:
                second = phi(image, n)
                check(second == (matrix ^ outer(row, n) ^ outer(col, n)))
                check(phi(phi(second, n), n) == matrix)

            tail, period = orbit(matrix, n)
            check(tail == total)
            check(period in (1, 2, 4))
            if not total and row != col:
                check(period == 4)
            if not total and row == col:
                check(period in (1, 2))

            fibres[image] += 1
            orbit_census[tail, period] += 1
            if not total:
                margin_census[row, col] += 1

        recurrent = 1 << (n * n - 1)
        equal_margin = 1 << (n * (n - 1))
        fixed = 1 << (n * (n - 1) // 2)
        two_cycles = (equal_margin - fixed) // 2
        four_cycles = (recurrent - equal_margin) // 4

        # Codomain-wide fibre law, including every zero-fibre target.
        zero_targets = unit_targets = large_targets = 0
        for target in range(count):
            _tr, target_col, target_total = margins(target, n)
            expected = 0
            if target_total == 0:
                expected = (1 << (n - 1)) + 1 if not any(target_col) else 1
            check(fibres[target] == expected)
            zero_targets += expected == 0
            unit_targets += expected == 1
            large_targets += expected > 1

        check(zero_targets == recurrent)
        check(large_targets == 1 << (n * (n - 1)))
        check(unit_targets + large_targets == recurrent)
        check(len(fibres) == recurrent)
        check(sum(fibres.values()) == count)

        expected_margin_size = 1 << ((n - 1) * (n - 1))
        check(len(margin_census) == 1 << (2 * n - 2))
        check(set(margin_census.values()) == {expected_margin_size})
        check(orbit_census[0, 1] == fixed)
        check(orbit_census[0, 2] == 2 * two_cycles)
        check(orbit_census[0, 4] == 4 * four_cycles)
        check(sum(v for (tail, _period), v in orbit_census.items() if tail == 1) == recurrent)

        print(
            f"n={n} states={count} image={recurrent} zero_targets={zero_targets} "
            f"unit_targets={unit_targets} large_targets={large_targets} "
            f"large_fibre={(1 << (n - 1)) + 1} fixed={fixed} "
            f"cycles2={two_cycles} cycles4={four_cycles}"
        )

    print(f"ASSERTIONS={ASSERTIONS}")
    print("STATUS=PASS")
    print("scope_sentinel=bounded enumeration is falsification evidence, never proof")
    print("release_sentinel=bounded owner non-hit is not novelty; external HOLD")


if __name__ == "__main__":
    main()
