#!/usr/bin/env python3
"""Exact bounded spike for parity two-path toggling on ordered DAGs."""

from collections import Counter


def matrices(n):
    m = n * (n - 1) // 2
    for mask in range(1 << m):
        rows = [0] * n
        bit = 0
        for i in range(n):
            for j in range(i + 1, n):
                if (mask >> bit) & 1:
                    rows[i] |= 1 << j
                bit += 1
        yield tuple(rows)


def multiply(a, b):
    out = []
    for row in a:
        value = 0
        todo = row
        while todo:
            low = todo & -todo
            value ^= b[low.bit_length() - 1]
            todo -= low
        out.append(value)
    return tuple(out)


def add(a, b):
    return tuple(x ^ y for x, y in zip(a, b))


def power(a, exponent):
    n = len(a)
    result = tuple(1 << i for i in range(n))
    base = a
    while exponent:
        if exponent & 1:
            result = multiply(result, base)
        base = multiply(base, base)
        exponent >>= 1
    return result


def zero(n):
    return (0,) * n


def update(a):
    return add(a, multiply(a, a))


def iterate(a, time):
    for _ in range(time):
        a = update(a)
    return a


def iterate_formula(a, time):
    """Lucas/binomial form: sum_{j subset time} A^(2^j)."""
    out = zero(len(a))
    for j in range(time + 1):
        if j & ~time == 0:  # C(time,j) is odd exactly for submasks.
            out = add(out, power(a, 1 << j))
    return out


def predicted_period(a):
    s = 0
    while power(a, 1 << (1 << s)) != zero(len(a)):
        s += 1
    return 1 << s


def actual_period(a):
    start = a
    time = 0
    while True:
        time += 1
        a = update(a)
        if a == start:
            return time
        assert time <= 64


def main():
    assertions = 0
    summary = {}
    for n in range(1, 7):
        images = set()
        periods = Counter()
        for a in matrices(n):
            b = update(a)
            images.add(b)
            assertions += 1
            for time in range(9):
                assert iterate(a, time) == iterate_formula(a, time)
                assertions += 1
            period = actual_period(a)
            assert period == predicted_period(a)
            assertions += 1
            periods[period] += 1
        state_count = 1 << (n * (n - 1) // 2)
        assert len(images) == state_count
        assertions += 1
        max_period = 1
        s = 0
        while (1 << (1 << s)) < n:
            s += 1
            max_period = 1 << s
        assert max(periods) == max_period
        assertions += 1
        summary[n] = dict(sorted(periods.items()))
    print({"assertions": assertions, "period_counts": summary})


if __name__ == "__main__":
    main()
