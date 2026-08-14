#!/usr/bin/env python3
"""Independent reconstruction of the HCS-P55 exact certificate."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp


PROJECT = Path(__file__).resolve().parents[1]
TRACK = PROJECT.parent
DEFAULT_CERTIFICATE = PROJECT / "results" / "c55_certificate.json"
DEFAULT_OUTPUT = PROJECT / "results" / "c55_independent_check.json"

ADJ = ((1, 0, 1, 0), (1, 0, 0, 0), (0, 1, 0, 1), (0, 1, 0, 0))
LABELS = ("--", "-+", "+-", "++")
x, t, z = sp.symbols("x t z")


def rotate_min(word: tuple[int, ...]) -> tuple[int, ...]:
    return min(word[i:] + word[:i] for i in range(len(word)))


def is_primitive(word: tuple[int, ...]) -> bool:
    n = len(word)
    for divisor in range(1, n):
        if n % divisor == 0 and word == word[:divisor] * (n // divisor):
            return False
    return True


def dfs_cycles(period: int) -> list[tuple[int, ...]]:
    cycles: set[tuple[int, ...]] = set()

    def extend(path: tuple[int, ...]) -> None:
        if len(path) == period:
            if ADJ[path[-1]][path[0]] and is_primitive(path):
                cycles.add(rotate_min(path))
            return
        for target, allowed in enumerate(ADJ[path[-1]]):
            if allowed:
                extend(path + (target,))

    for start in range(4):
        extend((start,))
    return sorted(cycles)


def counts(word: tuple[int, ...], width: int) -> dict[tuple[int, ...], int]:
    result: dict[tuple[int, ...], int] = {}
    for start in range(len(word)):
        block = tuple(word[(start + offset) % len(word)] for offset in range(width))
        result[block] = result.get(block, 0) + 1
    return result


def add_rows(*rows: tuple[int, dict[tuple[int, ...], int]]) -> dict[tuple[int, ...], int]:
    result: dict[tuple[int, ...], int] = {}
    for sign, row in rows:
        for block, value in row.items():
            result[block] = result.get(block, 0) + sign * value
    return {block: value for block, value in result.items() if value}


def jacobian(q: sp.Expr) -> sp.Matrix:
    return sp.Matrix([[-12 * q, -1], [1, 0]])


def trace_of(coordinates: tuple[sp.Expr, ...]) -> sp.Expr:
    matrix = sp.eye(2)
    for q in coordinates:
        matrix = jacobian(q) * matrix
    return sp.simplify(sp.trace(matrix))


def reconstruct() -> dict[str, object]:
    cycles = {period: dfs_cycles(period) for period in range(1, 6)}
    cycle_counts = {period: len(words) for period, words in cycles.items()}
    if cycle_counts != {1: 1, 2: 0, 3: 1, 4: 2, 5: 2}:
        raise AssertionError("independent symbolic enumeration failed")

    g1, g3 = (0,), (0, 2, 1)
    g4a, g4b = (0, 0, 2, 1), (0, 2, 3, 1)
    g5 = (0, 0, 2, 3, 1)
    if add_rows((1, counts(g4a, 1)), (-1, counts(g1, 1)), (-1, counts(g3, 1))):
        raise AssertionError("independent one-block relation failed")
    if add_rows((1, counts(g4a, 2)), (-1, counts(g1, 2)), (-1, counts(g3, 2))):
        raise AssertionError("independent two-block relation failed")
    if add_rows(
        (1, counts(g3, 3)),
        (1, counts(g5, 3)),
        (-1, counts(g4a, 3)),
        (-1, counts(g4b, 3)),
    ):
        raise AssertionError("independent three-block relation failed")

    words = [g1, g3, g4a, g4b, g5]
    selected = [(0, 0, 0, 0), (0, 0, 2, 1), (0, 0, 2, 3), (0, 2, 1, 0), (0, 2, 3, 1)]
    interpolation = sp.Matrix([[counts(word, 4).get(block, 0) for block in selected] for word in words])
    if interpolation.det() != -1:
        raise AssertionError("independent finite width-four interpolation failed")

    sqrt6 = sp.sqrt(6)
    a4 = -sp.sqrt((3 + sqrt6) / 18)
    b4 = -sqrt6 / 6
    p4_trace = trace_of((a4, b4, -a4, b4))
    if p4_trace != -574 - 192 * sqrt6:
        raise AssertionError("independent period-four trace failed")
    p4_half_conjugate_trace = 287 - 96 * sqrt6

    b = (1 - 6 * x**2) / 2
    c = sp.expand(1 - 6 * b**2 - x)
    f = sp.Poly(
        5832 * x**6 - 1944 * x**5 - 2268 * x**4 + 648 * x**3 + 144 * x**2 - 12 * x - 1,
        x,
    )
    close = sp.factor(6 * c**2 + b + c - 1)
    if sp.expand(close - (6 * x**2 + 2 * x - 1) * f.as_expr() / 2) != 0:
        raise AssertionError("independent period-five closure failed")

    raw_trace = trace_of((x, b, c, c, b))
    numerator, denominator = sp.together(raw_trace).as_numer_denom()
    reduced_trace = sp.factor(sp.rem(numerator, f, x) / denominator)
    trace_resultant = sp.resultant(f.as_expr(), sp.together(t - reduced_trace).as_numer_denom()[0], x)
    trace_poly = sp.Poly(trace_resultant, t).primitive()[1]
    expected_trace_poly = sp.Poly(
        t**6
        + 3300 * t**5
        - 34165368 * t**4
        - 7291075328 * t**3
        + 26529205510272 * t**2
        + 3609165326736384 * t
        - 4266315336505009664,
        t,
    )
    if trace_poly != expected_trace_poly:
        raise AssertionError("independent period-five trace resultant failed")

    intervals = [(-7607, -7606), (-711, -710), (-590, -589), (390, 391), (770, 771), (4445, 4446)]
    interval_counts = [int(trace_poly.count_roots(left, right)) for left, right in intervals]
    if interval_counts != [1] * 6:
        raise AssertionError("independent trace-root isolation failed")

    coordinate_interval = (sp.Rational(-279433, 500000), sp.Rational(-111773, 200000))
    if f.count_roots(*coordinate_interval) != 1:
        raise AssertionError("independent physical-coordinate isolation failed")
    coordinate_midpoint = sum(coordinate_interval, sp.Rational(0)) / 2
    derivative_rows = {
        "b": sp.Poly(sp.diff(b, x), x),
        "c": sp.Poly(sp.diff(c, x), x),
        "trace": sp.Poly(sp.diff(reduced_trace, x), x),
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
        raise AssertionError("independent physical monotonicity isolation failed")
    if derivative_midpoint_signs != {"b": 1, "c": 1, "trace": -1}:
        raise AssertionError("independent physical monotonicity signs failed")
    if not (
        coordinate_interval[1] < 0
        and b.subs(x, coordinate_interval[0]) < 0
        and b.subs(x, coordinate_interval[1]) < 0
        and c.subs(x, coordinate_interval[0]) > 0
        and c.subs(x, coordinate_interval[1]) > 0
    ):
        raise AssertionError("independent physical sign word failed")
    trace_left = reduced_trace.subs(x, coordinate_interval[0])
    trace_right = reduced_trace.subs(x, coordinate_interval[1])
    if not (4445 < trace_right < trace_left < 4446):
        raise AssertionError("independent physical trace interval failed")

    multiplier = sp.Poly(
        sp.expand(sp.resultant(trace_poly.as_expr(), t - (z + 1 / z), t) * z**6), z
    )
    if multiplier.degree() != 12 or multiplier.LC() != 1 or multiplier.TC() != 1:
        raise AssertionError("independent multiplier polynomial failed")
    if len(sp.factor_list(multiplier.as_expr())[1]) != 1:
        raise AssertionError("independent multiplier irreducibility failed")

    if not (96**2 * 6 - 235**2 > 0 and 236**2 - 96**2 * 6 > 0 and 47**2 - 21**2 * 5 > 0):
        raise AssertionError("independent exact comparison failed")
    roots = sorted([sp.re(root) for root in sp.nroots(trace_poly.as_expr(), n=70)], key=float)
    logs = [sp.acosh(sp.Abs(root) / 2) for root in roots]
    p5_excess = sum(logs[:-1], sp.Float(0, 70))

    return {
        "cycle_counts": {str(period): count for period, count in cycle_counts.items()},
        "relations": {
            "width_1": "gamma_4a=gamma_1+gamma_3 in block incidence",
            "width_2": "gamma_4a=gamma_1+gamma_3 in block incidence",
            "width_3": "gamma_3+gamma_5=gamma_4a+gamma_4b in block incidence",
        },
        "width_4_interpolation_determinant": int(interpolation.det()),
        "period_4a_trace": str(p4_trace),
        "period_4a_excess_decimal_40": str(sp.N(sp.acosh(p4_half_conjugate_trace), 40)),
        "period_5_trace_polynomial_coefficients": [int(value) for value in trace_poly.all_coeffs()],
        "period_5_trace_interval_counts": interval_counts,
        "period_5_physical_coordinate_root_count": 1,
        "period_5_physical_embedding_certificate": {
            "derivative_root_counts": derivative_root_counts,
            "derivative_midpoint_signs": derivative_midpoint_signs,
            "coordinate_signs": ["negative", "negative", "positive", "positive", "negative"],
            "trace_monotonicity": "strictly decreasing on the physical coordinate interval",
        },
        "period_5_multiplier_degree": multiplier.degree(),
        "period_5_excess_decimal_40": str(sp.N(p5_excess, 40)),
        "strict_obstruction": bool(p5_excess > sp.N(sp.acosh(p4_half_conjugate_trace), 60)),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if not args.check:
        raise SystemExit("explicit --check is required")

    certificate = json.loads(args.certificate.read_text(encoding="utf-8"))
    for row in certificate["dependency_locks"].values():
        path = TRACK / row["path"]
        if hashlib.sha256(path.read_bytes()).hexdigest() != row["sha256"]:
            raise RuntimeError(f"dependency changed: {path}")

    reconstructed = reconstruct()
    certified = certificate["exact_orbit_algebra"]
    if reconstructed["period_4a_trace"] != certified["period_4a"]["trace"]:
        raise AssertionError("certificate period-four trace differs")
    certified_trace_poly = sp.Poly(
        sp.sympify(certified["period_5"]["trace_polynomial"], locals={"T": t}), t
    )
    if reconstructed["period_5_trace_polynomial_coefficients"] != [
        int(value) for value in certified_trace_poly.all_coeffs()
    ]:
        raise AssertionError("certificate period-five polynomial differs")
    if reconstructed["period_5_trace_interval_counts"] != certified["period_5"]["trace_root_counts"]:
        raise AssertionError("certificate root counts differ")
    if (
        reconstructed["period_5_physical_coordinate_root_count"]
        != certified["period_5"]["physical_coordinate_root_count"]
    ):
        raise AssertionError("certificate physical-coordinate count differs")
    if (
        reconstructed["period_5_physical_embedding_certificate"]
        != certified["period_5"]["physical_embedding_certificate"]
    ):
        raise AssertionError("certificate physical-embedding proof differs")
    if not reconstructed["strict_obstruction"]:
        raise AssertionError("strict obstruction was not independently recovered")

    result = {
        "check": True,
        "candidate_id": "HCS-P55",
        "certificate_sha256": hashlib.sha256(args.certificate.read_bytes()).hexdigest(),
        "reconstruction": reconstructed,
        "claim_boundary": "independent check certifies the width-at-most-three obstruction only; general Holder realization remains open",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"check": True, "certificate_sha256": result["certificate_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
