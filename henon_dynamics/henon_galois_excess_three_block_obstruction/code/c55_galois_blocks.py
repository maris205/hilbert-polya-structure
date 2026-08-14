#!/usr/bin/env python3
"""Exact HCS-P55 certificate for the three-block Galois-excess obstruction."""

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
DEFAULT_OUTPUT = PROJECT / "results" / "c55_certificate.json"

X, T, Z = sp.symbols("X T Z")
STATE_LABELS = ("--", "-+", "+-", "++")
ADJACENCY = (
    (1, 0, 1, 0),
    (1, 0, 0, 0),
    (0, 1, 0, 1),
    (0, 1, 0, 0),
)

DEPENDENCIES = {
    "c31_readme": (
        TRACK / "henon_bowen_pressure_gate" / "README.md",
        "49b2d14684d868c38e2017f44cb766bfd035a7f716d9fe442e6174c4c7327eaa",
    ),
    "c31_certificate": (
        TRACK / "henon_bowen_pressure_gate" / "results" / "c31_certificate.json",
        "9f326c8442f5f1dfb8215527491a9ebbac2395fde7892c88bc78634df24c5cca",
    ),
    "c48_readme": (
        TRACK / "henon_pressure_label_six_exponentials_obstruction" / "README.md",
        "5e292ff19c65d7878326c68cf937d86cbdb1bc5be1abd47e93c4e243c43fe108",
    ),
    "c48_certificate": (
        TRACK
        / "henon_pressure_label_six_exponentials_obstruction"
        / "results"
        / "c48_certificate.json",
        "7134167226aa6bd22596675bf21826b8303a2a731f087d6ad7405d7137a51234",
    ),
    "c54_readme": (
        TRACK / "henon_mahler_pressure_pole_galois_excess_gate" / "README.md",
        "6de8713f03a3cde956b425f5b4a51e87b8b01a0ac32497facc57ef7a70ffde65",
    ),
    "c54_certificate": (
        TRACK
        / "henon_mahler_pressure_pole_galois_excess_gate"
        / "results"
        / "c54_certificate.json",
        "d6932d0b24111866253508b5dd7c33972856cfdbddd5dfdd7db77a92a38f233c",
    ),
    "certified_orbit_catalog": (
        TRACK / "henon_instability_roof_zeta" / "results" / "catalog_validation.json",
        "0eab1930a17e4315e59eebc9dc7d3ef111b674d3625f09ca3396c1aa7c814fde",
    ),
    "exact_algebra_appendix": (
        TRACK / "henon_instability_roof_zeta" / "paper" / "sections" / "A_exact_algebra.tex",
        "bd9b6c20aad7358f33d18a01ee9d206c3534892f667dc8f2d3e57dfc5c9e24dc",
    ),
}


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


def primitive_cycles(max_period: int = 5) -> dict[int, list[tuple[int, ...]]]:
    result: dict[int, list[tuple[int, ...]]] = {}
    for n in range(1, max_period + 1):
        found: set[tuple[int, ...]] = set()
        for word in itertools.product(range(4), repeat=n):
            if not all(ADJACENCY[word[i]][word[(i + 1) % n]] for i in range(n)):
                continue
            if not primitive(word):
                continue
            found.add(min(rotations(word)))
        result[n] = sorted(found)
    return result


def block_counter(word: tuple[int, ...], width: int) -> dict[tuple[int, ...], int]:
    result: dict[tuple[int, ...], int] = {}
    for i in range(len(word)):
        block = tuple(word[(i + j) % len(word)] for j in range(width))
        result[block] = result.get(block, 0) + 1
    return result


def common_incidence(
    words: list[tuple[int, ...]], width: int
) -> tuple[list[tuple[int, ...]], sp.Matrix]:
    counters = [block_counter(word, width) for word in words]
    blocks = sorted({block for counter in counters for block in counter})
    matrix = sp.Matrix([[counter.get(block, 0) for block in blocks] for counter in counters])
    return blocks, matrix


def derivative(q: sp.Expr) -> sp.Matrix:
    return sp.Matrix([[-12 * q, -1], [1, 0]])


def monodromy(coordinates: tuple[sp.Expr, ...]) -> sp.Matrix:
    result = sp.eye(2)
    for coordinate in coordinates:
        result = derivative(coordinate) * result
    return result.applyfunc(sp.simplify)


