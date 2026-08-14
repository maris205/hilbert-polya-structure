#!/usr/bin/env python3
"""Independent exact reconstruction for HCS-P58."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp


PROJECT = Path(__file__).resolve().parents[1]
DEFAULT_CERTIFICATE = PROJECT / "results" / "c58_certificate.json"
DEFAULT_OUTPUT = PROJECT / "results" / "c58_independent_check.json"

x, t = sp.symbols("x t")

INTERVALS = {
    "A8": (
        (-2793061, -2793060), (-242473, -242472), (-102623, -102622),
        (-71703, -71702), (-69893, -69892), (-33020, -33019),
        (-10678, -10677), (-9340, -9339), (10954, 10955),
        (95183, 95184), (252649, 252650), (259912, 259913),
    ),
    "B8": (
        (21828, 21829), (30715, 30716), (67810, 67811),
        (216151, 216152), (1000641, 1000642), (1652592, 1652593),
    ),
    "P9": (
        (-19975348, -19975347), (-4644653, -4644652),
        (-1734047, -1734046), (-518197, -518196), (-516613, -516612),
        (-504171, -504170), (-407093, -407092), (-350625, -350624),
        (-122928, -122927), (-87690, -87689), (-58024, -58023),
        (-56520, -56519), (-40350, -40349), (-33678, -33677),
        (27764, 27765), (39697, 39698), (83805, 83806), (91109, 91110),
        (232988, 232989), (438821, 438822), (516842, 516843),
        (1549429, 1549430), (1832226, 1832227), (1858726, 1858727),
        (2569981, 2569982), (7178561, 7178562), (7943186, 7943187),
        (11819577, 11819578),
    ),
}

P7_INTERVALS = (
    (-390512, -390511), (-76494, -76493), (-33929, -33928),
    (-9534, -9533), (-9431, -9430), (-5707, -5706), (-4082, -4081),
    (3217, 3218), (5681, 5682), (29838, 29839), (32741, 32742),
    (36376, 36377), (137464, 137465), (230985, 230986),
)

EXPECTED_TRACE_SHA = {
    "A8": "c10a3536d0781bdbbfbb320d48441a97583af9cd18517991c76e71813936c8ab",
    "B8": "49e0a21377ff47f504fa00d85f8ed3cee17d70d0677085bdc52e4203f4ac77fd",
    "P9": "f52d222e2934061dc367950e3e98e56d4fb9e0e6bd95c7b383fec9061bd7ac3b",
}


def canonical_sha(payload: object) -> str:
    data = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(data).hexdigest()


def chain(vertex: bool, depth: int) -> tuple[sp.Expr, ...]:
    second = (1 - 6 * x**2) / 2 if vertex else 1 - 6 * x**2 - x
    values = [x, sp.expand(second)]
    while len(values) <= depth:
        values.append(sp.expand(1 - 6 * values[-1] ** 2 - values[-2]))
    return tuple(values)


def selected_factor(expression: sp.Expr, degree: int) -> sp.Poly:
    rows = [sp.Poly(f, x) for f, power in sp.factor_list(expression)[1] if power == 1]
    choices = [row for row in rows if row.degree() == degree]
    if len(choices) != 1:
        raise ArithmeticError("primitive factor selection failed")
    return choices[0]


def trace_field(modulus: sp.Poly, coordinates: tuple[sp.Expr, ...]) -> tuple[sp.Poly, int]:
    matrix = sp.eye(2)
    for value in coordinates:
        matrix = sp.Matrix([[-12 * value, -1], [1, 0]]) * matrix
    trace_map = sp.rem(sp.expand(sp.trace(matrix)), modulus, x)
    resultant = sp.Poly(sp.resultant(modulus.as_expr(), t - trace_map, x), t).primitive()[1]
    factors = sp.factor_list(resultant.as_expr())[1]
    if len(factors) != 1:
        raise ArithmeticError("trace resultant split unexpectedly")
    return sp.Poly(factors[0][0], t), int(factors[0][1])


def lower(interval: tuple[int, int]) -> int:
    a, b = interval
    return (a if a > 0 else -b) - 1


def upper(interval: tuple[int, int]) -> int:
    a, b = interval
    return b if a > 0 else -a


def product(values: list[int]) -> int:
    answer = 1
    for value in values:
        answer *= value
    return answer


def reconstruct() -> dict[str, object]:
    vertex = chain(True, 4)
    edge = chain(False, 3)
    cases = {
        "A8": (
            selected_factor(1 - 6 * vertex[4] ** 2 - 2 * vertex[3], 24),
            (vertex[0], vertex[1], vertex[2], vertex[3], vertex[4], vertex[3], vertex[2], vertex[1]),
            12,
            2,
        ),
        "B8": (
            selected_factor(1 - 6 * edge[3] ** 2 - edge[2] - edge[3], 12),
            (edge[0], edge[0], edge[1], edge[2], edge[3], edge[3], edge[2], edge[1]),
            6,
            2,
        ),
        "P9": (
            selected_factor(1 - 6 * vertex[4] ** 2 - vertex[3] - vertex[4], 28),
            (vertex[0], vertex[1], vertex[2], vertex[3], vertex[4], vertex[4], vertex[3], vertex[2], vertex[1]),
            28,
            1,
        ),
    }

    fields: dict[str, object] = {}
    for name, (coordinate, coordinates, expected_degree, expected_multiplicity) in cases.items():
        trace, multiplicity = trace_field(coordinate, coordinates)
        coefficient_sha = canonical_sha([int(v) for v in trace.all_coeffs()])
        root_counts = [int(trace.count_roots(a, b)) for a, b in INTERVALS[name]]
        if trace.degree() != expected_degree or multiplicity != expected_multiplicity:
            raise ArithmeticError(f"{name} trace degree/multiplicity failed")
        if coefficient_sha != EXPECTED_TRACE_SHA[name] or root_counts != [1] * expected_degree:
            raise ArithmeticError(f"{name} trace field reconstruction failed")
        fields[name] = {
            "coordinate_degree": coordinate.degree(),
            "trace_degree": trace.degree(),
            "trace_resultant_multiplicity": multiplicity,
            "trace_coefficients_sha256": coefficient_sha,
            "root_counts": root_counts,
        }

    delta6_lower = product(
        [lower(P7_INTERVALS[j]) for j in range(1, 14)]
        + [lower(P7_INTERVALS[j]) for j in range(0, 13)]
    )
    delta6_upper = product([1095, 5138] + [upper(INTERVALS["B8"][j]) for j in range(5)])
    delta7_lower = product(
        [lower(P7_INTERVALS[j]) for j in range(1, 14)]
        + [lower(INTERVALS["P9"][j]) for j in range(27)]
    )
    delta7_upper = product(
        [upper(INTERVALS["A8"][j]) for j in range(1, 12)]
        + [upper(INTERVALS["B8"][j]) for j in range(5)]
    )
    if not delta6_lower > delta6_upper or not delta7_lower > delta7_upper:
        raise ArithmeticError("integer-product parity certificate failed")

    q_minus = -(1 + sp.sqrt(7)) / 6
    trace_fixed = 2 + 2 * sp.sqrt(7)
    unstable = sp.simplify((trace_fixed + sp.sqrt(trace_fixed**2 - 4)) / 2)
    stable = sp.simplify(1 / unstable)
    if sp.simplify(q_minus - (1 - 6 * q_minus**2 - q_minus)) != 0:
        raise ArithmeticError("negative fixed point failed")
    if not 0 < stable < 2 / sp.sqrt(17) < 1:
        raise ArithmeticError("stable-tail ordering failed")

    return {
        "candidate_id": "HCS-P58",
        "fields": fields,
        "Delta_6_lower_product": delta6_lower,
        "Delta_6_upper_product": delta6_upper,
        "Delta_6_exact_sign": "negative",
        "Delta_7_lower_product": delta7_lower,
        "Delta_7_upper_product": delta7_upper,
        "Delta_7_exact_sign": "positive",
        "negative_fixed_point": str(q_minus),
        "stable_eigenvalue_positive": True,
        "arithmetic_advance": "NO",
    }


def compare(result: dict[str, object], certificate: dict[str, object]) -> None:
    primary_fields = certificate["reflection_algebra"]
    expected = {
        "candidate_id": certificate["candidate_id"],
        "fields": {
            "A8": {
                "coordinate_degree": primary_fields["A8_vertex_vertex"]["coordinate_degree"],
                "trace_degree": primary_fields["A8_vertex_vertex"]["trace_degree"],
                "trace_resultant_multiplicity": primary_fields["A8_vertex_vertex"]["trace_resultant_multiplicity"],
                "trace_coefficients_sha256": primary_fields["A8_vertex_vertex"]["trace_coefficients_sha256"],
                "root_counts": primary_fields["A8_vertex_vertex"]["trace_intervals"] and [1] * 12,
            },
            "B8": {
                "coordinate_degree": primary_fields["B8_edge_edge"]["coordinate_degree"],
                "trace_degree": primary_fields["B8_edge_edge"]["trace_degree"],
                "trace_resultant_multiplicity": primary_fields["B8_edge_edge"]["trace_resultant_multiplicity"],
                "trace_coefficients_sha256": primary_fields["B8_edge_edge"]["trace_coefficients_sha256"],
                "root_counts": primary_fields["B8_edge_edge"]["trace_intervals"] and [1] * 6,
            },
            "P9": {
                "coordinate_degree": primary_fields["A9_B9_vertex_edge"]["coordinate_degree"],
                "trace_degree": primary_fields["A9_B9_vertex_edge"]["trace_degree"],
                "trace_resultant_multiplicity": primary_fields["A9_B9_vertex_edge"]["trace_resultant_multiplicity"],
                "trace_coefficients_sha256": primary_fields["A9_B9_vertex_edge"]["trace_coefficients_sha256"],
                "root_counts": primary_fields["A9_B9_vertex_edge"]["trace_intervals"] and [1] * 28,
            },
        },
        "Delta_6_lower_product": certificate["parity_falsifier"]["Delta_6_lower_product_for_E_A7_plus_E_B7"],
        "Delta_6_upper_product": certificate["parity_falsifier"]["Delta_6_upper_product_for_E_A6_plus_E_B8"],
        "Delta_6_exact_sign": certificate["parity_falsifier"]["Delta_6_exact_sign"],
        "Delta_7_lower_product": certificate["parity_falsifier"]["Delta_7_lower_product_for_E_A7_plus_E_B9"],
        "Delta_7_upper_product": certificate["parity_falsifier"]["Delta_7_upper_product_for_E_A8_plus_E_B8"],
        "Delta_7_exact_sign": certificate["parity_falsifier"]["Delta_7_exact_sign"],
        "negative_fixed_point": certificate["fixed_point_tail"]["negative_fixed_point"],
        "stable_eigenvalue_positive": certificate["fixed_point_tail"]["stable_eigenvalue_positive"],
        "arithmetic_advance": certificate["arithmetic_advance"],
    }
    if result != expected:
        raise ArithmeticError("independent reconstruction disagrees with primary certificate")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if not args.check:
        raise SystemExit("explicit --check is required")
    certificate = json.loads(args.certificate.read_text(encoding="utf-8"))
    result = reconstruct()
    compare(result, certificate)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"candidate_id": "HCS-P58", "check": True, "result_sha256": canonical_sha(result)}, sort_keys=True))


if __name__ == "__main__":
    main()
