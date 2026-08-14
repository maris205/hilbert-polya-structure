#!/usr/bin/env python3
"""Independent exact reconstruction for HCS-P60 (no primary-code imports)."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
X = sp.symbols("X")


def digest(payload: object) -> str:
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def poly_digest(poly: sp.Poly) -> str:
    integer = poly.clear_denoms()[1].primitive()[1]
    if integer.LC() < 0:
        integer = -integer
    return digest([int(value) for value in integer.all_coeffs()])


def reconstruct() -> dict[str, object]:
    q = [X, sp.expand((1 - 6 * X**2) / 2)]
    closures: dict[int, sp.Poly] = {}
    primitive: dict[int, sp.Poly] = {}
    rows: list[dict[str, object]] = []
    for m in range(8):
        n = 2 * m + 1
        while len(q) <= m + 1:
            q.append(sp.expand(1 - 6 * q[-1] ** 2 - q[-2]))
        closure = sp.Poly(q[m + 1] - q[m], X, domain=sp.QQ).monic()
        closures[n] = closure
        lower = sp.Poly(1, X, domain=sp.QQ)
        for d in sp.divisors(n):
            if d < n:
                lower *= primitive[int(d)]
        quotient, remainder = sp.div(closure, lower, domain=sp.QQ)
        if not remainder.is_zero:
            raise ArithmeticError(f"non-polynomial quotient at n={n}")
        primitive[n] = quotient.monic()
        expected_degree = sum(
            int(sp.mobius(n // d)) * 2 ** ((d + 1) // 2)
            for d in sp.divisors(n)
        )
        if closure.degree() != 2 ** ((n + 1) // 2):
            raise ArithmeticError("closure degree failure")
        if primitive[n].degree() != expected_degree:
            raise ArithmeticError("primitive degree failure")
        if sp.gcd(closure, closure.diff()).degree() != 0:
            raise ArithmeticError("squarefree failure")
        for d in sp.divisors(n):
            if d < n and not sp.rem(closure, closures[int(d)], domain=sp.QQ).is_zero:
                raise ArithmeticError("divisibility failure")
        rows.append({
            "period": n,
            "closure_degree": closure.degree(),
            "quotient_degree": primitive[n].degree(),
            "closure_coefficients_sha256": poly_digest(closure),
            "quotient_coefficients_sha256": poly_digest(primitive[n]),
        })
    return {
        "candidate_id": "HCS-P60",
        "rows": rows,
        "period9_quotient_sha256": rows[4]["quotient_coefficients_sha256"],
        "degree_sequence": [row["quotient_degree"] for row in rows],
        "check": True,
    }


EXPECTED_RESULT_SHA256 = "06eddc3a27aad028b813be1c91e21b1b96b7bd286d1512c086cabc59e04bbc41"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, default=ROOT / "results" / "c60_certificate.json")
    parser.add_argument("--output", type=Path, default=ROOT / "results" / "c60_independent_check.json")
    args = parser.parse_args()
    primary = json.loads(args.certificate.read_text(encoding="utf-8"))
    result = reconstruct()
    primary_rows = primary["finite_exact_rows"]
    for left, right in zip(result["rows"], primary_rows, strict=True):
        for key, value in left.items():
            if key != "period" and value != right[key]:
                raise ArithmeticError(f"primary mismatch at period {left['period']}: {key}")
    if result["period9_quotient_sha256"] != primary["p58_period9_quotient_match"]:
        raise ArithmeticError("P58 period-nine crosslock mismatch")
    result_sha = digest(result)
    if EXPECTED_RESULT_SHA256 == "TO_BE_FROZEN":
        raise RuntimeError(f"freeze independent SHA256: {result_sha}")
    if result_sha != EXPECTED_RESULT_SHA256:
        raise RuntimeError("independent result digest changed")
    payload = {**result, "result_sha256": result_sha}
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"candidate_id": "HCS-P60", "check": True, "result_sha256": result_sha}, sort_keys=True))


if __name__ == "__main__":
    main()
