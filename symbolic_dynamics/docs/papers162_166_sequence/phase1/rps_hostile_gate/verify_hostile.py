#!/usr/bin/env python3
"""Independent exact hostile verifier for the random-permutation sieve.

No author module is imported.  Permutations are traversed literally; the
subset transition rows, Boolean-zeta conjugation, cardinality-chain moments,
and cycle-marked powers are reconstructed here from scratch.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import permutations
from math import comb, factorial


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def eq(self, got, want, label: str) -> None:
        self.assertions += 1
        if got != want:
            raise AssertionError(f"{label}: got {got!r}, want {want!r}")

    def ok(self, condition: bool, label: str) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(label)


A = Audit()
Poly = tuple[int, ...]


def trim(p: list[int] | tuple[int, ...]) -> Poly:
    q = list(p)
    while len(q) > 1 and q[-1] == 0:
        q.pop()
    return tuple(q or [0])


def poly_add(left: Poly, right: Poly, scale: int = 1) -> Poly:
    out = [0] * max(len(left), len(right))
    for i, value in enumerate(left):
        out[i] += value
    for i, value in enumerate(right):
        out[i] += scale * value
    return trim(out)


def poly_mul(left: Poly, right: Poly) -> Poly:
    out = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] += x * y
    return trim(out)


def poly_pow(base: Poly, exponent: int) -> Poly:
    out = (1,)
    while exponent:
        if exponent & 1:
            out = poly_mul(out, base)
        base = poly_mul(base, base)
        exponent //= 2
    return out


def poly_eval(p: Poly, value: int) -> int:
    out = 0
    for coefficient in reversed(p):
        out = out * value + coefficient
    return out


def permutation_profile(n: int) -> tuple[tuple[int, int], ...]:
    """Return literal (fixed-set mask, cycle count) data for every pi in S_n."""
    rows = []
    for pi in permutations(range(n)):
        fixed = sum(1 << i for i in range(n) if pi[i] == i)
        seen = set()
        cycles = 0
        for start in range(n):
            if start in seen:
                continue
            cycles += 1
            x = start
            while x not in seen:
                seen.add(x)
                x = pi[x]
        A.eq(len(seen), n, "literal cycle decomposition covers [n]")
        rows.append((fixed, cycles))
    A.eq(len(rows), factorial(n), "literal permutation count")
    return tuple(rows)


def literal_rows(n: int, profile: tuple[tuple[int, int], ...]):
    size = 1 << n
    rows: list[Counter[int]] = []
    marked: list[dict[int, Poly]] = []
    for source in range(size):
        row: Counter[int] = Counter()
        by_target: dict[int, Counter[int]] = defaultdict(Counter)
        for fixed, cycles in profile:
            target = source & fixed
            row[target] += 1
            by_target[target][cycles] += 1
        rows.append(row)
        marked.append({
            target: trim([counts.get(k, 0) for k in range(n + 1)])
            for target, counts in by_target.items()
        })
    return tuple(rows), tuple(marked)


def endpoint_count(n: int, source: int, target: int, t: int) -> int:
    if target & ~source:
        return 0
    a = source.bit_count()
    b = target.bit_count()
    return sum(
        (-1) ** j * comb(a - b, j) * factorial(n - b - j) ** t
        for j in range(a - b + 1)
    )


def count_step(distribution: Counter[int], rows: tuple[Counter[int], ...]) -> Counter[int]:
    out: Counter[int] = Counter()
    for state, histories in distribution.items():
        for target, multiplicity in rows[state].items():
            out[target] += histories * multiplicity
    return +out


def rising_cycle_polynomial(n: int, prescribed: int) -> Poly:
    """u^prescribed times u rising to n-prescribed, built algebraically."""
    out: Poly = (0,) * prescribed + (1,)
    for shift in range(n - prescribed):
        out = poly_mul(out, (shift, 1))
    return out


def marked_endpoint_formula(n: int, source: int, target: int, t: int) -> Poly:
    if target & ~source:
        return (0,)
    a = source.bit_count()
    b = target.bit_count()
    out: Poly = (0,)
    for j in range(a - b + 1):
        term = poly_pow(rising_cycle_polynomial(n, b + j), t)
        out = poly_add(out, term, (-1) ** j * comb(a - b, j))
    return out


def marked_step(distribution: dict[int, Poly], rows: tuple[dict[int, Poly], ...]) -> dict[int, Poly]:
    out: dict[int, Poly] = {}
    for state, history_poly in distribution.items():
        for target, epoch_poly in rows[state].items():
            product_poly = poly_mul(history_poly, epoch_poly)
            out[target] = poly_add(out.get(target, (0,)), product_poly)
    return {target: p for target, p in out.items() if p != (0,)}


def lambda_value(n: int, r: int) -> Fraction:
    return Fraction(factorial(n - r), factorial(n))


def cdf_formula(n: int, a: int, t: int) -> Fraction:
    return sum(
        (Fraction((-1) ** j * comb(a, j)) * lambda_value(n, j) ** t
         for j in range(a + 1)),
        Fraction(0),
    )


def survival_formula(n: int, a: int, t: int) -> Fraction:
    return sum(
        (Fraction((-1) ** (j + 1) * comb(a, j)) * lambda_value(n, j) ** t
         for j in range(1, a + 1)),
        Fraction(0),
    )


def mean_formula(n: int, a: int) -> Fraction:
    return sum(
        (Fraction((-1) ** (j + 1) * comb(a, j), 1 - lambda_value(n, j))
         for j in range(1, a + 1)),
        Fraction(0),
    )


def second_formula(n: int, a: int) -> Fraction:
    return sum(
        (Fraction((-1) ** (j + 1) * comb(a, j))
         * (1 + lambda_value(n, j)) / (1 - lambda_value(n, j)) ** 2
         for j in range(1, a + 1)),
        Fraction(0),
    )


def pgf_formula(n: int, a: int, s: Fraction) -> Fraction:
    if a == 0:
        return Fraction(1)
    tail = sum(
        (Fraction((-1) ** (j + 1) * comb(a, j), 1 - s * lambda_value(n, j))
         for j in range(1, a + 1)),
        Fraction(0),
    )
    return 1 - (1 - s) * tail


def cardinality_kernel(n: int, rows: tuple[Counter[int], ...]) -> tuple[tuple[int, ...], ...]:
    kernel = []
    for a in range(n + 1):
        source = (1 << a) - 1
        counts = [0] * (n + 1)
        for target, multiplicity in rows[source].items():
            counts[target.bit_count()] += multiplicity
        A.eq(sum(counts), factorial(n), "cardinality-chain row mass")
        kernel.append(tuple(counts))
    return tuple(kernel)


def recurrence_moments(n: int, kernel: tuple[tuple[int, ...], ...]):
    denominator = factorial(n)
    means = [Fraction(0)] * (n + 1)
    seconds = [Fraction(0)] * (n + 1)
    for a in range(1, n + 1):
        stay = Fraction(kernel[a][a], denominator)
        strict_mean = sum(
            (Fraction(kernel[a][b], denominator) * means[b] for b in range(a)),
            Fraction(0),
        )
        strict_second = sum(
            (Fraction(kernel[a][b], denominator) * seconds[b] for b in range(a)),
            Fraction(0),
        )
        means[a] = (1 + strict_mean) / (1 - stay)
        seconds[a] = (1 + 2 * (stay * means[a] + strict_mean) + strict_second) / (1 - stay)
    return tuple(means), tuple(seconds)


def recurrence_pgf(n: int, kernel: tuple[tuple[int, ...], ...], s: Fraction) -> tuple[Fraction, ...]:
    denominator = factorial(n)
    values = [Fraction(1)] + [Fraction(0)] * n
    for a in range(1, n + 1):
        lower = sum(
            (Fraction(kernel[a][b], denominator) * values[b] for b in range(a)),
            Fraction(0),
        )
        stay = Fraction(kernel[a][a], denominator)
        values[a] = s * lower / (1 - s * stay)
    return tuple(values)


def check_unmarked() -> tuple[int, str]:
    payload = []
    boxes = 0
    for n in range(1, 8):
        profile = permutation_profile(n)
        rows, _ = literal_rows(n, profile)
        size = 1 << n
        den = factorial(n)

        # One-step literal rows and all-time endpoint formula, including t=0.
        for source in range(size):
            A.eq(sum(rows[source].values()), den, "literal row mass")
            distribution = Counter({source: 1})
            for t in range(0, 6):
                for target in range(size):
                    literal = distribution[target]
                    predicted = endpoint_count(n, source, target, t)
                    A.eq(literal, predicted, "all-time every-endpoint IE")
                    if t == 0:
                        A.eq(literal > 0, target == source, "t=0 identity support")
                    else:
                        allowed = not (target & ~source) and not (
                            source == size - 1 and target.bit_count() == n - 1
                        )
                        A.eq(literal > 0, allowed, "positive-time unique support hole")
                A.eq(sum(distribution.values()), den**t, "history mass")
                distribution = count_step(distribution, rows)

        # Full zeta conjugation, its explicit inverse, and repeated eigenvalues.
        for source in range(size):
            for witness in range(size):
                lhs = sum(
                    multiplicity
                    for target, multiplicity in rows[source].items()
                    if target & witness == witness
                )
                rhs = factorial(n - witness.bit_count()) if source & witness == witness else 0
                A.eq(lhs, rhs, "M Z = Z D")
        for source in range(size):
            for target in range(size):
                inverse_entry = sum(
                    ((-1) ** ((middle ^ target).bit_count())
                     for middle in range(size)
                     if middle & ~source == 0 and target & ~middle == 0),
                    0,
                )
                A.eq(inverse_entry, int(source == target), "Boolean zeta/Mobius inverse")
        multiplicities = Counter(factorial(n - witness.bit_count()) for witness in range(size))
        if n == 1:
            A.eq(multiplicities, Counter({1: 2}), "n=1 repeated spectrum")
        else:
            A.eq(multiplicities[1], n + 1, "lambda_(n-1)=lambda_n repeat")
            A.eq(sum(multiplicities.values()), size, "complete eigenbasis multiplicity")

        # Absorption CDF, moments, and PGF from an independent size-chain solve.
        if n == 1:
            A.eq(rows[1], Counter({1: 1}), "n=1 nonempty state absorbing")
        else:
            kernel = cardinality_kernel(n, rows)
            means, seconds = recurrence_moments(n, kernel)
            for a in range(n + 1):
                A.eq(means[a], mean_formula(n, a), "absorption mean")
                A.eq(seconds[a], second_formula(n, a), "absorption second moment")
                source = (1 << a) - 1
                distribution = Counter({source: 1})
                for t in range(0, 9):
                    direct = Fraction(distribution[0], den**t)
                    A.eq(direct, cdf_formula(n, a, t), "absorption CDF")
                    A.eq(1 - direct, survival_formula(n, a, t), "survival tail finite sum")
                    distribution = count_step(distribution, rows)
            for s in (Fraction(0), Fraction(1, 5), Fraction(1, 2), Fraction(2, 3), Fraction(1)):
                solved = recurrence_pgf(n, kernel, s)
                for a in range(n + 1):
                    A.eq(solved[a], pgf_formula(n, a, s), "absorption PGF")

            # The repeated factorial eigenvalue creates distinct n=2 and n=3 boundaries.
            for a in range(1, n + 1):
                for t in range(0, 12):
                    actual = survival_formula(n, a, t)
                    if n == 2:
                        boundary = Fraction(a - comb(a, 2), 2**t)
                        A.eq(actual, boundary, "n=2 combined leading eigenspace")
                    elif n == 3:
                        boundary = Fraction(a, 3**t) - Fraction(comb(a, 2) - comb(a, 3), 6**t)
                        A.eq(actual, boundary, "n=3 combined second eigenspace")
                    else:
                        first_two = Fraction(a, n**t) - Fraction(comb(a, 2), (n * (n - 1)) ** t)
                        remainder = sum(
                            (Fraction((-1) ** (j + 1) * comb(a, j)) * lambda_value(n, j) ** t
                             for j in range(3, a + 1)),
                            Fraction(0),
                        )
                        A.eq(actual, first_two + remainder, "n>=4 separated first two scales")

        payload.append((n, tuple(sorted(rows[size - 1].items())), tuple(sorted(multiplicities.items()))))
        boxes += 1
    return boxes, sha256(repr(payload).encode()).hexdigest()


def check_marked() -> tuple[int, str]:
    payload = []
    boxes = 0
    for n in range(1, 6):
        profile = permutation_profile(n)
        rows, marked_rows = literal_rows(n, profile)
        size = 1 << n

        # First check the prescribed-fixed cycle enumerator directly.
        for prescribed in range(n + 1):
            direct = [0] * (n + 1)
            required_mask = (1 << prescribed) - 1
            for fixed, cycles in profile:
                if fixed & required_mask == required_mask:
                    direct[cycles] += 1
            A.eq(trim(direct), rising_cycle_polynomial(n, prescribed), "prescribed-fixed cycle polynomial")

        # Polynomial transition powers versus marked inclusion--exclusion.
        for source in range(size):
            distribution: dict[int, Poly] = {source: (1,)}
            for t in range(0, 4):
                for target in range(size):
                    literal = distribution.get(target, (0,))
                    predicted = marked_endpoint_formula(n, source, target, t)
                    A.eq(literal, predicted, "cycle-marked every-history formula")
                    A.ok(all(coefficient >= 0 for coefficient in predicted), "marked coefficients nonnegative")
                    A.eq(poly_eval(predicted, 1), endpoint_count(n, source, target, t), "u=1 marked specialization")
                distribution = marked_step(distribution, marked_rows)

        payload.append((n, tuple((target, p) for target, p in sorted(marked_rows[size - 1].items()))))
        boxes += 1
    return boxes, sha256(repr(payload).encode()).hexdigest()


def check_parameter_recovery() -> tuple[int, str]:
    seen: dict[Fraction, int] = {}
    rows = []
    for n in range(2, 13):
        self_loop = Fraction(factorial(n - 1), factorial(n))
        A.eq(self_loop, Fraction(1, n), "singleton self-loop")
        A.ok(self_loop not in seen, "parameter recovery injective")
        seen[self_loop] = n
        rows.append((n, self_loop.numerator, self_loop.denominator))
    return len(rows), sha256(repr(rows).encode()).hexdigest()


def main() -> None:
    unmarked_boxes, unmarked_digest = check_unmarked()
    marked_boxes, marked_digest = check_marked()
    recovery_boxes, recovery_digest = check_parameter_recovery()
    print("RPS INDEPENDENT HOSTILE GATE")
    print(f"unmarked_boxes={unmarked_boxes} digest={unmarked_digest}")
    print(f"marked_boxes={marked_boxes} digest={marked_digest}")
    print(f"recovery_boxes={recovery_boxes} digest={recovery_digest}")
    print("boundary_tail=n2_combined_lambda1_lambda2,n3_combined_lambda2_lambda3")
    print(f"ASSERTIONS {A.assertions}")
    print("STATUS PASS_WITH_N3_TAIL_STATEMENT_REPAIR")


if __name__ == "__main__":
    main()
