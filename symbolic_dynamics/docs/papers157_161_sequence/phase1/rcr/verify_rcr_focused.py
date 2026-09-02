#!/usr/bin/env python3
"""Exact counterexample pressure for random anchored-rectangle contraction.

The all-parameter claims in the focused package are proved symbolically in the
companion Markdown files.  This standard-library program checks finite exact
consequences with ``fractions.Fraction``; it is not a proof or an owner search.
"""

from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from math import comb, factorial


class Audit:
    def __init__(self):
        self.assertions = 0
        self.lanes = []

    def equal(self, left, right, label=""):
        self.assertions += 1
        if left != right:
            raise AssertionError(f"{label}: {left!r} != {right!r}")

    def true(self, condition, label=""):
        self.assertions += 1
        if not condition:
            raise AssertionError(label or "assertion failed")

    def lane(self, name, start):
        count = self.assertions - start
        self.lanes.append((name, count))
        print(f"[{name}] PASS assertions={count}")


def harmonic(n, power=1):
    return sum((Fraction(1, k**power) for k in range(1, n + 1)), Fraction(0))


def alpha(m, r):
    """Coefficient in P(H_m>t)=sum_{r=2}^m alpha(m,r) r^{-t}."""
    if not (m >= 2 and 2 <= r <= m):
        return 0
    return (-1) ** (r - 2) * comb(m - 1, r - 1)


def transition_coefficient(m, k, r):
    """Coefficient of r^{-t} in P_m(X_t=k)."""
    if not (1 <= k <= r <= m):
        return 0
    return Fraction(
        (-1) ** (r - k) * factorial(m - 1),
        factorial(k - 1) * factorial(r - k) * factorial(m - r),
    )


@lru_cache(maxsize=None)
def one_law(m, t):
    if t == 0:
        return ((m, Fraction(1)),)
    previous = dict(one_law(m, t - 1))
    current = defaultdict(Fraction)
    for state, mass in previous.items():
        for target in range(1, state + 1):
            current[target] += mass / state
    return tuple(sorted(current.items()))


@lru_cache(maxsize=None)
def rectangle_law(a, b, t):
    if t == 0:
        return (((a, b), Fraction(1)),)
    previous = dict(rectangle_law(a, b, t - 1))
    current = defaultdict(Fraction)
    for (x, y), mass in previous.items():
        for i in range(1, x + 1):
            for j in range(1, y + 1):
                current[(i, j)] += mass / (x * y)
    return tuple(sorted(current.items()))


def transition_formula(m, k, t):
    if not 1 <= k <= m:
        return Fraction(0)
    return sum(
        (
            transition_coefficient(m, k, r) * Fraction(1, r**t)
            for r in range(k, m + 1)
        ),
        Fraction(0),
    )


def survival(m, t):
    if t < 0:
        return Fraction(1)
    if m == 1:
        return Fraction(0)
    return sum(
        (Fraction(alpha(m, r), r**t) for r in range(2, m + 1)),
        Fraction(0),
    )


def cdf(m, t):
    if t < 0:
        return Fraction(0)
    return 1 - survival(m, t)


def hitting_pmf_formula(m, t):
    if m == 1:
        return Fraction(int(t == 0))
    if t < 1:
        return Fraction(0)
    return (m - 1) * sum(
        (
            Fraction((-1) ** (r - 2) * comb(m - 2, r - 2), r**t)
            for r in range(2, m + 1)
        ),
        Fraction(0),
    )


def geometric_sum_pmf(m, t):
    """Mass at t for 1+sum_{r=2}^m Geom0((r-1)/r)."""
    if m == 1:
        return Fraction(int(t == 0))
    if t < 1:
        return Fraction(0)
    degree = t - 1
    polynomial = [Fraction(1)] + [Fraction(0)] * degree
    for r in range(2, m + 1):
        updated = [Fraction(0)] * (degree + 1)
        for old_degree, old_mass in enumerate(polynomial):
            for extra in range(degree - old_degree + 1):
                updated[old_degree + extra] += (
                    old_mass * Fraction(r - 1, r ** (extra + 1))
                )
        polynomial = updated
    return polynomial[degree]


def one_pgf_formula(m, z):
    if m == 1:
        return Fraction(1)
    denominator = Fraction(1)
    for r in range(2, m + 1):
        denominator *= r - z
    return z * factorial(m - 1) / denominator


def one_pgf_bellman(maximum, z):
    values = {1: Fraction(1)}
    for m in range(2, maximum + 1):
        values[m] = z * sum(values[j] for j in range(1, m)) / (m - z)
    return values[maximum]


