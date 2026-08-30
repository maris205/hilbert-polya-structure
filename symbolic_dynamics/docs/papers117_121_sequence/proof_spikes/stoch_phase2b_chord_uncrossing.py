#!/usr/bin/env python3
"""Exact Phase-2b pilot: random parallel uncrossing of chord matchings.

Endpoints are 0,...,2n-1 around a circle.  If (a,c) and (b,d) cross with
a<b<c<d, the chosen pair is replaced by (a,b) and (c,d).  Every probability
is a Fraction and distinct crossing occurrences retain multiplicity.
"""

from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import factorial


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def normalize(edges):
    return tuple(sorted((min(left, right), max(left, right)) for left, right in edges))


def cross(first, second):
    a, c = first
    b, d = second
    return (a < b < c < d) or (b < a < d < c)


def crossing_count(matching):
    return sum(cross(first, second) for first, second in combinations(matching, 2))


def span_potential(matching):
    return sum(right - left for left, right in matching)


def successors(matching):
    answer = []
    for first_index, second_index in combinations(range(len(matching)), 2):
        first = matching[first_index]
        second = matching[second_index]
        if not cross(first, second):
            continue
        a, b, c, d = sorted(first + second)
        remaining = [
            edge
            for index, edge in enumerate(matching)
            if index not in (first_index, second_index)
        ]
        answer.append(normalize(remaining + [(a, b), (c, d)]))
    return tuple(answer)


@lru_cache(maxsize=None)
def joint_law(matching):
    next_states = successors(matching)
    if not next_states:
        return {(matching, 0): Fraction(1)}

    old_crossings = crossing_count(matching)
    old_span = span_potential(matching)
    weight = Fraction(1, len(next_states))
    answer = {}
    for nxt in next_states:
        crossing_drop = old_crossings - crossing_count(nxt)
        span_drop = old_span - span_potential(nxt)
        check(crossing_drop > 0 and crossing_drop % 2 == 1, (matching, nxt, crossing_drop))
        check(span_drop > 0 and span_drop % 2 == 0, (matching, nxt, span_drop))
        for (terminal, time), mass in joint_law(nxt).items():
            key = (terminal, time + 1)
            answer[key] = answer.get(key, Fraction(0)) + weight * mass
    return dict(sorted(answer.items(), key=lambda item: (item[0][1], item[0][0])))


def complete_crossing_matching(chord_count):
    return normalize((index, index + chord_count) for index in range(chord_count))


def adjacent_matching(chord_count):
    return normalize((2 * index, 2 * index + 1) for index in range(chord_count))


def time_law(chord_count):
    answer = {}
    for (_, time), mass in joint_law(complete_crossing_matching(chord_count)).items():
        answer[time] = answer.get(time, Fraction(0)) + mass
    return dict(sorted(answer.items()))


def terminal_law(chord_count):
    answer = {}
    for (terminal, _), mass in joint_law(complete_crossing_matching(chord_count)).items():
        answer[terminal] = answer.get(terminal, Fraction(0)) + mass
    return dict(sorted(answer.items()))


def odd_double_factorial(value):
    answer = 1
    for factor in range(value, 0, -2):
        answer *= factor
    return answer


def longest_atom_conjecture(chord_count):
    denominator = 1
    for size in range(2, chord_count):
        denominator *= odd_double_factorial(2 * size - 1)
    return Fraction(1, denominator)


@lru_cache(maxsize=None)
def unit_drop_history_count(matching):
    """Count occurrence-labelled histories that remove one crossing per move."""
    old_crossings = crossing_count(matching)
    if old_crossings == 0:
        return 1
    return sum(
        unit_drop_history_count(nxt)
        for nxt in successors(matching)
        if crossing_count(nxt) == old_crossings - 1
    )


def run():
    terminal_counts = []
    for chord_count in range(1, 8):
        initial = complete_crossing_matching(chord_count)
        law = time_law(chord_count)
        terminals = terminal_law(chord_count)
        check(sum(law.values(), Fraction(0)) == 1, (chord_count, law))
        check(sum(terminals.values(), Fraction(0)) == 1, (chord_count, terminals))
        check(crossing_count(initial) == chord_count * (chord_count - 1) // 2, initial)
        check(all(crossing_count(terminal) == 0 for terminal in terminals), terminals)

        minimum = chord_count // 2
        maximum = chord_count * (chord_count - 1) // 2
        check(tuple(law) == tuple(range(minimum, maximum + 1, 2)), (chord_count, law))
        check(law[maximum] == longest_atom_conjecture(chord_count), (chord_count, law[maximum]))

        # Along a longest history there are exactly c available crossing
        # occurrences when c crossings remain, so every such history has
        # weight 1/maximum!.  The resulting history count is the staircase
        # hook-length number f^(n-1,n-2,...,1).
        hook_product = longest_atom_conjecture(chord_count).denominator
        history_count = unit_drop_history_count(initial)
        check(history_count * hook_product == factorial(maximum), (chord_count, history_count))
        check(Fraction(history_count, factorial(maximum)) == law[maximum], chord_count)

        maximum_terminal_mass = sum(
            mass
            for (terminal, time), mass in joint_law(initial).items()
            if time == maximum and terminal == adjacent_matching(chord_count)
        )
        check(maximum_terminal_mass == law[maximum], (chord_count, maximum_terminal_mass))
        terminal_counts.append(len(terminals))

    check(terminal_counts == [1, 1, 3, 5, 18, 37, 143], terminal_counts)
    check(
        time_law(4)
        == {2: Fraction(8, 15), 4: Fraction(4, 9), 6: Fraction(1, 45)},
        time_law(4),
    )
    check(len(set(terminal_law(4).values())) > 1, "terminal law accidentally uniform")

    print("stoch_phase2b_chord_uncrossing: PASS")
    print(f"assertions={ASSERTIONS}")
    print(f"states={joint_law.cache_info().currsize}")
    print(f"unit_drop_states={unit_drop_history_count.cache_info().currsize}")
    print("support=floor(n/2),floor(n/2)+2,...,binom(n,2) checked_n<=7")
    print("longest_atom=1/product_{j=2}^{n-1}(2j-1)!! checked_n<=7")
    print("terminal_counts_n1_to_n7=1,1,3,5,18,37,143")
    print("killed_guess=uniform_terminal_measure")


if __name__ == "__main__":
    run()
