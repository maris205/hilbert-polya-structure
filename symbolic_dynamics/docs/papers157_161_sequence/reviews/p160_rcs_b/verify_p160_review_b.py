#!/usr/bin/env python3
"""Independent exact verifier for P160 Hostile Review B.

This program uses only the Python standard library.  It deliberately does
not import the author verifier or any earlier review verifier.  Literal
partition enumeration is compared against separately implemented formulas.
"""

from __future__ import annotations

from collections import defaultdict
from functools import lru_cache
from hashlib import sha256
from pathlib import Path


MAX_WEIGHT = 28
ITERATE_WEIGHT = 28


class Audit:
    def __init__(self) -> None:
        self.assertions = 0
        self.sections: list[tuple[str, int]] = []

    def check(self, condition: bool, message: str) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(f"assertion {self.assertions}: {message}")

    def equal(self, actual, expected, message: str) -> None:
        self.assertions += 1
        if actual != expected:
            raise AssertionError(
                f"assertion {self.assertions}: {message}: "
                f"actual={actual!r}, expected={expected!r}"
            )

    def mark(self, name: str, start: int) -> None:
        self.sections.append((name, self.assertions - start))


AUDIT = Audit()


@lru_cache(maxsize=None)
def partitions_of(n: int, ceiling: int | None = None) -> tuple[tuple[int, ...], ...]:
    """Return all partitions of n in reverse lexicographic order."""
    if n < 0:
        return ()
    if n == 0:
        return ((),)
    if ceiling is None or ceiling > n:
        ceiling = n
    out: list[tuple[int, ...]] = []
    for first in range(ceiling, 0, -1):
        for tail in partitions_of(n - first, first):
            out.append((first,) + tail)
    return tuple(out)


PARTS_BY_WEIGHT = tuple(partitions_of(n) for n in range(MAX_WEIGHT + 1))
ALL_PARTS = tuple(part for level in PARTS_BY_WEIGHT for part in level)


def weight(part: tuple[int, ...]) -> int:
    return sum(part)


def is_partition(part: tuple[int, ...]) -> bool:
    return all(x > 0 for x in part) and all(
        part[i] >= part[i + 1] for i in range(len(part) - 1)
    )


def conjugate(part: tuple[int, ...]) -> tuple[int, ...]:
    if not part:
        return ()
    return tuple(sum(row >= j for row in part) for j in range(1, part[0] + 1))


def literal_crop(part: tuple[int, ...], rows: int, columns: int) -> tuple[int, ...]:
    """Delete rows and columns literally, then omit empty rows."""
    assert rows >= 0 and columns >= 0
    return tuple(row - columns for row in part[rows:] if row > columns)


def literal_step(part: tuple[int, ...], a: int, b: int) -> tuple[int, ...]:
    assert a >= 1 and b >= 1
    return literal_crop(part, a, b)


def repeated_step(part: tuple[int, ...], a: int, b: int, t: int) -> tuple[int, ...]:
    out = part
    for _ in range(t):
        out = literal_step(out, a, b)
    return out


def formula_iterate(part: tuple[int, ...], a: int, b: int, t: int) -> tuple[int, ...]:
    return literal_crop(part, a * t, b * t)


def clock_literal(part: tuple[int, ...], a: int, b: int) -> int:
    t = 0
    state = part
    while state:
        state = literal_step(state, a, b)
        t += 1
    return t


def clock_formula(part: tuple[int, ...], a: int, b: int) -> int:
    t = 0
    while True:
        indexed_part = part[a * t] if a * t < len(part) else 0
        if indexed_part <= b * t:
            return t
        t += 1


def capped_height_formula(a: int, b: int, cap: int) -> int:
    t = 0
    while (a * t + 1) * (b * t + 1) <= cap:
        t += 1
    return t


@lru_cache(maxsize=None)
def bounded_partition_coefficients(bound: int, degree: int) -> tuple[int, ...]:
    """Coefficients of prod_{j=1}^bound (1-q^j)^(-1) through degree."""
    coeff = [0] * (degree + 1)
    coeff[0] = 1
    for size in range(1, bound + 1):
        for n in range(size, degree + 1):
            coeff[n] += coeff[n - size]
    return tuple(coeff)


def convolution_coeff(h: int, w: int, degree: int) -> int:
    if degree < 0:
        return 0
    ph = bounded_partition_coefficients(h, degree)
    pw = bounded_partition_coefficients(w, degree)
    return sum(ph[j] * pw[degree - j] for j in range(degree + 1))


def empty_formula_coeff(h: int, w: int, n: int) -> int:
    """Coefficient of E_{h,w}, implemented directly from its finite sum."""
    total = 0
    ph = bounded_partition_coefficients(h, n)
    for k in range(w + 1):
        rectangle = k * (h + 1)
        if rectangle <= n:
            pk = bounded_partition_coefficients(k, n - rectangle)
            total += sum(
                ph[j] * pk[n - rectangle - j]
                for j in range(n - rectangle + 1)
            )
    return total


