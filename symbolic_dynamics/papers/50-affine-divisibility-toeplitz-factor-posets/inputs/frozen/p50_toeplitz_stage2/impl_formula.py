#!/usr/bin/env python3
"""Direct-formula implementation for the frozen p-divisibility Toeplitz family.

This module intentionally uses the affine expression (p-1)k+1.  The second
implementation in impl_holefill.py uses nested hole filling instead and does
not import this module.
"""

from __future__ import annotations

from itertools import product
from math import gcd, lcm


def _check_p(p: int) -> None:
    if not isinstance(p, int) or p < 3:
        raise ValueError("p must be an integer >= 3")


def divexp(p: int, n: int) -> int:
    """Return max e >= 0 with p**e dividing nonzero n."""
    _check_p(p)
    if n == 0:
        raise ValueError("the p-divisibility exponent is undefined at zero")
    n = abs(n)
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def affine(p: int, k: int) -> int:
    _check_p(p)
    return (p - 1) * k + 1


def value(p: int, directive: tuple[int, ...], k: int) -> int:
    if not directive:
        raise ValueError("directive must be nonempty")
    return directive[divexp(p, affine(p, k)) % len(directive)]


def hole_residue(p: int, n: int) -> int:
    _check_p(p)
    if n < 0:
        raise ValueError("n must be nonnegative")
    return (p**n - 1) // (p - 1)


def least_period(word: tuple[int, ...]) -> int:
    if not word:
        raise ValueError("word must be nonempty")
    length = len(word)
    for d in range(1, length + 1):
        if length % d == 0 and all(word[i] == word[i % d] for i in range(length)):
            return d
    raise AssertionError("unreachable")


def canonicalize(word: tuple[int, ...]) -> tuple[int, ...]:
    relabel: dict[int, int] = {}
    out: list[int] = []
    for letter in word:
        if letter not in relabel:
            relabel[letter] = len(relabel)
        out.append(relabel[letter])
    return tuple(out)


def is_frozen_directive(word: tuple[int, ...]) -> bool:
    if len(word) < 2 or least_period(word) != len(word):
        return False
    if set(word) != set(range(max(word) + 1)):
        return False
    return all(word[i] != word[(i + 1) % len(word)] for i in range(len(word)))


def enumerate_directives(max_period: int, max_alphabet: int) -> list[tuple[int, ...]]:
    """Product-based canonical enumeration, independent of impl_holefill."""
    out: set[tuple[int, ...]] = set()
    for length in range(2, max_period + 1):
        for alphabet_size in range(2, min(max_alphabet, length) + 1):
            for raw in product(range(alphabet_size), repeat=length):
                if raw[0] != 0 or canonicalize(raw) != raw:
                    continue
                if max(raw) + 1 != alphabet_size:
                    continue
                if is_frozen_directive(raw):
                    out.add(raw)
    return sorted(out, key=lambda w: (len(w), max(w) + 1, w))


