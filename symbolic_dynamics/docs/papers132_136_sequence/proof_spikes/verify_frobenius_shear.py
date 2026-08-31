#!/usr/bin/env python3
"""Exact small-scope checks for T(f)=f+f^p on x F_p[x]/(x^N).

The finite run checks the closed fixed-point formula, exact p-power period
census, bijectivity, and the predicted order.  It is evidence, not proof.
"""

from collections import Counter


def digits(state, p, length):
    out = []
    for _ in range(length):
        out.append(state % p)
        state //= p
    return out


def encode(coeffs, p):
    out = 0
    place = 1
    for coeff in coeffs:
        out += coeff * place
        place *= p
    return out


def step(state, p, n):
    # coeffs[j-1] is the coefficient of x^j, 1 <= j < n.
    old = digits(state, p, n - 1)
    new = old[:]
    for j, coeff in enumerate(old, start=1):
        if j * p < n:
            new[j * p - 1] = (new[j * p - 1] + coeff) % p
    return encode(new, p)


def vp(t, p):
    r = 0
    while t % p == 0:
        t //= p
        r += 1
    return r


def predicted_fixed(p, n, t):
    s = p ** vp(t, p)
    multiplier = p ** s
    free_coeffs = (n - 1) - (n - 1) // multiplier
    return p ** free_coeffs


def predicted_order(p, n):
    order = 1
    frobenius_iterations = 1
    while p ** frobenius_iterations < n:
        order *= p
        frobenius_iterations *= p
    return order


def audit(p, n):
    size = p ** (n - 1)
    image = [step(state, p, n) for state in range(size)]
    assert len(set(image)) == size
    assertions = size + 1

    order = predicted_order(p, n)
    fixed = {}
    for t in range(1, 2 * order + 1):
        count = 0
        for state in range(size):
            value = state
            for _ in range(t):
                value = image[value]
            count += value == state
            assertions += 1
        fixed[t] = count
        assert count == predicted_fixed(p, n, t)
        assertions += 1

    period_points = Counter()
    for state in range(size):
        value = image[state]
        period = 1
        while value != state:
            value = image[value]
            period += 1
            assert period <= order
            assertions += 1
        assert order % period == 0
        probe = period
        while probe > 1:
            assert probe % p == 0
            probe //= p
            assertions += 1
        period_points[period] += 1
    assertions += size

    formula_points = {}
    previous = 0
    power = 1
    while power <= order:
        current = predicted_fixed(p, n, power)
        formula_points[power] = current - previous
        previous = current
        power *= p
    assert dict(sorted(period_points.items())) == formula_points
    assert sum(period_points.values()) == size
    assertions += 2

    cycles = {period: count // period for period, count in period_points.items()}
    assert all(period * cycles[period] == count for period, count in period_points.items())
    assertions += len(cycles)
    return order, dict(sorted(period_points.items())), cycles, assertions


def main():
    scopes = ((2, 12), (3, 8), (5, 6))
    total_assertions = 0
    audits = 0
    for p, max_n in scopes:
        for n in range(2, max_n + 1):
            order, points, cycles, assertions = audit(p, n)
            total_assertions += assertions
            audits += 1
            print(
                f"p={p} N={n} states={p ** (n - 1)} order={order} "
                f"period_points={points} cycles={cycles} assertions={assertions}"
            )
    print(f"AUDITS={audits}")
    print(f"TOTAL_ASSERTIONS={total_assertions}")
    print("scope_sentinel=finite checks are evidence, not proof")
    print("release_sentinel=HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