def threshold(mu: tuple[int, ...], h: int, w: int) -> int:
    assert mu
    return weight(mu) + h * (mu[0] + w) + w * len(mu)


def split_source(
    source: tuple[int, ...], h: int, w: int
) -> tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]:
    """Decode a nonempty crop fibre as (target, top excess, bottom)."""
    mu = literal_crop(source, h, w)
    assert mu
    r = len(mu)
    baseline = mu[0] + w
    gamma_padded = tuple(source[i] - baseline for i in range(h))
    gamma = tuple(x for x in gamma_padded if x > 0)
    beta = source[h + r :]
    return mu, gamma, beta


def rebuild_source(
    mu: tuple[int, ...],
    h: int,
    w: int,
    gamma: tuple[int, ...],
    beta: tuple[int, ...],
) -> tuple[int, ...]:
    assert mu
    assert len(gamma) <= h
    assert not beta or beta[0] <= w
    padded = gamma + (0,) * (h - len(gamma))
    baseline = mu[0] + w
    top = tuple(baseline + x for x in padded)
    middle = tuple(x + w for x in mu)
    return top + middle + beta


def every_weight_witness(
    mu: tuple[int, ...], h: int, w: int, excess: int
) -> tuple[int, ...]:
    """Boundary-aware witness; actual theorem uses only h,w>0."""
    assert mu and excess >= 0
    if h > 0:
        gamma = () if excess == 0 else (excess,)
        beta: tuple[int, ...] = ()
    elif w > 0:
        gamma = ()
        beta = (1,) * excess
    else:
        assert excess == 0
        gamma = ()
        beta = ()
    return rebuild_source(mu, h, w, gamma, beta)


def test_partition_engine() -> None:
    start = AUDIT.assertions
    seen: set[tuple[int, ...]] = set()
    for n, level in enumerate(PARTS_BY_WEIGHT):
        for part in level:
            AUDIT.check(is_partition(part) or not part, f"partition validity {part}")
            AUDIT.equal(weight(part), n, f"partition weight {part}")
            AUDIT.check(part not in seen, f"duplicate partition {part}")
            seen.add(part)
            AUDIT.equal(conjugate(conjugate(part)), part, f"double conjugate {part}")
    AUDIT.mark("partition_engine", start)


def test_iterates_clocks_heights_and_conjugation() -> None:
    start = AUDIT.assertions
    parameter_pairs = (
        (1, 1),
        (1, 2),
        (2, 1),
        (1, 3),
        (3, 1),
        (2, 3),
        (3, 2),
        (2, 2),
    )
    all_small = tuple(
        part for n in range(ITERATE_WEIGHT + 1) for part in PARTS_BY_WEIGHT[n]
    )
    for a, b in parameter_pairs:
        clocks_by_weight: list[list[int]] = [[] for _ in range(ITERATE_WEIGHT + 1)]
        for source in all_small:
            tau_lit = clock_literal(source, a, b)
            AUDIT.equal(tau_lit, clock_formula(source, a, b), f"clock {a,b,source}")
            clocks_by_weight[weight(source)].append(tau_lit)
            for t in range(6):
                literal = repeated_step(source, a, b, t)
                closed = formula_iterate(source, a, b, t)
                AUDIT.equal(literal, closed, f"iterate {a,b,t,source}")
                row_index = a * t
                row_length = source[row_index] if row_index < len(source) else 0
                survives = row_length >= b * t + 1
                AUDIT.equal(bool(literal), survives, f"corner survival {a,b,t,source}")
            lhs = conjugate(literal_step(source, a, b))
            rhs = literal_step(conjugate(source), b, a)
            AUDIT.equal(lhs, rhs, f"conjugation {a,b,source}")

        running_max = 0
        for cap in range(ITERATE_WEIGHT + 1):
            if clocks_by_weight[cap]:
                running_max = max(running_max, max(clocks_by_weight[cap]))
            expected = capped_height_formula(a, b, cap)
            AUDIT.equal(running_max, expected, f"height {a,b,cap}")
            if expected == 0:
                AUDIT.equal(cap, 0, f"zero height cap {a,b,cap}")
            else:
                prev = expected - 1
                rect_weight = (a * prev + 1) * (b * prev + 1)
                witness = (b * prev + 1,) * (a * prev + 1)
                AUDIT.check(rect_weight <= cap, f"sharp rectangle fits {a,b,cap}")
                AUDIT.equal(weight(witness), rect_weight, f"rectangle weight {a,b,cap}")
                AUDIT.check(
                    clock_literal(witness, a, b) > prev,
                    f"sharp rectangle survives {a,b,cap}",
                )
    AUDIT.mark("iterates_clocks_heights_conjugation", start)


