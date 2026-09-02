#!/usr/bin/env python3
"""Independent exhaustive checks for cyclic sliding-AND erosion.

The program starts from the literal map E(x)_i=x_i*x_{i+1}.  The formula
side never calls the literal iterator.  Only the Python standard library is
used, and iteration order is fixed so that stdout is reproducible.
"""

from collections import Counter, defaultdict
from itertools import product


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def step(x):
    n = len(x)
    return tuple(x[i] & x[(i + 1) % n] for i in range(n))


def literal_iterate(x, t):
    y = x
    for _ in range(t):
        y = step(y)
    return y


def window_iterate(x, t):
    n = len(x)
    return tuple(
        int(all(x[(i + j) % n] for j in range(t + 1))) for i in range(n)
    )


def fixed(x):
    return step(x) == x


def longest_cyclic_one_run(x):
    """Longest cyclic 1-run; all-one is returned as n."""
    n = len(x)
    if not any(x):
        return 0
    if all(x):
        return n
    cut = x.index(0)
    best = cur = 0
    for j in range(1, n + 1):
        bit = x[(cut + j) % n]
        cur = cur + 1 if bit else 0
        best = max(best, cur)
    return best


def literal_depth(x):
    if fixed(x):
        return 0
    y = x
    d = 0
    while not fixed(y):
        y = step(y)
        d += 1
        if d > len(x):
            raise AssertionError("literal orbit exceeded the claimed cap")
    return d


def add_to(counter, exponent, coefficient):
    if coefficient:
        counter[exponent] += coefficient


def poly_mul(p, q):
    out = Counter()
    for i, a in p.items():
        for j, b in q.items():
            add_to(out, i + j, a * b)
    return +out


def shift_poly(p, shift):
    return Counter({degree + shift: coefficient for degree, coefficient in p.items()})


def transfer_step(distribution, t):
    """Apply Q_t(z): zero has weight 1, one has weight z."""
    out = defaultdict(Counter)
    for state, polynomial in distribution.items():
        for degree, coefficient in polynomial.items():
            add_to(out[0], degree, coefficient)
            if state < t:
                add_to(out[state + 1], degree + 1, coefficient)
    return out


def trace_polynomial(n, t):
    """tr(Q_t(z)^n), the cyclic run-avoidance weight polynomial."""
    answer = Counter()
    for start in range(t + 1):
        distribution = {start: Counter({0: 1})}
        for _ in range(n):
            distribution = transfer_step(distribution, t)
        for degree, coefficient in distribution.get(start, {}).items():
            add_to(answer, degree, coefficient)
    return +answer


def gap_polynomial(m, t):
    """Length-m word, both endpoints zero, avoiding 1^(t+1)."""
    if m < 1:
        raise ValueError("gap remainder must be nonempty")
    distribution = {0: Counter({0: 1})}
    for _ in range(m - 1):
        distribution = transfer_step(distribution, t)
    return +distribution.get(0, Counter())


def run_gap_profile(y):
    """For a nonconstant target with a one, return cyclic (one-run, next gap)."""
    n = len(y)
    if not any(y) or all(y):
        raise ValueError("profile is only for nonconstant targets containing a one")
    starts = [i for i in range(n) if y[i] and not y[(i - 1) % n]]
    profile = []
    for start in starts:
        a = 0
        while y[(start + a) % n]:
            a += 1
        b = 0
        while not y[(start + a + b) % n]:
            b += 1
        profile.append((a, b))
    return profile


def predicted_fibre(y, t):
    """Weight polynomial sum_{E^t x=y} z^|x| from the proposed atlas."""
    n = len(y)
    if all(y):
        return Counter({n: 1})
    if not any(y):
        return trace_polynomial(n, t)
    profile = run_gap_profile(y)
    if any(b < t + 1 for _, b in profile):
        return Counter()
    forced = sum(a + t for a, _ in profile)
    answer = Counter({0: 1})
    for _, b in profile:
        answer = poly_mul(answer, gap_polynomial(b - t, t))
    return shift_poly(answer, forced)


def brute_gap_polynomial(m, t):
    answer = Counter()
    for word in product((0, 1), repeat=m):
        valid = word[0] == 0 and word[-1] == 0
        valid = valid and all(
            not all(word[i + j] for j in range(t + 1))
            for i in range(max(0, m - t))
        )
        if valid:
            answer[sum(word)] += 1
    return +answer


def fmt_counter(counter):
    return ",".join(f"{k}:{counter[k]}" for k in sorted(counter))


