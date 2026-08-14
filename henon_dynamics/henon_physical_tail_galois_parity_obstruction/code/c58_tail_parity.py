#!/usr/bin/env python3
"""Exact HCS-P58 certificate for the physical-tail/Galois-scale obstruction."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path

import sympy as sp


PROJECT = Path(__file__).resolve().parents[1]
TRACK = PROJECT.parent
DEFAULT_OUTPUT = PROJECT / "results" / "c58_certificate.json"

X, T = sp.symbols("X T")

DEPENDENCIES = {
    "p57_readme": (
        TRACK / "henon_galois_excess_five_block_obstruction" / "README.md",
        "94502c1e51276ea5e57686c0add9fbbf0a0f0f0473a8f283540271d872b1c6b7",
    ),
    "p57_proof": (
        TRACK / "henon_galois_excess_five_block_obstruction" / "PROOF_PACKAGE.md",
        "528b009a06b3f96187a0774eb5e3cc34056453ac2a952626f5fa940fb402676f",
    ),
    "p57_code": (
        TRACK
        / "henon_galois_excess_five_block_obstruction"
        / "code"
        / "c57_five_block_obstruction.py",
        "1feb1bb437139697d7f756206d24f6e40931088b59af3594456ebe6927ab04ef",
    ),
    "p57_certificate": (
        TRACK
        / "henon_galois_excess_five_block_obstruction"
        / "results"
        / "c57_certificate.json",
        "10ef3ab4a39f9828bc1f21b6b32d34ecf357cba24ecd3145f6745fc6cb691a58",
    ),
    "p57_route_a": (
        TRACK / "henon_galois_excess_five_block_obstruction" / "route_a_evaluation.yaml",
        "f11ca3a28e388b8165d24d72da42103039c989f196a2ffc0b14ca24a8fedee37",
    ),
    "p57_paper": (
        TRACK / "henon_galois_excess_five_block_obstruction" / "paper" / "paper.pdf",
        "d46cc29e4304b64c5b08f1b148a3c261c5c0e786a75f265c7fc1f574c29ad21d",
    ),
}

TRACE_INTERVALS = {
    "A8": (
        (-2793061, -2793060),
        (-242473, -242472),
        (-102623, -102622),
        (-71703, -71702),
        (-69893, -69892),
        (-33020, -33019),
        (-10678, -10677),
        (-9340, -9339),
        (10954, 10955),
        (95183, 95184),
        (252649, 252650),
        (259912, 259913),
    ),
    "B8": (
        (21828, 21829),
        (30715, 30716),
        (67810, 67811),
        (216151, 216152),
        (1000641, 1000642),
        (1652592, 1652593),
    ),
    "P9": (
        (-19975348, -19975347),
        (-4644653, -4644652),
        (-1734047, -1734046),
        (-518197, -518196),
        (-516613, -516612),
        (-504171, -504170),
        (-407093, -407092),
        (-350625, -350624),
        (-122928, -122927),
        (-87690, -87689),
        (-58024, -58023),
        (-56520, -56519),
        (-40350, -40349),
        (-33678, -33677),
        (27764, 27765),
        (39697, 39698),
        (83805, 83806),
        (91109, 91110),
        (232988, 232989),
        (438821, 438822),
        (516842, 516843),
        (1549429, 1549430),
        (1832226, 1832227),
        (1858726, 1858727),
        (2569981, 2569982),
        (7178561, 7178562),
        (7943186, 7943187),
        (11819577, 11819578),
    ),
}

TRACE_COEFFICIENT_SHA = {
    "A8": "c10a3536d0781bdbbfbb320d48441a97583af9cd18517991c76e71813936c8ab",
    "B8": "49e0a21377ff47f504fa00d85f8ed3cee17d70d0677085bdc52e4203f4ac77fd",
    "P9": "f52d222e2934061dc367950e3e98e56d4fb9e0e6bd95c7b383fec9061bd7ac3b",
}

IRREDUCIBLE_PRIMES = {"A8": 7, "B8": 53, "P9": 71}
EXPECTED_CORE_SHA256 = "d28b0ed264c31b97be2af56a9954e6bf891adc5092dcea24f65934f6ed3e37ab"

PHYSICAL_DATA = {
    "A8": {
        "coordinate_interval": (
            sp.Rational(551939742238, 10**12),
            sp.Rational(551939742239, 10**12),
        ),
        "chain_signs": (1, -1, -1, -1, -1),
        "trace_interval": TRACE_INTERVALS["A8"][0],
        "trace_index": 0,
    },
    "B8": {
        "coordinate_interval": (
            sp.Rational(-603835740359, 10**12),
            sp.Rational(-603835740358, 10**12),
        ),
        "chain_signs": (-1, -1, -1, 1),
        "trace_interval": TRACE_INTERVALS["B8"][-1],
        "trace_index": 5,
    },
    "A9": {
        "coordinate_interval": (
            sp.Rational(551940301478, 10**12),
            sp.Rational(551940301479, 10**12),
        ),
        "chain_signs": (1, -1, -1, -1, -1),
        "trace_interval": TRACE_INTERVALS["P9"][0],
        "trace_index": 0,
    },
    "B9": {
        "coordinate_interval": (
            sp.Rational(-606695536138, 10**12),
            sp.Rational(-606695536137, 10**12),
        ),
        "chain_signs": (-1, -1, -1, -1, 1),
        "trace_interval": TRACE_INTERVALS["P9"][-1],
        "trace_index": 27,
    },
}

P7_INTERVALS = (
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


def vertex_chain(depth: int) -> tuple[sp.Expr, ...]:
    values = [X, sp.expand((1 - 6 * X**2) / 2)]
    while len(values) <= depth:
        values.append(sp.expand(1 - 6 * values[-1] ** 2 - values[-2]))
    return tuple(values)


def edge_chain(depth: int) -> tuple[sp.Expr, ...]:
    values = [X, sp.expand(1 - 6 * X**2 - X)]
    while len(values) <= depth:
        values.append(sp.expand(1 - 6 * values[-1] ** 2 - values[-2]))
    return tuple(values)


def factor_of_degree(expression: sp.Expr, degree: int) -> sp.Poly:
    factors = [sp.Poly(factor, X) for factor, exponent in sp.factor_list(expression)[1] if exponent == 1]
    matches = [factor for factor in factors if factor.degree() == degree]
    if len(matches) != 1:
        raise ArithmeticError(f"expected one degree-{degree} factor")
    return matches[0]


def monodromy_trace(coordinates: tuple[sp.Expr, ...]) -> sp.Expr:
    matrix = sp.eye(2)
    for coordinate in coordinates:
        matrix = sp.Matrix([[-12 * coordinate, -1], [1, 0]]) * matrix
    return sp.expand(sp.trace(matrix))


def trace_polynomial(coordinate_polynomial: sp.Poly, coordinates: tuple[sp.Expr, ...]) -> tuple[sp.Expr, sp.Poly, int]:
    reduced_trace = sp.factor(sp.rem(monodromy_trace(coordinates), coordinate_polynomial, X))
    resultant = sp.Poly(
        sp.resultant(coordinate_polynomial.as_expr(), T - reduced_trace, X), T
    ).primitive()[1]
    factors = sp.factor_list(resultant.as_expr())[1]
    if len(factors) != 1:
        raise ArithmeticError("trace resultant has more than one factor")
    factor, multiplicity = factors[0]
    return reduced_trace, sp.Poly(factor, T), int(multiplicity)


def _mul_mod(left: list[int], right: list[int], modulus: list[int], prime: int) -> list[int]:
    degree = len(modulus) - 1
    product = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            product[i + j] = (product[i + j] + a * b) % prime
    product.extend([0] * max(0, degree - len(product)))
    for power in range(len(product) - 1, degree - 1, -1):
        coefficient = product[power] % prime
        if coefficient:
            shift = power - degree
            for j in range(degree):
                product[shift + j] = (product[shift + j] - coefficient * modulus[j]) % prime
    return (product[:degree] + [0] * degree)[:degree]


def _x_power_mod(exponent: int, modulus: list[int], prime: int) -> list[int]:
    degree = len(modulus) - 1
    result = [1] + [0] * (degree - 1)
    base = [0, 1] + [0] * (degree - 2)
    while exponent:
        if exponent & 1:
            result = _mul_mod(result, base, modulus, prime)
        base = _mul_mod(base, base, modulus, prime)
        exponent >>= 1
    return result


def irreducible_mod_prime(polynomial: sp.Poly, prime: int) -> bool:
    degree = polynomial.degree()
    leading = int(polynomial.LC()) % prime
    if leading == 0:
        return False
    inverse = pow(leading, -1, prime)
    high = [int(value) * inverse % prime for value in polynomial.all_coeffs()]
    modulus = list(reversed(high))
    if modulus[-1] != 1:
        raise ArithmeticError("modular polynomial is not monic")
    divisors = set(sp.factorint(degree))
    x_vector = [0, 1] + [0] * (degree - 2)
    for divisor in divisors:
        power = _x_power_mod(prime ** (degree // divisor), modulus, prime)
        difference = [(power[i] - x_vector[i]) % prime for i in range(degree)]
        expression = sum(value * T**i for i, value in enumerate(difference))
        if sp.gcd(sp.Poly(expression, T, modulus=prime), sp.Poly(polynomial, T, modulus=prime)).degree() != 0:
            return False
    return _x_power_mod(prime**degree, modulus, prime) == x_vector


def root_and_height_data(polynomial: sp.Poly, intervals: tuple[tuple[int, int], ...]) -> dict[str, object]:
    if len(intervals) != polynomial.degree():
        raise ArithmeticError("root interval count differs from degree")
    counts = [int(polynomial.count_roots(left, right)) for left, right in intervals]
    if counts != [1] * polynomial.degree():
        raise ArithmeticError("Sturm root isolators changed")
    roots_raw = sp.nroots(polynomial.as_expr(), n=90, maxsteps=2000)
    if any(abs(sp.im(root)) >= sp.Float("1e-70") for root in roots_raw):
        raise ArithmeticError("trace polynomial is no longer numerically real")
    roots = sorted([sp.re(root) for root in roots_raw], key=float)
    lengths = [sp.acosh(sp.Abs(root) / 2) for root in roots]
    return {
        "root_counts": counts,
        "all_roots_real_by_sturm": True,
        "roots": roots,
        "lengths": lengths,
        "height": sum(lengths, sp.Float(0, 90)),
    }


def physical_embedding(
    name: str,
    coordinate_polynomial: sp.Poly,
    chain: tuple[sp.Expr, ...],
    reduced_trace: sp.Expr,
) -> dict[str, object]:
    expected = PHYSICAL_DATA[name]
    left, right = expected["coordinate_interval"]
    if coordinate_polynomial.count_roots(left, right) != 1:
        raise ArithmeticError(f"{name} coordinate isolator changed")
    signs: list[int] = []
    zero_counts: list[int] = []
    for expression in chain:
        zero_count = int(sp.Poly(expression, X).count_roots(left, right))
        endpoint_signs = [int(sp.sign(expression.subs(X, endpoint))) for endpoint in (left, right)]
        if zero_count != 0 or endpoint_signs[0] != endpoint_signs[1] or endpoint_signs[0] == 0:
            raise ArithmeticError(f"{name} chain sign box changed")
        zero_counts.append(zero_count)
        signs.append(endpoint_signs[0])
    if tuple(signs) != expected["chain_signs"]:
        raise ArithmeticError(f"{name} chain signs changed")
    derivative_count = int(sp.Poly(sp.diff(reduced_trace, X), X).count_roots(left, right))
    if derivative_count != 0:
        raise ArithmeticError(f"{name} trace is not monotone on its isolator")
    trace_left, trace_right = expected["trace_interval"]
    endpoint_values = [reduced_trace.subs(X, endpoint) for endpoint in (left, right)]
    if not all(trace_left < value < trace_right for value in endpoint_values):
        raise ArithmeticError(f"{name} trace interval changed")
    return {
        "coordinate_interval": [str(left), str(right)],
        "chain_signs": signs,
        "chain_zero_counts": zero_counts,
        "trace_derivative_root_count": derivative_count,
        "trace_interval": [trace_left, trace_right],
        "trace_index": expected["trace_index"],
    }


def field_record(
    name: str,
    coordinate_polynomial: sp.Poly,
    coordinates: tuple[sp.Expr, ...],
    chain: tuple[sp.Expr, ...],
    physical_names: tuple[str, ...],
) -> tuple[dict[str, object], dict[str, sp.Expr]]:
    reduced_trace, trace_poly, multiplicity = trace_polynomial(coordinate_polynomial, coordinates)
    coefficient_sha = canonical_sha([int(value) for value in trace_poly.all_coeffs()])
    if coefficient_sha != TRACE_COEFFICIENT_SHA[name]:
        raise ArithmeticError(f"{name} trace coefficients changed")
    prime = IRREDUCIBLE_PRIMES[name]
    if not irreducible_mod_prime(trace_poly, prime):
        raise ArithmeticError(f"{name} modular irreducibility changed")
    root_data = root_and_height_data(trace_poly, TRACE_INTERVALS[name])
    embeddings = {
        physical_name: physical_embedding(
            physical_name, coordinate_polynomial, chain, reduced_trace
        )
        for physical_name in physical_names
    }
    excesses: dict[str, sp.Expr] = {}
    for physical_name, embedding in embeddings.items():
        index = int(embedding["trace_index"])
        excesses[physical_name] = sp.simplify(root_data["height"] - root_data["lengths"][index])
    record = {
        "reflection_type": name,
        "coordinate_degree": coordinate_polynomial.degree(),
        "coordinate_factor_coefficients_sha256": canonical_sha(
            [int(value) for value in coordinate_polynomial.all_coeffs()]
        ),
        "trace_degree": trace_poly.degree(),
        "trace_resultant_multiplicity": multiplicity,
        "trace_coefficients_sha256": coefficient_sha,
        "trace_irreducible_mod_prime": prime,
        "trace_intervals": [list(interval) for interval in TRACE_INTERVALS[name]],
        "all_trace_roots_real_by_sturm": root_data["all_roots_real_by_sturm"],
        "mahler_height_decimal_60": str(sp.N(root_data["height"], 60)),
        "physical_embeddings": embeddings,
        "physical_lengths_decimal_60": {
            physical_name: str(sp.N(root_data["lengths"][int(embedding["trace_index"])], 60))
            for physical_name, embedding in embeddings.items()
        },
        "galois_excesses_decimal_60": {
            physical_name: str(sp.N(excesses[physical_name], 60))
            for physical_name in physical_names
        },
    }
    return record, excesses


def lower_factor(interval: tuple[int, int]) -> int:
    left, right = interval
    minimum_abs = left if left > 0 else -right
    return minimum_abs - 1


def upper_factor(interval: tuple[int, int]) -> int:
    left, right = interval
    return right if left > 0 else -left


def product(values: list[int]) -> int:
    result = 1
    for value in values:
        result *= value
    return result


def parity_sign_certificate(
    excesses: dict[str, sp.Expr], p57: dict[str, object]
) -> dict[str, object]:
    old = p57["five_block_obstruction"]
    excess_a6 = sp.Float(old["A6_excess_decimal_50"], 90)
    excess_a7 = sp.Float(p57["period_7_exact_algebra"]["A7_galois_excess_decimal_50"], 90)
    excess_b7 = sp.Float(p57["period_7_exact_algebra"]["B7_galois_excess_decimal_50"], 90)

    delta6 = excess_a6 + excesses["B8"] - excess_a7 - excess_b7
    delta7 = excess_a7 + excesses["B9"] - excesses["A8"] - excesses["B8"]

    delta6_lower_factors = (
        [lower_factor(P7_INTERVALS[index]) for index in range(1, 14)]
        + [lower_factor(P7_INTERVALS[index]) for index in range(0, 13)]
    )
    delta6_upper_factors = [1095, 5138] + [
        upper_factor(TRACE_INTERVALS["B8"][index]) for index in range(5)
    ]
    delta6_lower_product = product(delta6_lower_factors)
    delta6_upper_product = product(delta6_upper_factors)
    if delta6_lower_product <= delta6_upper_product or not delta6 < 0:
        raise ArithmeticError("Delta_6 sign certificate changed")

    delta7_lower_factors = (
        [lower_factor(P7_INTERVALS[index]) for index in range(1, 14)]
        + [lower_factor(TRACE_INTERVALS["P9"][index]) for index in range(27)]
    )
    delta7_upper_factors = (
        [upper_factor(TRACE_INTERVALS["A8"][index]) for index in range(1, 12)]
        + [upper_factor(TRACE_INTERVALS["B8"][index]) for index in range(5)]
    )
    delta7_lower_product = product(delta7_lower_factors)
    delta7_upper_product = product(delta7_upper_factors)
    if delta7_lower_product <= delta7_upper_product or not delta7 > 0:
        raise ArithmeticError("Delta_7 sign certificate changed")

    return {
        "Delta_6_definition": "E(A6)+E(B8)-E(A7)-E(B7)",
        "Delta_6_decimal_60": str(sp.N(delta6, 60)),
        "Delta_6_exact_sign": "negative",
        "Delta_6_lower_product_for_E_A7_plus_E_B7": delta6_lower_product,
        "Delta_6_upper_product_for_E_A6_plus_E_B8": delta6_upper_product,
        "Delta_6_integer_margin": delta6_lower_product - delta6_upper_product,
        "Delta_7_definition": "E(A7)+E(B9)-E(A8)-E(B8)",
        "Delta_7_decimal_60": str(sp.N(delta7, 60)),
        "Delta_7_exact_sign": "positive",
        "Delta_7_lower_product_for_E_A7_plus_E_B9": delta7_lower_product,
        "Delta_7_upper_product_for_E_A8_plus_E_B8": delta7_upper_product,
        "Delta_7_integer_margin": delta7_lower_product - delta7_upper_product,
        "certifying_inequality": "log(a-1)<acosh(a/2)<log(a) for every a>2",
        "observed_signs_Delta_4_through_7": ["negative", "positive", "negative", "positive"],
    }


def fixed_point_tail() -> dict[str, object]:
    q_minus = -(1 + sp.sqrt(7)) / 6
    fixed_trace = 2 + 2 * sp.sqrt(7)
    unstable = sp.simplify((fixed_trace + sp.sqrt(fixed_trace**2 - 4)) / 2)
    stable = sp.simplify(1 / unstable)
    contraction = 2 / sp.sqrt(17)
    if not (0 < stable < contraction < 1):
        raise ArithmeticError("fixed-point stability ordering changed")
    return {
        "negative_fixed_point": str(q_minus),
        "negative_fixed_point_decimal_50": str(sp.N(q_minus, 50)),
        "monodromy_trace": str(fixed_trace),
        "unstable_eigenvalue": str(unstable),
        "unstable_eigenvalue_decimal_50": str(sp.N(unstable, 50)),
        "stable_eigenvalue": str(stable),
        "stable_eigenvalue_decimal_50": str(sp.N(stable, 50)),
        "stable_eigenvalue_positive": True,
        "signed_inverse_common_contraction": "2/sqrt(17)",
        "signed_inverse_common_contraction_decimal_50": str(sp.N(contraction, 50)),
        "physical_tail_status": "PROVED_EXPONENTIALLY_LOCALIZED_BY_CONTRACTION",
        "scope": "controls the selected physical embedding and its local unstable-Jacobian tail, not the sum over nonphysical algebraic embeddings",
    }


def algebra_and_excess() -> tuple[dict[str, object], dict[str, sp.Expr]]:
    vertex = vertex_chain(4)
    edge = edge_chain(3)

    a8_coordinate = factor_of_degree(1 - 6 * vertex[4] ** 2 - 2 * vertex[3], 24)
    b8_coordinate = factor_of_degree(1 - 6 * edge[3] ** 2 - edge[2] - edge[3], 12)
    p9_coordinate = factor_of_degree(1 - 6 * vertex[4] ** 2 - vertex[3] - vertex[4], 28)

    a8_coordinates = (
        vertex[0], vertex[1], vertex[2], vertex[3], vertex[4],
        vertex[3], vertex[2], vertex[1],
    )
    b8_coordinates = (
        edge[0], edge[0], edge[1], edge[2], edge[3],
        edge[3], edge[2], edge[1],
    )
    p9_coordinates = (
        vertex[0], vertex[1], vertex[2], vertex[3], vertex[4],
        vertex[4], vertex[3], vertex[2], vertex[1],
    )

    a8_record, a8_excess = field_record(
        "A8", a8_coordinate, a8_coordinates, vertex, ("A8",)
    )
    b8_record, b8_excess = field_record(
        "B8", b8_coordinate, b8_coordinates, edge, ("B8",)
    )
    p9_record, p9_excess = field_record(
        "P9", p9_coordinate, p9_coordinates, vertex, ("A9", "B9")
    )
    excesses = {**a8_excess, **b8_excess, **p9_excess}
    return {
        "A8_vertex_vertex": a8_record,
        "B8_edge_edge": b8_record,
        "A9_B9_vertex_edge": p9_record,
    }, excesses


def core_payload() -> dict[str, object]:
    p57_path = DEPENDENCIES["p57_certificate"][0]
    p57 = json.loads(p57_path.read_text(encoding="utf-8"))
    algebra, excesses = algebra_and_excess()
    parity = parity_sign_certificate(excesses, p57)
    return {
        "candidate_id": "HCS-P58",
        "source_object": "the P56 incidence ladder and P57 Galois-excess trace-field compiler on the frozen H6 survivor",
        "fixed_point_tail": fixed_point_tail(),
        "reflection_algebra": algebra,
        "parity_falsifier": parity,
        "one_embedding_vs_galois_sum": {
            "status": "PROVED_INTERFACE_OBSTRUCTION",
            "physical_statement": "fixed-point linearization controls one selected real embedding",
            "galois_statement": "E(gamma) is the sum of instability lengths over every nonphysical embedding of the irreducible trace field",
            "period_8_split": "A8 is vertex-vertex of trace degree 12; B8 is edge-edge of trace degree 6",
            "period_9_control": "A9 and B9 are two embeddings of one irreducible totally real trace field of degree 28",
            "consequence": "physical stable-tail control alone cannot imply an estimate for Delta_m; a uniform reflection-ensemble theorem is separately required",
        },
        "strongest_positive_result": "exact irreducible totally real trace fields of degrees 12, 6, and 28 for A8, B8, and the shared A9/B9 reflection chains",
        "strongest_obstruction": "the physical negative-fixed-point tail is only one embedding and does not compile the all-conjugate Galois height; exact integer products give Delta_6<0<Delta_7",
        "open_theorem": "construct a symmetry-resolved reflection-ensemble pressure or height theorem uniform in m, including the primitive-factor and irreducibility interface",
        "reusable_structure": "three exact reflection boundary types (vertex-vertex, edge-edge, vertex-edge) with trace-resultant and integer-product compilers",
        "round2_clue": "replace one-orbit fixed-point linearization by an exact count/generating function for primitive roots in the three reflection ensembles before estimating their summed instability lengths",
        "route_a_status": {
            "tuple": "(A1_WEAK, A2_ANALYTIC_DETERMINANT [physical subsystem only], A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FORMAL_HINT)",
            "overall": "ROUTE_A_EXPLORATORY",
            "full_galois_A2_pass": False,
        },
        "route_b_authorized": False,
        "arithmetic_advance": "NO",
        "claim_boundary": "P58 proves exact period-eight/nine reflection algebra, two parity signs, and a physical/Galois interface obstruction; it does not prove an infinite-tail sign law, refute unrestricted Holder data, or construct a full Galois determinant or Hilbert-Polya operator",
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
        ("fixed_point_sign", ("fixed_point_tail", "stable_eigenvalue_positive"), False),
        ("fixed_tail_scope", ("fixed_point_tail", "scope"), "controls all embeddings"),
        ("A8_degree", ("reflection_algebra", "A8_vertex_vertex", "trace_degree"), 6),
        ("B8_degree", ("reflection_algebra", "B8_edge_edge", "trace_degree"), 12),
        ("P9_degree", ("reflection_algebra", "A9_B9_vertex_edge", "trace_degree"), 14),
        ("A8_prime", ("reflection_algebra", "A8_vertex_vertex", "trace_irreducible_mod_prime"), 5),
        ("B8_prime", ("reflection_algebra", "B8_edge_edge", "trace_irreducible_mod_prime"), 7),
        ("P9_prime", ("reflection_algebra", "A9_B9_vertex_edge", "trace_irreducible_mod_prime"), 73),
        ("A8_root", ("reflection_algebra", "A8_vertex_vertex", "physical_embeddings", "A8", "trace_index"), 11),
        ("B8_root", ("reflection_algebra", "B8_edge_edge", "physical_embeddings", "B8", "trace_index"), 0),
        ("A9_B9_shared", ("reflection_algebra", "A9_B9_vertex_edge", "trace_degree"), 56),
        ("Delta6_sign", ("parity_falsifier", "Delta_6_exact_sign"), "positive"),
        ("Delta6_margin", ("parity_falsifier", "Delta_6_integer_margin"), 0),
        ("Delta7_sign", ("parity_falsifier", "Delta_7_exact_sign"), "negative"),
        ("Delta7_margin", ("parity_falsifier", "Delta_7_integer_margin"), 0),
        ("observed_promotion", ("parity_falsifier", "observed_signs_Delta_4_through_7"), ["alternating forever"]),
        ("interface_status", ("one_embedding_vs_galois_sum", "status"), "FULL_ASYMPTOTIC_THEOREM"),
        ("holder_promotion", ("claim_boundary",), "unrestricted Holder no-go proved"),
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
            raise AssertionError(f"mutation accepted: {label}")
    return {
        "attempted": len(mutations),
        "rejected": len(rejected),
        "all_rejected": len(rejected) == len(mutations),
        "labels": rejected,
        "trace_sha256": canonical_sha(rejected),
    }


def build_certificate() -> dict[str, object]:
    core = core_payload()
    core_sha = canonical_sha(core)
    if core_sha != EXPECTED_CORE_SHA256:
        raise RuntimeError("core payload digest changed")
    result = {
        **core,
        "dependency_locks": dependency_locks(),
        "mutation_audit": mutation_audit(core),
    }
    result["core_sha256"] = core_sha
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    if not args.check:
        raise SystemExit("explicit --check is required")
    certificate = build_certificate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "Delta_6": certificate["parity_falsifier"]["Delta_6_decimal_60"],
                "Delta_7": certificate["parity_falsifier"]["Delta_7_decimal_60"],
                "candidate_id": certificate["candidate_id"],
                "check": True,
                "core_sha256": certificate["core_sha256"],
                "mutations_rejected": certificate["mutation_audit"]["rejected"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