def recurrence_residuals(coordinates: tuple[sp.Expr, ...]) -> tuple[sp.Expr, ...]:
    n = len(coordinates)
    return tuple(
        sp.simplify(
            1
            - 6 * coordinates[i] ** 2
            - coordinates[(i - 1) % n]
            - coordinates[(i + 1) % n]
        )
        for i in range(n)
    )


def exact_orbit_algebra() -> dict[str, object]:
    sqrt6 = sp.sqrt(6)
    a4 = -sp.sqrt((3 + sqrt6) / 18)
    b4 = -sqrt6 / 6
    p4a_coordinates = (a4, b4, -a4, b4)
    p4a_matrix = monodromy(p4a_coordinates)
    p4a_trace = sp.simplify(sp.trace(p4a_matrix))
    if p4a_trace != -574 - 192 * sqrt6:
        raise ArithmeticError("period-four-a trace mismatch")
    if any(recurrence_residuals(p4a_coordinates)):
        raise ArithmeticError("period-four-a recurrence mismatch")
    p4a_abs_trace = 574 + 192 * sqrt6
    p4a_multiplier = sp.simplify(
        (p4a_abs_trace + sp.sqrt(p4a_abs_trace**2 - 4)) / 2
    )
    p4a_minpoly = sp.Poly(sp.minimal_polynomial(p4a_multiplier, X), X)
    expected_p4a_minpoly = sp.Poly(X**4 - 1148 * X**3 + 108294 * X**2 - 1148 * X + 1, X)
    if p4a_minpoly != expected_p4a_minpoly:
        raise ArithmeticError("period-four-a multiplier polynomial mismatch")

    p4a_conjugate_half_trace = 287 - 96 * sqrt6
    p4a_excess = sp.acosh(p4a_conjugate_half_trace)
    p3_excess = sp.acosh(21 * sp.sqrt(5) - 19)
    if not (
        96**2 * 6 - 235**2 == 71
        and 236**2 - 96**2 * 6 == 400
        and 47**2 - 21**2 * 5 == 4
    ):
        raise ArithmeticError("surds inequality witness mismatch")

    x = X
    b5 = sp.expand((1 - 6 * x**2) / 2)
    c5 = sp.expand(1 - 6 * b5**2 - x)
    coordinate_polynomial = sp.Poly(
        5832 * x**6
        - 1944 * x**5
        - 2268 * x**4
        + 648 * x**3
        + 144 * x**2
        - 12 * x
        - 1,
        x,
    )
    closing_polynomial = sp.factor(6 * c5**2 + b5 + c5 - 1)
    expected_closing = sp.factor((6 * x**2 + 2 * x - 1) * coordinate_polynomial.as_expr() / 2)
    if sp.expand(closing_polynomial - expected_closing) != 0:
        raise ArithmeticError("period-five closing factorization mismatch")
    residuals_mod_coordinate = (
        sp.rem(sp.together(b5 - (1 - 6 * x**2 - b5)).as_numer_denom()[0], coordinate_polynomial, x),
        sp.rem(sp.together(c5 - (1 - 6 * b5**2 - x)).as_numer_denom()[0], coordinate_polynomial, x),
        sp.rem(sp.together(c5 - (1 - 6 * c5**2 - b5)).as_numer_denom()[0], coordinate_polynomial, x),
        sp.rem(sp.together(b5 - (1 - 6 * c5**2 - c5)).as_numer_denom()[0], coordinate_polynomial, x),
        sp.rem(sp.together(x - (1 - 6 * b5**2 - c5)).as_numer_denom()[0], coordinate_polynomial, x),
    )
    if any(residual.as_expr() != 0 for residual in residuals_mod_coordinate):
        raise ArithmeticError("period-five recurrence failed modulo its coordinate polynomial")

    p5_matrix = monodromy((x, b5, c5, c5, b5))
    p5_trace_raw = sp.trace(p5_matrix)
    numerator, denominator = sp.together(p5_trace_raw).as_numer_denom()
    p5_trace_reduced = sp.factor(sp.rem(numerator, coordinate_polynomial, x) / denominator)
    expected_trace_reduced = -4 * (
        174960 * x**5
        - 6804 * x**4
        - 53136 * x**3
        + 4050 * x**2
        + 2457 * x
        - 76
    )
    if sp.expand(p5_trace_reduced - expected_trace_reduced) != 0:
        raise ArithmeticError("period-five reduced trace mismatch")

    trace_resultant = sp.resultant(
        coordinate_polynomial.as_expr(),
        sp.together(T - p5_trace_reduced).as_numer_denom()[0],
        x,
    )
    trace_primitive = sp.Poly(trace_resultant, T).primitive()[1]
    trace_polynomial = sp.Poly(
        T**6
        + 3300 * T**5
        - 34165368 * T**4
        - 7291075328 * T**3
        + 26529205510272 * T**2
        + 3609165326736384 * T
        - 4266315336505009664,
        T,
    )
    if trace_primitive != trace_polynomial:
        raise ArithmeticError("period-five trace polynomial mismatch")
    if sp.factor_list(trace_polynomial.as_expr())[1] != [(trace_polynomial.as_expr(), 1)]:
        raise ArithmeticError("period-five trace polynomial is reducible")

    trace_intervals = [
        (-7607, -7606),
        (-711, -710),
        (-590, -589),
        (390, 391),
        (770, 771),
        (4445, 4446),
    ]
    root_counts = [int(trace_polynomial.count_roots(left, right)) for left, right in trace_intervals]
    if root_counts != [1] * 6:
        raise ArithmeticError("period-five real-root isolation mismatch")

    coordinate_interval = (sp.Rational(-279433, 500000), sp.Rational(-111773, 200000))
    if coordinate_polynomial.count_roots(*coordinate_interval) != 1:
        raise ArithmeticError("physical period-five coordinate was not isolated")
    coordinate_midpoint = sum(coordinate_interval, sp.Rational(0)) / 2
    derivative_rows = {
        "b": sp.Poly(sp.diff(b5, x), x),
        "c": sp.Poly(sp.diff(c5, x), x),
        "trace": sp.Poly(sp.diff(p5_trace_reduced, x), x),
    }
    derivative_root_counts = {
        name: int(row.count_roots(*coordinate_interval))
        for name, row in derivative_rows.items()
    }
    derivative_midpoint_signs = {
        name: int(sp.sign(row.as_expr().subs(x, coordinate_midpoint)))
        for name, row in derivative_rows.items()
    }
    if derivative_root_counts != {"b": 0, "c": 0, "trace": 0}:
        raise ArithmeticError("physical period-five monotonicity was not isolated")
    if derivative_midpoint_signs != {"b": 1, "c": 1, "trace": -1}:
        raise ArithmeticError("physical period-five monotonicity signs changed")
    if not (
        coordinate_interval[1] < 0
        and b5.subs(x, coordinate_interval[0]) < 0
        and b5.subs(x, coordinate_interval[1]) < 0
        and c5.subs(x, coordinate_interval[0]) > 0
        and c5.subs(x, coordinate_interval[1]) > 0
    ):
        raise ArithmeticError("physical period-five symbolic sign word changed")
    trace_at_left = sp.simplify(p5_trace_reduced.subs(x, coordinate_interval[0]))
    trace_at_right = sp.simplify(p5_trace_reduced.subs(x, coordinate_interval[1]))
    if not (4445 < trace_at_right < trace_at_left < 4446):
        raise ArithmeticError("physical period-five trace interval mismatch")

    multiplier_resultant = sp.resultant(
        trace_polynomial.as_expr(), T - (Z + 1 / Z), T
    ) * Z**6
    multiplier_polynomial = sp.Poly(sp.expand(multiplier_resultant), Z)
    expected_multiplier = sp.Poly(
        Z**12
        + 3300 * Z**11
        - 34165362 * Z**10
        - 7291058828 * Z**9
        + 26529068848815 * Z**8
        + 3609143453543400 * Z**7
        - 4266262278298981308 * Z**6
        + 3609143453543400 * Z**5
        + 26529068848815 * Z**4
        - 7291058828 * Z**3
        - 34165362 * Z**2
        + 3300 * Z
        + 1,
        Z,
    )
    if multiplier_polynomial != expected_multiplier:
        raise ArithmeticError("period-five multiplier polynomial mismatch")
    if sp.factor_list(multiplier_polynomial.as_expr())[1] != [(multiplier_polynomial.as_expr(), 1)]:
        raise ArithmeticError("period-five multiplier polynomial is reducible")

    numeric_trace_roots = sorted(
        [sp.re(root) for root in sp.nroots(trace_polynomial.as_expr(), n=80, maxsteps=500)],
        key=lambda value: float(value),
    )
    reciprocal_pair_logs = [sp.acosh(sp.Abs(root) / 2) for root in numeric_trace_roots]
    p5_height = sum(reciprocal_pair_logs, sp.Float(0, 80))
    p5_physical_length = reciprocal_pair_logs[-1]
    p5_excess = p5_height - p5_physical_length

    return {
        "period_4a": {
            "coordinates": [str(sp.simplify(value)) for value in p4a_coordinates],
            "state_word": ["--", "--", "+-", "-+"],
            "trace": str(p4a_trace),
            "determinant": str(sp.simplify(p4a_matrix.det())),
            "multiplier_minimal_polynomial": str(p4a_minpoly.as_expr()),
            "galois_excess_formula": "acosh(287-96*sqrt(6))",
            "galois_excess_decimal_50": str(sp.N(p4a_excess, 50)),
        },
        "period_5": {
            "state_word": ["--", "--", "+-", "++", "-+"],
            "coordinate_pattern": ["a", "b", "c", "c", "b"],
            "b_as_polynomial_in_a": str(b5),
            "c_as_polynomial_in_a": str(c5),
            "coordinate_polynomial": str(coordinate_polynomial.as_expr()),
            "physical_coordinate_interval": [str(value) for value in coordinate_interval],
            "physical_coordinate_root_count": 1,
            "physical_embedding_certificate": {
                "derivative_root_counts": derivative_root_counts,
                "derivative_midpoint_signs": derivative_midpoint_signs,
                "coordinate_signs": ["negative", "negative", "positive", "positive", "negative"],
                "trace_monotonicity": "strictly decreasing on the physical coordinate interval",
            },
            "trace_as_polynomial_in_a": str(p5_trace_reduced),
            "trace_polynomial": str(trace_polynomial.as_expr()),
            "trace_root_intervals": [[left, right] for left, right in trace_intervals],
            "trace_root_counts": root_counts,
            "physical_trace_interval": [4445, 4446],
            "multiplier_minimal_polynomial": str(multiplier_polynomial.as_expr()),
            "reciprocal_pair_logs_decimal_40": [str(sp.N(value, 40)) for value in reciprocal_pair_logs],
            "physical_instability_length_decimal_50": str(sp.N(p5_physical_length, 50)),
            "mahler_height_decimal_50": str(sp.N(p5_height, 50)),
            "galois_excess_decimal_50": str(sp.N(p5_excess, 50)),
            "exact_excess_definition": "sum(acosh(abs(theta)/2) over the five nonphysical real roots theta of the trace polynomial)",
        },
        "exact_inequalities": {
            "period_3_excess_positive": True,
            "period_4a_exceeds_period_3": True,
            "period_5_exceeds_period_4a": True,
            "period_4a_half_conjugate_trace_lt_52": "96^2*6-235^2=71>0",
            "period_4a_half_conjugate_trace_gt_51": "236^2-96^2*6=400>0",
            "period_3_half_conjugate_trace_lt_28": "47^2-21^2*5=4>0",
            "period_5_nonphysical_trace_witness": "one trace root lies in (390,391), so its reciprocal-pair log exceeds acosh(195)>E_4a",
        },
    }