def one_moments_bellman(maximum):
    means = {1: Fraction(0)}
    seconds = {1: Fraction(0)}
    for m in range(2, maximum + 1):
        lower_mean = sum((means[j] for j in range(1, m)), Fraction(0))
        means[m] = Fraction(m, m - 1) + lower_mean / (m - 1)
        lower_second = sum((seconds[j] for j in range(1, m)), Fraction(0))
        seconds[m] = (
            m + 2 * (lower_mean + means[m]) + lower_second
        ) / (m - 1)
    return means[maximum], seconds[maximum]


def one_mean_formula(m):
    return Fraction(0) if m == 1 else 1 + harmonic(m - 1)


def one_variance_formula(m):
    return Fraction(0) if m == 1 else harmonic(m - 1) + harmonic(m - 1, 2)


def rectangle_cdf(a, b, t):
    return cdf(a, t) * cdf(b, t)


def rectangle_tail_terms(a, b):
    """Return q -> coefficient for P(T_(a,b)>t)=sum coefficient*q^t."""
    terms = defaultdict(Fraction)
    for r in range(2, a + 1):
        terms[Fraction(1, r)] += alpha(a, r)
    for s in range(2, b + 1):
        terms[Fraction(1, s)] += alpha(b, s)
    for r in range(2, a + 1):
        for s in range(2, b + 1):
            terms[Fraction(1, r * s)] -= alpha(a, r) * alpha(b, s)
    return {q: coefficient for q, coefficient in terms.items() if coefficient}


def rectangle_pgf_formula(a, b, z):
    tail_series = sum(
        (coefficient / (1 - z * q) for q, coefficient in rectangle_tail_terms(a, b).items()),
        Fraction(0),
    )
    return 1 + (z - 1) * tail_series


def rectangle_pgf_bellman(a, b, z):
    values = {}
    for x in range(1, a + 1):
        for y in range(1, b + 1):
            if (x, y) == (1, 1):
                values[(x, y)] = Fraction(1)
                continue
            lower = sum(
                (
                    values[(i, j)]
                    for i in range(1, x + 1)
                    for j in range(1, y + 1)
                    if (i, j) != (x, y)
                ),
                Fraction(0),
            )
            values[(x, y)] = z * lower / (x * y - z)
    return values[(a, b)]


def rectangle_moments_formula(a, b):
    terms = rectangle_tail_terms(a, b)
    mean = sum(
        (coefficient / (1 - q) for q, coefficient in terms.items()),
        Fraction(0),
    )
    second = sum(
        (
            coefficient * (1 + q) / (1 - q) ** 2
            for q, coefficient in terms.items()
        ),
        Fraction(0),
    )
    return mean, second


def rectangle_moments_bellman(a, b):
    means = {}
    for x in range(1, a + 1):
        for y in range(1, b + 1):
            if (x, y) == (1, 1):
                means[(x, y)] = Fraction(0)
                continue
            lower = sum(
                (
                    means[(i, j)]
                    for i in range(1, x + 1)
                    for j in range(1, y + 1)
                    if (i, j) != (x, y)
                ),
                Fraction(0),
            )
            means[(x, y)] = (x * y + lower) / (x * y - 1)

    seconds = {}
    for x in range(1, a + 1):
        for y in range(1, b + 1):
            if (x, y) == (1, 1):
                seconds[(x, y)] = Fraction(0)
                continue
            all_next_means = sum(
                (
                    means[(i, j)]
                    for i in range(1, x + 1)
                    for j in range(1, y + 1)
                ),
                Fraction(0),
            )
            lower_seconds = sum(
                (
                    seconds[(i, j)]
                    for i in range(1, x + 1)
                    for j in range(1, y + 1)
                    if (i, j) != (x, y)
                ),
                Fraction(0),
            )
            seconds[(x, y)] = (
                x * y + 2 * all_next_means + lower_seconds
            ) / (x * y - 1)
    return means[(a, b)], seconds[(a, b)]


def discounted_potential_formula(a, b, i, j, z):
    if i > a or j > b:
        return Fraction(0)
    return sum(
        (
            transition_coefficient(a, i, r)
            * transition_coefficient(b, j, s)
            / (1 - Fraction(z, r * s))
            for r in range(i, a + 1)
            for s in range(j, b + 1)
        ),
        Fraction(0),
    )


def discounted_potential_bellman(a, b, i, j, z):
    values = {}
    for x in range(1, a + 1):
        for y in range(1, b + 1):
            if x < i or y < j:
                values[(x, y)] = Fraction(0)
                continue
            lower = sum(
                (
                    values[(u, v)]
                    for u in range(1, x + 1)
                    for v in range(1, y + 1)
                    if (u, v) != (x, y)
                ),
                Fraction(0),
            )
            source = x * y if (x, y) == (i, j) else 0
            values[(x, y)] = (source + z * lower) / (x * y - z)
    return values[(a, b)]


