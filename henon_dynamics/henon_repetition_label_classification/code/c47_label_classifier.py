#!/usr/bin/env python3
"""Finite adversarial sentinels for the C47 rational classification theorem."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
TRACK = PROJECT.parent
DEFAULT_OUTPUT = PROJECT / "results" / "c47_certificate.json"
DEPENDENCIES = {
    "c46_readme": (
        TRACK / "henon_integral_monodromy_units" / "README.md",
        "700cce354f56c3b218984f2a8606d04b122304336c65735da86adb7f93cb9a47",
    ),
    "c46_certificate": (
        TRACK / "henon_integral_monodromy_units" / "results" / "c46_certificate.json",
        "43251f10b1c900921963b95648b0e95b15e70bdb6bd9d3a9674cf7b234f55f85",
    ),
}


def clean(polynomial: dict[int, int]) -> dict[int, int]:
    return {exponent: coefficient for exponent, coefficient in polynomial.items() if coefficient}


def square(polynomial: dict[int, int]) -> dict[int, int]:
    result: dict[int, int] = {}
    for left_exp, left_coefficient in polynomial.items():
        for right_exp, right_coefficient in polynomial.items():
            exponent = left_exp + right_exp
            result[exponent] = result.get(exponent, 0) + left_coefficient * right_coefficient
    return clean(result)


def substitute_square(polynomial: dict[int, int]) -> dict[int, int]:
    return clean({2 * exponent: coefficient for exponent, coefficient in polynomial.items()})


def satisfies_square_law(polynomial: dict[int, int]) -> bool:
    return substitute_square(polynomial) == square(polynomial)


def dependency_locks() -> dict[str, dict[str, str]]:
    locks: dict[str, dict[str, str]] = {}
    for name, (path, expected) in DEPENDENCIES.items():
        observed = hashlib.sha256(path.read_bytes()).hexdigest()
        if observed != expected:
            raise RuntimeError(f"dependency hash changed: {name}")
        locks[name] = {"path": str(path.relative_to(TRACK)), "sha256": observed}
    return locks


def laurent_scan(radius: int = 3) -> dict[str, object]:
    exponents = list(range(-radius, radius + 1))
    solutions: list[dict[str, object]] = []
    tested = 0
    for coefficients in itertools.product((-1, 0, 1), repeat=len(exponents)):
        polynomial = clean(dict(zip(exponents, coefficients)))
        tested += 1
        if satisfies_square_law(polynomial):
            solutions.append({"terms": [[exponent, coefficient] for exponent, coefficient in sorted(polynomial.items())]})
    expected = 1 + len(exponents)  # zero plus x^k for each exponent
    if len(solutions) != expected:
        raise ArithmeticError("unexpected Laurent-polynomial solution")
    return {"radius": radius, "tested": tested, "solutions": solutions, "solution_count": len(solutions)}


def build_certificate() -> dict[str, object]:
    scan = laurent_scan(3)
    trace = {-1: 1, 1: 1}
    fixed_det = {-1: -1, 0: 2, 1: -1}
    payload = {
        "candidate_id": "HCS-C47",
        "dependency_locks": dependency_locks(),
        "classification": {
            "rational_identity": "R(X^r)=R(X)^r for every r",
            "solutions": "R(X)=X^k, k in Z",
            "continuous_positive_unstable_ray_solutions": "L(X)=X^c, c in R",
            "status": "PROVED",
        },
        "finite_laurent_scan": scan,
        "counterexamples": {
            "trace_terms": [[exponent, coefficient] for exponent, coefficient in sorted(trace.items())],
            "trace_square_law": satisfies_square_law(trace),
            "fixed_determinant_terms": [
                [exponent, coefficient] for exponent, coefficient in sorted(fixed_det.items())
            ],
            "fixed_determinant_square_law": satisfies_square_law(fixed_det),
        },
        "henon_consequence": "rational repetition-compatible labels of H6 algebraic-unit multipliers remain units and cannot be rational primes",
        "survivor": "the non-rational pressure label |Lambda|^h_star",
        "status": "PROVED_RATIONAL_SCALAR_LABEL_NO_GO_WITH_PRESSURE_POWER_SURVIVOR",
        "claim_boundary": "rational classification is functorial on G_m; continuous repetition classification is restricted to the unstable ray X>1",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["payload_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = build_certificate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"check": True, "sha256": payload["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