def symbolic_certificate() -> dict[str, object]:
    cycles = primitive_cycles(5)
    expected_counts = {1: 1, 2: 0, 3: 1, 4: 2, 5: 2}
    observed_counts = {period: len(rows) for period, rows in cycles.items()}
    if observed_counts != expected_counts:
        raise ArithmeticError("primitive symbolic cycle counts changed")

    g1 = (0,)
    g3 = (0, 2, 1)
    g4a = (0, 0, 2, 1)
    g4b = (0, 2, 3, 1)
    g5 = (0, 0, 2, 3, 1)
    witness_words = [g1, g3, g4a, g4b, g5]
    for word in witness_words:
        if word not in cycles[len(word)]:
            raise ArithmeticError(f"missing witness cycle: {word}")

    relation_rows: dict[str, object] = {}
    for width in (1, 2):
        blocks, matrix = common_incidence([g1, g3, g4a], width)
        residual = matrix.row(2) - matrix.row(0) - matrix.row(1)
        if residual != sp.zeros(1, len(blocks)):
            raise ArithmeticError(f"width-{width} incidence relation failed")
        relation_rows[f"width_{width}"] = {
            "blocks": [[STATE_LABELS[value] for value in block] for block in blocks],
            "matrix": [[int(value) for value in matrix.row(i)] for i in range(matrix.rows)],
            "relation": "N(gamma_4a)=N(gamma_1)+N(gamma_3)",
        }

    blocks3, matrix3 = common_incidence([g3, g4a, g4b, g5], 3)
    residual3 = matrix3.row(0) + matrix3.row(3) - matrix3.row(1) - matrix3.row(2)
    if residual3 != sp.zeros(1, len(blocks3)):
        raise ArithmeticError("width-three incidence relation failed")
    relation_rows["width_3"] = {
        "blocks": [[STATE_LABELS[value] for value in block] for block in blocks3],
        "matrix": [[int(value) for value in matrix3.row(i)] for i in range(matrix3.rows)],
        "row_order": ["gamma_3", "gamma_4a", "gamma_4b", "gamma_5"],
        "relation": "N(gamma_3)+N(gamma_5)=N(gamma_4a)+N(gamma_4b)",
    }

    blocks4, matrix4 = common_incidence(witness_words, 4)
    selected_blocks = [
        (0, 0, 0, 0),
        (0, 0, 2, 1),
        (0, 0, 2, 3),
        (0, 2, 1, 0),
        (0, 2, 3, 1),
    ]
    selected_columns = [blocks4.index(block) for block in selected_blocks]
    selected_matrix = matrix4[:, selected_columns]
    if selected_matrix.det() != -1 or matrix4.rank() != 5:
        raise ArithmeticError("width-four finite interpolation matrix lost full rank")

    return {
        "state_labels": list(STATE_LABELS),
        "adjacency": [list(row) for row in ADJACENCY],
        "primitive_cycle_counts_through_5": {str(k): v for k, v in observed_counts.items()},
        "primitive_cycles": {
            str(period): [[STATE_LABELS[value] for value in word] for word in words]
            for period, words in cycles.items()
        },
        "witness_cycle_names": ["gamma_1", "gamma_3", "gamma_4a", "gamma_4b", "gamma_5"],
        "witness_cycles": [[STATE_LABELS[value] for value in word] for word in witness_words],
        "incidence_relations": relation_rows,
        "width_4_finite_interpolation": {
            "all_blocks": [[STATE_LABELS[value] for value in block] for block in blocks4],
            "matrix_rank": int(matrix4.rank()),
            "selected_blocks": [[STATE_LABELS[value] for value in block] for block in selected_blocks],
            "selected_matrix": [
                [int(value) for value in selected_matrix.row(i)] for i in range(selected_matrix.rows)
            ],
            "selected_determinant": int(selected_matrix.det()),
            "potential_values": [
                "E_1",
                "E_4a-E_3",
                "E_5-E_4b",
                "E_3",
                "E_4b",
            ],
            "scope": "interpolates only the five exact witnesses; it is not an all-orbit Holder realization",
        },
    }


