#!/usr/bin/env python3
"""Exact proof spike for the bounded Cartier-operator functional graph.

For q=p^a and f=sum_{j=0}^n c_j x^j, the update is

    C(f) = sum_j c_{pj}^{1/p} x^j.

Small finite fields are implemented literally.  The script compares direct
orbits with the coefficient-selection iterate, image/fibre ranks, the exact
core-entry CDF, and the Frobenius core-cycle census.
"""

from collections import Counter
from itertools import product
from math import gcd


class Audit:
    def __init__(self):
        self.assertions = 0

    def check(self, condition, message="assertion failed"):
        self.assertions += 1
        if not condition:
            raise AssertionError(message)


AUDIT = Audit()


class FiniteField:
    """Tiny polynomial-basis field used only for hostile finite controls."""

    def __init__(self, p, modulus):
        self.p = p
        self.modulus = tuple(modulus)  # monic, low coefficient first
        self.a = len(self.modulus) - 1
        self.q = p**self.a
        AUDIT.check(self.modulus[-1] == 1)

    def digits(self, value, length=None):
        if length is None:
            length = self.a
        out = []
        for _ in range(length):
            out.append(value % self.p)
            value //= self.p
        return out

    def encode(self, digits):
        value = 0
        place = 1
        for digit in digits:
            value += (digit % self.p) * place
            place *= self.p
        return value

    def mul(self, left, right):
        x = self.digits(left)
        y = self.digits(right)
        raw = [0] * (2 * self.a - 1)
        for i, xi in enumerate(x):
            for j, yj in enumerate(y):
                raw[i + j] = (raw[i + j] + xi * yj) % self.p
        for degree in range(len(raw) - 1, self.a - 1, -1):
            coefficient = raw[degree] % self.p
            if not coefficient:
                continue
            shift = degree - self.a
            for j in range(self.a + 1):
                raw[shift + j] = (
                    raw[shift + j] - coefficient * self.modulus[j]
                ) % self.p
        return self.encode(raw[: self.a])

    def power(self, value, exponent):
        result = 1
        base = value
        while exponent:
            if exponent & 1:
                result = self.mul(result, base)
            base = self.mul(base, base)
            exponent //= 2
        return result

    def frobenius_inverse(self, value, times=1):
        times %= self.a
        if not times:
            return value
        return self.power(value, self.p ** (self.a - times))

    def audit_field(self):
        for x in range(self.q):
            AUDIT.check(self.power(x, self.q) == x, "Frobenius failure")
            y = self.frobenius_inverse(x)
            AUDIT.check(self.power(y, self.p) == x, "inverse Frobenius failure")
        for x in range(1, self.q):
            AUDIT.check(self.power(x, self.q - 1) == 1, "not a field")


def cartier(vector, field):
    n = len(vector) - 1
    out = [0] * (n + 1)
    for j in range(n // field.p + 1):
        out[j] = field.frobenius_inverse(vector[field.p * j])
    return tuple(out)


def iterate(vector, field, times):
    for _ in range(times):
        vector = cartier(vector, field)
    return vector


def iterate_formula(vector, field, times):
    n = len(vector) - 1
    scale = field.p**times
    out = [0] * (n + 1)
    for j in range(n // scale + 1):
        out[j] = field.frobenius_inverse(vector[scale * j], times)
    return tuple(out)


def core_entry_time(vector, field):
    current = tuple(vector)
    time = 0
    while any(current[1:]):
        current = cartier(current, field)
        time += 1
        AUDIT.check(time <= len(vector), "core entry failed")
    return time


def predicted_entry_time(vector, p):
    occupied = [j for j, coefficient in enumerate(vector) if j and coefficient]
    if not occupied:
        return 0
    valuations = []
    for j in occupied:
        value = 0
        while j % p == 0:
            j //= p
            value += 1
        valuations.append(value)
    return 1 + max(valuations)


def mobius(n):
    prime_count = 0
    divisor = 2
    remaining = n
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            remaining //= divisor
            prime_count += 1
            if remaining % divisor == 0:
                return 0
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1
    if remaining > 1:
        prime_count += 1
    return -1 if prime_count % 2 else 1


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def exact_core_points(field, period):
    return sum(mobius(period // d) * field.p**d for d in divisors(period))


def run_lane(field, n):
    field.audit_field()
    phase = list(product(range(field.q), repeat=n + 1))
    depth_histogram = Counter()
    core_cycle_histogram = Counter()

    for vector in phase:
        for t in range(0, n + 2):
            AUDIT.check(
                iterate(vector, field, t) == iterate_formula(vector, field, t),
                f"iterate mismatch q={field.q}, n={n}, t={t}",
            )
        literal_depth = core_entry_time(vector, field)
        AUDIT.check(literal_depth == predicted_entry_time(vector, field.p))
        depth_histogram[literal_depth] += 1

    max_depth = 0
    scale = 1
    while scale <= n:
        max_depth += 1
        scale *= field.p
    AUDIT.check(max(depth_histogram) == max_depth if n else max(depth_histogram) == 0)

    for t in range(max_depth + 1):
        literal_cdf = sum(count for depth, count in depth_histogram.items() if depth <= t)
        selected_nonconstant = n // (field.p**t)
        formula_cdf = field.q ** (n + 1 - selected_nonconstant)
        AUDIT.check(
            literal_cdf == formula_cdf,
            f"depth CDF mismatch q={field.q}, n={n}, t={t}",
        )

        fibres = Counter(iterate(vector, field, t) for vector in phase)
        image_dimension = n // (field.p**t) + 1
        AUDIT.check(len(fibres) == field.q**image_dimension)
        expected_fibre = field.q ** (n + 1 - image_dimension)
        for size in fibres.values():
            AUDIT.check(size == expected_fibre, "nonuniform iterate fibre")

    constants = list(range(field.q))
    unseen = set(constants)
    while unseen:
        start = min(unseen)
        orbit = []
        current = start
        while current not in orbit:
            orbit.append(current)
            current = field.frobenius_inverse(current)
        AUDIT.check(current == start)
        for value in orbit:
            unseen.remove(value)
        core_cycle_histogram[len(orbit)] += 1

    for d in divisors(field.a):
        formula_cycles = exact_core_points(field, d) // d
        AUDIT.check(core_cycle_histogram[d] == formula_cycles)
    AUDIT.check(
        sum(period * count for period, count in core_cycle_histogram.items())
        == field.q
    )

    for m in range(1, 2 * field.a + 1):
        fixed = sum(
            1 for vector in phase if iterate(vector, field, m) == vector
        )
        AUDIT.check(fixed == field.p ** gcd(field.a, m))

    print(
        f"q={field.q}=({field.p}^{field.a}), n={n}: phase={len(phase)}, "
        f"depths={dict(sorted(depth_histogram.items()))}, "
        f"core cycles={dict(sorted(core_cycle_histogram.items()))}"
    )


def main():
    lanes = [
        (FiniteField(2, (0, 1)), 7),
        (FiniteField(3, (0, 1)), 5),
        (FiniteField(2, (1, 1, 1)), 5),
        (FiniteField(2, (1, 1, 0, 1)), 4),
        (FiniteField(3, (1, 0, 1)), 3),
        (FiniteField(2, (1, 1, 0, 0, 1)), 2),
    ]
    for field, n in lanes:
        run_lane(field, n)
    print(f"PASS: {AUDIT.assertions:,} exact assertions")


if __name__ == "__main__":
    main()
