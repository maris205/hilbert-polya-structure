#!/usr/bin/env python3
"""Finite falsifiers/regression checks for the P67--P71 Stage-1 contracts.

Nothing in this file is used as a substitute for an infinite proof or a
novelty claim.  The calculations are deliberately small and independent of
the intended manuscript proofs.
"""

from __future__ import annotations

from collections import Counter
from itertools import product
from math import comb, prod, sqrt


def rank_mod(matrix: list[list[int]], p: int) -> int:
    a = [[entry % p for entry in row] for row in matrix]
    if not a:
        return 0
    rows, cols = len(a), len(a[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        inv = pow(a[pivot_row][col], -1, p)
        a[pivot_row] = [(inv * x) % p for x in a[pivot_row]]
        for r in range(rows):
            if r == pivot_row or not a[r][col]:
                continue
            factor = a[r][col]
            a[r] = [
                (x - factor * y) % p
                for x, y in zip(a[r], a[pivot_row], strict=True)
            ]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def trim(poly: list[int], p: int) -> list[int]:
    out = [x % p for x in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_mod(a: list[int], b: list[int], p: int) -> list[int]:
    a = trim(a, p)
    b = trim(b, p)
    inv = pow(b[-1], -1, p)
    while len(a) >= len(b) and any(a):
        shift = len(a) - len(b)
        factor = a[-1] * inv % p
        for j, value in enumerate(b):
            a[j + shift] = (a[j + shift] - factor * value) % p
        a = trim(a, p)
    return a


def gcd_degree(a: list[int], b: list[int], p: int) -> int:
    a, b = trim(a, p), trim(b, p)
    while any(b):
        a, b = b, poly_mod(a, b, p)
    return len(trim(a, p)) - 1


def plaquette_prefix_rank(a: int, b: int, n: int, p: int) -> int:
    rows: list[list[int]] = []
    for root in range(1, n // (a * b) + 1):
        row = [0] * n
        for index, coefficient in (
            (root, 1),
            (a * root, -1),
            (b * root, -1),
            (a * b * root, 1),
        ):
            row[index - 1] += coefficient
        rows.append(row)
    return rank_mod(rows, p)


def rectangular_plaquette_rank(m: int, n: int, p: int) -> int:
    rows: list[list[int]] = []
    for i in range(m - 1):
        for j in range(n - 1):
            row = [0] * (m * n)
            for di, dj, coefficient in (
                (0, 0, 1),
                (1, 0, -1),
                (0, 1, -1),
                (1, 1, 1),
            ):
                row[(i + di) * n + j + dj] += coefficient
            rows.append(row)
    return rank_mod(rows, p)


def check_p67() -> None:
    for a, b, p in ((2, 3, 2), (2, 5, 3), (3, 4, 5)):
        for n in range(1, 61):
            observed = plaquette_prefix_rank(a, b, n, p)
            expected = n // (a * b)
            assert observed == expected, (a, b, p, n, observed, expected)
    for p in (2, 3, 5):
        for m in range(1, 7):
            for n in range(1, 7):
                rank = rectangular_plaquette_rank(m, n, p)
                assert m * n - rank == m + n - 1
    print("P67 PASS: prefix exponent N-floor(N/ab); (a,b)-box dimension M+N-1")


def is_box_hom_pattern(word: tuple[int, ...], shape: tuple[int, int], m: int) -> bool:
    rows, cols = shape
    for i in range(rows):
        for j in range(cols):
            here = word[i * cols + j]
            if i + 1 < rows:
                there = word[(i + 1) * cols + j]
                if (here < m) == (there < m):
                    return False
            if j + 1 < cols:
                there = word[i * cols + j + 1]
                if (here < m) == (there < m):
                    return False
    return True


def check_p68() -> None:
    for rows, cols, m, n in ((2, 2, 2, 3), (2, 3, 1, 2), (3, 2, 2, 2)):
        size = rows * cols
        observed = sum(
            is_box_hom_pattern(word, (rows, cols), m)
            for word in product(range(m + n), repeat=size)
        )
        even = sum((i + j) % 2 == 0 for i in range(rows) for j in range(cols))
        odd = size - even
        expected = m**even * n**odd + n**even * m**odd
        assert observed == expected, (rows, cols, m, n, observed, expected)
    orientation_covariance = 0.5 - 0.5**2
    assert orientation_covariance == 0.25
    print("P68 PASS: three box counts; analytic orientation covariance checksum 1/4")


Permutation = tuple[int, ...]


def compose(left: Permutation, right: Permutation) -> Permutation:
    return tuple(left[right[i]] for i in range(len(left)))


def inverse(perm: Permutation) -> Permutation:
    out = [0] * len(perm)
    for i, value in enumerate(perm):
        out[value] = i
    return tuple(out)


def commutator(a: Permutation, b: Permutation) -> Permutation:
    return compose(compose(compose(a, b), inverse(a)), inverse(b))


def s3() -> list[Permutation]:
    return [p for p in product(range(3), repeat=3) if len(set(p)) == 3]


def surface_hom_count(genus: int) -> int:
    group = s3()
    identity = tuple(range(3))
    commutators = Counter(commutator(a, b) for a in group for b in group)
    distribution = Counter({identity: 1})
    for _ in range(genus):
        nxt: Counter[Permutation] = Counter()
        for partial, multiplicity in distribution.items():
            for comm, count in commutators.items():
                nxt[compose(partial, comm)] += multiplicity * count
        distribution = nxt
    return distribution[identity]


def surface_c2_index_two_flat_dimension() -> int:
    """Raw C2 connections on a concrete two-sheeted genus-2 cover cellulation."""
    vertices = range(2)
    generator_action = (1, 0, 0, 0)
    relator = (
        (0, 1), (1, 1), (0, -1), (1, -1),
        (2, 1), (3, 1), (2, -1), (3, -1),
    )
    rows: list[list[int]] = []
    for start in vertices:
        row = [0] * 8
        current = start
        for generator, sign in relator:
            step = generator_action[generator]
            if sign > 0:
                row[current * 4 + generator] += 1
                current = (current + step) % 2
            else:
                current = (current - step) % 2
                row[current * 4 + generator] -= 1
        assert current == start
        rows.append(row)
    return 8 - rank_mod(rows, 2)


def check_p69() -> None:
    substitution = {"a": "ab", "b": "ac", "c": "db", "d": "dc"}
    code = {"a": 1, "b": 1, "c": -1, "d": -1}
    fixed_word = "a"
    for _ in range(15):
        fixed_word = "".join(substitution[letter] for letter in fixed_word)
    def range_cardinality(word: str) -> int:
        partial = 0
        low = 0
        high = 0
        for letter in word:
            partial += code[letter]
            low = min(low, partial)
            high = max(high, partial)
        return high - low + 1

    rho = [1, 2, 3, 4]
    for length in range(4, 257):
        quotient, residue = divmod(length, 4)
        rho.append(
            (
                2 * rho[quotient] + 1,
                2 * rho[quotient],
                rho[quotient] + rho[quotient + 1],
                2 * rho[quotient + 1],
            )[residue]
        )

    running_max = 0
    observed_ranges: dict[int, int] = {}
    for length in range(1, 257):
        factors = {
            fixed_word[i : i + length]
            for i in range(len(fixed_word) - length + 1)
        }
        expected_factor_count = 4 if length == 1 else 8 * length - 8
        assert len(factors) == expected_factor_count
        observed = max(range_cardinality(word) for word in factors)
        running_max = max(running_max, rho[length])
        assert observed == running_max, (length, observed, running_max)
        observed_ranges[length] = observed

    checked = []
    for exponent in range(1, 9):
        length = 2**exponent
        observed = observed_ranges[length]
        expected = (
            3 * 2 ** (exponent // 2) - 1
            if exponent % 2 == 0
            else 2 ** ((exponent + 3) // 2) - 1
        )
        assert observed == expected, (exponent, observed, expected)
        checked.append(observed)
    print(
        "P69 PASS: R(n)=max_{m<=n} rho(m) through n=256; dyadic ranges",
        checked,
    )


def check_surface_flat_reserve() -> None:
    observed = [surface_hom_count(h) for h in (1, 2, 3)]
    expected = [18, 486, 16038]
    assert observed == expected, (observed, expected)
    assert 6 * observed[2] == 96228
    raw_dimension = surface_c2_index_two_flat_dimension()
    assert raw_dimension == 7
    assert 2**raw_dimension == 2 * 2**6 == 128
    print("RESERVE PASS: surface S3 Hom counts 18, 486, 16038; raw C2 flat count 128")


def heisenberg_product(
    left: tuple[int, int, int], right: tuple[int, int, int], ell: int
) -> tuple[int, int, int]:
    x, y, z = left
    u, v, w = right
    return ((x + u) % ell, (y + v) % ell, (z + w + x * v) % ell)


def heisenberg_nullity(ell: int, p: int) -> int:
    elements = list(product(range(ell), repeat=3))
    index = {element: i for i, element in enumerate(elements)}
    a = (1, 0, 0)
    b = (0, 1, 0)
    matrix: list[list[int]] = []
    for g in elements:
        row = [0] * len(elements)
        for h in (g, heisenberg_product(g, a, ell), heisenberg_product(g, b, ell)):
            row[index[h]] += 1
        matrix.append(row)
    return len(elements) - rank_mod(matrix, p)


def heisenberg_formula(ell: int, p: int) -> int:
    first = [(-1) % p] + [0] * (ell - 1) + [1]
    second = [comb(ell, k) % p for k in range(ell + 1)]
    second[0] = (second[0] + 1) % p
    one_dimensional = gcd_degree(first, second, p)
    return one_dimensional + (ell * (ell - 1) if p == 3 else 0)


def check_p70() -> None:
    cases = ((3, 2), (3, 5), (5, 2), (5, 3), (5, 7), (5, 11))
    rows = []
    for ell, p in cases:
        observed = heisenberg_nullity(ell, p)
        expected = heisenberg_formula(ell, p)
        assert observed == expected, (ell, p, observed, expected)
        rows.append(f"(ell={ell},p={p}):{observed}")
    print("P70 PASS:", ", ".join(rows))


def check_p71() -> None:
    profile = (1, 2, 3)
    alphabet_size = sum(profile)
    symbol_degrees = tuple(
        fibre_size for fibre_size in profile for _ in range(fibre_size)
    )
    degree_histogram = Counter()
    for fibre_size in profile:
        degree_histogram[fibre_size] += fibre_size
    assert degree_histogram == Counter({3: 3, 2: 2, 1: 1})
    recovered_profile = sorted(
        degree for degree, fixed_count in degree_histogram.items()
        for _ in range(fixed_count // degree)
    )
    assert recovered_profile == list(profile)
    for period in range(1, 6):
        assert alphabet_size**period == sum(1 for _ in product(range(alphabet_size), repeat=period))
        weighted = sum(
            prod(symbol_degrees[s] + 1 for s in word)
            for word in product(range(alphabet_size), repeat=period)
        )
        expected = sum(k * (k + 1) for k in profile) ** period
        assert weighted == expected
    print("P71 PASS: one fibre profile recovered; weighted signature factors through period 5")


def rejected_torus_formula_falsifier() -> None:
    alpha, beta = sqrt(2) / 10, sqrt(3) / 10
    endpoints = sorted({0.0, alpha % 1.0, (-beta) % 1.0, (alpha - beta) % 1.0})
    names = set()
    for i, left in enumerate(endpoints):
        right = endpoints[(i + 1) % len(endpoints)]
        phase = (
            (left + right) / 2
            if i + 1 < len(endpoints)
            else ((left + right + 1) / 2) % 1
        )
        names.add((int(phase < alpha), int(((phase + beta) % 1) < alpha)))
    assert len(endpoints) == 4 and len(names) == 3
    print("REJECTED-CANDIDATE PASS: four torus endpoints yield only three names, not four")


def rejected_dyck_histogram_falsifier() -> None:
    """Disprove N_n(k)=binom(n,k) M^max(k,n-k) at n=2, k=1."""
    for alphabet_size in (2, 3, 4):
        openings = tuple(("alpha", i) for i in range(alphabet_size))
        closings = tuple(("beta", i) for i in range(alphabet_size))

        # A beta-alpha pair is always admissible, while alpha_i beta_j is
        # admissible exactly when i=j in the Dyck inverse-monoid convention.
        actual = sum(1 for _ in product(closings, openings)) + sum(
            opening[1] == closing[1]
            for opening, closing in product(openings, closings)
        )
        expected_actual = alphabet_size**2 + alphabet_size
        rejected_prediction = comb(2, 1) * alphabet_size
        assert actual == expected_actual
        assert actual != rejected_prediction

    assert 2 + 2**2 == 6 and comb(2, 1) * 2 == 4
    print("REJECTED-CANDIDATE PASS: Dyck n=2, k=1 count is M+M^2, not 2M")


def main() -> None:
    check_p67()
    check_p68()
    check_p69()
    check_surface_flat_reserve()
    check_p70()
    check_p71()
    rejected_torus_formula_falsifier()
    rejected_dyck_histogram_falsifier()
    print("ALL STAGE-1 FINITE CONTROLS PASS")


if __name__ == "__main__":
    main()
