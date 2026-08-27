#!/usr/bin/env python3
"""Exact controls for the period-six moving-hole order obstruction."""

from itertools import product

import sympy as sp


A = sp.Matrix([[0, 1, 1], [1, 1, 1], [1, 1, 1]])  # forbid 00
B = sp.Matrix([[1, 1, 1], [1, 0, 1], [1, 1, 1]])  # forbid 11
SCHEDULES = {
    "block": "AAABBB",
    "mixed": "AABABB",
}


def matrix(letter):
    return A if letter == "A" else B


def period_product(schedule):
    answer = sp.eye(3)
    for letter in schedule:
        answer *= matrix(letter)
    return answer


def autonomous_matrix(schedule):
    period = len(schedule)
    answer = sp.zeros(3 * period)
    for phase, letter in enumerate(schedule):
        local = matrix(letter)
        for left in range(3):
            for right in range(3):
                answer[3 * phase + left, 3 * ((phase + 1) % period) + right] = local[left, right]
    return answer


def direct_word_count(schedule, transitions, phase=0):
    count = 0
    for word in product(range(3), repeat=transitions + 1):
        legal = True
        for time in range(transitions):
            local = matrix(schedule[(phase + time) % len(schedule)])
            if not local[word[time], word[time + 1]]:
                legal = False
                break
        count += legal
    return count


def matrix_word_count(schedule, transitions, phase=0):
    answer = sp.eye(3)
    for time in range(transitions):
        answer *= matrix(schedule[(phase + time) % len(schedule)])
    return int(sum(answer))


def rotate(word, amount):
    amount %= len(word)
    return word[amount:] + word[:amount]


def main():
    x, t = sp.symbols("x t")
    expected = {
        "block": x * (x**2 - 392 * x + 16),
        "mixed": x * (x**2 - 364 * x + 4),
    }
    expected_det = {
        "block": 1 - 392 * t**6 + 16 * t**12,
        "mixed": 1 - 364 * t**6 + 4 * t**12,
    }

    assert A.charpoly(x).as_expr() == B.charpoly(x).as_expr()
    count_checks = 0
    for name, schedule in SCHEDULES.items():
        period = period_product(schedule)
        assert sp.factor(period.charpoly(x).as_expr() - expected[name]) == 0
        autonomous = autonomous_matrix(schedule)
        assert sp.factor((sp.eye(18) - t * autonomous).det() - expected_det[name]) == 0
        for amount in range(6):
            rotated = period_product(rotate(schedule, amount))
            assert rotated.charpoly(x).as_expr() == period.charpoly(x).as_expr()
        for phase in range(6):
            for transitions in range(0, 9):
                assert direct_word_count(schedule, transitions, phase) == matrix_word_count(
                    schedule, transitions, phase
                )
                count_checks += 1

    block_radius = 196 + 80 * sp.sqrt(6)
    mixed_radius = 182 + 12 * sp.sqrt(230)
    assert sp.simplify(expected["block"].subs(x, block_radius)) == 0
    assert sp.simplify(expected["mixed"].subs(x, mixed_radius)) == 0
    assert block_radius > mixed_radius
    print("PASS static-hole conjugate characteristic polynomial:", A.charpoly(x).as_expr())
    print(f"PASS direct-word/matrix checks: {count_checks}")
    print("block product characteristic polynomial:", expected["block"])
    print("mixed product characteristic polynomial:", expected["mixed"])
    print("PF radii:", block_radius, mixed_radius)
    print("dimensions:", sp.N(sp.log(block_radius) / (6 * sp.log(3)), 12), sp.N(sp.log(mixed_radius) / (6 * sp.log(3)), 12))


if __name__ == "__main__":
    main()
