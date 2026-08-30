#!/usr/bin/env python3
"""Exact pilot for a legal-schedule abelian queue with one local defect."""

from fractions import Fraction
from functools import lru_cache
from math import comb


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def legal_successors(state):
    x_count, y_count = state
    out = []
    if x_count > 0:
        out.append(("A", (x_count - 1, y_count + 1)))
    if y_count > 0:
        if state == (1, 1):
            out.append(("B*", (0, 0)))
        else:
            out.append(("B", (x_count, y_count - 1)))
    return tuple(out)


@lru_cache(maxsize=None)
def absorption_law(state):
    if state == (0, 0):
        return {0: Fraction(1)}
    moves = legal_successors(state)
    answer = {}
    weight = Fraction(1, len(moves))
    for _, nxt in moves:
        for time, probability in absorption_law(nxt).items():
            answer[time + 1] = answer.get(time + 1, Fraction(0)) + weight * probability
    return dict(sorted(answer.items()))


@lru_cache(maxsize=None)
def defect_probability(state):
    if state == (0, 0):
        return Fraction(0)
    moves = legal_successors(state)
    answer = Fraction(0)
    for label, nxt in moves:
        answer += Fraction(1, len(moves)) * (
            Fraction(1) if label == "B*" else defect_probability(nxt)
        )
    return answer


def frontier_distribution(n_value):
    """Queue length immediately after x first reaches 1, before the defect is active."""
    active = {(n_value, 0): Fraction(1)}
    frontier = {}
    while active:
        nxt_layer = {}
        for (x_count, y_count), probability in active.items():
            if x_count == 1:
                frontier[y_count] = frontier.get(y_count, Fraction(0)) + probability
                continue
            moves = [(x_count - 1, y_count + 1)]
            if y_count > 0:
                moves.append((x_count, y_count - 1))
            for nxt in moves:
                nxt_layer[nxt] = nxt_layer.get(nxt, Fraction(0)) + probability / len(moves)
        active = nxt_layer
    return dict(sorted(frontier.items()))


def central_probability(n_value):
    return Fraction(comb(2 * n_value - 2, n_value - 1), 4 ** (n_value - 1))


def run():
    check(absorption_law((0, 0)) == {0: Fraction(1)}, "n=0 orientation")
    check(absorption_law((1, 0)) == {2: Fraction(1)}, "n=1 endpoint")
    check(defect_probability((1, 0)) == 0, "defect unreachable from (1,0)")

    previous = None
    probabilities = []
    for n_value in range(2, 25):
        rho = central_probability(n_value)
        probabilities.append(rho)
        law = absorption_law((n_value, 0))
        expected_law = {2 * n_value - 2: rho, 2 * n_value: 1 - rho}
        check(law == expected_law, (n_value, law, expected_law))
        check(defect_probability((n_value, 0)) == rho, (n_value, rho))
        check(sum(law.values(), Fraction(0)) == 1, (n_value, law))
        mean = sum(time * mass for time, mass in law.items())
        variance = sum((time - mean) ** 2 * mass for time, mass in law.items())
        check(mean == 2 * n_value - 2 * rho, (n_value, mean))
        check(variance == 4 * rho * (1 - rho), (n_value, variance))

        frontier = frontier_distribution(n_value)
        check(sum(frontier.values(), Fraction(0)) == 1, (n_value, frontier))
        check(all(queue >= 1 for queue in frontier), (n_value, frontier))
        from_frontier = sum(mass * Fraction(1, 2**queue) for queue, mass in frontier.items())
        check(from_frontier == rho, (n_value, frontier, rho))

        if previous is not None:
            check(rho / previous == Fraction(2 * n_value - 3, 2 * n_value - 2), n_value)
        previous = rho

    for queue in range(1, 21):
        check(defect_probability((1, queue)) == Fraction(1, 2**queue), queue)

    check(probabilities[0] != probabilities[1], "defect probability is not constant")
    check(
        probabilities[1] / probabilities[0] != probabilities[2] / probabilities[1],
        "defect probability is not geometric",
    )

    print("stoch_one_defect_queue: PASS")
    print(f"assertions={ASSERTIONS}")
    print("rho_n=binom(2n-2,n-1)/4^(n-1), n>=2")
    print("law(T_n)={2n-2:rho_n, 2n:1-rho_n}")
    print("mean=2n-2rho_n; variance=4rho_n(1-rho_n)")
    print("killed=constant_defect_probability, geometric_defect_probability")


if __name__ == "__main__":
    run()