def test_fibres_and_artificial_boundaries() -> dict[tuple[int, int], dict[tuple[int, ...], list[int]]]:
    start = AUDIT.assertions
    boundary_pairs = (
        (0, 0),
        (0, 1),
        (0, 4),
        (1, 0),
        (4, 0),
        (1, 1),
        (1, 2),
        (2, 1),
        (2, 3),
        (3, 2),
        (4, 2),
        (2, 4),
        (5, 3),
        (3, 5),
    )
    all_counts: dict[tuple[int, int], dict[tuple[int, ...], list[int]]] = {}
    for h, w in boundary_pairs:
        counts: dict[tuple[int, ...], list[int]] = defaultdict(
            lambda: [0] * (MAX_WEIGHT + 1)
        )
        for source in ALL_PARTS:
            mu = literal_crop(source, h, w)
            counts[mu][weight(source)] += 1
            if mu:
                decoded_mu, gamma, beta = split_source(source, h, w)
                AUDIT.equal(decoded_mu, mu, f"decoded target {h,w,source}")
                AUDIT.check(len(gamma) <= h, f"gamma length {h,w,source,gamma}")
                AUDIT.check(is_partition(gamma) or not gamma, f"gamma shape {h,w,source,gamma}")
                AUDIT.check(is_partition(beta) or not beta, f"beta shape {h,w,source,beta}")
                AUDIT.check(not beta or beta[0] <= w, f"beta bound {h,w,source,beta}")
                AUDIT.equal(
                    rebuild_source(mu, h, w, gamma, beta),
                    source,
                    f"fibre bijection {h,w,source}",
                )
                AUDIT.equal(
                    weight(source),
                    threshold(mu, h, w) + weight(gamma) + weight(beta),
                    f"fibre weight split {h,w,source}",
                )

        for n in range(MAX_WEIGHT + 1):
            AUDIT.equal(
                counts[()][n],
                empty_formula_coeff(h, w, n),
                f"empty fibre coefficient {h,w,n}",
            )
        for mu in ALL_PARTS:
            if not mu:
                continue
            m = threshold(mu, h, w)
            observed = counts[mu]
            for n in range(MAX_WEIGHT + 1):
                expected = convolution_coeff(h, w, n - m)
                AUDIT.equal(observed[n], expected, f"target fibre {h,w,mu,n}")
        all_counts[(h, w)] = counts
    AUDIT.mark("fibres_empty_branch_artificial_boundaries", start)
    return all_counts


def test_support_caps_and_repaired_witness(
    all_counts: dict[tuple[int, int], dict[tuple[int, ...], list[int]]]
) -> None:
    start = AUDIT.assertions
    targets = (
        (1,),
        (2,),
        (1, 1),
        (3, 1),
        (3, 3),
        (4, 2, 1),
        (2, 2, 2),
    )
    actual_pairs = ((1, 1), (1, 2), (2, 1), (2, 3), (3, 2), (4, 2), (2, 4))
    for h, w in actual_pairs:
        counts = all_counts[(h, w)]
        for mu in targets:
            m = threshold(mu, h, w)
            for excess in range(max(0, MAX_WEIGHT - m) + 1):
                # This is exactly the repaired gamma=(d), beta=empty witness.
                source = every_weight_witness(mu, h, w, excess)
                expected_gamma = () if excess == 0 else (excess,)
                decoded_mu, gamma, beta = split_source(source, h, w)
                AUDIT.equal(decoded_mu, mu, f"witness target {h,w,mu,excess}")
                AUDIT.equal(gamma, expected_gamma, f"gamma=(d) {h,w,mu,excess}")
                AUDIT.equal(beta, (), f"witness beta empty {h,w,mu,excess}")
                AUDIT.check(len(gamma) <= h, f"witness gamma legal {h,w,mu,excess}")
                AUDIT.check(is_partition(source), f"witness source shape {h,w,mu,excess}")
                AUDIT.equal(weight(source), m + excess, f"witness weight {h,w,mu,excess}")
                AUDIT.equal(literal_crop(source, h, w), mu, f"witness maps {h,w,mu,excess}")

            for cap in range(MAX_WEIGHT + 1):
                actual_in_cap_image = any(counts[mu][n] for n in range(cap + 1))
                AUDIT.equal(actual_in_cap_image, m <= cap, f"cap image {h,w,mu,cap}")
            expected_weights = set(range(m, MAX_WEIGHT + 1)) if m <= MAX_WEIGHT else set()
            actual_weights = {n for n, count in enumerate(counts[mu]) if count}
            AUDIT.equal(actual_weights, expected_weights, f"every source weight {h,w,mu}")

    # Artificial degeneracies are not within a,b>=1,t>=1, but stress the
    # boundary conventions.  gamma=(d) remains legal for h>0,w=0.  If h=0
    # and w>0, bottom beta=(1^d) supplies every excess; for h=w=0 only d=0.
    for h, w in ((1, 0), (4, 0), (0, 1), (0, 4), (0, 0)):
        for mu in targets:
            m = threshold(mu, h, w)
            limit = max(0, min(8, MAX_WEIGHT - m))
            for excess in range(limit + 1):
                if h == 0 and w == 0 and excess > 0:
                    continue
                source = every_weight_witness(mu, h, w, excess)
                decoded_mu, gamma, beta = split_source(source, h, w)
                AUDIT.equal(decoded_mu, mu, f"boundary witness target {h,w,mu,excess}")
                AUDIT.equal(weight(source), m + excess, f"boundary witness weight {h,w,mu,excess}")
                AUDIT.equal(literal_crop(source, h, w), mu, f"boundary witness map {h,w,mu,excess}")
                if h > 0:
                    AUDIT.equal(gamma, () if excess == 0 else (excess,), f"boundary gamma {h,w,mu,excess}")
                    AUDIT.equal(beta, (), f"boundary beta {h,w,mu,excess}")
                elif w > 0:
                    AUDIT.equal(gamma, (), f"boundary gamma absent {h,w,mu,excess}")
                    AUDIT.equal(beta, (1,) * excess, f"boundary beta=(1^d) {h,w,mu,excess}")
                else:
                    AUDIT.equal(excess, 0, f"identity exact weight {mu}")
    AUDIT.mark("support_caps_repaired_witness", start)