def first_hit_pgf_bellman(a, b, i, j, z):
    values = {}
    for x in range(1, a + 1):
        for y in range(1, b + 1):
            if x < i or y < j:
                values[(x, y)] = Fraction(0)
            elif (x, y) == (i, j):
                values[(x, y)] = Fraction(1)
            else:
                lower = sum(
                    (
                        values[(u, v)]
                        for u in range(1, x + 1)
                        for v in range(1, y + 1)
                        if (u, v) != (x, y)
                    ),
                    Fraction(0),
                )
                values[(x, y)] = z * lower / (x * y - z)
    return values[(a, b)]


def first_hit_pgf_formula(a, b, i, j, z):
    return (1 - Fraction(z, i * j)) * discounted_potential_formula(
        a, b, i, j, z
    )


def transient_green(a, b, i, j):
    if (i, j) == (1, 1):
        raise ValueError("the absorbing target has infinite ordinary potential")
    return discounted_potential_formula(a, b, i, j, Fraction(1))


def audit_one_dimensional(audit):
    start = audit.assertions
    for m in range(1, 19):
        for t in range(0, 11):
            law = dict(one_law(m, t))
            audit.equal(sum(law.values(), Fraction(0)), 1, f"one mass m={m},t={t}")
            for k in range(1, m + 1):
                audit.equal(
                    law.get(k, Fraction(0)),
                    transition_formula(m, k, t),
                    f"one transition m={m},k={k},t={t}",
                )
            audit.equal(law.get(1, Fraction(0)), cdf(m, t), f"one cdf m={m},t={t}")

    for m in range(1, 31):
        for z in (Fraction(-1, 2), Fraction(1, 3), Fraction(2, 3), Fraction(3, 2)):
            audit.equal(
                one_pgf_bellman(m, z), one_pgf_formula(m, z), f"one pgf m={m},z={z}"
            )

    for m in range(1, 19):
        for t in range(0, 13):
            literal = cdf(m, t) - cdf(m, t - 1)
            audit.equal(literal, hitting_pmf_formula(m, t), f"one pmf m={m},t={t}")
            audit.equal(literal, geometric_sum_pmf(m, t), f"geom sum m={m},t={t}")

    for m in range(1, 41):
        mean, second = one_moments_bellman(m)
        expected_mean = one_mean_formula(m)
        expected_variance = one_variance_formula(m)
        audit.equal(mean, expected_mean, f"one mean m={m}")
        audit.equal(second - mean * mean, expected_variance, f"one variance m={m}")
        if m >= 2:
            audit.equal(hitting_pmf_formula(m, 1), Fraction(1, m), f"one first atom m={m}")
            audit.equal(alpha(m, 2), m - 1, f"one leading tail m={m}")
            audit.true(
                all(Fraction(1, r) < Fraction(1, 2) for r in range(3, m + 1)),
                f"one tail separation m={m}",
            )
    audit.lane("A one-dimensional clock/transition law", start)


def audit_rectangle_clock(audit):
    start = audit.assertions
    for a in range(1, 11):
        for b in range(1, 11):
            for t in range(0, 8):
                literal = dict(rectangle_law(a, b, t))
                xlaw = dict(one_law(a, t))
                ylaw = dict(one_law(b, t))
                audit.equal(sum(literal.values(), Fraction(0)), 1, f"rect mass {a},{b},{t}")
                for i in range(1, a + 1):
                    for j in range(1, b + 1):
                        audit.equal(
                            literal.get((i, j), Fraction(0)),
                            xlaw.get(i, Fraction(0)) * ylaw.get(j, Fraction(0)),
                            f"rect product {a},{b}->{i},{j},t={t}",
                        )
                audit.equal(
                    literal.get((1, 1), Fraction(0)),
                    rectangle_cdf(a, b, t),
                    f"rect cdf {a},{b},t={t}",
                )

    for a in range(1, 11):
        for b in range(1, 11):
            for z in (Fraction(-1, 2), Fraction(1, 3), Fraction(2, 3), Fraction(3, 2)):
                audit.equal(
                    rectangle_pgf_bellman(a, b, z),
                    rectangle_pgf_formula(a, b, z),
                    f"rect pgf {a},{b},z={z}",
                )
            mean, second = rectangle_moments_bellman(a, b)
            formula_mean, formula_second = rectangle_moments_formula(a, b)
            audit.equal(mean, formula_mean, f"rect mean {a},{b}")
            audit.equal(second, formula_second, f"rect second {a},{b}")
            if (a, b) == (1, 1):
                audit.equal(mean, 0, "absorbing rectangle mean")
                audit.equal(rectangle_cdf(a, b, 0), 1, "absorbing rectangle time zero")
            else:
                first_atom = rectangle_cdf(a, b, 1) - rectangle_cdf(a, b, 0)
                audit.equal(first_atom, Fraction(1, a * b), f"rect first atom {a},{b}")
                terms = rectangle_tail_terms(a, b)
                audit.equal(
                    terms.get(Fraction(1, 2), Fraction(0)),
                    a + b - 2,
                    f"rect leading tail {a},{b}",
                )
                audit.true(
                    all(q < Fraction(1, 2) for q in terms if q != Fraction(1, 2)),
                    f"rect tail separation {a},{b}",
                )
            if a >= 2 and b >= 2:
                audit.true(mean > max(one_mean_formula(a), one_mean_formula(b)), "strict max")
                audit.true(mean < one_mean_formula(a) + one_mean_formula(b), "strict sum")
            else:
                audit.equal(mean, max(one_mean_formula(a), one_mean_formula(b)), "boundary max")
    audit.lane("B rectangle maximum clock", start)


