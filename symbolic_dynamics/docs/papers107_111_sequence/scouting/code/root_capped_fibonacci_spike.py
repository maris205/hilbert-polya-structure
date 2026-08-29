#!/usr/bin/env python3
"""Exact spike for capped Fibonacci dynamics (x,y)->(y,min(a,x+y))."""


def fibs(n):
    f = [0, 1]
    while len(f) <= n:
        f.append(f[-1] + f[-2])
    return f


FIB = fibs(40)


def step(a, state):
    x, y = state
    return y, min(a, x + y)


def formula(a, state, t):
    x, y = state
    if t == 0:
        return state
    return (
        min(a, FIB[t - 1] * x + FIB[t] * y),
        min(a, FIB[t] * x + FIB[t + 1] * y),
    )


def depth(a, state):
    current = state
    for t in range(40):
        if step(a, current) == current:
            return t
        current = step(a, current)
    raise AssertionError((a, state))


def cdf_formula(a, t):
    if t == 0:
        return 2
    u, v = FIB[t - 1], FIB[t]
    return 1 + sum(
        u * x + v * y >= a
        for x in range(a + 1)
        for y in range(a + 1)
        if (x, y) != (0, 0)
    )


def run():
    assertions = 0
    for a in range(1, 251):
        hist = {}
        fixed = 0
        for x in range(a + 1):
            for y in range(a + 1):
                state = (x, y)
                fixed += step(a, state) == state
                tau = depth(a, state)
                hist[tau] = hist.get(tau, 0) + 1
                current = state
                for t in range(max(hist) + 3):
                    assert current == formula(a, state, t)
                    assertions += 1
                    current = step(a, current)
        assert fixed == 2
        assertions += 1
        for t in range(max(hist) + 1):
            observed = sum(count for tau, count in hist.items() if tau <= t)
            assert observed == cdf_formula(a, t)
            assertions += 1
        worst = next(t for t in range(1, 40) if FIB[t - 1] >= a)
        assert max(hist) == worst
        assertions += 1
    print("root capped-Fibonacci spike: PASS")
    print(f"exact assertions: {assertions}")
    print("checked every state for caps a=1..250")


if __name__ == "__main__":
    run()
