#!/usr/bin/env python3
"""Exact Phase-2b pilot: uniform active-edge greedy matching on a staircase board."""

from fractions import Fraction
from functools import lru_cache
from math import factorial


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def staircase_board(order):
    return frozenset((row, column) for row in range(order) for column in range(row + 1))


@lru_cache(maxsize=None)
def matching_size_law(board):
    if not board:
        return {0: Fraction(1)}
    weight = Fraction(1, len(board))
    answer = {}
    for row, column in board:
        nxt = frozenset(
            (other_row, other_column)
            for other_row, other_column in board
            if other_row != row and other_column != column
        )
        check(len(nxt) < len(board), (board, row, column))
        for size, mass in matching_size_law(nxt).items():
            answer[size + 1] = answer.get(size + 1, Fraction(0)) + weight * mass
    return dict(sorted(answer.items()))


def perfect_probability(order):
    return Fraction(2**order, factorial(order + 1))


def run():
    for order in range(1, 11):
        law = matching_size_law(staircase_board(order))
        check(sum(law.values(), Fraction(0)) == 1, (order, law))
        check(tuple(law) == tuple(range((order + 1) // 2, order + 1)), (order, law))
        check(law[order] == perfect_probability(order), (order, law[order]))

        # Independent hazard product: conditional on having selected only
        # diagonal edges, an induced staircase on r surviving indices has r
        # safe diagonal edges among r(r+1)/2 active edges.
        hazard = Fraction(1)
        for survivors in range(order, 0, -1):
            hazard *= Fraction(2, survivors + 1)
        check(hazard == law[order], (order, hazard, law[order]))

    check(
        matching_size_law(staircase_board(4))
        == {
            2: Fraction(31, 300),
            3: Fraction(229, 300),
            4: Fraction(2, 15),
        },
        "order-four sentinel",
    )
    check(
        len(set(matching_size_law(staircase_board(4)).values())) == 3,
        "uniform-size guess survived",
    )

    print("stoch_phase2b_ferrers_greedy: PASS")
    print(f"assertions={ASSERTIONS}")
    print(f"states={matching_size_law.cache_info().currsize}")
    print("support=ceil(n/2),...,n checked_n<=10")
    print("perfect_atom=2^n/(n+1)! checked_n<=10")
    print("killed_guess=uniform_matching_size_law")


if __name__ == "__main__":
    run()
