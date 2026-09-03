#!/usr/bin/env python3
"""Author-side exact verifier for P170.

The implementation is deliberately standalone.  It imports no scouting,
gate, manuscript, or earlier-paper code.  Uniform permutations are generated
literally, subset histories are multiplied directly, and the displayed
closed forms are implemented separately.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import permutations
from math import ceil, comb, factorial


class Ledger:
    def __init__(self) -> None:
        self.assertions = 0
        self.section_counts: Counter[str] = Counter()
        self.digest = sha256()
        self.rows = 0

    def equal(self, section: str, got, expected, label: str) -> None:
        self.assertions += 1
        self.section_counts[section] += 1
        if got != expected:
            raise AssertionError(f"{label}: got {got!r}, expected {expected!r}")

    def true(self, section: str, condition: bool, label: str) -> None:
        self.equal(section, bool(condition), True, label)

    def record(self, *items) -> None:
        row = "|".join(str(item) for item in items) + "\n"
        self.digest.update(row.encode("ascii"))
        self.rows += 1


def subsets(mask: int):
    current = mask
    while True:
        yield current
        if current == 0:
            return
        current = (current - 1) & mask


def number_of_cycles(perm: tuple[int, ...]) -> int:
    visited = [False] * len(perm)
    answer = 0
    for start in range(len(perm)):
        if visited[start]:
            continue
        answer += 1
        point = start
        while not visited[point]:
            visited[point] = True
            point = perm[point]
    return answer


def literal_atoms(n: int):
    atoms: Counter[tuple[int, int]] = Counter()
    for perm in permutations(range(n)):
        fixed = sum(1 << i for i, image in enumerate(perm) if image == i)
        atoms[(fixed, number_of_cycles(perm))] += 1
    return atoms


def add_poly(left: tuple[int, ...], right: tuple[int, ...]):
    out = [0] * max(len(left), len(right))
    for i, value in enumerate(left):
        out[i] += value
    for i, value in enumerate(right):
        out[i] += value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def scale_poly(poly: tuple[int, ...], scalar: int):
    return tuple(value * scalar for value in poly)


def multiply_poly(left: tuple[int, ...], right: tuple[int, ...]):
    if not any(left) or not any(right):
        return (0,)
    out = [0] * (len(left) + len(right) - 1)
    for i, first in enumerate(left):
        for j, second in enumerate(right):
            out[i + j] += first * second
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def power_poly(poly: tuple[int, ...], exponent: int):
    answer = (1,)
    base = poly
    while exponent:
        if exponent & 1:
            answer = multiply_poly(answer, base)
        base = multiply_poly(base, base)
        exponent //= 2
    return answer


@lru_cache(maxsize=None)
def prescribed_cycle_poly(n: int, fixed_labels: int):
    # u^s times the rising factorial u(u+1)...(u+n-s-1).
    answer = (0,) * fixed_labels + (1,)
    for q in range(n - fixed_labels):
        answer = multiply_poly(answer, (q, 1))
    return answer


def closed_count(n: int, a: int, b: int, time: int) -> int:
    return sum(
        (-1) ** j * comb(a - b, j) * factorial(n - b - j) ** time
        for j in range(a - b + 1)
    )


@lru_cache(maxsize=None)
def closed_marked(n: int, a: int, b: int, time: int):
    answer = (0,)
    for j in range(a - b + 1):
        term = power_poly(prescribed_cycle_poly(n, b + j), time)
        answer = add_poly(answer, scale_poly(term, (-1) ** j * comb(a - b, j)))
    return answer


def harmonic(m: int) -> Fraction:
    return sum((Fraction(1, q) for q in range(1, m + 1)), Fraction(0))


def closed_marked_derivative(n: int, a: int, b: int, time: int):
    return sum(
        Fraction(
            (-1) ** j
            * comb(a - b, j)
            * factorial(n - b - j) ** time
            * time,
            1,
        )
        * (b + j + harmonic(n - b - j))
        for j in range(a - b + 1)
    )


def poly_derivative_at_one(poly: tuple[int, ...]) -> int:
    return sum(degree * coefficient for degree, coefficient in enumerate(poly))


def polynomial_support(poly: tuple[int, ...]):
    return [degree for degree, coefficient in enumerate(poly) if coefficient]


def advance_unmarked(rows, fixed_profile):
    answer = []
    for row in rows:
        next_row: defaultdict[int, int] = defaultdict(int)
        for middle, old_count in row.items():
            for fixed, multiplicity in fixed_profile.items():
                next_row[middle & fixed] += old_count * multiplicity
        answer.append(dict(next_row))
    return answer


def advance_marked(rows, atoms):
    answer = []
    for row in rows:
        next_row: dict[int, tuple[int, ...]] = {}
        for middle, old_poly in row.items():
            for (fixed, cycles), multiplicity in atoms.items():
                step = (0,) * cycles + (multiplicity,)
                target = middle & fixed
                product = multiply_poly(old_poly, step)
                next_row[target] = add_poly(next_row.get(target, (0,)), product)
        answer.append(next_row)
    return answer


def supported(n: int, a: int, b: int) -> bool:
    return not (a == n and b == n - 1)


def verify_literal_histories(ledger: Ledger) -> None:
    for n in range(1, 8):
        atoms = literal_atoms(n)
        fixed_profile: Counter[int] = Counter()
        for (fixed, _cycles), multiplicity in atoms.items():
            fixed_profile[fixed] += multiplicity
        ledger.equal("literal", sum(atoms.values()), factorial(n), f"atom mass n={n}")
        ledger.record("atoms", n, sorted(atoms.items()))

        size = 1 << n
        histories = [{source: 1} for source in range(size)]
        for time in range(0, 6):
            for source in range(size):
                a = source.bit_count()
                for target in range(size):
                    literal = histories[source].get(target, 0)
                    if target & ~source:
                        expected = 0
                    else:
                        expected = closed_count(n, a, target.bit_count(), time)
                    ledger.equal(
                        "literal",
                        literal,
                        expected,
                        f"unmarked n={n},t={time},A={source},B={target}",
                    )
                    if time >= 1 and not (target & ~source):
                        expected_positive = supported(n, a, target.bit_count())
                        ledger.equal(
                            "support",
                            literal > 0,
                            expected_positive,
                            f"support n={n},t={time},A={source},B={target}",
                        )
            if time < 5:
                histories = advance_unmarked(histories, fixed_profile)


def verify_marked_histories(ledger: Ledger) -> None:
    for n in range(1, 7):
        atoms = literal_atoms(n)
        size = 1 << n
        histories = [{source: (1,)} for source in range(size)]
        for time in range(0, 4):
            for source in range(size):
                a = source.bit_count()
                for target in range(size):
                    literal = histories[source].get(target, (0,))
                    if target & ~source:
                        expected = (0,)
                    else:
                        expected = closed_marked(n, a, target.bit_count(), time)
                    ledger.equal(
                        "marked",
                        literal,
                        expected,
                        f"marked n={n},t={time},A={source},B={target}",
                    )
                    ledger.true(
                        "marked",
                        all(coefficient >= 0 for coefficient in literal),
                        f"nonnegative n={n},t={time},A={source},B={target}",
                    )
                    if time >= 1 and expected != (0,):
                        b = target.bit_count()
                        degrees = polynomial_support(expected)
                        ledger.equal(
                            "extrema",
                            min(degrees),
                            time * (b + (b < n)),
                            f"minimum n={n},t={time},a={a},b={b}",
                        )
                        ledger.equal(
                            "extrema",
                            max(degrees),
                            time * n - ceil((a - b) / 2),
                            f"maximum n={n},t={time},a={a},b={b}",
                        )
                        count = sum(expected)
                        derivative = poly_derivative_at_one(expected)
                        ledger.equal(
                            "expectation",
                            Fraction(derivative, count),
                            closed_marked_derivative(n, a, b, time) / count,
                            f"conditional mean n={n},t={time},a={a},b={b}",
                        )
                        ledger.true(
                            "expectation",
                            Fraction(min(degrees), 1)
                            <= Fraction(derivative, count)
                            <= Fraction(max(degrees), 1),
                            f"mean in range n={n},t={time},a={a},b={b}",
                        )
            if time < 3:
                histories = advance_marked(histories, atoms)
        ledger.record("marked", n, sum(len(row) for row in histories))


def make_cycle_permutation(n: int, cycles: list[list[int]]):
    perm = list(range(n))
    for cycle in cycles:
        if len(cycle) <= 1:
            continue
        for left, right in zip(cycle, cycle[1:] + cycle[:1]):
            perm[left] = right
    return tuple(perm)


def endpoint_after(source: int, history: list[tuple[int, ...]]) -> int:
    state = source
    for perm in history:
        fixed = sum(1 << i for i, image in enumerate(perm) if image == i)
        state &= fixed
    return state


def verify_uniform_marked_contract(ledger: Ledger) -> None:
    # Size-form formulas far beyond the literal permutation boxes.
    for n in range(1, 19):
        for a in range(n + 1):
            for b in range(a + 1):
                for time in range(1, 6):
                    poly = closed_marked(n, a, b, time)
                    positive = any(poly)
                    ledger.equal(
                        "uniform",
                        positive,
                        supported(n, a, b),
                        f"formula support n={n},a={a},b={b},t={time}",
                    )
                    if not positive:
                        continue
                    ledger.true(
                        "uniform",
                        all(value >= 0 for value in poly),
                        f"formula nonnegative n={n},a={a},b={b},t={time}",
                    )
                    degrees = polynomial_support(poly)
                    lower = time * (b + (b < n))
                    upper = time * n - ceil((a - b) / 2)
                    ledger.equal("uniform", min(degrees), lower, "uniform minimum")
                    ledger.equal("uniform", max(degrees), upper, "uniform maximum")
                    ledger.equal(
                        "uniform",
                        sum(poly),
                        closed_count(n, a, b, time),
                        "u=1 specialization",
                    )
                    ledger.equal(
                        "uniform",
                        Fraction(poly_derivative_at_one(poly), 1),
                        closed_marked_derivative(n, a, b, time),
                        "uniform derivative",
                    )
                ledger.record("size", n, a, b, closed_count(n, a, b, 3))

    # Construct the lower- and upper-degree histories for every supported
    # size triple; this separately checks all parity and d=1 boundary cases.
    for n in range(1, 65):
        identity = tuple(range(n))
        for a in range(n + 1):
            source = (1 << a) - 1
            for b in range(a + 1):
                if not supported(n, a, b):
                    continue
                target = (1 << b) - 1
                complement = list(range(b, n))
                low_perm = make_cycle_permutation(n, [complement])
                low_history = [low_perm] * 4
                ledger.equal("witness", endpoint_after(source, low_history), target, "low endpoint")
                ledger.equal(
                    "witness",
                    sum(number_of_cycles(perm) for perm in low_history),
                    4 * (b + (b < n)),
                    "low degree",
                )

                lost = list(range(b, a))
                cycles: list[list[int]] = []
                if len(lost) == 1:
                    ledger.true("witness", a < n, "d=1 requires outside label")
                    cycles = [[lost[0], a]]
                elif len(lost) % 2 == 1:
                    cycles = [lost[:3]]
                    cycles.extend([lost[q : q + 2] for q in range(3, len(lost), 2)])
                else:
                    cycles = [lost[q : q + 2] for q in range(0, len(lost), 2)]
                high_perm = make_cycle_permutation(n, cycles)
                high_history = [high_perm, identity, identity, identity]
                ledger.equal("witness", endpoint_after(source, high_history), target, "high endpoint")
                ledger.equal(
                    "witness",
                    sum(number_of_cycles(perm) for perm in high_history),
                    4 * n - ceil((a - b) / 2),
                    "high degree",
                )


def verify_spectrum(ledger: Ledger) -> None:
    for n in range(1, 8):
        atoms = literal_atoms(n)
        fixed_profile: Counter[int] = Counter()
        for (fixed, _), multiplicity in atoms.items():
            fixed_profile[fixed] += multiplicity
        size = 1 << n
        for source in range(size):
            for basis_set in range(size):
                action = sum(
                    multiplicity
                    for fixed, multiplicity in fixed_profile.items()
                    if not (basis_set & ~(source & fixed))
                )
                expected = (
                    factorial(n - basis_set.bit_count())
                    if not (basis_set & ~source)
                    else 0
                )
                ledger.equal("spectrum", action, expected, "zeta eigenvector")
        for lower in range(size):
            for upper in range(size):
                if lower & ~upper:
                    inverse_entry = 0
                else:
                    inverse_entry = sum(
                        (-1) ** (middle.bit_count() - lower.bit_count())
                        for middle in subsets(upper)
                        if not (lower & ~middle)
                    )
                ledger.equal(
                    "spectrum",
                    inverse_entry,
                    int(lower == upper),
                    "Boolean zeta/Mobius inverse",
                )
        lambdas = [Fraction(factorial(n - r), factorial(n)) for r in range(n + 1)]
        repetitions = [
            (r, s) for r in range(n + 1) for s in range(r + 1, n + 1) if lambdas[r] == lambdas[s]
        ]
        ledger.equal("spectrum", repetitions, [(n - 1, n)], f"terminal collision n={n}")
        ledger.record("spectrum", n, lambdas)


def spectral_survival(n: int, a: int, time: int) -> Fraction:
    return sum(
        Fraction((-1) ** (j + 1) * comb(a, j), 1)
        * Fraction(factorial(n - j), factorial(n)) ** time
        for j in range(1, a + 1)
    )


def verify_absorption(ledger: Ledger) -> None:
    for n in range(2, 13):
        total = factorial(n)
        mean = [Fraction(0)] * (n + 1)
        second = [Fraction(0)] * (n + 1)
        pgf_values = [Fraction(-1, 3), Fraction(0), Fraction(1, 4), Fraction(2, 3), Fraction(1)]
        pgf = {s: [Fraction(1)] + [Fraction(0)] * n for s in pgf_values}
        for a in range(1, n + 1):
            probabilities = [Fraction(comb(a, b) * closed_count(n, a, b, 1), total) for b in range(a + 1)]
            ledger.equal("absorption", sum(probabilities), Fraction(1), "size-row mass")
            self_loop = probabilities[a]
            mean[a] = (
                1 + sum(probabilities[b] * mean[b] for b in range(1, a))
            ) / (1 - self_loop)
            second[a] = (
                1
                + 2 * sum(probabilities[b] * mean[b] for b in range(1, a + 1))
                + sum(probabilities[b] * second[b] for b in range(1, a))
            ) / (1 - self_loop)
            lambda_values = [Fraction(factorial(n - j), total) for j in range(a + 1)]
            closed_mean = sum(
                Fraction((-1) ** (j + 1) * comb(a, j), 1 - lambda_values[j])
                for j in range(1, a + 1)
            )
            closed_second = sum(
                Fraction(
                    (-1) ** (j + 1) * comb(a, j) * (1 + lambda_values[j]),
                    (1 - lambda_values[j]) ** 2,
                )
                for j in range(1, a + 1)
            )
            ledger.equal("absorption", mean[a], closed_mean, f"mean n={n},a={a}")
            ledger.equal("absorption", second[a], closed_second, f"second n={n},a={a}")
            for s in pgf_values:
                pgf[s][a] = (
                    s * probabilities[0]
                    + s * sum(probabilities[b] * pgf[s][b] for b in range(1, a))
                ) / (1 - s * self_loop)
                closed_pgf = 1 - (1 - s) * sum(
                    Fraction((-1) ** (j + 1) * comb(a, j), 1 - s * lambda_values[j])
                    for j in range(1, a + 1)
                )
                ledger.equal("absorption", pgf[s][a], closed_pgf, "PGF")
            for time in range(0, 9):
                cdf_from_endpoint = Fraction(closed_count(n, a, 0, time), total**time)
                ledger.equal(
                    "absorption",
                    1 - cdf_from_endpoint,
                    spectral_survival(n, a, time),
                    "survival/CDF",
                )
            ledger.record("absorption", n, a, mean[a], second[a])

    ledger.equal("boundary", endpoint_after(1, [(0,)] * 5), 1, "n=1 never absorbs")
    for a in range(1, 3):
        for time in range(0, 15):
            ledger.equal(
                "boundary",
                spectral_survival(2, a, time),
                Fraction(1, 2) ** time,
                "n=2 collapse",
            )
    for a in range(1, 4):
        for time in range(0, 15):
            repaired = a * Fraction(1, 3) ** time - (comb(a, 2) - comb(a, 3)) * Fraction(1, 6) ** time
            ledger.equal("boundary", spectral_survival(3, a, time), repaired, "n=3 repair")
    for n in range(4, 65):
        lambdas = [Fraction(factorial(n - j), factorial(n)) for j in range(4)]
        ledger.true("boundary", lambdas[1] > lambdas[2] > lambdas[3], "n>=4 scale separation")


def main() -> None:
    ledger = Ledger()
    verify_literal_histories(ledger)
    verify_marked_histories(ledger)
    verify_uniform_marked_contract(ledger)
    verify_spectrum(ledger)
    verify_absorption(ledger)
    print("P170_AUTHOR_EXACT_VERIFIER_V1")
    for section in sorted(ledger.section_counts):
        print(f"{section}_assertions={ledger.section_counts[section]}")
    print(f"fingerprint_rows={ledger.rows}")
    print(f"payload_sha256={ledger.digest.hexdigest()}")
    print(f"assertions={ledger.assertions}")
    print("n3_boundary=REPAIRED_EXACT")
    print("decision=AUTHOR_ROUND0_PASS")
    print("external_status=HOLD_EXTERNAL_OWNER_THIN")


if __name__ == "__main__":
    main()
