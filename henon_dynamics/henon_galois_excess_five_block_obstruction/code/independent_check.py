#!/usr/bin/env python3
"""Independent reconstruction of the HCS-P57 algebra and incidence witness."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp


PROJECT = Path(__file__).resolve().parents[1]
DEFAULT_CERTIFICATE = PROJECT / "results" / "c57_certificate.json"
DEFAULT_OUTPUT = PROJECT / "results" / "c57_independent_check.json"

x, t = sp.symbols("x t")
ADJACENCY = (
    (1, 0, 1, 0),
    (1, 0, 0, 0),
    (0, 1, 0, 1),
    (0, 1, 0, 0),
)


def rotations(word: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(word[i:] + word[:i] for i in range(len(word)))


def primitive(word: tuple[int, ...]) -> bool:
    n = len(word)
    return not any(n % d == 0 and word == word[:d] * (n // d) for d in range(1, n))


def cycle_count(period: int) -> int:
    found: set[tuple[int, ...]] = set()
    for word in itertools.product(range(4), repeat=period):
        if all(ADJACENCY[word[i]][word[(i + 1) % period]] for i in range(period)) and primitive(word):
            found.add(min(rotations(word)))
    return len(found)


def family_a(n: int) -> tuple[int, ...]:
    return (0,) * (n - 2) + (2, 1)


def family_b(n: int) -> tuple[int, ...]:
    return (0,) * (n - 3) + (2, 3, 1)


def blocks(word: tuple[int, ...], width: int) -> dict[tuple[int, ...], int]:
    result: dict[tuple[int, ...], int] = {}
    for i in range(len(word)):
        block = tuple(word[(i + j) % len(word)] for j in range(width))
        result[block] = result.get(block, 0) + 1
    return result


def derivative(value: sp.Expr) -> sp.Matrix:
    return sp.Matrix([[-12 * value, -1], [1, 0]])


def trace_of(coordinates: tuple[sp.Expr, ...], modulus: sp.Poly) -> sp.Expr:
    matrix = sp.eye(2)
    for value in coordinates:
        matrix = derivative(value) * matrix
    numerator, denominator = sp.together(sp.trace(matrix)).as_numer_denom()
    return sp.factor(sp.rem(numerator, modulus, x) / denominator)


def reconstruct() -> dict[str, object]:
    counts = {period: cycle_count(period) for period in range(1, 8)}
    if counts != {1: 1, 2: 0, 3: 1, 4: 2, 5: 2, 6: 2, 7: 4}:
        raise ArithmeticError("independent cycle census failed")

    b = sp.expand((1 - 6 * x**2) / 2)
    c = sp.expand(1 - 6 * b**2 - x)
    d = sp.expand(1 - 6 * c**2 - b)

    a6_factorization = sp.factor_list(1 - 6 * d**2 - 2 * c)
    a6_factors = [sp.Poly(factor, x) for factor, exponent in a6_factorization[1] for _ in range(exponent)]
    a6_candidates = [factor for factor in a6_factors if factor.degree() == 6]
    if len(a6_candidates) != 1:
        raise ArithmeticError("independent A6 factor selection failed")
    a6_coordinate = a6_candidates[0]
    a6_trace_map = trace_of((x, b, c, d, c, b), a6_coordinate)
    a6_resultant = sp.Poly(sp.resultant(a6_coordinate.as_expr(), t - a6_trace_map, x), t).primitive()[1]
    a6_factor_rows = sp.factor_list(a6_resultant.as_expr())[1]
    if len(a6_factor_rows) != 1 or a6_factor_rows[0][1] != 2:
        raise ArithmeticError("independent A6 trace multiplicity failed")
    a6_trace = sp.Poly(a6_factor_rows[0][0], t)
    a6_intervals = ((-54575, -54574), (1094, 1095), (5137, 5138))
    if [int(a6_trace.count_roots(*interval)) for interval in a6_intervals] != [1, 1, 1]:
        raise ArithmeticError("independent A6 trace isolation failed")
    a6_coordinate_interval = (sp.Rational(551907131, 10**9), sp.Rational(551907132, 10**9))
    if a6_coordinate.count_roots(*a6_coordinate_interval) != 1:
        raise ArithmeticError("independent A6 coordinate isolation failed")
    if [int(sp.Poly(value, x).count_roots(*a6_coordinate_interval)) for value in (x, b, c, d)] != [0] * 4:
        raise ArithmeticError("independent A6 sign box failed")
    if sp.Poly(sp.diff(a6_trace_map, x), x).count_roots(*a6_coordinate_interval) != 0:
        raise ArithmeticError("independent A6 trace monotonicity failed")
    if not all(
        -54575 < a6_trace_map.subs(x, endpoint) < -54574
        for endpoint in a6_coordinate_interval
    ):
        raise ArithmeticError("independent A6 physical trace image failed")

    p7_factorization = sp.factor_list(1 - 6 * d**2 - c - d)
    p7_factors = [sp.Poly(factor, x) for factor, exponent in p7_factorization[1] for _ in range(exponent)]
    p7_candidates = [factor for factor in p7_factors if factor.degree() == 14]
    if len(p7_candidates) != 1:
        raise ArithmeticError("independent period-seven factor selection failed")
    p7_coordinate = p7_candidates[0]
    p7_trace_map = trace_of((x, b, c, d, d, c, b), p7_coordinate)
    p7_trace = sp.Poly(sp.resultant(p7_coordinate.as_expr(), t - p7_trace_map, x), t).primitive()[1]
    p7_intervals = (
        (-390512, -390511), (-76494, -76493), (-33929, -33928),
        (-9534, -9533), (-9431, -9430), (-5707, -5706), (-4082, -4081),
        (3217, 3218), (5681, 5682), (29838, 29839), (32741, 32742),
        (36376, 36377), (137464, 137465), (230985, 230986),
    )
    if [int(p7_trace.count_roots(*interval)) for interval in p7_intervals] != [1] * 14:
        raise ArithmeticError("independent period-seven trace isolation failed")
    physical_rows = (
        (
            "B7",
            (sp.Rational(-600956965, 10**9), sp.Rational(-600956964, 10**9)),
            (-1, -1, -1, 1),
            (230985, 230986),
        ),
        (
            "A7",
            (sp.Rational(551935742, 10**9), sp.Rational(551935743, 10**9)),
            (1, -1, -1, -1),
            (-390512, -390511),
        ),
    )
    for name, coordinate_interval, expected_signs, trace_interval in physical_rows:
        if p7_coordinate.count_roots(*coordinate_interval) != 1:
            raise ArithmeticError(f"independent {name} coordinate isolation failed")
        signs = tuple(int(sp.sign(value.subs(x, coordinate_interval[0]))) for value in (x, b, c, d))
        zero_counts = tuple(
            int(sp.Poly(value, x).count_roots(*coordinate_interval)) for value in (x, b, c, d)
        )
        if signs != expected_signs or zero_counts != (0, 0, 0, 0):
            raise ArithmeticError(f"independent {name} sign box failed")
        if sp.Poly(sp.diff(p7_trace_map, x), x).count_roots(*coordinate_interval) != 0:
            raise ArithmeticError(f"independent {name} trace monotonicity failed")
        if not all(
            trace_interval[0] < p7_trace_map.subs(x, endpoint) < trace_interval[1]
            for endpoint in coordinate_interval
        ):
            raise ArithmeticError(f"independent {name} physical trace image failed")

    p5_trace = sp.Poly(
        t**6 + 3300 * t**5 - 34165368 * t**4 - 7291075328 * t**3
        + 26529205510272 * t**2 + 3609165326736384 * t
        - 4266315336505009664,
        t,
    )
    def lengths(polynomial: sp.Poly) -> list[sp.Expr]:
        roots = sorted(
            [sp.re(root) for root in sp.nroots(polynomial.as_expr(), n=90, maxsteps=1000)],
            key=float,
        )
        return [sp.acosh(sp.Abs(root) / 2) for root in roots]

    lengths5 = lengths(p5_trace)
    lengths6 = lengths(a6_trace)
    lengths7 = lengths(p7_trace)
    excess_a5 = sum(lengths5, sp.Float(0, 90)) - lengths5[0]
    excess_a6 = sum(lengths6, sp.Float(0, 90)) - lengths6[0]
    excess_b6 = sp.acosh(9031 - 2676 * sp.sqrt(7))
    excess_b7 = sum(lengths7, sp.Float(0, 90)) - lengths7[-1]
    delta5 = excess_a5 + excess_b7 - excess_a6 - excess_b6
    if not delta5 > 139:
        raise ArithmeticError("independent Delta_5 lower bound failed")

    relation_words = [family_a(5), family_b(7), family_a(6), family_b(6)]
    all5 = sorted({block for word in relation_words for block in blocks(word, 5)})
    matrix5 = sp.Matrix([[blocks(word, 5).get(block, 0) for block in all5] for word in relation_words])
    if matrix5.rank() != 3 or sp.Matrix([[1, 1, -1, -1]]) * matrix5 != sp.zeros(1, len(all5)):
        raise ArithmeticError("independent width-five relation failed")
    selected6 = ((0, 0, 0, 0, 2, 1), (0, 0, 0, 0, 2, 3), (0, 0, 0, 2, 1, 0), (0, 0, 0, 2, 3, 1))
    minor6 = sp.Matrix([[blocks(word, 6).get(block, 0) for block in selected6] for word in relation_words])
    if minor6.det() != -1:
        raise ArithmeticError("independent width-six minor failed")

    lower_product = 709 * 588 * 389 * 769 * 4444
    upper_product = 1095 * 5138 * 3902
    if lower_product - upper_product != 554187019465548:
        raise ArithmeticError("independent exact margin failed")

    return {
        "cycle_counts": {str(key): value for key, value in counts.items()},
        "A6_coordinate_degree": a6_coordinate.degree(),
        "A6_trace_polynomial": str(a6_trace.as_expr()).replace("t", "T"),
        "A6_trace_intervals": [list(interval) for interval in a6_intervals],
        "P7_coordinate_degree": p7_coordinate.degree(),
        "P7_trace_degree": p7_trace.degree(),
        "P7_trace_sha256": hashlib.sha256(
            str(p7_trace.as_expr()).replace("t", "T").encode()
        ).hexdigest(),
        "P7_trace_intervals": [list(interval) for interval in p7_intervals],
        "Delta_5_decimal_50": str(sp.N(delta5, 50)),
        "exact_integer_margin": lower_product - upper_product,
        "width_5_rank": matrix5.rank(),
        "width_6_minor_determinant": int(minor6.det()),
    }


def compare(result: dict[str, object], certificate: dict[str, object]) -> None:
    expected = {
        "cycle_counts": certificate["symbolic_certificate"]["primitive_cycle_counts_through_7"],
        "A6_coordinate_degree": certificate["A6_exact_algebra"]["coordinate_polynomial_degree"],
        "A6_trace_polynomial": certificate["A6_exact_algebra"]["trace_polynomial"],
        "A6_trace_intervals": certificate["A6_exact_algebra"]["trace_root_intervals"],
        "P7_coordinate_degree": certificate["period_7_exact_algebra"]["coordinate_polynomial_degree"],
        "P7_trace_degree": certificate["period_7_exact_algebra"]["trace_polynomial_degree"],
        "P7_trace_sha256": hashlib.sha256(certificate["period_7_exact_algebra"]["trace_polynomial"].encode()).hexdigest(),
        "P7_trace_intervals": certificate["period_7_exact_algebra"]["trace_root_intervals"],
        "Delta_5_decimal_50": certificate["five_block_obstruction"]["Delta_5_decimal_50"],
        "exact_integer_margin": certificate["five_block_obstruction"]["integer_margin"],
        "width_5_rank": certificate["finite_sharpness"]["width_5_rank"],
        "width_6_minor_determinant": certificate["finite_sharpness"]["width_6_four_row_determinant"],
    }
    if result != expected:
        raise ArithmeticError("independent reconstruction disagrees with the primary certificate")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if not args.check:
        raise SystemExit("explicit --check is required")
    result = reconstruct()
    certificate = json.loads(args.certificate.read_text(encoding="utf-8"))
    compare(result, certificate)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"check": True, "Delta_5": result["Delta_5_decimal_50"], "independent": True}, sort_keys=True))


if __name__ == "__main__":
    main()