def test_t_zero_recovery_and_mass(
    all_counts: dict[tuple[int, int], dict[tuple[int, ...], list[int]]]
) -> None:
    start = AUDIT.assertions
    # t=0 is identity: singleton source at exactly the target weight.
    identity_counts = all_counts[(0, 0)]
    for mu in ALL_PARTS:
        for n in range(MAX_WEIGHT + 1):
            AUDIT.equal(
                identity_counts[mu][n],
                int(n == weight(mu)),
                f"t=0 singleton fibre {mu,n}",
            )

    # One-step target thresholds recover ordered, including asymmetric pairs.
    for a, b in ((1, 1), (1, 2), (2, 1), (1, 3), (3, 1), (2, 3), (3, 2)):
        probes = ((1,), (2,), (1, 1))
        minima: dict[tuple[int, ...], int] = {}
        for mu in probes:
            candidates = [
                weight(source)
                for source in ALL_PARTS
                if literal_step(source, a, b) == mu
            ]
            AUDIT.check(bool(candidates), f"recovery source exists {a,b,mu}")
            minima[mu] = min(candidates)
            AUDIT.equal(minima[mu], threshold(mu, a, b), f"probe threshold {a,b,mu}")
        recovered_a = minima[(2,)] - minima[(1,)] - 1
        recovered_b = minima[(1, 1)] - minima[(1,)] - 1
        AUDIT.equal(recovered_a, a, f"recover a {a,b}")
        AUDIT.equal(recovered_b, b, f"recover b {a,b}")
        AUDIT.equal(minima[(1,)], (a + 1) * (b + 1), f"one-cell threshold {a,b}")

    # Coefficientwise mass identity, including one-sided and zero boundaries.
    for h, w in ((0, 0), (0, 3), (3, 0), (1, 2), (2, 1), (3, 4), (4, 3)):
        for n in range(MAX_WEIGHT + 1):
            rhs = empty_formula_coeff(h, w, n)
            for mu in ALL_PARTS:
                if mu:
                    rhs += convolution_coeff(h, w, n - threshold(mu, h, w))
            AUDIT.equal(rhs, len(PARTS_BY_WEIGHT[n]), f"mass identity {h,w,n}")
    AUDIT.mark("t_zero_recovery_mass", start)


def main() -> None:
    test_partition_engine()
    test_iterates_clocks_heights_and_conjugation()
    all_counts = test_fibres_and_artificial_boundaries()
    test_support_caps_and_repaired_witness(all_counts)
    test_t_zero_recovery_and_mass(all_counts)

    script_hash = sha256(Path(__file__).read_bytes()).hexdigest()
    print("P160 HOSTILE REVIEW B -- INDEPENDENT EXACT VERIFIER")
    print(f"script_sha256={script_hash}")
    print(f"max_weight={MAX_WEIGHT}")
    print(f"partitions_enumerated={len(ALL_PARTS)}")
    for name, count in AUDIT.sections:
        print(f"section.{name}={count}")
    print(f"assertions={AUDIT.assertions}")
    print("result=PASS")


if __name__ == "__main__":
    main()
