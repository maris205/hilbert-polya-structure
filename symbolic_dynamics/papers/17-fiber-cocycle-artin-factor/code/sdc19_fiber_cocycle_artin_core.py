"""Exact certificates for SD-C19, the tensor-subset C2 parity extension.

This module deliberately uses only integers, fractions, sparse formal
polynomials, and SymPy's exact polynomial matrices.  It contains no target-zero
data and no floating-point fitting.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import product
from math import comb, gcd
import json
import random
from typing import Callable, Iterable, Iterator

import sympy as sp


Exponent = tuple[int, ...]
Poly = dict[Exponent, Fraction]


def epsilon(cardinality: int) -> int:
    return 1 if cardinality % 2 else -1


def _clean(poly: dict[Exponent, Fraction]) -> Poly:
    return {e: Fraction(c) for e, c in poly.items() if c}


def poly_const(nvars: int, value: int | Fraction = 1) -> Poly:
    value = Fraction(value)
    return {(0,) * nvars: value} if value else {}


def poly_add(left: Poly, right: Poly, right_scale: int | Fraction = 1) -> Poly:
    out: defaultdict[Exponent, Fraction] = defaultdict(Fraction)
    out.update(left)
    scale = Fraction(right_scale)
    for exponent, coefficient in right.items():
        out[exponent] += scale * coefficient
    return _clean(out)


def poly_scale(poly: Poly, scale: int | Fraction) -> Poly:
    scale = Fraction(scale)
    return _clean({e: scale * c for e, c in poly.items()})


def poly_mul(left: Poly, right: Poly) -> Poly:
    if not left or not right:
        return {}
    out: defaultdict[Exponent, Fraction] = defaultdict(Fraction)
    for le, lc in left.items():
        for re, rc in right.items():
            out[tuple(a + b for a, b in zip(le, re))] += lc * rc
    return _clean(out)


def poly_product_atom_factors(nvars: int, sign: int, atom_power: int = 1) -> Poly:
    """Return product_i (1 + sign*x_i**atom_power)."""
    out = poly_const(nvars)
    for index in range(nvars):
        exponent = [0] * nvars
        exponent[index] = atom_power
        out = poly_mul(
            out,
            {
                (0,) * nvars: Fraction(1),
                tuple(exponent): Fraction(sign),
            },
        )
    return out


def poly_digest(poly: Poly) -> str:
    payload = [
        [list(e), c.numerator, c.denominator]
        for e, c in sorted(poly.items())
    ]
    return sha256(json.dumps(payload, separators=(",", ":")).encode()).hexdigest()


def formal_c2_certificate(nvars: int) -> dict[str, object]:
    """Build the full subset transfer and exact 2x2 regular determinant."""
    zero = (0,) * nvars
    b_plus: Poly = {}
    b_minus: Poly = {}
    b_even: Poly = {}
    b_odd: Poly = {}

    for mask in range(1, 1 << nvars):
        exponent = tuple((mask >> i) & 1 for i in range(nvars))
        cardinality = mask.bit_count()
        scalar = Fraction(epsilon(cardinality))
        b_plus[exponent] = scalar
        b_minus[exponent] = scalar * ((-1) ** cardinality)
        target = b_even if cardinality % 2 == 0 else b_odd
        target[exponent] = scalar

    one = {zero: Fraction(1)}
    d_plus = poly_add(one, b_plus, -1)
    d_minus = poly_add(one, b_minus, -1)

    # I-B_reg = [[1-B_even, -B_odd],[-B_odd,1-B_even]].
    diagonal = poly_add(one, b_even, -1)
    off_diagonal = poly_scale(b_odd, -1)
    d_regular = poly_add(
        poly_mul(diagonal, diagonal),
        poly_mul(off_diagonal, off_diagonal),
        -1,
    )

    expected_plus = poly_product_atom_factors(nvars, -1)
    expected_minus = poly_product_atom_factors(nvars, +1)
    expected_regular = poly_product_atom_factors(nvars, -1, atom_power=2)
    block_product = poly_mul(d_plus, d_minus)

    return {
        "n_atoms": nvars,
        "alphabet_size": (1 << nvars) - 1,
        "d_plus_terms": len(d_plus),
        "d_minus_terms": len(d_minus),
        "d_regular_terms": len(d_regular),
        "d_plus_mismatch_terms": len(poly_add(d_plus, expected_plus, -1)),
        "d_minus_mismatch_terms": len(poly_add(d_minus, expected_minus, -1)),
        "d_regular_mismatch_terms": len(poly_add(d_regular, expected_regular, -1)),
        "same_object_block_mismatch_terms": len(poly_add(d_regular, block_product, -1)),
        "d_plus_sha256": poly_digest(d_plus),
        "d_minus_sha256": poly_digest(d_minus),
        "d_regular_sha256": poly_digest(d_regular),
    }


def c2_transitivity_certificate(n_atoms: int) -> dict[str, object]:
    """Exact two-state adjacency count for the parity extension."""
    odd_edges = sum(comb(n_atoms, degree) for degree in range(1, n_atoms + 1, 2))
    even_edges = sum(comb(n_atoms, degree) for degree in range(2, n_atoms + 1, 2))
    strongly_connected = odd_edges > 0
    mixing = strongly_connected and even_edges > 0
    return {
        "n_atoms": n_atoms,
        "fiber_adjacency": f"[[{even_edges},{odd_edges}],[{odd_edges},{even_edges}]]",
        "odd_fiber_changing_edges": odd_edges,
        "even_fiber_preserving_edges": even_edges,
        "topologically_transitive": strongly_connected,
        "mixing": mixing,
        "period": 1 if mixing else 2,
    }


def series_add(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    size = max(len(left), len(right))
    return [
        (left[i] if i < len(left) else Fraction(0))
        + (right[i] if i < len(right) else Fraction(0))
        for i in range(size)
    ]


def series_scale(series: list[Fraction], scale: int | Fraction) -> list[Fraction]:
    scale = Fraction(scale)
    return [scale * coefficient for coefficient in series]


def series_mul(
    left: list[Fraction], right: list[Fraction], max_degree: int
) -> list[Fraction]:
    out = [Fraction(0) for _ in range(max_degree + 1)]
    for i, lc in enumerate(left):
        if not lc or i > max_degree:
            continue
        for j, rc in enumerate(right):
            if i + j > max_degree:
                break
            if rc:
                out[i + j] += lc * rc
    return out


def series_power(series: list[Fraction], power_: int, max_degree: int) -> list[Fraction]:
    out = [Fraction(1)] + [Fraction(0)] * max_degree
    base = list(series[: max_degree + 1])
    exponent = power_
    while exponent:
        if exponent & 1:
            out = series_mul(out, base, max_degree)
        exponent //= 2
        if exponent:
            base = series_mul(base, base, max_degree)
    return out


def trace_log_sum(b_series: list[Fraction], max_degree: int) -> list[Fraction]:
    """Return sum_{r>=1} B(t)^r/r through max_degree."""
    out = [Fraction(0)] * (max_degree + 1)
    current = [Fraction(1)] + [Fraction(0)] * max_degree
    for repetition in range(1, max_degree + 1):
        current = series_mul(current, b_series, max_degree)
        out = series_add(out, series_scale(current, Fraction(1, repetition)))
    return out[: max_degree + 1]


def collapsed_character_series(n_atoms: int, sign_character: bool, max_degree: int) -> list[Fraction]:
    """B_chi after setting every atom variable to the same formal t."""
    out = [Fraction(0)] * (max_degree + 1)
    for degree in range(1, min(n_atoms, max_degree) + 1):
        coefficient = epsilon(degree) * comb(n_atoms, degree)
        if sign_character:
            coefficient *= (-1) ** degree
        out[degree] = Fraction(coefficient)
    return out


def repetition_ledger(n_atoms: int, max_degree: int = 10) -> list[dict[str, object]]:
    b_plus = collapsed_character_series(n_atoms, False, max_degree)
    b_minus = collapsed_character_series(n_atoms, True, max_degree)
    plus_trace = trace_log_sum(b_plus, max_degree)
    minus_trace = trace_log_sum(b_minus, max_degree)
    regular_trace = series_add(plus_trace, minus_trace)

    rows: list[dict[str, object]] = []
    for degree in range(1, max_degree + 1):
        plus_closed = Fraction(n_atoms, degree)
        minus_closed = Fraction(n_atoms * ((-1) ** degree), degree)
        if degree % 2:
            regular_closed = Fraction(0)
        else:
            regular_closed = Fraction(2 * n_atoms, degree)
        for block, actual, expected in (
            ("trivial_character", plus_trace[degree], plus_closed),
            ("sign_character", minus_trace[degree], minus_closed),
            ("regular_whole_extension", regular_trace[degree], regular_closed),
        ):
            rows.append(
                {
                    "n_atoms": n_atoms,
                    "formal_degree": degree,
                    "block": block,
                    "trace_repetition_coefficient": str(actual),
                    "closed_factor_coefficient": str(expected),
                    "exact_match": actual == expected,
                }
            )
    return rows


def _int_poly_mul(left: dict[int, int], right: dict[int, int]) -> dict[int, int]:
    out: defaultdict[int, int] = defaultdict(int)
    for i, lc in left.items():
        for j, rc in right.items():
            out[i + j] += lc * rc
    return {degree: count for degree, count in out.items() if count}


def _int_poly_power(base: dict[int, int], exponent: int) -> dict[int, int]:
    out = {0: 1}
    current = dict(base)
    while exponent:
        if exponent & 1:
            out = _int_poly_mul(out, current)
        exponent //= 2
        if exponent:
            current = _int_poly_mul(current, current)
    return out


def proper_divisors(number: int) -> list[int]:
    return [d for d in range(1, number) if number % d == 0]


@lru_cache(maxsize=None)
def primitive_word_degree_counts(n_atoms: int, word_length: int) -> tuple[tuple[int, int], ...]:
    """Exact primitive *words* by total subset degree."""
    alphabet = {degree: comb(n_atoms, degree) for degree in range(1, n_atoms + 1)}
    all_words = _int_poly_power(alphabet, word_length)
    primitive = dict(all_words)
    for shorter in proper_divisors(word_length):
        repeats = word_length // shorter
        for base_degree, count in primitive_word_degree_counts(n_atoms, shorter):
            primitive[repeats * base_degree] -= count
    primitive = {degree: count for degree, count in primitive.items() if count}
    if any(count < 0 for count in primitive.values()):
        raise AssertionError("negative primitive word count")
    return tuple(sorted(primitive.items()))


def primitive_necklace_degree_counts(n_atoms: int, word_length: int) -> dict[int, int]:
    out: dict[int, int] = {}
    for degree, word_count in primitive_word_degree_counts(n_atoms, word_length):
        quotient, remainder = divmod(word_count, word_length)
        if remainder:
            raise AssertionError("primitive word count not divisible by rotation length")
        out[degree] = quotient
    return out


def primitive_census_row(n_atoms: int, word_length: int, group_order: int) -> dict[str, object]:
    by_degree = primitive_necklace_degree_counts(n_atoms, word_length)
    total = sum(by_degree.values())
    total_mixed = total - (n_atoms if word_length == 1 else 0)
    closes_once = sum(count for degree, count in by_degree.items() if degree % group_order == 0)
    closes_once_mixed = closes_once
    q_distribution: defaultdict[int, int] = defaultdict(int)
    lifted_cycles = 0
    for degree, count in by_degree.items():
        q = group_order // gcd(group_order, degree)
        q_distribution[q] += count
        lifted_cycles += gcd(group_order, degree) * count
    return {
        "n_atoms": n_atoms,
        "base_word_length": word_length,
        "group_order": group_order,
        "base_primitive_necklaces": total,
        "mixed_base_primitive_necklaces": total_mixed,
        "base_necklaces_closing_after_one_traversal": closes_once,
        "mixed_members_closing_after_one_traversal": closes_once_mixed,
        "lifted_primitive_cycles_total": lifted_cycles,
        "base_necklace_q_distribution_json": json.dumps(
            dict(sorted(q_distribution.items())), sort_keys=True
        ),
        "degree_distribution_sha256": sha256(
            json.dumps(sorted(by_degree.items()), separators=(",", ":")).encode()
        ).hexdigest(),
    }


def _least_rotation(word: tuple[int, ...]) -> tuple[int, ...]:
    return min(word[index:] + word[:index] for index in range(len(word)))


def brute_primitive_necklace_degree_counts(n_atoms: int, word_length: int) -> dict[int, int]:
    """Small test oracle; never used for the production n=5,r=10 census."""
    alphabet = tuple(range(1, 1 << n_atoms))
    counts: defaultdict[int, int] = defaultdict(int)
    for word in product(alphabet, repeat=word_length):
        if word != _least_rotation(word):
            continue
        is_primitive = all(
            not (
                word_length % period == 0
                and word == word[:period] * (word_length // period)
            )
            for period in range(1, word_length)
        )
        if is_primitive:
            counts[sum(mask.bit_count() for mask in word)] += 1
    return dict(sorted(counts.items()))


def cm_character_certificate(n_atoms: int, group_order: int, character_index: int) -> dict[str, object]:
    mismatch = 0
    for mask in range(1, 1 << n_atoms):
        degree = mask.bit_count()
        # D=1-B has coefficient (-1)^degree and character phase j*degree.
        derived = ((-epsilon(degree)), (character_index * degree) % group_order)
        expected = (((-1) ** degree), (character_index * degree) % group_order)
        mismatch += derived != expected
    return {
        "n_atoms": n_atoms,
        "group_order": group_order,
        "character_index": character_index,
        "is_trivial_character": character_index == 0,
        "formal_monomials_checked": (1 << n_atoms) - 1,
        "coefficient_phase_mismatches": mismatch,
        "atom_local_factorization_exact": mismatch == 0,
    }


def regular_local_cyclotomic_certificate(group_order: int) -> dict[str, object]:
    x = sp.Symbol("x")
    permutation = sp.zeros(group_order)
    for column in range(group_order):
        permutation[(column + 1) % group_order, column] = 1
    actual = sp.Poly(sp.expand((sp.eye(group_order) - x * permutation).det()), x)
    expected = sp.Poly(1 - x**group_order, x)
    return {
        "group_order": group_order,
        "det_I_minus_x_regular_generator": str(actual.as_expr()),
        "expected": str(expected.as_expr()),
        "exact_match": actual == expected,
    }


def enumerate_natural_tables(
    max_degree: int, group_order: int
) -> tuple[list[dict[str, object]], dict[str, object]]:
    """Enumerate cardinality tables r_1=1, r_2,...,r_n in C_m."""
    details: list[dict[str, object]] = []
    operator_coefficient_clean_count = 0
    character_clean_counts = {j: 0 for j in range(1, group_order)}
    first_leak_histogram: defaultdict[str, int] = defaultdict(int)

    for tail in product(range(group_order), repeat=max_degree - 1):
        table = (1 % group_order,) + tail
        deltas = [
            (table[degree - 1] - degree) % group_order
            for degree in range(1, max_degree + 1)
        ]
        first_leak = next(
            (degree for degree, delta in enumerate(deltas, start=1) if delta),
            None,
        )
        operator_coefficient_clean = first_leak is None
        operator_coefficient_clean_count += int(operator_coefficient_clean)
        first_leak_histogram[str(first_leak or "none")] += 1
        clean_characters = []
        for character in range(1, group_order):
            if all((character * delta) % group_order == 0 for delta in deltas):
                character_clean_counts[character] += 1
                clean_characters.append(character)
        details.append(
            {
                "max_degree": max_degree,
                "group_order": group_order,
                "table": ":".join(map(str, table)),
                "natural_by_cardinality": True,
                "inclusion_compatible_through_cutoff": True,
                "operator_coefficient_clean": operator_coefficient_clean,
                "first_regular_leakage_degree": first_leak or "",
                "clean_nontrivial_character_indices": ":".join(map(str, clean_characters)),
            }
        )

    expected_table_count = group_order ** (max_degree - 1)
    summary = {
        "max_degree": max_degree,
        "group_order": group_order,
        "tables_enumerated": len(details),
        "expected_tables": expected_table_count,
        "operator_coefficient_clean_tables": operator_coefficient_clean_count,
        "expected_unique_power_table": 1,
        "unique_power_table_confirmed": operator_coefficient_clean_count == 1,
        "nontrivial_character_clean_counts_json": json.dumps(character_clean_counts, sort_keys=True),
        "first_regular_leakage_histogram_json": json.dumps(
            dict(sorted(first_leak_histogram.items())), sort_keys=True
        ),
    }
    return details, summary


def _all_cycle_holonomies(
    vertex_count: int,
    group_order: int,
    alpha: Callable[[int, int], int],
    max_length: int,
) -> Iterator[tuple[tuple[int, ...], int]]:
    for length in range(1, max_length + 1):
        for cycle in product(range(vertex_count), repeat=length):
            holonomy = sum(
                alpha(cycle[index], cycle[(index + 1) % length])
                for index in range(length)
            ) % group_order
            yield cycle, holonomy


def coboundary_control_rows(max_cycle_length: int = 6) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    beta_families = {
        "identity": lambda vertex, modulus: 0,
        "affine": lambda vertex, modulus: vertex % modulus,
        "quadratic": lambda vertex, modulus: (vertex * vertex + vertex + 1) % modulus,
    }
    for vertex_count in range(2, 5):
        for group_order in range(2, 9):
            for family, beta_rule in beta_families.items():
                beta = [beta_rule(v, group_order) for v in range(vertex_count)]
                alpha = lambda u, v, beta=beta, m=group_order: (beta[v] - beta[u]) % m
                bad_cycles = sum(
                    holonomy != 0
                    for _, holonomy in _all_cycle_holonomies(
                        vertex_count, group_order, alpha, max_cycle_length
                    )
                )
                gauge_edge_mismatches = sum(
                    alpha(u, v) != (beta[v] - beta[u]) % group_order
                    for u in range(vertex_count)
                    for v in range(vertex_count)
                )
                determinant_match: bool | str = "not_applicable_nonreal_character"
                if group_order == 2:
                    untwisted = sp.Matrix(
                        [
                            [sp.Rational(1, (u + 2) * (v + 3) + 1) for v in range(vertex_count)]
                            for u in range(vertex_count)
                        ]
                    )
                    diagonal = sp.diag(*[((-1) ** value) for value in beta])
                    twisted = diagonal.inv() * untwisted * diagonal
                    determinant_match = sp.expand(
                        (sp.eye(vertex_count) - twisted).det()
                        - (sp.eye(vertex_count) - untwisted).det()
                    ) == 0
                rows.append(
                    {
                        "control_kind": "vertex_coboundary",
                        "family": family,
                        "vertex_count": vertex_count,
                        "group_order": group_order,
                        "cycles_checked": sum(vertex_count**length for length in range(1, max_cycle_length + 1)),
                        "nonidentity_periodic_holonomies": bad_cycles,
                        "gauge_edge_mismatches": gauge_edge_mismatches,
                        "c2_exact_determinant_gauge_match": determinant_match,
                    }
                )

            constant_alpha = lambda _u, _v: 1 % group_order
            witness = next(
                (cycle for cycle, holonomy in _all_cycle_holonomies(
                    vertex_count, group_order, constant_alpha, 1
                ) if holonomy),
                None,
            )
            rows.append(
                {
                    "control_kind": "noncoboundary_negative_control",
                    "family": "constant_one",
                    "vertex_count": vertex_count,
                    "group_order": group_order,
                    "cycles_checked": vertex_count,
                    "nonidentity_periodic_holonomies": vertex_count,
                    "gauge_edge_mismatches": "not_applicable",
                    "c2_exact_determinant_gauge_match": "not_applicable",
                    "periodic_witness": str(witness),
                }
            )
    return rows


def _is_c2_vertex_coboundary(vertices: list[int], alpha: Callable[[int, int], int]) -> bool:
    root = vertices[0]
    beta = {root: 0}
    for vertex in vertices[1:]:
        beta[vertex] = alpha(root, vertex) % 2
    return all(
        alpha(u, v) % 2 == (beta[v] - beta[u]) % 2
        for u in vertices
        for v in vertices
    )


def _first_nonzero_cycle(
    vertices: list[int], alpha: Callable[[int, int], int], max_length: int = 4
) -> tuple[int, ...] | None:
    for length in range(1, max_length + 1):
        for cycle in product(vertices, repeat=length):
            holonomy = sum(
                alpha(cycle[index], cycle[(index + 1) % length])
                for index in range(length)
            ) % 2
            if holonomy:
                return cycle
    return None


def _first_sympy_term(expression: sp.Expr, variables: tuple[sp.Symbol, ...]) -> str:
    if sp.expand(expression) == 0:
        return ""
    polynomial = sp.Poly(sp.expand(expression), *variables)
    terms = sorted(
        ((sum(exponents), exponents, coefficient) for exponents, coefficient in polynomial.terms()),
        key=lambda item: (item[0], item[1]),
    )
    if not terms:
        return ""
    _, exponents, coefficient = terms[0]
    return f"coeff={coefficient};exponents={exponents}"


def _first_sympy_degree(expression: sp.Expr, variables: tuple[sp.Symbol, ...]) -> int | None:
    if sp.expand(expression) == 0:
        return None
    polynomial = sp.Poly(sp.expand(expression), *variables)
    return min(sum(exponents) for exponents, _ in polynomial.terms())


def transition_countercontrol_rows() -> list[dict[str, object]]:
    """Minimal n=2 transition controls delimiting the one-letter theorem."""
    x, y = sp.symbols("x y")
    variables = (x, y)
    vertices = [1, 2, 3]  # {p}, {q}, {p,q}
    weights = {1: x, 2: y, 3: -x * y}
    degree_parity = {mask: mask.bit_count() % 2 for mask in vertices}
    controls: dict[str, Callable[[int, int], int]] = {
        "vertex_coboundary_degree": lambda source, target: (
            degree_parity[target] - degree_parity[source]
        ) % 2,
        "diagonal_return": lambda source, target: int(source == target),
        "incidence_intersection_parity": lambda source, target: (source & target).bit_count() % 2,
        "strict_symbol_change": lambda source, target: int(source != target),
    }
    d_plus = sp.expand((1 - x) * (1 - y))
    d_minus = sp.expand((1 + x) * (1 + y))
    rows: list[dict[str, object]] = []
    for name, alpha in controls.items():
        matrix = sp.Matrix(
            [
                [weights[target] * ((-1) ** alpha(source, target)) for target in vertices]
                for source in vertices
            ]
        )
        determinant = sp.expand((sp.eye(len(vertices)) - matrix).det())
        delta_plus = sp.expand(determinant - d_plus)
        delta_minus = sp.expand(determinant - d_minus)
        is_coboundary = _is_c2_vertex_coboundary(vertices, alpha)
        witness = _first_nonzero_cycle(vertices, alpha)
        plus_degree = _first_sympy_degree(delta_plus, variables)
        minus_degree = _first_sympy_degree(delta_minus, variables)
        if plus_degree is None:
            nearest_name, nearest_delta = "D_plus", delta_plus
        elif minus_degree is None:
            nearest_name, nearest_delta = "D_minus", delta_minus
        elif plus_degree >= minus_degree:
            nearest_name, nearest_delta = "D_plus", delta_plus
        else:
            nearest_name, nearest_delta = "D_minus", delta_minus
        rows.append(
            {
                "control": name,
                "alphabet": "{p},{q},{p,q}",
                "transition_dependent": True,
                "is_vertex_coboundary": is_coboundary,
                "first_nontrivial_periodic_holonomy": str(witness) if witness else "",
                "sign_block_determinant": str(determinant),
                "delta_from_D_plus": str(delta_plus),
                "delta_from_D_minus": str(delta_minus),
                "equals_trivial_atom_local_factor": delta_plus == 0,
                "equals_parity_sign_atom_local_factor": delta_minus == 0,
                "nearest_atom_local_baseline": nearest_name,
                "first_leak_vs_nearest_atom_local": _first_sympy_term(nearest_delta, variables),
            }
        )
    return rows


def first_primes(count: int) -> list[int]:
    primes: list[int] = []
    candidate = 2
    while len(primes) < count:
        if all(candidate % prime for prime in primes if prime * prime <= candidate):
            primes.append(candidate)
        candidate += 1
    return primes


def first_composites(count: int) -> list[int]:
    out: list[int] = []
    candidate = 4
    while len(out) < count:
        if any(candidate % divisor == 0 for divisor in range(2, int(candidate**0.5) + 1)):
            out.append(candidate)
        candidate += 1
    return out


def inventory_values(kind: str, n_atoms: int, seed: int) -> list[Fraction]:
    rng = random.Random(seed)
    if kind == "prime":
        return [Fraction(1, value * value) for value in first_primes(n_atoms)]
    if kind == "shuffled_prime":
        values = [Fraction(1, value * value) for value in first_primes(n_atoms)]
        rng.shuffle(values)
        return values
    if kind == "composite":
        values = [Fraction(1, value * value) for value in first_composites(n_atoms)]
        rng.shuffle(values)
        return values
    if kind == "random_rational":
        values = []
        for _ in range(n_atoms):
            denominator = rng.randint(17, 97)
            numerator = rng.randint(1, denominator - 1)
            values.append(Fraction(numerator, denominator))
        return values
    raise ValueError(f"unknown inventory kind: {kind}")


def numeric_fraction_certificate(values: list[Fraction]) -> dict[str, object]:
    b_plus = Fraction(0)
    b_minus = Fraction(0)
    b_even = Fraction(0)
    b_odd = Fraction(0)
    n_atoms = len(values)
    for mask in range(1, 1 << n_atoms):
        degree = mask.bit_count()
        monomial = Fraction(1)
        for index, value in enumerate(values):
            if mask >> index & 1:
                monomial *= value
        term = epsilon(degree) * monomial
        b_plus += term
        b_minus += term * ((-1) ** degree)
        if degree % 2:
            b_odd += term
        else:
            b_even += term
    d_plus = 1 - b_plus
    d_minus = 1 - b_minus
    d_regular = (1 - b_even) ** 2 - b_odd**2
    expected_plus = Fraction(1)
    expected_minus = Fraction(1)
    expected_regular = Fraction(1)
    for value in values:
        expected_plus *= 1 - value
        expected_minus *= 1 + value
        expected_regular *= 1 - value**2
    return {
        "d_plus": str(d_plus),
        "d_minus": str(d_minus),
        "d_regular": str(d_regular),
        "d_plus_exact": d_plus == expected_plus,
        "d_minus_exact": d_minus == expected_minus,
        "d_regular_exact": d_regular == expected_regular,
        "same_object_exact": d_regular == d_plus * d_minus,
    }


def inventory_control_rows(
    n_atoms: int = 10, seeds: Iterable[int] = range(17000, 17016)
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for seed in seeds:
        for kind in ("prime", "shuffled_prime", "composite", "random_rational"):
            values = inventory_values(kind, n_atoms, seed)
            certificate = numeric_fraction_certificate(values)
            rows.append(
                {
                    "seed": seed,
                    "inventory_kind": kind,
                    "n_atoms": n_atoms,
                    "values_sha256": sha256(
                        json.dumps([str(value) for value in values], separators=(",", ":")).encode()
                    ).hexdigest(),
                    **certificate,
                }
            )
    return rows
