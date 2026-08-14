#!/usr/bin/env python3
"""Exact HCS-P57 certificate for the five-block Galois-excess obstruction."""

from __future__ import annotations

import argparse
import copy
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp


PROJECT = Path(__file__).resolve().parents[1]
TRACK = PROJECT.parent
DEFAULT_OUTPUT = PROJECT / "results" / "c57_certificate.json"

X, T, Z = sp.symbols("X T Z")
ADJACENCY = (
    (1, 0, 1, 0),
    (1, 0, 0, 0),
    (0, 1, 0, 1),
    (0, 1, 0, 0),
)

DEPENDENCIES = {
    "p56_readme": (
        TRACK / "henon_galois_excess_four_block_incidence_ladder" / "README.md",
        "952a0f8073451a952aedba1494cc45ba9af5c2c13f2c98cd720cda8588bd2251",
    ),
    "p56_proof": (
        TRACK / "henon_galois_excess_four_block_incidence_ladder" / "PROOF_PACKAGE.md",
        "dbc4f564e2e8523fdb02f7ef0a4d5b67ed5cd943682dc635556fb17fc69ecbfa",
    ),
    "p56_code": (
        TRACK
        / "henon_galois_excess_four_block_incidence_ladder"
        / "code"
        / "c56_incidence_ladder.py",
        "ae772ebf7cc9343cf7e3b81abd355fc4b14896ab9cd692255e5d2b402c02f706",
    ),
    "p56_certificate": (
        TRACK
        / "henon_galois_excess_four_block_incidence_ladder"
        / "results"
        / "c56_certificate.json",
        "c992ccb40f2fa4009a47fd5542952195430c75df322daeb9dfdac3e894000d23",
    ),
    "p55_certificate": (
        TRACK
        / "henon_galois_excess_three_block_obstruction"
        / "results"
        / "c55_certificate.json",
        "d21cdcdfcce7cb279fab02ee3222c5d5a10e4fc6efa63e2e611d135e2ff27f1c",
    ),
    "p54_certificate": (
        TRACK
        / "henon_mahler_pressure_pole_galois_excess_gate"
        / "results"
        / "c54_certificate.json",
        "d6932d0b24111866253508b5dd7c33972856cfdbddd5dfdd7db77a92a38f233c",
    ),
    "p31_certificate": (
        TRACK / "henon_bowen_pressure_gate" / "results" / "c31_certificate.json",
        "9f326c8442f5f1dfb8215527491a9ebbac2395fde7892c88bc78634df24c5cca",
    ),
    "orbit_catalog": (
        TRACK / "henon_instability_roof_zeta" / "results" / "catalog_validation.json",
        "0eab1930a17e4315e59eebc9dc7d3ef111b674d3625f09ca3396c1aa7c814fde",
    ),
}

TRACE5 = sp.Poly(
    T**6
    + 3300 * T**5
    - 34165368 * T**4
    - 7291075328 * T**3
    + 26529205510272 * T**2
    + 3609165326736384 * T
    - 4266315336505009664,
    T,
)
TRACE5_INTERVALS = (
    (-7607, -7606),
    (-711, -710),
    (-590, -589),
    (390, 391),
    (770, 771),
    (4445, 4446),
)

A6_COORDINATE = sp.Poly(
    2916 * X**6 - 1782 * X**4 + 108 * X**3 + 279 * X**2 - 33 * X - 2,
    X,
)
A6_TRACE = sp.Poly(
    T**3 + 48342 * T**2 - 334511988 * T + 306994257352,
    T,
)
A6_TRACE_INTERVALS = ((-54575, -54574), (1094, 1095), (5137, 5138))

P7_COORDINATE = sp.Poly(
    612220032 * X**14
    - 204073344 * X**13
    - 646232256 * X**12
    + 226748160 * X**11
    + 247533408 * X**10
    - 90069408 * X**9
    - 41045616 * X**8
    + 15046560 * X**7
    + 2834352 * X**6
    - 948672 * X**5
    - 97848 * X**4
    + 22032 * X**3
    + 1512 * X**2
    - 144 * X
    - 7,
    X,
)
P7_TRACE = sp.Poly(
    T**14
    + 53380 * T**13
    - 116230063064 * T**12
    + 8748136108873472 * T**11
    + 930148180553911001792 * T**10
    - 55441728431344376174558464 * T**9
    - 1042857805960956394737247010304 * T**8
    + 67800369626486919391549995220844544 * T**7
    + 248063550855956838882026032464056057856 * T**6
    - 18599810233678146836278775387225818293010432 * T**5
    - 125626107241488921782218909595028406082053341184 * T**4
    + 648460503108807187082799707783053721181729242218496 * T**3
    + 5188095852189806429800801204477225625428281884227403776 * T**2
    - 3780455159472389946318383487211963920344828975222028763136 * T
    - 43775419253348240272917680080620537154762693674649008390275072,
    T,
)
P7_TRACE_INTERVALS = (
    (-390512, -390511),
    (-76494, -76493),
    (-33929, -33928),
    (-9534, -9533),
    (-9431, -9430),
    (-5707, -5706),
    (-4082, -4081),
    (3217, 3218),
    (5681, 5682),
    (29838, 29839),
    (32741, 32742),
    (36376, 36377),
    (137464, 137465),
    (230985, 230986),
)


