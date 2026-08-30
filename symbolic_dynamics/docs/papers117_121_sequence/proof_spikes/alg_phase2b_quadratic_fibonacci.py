#!/usr/bin/env python3
"""Exact pilot for a quadratic functional-controlled Fibonacci bijection."""

from collections import Counter
import json


class Checker:
    def __init__(self):
        self.assertions = 0

    def check(self, condition, message):
        self.assertions += 1
        if not condition:
            raise AssertionError(message)


def functional(vector):
    """The fixed nonzero linear functional: first coordinate over F_2."""
    return vector & 1


def update(state):
    x, y = state
    return y, x ^ (y if functional(y) else 0)


def inverse(state):
    u, v = state
    return v ^ (u if functional(u) else 0), u


def conjugacy(state):
    """Piecewise-linear gauge that exposes the generic linear wrapper."""
    x, y = state
    a, b = functional(x), functional(y)
    u, v = x & ~1, y & ~1
    if (a, b) == (1, 0):
        u, v = u, u ^ v
    elif (a, b) == (0, 1):
        u, v = u ^ v, v
    return u | a, v | b


def linear_model(state):
    """Direct product of a fibre swap and the order-three scalar Fibonacci map."""
    x, y = state
    a, b = functional(x), functional(y)
    u, v = x & ~1, y & ~1
    return v | b, u | (a ^ b)


def iterate(state, time):
    for _ in range(time):
        state = update(state)
    return state


def actual_period(state):
    current = state
    for period in range(1, 7):
        current = update(current)
        if current == state:
            return period
    raise AssertionError("period exceeded six")


def predicted_period(state):
    x, y = state
    a, b = functional(x), functional(y)
    u, v = x & ~1, y & ~1
    if (a, b) == (0, 0):
        return 1 if u == v else 2
    if (a, b) == (1, 0):
        return 3 if v == 0 else 6
    if (a, b) == (0, 1):
        return 3 if u == 0 else 6
    return 3 if u == v else 6


def verify_dimension(checker, dimension):
    size = 1 << dimension
    half = size // 2
    counts = Counter()
    images = set()
    for x in range(size):
        for y in range(size):
            state = (x, y)
            image = update(state)
            images.add(image)
            checker.check(inverse(image) == state, "left inverse failed")
            checker.check(update(inverse(state)) == state, "right inverse failed")
            checker.check(iterate(state, 6) == state, "sixth iterate failed")
            checker.check(
                conjugacy(update(state)) == linear_model(conjugacy(state)),
                "piecewise-linear conjugacy failed",
            )
            period = actual_period(state)
            checker.check(period == predicted_period(state), "period classification failed")
            counts[period] += 1

    expected = {
        1: half,
        2: half * (half - 1),
        3: 3 * half,
        6: 3 * half * (half - 1),
    }
    checker.check(dict(counts) == {key: value for key, value in expected.items() if value}, "point census failed")
    checker.check(len(images) == size * size, "map was not bijective")
    for period, count in counts.items():
        checker.check(count % period == 0, "point count did not split into cycles")

    return {
        "dimension": dimension,
        "states": size * size,
        "point_period_counts": dict(sorted(counts.items())),
        "cycle_counts": {period: count // period for period, count in sorted(counts.items())},
    }


def nonlinearity_lane(checker):
    # In dimension two, y -> ell(y)y sends 1,3,1+3=2 to 1,3,0.
    left = update((0, 1 ^ 3))
    first = update((0, 1))
    second = update((0, 3))
    componentwise_sum = (first[0] ^ second[0], first[1] ^ second[1])
    checker.check(left != componentwise_sum, "quadratic update accidentally became additive")
    return {
        "inputs": [[0, 1], [0, 3]],
        "update_of_sum": list(left),
        "sum_of_updates": list(componentwise_sum),
    }


def main():
    checker = Checker()
    summaries = [verify_dimension(checker, dimension) for dimension in range(1, 11)]
    result = {
        "assertions": checker.assertions,
        "dimensions": summaries,
        "nonlinearity_witness": nonlinearity_lane(checker),
    }
    result["assertions"] = checker.assertions
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
