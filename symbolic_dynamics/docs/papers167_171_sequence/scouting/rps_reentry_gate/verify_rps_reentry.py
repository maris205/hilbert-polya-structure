#!/usr/bin/env python3
"""Independent hostile verifier for the random-permutation fixed-point sieve.

This file imports no earlier scout or paper code.  It constructs uniform
permutations literally, builds the subset chain and its cycle-marked version,
and compares them with independently implemented closed forms.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import permutations
from math import comb, factorial


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def ok(self, condition: bool, label: str) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(label)

    def eq(self, left, right, label: str) -> None:
        self.assertions += 1
        if left != right:
            raise AssertionError(f"{label}: {left!r} != {right!r}")


class Fingerprint:
    def __init__(self) -> None:
        self._hash = sha256()
        self.rows = 0

    def add(self, *items) -> None:
        row = "|".join(str(item) for item in items) + "\n"
        self._hash.update(row.encode("ascii"))
        self.rows += 1

    @property
    def digest(self) -> str:
        return self._hash.hexdigest()


def submasks(mask: int):
    current = mask
    while True:
        yield current
        if current == 0:
            break
        current = (current - 1) & mask


def cycle_count(perm: tuple[int, ...]) -> int:
    seen = [False] * len(perm)
    answer = 0
    for start in range(len(perm)):
        if seen[start]:
            continue
        answer += 1
        point = start
        while not seen[point]:
            seen[point] = True
            point = perm[point]
    return answer


def literal_permutation_profile(n: int):
    by_fix = defaultdict(int)
    by_fix_and_cycles = defaultdict(lambda: defaultdict(int))
    for perm in permutations(range(n)):
        fixed = 0
        for point, image in enumerate(perm):
            if point == image:
                fixed |= 1 << point
        cycles = cycle_count(perm)
        by_fix[fixed] += 1
        by_fix_and_cycles[fixed][cycles] += 1
    return dict(by_fix), {
        fixed: dict(distribution)
        for fixed, distribution in by_fix_and_cycles.items()
    }


def trim(poly: list[int] | tuple[int, ...]) -> tuple[int, ...]:
    result = list(poly)
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    if not result:
        result = [0]
    return tuple(result)


def poly_add(left, right):
    result = [0] * max(len(left), len(right))
    for index, value in enumerate(left):
        result[index] += value
    for index, value in enumerate(right):
        result[index] += value
    return trim(result)


def poly_scale(poly, scalar: int):
    return trim([scalar * value for value in poly])


def poly_mul(left, right):
    if trim(left) == (0,) or trim(right) == (0,):
        return (0,)
    result = [0] * (len(left) + len(right) - 1)
    for i, first in enumerate(left):
        for j, second in enumerate(right):
            result[i + j] += first * second
    return trim(result)


def poly_power(poly, exponent: int):
    result = (1,)
    base = trim(poly)
    power = exponent
    while power:
        if power & 1:
            result = poly_mul(result, base)
        base = poly_mul(base, base)
        power //= 2
    return result


def poly_at_one(poly) -> int:
    return sum(poly)


def poly_derivative_at_one(poly) -> int:
    return sum(degree * coefficient for degree, coefficient in enumerate(poly))


def prescribed_cycle_polynomial(n: int, prescribed: int):
    # The prescribed labels give u^prescribed.  The remaining labels carry
    # the literal rising-factorial cycle polynomial.
    result = (0,) * prescribed + (1,)
    for offset in range(n - prescribed):
        result = poly_mul(result, (offset, 1))
    return result


def unmarked_history_formula(n: int, a: int, b: int, time: int) -> int:
    return sum(
        (-1) ** extra
        * comb(a - b, extra)
        * factorial(n - b - extra) ** time
        for extra in range(a - b + 1)
    )


def marked_history_formula(n: int, a: int, b: int, time: int):
    answer = (0,)
    for extra in range(a - b + 1):
        summand = poly_power(
            prescribed_cycle_polynomial(n, b + extra), time
        )
        answer = poly_add(
            answer,
            poly_scale(summand, (-1) ** extra * comb(a - b, extra)),
        )
    return answer


def harmonic(number: int) -> Fraction:
    return sum((Fraction(1, index) for index in range(1, number + 1)), Fraction(0))


def marked_first_moment_formula(
    n: int, a: int, b: int, time: int
) -> Fraction:
    total = Fraction(0)
    for extra in range(a - b + 1):
        prescribed = b + extra
        free = n - prescribed
        total += (
            (-1) ** extra
            * comb(a - b, extra)
            * factorial(free) ** time
            * time
            * (prescribed + harmonic(free))
        )
    return total


def literal_unmarked_kernel(n: int, profile):
    size = 1 << n
    kernel = []
    for source in range(size):
        row = defaultdict(int)
        for fixed, multiplicity in profile.items():
            row[source & fixed] += multiplicity
        kernel.append(dict(row))
    return kernel


def literal_marked_kernel(n: int, marked_profile):
    size = 1 << n
    kernel = []
    for source in range(size):
        row = defaultdict(lambda: [0] * (n + 1))
        for fixed, distribution in marked_profile.items():
            target = source & fixed
            for cycles, multiplicity in distribution.items():
                row[target][cycles] += multiplicity
        kernel.append({target: trim(poly) for target, poly in row.items()})
    return kernel


def advance_unmarked(histories, kernel):
    advanced = []
    for source_row in histories:
        row = defaultdict(int)
        for middle, old_count in source_row.items():
            for target, step_count in kernel[middle].items():
                row[target] += old_count * step_count
        advanced.append(dict(row))
    return advanced


def advance_marked(histories, kernel):
    advanced = []
    for source_row in histories:
        row = {}
        for middle, old_poly in source_row.items():
            for target, step_poly in kernel[middle].items():
                product = poly_mul(old_poly, step_poly)
                row[target] = poly_add(row.get(target, (0,)), product)
        advanced.append({target: trim(poly) for target, poly in row.items()})
    return advanced


def verify_literal_kernels(audit: Audit, fingerprint: Fingerprint):
    unmarked_boxes = 0
    marked_boxes = 0
    saved = {}
    for n in range(1, 8):
        profile, marked_profile = literal_permutation_profile(n)
        audit.eq(sum(profile.values()), factorial(n), f"profile mass n={n}")
        audit.eq(
            sum(sum(row.values()) for row in marked_profile.values()),
            factorial(n),
            f"marked profile mass n={n}",
        )
        for fixed, multiplicity in sorted(profile.items()):
            audit.eq(
                sum(marked_profile[fixed].values()),
                multiplicity,
                f"profile specialization n={n}, fixed={fixed}",
            )
            fingerprint.add("profile", n, fixed, multiplicity, sorted(marked_profile[fixed].items()))

        kernel = literal_unmarked_kernel(n, profile)
        size = 1 << n
        for source, row in enumerate(kernel):
            audit.eq(sum(row.values()), factorial(n), f"kernel mass n={n}, A={source}")
            for target in range(size):
                literal = row.get(target, 0)
                if target & ~source:
                    predicted = 0
                else:
                    predicted = unmarked_history_formula(
                        n, source.bit_count(), target.bit_count(), 1
                    )
                audit.eq(literal, predicted, f"one-step n={n}, A={source}, B={target}")

        histories = [{source: 1} for source in range(size)]
        for time in range(6):
            for source in range(size):
                for target in range(size):
                    literal = histories[source].get(target, 0)
                    if target & ~source:
                        predicted = 0
                    else:
                        predicted = unmarked_history_formula(
                            n, source.bit_count(), target.bit_count(), time
                        )
                    audit.eq(
                        literal,
                        predicted,
                        f"all-time n={n}, t={time}, A={source}, B={target}",
                    )
                    if time > 0:
                        obstruction = source == size - 1 and target.bit_count() == n - 1
                        supported = not (target & ~source) and not obstruction
                        audit.eq(
                            literal > 0,
                            supported,
                            f"support n={n}, t={time}, A={source}, B={target}",
                        )
                    fingerprint.add("unmarked", n, time, source, target, literal)
                    unmarked_boxes += 1
            if time < 5:
                histories = advance_unmarked(histories, kernel)
        saved[n] = (kernel, histories)

        if n <= 6:
            marked_kernel = literal_marked_kernel(n, marked_profile)
            marked_histories = [{source: (1,)} for source in range(size)]
            for time in range(4):
                for source in range(size):
                    for target in range(size):
                        literal = marked_histories[source].get(target, (0,))
                        if target & ~source:
                            predicted = (0,)
                        else:
                            predicted = marked_history_formula(
                                n, source.bit_count(), target.bit_count(), time
                            )
                        audit.eq(
                            literal,
                            predicted,
                            f"marked n={n}, t={time}, A={source}, B={target}",
                        )
                        audit.ok(
                            all(coefficient >= 0 for coefficient in literal),
                            f"marked positivity n={n}, t={time}, A={source}, B={target}",
                        )
                        if time > 0:
                            audit.eq(
                                poly_at_one(literal),
                                unmarked_history_formula(
                                    n,
                                    source.bit_count(),
                                    target.bit_count(),
                                    time,
                                )
                                if not (target & ~source)
                                else 0,
                                f"marked specialization n={n}, t={time}, A={source}, B={target}",
                            )
                        fingerprint.add("marked", n, time, source, target, literal)
                        marked_boxes += 1
                if time < 3:
                    marked_histories = advance_marked(marked_histories, marked_kernel)
    return unmarked_boxes, marked_boxes, saved


def verify_zeta_spectrum(audit: Audit, fingerprint: Fingerprint):
    spectral_boxes = 0
    for n in range(1, 8):
        profile, _ = literal_permutation_profile(n)
        kernel = literal_unmarked_kernel(n, profile)
        size = 1 << n
        for source in range(size):
            for support in range(size):
                left = sum(
                    multiplicity
                    for target, multiplicity in kernel[source].items()
                    if support & ~target == 0
                )
                right = (
                    factorial(n - support.bit_count())
                    if support & ~source == 0
                    else 0
                )
                audit.eq(left, right, f"zeta eigenvector n={n}, A={source}, S={support}")
                fingerprint.add("eigen", n, source, support, left)
                spectral_boxes += 1

        for lower in range(size):
            for upper in range(size):
                if lower & ~upper:
                    convolution = 0
                else:
                    convolution = sum(
                        (-1) ** (middle.bit_count() - lower.bit_count())
                        for middle in submasks(upper)
                        if lower & ~middle == 0
                    )
                audit.eq(
                    convolution,
                    int(lower == upper),
                    f"Boolean zeta/Mobius inverse n={n}, S={lower}, A={upper}",
                )
                spectral_boxes += 1

        values = [Fraction(factorial(n - rank), factorial(n)) for rank in range(n + 1)]
        if n >= 2:
            audit.eq(values[-2], values[-1], f"terminal eigenvalue collision n={n}")
            audit.eq(
                sum(comb(n, rank) for rank in (n - 1, n)),
                n + 1,
                f"terminal zeta-basis multiplicity n={n}",
            )
            audit.eq(len(set(values)), n, f"only one numerical collision n={n}")
        else:
            audit.eq(values, [Fraction(1), Fraction(1)], "n=1 spectrum boundary")
    return spectral_boxes


def cardinality_kernel(n: int):
    total = factorial(n)
    rows = []
    for a in range(n + 1):
        row = []
        for b in range(a + 1):
            row.append(comb(a, b) * unmarked_history_formula(n, a, b, 1))
        if sum(row) != total:
            raise AssertionError(f"cardinality row does not sum to n!: n={n}, a={a}")
        rows.append(row)
    return rows


def closed_mean(n: int, a: int) -> Fraction:
    total = factorial(n)
    return sum(
        (
            Fraction(
                (-1) ** (index + 1) * comb(a, index),
                1,
            )
            / (1 - Fraction(factorial(n - index), total))
        )
        for index in range(1, a + 1)
    )


def closed_second_moment(n: int, a: int) -> Fraction:
    total = factorial(n)
    answer = Fraction(0)
    for index in range(1, a + 1):
        eigenvalue = Fraction(factorial(n - index), total)
        answer += (
            (-1) ** (index + 1)
            * comb(a, index)
            * (1 + eigenvalue)
            / (1 - eigenvalue) ** 2
        )
    return answer


def closed_pgf(n: int, a: int, variable: Fraction) -> Fraction:
    total = factorial(n)
    partial = Fraction(0)
    for index in range(1, a + 1):
        eigenvalue = Fraction(factorial(n - index), total)
        partial += (
            (-1) ** (index + 1)
            * comb(a, index)
            / (1 - variable * eigenvalue)
        )
    return 1 - (1 - variable) * partial


def verify_absorption(audit: Audit, fingerprint: Fingerprint):
    absorption_boxes = 0
    # n=1 is a genuine nonabsorbing boundary from the unique nonempty state.
    profile, _ = literal_permutation_profile(1)
    kernel = literal_unmarked_kernel(1, profile)
    audit.eq(kernel[1], {1: 1}, "n=1 nonempty state is absorbing")

    for n in range(2, 9):
        total = factorial(n)
        counts = cardinality_kernel(n)
        means = [Fraction(0)] * (n + 1)
        seconds = [Fraction(0)] * (n + 1)
        for a in range(1, n + 1):
            probabilities = [Fraction(value, total) for value in counts[a]]
            self_loop = probabilities[a]
            lower_mean = sum(
                probabilities[b] * means[b] for b in range(a)
            )
            means[a] = (1 + lower_mean) / (1 - self_loop)
            continuation_mean = sum(
                probabilities[b] * means[b] for b in range(a + 1)
            )
            lower_second = sum(
                probabilities[b] * seconds[b] for b in range(a)
            )
            seconds[a] = (
                1 + 2 * continuation_mean + lower_second
            ) / (1 - self_loop)
            audit.eq(means[a], closed_mean(n, a), f"mean n={n}, a={a}")
            audit.eq(
                seconds[a],
                closed_second_moment(n, a),
                f"second moment n={n}, a={a}",
            )
            fingerprint.add("moments", n, a, means[a], seconds[a])
            absorption_boxes += 2

        for variable in (Fraction(0), Fraction(1, 3), Fraction(1, 2), Fraction(2, 3), Fraction(1)):
            pgf = [Fraction(1)] + [Fraction(0)] * n
            for a in range(1, n + 1):
                probabilities = [Fraction(value, total) for value in counts[a]]
                numerator = variable * sum(
                    probabilities[b] * pgf[b] for b in range(a)
                )
                pgf[a] = numerator / (1 - variable * probabilities[a])
                audit.eq(
                    pgf[a],
                    closed_pgf(n, a, variable),
                    f"PGF n={n}, a={a}, s={variable}",
                )
                fingerprint.add("pgf", n, a, variable, pgf[a])
                absorption_boxes += 1

        for a in range(1, n + 1):
            for time in range(7):
                eigenvalues = [
                    Fraction(factorial(n - index), total)
                    for index in range(a + 1)
                ]
                survival = sum(
                    (-1) ** (index + 1)
                    * comb(a, index)
                    * eigenvalues[index] ** time
                    for index in range(1, a + 1)
                )
                cdf = sum(
                    (-1) ** index
                    * comb(a, index)
                    * eigenvalues[index] ** time
                    for index in range(a + 1)
                )
                audit.eq(cdf + survival, 1, f"CDF/tail n={n}, a={a}, t={time}")
                if n == 2:
                    expected = Fraction(a - comb(a, 2), 2**time)
                    audit.eq(survival, expected, f"n=2 coalesced tail a={a}, t={time}")
                elif n == 3:
                    expected = Fraction(a, 3**time) - Fraction(
                        comb(a, 2) - comb(a, 3), 6**time
                    )
                    audit.eq(survival, expected, f"n=3 coalesced tail a={a}, t={time}")
                else:
                    first_two = Fraction(a, n**time) - Fraction(
                        comb(a, 2), (n * (n - 1)) ** time
                    )
                    remainder = sum(
                        (-1) ** (index + 1)
                        * comb(a, index)
                        * eigenvalues[index] ** time
                        for index in range(3, a + 1)
                    )
                    audit.eq(
                        survival - first_two,
                        remainder,
                        f"n>=4 separated tail n={n}, a={a}, t={time}",
                    )
                    audit.ok(
                        (a < 2 or eigenvalues[1] > eigenvalues[2])
                        and (a < 3 or eigenvalues[2] > eigenvalues[3]),
                        f"n>=4 scale separation n={n}, a={a}",
                    )
                fingerprint.add("tail", n, a, time, survival)
                absorption_boxes += 2
    return absorption_boxes


def verify_marked_extremes(audit: Audit, fingerprint: Fingerprint):
    marked_formula_boxes = 0
    for n in range(1, 19):
        for a in range(n + 1):
            for b in range(a + 1):
                difference = a - b
                obstruction = a == n and b == n - 1
                for time in range(1, 6):
                    poly = marked_history_formula(n, a, b, time)
                    nonzero_degrees = [
                        degree
                        for degree, coefficient in enumerate(poly)
                        if coefficient
                    ]
                    if obstruction:
                        audit.eq(poly, (0,), f"marked hole n={n}, a={a}, b={b}, t={time}")
                        marked_formula_boxes += 1
                        continue
                    audit.ok(nonzero_degrees, f"marked support n={n}, a={a}, b={b}, t={time}")
                    expected_low = time * (b + int(b < n))
                    expected_high = time * n - (difference + 1) // 2
                    audit.eq(
                        min(nonzero_degrees),
                        expected_low,
                        f"minimum cycles n={n}, a={a}, b={b}, t={time}",
                    )
                    audit.eq(
                        max(nonzero_degrees),
                        expected_high,
                        f"maximum cycles n={n}, a={a}, b={b}, t={time}",
                    )
                    audit.ok(
                        poly[expected_low] > 0 and poly[expected_high] > 0,
                        f"sharp cycle endpoints n={n}, a={a}, b={b}, t={time}",
                    )
                    history_count = unmarked_history_formula(n, a, b, time)
                    audit.eq(
                        poly_at_one(poly),
                        history_count,
                        f"closed marked specialization n={n}, a={a}, b={b}, t={time}",
                    )
                    derivative = poly_derivative_at_one(poly)
                    predicted_derivative = marked_first_moment_formula(
                        n, a, b, time
                    )
                    audit.eq(
                        Fraction(derivative),
                        predicted_derivative,
                        f"conditional cycle numerator n={n}, a={a}, b={b}, t={time}",
                    )
                    conditional_mean = Fraction(derivative, history_count)
                    audit.ok(
                        expected_low <= conditional_mean <= expected_high,
                        f"conditional cycle mean bounds n={n}, a={a}, b={b}, t={time}",
                    )
                    fingerprint.add(
                        "marked-extremes",
                        n,
                        a,
                        b,
                        time,
                        expected_low,
                        expected_high,
                        poly[expected_low],
                        poly[expected_high],
                        conditional_mean,
                    )
                    marked_formula_boxes += 8
    return marked_formula_boxes


def verify_parameter_probe(audit: Audit, fingerprint: Fingerprint):
    for n in range(1, 33):
        self_loop = Fraction(factorial(n - 1), factorial(n))
        audit.eq(self_loop, Fraction(1, n), f"singleton recovery n={n}")
        audit.eq(self_loop.denominator, n, f"singleton denominator n={n}")
        fingerprint.add("probe", n, self_loop)


def main() -> None:
    audit = Audit()
    fingerprint = Fingerprint()
    unmarked_boxes, marked_boxes, _ = verify_literal_kernels(audit, fingerprint)
    spectral_boxes = verify_zeta_spectrum(audit, fingerprint)
    absorption_boxes = verify_absorption(audit, fingerprint)
    marked_formula_boxes = verify_marked_extremes(audit, fingerprint)
    verify_parameter_probe(audit, fingerprint)

    print("RPS_REENTRY_HOSTILE_GATE_V1")
    print(f"literal_unmarked_boxes={unmarked_boxes}")
    print(f"literal_marked_boxes={marked_boxes}")
    print(f"spectral_boxes={spectral_boxes}")
    print(f"absorption_boxes={absorption_boxes}")
    print(f"marked_formula_boxes={marked_formula_boxes}")
    print(f"fingerprint_rows={fingerprint.rows}")
    print(f"payload_sha256={fingerprint.digest}")
    print(f"assertions={audit.assertions}")
    print("VERDICT GREEN_OWNER_THIN_WITH_N3_REPAIR")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