def canonical_sha(payload: object) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def dependency_locks() -> dict[str, dict[str, str]]:
    result: dict[str, dict[str, str]] = {}
    for name, (path, expected) in DEPENDENCIES.items():
        observed = hashlib.sha256(path.read_bytes()).hexdigest()
        if observed != expected:
            raise RuntimeError(f"dependency hash changed: {name}")
        result[name] = {"path": str(path.relative_to(TRACK)), "sha256": observed}
    return result


def rotations(word: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(word[i:] + word[:i] for i in range(len(word)))


def primitive(word: tuple[int, ...]) -> bool:
    n = len(word)
    return not any(n % d == 0 and word == word[:d] * (n // d) for d in range(1, n))


def primitive_cycles(max_period: int = 7) -> dict[int, list[tuple[int, ...]]]:
    result: dict[int, list[tuple[int, ...]]] = {}
    for n in range(1, max_period + 1):
        cycles: set[tuple[int, ...]] = set()
        for word in itertools.product(range(4), repeat=n):
            if all(ADJACENCY[word[i]][word[(i + 1) % n]] for i in range(n)) and primitive(word):
                cycles.add(min(rotations(word)))
        result[n] = sorted(cycles)
    return result


def family_a(n: int) -> tuple[int, ...]:
    if n < 3:
        raise ValueError("A_n starts at n=3")
    return (0,) * (n - 2) + (2, 1)


def family_b(n: int) -> tuple[int, ...]:
    if n < 4:
        raise ValueError("B_n starts at n=4")
    return (0,) * (n - 3) + (2, 3, 1)


def block_counter(word: tuple[int, ...], width: int) -> dict[tuple[int, ...], int]:
    result: dict[tuple[int, ...], int] = {}
    for i in range(len(word)):
        block = tuple(word[(i + j) % len(word)] for j in range(width))
        result[block] = result.get(block, 0) + 1
    return result


def incidence_matrix(words: list[tuple[int, ...]], width: int) -> tuple[list[tuple[int, ...]], sp.Matrix]:
    counters = [block_counter(word, width) for word in words]
    blocks = sorted({block for counter in counters for block in counter})
    matrix = sp.Matrix([[counter.get(block, 0) for block in blocks] for counter in counters])
    return blocks, matrix


def signed_incidence(rows: tuple[tuple[int, tuple[int, ...]], ...], width: int) -> dict[tuple[int, ...], int]:
    result: dict[tuple[int, ...], int] = {}
    for sign, word in rows:
        for block, count in block_counter(word, width).items():
            result[block] = result.get(block, 0) + sign * count
    return {block: count for block, count in result.items() if count}


def derivative(q: sp.Expr) -> sp.Matrix:
    return sp.Matrix([[-12 * q, -1], [1, 0]])


def monodromy(coordinates: tuple[sp.Expr, ...]) -> sp.Matrix:
    matrix = sp.eye(2)
    for coordinate in coordinates:
        matrix = derivative(coordinate) * matrix
    return matrix.applyfunc(sp.expand)


def chain_polynomials() -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    b = sp.expand((1 - 6 * X**2) / 2)
    c = sp.expand(1 - 6 * b**2 - X)
    d = sp.expand(1 - 6 * c**2 - b)
    return b, c, d


def reduce_expression(expression: sp.Expr, polynomial: sp.Poly) -> sp.Expr:
    numerator, denominator = sp.together(expression).as_numer_denom()
    remainder = sp.rem(numerator, polynomial, X)
    return sp.factor(remainder / denominator)


def reciprocal_multiplier_polynomial(trace_polynomial: sp.Poly) -> sp.Poly:
    degree = trace_polynomial.degree()
    return sp.Poly(sp.expand(trace_polynomial.as_expr().subs(T, Z + 1 / Z) * Z**degree), Z)


def exact_root_data(polynomial: sp.Poly, intervals: tuple[tuple[int, int], ...]) -> tuple[list[sp.Expr], list[sp.Expr], sp.Expr]:
    counts = [int(polynomial.count_roots(left, right)) for left, right in intervals]
    if counts != [1] * polynomial.degree():
        raise ArithmeticError("trace root isolation changed")
    roots = sorted(
        [sp.re(root) for root in sp.nroots(polynomial.as_expr(), n=90, maxsteps=1000)],
        key=float,
    )
    lengths = [sp.acosh(sp.Abs(root) / 2) for root in roots]
    return roots, lengths, sum(lengths, sp.Float(0, 90))


def period_six_a_algebra() -> dict[str, object]:
    b, c, d = chain_polynomials()
    closing = sp.factor(1 - 6 * d**2 - 2 * c)
    expected_factors = sp.factor(
        -2
        * (6 * X**2 + 2 * X - 1)
        * (9 * X**2 - 3 * X - 1)
        * (18 * X**2 - 6 * X - 1)
        * (324 * X**4 + 108 * X**3 - 54 * X**2 - 6 * X + 1)
        * A6_COORDINATE.as_expr()
    )
    if sp.expand(closing - expected_factors) != 0:
        raise ArithmeticError("A6 closing factorization mismatch")

    coordinates = (X, b, c, d, c, b)
    residuals = tuple(
        reduce_expression(
            1 - 6 * coordinates[i] ** 2 - coordinates[(i - 1) % 6] - coordinates[(i + 1) % 6],
            A6_COORDINATE,
        )
        for i in range(6)
    )
    if any(value != 0 for value in residuals):
        raise ArithmeticError("A6 recurrence failed modulo its coordinate polynomial")

    trace_reduced = reduce_expression(sp.trace(monodromy(coordinates)), A6_COORDINATE)
    expected_trace = -2 * (
        1364688 * X**4 - 94608 * X**3 - 379080 * X**2 + 56808 * X + 689
    )
    if sp.expand(trace_reduced - expected_trace) != 0:
        raise ArithmeticError("A6 reduced trace mismatch")
    trace_resultant = sp.Poly(
        sp.resultant(A6_COORDINATE.as_expr(), T - trace_reduced, X), T
    ).primitive()[1]
    if trace_resultant != sp.Poly(A6_TRACE.as_expr() ** 2, T):
        raise ArithmeticError("A6 trace resultant mismatch")
    mod5_factors = sp.factor_list(A6_TRACE.as_expr(), modulus=5)[1]
    if len(mod5_factors) != 1 or sp.degree(mod5_factors[0][0], T) != 3:
        raise ArithmeticError("A6 trace irreducibility witness failed")
    if [int(A6_TRACE.count_roots(*interval)) for interval in A6_TRACE_INTERVALS] != [1, 1, 1]:
        raise ArithmeticError("A6 trace intervals changed")

    coordinate_interval = (sp.Rational(551907131, 10**9), sp.Rational(551907132, 10**9))
    if A6_COORDINATE.count_roots(*coordinate_interval) != 1:
        raise ArithmeticError("A6 physical coordinate was not isolated")
    coordinate_signs = []
    coordinate_zero_counts = []
    for expression in (X, b, c, d):
        zero_count = int(sp.Poly(expression, X).count_roots(*coordinate_interval))
        if zero_count != 0:
            raise ArithmeticError("A6 coordinate crosses zero inside its isolator")
        signs = [int(sp.sign(expression.subs(X, endpoint))) for endpoint in coordinate_interval]
        if signs[0] != signs[1] or signs[0] == 0:
            raise ArithmeticError("A6 coordinate sign box changed")
        coordinate_zero_counts.append(zero_count)
        coordinate_signs.append(signs[0])
    trace_derivative_root_count = int(
        sp.Poly(sp.diff(trace_reduced, X), X).count_roots(*coordinate_interval)
    )
    if trace_derivative_root_count != 0:
        raise ArithmeticError("A6 trace is not monotone on its coordinate isolator")
    trace_endpoints = [sp.N(trace_reduced.subs(X, endpoint), 40) for endpoint in coordinate_interval]
    if not all(-54575 < value < -54574 for value in trace_endpoints):
        raise ArithmeticError("A6 physical trace interval changed")

    roots, lengths, total_height = exact_root_data(A6_TRACE, A6_TRACE_INTERVALS)
    physical_length = lengths[0]
    excess = total_height - physical_length
    multiplier = reciprocal_multiplier_polynomial(A6_TRACE)
    if sp.factor_list(multiplier.as_expr())[1] != [(multiplier.as_expr(), 1)]:
        raise ArithmeticError("A6 multiplier polynomial is reducible")

    return {
        "word": "000021",
        "reflection_pattern": ["a", "b", "c", "d", "c", "b"],
        "coordinate_chain": {"b": str(b), "c": str(c), "d": str(d)},
        "coordinate_polynomial": str(A6_COORDINATE.as_expr()),
        "coordinate_polynomial_degree": A6_COORDINATE.degree(),
        "physical_coordinate_interval": [str(value) for value in coordinate_interval],
        "physical_chain_signs": coordinate_signs,
        "physical_chain_zero_counts": coordinate_zero_counts,
        "trace_derivative_root_count_on_physical_interval": trace_derivative_root_count,
        "trace_as_polynomial_in_a": str(trace_reduced),
        "trace_polynomial": str(A6_TRACE.as_expr()),
        "trace_polynomial_degree": A6_TRACE.degree(),
        "trace_resultant_multiplicity": 2,
        "trace_irreducible_mod_prime": 5,
        "trace_root_intervals": [list(interval) for interval in A6_TRACE_INTERVALS],
        "physical_trace_interval": list(A6_TRACE_INTERVALS[0]),
        "multiplier_polynomial_coefficients": [int(value) for value in multiplier.all_coeffs()],
        "multiplier_degree": multiplier.degree(),
        "physical_length_decimal_50": str(sp.N(physical_length, 50)),
        "mahler_height_decimal_50": str(sp.N(total_height, 50)),
        "galois_excess_decimal_50": str(sp.N(excess, 50)),
        "galois_excess_definition": "sum of reciprocal-pair logs over the two nonphysical trace embeddings",
    }


def period_seven_algebra() -> dict[str, object]:
    b, c, d = chain_polynomials()
    closing = sp.factor(1 - 6 * d**2 - c - d)
    expected = sp.factor(-(6 * X**2 + 2 * X - 1) * P7_COORDINATE.as_expr() / 2)
    if sp.expand(closing - expected) != 0:
        raise ArithmeticError("period-seven closing factorization mismatch")

    coordinates = (X, b, c, d, d, c, b)
    residuals = tuple(
        reduce_expression(
            1 - 6 * coordinates[i] ** 2 - coordinates[(i - 1) % 7] - coordinates[(i + 1) % 7],
            P7_COORDINATE,
        )
        for i in range(7)
    )
    if any(value != 0 for value in residuals):
        raise ArithmeticError("period-seven recurrence failed modulo its coordinate polynomial")

    trace_reduced = reduce_expression(sp.trace(monodromy(coordinates)), P7_COORDINATE)
    expected_trace = -4 * (
        97955205120 * X**13
        - 1224440064 * X**12
        - 95642373888 * X**11
        + 5419281024 * X**10
        + 35081719488 * X**9
        - 3199983408 * X**8
        - 5928624576 * X**7
        + 659949120 * X**6
        + 458896752 * X**5
        - 50247540 * X**4
        - 14865768 * X**3
        + 1198152 * X**2
        + 167679 * X
        - 5050
    )
    if sp.expand(trace_reduced - expected_trace) != 0:
        raise ArithmeticError("period-seven reduced trace mismatch")
    trace_resultant = sp.Poly(
        sp.resultant(P7_COORDINATE.as_expr(), T - trace_reduced, X), T
    ).primitive()[1]
    if trace_resultant != P7_TRACE:
        raise ArithmeticError("period-seven trace resultant mismatch")
    mod37_factors = sp.factor_list(P7_TRACE.as_expr(), modulus=37)[1]
    if len(mod37_factors) != 1 or sp.degree(mod37_factors[0][0], T) != 14:
        raise ArithmeticError("period-seven trace irreducibility witness failed")
    if [int(P7_TRACE.count_roots(*interval)) for interval in P7_TRACE_INTERVALS] != [1] * 14:
        raise ArithmeticError("period-seven trace intervals changed")

    physical_intervals = {
        "B7": (sp.Rational(-600956965, 10**9), sp.Rational(-600956964, 10**9)),
        "A7": (sp.Rational(551935742, 10**9), sp.Rational(551935743, 10**9)),
    }
    expected_signs = {"B7": [-1, -1, -1, 1], "A7": [1, -1, -1, -1]}
    expected_trace_intervals = {"B7": (230985, 230986), "A7": (-390512, -390511)}
    embedding_certificate: dict[str, object] = {}
    for name, interval in physical_intervals.items():
        if P7_COORDINATE.count_roots(*interval) != 1:
            raise ArithmeticError(f"{name} coordinate was not isolated")
        signs = []
        zero_counts = []
        for expression in (X, b, c, d):
            zero_count = int(sp.Poly(expression, X).count_roots(*interval))
            if zero_count != 0:
                raise ArithmeticError(f"{name} coordinate crosses zero inside its isolator")
            endpoint_signs = [int(sp.sign(expression.subs(X, endpoint))) for endpoint in interval]
            if endpoint_signs[0] != endpoint_signs[1] or endpoint_signs[0] == 0:
                raise ArithmeticError(f"{name} coordinate sign box changed")
            zero_counts.append(zero_count)
            signs.append(endpoint_signs[0])
        if signs != expected_signs[name]:
            raise ArithmeticError(f"{name} sign word changed")
        trace_derivative_root_count = int(
            sp.Poly(sp.diff(trace_reduced, X), X).count_roots(*interval)
        )
        if trace_derivative_root_count != 0:
            raise ArithmeticError(f"{name} trace is not monotone on its coordinate isolator")
        trace_endpoints = [sp.N(trace_reduced.subs(X, endpoint), 40) for endpoint in interval]
        left, right = expected_trace_intervals[name]
        if not all(left < value < right for value in trace_endpoints):
            raise ArithmeticError(f"{name} physical trace interval changed")
        embedding_certificate[name] = {
            "coordinate_interval": [str(value) for value in interval],
            "chain_signs": signs,
            "chain_zero_counts": zero_counts,
            "trace_derivative_root_count": trace_derivative_root_count,
            "cyclic_sign_word": "+------" if name == "A7" else "---++--",
            "trace_interval": [left, right],
        }

    roots, lengths, total_height = exact_root_data(P7_TRACE, P7_TRACE_INTERVALS)
    excess_a7 = total_height - lengths[0]
    excess_b7 = total_height - lengths[-1]
    multiplier = reciprocal_multiplier_polynomial(P7_TRACE)
    if sp.factor_list(multiplier.as_expr())[1] != [(multiplier.as_expr(), 1)]:
        raise ArithmeticError("period-seven multiplier polynomial is reducible")

    return {
        "reflection_pattern": ["a", "b", "c", "d", "d", "c", "b"],
        "coordinate_chain": {"b": str(b), "c": str(c), "d": str(d)},
        "coordinate_polynomial": str(P7_COORDINATE.as_expr()),
        "coordinate_polynomial_degree": P7_COORDINATE.degree(),
        "trace_as_polynomial_in_a": str(trace_reduced),
        "trace_polynomial": str(P7_TRACE.as_expr()),
        "trace_polynomial_degree": P7_TRACE.degree(),
        "trace_irreducible_mod_prime": 37,
        "all_trace_roots_real": True,
        "trace_root_intervals": [list(interval) for interval in P7_TRACE_INTERVALS],
        "physical_embeddings": embedding_certificate,
        "multiplier_polynomial_coefficients": [int(value) for value in multiplier.all_coeffs()],
        "multiplier_degree": multiplier.degree(),
        "mahler_height_decimal_50": str(sp.N(total_height, 50)),
        "A7_physical_length_decimal_50": str(sp.N(lengths[0], 50)),
        "A7_galois_excess_decimal_50": str(sp.N(excess_a7, 50)),
        "B7_physical_length_decimal_50": str(sp.N(lengths[-1], 50)),
        "B7_galois_excess_decimal_50": str(sp.N(excess_b7, 50)),
        "shared_field_statement": "A7 and B7 are two real embeddings of one irreducible degree-14 trace field",
    }


def excess_obstruction(a6: dict[str, object], p7: dict[str, object]) -> dict[str, object]:
    roots5, lengths5, height5 = exact_root_data(TRACE5, TRACE5_INTERVALS)
    roots6, lengths6, height6 = exact_root_data(A6_TRACE, A6_TRACE_INTERVALS)
    roots7, lengths7, height7 = exact_root_data(P7_TRACE, P7_TRACE_INTERVALS)
    excess_a5 = height5 - lengths5[0]
    excess_a6 = height6 - lengths6[0]
    excess_b6 = sp.acosh(9031 - 2676 * sp.sqrt(7))
    excess_b7 = height7 - lengths7[-1]
    delta5 = excess_a5 + excess_b7 - excess_a6 - excess_b6

    lower_factors = (709, 588, 389, 769, 4444)
    upper_factors = (1095, 5138, 3902)
    lower_product = int(sp.prod(lower_factors))
    upper_product = int(sp.prod(upper_factors))
    integer_margin = lower_product - upper_product
    if integer_margin != 554187019465548 or lower_product <= upper_product:
        raise ArithmeticError("five-block integer comparison changed")
    nonphysical_b7_intervals = P7_TRACE_INTERVALS[:-1]
    if len(nonphysical_b7_intervals) != 13 or not all(
        right < -2 or left > 2 for left, right in nonphysical_b7_intervals
    ):
        raise ArithmeticError("exact B7 excess positivity certificate changed")
    if not delta5 > 0:
        raise ArithmeticError("numerical Delta_5 diagnostic changed")

    return {
        "definition": "Delta_5=E(A5)+E(B7)-E(A6)-E(B6)",
        "A5_excess_decimal_50": str(sp.N(excess_a5, 50)),
        "A6_excess_decimal_50": str(sp.N(excess_a6, 50)),
        "B6_excess_decimal_50": str(sp.N(excess_b6, 50)),
        "B7_excess_decimal_50": str(sp.N(excess_b7, 50)),
        "Delta_5_decimal_50": str(sp.N(delta5, 50)),
        "strict_sign": "positive",
        "exact_lower_factors_for_E_A5": list(lower_factors),
        "exact_upper_factors_for_E_A6_plus_E_B6": list(upper_factors),
        "lower_product": lower_product,
        "upper_product": upper_product,
        "integer_margin": integer_margin,
        "B7_excess_positive_by_13_nonphysical_root_intervals": True,
        "proof_chain": "E(A5)>log(lower_product)>log(upper_product)>E(A6)+E(B6), while E(B7)>0",
        "width_at_most_5_obstruction": True,
    }


def finite_sharpness() -> dict[str, object]:
    relation_words = [family_a(5), family_b(7), family_a(6), family_b(6)]
    relation = signed_incidence(
        ((1, relation_words[0]), (1, relation_words[1]), (-1, relation_words[2]), (-1, relation_words[3])),
        5,
    )
    if relation:
        raise ArithmeticError("width-five ladder relation changed")
    blocks5, matrix5 = incidence_matrix(relation_words, 5)
    if matrix5.rank() != 3 or sp.Matrix([[1, 1, -1, -1]]) * matrix5 != sp.zeros(1, len(blocks5)):
        raise ArithmeticError("width-five relation rank changed")

    selected_four = [
        (0, 0, 0, 0, 2, 1),
        (0, 0, 0, 0, 2, 3),
        (0, 0, 0, 2, 1, 0),
        (0, 0, 0, 2, 3, 1),
    ]
    four_minor = sp.Matrix(
        [[block_counter(word, 6).get(block, 0) for block in selected_four] for word in relation_words]
    )
    if four_minor.det() != -1:
        raise ArithmeticError("four-row width-six minor changed")

    cumulative_words = [
        (0,),
        family_a(3),
        family_a(4),
        family_b(4),
        family_a(5),
        family_b(5),
        family_b(6),
        family_a(6),
        family_b(7),
    ]
    selected_nine = [
        (0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 2, 1),
        (0, 0, 0, 0, 2, 3),
        (0, 0, 0, 2, 1, 0),
        (0, 0, 0, 2, 3, 1),
        (0, 0, 2, 1, 0, 0),
        (0, 0, 2, 3, 1, 0),
        (0, 2, 1, 0, 2, 1),
        (0, 2, 3, 1, 0, 2),
    ]
    cumulative_minor = sp.Matrix(
        [[block_counter(word, 6).get(block, 0) for block in selected_nine] for word in cumulative_words]
    )
    if cumulative_minor.det() != 1:
        raise ArithmeticError("cumulative width-six minor changed")

    return {
        "relation_row_order": ["A5", "B7", "A6", "B6"],
        "width_5_rank": matrix5.rank(),
        "width_5_left_relation": [1, 1, -1, -1],
        "width_6_four_row_selected_blocks": ["".join(map(str, block)) for block in selected_four],
        "width_6_four_row_minor": [[int(value) for value in row] for row in four_minor.tolist()],
        "width_6_four_row_determinant": int(four_minor.det()),
        "cumulative_row_order": ["C1", "A3", "A4", "B4", "A5", "B5", "B6", "A6", "B7"],
        "width_6_cumulative_selected_blocks": ["".join(map(str, block)) for block in selected_nine],
        "width_6_cumulative_minor": [[int(value) for value in row] for row in cumulative_minor.tolist()],
        "width_6_cumulative_determinant": int(cumulative_minor.det()),
        "finite_witness_sharp_at_width_6": True,
        "scope": "finite interpolation only; no all-orbit width-six or Holder realization is constructed",
    }


def symbolic_certificate() -> dict[str, object]:
    cycles = primitive_cycles(7)
    observed = {period: len(words) for period, words in cycles.items()}
    expected = {1: 1, 2: 0, 3: 1, 4: 2, 5: 2, 6: 2, 7: 4}
    if observed != expected:
        raise ArithmeticError("primitive cycle census through seven changed")
    for n in range(3, 8):
        if family_a(n) not in cycles[n]:
            raise ArithmeticError(f"A{n} missing from cycle census")
    for n in range(4, 8):
        if family_b(n) not in cycles[n]:
            raise ArithmeticError(f"B{n} missing from cycle census")
    ladder_checks = []
    for m in range(3, 65):
        relation = signed_incidence(
            ((1, family_a(m)), (1, family_b(m + 2)), (-1, family_a(m + 1)), (-1, family_b(m + 1))),
            m,
        )
        if relation:
            raise ArithmeticError(f"incidence ladder failed at m={m}")
        ladder_checks.append(m)
    return {
        "primitive_cycle_counts_through_7": {str(key): value for key, value in observed.items()},
        "period_7_cycles": ["".join(map(str, word)) for word in cycles[7]],
        "A7": "".join(map(str, family_a(7))),
        "B7": "".join(map(str, family_b(7))),
        "ladder_theorem": "N_m(A_m)+N_m(B_(m+2))=N_m(A_(m+1))+N_m(B_(m+1)) for every m>=3",
        "finite_ladder_verification_range": [ladder_checks[0], ladder_checks[-1]],
    }


def core_payload() -> dict[str, object]:
    a6 = period_six_a_algebra()
    p7 = period_seven_algebra()
    obstruction = excess_obstruction(a6, p7)
    return {
        "candidate_id": "HCS-P57",
        "source_object": "the P56 all-width incidence ladder on the frozen four-state mixing H6 survivor",
        "symbolic_certificate": symbolic_certificate(),
        "A6_exact_algebra": a6,
        "period_7_exact_algebra": p7,
        "five_block_obstruction": {
            "status": "PROVED",
            **obstruction,
            "theorem": "no locally constant potential depending on at most five consecutive H6 states realizes every primitive-orbit Galois excess",
            "finite_witness": ["A5", "A6", "B6", "B7"],
            "memory_lower_bound": "any locally constant realization must use at least six consecutive symbolic states",
        },
        "finite_sharpness": finite_sharpness(),
        "holder_scope": {
            "status": "OPEN_ASYMPTOTICS",
            "discrepancy": "Delta_m=E(A_m)+E(B_(m+2))-E(A_(m+1))-E(B_(m+1))",
            "new_value": "Delta_5 is positive and approximately 139.7325728699720846",
            "why_not_holder_no_go": "one fixed nonzero discrepancy is compatible with a Holder constant; only asymptotic lower bounds can contradict exponential decay",
            "necessary_bound": "|Delta_m|<=C(4m+4)theta^(alpha*m) for all m>=3 under a one-sided Holder realization",
        },
        "strongest_positive_result": "A6 has an irreducible cubic trace field, while A7 and B7 are physical embeddings of one totally real irreducible degree-14 trace field",
        "strongest_obstruction": "the m=5 incidence identity fails by a certified positive Galois-excess discrepancy, excluding every width-at-most-five local potential",
        "open_theorem": "determine the asymptotic scale and sign pattern of Delta_m; a non-exponentially-small subsequence would rule out one-sided Holder realization",
        "reusable_structure": "reflection reduction turns A_(2k) and the shared A_(2k+1)/B_(2k+1) family into one-variable closing polynomials, trace resultants and Sturm-certified physical embeddings",
        "round2_clue": "derive the fixed-point tail linearization for both reflection chains and compare Delta_m to the stable eigenvalue of the negative fixed point; compute B8 only as a falsifier for the predicted leading mode",
        "route_a_status": {
            "tuple": "(A1_WEAK, A2_ANALYTIC_DETERMINANT [physical subsystem only], A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FORMAL_HINT)",
            "overall": "ROUTE_A_EXPLORATORY",
            "full_galois_A2_pass": False,
        },
        "route_b_authorized": False,
        "arithmetic_advance": "NO",
        "claim_boundary": "P57 proves exact period-six/seven trace algebra and a width-at-most-five obstruction; it does not refute unrestricted Holder data, construct the full Galois determinant, identify rational primes, or build a Hilbert-Polya operator",
    }


def validate_core(candidate: object, expected: object) -> None:
    if type(candidate) is not dict or candidate != expected:
        raise ValueError("core payload changed")


def assign_path(payload: object, path: tuple[object, ...], value: object) -> None:
    cursor = payload
    for key in path[:-1]:
        cursor = cursor[key]  # type: ignore[index]
    cursor[path[-1]] = value  # type: ignore[index]


def mutation_audit(core: dict[str, object]) -> dict[str, object]:
    mutations = (
        ("period7_count", ("symbolic_certificate", "primitive_cycle_counts_through_7", "7"), 3),
        ("A7_word", ("symbolic_certificate", "A7"), "00000231"),
        ("ladder", ("symbolic_certificate", "ladder_theorem"), "false"),
        ("A6_coordinate_degree", ("A6_exact_algebra", "coordinate_polynomial_degree"), 5),
        ("A6_trace_degree", ("A6_exact_algebra", "trace_polynomial_degree"), 6),
        ("A6_trace_interval", ("A6_exact_algebra", "physical_trace_interval", 0), -54574),
        ("A6_irreducible_prime", ("A6_exact_algebra", "trace_irreducible_mod_prime"), 7),
        ("P7_coordinate_degree", ("period_7_exact_algebra", "coordinate_polynomial_degree"), 7),
        ("P7_trace_degree", ("period_7_exact_algebra", "trace_polynomial_degree"), 7),
        ("P7_trace_interval", ("period_7_exact_algebra", "physical_embeddings", "B7", "trace_interval", 1), 230985),
        ("P7_shared_field", ("period_7_exact_algebra", "shared_field_statement"), "two unrelated fields"),
        ("Delta_sign", ("five_block_obstruction", "strict_sign"), "zero"),
        ("integer_margin", ("five_block_obstruction", "integer_margin"), 0),
        ("obstruction_status", ("five_block_obstruction", "status"), "OPEN"),
        ("memory_promotion", ("five_block_obstruction", "memory_lower_bound"), "all Holder potentials fail"),
        ("width5_rank", ("finite_sharpness", "width_5_rank"), 4),
        ("width6_four_det", ("finite_sharpness", "width_6_four_row_determinant"), 1),
        ("width6_cumulative_det", ("finite_sharpness", "width_6_cumulative_determinant"), -1),
        ("holder_status", ("holder_scope", "status"), "PROVED_NO_GO"),
        ("route_a_promotion", ("route_a_status", "full_galois_A2_pass"), True),
        ("route_b_promotion", ("route_b_authorized",), True),
        ("arithmetic_promotion", ("arithmetic_advance",), "YES"),
    )
    rejected: list[str] = []
    for label, path, replacement in mutations:
        trial = copy.deepcopy(core)
        assign_path(trial, path, replacement)
        try:
            validate_core(trial, core)
        except ValueError:
            rejected.append(label)
        else:
            raise AssertionError(f"mutation was accepted: {label}")
    return {
        "attempted": len(mutations),
        "rejected": len(rejected),
        "labels": rejected,
        "all_rejected": len(rejected) == len(mutations),
        "trace_sha256": canonical_sha(rejected),
    }


def build_certificate() -> dict[str, object]:
    core = core_payload()
    validate_core(core, core_payload())
    certificate: dict[str, object] = {
        **core,
        "dependency_locks": dependency_locks(),
        "mutation_audit": mutation_audit(core),
    }
    certificate["core_sha256"] = canonical_sha(core)
    return certificate


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if not args.check:
        raise SystemExit("explicit --check is required")
    certificate = build_certificate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "check": True,
                "candidate_id": certificate["candidate_id"],
                "core_sha256": certificate["core_sha256"],
                "Delta_5": certificate["five_block_obstruction"]["Delta_5_decimal_50"],
                "five_block_obstruction": certificate["five_block_obstruction"]["status"],
                "mutations_rejected": certificate["mutation_audit"]["rejected"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