def core_payload() -> dict[str, object]:
    symbolic = symbolic_certificate()
    algebra = exact_orbit_algebra()
    return {
        "candidate_id": "HCS-P55",
        "source_object": "the frozen four-state mixing H6 survivor and the P54 Mahler Galois-excess assignment",
        "local_potential_convention": "a width-r locally constant potential depends on r consecutive symbolic states and its orbit sum is the pairing with cyclic r-block incidence",
        "symbolic_cycle_certificate": symbolic,
        "exact_orbit_algebra": algebra,
        "three_block_obstruction": {
            "status": "PROVED",
            "theorem": "no locally constant potential depending on at most three consecutive H6 states has periodic sums E_gamma on every primitive orbit",
            "finite_witness": ["gamma_3", "gamma_4a", "gamma_4b", "gamma_5"],
            "forced_identity": "E_3+E_5=E_4a+E_4b",
            "actual_strict_inequality": "E_3+E_5>E_4a+E_4b because E_3>0, E_5>E_4a, and E_4b=0",
            "memory_lower_bound": "any locally constant realization must use at least four consecutive symbolic states",
        },
        "finite_sharpness": {
            "status": "PROVED_FINITE_WITNESS_ONLY",
            "statement": "the five exact rows are interpolable by a nonnegative width-four potential on five selected four-blocks",
            "not_claimed": "no all-orbit width-four or Holder realization is constructed",
        },
        "livsic_scope_firewall": {
            "finite_holder_interpolation": "finite disjoint periodic orbits can be interpolated by a Holder function, so the finite witness does not refute general Holder realizability",
            "cohomology_statement": "Livsic periodic sums test equality modulo coboundary between already-defined Holder observables; they do not turn an arbitrary orbit assignment into an observable",
            "open_all_orbit_gate": "prove an all-period regularity/consistency theorem for E_gamma or produce a sequence of higher-block relations with a quantitative Holder contradiction",
        },
        "strongest_positive_result": "an exact degree-12 period-five multiplier polynomial and a cycle-homology compiler locate the first three-block failure of the Galois-excess assignment",
        "strongest_obstruction": "Galois excess violates the shortest triple-block incidence relation, so no width-at-most-three local potential can complete the P54 weighted zeta",
        "open_theorem": "general Holder or controlled asymptotically additive realization remains open; the next exact local test is the first four-block relation involving periods 4,5,5,6",
        "reusable_structure": "cyclic block-incidence homology converts any locally constant periodic-sum proposal into exact integer relations before thermodynamic formalism is invoked",
        "round2_clue": "derive the exact period-six trace field and test the shortest width-four relation gamma_4a+gamma_6=gamma_5a+gamma_5b; in parallel seek a quantitative shadowing criterion for general Holder data",
        "route_a_status": {
            "tuple": "(A1_WEAK, A2_ANALYTIC_DETERMINANT [physical subsystem only], A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FORMAL_HINT)",
            "overall": "ROUTE_A_EXPLORATORY",
            "full_galois_A2_pass": False,
        },
        "route_b_authorized": False,
        "arithmetic_advance": "NO",
        "claim_boundary": "P55 proves a finite-memory obstruction and exact period-five algebra, not failure of every Holder/asymptotically additive model, not a rational-prime trace, and not a Hilbert-Polya operator",
    }