def audit_every_target(audit):
    start = audit.assertions
    for a in range(1, 9):
        for b in range(1, 9):
            for i in range(1, a + 1):
                for j in range(1, b + 1):
                    if (i, j) == (1, 1):
                        audit.equal(
                            first_hit_pgf_bellman(a, b, i, j, Fraction(1)),
                            1,
                            f"absorbing hit {a},{b}",
                        )
                        continue
                    green = transient_green(a, b, i, j)
                    hit = first_hit_pgf_bellman(a, b, i, j, Fraction(1))
                    audit.equal(
                        hit,
                        Fraction(i * j - 1, i * j) * green,
                        f"hit/green {a},{b}->{i},{j}",
                    )
                    audit.true(Fraction(0) < hit <= 1, f"hit probability range {a},{b}->{i},{j}")
                    audit.true(green > 0, f"green positivity {a},{b}->{i},{j}")

    for a in range(1, 8):
        for b in range(1, 8):
            for i in range(1, a + 1):
                for j in range(1, b + 1):
                    for z in (Fraction(-1, 2), Fraction(1, 3), Fraction(2, 3)):
                        spectral = discounted_potential_formula(a, b, i, j, z)
                        bellman = discounted_potential_bellman(a, b, i, j, z)
                        audit.equal(spectral, bellman, f"potential {a},{b}->{i},{j},z={z}")
                        audit.equal(
                            first_hit_pgf_formula(a, b, i, j, z),
                            first_hit_pgf_bellman(a, b, i, j, z),
                            f"first hit {a},{b}->{i},{j},z={z}",
                        )

    for a in range(1, 9):
        for b in range(1, 9):
            for t in range(0, 9):
                literal = dict(rectangle_law(a, b, t))
                for i in range(1, a + 1):
                    for j in range(1, b + 1):
                        spectral = sum(
                            (
                                transition_coefficient(a, i, r)
                                * transition_coefficient(b, j, s)
                                * Fraction(1, (r * s) ** t)
                                for r in range(i, a + 1)
                                for s in range(j, b + 1)
                            ),
                            Fraction(0),
                        )
                        audit.equal(
                            literal.get((i, j), Fraction(0)),
                            spectral,
                            f"target atlas {a},{b}->{i},{j},t={t}",
                        )

    for a, b, i, j in ((2, 2, 3, 1), (2, 2, 1, 3), (3, 4, 4, 4)):
        audit.equal(discounted_potential_formula(a, b, i, j, Fraction(1, 3)), 0, "inaccessible")
    audit.lane("C every-target potential/hitting atlas", start)


def main():
    print("RCR FOCUSED EXACT FALSIFICATION")
    print("arithmetic=fractions.Fraction; randomness=none; dependencies=stdlib-only")
    audit = Audit()
    audit_one_dimensional(audit)
    audit_rectangle_clock(audit)
    audit_every_target(audit)

    absorbed = rectangle_cdf(4, 3, 4)
    rect_mean, rect_second = rectangle_moments_formula(4, 3)
    selected_green = {
        (1, 2): transient_green(4, 3, 1, 2),
        (2, 2): transient_green(4, 3, 2, 2),
        (3, 2): transient_green(4, 3, 3, 2),
        (4, 3): transient_green(4, 3, 4, 3),
    }
    print(
        "SIGNATURE H5 "
        f"pgf=z*24/((2-z)(3-z)(4-z)(5-z)); mean={one_mean_formula(5)}; "
        f"variance={one_variance_formula(5)}; F(4)={cdf(5, 4)}"
    )
    print(
        f"SIGNATURE R4x3 P(T<=4)={absorbed}; mean={rect_mean}; "
        f"second_moment={rect_second}"
    )
    print(
        "SIGNATURE GREEN R4x3 "
        + ",".join(f"{target}:{value}" for target, value in selected_green.items())
    )
    print(f"TOTAL PASS assertions={audit.assertions}")
    print("EVIDENCE_BOUNDARY finite exact checks are counterexample pressure, not proof or novelty")
    print("EXTERNAL_STATUS HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
