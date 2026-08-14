#!/usr/bin/env python3
"""Independent reconstruction of the HCS-P56 certificate."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

import sympy as sp


PROJECT = Path(__file__).resolve().parents[1]
DEFAULT_CERTIFICATE = PROJECT / "results" / "c56_certificate.json"
DEFAULT_OUTPUT = PROJECT / "results" / "c56_independent_check.json"
ADJ = ((1, 0, 1, 0), (1, 0, 0, 0), (0, 1, 0, 1), (0, 1, 0, 0))
t, z = sp.symbols("t z")


def canonical(word: tuple[int, ...]) -> tuple[int, ...]:
    return min(word[i:] + word[:i] for i in range(len(word)))


def primitive(word: tuple[int, ...]) -> bool:
    n = len(word)
    return all(n % d or word != word[:d] * (n // d) for d in range(1, n))


def dfs_cycles(period: int) -> list[tuple[int, ...]]:
    found: set[tuple[int, ...]] = set()

    def extend(path: tuple[int, ...]) -> None:
        if len(path) == period:
            if ADJ[path[-1]][path[0]] and primitive(path):
                found.add(canonical(path))
            return
        for target, allowed in enumerate(ADJ[path[-1]]):
            if allowed:
                extend(path + (target,))

    for start in range(4):
        extend((start,))
    return sorted(found)


def windows(word: tuple[int, ...], width: int) -> Counter[tuple[int, ...]]:
    doubled = word + word
    return Counter(tuple(doubled[i : i + width]) if i + width <= 2 * len(word) else tuple(word[(i + j) % len(word)] for j in range(width)) for i in range(len(word)))


def a_word(n: int) -> tuple[int, ...]:
    return (0,) * (n - 2) + (2, 1)


def b_word(n: int) -> tuple[int, ...]:
    return (0,) * (n - 3) + (2, 3, 1)


def jacobian(q: sp.Expr) -> sp.Matrix:
    return sp.Matrix([[-12 * q, -1], [1, 0]])


def trace_of(coordinates: tuple[sp.Expr, ...]) -> sp.Expr:
    matrix = sp.eye(2)
    for q in coordinates:
        matrix = matrix * jacobian(q)
    return sp.simplify(sp.trace(matrix))


def reconstruct() -> dict[str, object]:
    cycles = {period: dfs_cycles(period) for period in range(1, 7)}
    counts = {period: len(rows) for period, rows in cycles.items()}
    if counts != {1: 1, 2: 0, 3: 1, 4: 2, 5: 2, 6: 2}:
        raise AssertionError("independent primitive-cycle census failed")
    for n in range(3, 7):
        if a_word(n) not in cycles[n]:
            raise AssertionError(f"A_{n} missing from independent census")
        if n >= 4 and b_word(n) not in cycles[n]:
            raise AssertionError(f"B_{n} missing from independent census")

    for m in range(3, 65):
        left = windows(a_word(m), m) + windows(b_word(m + 2), m)
        right = windows(a_word(m + 1), m) + windows(b_word(m + 1), m)
        if left != right:
            raise AssertionError(f"independent ladder failed at m={m}")
        da = windows(a_word(m + 1), m).copy()
        da.subtract(windows(a_word(m), m))
        db = windows(b_word(m + 2), m).copy()
        db.subtract(windows(b_word(m + 1), m))
        da = Counter({key: value for key, value in da.items() if value})
        db = Counter({key: value for key, value in db.items() if value})
        if da != db or sorted(da.values()) != [-1, 1, 1]:
            raise AssertionError(f"independent insertion row failed at m={m}")

    sqrt7 = sp.sqrt(7)
    radical = sp.sqrt(25 + 4 * sqrt7)
    aa = (-1 - radical) / 12
    cc = -sqrt7 / 6
    dd = (-1 + radical) / 12
    orbit = (aa, aa, cc, dd, dd, cc)
    recurrence = [
        sp.simplify(1 - 6 * orbit[i] ** 2 - orbit[i - 1] - orbit[(i + 1) % 6])
        for i in range(6)
    ]
    if any(recurrence):
        raise AssertionError("independent period-six recurrence failed")
    trace6 = trace_of(orbit)
    if trace6 != 18062 + 5352 * sqrt7:
        raise AssertionError("independent period-six trace failed")
    trace6_poly = sp.Poly(sp.minimal_polynomial(trace6, t), t)
    multiplier6 = sp.Poly(z**4 - 36124 * z**3 + 125728518 * z**2 - 36124 * z + 1, z)
    if trace6_poly != sp.Poly(t**2 - 36124 * t + 125728516, t):
        raise AssertionError("independent period-six trace polynomial failed")
    if len(sp.factor_list(multiplier6.as_expr())[1]) != 1:
        raise AssertionError("independent period-six multiplier irreducibility failed")
    reduction13 = sp.Poly(multiplier6.as_expr(), z, modulus=13)
    if sp.gcd(reduction13, sp.Poly(z**13 - z, z, modulus=13)).degree() or sp.gcd(
        reduction13, sp.Poly(z**169 - z, z, modulus=13)
    ).degree():
        raise AssertionError("independent mod-13 witness failed")
    half_conjugate = 9031 - 2676 * sqrt7
    if not (1950 < half_conjugate < 1951):
        raise AssertionError("independent period-six conjugate isolation failed")

    trace5 = sp.Poly(
        t**6
        + 3300 * t**5
        - 34165368 * t**4
        - 7291075328 * t**3
        + 26529205510272 * t**2
        + 3609165326736384 * t
        - 4266315336505009664,
        t,
    )
    intervals = ((-7607, -7606), (-711, -710), (-590, -589), (390, 391), (770, 771), (4445, 4446))
    if [int(trace5.count_roots(left, right)) for left, right in intervals] != [1] * 6:
        raise AssertionError("independent period-five isolation failed")
    roots = sorted((sp.re(root) for root in sp.nroots(trace5.as_expr(), n=80)), key=float)
    lengths = [sp.acosh(sp.Abs(root) / 2) for root in roots]
    total = sum(lengths, sp.Float(0, 80))
    e5a, e5b = total - lengths[0], total - lengths[-1]
    e4a = sp.acosh(287 - 96 * sp.sqrt(6))
    e6b = sp.acosh(half_conjugate)
    delta4 = e4a + e6b - e5a - e5b
    if not delta4 < 0:
        raise AssertionError("independent four-block obstruction failed")
    if not (709**2 > 104 * 3902):
        raise AssertionError("independent integer log comparison failed")

    four = [a_word(4), b_word(6), a_word(5), b_word(5)]
    blocks4 = sorted(set().union(*(windows(word, 4) for word in four)))
    matrix4 = sp.Matrix([[windows(word, 4)[block] for block in blocks4] for word in four])
    if matrix4.rank() != 3 or sp.Matrix([[1, 1, -1, -1]]) * matrix4 != sp.zeros(1, len(blocks4)):
        raise AssertionError("independent width-four relation failed")

    seven = [(0,), a_word(3), a_word(4), b_word(4), a_word(5), b_word(5), b_word(6)]
    selected = ((0, 0, 0, 0, 0), (0, 0, 0, 2, 1), (0, 0, 0, 2, 3), (0, 0, 2, 1, 0), (0, 0, 2, 3, 1), (0, 2, 1, 0, 2), (0, 2, 3, 1, 0))
    matrix5 = sp.Matrix([[windows(word, 5)[block] for block in selected] for word in seven])
    if matrix5.det() != 1:
        raise AssertionError("independent width-five minor failed")

    return {
        "check": True,
        "cycle_counts": {str(key): value for key, value in counts.items()},
        "ladder_verified_range": [3, 64],
        "period_6_trace": str(trace6),
        "period_6_trace_minpoly_coefficients": [int(value) for value in trace6_poly.all_coeffs()],
        "period_6_multiplier_degree": multiplier6.degree(),
        "period_6_multiplier_mod_13": [1, 3, 6, 3, 1],
        "period_6_excess_decimal_50": str(sp.N(e6b, 50)),
        "delta_4_decimal_50": str(sp.N(delta4, 50)),
        "strict_four_block_obstruction": bool(delta4 < 0),
        "width_4_rank": matrix4.rank(),
        "width_5_determinant": int(matrix5.det()),
        "integer_margin": 709**2 - 104 * 3902,
    }


def compare_with_primary(independent: dict[str, object], certificate: dict[str, object]) -> None:
    if certificate.get("check") is not True:
        raise AssertionError("primary certificate is not sealed")
    checks = {
        "cycle_counts": certificate["cycle_counts"],
        "period_6_trace": certificate["period_6_B"]["trace"],
        "period_6_multiplier_degree": certificate["period_6_B"]["multiplier_degree"],
        "period_6_excess_decimal_50": certificate["period_6_B"]["galois_excess_decimal_50"],
        "delta_4_decimal_50": certificate["four_block_obstruction"]["delta_4_decimal_50"],
        "width_4_rank": certificate["finite_sharpness"]["width_4_four_row_rank"],
        "width_5_determinant": certificate["finite_sharpness"]["width_5_determinant"],
        "integer_margin": certificate["four_block_obstruction"]["integer_comparison"]["margin"],
    }
    for key, expected in checks.items():
        if independent[key] != expected:
            raise AssertionError(f"primary/independent mismatch: {key}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--certificate", type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    if not args.check:
        raise SystemExit("explicit --check is required")
    certificate = json.loads(args.certificate.read_text(encoding="utf-8"))
    result = reconstruct()
    compare_with_primary(result, certificate)
    result["primary_certificate_sha256"] = hashlib.sha256(args.certificate.read_bytes()).hexdigest()
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