def adjacency_edges(directive: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    edges = {
        tuple(sorted((directive[i], directive[(i + 1) % len(directive)])))
        for i in range(len(directive))
    }
    return tuple(sorted(edges))


def enumerate_partitions(n: int) -> list[tuple[int, ...]]:
    """Enumerate set partitions by filtering all canonical label strings."""
    if n <= 0:
        raise ValueError("n must be positive")
    out: set[tuple[int, ...]] = set()
    for raw in product(range(n), repeat=n):
        if raw[0] == 0 and canonicalize(raw) == raw:
            out.add(raw)
    return sorted(out, key=lambda r: (max(r) + 1, r))


def partition_is_admissible(
    directive: tuple[int, ...], partition: tuple[int, ...]
) -> bool:
    if len(partition) != max(directive) + 1:
        return False
    return all(
        partition[directive[i]] != partition[directive[(i + 1) % len(directive)]]
        for i in range(len(directive))
    )


def graphical_stirling_counts(directive: tuple[int, ...]) -> dict[int, int]:
    counts: dict[int, int] = {}
    for partition in enumerate_partitions(max(directive) + 1):
        if partition_is_admissible(directive, partition):
            k = max(partition) + 1
            counts[k] = counts.get(k, 0) + 1
    return dict(sorted(counts.items()))


def proper_coloring_count(directive: tuple[int, ...], colors: int) -> int:
    """Count labeled proper colorings by a direct Cartesian-product scan."""
    if colors < 0:
        raise ValueError("colors must be nonnegative")
    vertices = max(directive) + 1
    edges = adjacency_edges(directive)
    return sum(
        all(coloring[a] != coloring[b] for a, b in edges)
        for coloring in product(range(colors), repeat=vertices)
    )


def quotient_directive(
    directive: tuple[int, ...], partition: tuple[int, ...]
) -> tuple[int, ...]:
    quotient = canonicalize(tuple(partition[a] for a in directive))
    return quotient[: least_period(quotient)]


def center_window(
    p: int, directive: tuple[int, ...], n: int, radius: int
) -> tuple[int, ...]:
    center = hole_residue(p, n)
    return tuple(value(p, directive, center + j) for j in range(-radius, radius + 1))


def center_lemma_holds(p: int, j: int, n: int) -> bool:
    if j == 0:
        raise ValueError("j must be nonzero")
    if n <= divexp(p, j):
        raise ValueError("n must exceed divexp(p,j)")
    return divexp(p, p**n + (p - 1) * j) == divexp(p, j)


def skeleton_certificate(p: int, directive: tuple[int, ...], n: int) -> dict:
    """Return exact and sampled evidence for the p**n skeleton."""
    if n < 1:
        raise ValueError("n must be >= 1")
    modulus = p**n
    hole = hole_residue(p, n)
    periodic_residues = 0
    sampled_equalities = 0
    for a in range(modulus):
        if a == hole:
            continue
        e = divexp(p, affine(p, a))
        if e >= n:
            raise AssertionError("non-hole residue has exponent >= n")
        periodic_residues += 1
        for t in range(-3, 4):
            if value(p, directive, a + t * modulus) != value(p, directive, a):
                raise AssertionError("predicted periodic residue changed")
            sampled_equalities += 1
    q0 = affine(p, hole) // modulus
    inv = pow(p - 1, -1, p * p)
    m0 = ((1 - q0) * inv) % (p * p)
    m1 = ((p - q0) * inv) % (p * p)
    e0 = divexp(p, affine(p, hole + m0 * modulus))
    e1 = divexp(p, affine(p, hole + m1 * modulus))
    if (e0, e1) != (n, n + 1):
        raise AssertionError("hole witnesses have wrong exponents")
    if directive[e0 % len(directive)] == directive[e1 % len(directive)]:
        raise AssertionError("cyclic-neighbor inequality was not enforced")
    return {
        "N": n,
        "hole_residue": hole,
        "modulus": modulus,
        "periodic_residue_count": periodic_residues,
        "sampled_periodic_equalities": sampled_equalities,
        "hole_witness_multipliers": [m0, m1],
        "hole_witness_exponents": [e0, e1],
    }


def prime_smaller_period_witness(
    p: int, directive: tuple[int, ...], n: int, q: int
) -> dict:
    """Witness that q < p**(n+1) is not a common period of B_n for prime p."""
    if q <= 0 or q >= p ** (n + 1):
        raise ValueError("q must satisfy 0 < q < p**(n+1)")
    j = divexp(p, q)
    if j > n:
        raise AssertionError("q bound should force j <= n")
    d = q // (p**j)
    if gcd(d, p) != 1:
        raise ValueError("this certificate requires prime p")
    t = ((p - 1) * pow((p - 1) * d, -1, p * p)) % (p * p)
    center = hole_residue(p, j)
    before = divexp(p, affine(p, center))
    after = divexp(p, affine(p, center + t * q))
    if (before, after) != (j, j + 1):
        raise AssertionError("prime rejection witness failed")
    if value(p, directive, center) == value(p, directive, center + t * q):
        raise AssertionError("prime rejection witness did not change the letter")
    return {"q": q, "level": j, "multiplier": t, "center": center}


def block_common_period_sample(
    p: int,
    directive: tuple[int, ...],
    n: int,
    q: int,
    t_min: int,
    t_max: int,
) -> int:
    comparisons = 0
    for k in range(p**n):
        expected = value(p, directive, k)
        for t in range(t_min, t_max + 1):
            if value(p, directive, k + t * q) != expected:
                raise AssertionError((p, n, q, k, t))
            comparisons += 1
    return comparisons


def sample_positions(p: int, radius: int, dense_radius: int, center_depth: int) -> list[int]:
    positions = set(range(-dense_radius, dense_radius + 1))
    positions.update(hole_residue(p, n) for n in range(center_depth + 1))
    return sorted(positions)


def local_constraint(
    p: int,
    source: tuple[int, ...],
    target: tuple[int, ...],
    radius: int,
    dense_radius: int,
    center_depth: int,
) -> dict:
    table: dict[tuple[int, ...], int] = {}
    conflict = False
    for k in sample_positions(p, radius, dense_radius, center_depth):
        window = tuple(value(p, source, k + j) for j in range(-radius, radius + 1))
        out = value(p, target, k)
        if window in table and table[window] != out:
            conflict = True
            break
        table[window] = out

    letter_map: dict[int, int] = {}
    quotient = True
    for n in range(lcm(len(source), len(target))):
        a, b = source[n % len(source)], target[n % len(target)]
        if a in letter_map and letter_map[a] != b:
            quotient = False
            break
        letter_map[a] = b
    if quotient:
        quotient = (
            set(letter_map) == set(source)
            and set(letter_map.values()) == set(target)
            and all(target[n % len(target)] == letter_map[source[n % len(source)]]
                    for n in range(lcm(len(source), len(target))))
        )
    return {
        "consistent": not conflict,
        "is_surjective_letter_quotient": quotient,
        "observed_window_count": len(table),
    }
