#!/usr/bin/env python3
"""Independent symbolic/numerical sentinel for HCS-P62."""

from __future__ import annotations

import argparse
import hashlib
import json
from itertools import product
from pathlib import Path

import sympy as sp


PROJECT = Path(__file__).resolve().parents[1]
DEFAULT_CERTIFICATE = PROJECT / "results" / "c62_certificate.json"
DEFAULT_OUTPUT = PROJECT / "results" / "c62_independent_check.json"
PERIODS = (1, 3, 5, 7, 9, 11)


def sha(payload: object) -> str:
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def primitive(word: tuple[int, ...]) -> bool:
    n = len(word)
    return not any(n % d == 0 and word == word[:d] * (n // d) for d in range(1, n))


def full_shift_counts(max_period: int = 13) -> list[dict[str, int]]:
    rows = []
    for n in range(1, max_period + 1):
        primitive_points = sum(1 for word in product((0, 1), repeat=n) if primitive(word))
        rows.append({
            "period": n,
            "fixed_points": 2**n,
            "primitive_points_cartesian": primitive_points,
            "primitive_orbits": primitive_points // n,
        })
    return rows


def independent_quotients() -> dict[int, sp.Poly]:
    x = sp.symbols("x")
    q0 = x
    q1 = sp.expand((1 - 6 * x**2) / 2)
    coordinates = [q0, q1]
    quotients: dict[int, sp.Poly] = {}
    for n in PERIODS:
        m = (n - 1) // 2
        while len(coordinates) <= m + 1:
            coordinates.append(sp.expand(1 - coordinates[-2] - 6 * coordinates[-1] ** 2))
        closure = sp.Poly(coordinates[m + 1] - coordinates[m], x, domain=sp.QQ).monic()
        inherited = sp.Poly(1, x, domain=sp.QQ)
        for d in sp.divisors(n):
            if d < n:
                inherited *= quotients[int(d)]
        quotient, remainder = sp.div(closure, inherited, domain=sp.QQ)
        if not remainder.is_zero:
            raise ArithmeticError(f"independent quotient division failed at n={n}")
        quotients[n] = quotient.monic()
    return quotients


def numerical_rows() -> list[dict[str, object]]:
    rows = []
    for n, quotient in independent_quotients().items():
        roots = sp.nroots(quotient.as_expr(), n=60, maxsteps=2000)
        imaginary_max = max(abs(complex(root).imag) for root in roots)
        real_roots = sorted(complex(root).real for root in roots if abs(complex(root).imag) < 1e-45)
        if len(real_roots) != quotient.degree():
            raise ArithmeticError(f"independent nonreal root at n={n}")
        minimum_gap = min(
            (right - left for left, right in zip(real_roots, real_roots[1:])),
            default=float("inf"),
        )
        if minimum_gap <= 1e-30:
            raise ArithmeticError(f"independent root collision at n={n}")
        rows.append({
            "period": n,
            "degree": quotient.degree(),
            "real_roots": len(real_roots),
            "max_abs_imaginary_part": f"{imaginary_max:.3e}",
            "minimum_real_root_gap": f"{minimum_gap:.16e}",
        })
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    certificate = json.loads(args.certificate.read_text(encoding="utf-8"))
    symbolic = full_shift_counts()
    certified_symbolic = certificate["all_period_fixed_point_rows"]
    for observed, frozen in zip(symbolic, certified_symbolic, strict=True):
        if observed["period"] != frozen["period"]:
            raise ArithmeticError("period row mismatch")
        if observed["fixed_points"] != frozen["fixed_points_of_nth_iterate"]:
            raise ArithmeticError("full-shift fixed count mismatch")
        if observed["primitive_points_cartesian"] != frozen["least_period_points"]:
            raise ArithmeticError("primitive point count mismatch")
    numerical = numerical_rows()
    certified_by_period = {row["period"]: row for row in certificate["finite_exact_rows"]}
    for row in numerical:
        frozen = certified_by_period[row["period"]]
        if row["degree"] != frozen["primitive_degree"] or row["real_roots"] != frozen["exact_real_simple_primitive_roots"]:
            raise ArithmeticError("independent primitive-root mismatch")
    core = {
        "candidate_id": "HCS-P62",
        "method": "Cartesian full-shift enumeration plus independent high-precision primitive-quotient roots",
        "full_shift_rows": symbolic,
        "numerical_rows": numerical,
        "parameter_endpoint_checks": {
            "six_gt_23347_over_4096": bool(sp.Rational(6) > sp.Rational(23347, 4096)),
            "ten_gt_5_plus_2sqrt5": bool(sp.Rational(25) > sp.Rational(20)),
        },
        "all_checks_match": True,
        "scope_preserved": certificate["claim_status"]["arithmetic_advance"] == "NO",
    }
    result = {**core, "result_sha256": sha(core), "check": True}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "candidate_id": result["candidate_id"],
        "check": result["check"],
        "result_sha256": result["result_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