def main():
    known_depths = {
        2: {0: 2, 1: 2},
        3: {0: 2, 1: 3, 2: 3},
        4: {0: 2, 1: 6, 2: 4, 3: 4},
        5: {0: 2, 1: 10, 2: 10, 3: 5, 4: 5},
        6: {0: 2, 1: 17, 2: 21, 3: 12, 4: 6, 5: 6},
        7: {0: 2, 1: 28, 2: 42, 3: 28, 4: 14, 5: 7, 6: 7},
        8: {0: 2, 1: 46, 2: 84, 3: 60, 4: 32, 5: 16, 6: 8, 7: 8},
    }
    summaries = []

    # The automaton polynomials are also checked against literal gap words.
    for t in range(0, 7):
        for m in range(1, 11):
            check(
                gap_polynomial(m, t) == brute_gap_polynomial(m, t),
                f"gap polynomial failed at m={m}, t={t}",
            )

    for n in range(2, 14):
        words = list(product((0, 1), repeat=n))
        depths = Counter()
        for x in words:
            d = literal_depth(x)
            depths[d] += 1
            check(fixed(x) == (not any(x) or all(x)), f"fixed classification n={n}, x={x}")
            expected_depth = 0 if (not any(x) or all(x)) else longest_cyclic_one_run(x)
            check(d == expected_depth, f"depth/run mismatch n={n}, x={x}")
            if not all(x):
                check(literal_iterate(x, d) == (0,) * n, f"absorption mismatch n={n}, x={x}")
            for t in range(0, n + 2):
                check(
                    literal_iterate(x, t) == window_iterate(x, t),
                    f"window formula failed n={n}, t={t}, x={x}",
                )
                check(
                    all(a <= b for a, b in zip(literal_iterate(x, t + 1), literal_iterate(x, t))),
                    f"coordinate monotonicity failed n={n}, t={t}, x={x}",
                )

        check(sum(depths.values()) == 2**n, f"depth mass n={n}")
        check(depths[0] == 2, f"fixed count n={n}")
        check(max(depths) == n - 1, f"sharp height n={n}")
        check(literal_depth((0,) + (1,) * (n - 1)) == n - 1, f"sharp witness n={n}")
        if n in known_depths:
            check(dict(sorted(depths.items())) == known_depths[n], f"depth sentinel n={n}")

        for t in range(0, n + 2):
            actual = defaultdict(Counter)
            for x in words:
                y = literal_iterate(x, t)
                actual[y][sum(x)] += 1
            for y in words:
                expected = predicted_fibre(y, t)
                observed = +actual.get(y, Counter())
                check(observed == expected, f"weighted fibre n={n}, t={t}, y={y}")
            check(
                sum(sum(p.values()) for p in actual.values()) == 2**n,
                f"fibre mass n={n}, t={t}",
            )
            cdf = sum(count for d, count in depths.items() if d <= t)
            trace_cdf = 1 + sum(trace_polynomial(n, t).values())
            check(cdf == trace_cdf, f"depth CDF n={n}, t={t}")

        image_one = len({step(x) for x in words})
        summaries.append((n, image_one, depths))

    # Symbolic/large-n boundary checks not tied to the exhaustive cap.
    for n in range(2, 41):
        check(sum(trace_polynomial(n, 0).values()) == 1, f"t=0 trace n={n}")
        check(sum(trace_polynomial(n, n - 1).values()) == 2**n - 1, f"saturated trace n={n}")
        check(predicted_fibre((1,) * n, n + 3) == Counter({n: 1}), f"all-one fibre n={n}")
        check(
            sum(predicted_fibre((0,) * n, n + 3).values()) == 2**n - 1,
            f"all-zero saturated fibre n={n}",
        )

    example = (1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
    check(run_gap_profile(example) == [(2, 3), (1, 6)], "profile example")
    check(
        predicted_fibre(example, 2) == Counter({7: 1, 8: 2, 9: 1}),
        "factorized example polynomial",
    )

    print("CYCLIC SLIDING-AND EROSION -- INDEPENDENT EXACT SCOUT")
    print("literal map             E(x)_i = x_i*x_(i+1) on Z/nZ")
    print("orientation             Wolfram Rule 136; reflected Rule 192")
    print("exhaustive box          2 <= n <= 13, 0 <= t <= n+1, every source/target")
    print("weighted atlas          PASS (all coefficients, including unreachable targets)")
    print("window/depth/CDF        PASS")
    print("gap automata            PASS for 0<=t<=6, 1<=m<=10")
    for n, image_one, depths in summaries:
        print(f"n={n:2d} states={2**n:5d} image(E)={image_one:4d} depths={fmt_counter(depths)}")
    print("example n=12,t=2       z^7 + 2*z^8 + z^9 PASS")
    print(f"ASSERTIONS              {ASSERTIONS}")
    print("MATHEMATICAL STATUS     PASS")
    print("SELECTION DECISION      KILL")
    print("EXTERNAL STATUS         HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
