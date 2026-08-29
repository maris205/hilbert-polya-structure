#!/usr/bin/env python3
"""Exact controls for (x,y) -> (y,min(a,x+y)) on a capped square."""

from collections import Counter, defaultdict


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


FIB = [0, 1]
while len(FIB) < 64:
    FIB.append(FIB[-1] + FIB[-2])


def ceil_div(x, y):
    return -((-x) // y)


def step(a, state):
    x, y = state
    return y, min(a, x + y)


def iterate_formula(a, state, t):
    if t == 0:
        return state
    x, y = state
    return (
        min(a, FIB[t - 1] * x + FIB[t] * y),
        min(a, FIB[t] * x + FIB[t + 1] * y),
    )


def depth_formula(a, state):
    if state in ((0, 0), (a, a)):
        return 0
    x, y = state
    for t in range(1, 63):
        if FIB[t - 1] * x + FIB[t] * y >= a:
            return t
    raise AssertionError((a, state))


def cdf_formula(a, t):
    if t == 0:
        return 2
    u, v = FIB[t - 1], FIB[t]
    total = 1
    for x in range(a + 1):
        lower = max(0, ceil_div(a - u * x, v))
        total += a + 1 - lower
    return total


def fibre_formula(a, output):
    u, v = output
    if v < u:
        return 0
    if v < a:
        return 1
    return u + 1


def run():
    states_checked = 0
    trajectory_checks = 0
    fibre_checks = 0
    for a in range(1, 221):
        depths = Counter()
        fibres = defaultdict(int)
        max_depth = 1 + next(k for k, value in enumerate(FIB) if value >= a)
        for x in range(a + 1):
            for y in range(a + 1):
                state = (x, y)
                states_checked += 1
                current = state
                observed_depth = None
                for t in range(max_depth + 3):
                    check(current == iterate_formula(a, state, t),
                          ("iterate", a, state, t))
                    trajectory_checks += 1
                    if observed_depth is None and current in ((0, 0), (a, a)):
                        observed_depth = t
                    current = step(a, current)
                predicted_depth = depth_formula(a, state)
                check(observed_depth == predicted_depth,
                      ("depth", a, state, observed_depth, predicted_depth))
                depths[predicted_depth] += 1
                fibres[step(a, state)] += 1
        check(max(depths) == max_depth, ("max-depth", a))
        check(depths[0] == 2, ("recurrent", a))
        for t in range(max_depth + 2):
            observed = sum(v for d, v in depths.items() if d <= t)
            check(observed == cdf_formula(a, t), ("cdf", a, t))
        image_size = 0
        garden = 0
        fibre_sum = 0
        for u in range(a + 1):
            for v in range(a + 1):
                predicted = fibre_formula(a, (u, v))
                observed = fibres[(u, v)]
                check(observed == predicted, ("fibre", a, u, v))
                fibre_checks += 1
                image_size += observed > 0
                garden += observed == 0
                fibre_sum += observed
        check(image_size == (a + 1) * (a + 2) // 2, ("image-size", a))
        check(garden == a * (a + 1) // 2, ("garden", a))
        check(fibre_sum == (a + 1) ** 2, ("fibre-sum", a))
    print("capped Fibonacci dynamics exact control: PASS")
    print(f"assertions={ASSERTIONS}")
    print(f"states_checked={states_checked}")
    print(f"trajectory_formula_checks={trajectory_checks}")
    print(f"fibre_formula_checks={fibre_checks}")
    print("caps=a=1..220")


if __name__ == "__main__":
    run()
