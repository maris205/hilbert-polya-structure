#!/usr/bin/env python3
"""Independent hostile-review verifier for P160 rectangular-corner stripping.

This file deliberately imports no author code.  The dynamical update is
implemented first as a literal operation on Ferrers cells.  Algebraic formulas,
generating-function coefficients, fibre counts, and reconstruction witnesses
are implemented separately and compared exactly over finite exhaustive ranges.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from itertools import product


MAX_WEIGHT = 30
MAX_TARGET_WEIGHT = 10
PARAMETERS = tuple(product(range(1, 5), repeat=2))
TIMES = tuple(range(0, 6))
BOUNDARY_WINDOWS = tuple(
    sorted({(0, w) for w in range(0, 6)} | {(h, 0) for h in range(0, 6)}
           | {(1, 1), (2, 3), (3, 2), (4, 5)})
)


checks = 0


def check(condition: bool, label: str) -> None:
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)


@lru_cache(maxsize=None)
def partitions_exact(n: int, cap: int | None = None) -> tuple[tuple[int, ...], ...]:
    """All partitions of n, recursively and independently of author code."""
    if n == 0:
        return ((),)
    if cap is None or cap > n:
        cap = n
    out: list[tuple[int, ...]] = []
    for first in range(cap, 0, -1):
        for tail in partitions_exact(n - first, first):
            out.append((first,) + tail)
    return tuple(out)


PARTS_BY_WEIGHT = tuple(partitions_exact(n) for n in range(MAX_WEIGHT + 1))
ALL_PARTS = tuple(shape for layer in PARTS_BY_WEIGHT for shape in layer)
TARGETS = tuple(
    shape for n in range(MAX_TARGET_WEIGHT + 1) for shape in PARTS_BY_WEIGHT[n]
)


def weight(shape: tuple[int, ...]) -> int:
    return sum(shape)


@lru_cache(maxsize=None)
def ferrers_cells(shape: tuple[int, ...]) -> frozenset[tuple[int, int]]:
    return frozenset((i, j) for i, row in enumerate(shape) for j in range(row))


def shape_from_cells(cells: frozenset[tuple[int, int]]) -> tuple[int, ...]:
    if not cells:
        return ()
    counts = Counter(i for i, _ in cells)
    rows = tuple(counts[i] for i in range(max(counts) + 1))
    check(all(rows[i] >= rows[i + 1] for i in range(len(rows) - 1)),
          f"non-Ferrers result {rows}")
    return tuple(row for row in rows if row > 0)


@lru_cache(maxsize=None)
def literal_crop(shape: tuple[int, ...], h: int, w: int) -> tuple[int, ...]:
    """Delete h rows and w columns literally, then translate retained cells."""
    kept = frozenset(
        (i - h, j - w)
        for i, j in ferrers_cells(shape)
        if i >= h and j >= w
    )
    return shape_from_cells(kept)


@lru_cache(maxsize=None)
def row_crop(shape: tuple[int, ...], h: int, w: int) -> tuple[int, ...]:
    return tuple(x - w for x in shape[h:] if x > w)


@lru_cache(maxsize=None)
def literal_iterate(shape: tuple[int, ...], a: int, b: int, t: int) -> tuple[int, ...]:
    out = shape
    for _ in range(t):
        out = literal_crop(out, a, b)
    return out


@lru_cache(maxsize=None)
def conjugate(shape: tuple[int, ...]) -> tuple[int, ...]:
    if not shape:
        return ()
    return tuple(sum(row >= j for row in shape) for j in range(1, shape[0] + 1))


def bounded_part_coeffs(bound: int, degree: int) -> tuple[int, ...]:
    """Coefficients of 1/(q;q)_bound through degree, via coin-change DP."""
    out = [0] * (degree + 1)
    out[0] = 1
    for part in range(1, bound + 1):
        for n in range(part, degree + 1):
            out[n] += out[n - part]
    return tuple(out)


BOUNDED = {
    r: bounded_part_coeffs(r, MAX_WEIGHT)
    for r in range(max(MAX_WEIGHT, 5) + 1)
}


def convolution(left: tuple[int, ...], right: tuple[int, ...], degree: int) -> int:
    return sum(left[j] * right[degree - j] for j in range(degree + 1))


def minimum_mass(mu: tuple[int, ...], h: int, w: int) -> int:
    assert mu
    return weight(mu) + h * (mu[0] + w) + w * len(mu)


@lru_cache(maxsize=None)
def empty_series_coeffs(h: int, w: int, degree: int) -> tuple[int, ...]:
    """Contract formula for E_{h,w}, computed coefficientwise."""
    out = [0] * (degree + 1)
    ph = BOUNDED[h]
    for k in range(w + 1):
        shift = k * (h + 1)
        pk = BOUNDED[k]
        for n in range(shift, degree + 1):
            out[n] += convolution(ph, pk, n - shift)
    return tuple(out)


def target_series_coeff(mu: tuple[int, ...], h: int, w: int, n: int) -> int:
    if not mu:
        return empty_series_coeffs(h, w, n)[n]
    excess = n - minimum_mass(mu, h, w)
    if excess < 0:
        return 0
    return convolution(BOUNDED[h], BOUNDED[w], excess)


def reconstruct(
    mu: tuple[int, ...], h: int, w: int,
    gamma: tuple[int, ...], beta: tuple[int, ...]
) -> tuple[int, ...]:
    assert mu
    assert len(gamma) <= h
    assert not beta or beta[0] <= w
    padded = gamma + (0,) * (h - len(gamma))
    top = tuple(mu[0] + w + g for g in padded)
    middle = tuple(x + w for x in mu)
    return top + middle + beta


def every_weight_witness(mu: tuple[int, ...], h: int, w: int, excess: int) -> tuple[int, ...]:
    """A correct source witness, including artificial h=0 or w=0 edges."""
    assert mu and excess >= 0
    if h > 0:
        gamma = () if excess == 0 else (excess,)
        beta = ()
    elif w > 0:
        gamma = ()
        beta = (1,) * excess
    else:
        assert excess == 0
        gamma = beta = ()
    return reconstruct(mu, h, w, gamma, beta)


def audit_iterates_clocks_heights_duality() -> None:
    for a, b in PARAMETERS:
        tau_by_shape: dict[tuple[int, ...], int] = {}
        for shape in ALL_PARTS:
            tau_direct = 0
            state = shape
            while state:
                state = literal_crop(state, a, b)
                tau_direct += 1
            tau_formula = min(
                t for t in range(MAX_WEIGHT + 2)
                if (shape[a * t] if a * t < len(shape) else 0) <= b * t
            )
            check(tau_direct == tau_formula,
                  f"tau a={a} b={b} shape={shape}")
            tau_by_shape[shape] = tau_direct
            for t in TIMES:
                direct = literal_iterate(shape, a, b, t)
                closed_cell = literal_crop(shape, a * t, b * t)
                closed_row = row_crop(shape, a * t, b * t)
                check(direct == closed_cell == closed_row,
                      f"iterate a={a} b={b} t={t} shape={shape}")
                survives = bool(direct)
                corner = len(shape) >= a * t + 1 and shape[a * t] >= b * t + 1
                check(survives == corner,
                      f"survival a={a} b={b} t={t} shape={shape}")
            left = conjugate(literal_crop(shape, a, b))
            right = literal_crop(conjugate(shape), b, a)
            check(left == right, f"duality a={a} b={b} shape={shape}")

        direct_height = 0
        for cap in range(MAX_WEIGHT + 1):
            direct_height = max(
                direct_height, max(tau_by_shape[shape] for shape in PARTS_BY_WEIGHT[cap])
            )
            formula_height = min(
                t for t in range(MAX_WEIGHT + 2)
                if (a * t + 1) * (b * t + 1) > cap
            )
            check(direct_height == formula_height,
                  f"height a={a} b={b} cap={cap}")


def audit_empty_fibres_shells_and_boundary_windows() -> None:
    for h, w in BOUNDARY_WINDOWS:
        expected = empty_series_coeffs(h, w, MAX_WEIGHT)
        for n, layer in enumerate(PARTS_BY_WEIGHT):
            actual = sum(literal_crop(shape, h, w) == () for shape in layer)
            check(actual == expected[n], f"empty h={h} w={w} n={n}")

    for a, b in PARAMETERS:
        previous = (0,) * (MAX_WEIGHT + 1)
        for t in TIMES:
            current = empty_series_coeffs(a * t, b * t, MAX_WEIGHT)
            for n, layer in enumerate(PARTS_BY_WEIGHT):
                absorbed = sum(not literal_iterate(shape, a, b, t) for shape in layer)
                check(absorbed == current[n],
                      f"absorbed a={a} b={b} t={t} n={n}")
                if t == 0:
                    direct_shell = sum(shape == () for shape in layer)
                else:
                    direct_shell = sum(
                        bool(literal_iterate(shape, a, b, t - 1))
                        and not literal_iterate(shape, a, b, t)
                        for shape in layer
                    )
                check(direct_shell == current[n] - previous[n],
                      f"shell a={a} b={b} t={t} n={n}")
            previous = current


def audit_all_fibres_mass_and_images() -> None:
    windows = set(BOUNDARY_WINDOWS)
    windows.update((a * t, b * t) for a, b in PARAMETERS for t in TIMES)
    for h, w in sorted(windows):
        counts_by_weight = tuple(
            Counter(literal_crop(shape, h, w) for shape in layer)
            for layer in PARTS_BY_WEIGHT
        )
        for mu in TARGETS:
            for n, counts_at_n in enumerate(counts_by_weight):
                actual = counts_at_n[mu]
                expected = target_series_coeff(mu, h, w, n)
                check(actual == expected,
                      f"fibre h={h} w={w} mu={mu} n={n}")

        for n, layer in enumerate(PARTS_BY_WEIGHT):
            # All target fibres, not merely those under MAX_TARGET_WEIGHT,
            # must recover the partition count at each source weight.
            image_counts = counts_by_weight[n]
            check(sum(image_counts.values()) == len(layer),
                  f"mass direct h={h} w={w} n={n}")
            rhs = empty_series_coeffs(h, w, n)[n]
            for mu in ALL_PARTS:
                if not mu:
                    continue
                m = minimum_mass(mu, h, w)
                if m > n:
                    continue
                rhs += convolution(BOUNDED[h], BOUNDED[w], n - m)
            check(rhs == len(layer), f"mass identity h={h} w={w} n={n}")

        for cap in range(MAX_WEIGHT + 1):
            actual_image = set().union(*(counts_by_weight[n] for n in range(cap + 1)))
            if h == 0 and w == 0:
                expected_image = {
                    shape for n in range(cap + 1) for shape in PARTS_BY_WEIGHT[n]
                }
            else:
                expected_image = {()}
                expected_image.update(
                    mu for mu in ALL_PARTS if mu and minimum_mass(mu, h, w) <= cap
                )
            check(actual_image == expected_image,
                  f"image h={h} w={w} cap={cap}")


def audit_every_weight_witnesses_and_probes() -> None:
    for h, w in BOUNDARY_WINDOWS:
        for mu in TARGETS:
            if not mu:
                continue
            max_excess = MAX_WEIGHT - minimum_mass(mu, h, w)
            if h == 0 and w == 0:
                max_excess = min(max_excess, 0)
            for excess in range(max_excess + 1):
                source = every_weight_witness(mu, h, w, excess)
                check(literal_crop(source, h, w) == mu,
                      f"witness image h={h} w={w} mu={mu} d={excess}")
                check(weight(source) == minimum_mass(mu, h, w) + excess,
                      f"witness weight h={h} w={w} mu={mu} d={excess}")

    for a in range(1, 8):
        for b in range(1, 8):
            m_cell = minimum_mass((1,), a, b)
            m_row = minimum_mass((2,), a, b)
            m_col = minimum_mass((1, 1), a, b)
            check(m_cell == (a + 1) * (b + 1), f"cell probe a={a} b={b}")
            check(m_row - m_cell - 1 == a, f"row probe a={a} b={b}")
            check(m_col - m_cell - 1 == b, f"column probe a={a} b={b}")


def audit_worked_example_and_t0_n0() -> None:
    mu = (3, 1)
    h, w = 4, 2
    check(minimum_mass(mu, h, w) == 28, "worked threshold")
    got = tuple(target_series_coeff(mu, h, w, n) for n in range(28, 33))
    check(got == (1, 2, 5, 9, 17), f"worked coefficients {got}")
    direct = tuple(
        sum(literal_crop(shape, h, w) == mu for shape in PARTS_BY_WEIGHT[n])
        for n in range(28, 31)
    )
    check(direct == (1, 2, 5), f"worked direct {direct}")

    check(literal_crop((), 0, 0) == (), "t=0 empty identity")
    for mu0 in TARGETS:
        check(literal_crop(mu0, 0, 0) == mu0, f"t=0 identity mu={mu0}")
    check(empty_series_coeffs(0, 0, 0) == (1,), "E00")
    check(min(t for t in range(2) if (2 * t + 1) * (3 * t + 1) > 0) == 0,
          "N=0 height")


def main() -> None:
    audit_iterates_clocks_heights_duality()
    audit_empty_fibres_shells_and_boundary_windows()
    audit_all_fibres_mass_and_images()
    audit_every_weight_witnesses_and_probes()
    audit_worked_example_and_t0_n0()
    print("P160 RCS HOSTILE REVIEW A: PASS")
    print(f"assertions={checks}")
    print(f"source_weight_max={MAX_WEIGHT}")
    print(f"target_weight_max={MAX_TARGET_WEIGHT}")
    print(f"parameter_pairs={len(PARAMETERS)}")
    print(f"times={TIMES[0]}..{TIMES[-1]}")
    print(f"boundary_windows={BOUNDARY_WINDOWS}")
    print("author_code_imported=no")


if __name__ == "__main__":
    main()