def validate_core(candidate: dict[str, object], expected: dict[str, object]) -> None:
    if type(candidate) is not dict or candidate != expected:
        raise ValueError("core payload changed")


def mutation_audit(core: dict[str, object]) -> dict[str, object]:
    mutations = [
        ("adjacency", ("symbolic_cycle_certificate", "adjacency", 0, 0), 0),
        ("primitive_count", ("symbolic_cycle_certificate", "primitive_cycle_counts_through_5", "5"), 3),
        ("width2_relation", ("symbolic_cycle_certificate", "incidence_relations", "width_2", "relation"), "false"),
        ("width3_relation", ("symbolic_cycle_certificate", "incidence_relations", "width_3", "relation"), "false"),
        ("width4_rank", ("symbolic_cycle_certificate", "width_4_finite_interpolation", "matrix_rank"), 4),
        ("width4_determinant", ("symbolic_cycle_certificate", "width_4_finite_interpolation", "selected_determinant"), 1),
        ("p4_trace", ("exact_orbit_algebra", "period_4a", "trace"), "-1044"),
        ("p4_excess", ("exact_orbit_algebra", "period_4a", "galois_excess_formula"), "0"),
        ("p5_coordinate_poly", ("exact_orbit_algebra", "period_5", "coordinate_polynomial"), "X**6+1"),
        ("p5_trace_poly", ("exact_orbit_algebra", "period_5", "trace_polynomial"), "T**6+1"),
        ("p5_root_count", ("exact_orbit_algebra", "period_5", "trace_root_counts", 3), 0),
        ("p5_physical_interval", ("exact_orbit_algebra", "period_5", "physical_trace_interval", 1), 4445),
        ("p5_physical_root", ("exact_orbit_algebra", "period_5", "physical_coordinate_root_count"), 0),
        ("p5_monotonicity", ("exact_orbit_algebra", "period_5", "physical_embedding_certificate", "trace_monotonicity"), "unknown"),
        ("strict_inequality", ("exact_orbit_algebra", "exact_inequalities", "period_5_exceeds_period_4a"), False),
        ("theorem_promotion", ("three_block_obstruction", "memory_lower_bound"), "all Holder potentials fail"),
        ("route_b_promotion", ("route_b_authorized",), True),
    ]
    rejected: list[str] = []
    for name, path, replacement in mutations:
        trial = copy.deepcopy(core)
        cursor: object = trial
        for key in path[:-1]:
            cursor = cursor[key]  # type: ignore[index]
        cursor[path[-1]] = replacement  # type: ignore[index]
        try:
            validate_core(trial, core)
        except ValueError:
            rejected.append(name)
        else:
            raise AssertionError(f"mutation was accepted: {name}")
    return {
        "attempted": len(mutations),
        "rejected": len(rejected),
        "labels": rejected,
        "all_rejected": len(rejected) == len(mutations),
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
                "mutations_rejected": certificate["mutation_audit"]["rejected"],
                "three_block_obstruction": certificate["three_block_obstruction"]["status"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
