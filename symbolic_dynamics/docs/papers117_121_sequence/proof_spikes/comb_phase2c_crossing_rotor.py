#!/usr/bin/env python3
"""Exact pilot for crossing-count rotation of circular chord matchings.

For a perfect matching M of cyclically labelled vertices, rotate every
endpoint clockwise by cr(M) positions.  Crossing number is rotation
invariant, so each orbit is an explicitly powered cyclic action.  The script
exhausts all matchings through seven chords and attacks stabilizer-blind
period guesses.
"""

from collections import Counter, defaultdict
from functools import lru_cache
from math import gcd


ASSERTIONS = 0


def check(condition, message="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


@lru_cache(maxsize=None)
def matchings(vertices):
    if not vertices:
        return ((),)
    first = vertices[0]
    answer = []
    for index in range(1, len(vertices)):
        partner = vertices[index]
        remaining = vertices[1:index] + vertices[index + 1 :]
        pair = (min(first, partner), max(first, partner))
        for rest in matchings(remaining):
            answer.append(tuple(sorted((pair,) + rest)))
    return tuple(answer)


def rotate(matching, steps, modulus):
    pairs = []
    for left, right in matching:
        a = (left + steps) % modulus
        b = (right + steps) % modulus
        pairs.append((min(a, b), max(a, b)))
    return tuple(sorted(pairs))


def crosses(first, second):
    a, b = first
    c, d = second
    return (a < c < b < d) or (c < a < d < b)


def crossing_number(matching):
    return sum(
        crosses(matching[i], matching[j])
        for i in range(len(matching))
        for j in range(i + 1, len(matching))
    )


def update(matching, modulus):
    return rotate(matching, crossing_number(matching), modulus)


def rotation_orbit_size(matching, modulus):
    for steps in range(1, modulus + 1):
        if rotate(matching, steps, modulus) == matching:
            return steps
    raise AssertionError("rotation orbit did not close")


def iterate(matching, modulus, steps):
    for _ in range(steps):
        matching = update(matching, modulus)
    return matching


def main():
    max_chords = 7
    totals = []
    maximum_periods = []
    period_tables = []
    first_crossing_fixed = None
    periods_by_crossing = defaultdict(set)

    for chords in range(1, max_chords + 1):
        modulus = 2 * chords
        states = matchings(tuple(range(modulus)))
        images = set()
        periods = Counter()
        maximum = 1
        for matching in states:
            crossings = crossing_number(matching)
            image = update(matching, modulus)
            images.add(image)
            check(crossing_number(image) == crossings, "crossing count changed")
            rotation_size = rotation_orbit_size(matching, modulus)
            predicted = rotation_size // gcd(rotation_size, crossings)
            check(iterate(matching, modulus, predicted) == matching)
            for time in range(1, predicted):
                check(iterate(matching, modulus, time) != matching)
            periods[predicted] += 1
            maximum = max(maximum, predicted)
            periods_by_crossing[crossings].add(predicted)
            if crossings and predicted == 1 and first_crossing_fixed is None:
                first_crossing_fixed = (chords, matching, crossings)

        check(len(images) == len(states), "map is not bijective")
        check(sum(periods.values()) == len(states))
        totals.append(len(states))
        maximum_periods.append(maximum)
        period_tables.append(dict(sorted(periods.items())))

        if chords >= 3:
            witness = tuple(sorted(((0, 2), (1, 3)) + tuple(
                (vertex, vertex + 1) for vertex in range(4, modulus, 2)
            )))
            check(crossing_number(witness) == 1)
            check(rotation_orbit_size(witness, modulus) == modulus)
            check(iterate(witness, modulus, modulus) == witness)
            check(all(iterate(witness, modulus, time) != witness for time in range(1, modulus)))
            check(maximum == modulus)

    check(first_crossing_fixed is not None)  # crossing does not imply movement
    check(any(len(periods) > 1 for periods in periods_by_crossing.values()))

    print("comb_phase2c_crossing_rotor: PASS")
    print(f"assertions={ASSERTIONS}")
    print("exact_chords=1..7")
    print("state_counts=" + ",".join(map(str, totals)))
    print("max_periods=" + ",".join(map(str, maximum_periods)))
    print("period_tables=" + repr(period_tables))
    print(
        "first_crossing_fixed="
        + f"n{first_crossing_fixed[0]}_cr{first_crossing_fixed[2]}_"
        + repr(first_crossing_fixed[1])
    )
    print("falsified=crossing_implies_motion;crossing_count_alone_determines_period")
    print("theorem=period=rotational_orbit_size/gcd(orbit_size,crossings)")
    print("max_period=2n_for_n>=3")


if __name__ == "__main__":
    main()
