#!/usr/bin/env python3
"""Exact two-clock audit for the Fibonacci Schrödinger trace map.

The script preserves chronological word products and separates:

* finite-time section hits d_k(E)=0,+/-2; and
* three-coordinate returns T^m ell(E)=ell(E).

It uses no floating-point arithmetic.
"""

from __future__ import annotations

import argparse
import csv
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp


PRIME = 1_000_003


def fibonacci_words(max_k: int) -> dict[int, str]:
    words = {-1: "b", 0: "a"}
    for k in range(0, max_k):
        words[k + 1] = words[k] + words[k - 1]
    return words


def word_lengths(max_k: int) -> dict[int, int]:
    lengths = {-1: 1, 0: 1}
    for k in range(0, max_k):
        lengths[k + 1] = lengths[k] + lengths[k - 1]
    return lengths


def site_matrix(E: sp.Symbol, potential: sp.Expr) -> sp.Matrix:
    return sp.Matrix([[E - potential, -1], [1, 0]])


def chronological_monodromy(word: str, E: sp.Symbol, coupling: sp.Expr) -> sp.Matrix:
    result = sp.eye(2)
    for letter in word:
        potential = coupling if letter == "a" else 0
        # Later physical sites multiply on the left.
        result = site_matrix(E, potential) * result
    return sp.simplify(result)


def trace_polynomials(max_k: int, coupling: sp.Expr = 1) -> tuple[sp.Symbol, dict[int, sp.Expr]]:
    E = sp.symbols("E")
    d: dict[int, sp.Expr] = {-2: sp.Integer(2), -1: E, 0: E - coupling}
    for k in range(0, max_k):
        d[k + 1] = sp.expand(d[k] * d[k - 1] - d[k - 2])
    return E, d


def verify_chronological_products(max_k: int = 5) -> dict[str, object]:
    E, lam = sp.symbols("E lambda")
    words = fibonacci_words(max_k)
    _, d = trace_polynomials(max_k, lam)
    checks: list[dict[str, object]] = []
    for k in range(-1, max_k + 1):
        matrix_trace = sp.expand(sp.trace(chronological_monodromy(words[k], E, lam)))
        expected = d[k]
        if sp.expand(matrix_trace - expected) != 0:
            raise AssertionError(f"chronological trace mismatch at k={k}")
        checks.append(
            {
                "k": k,
                "word": words[k],
                "physical_length": len(words[k]),
                "degree_E": int(sp.degree(expected, E)),
                "verified": True,
            }
        )
    return {"checks": checks, "word_convention": "w[k+1]=w[k]w[k-1]; later sites multiply on the left"}


def half_trace_sequence(energy: int, coupling: int, through_k: int) -> dict[int, Fraction]:
    x: dict[int, Fraction] = {
        -2: Fraction(1),
        -1: Fraction(energy, 2),
        0: Fraction(energy - coupling, 2),
    }
    for k in range(0, through_k):
        x[k + 1] = 2 * x[k] * x[k - 1] - x[k - 2]
    return x


def first_escape_triple(sequence: dict[int, Fraction]) -> tuple[int, tuple[Fraction, Fraction, Fraction]]:
    keys = sorted(sequence)
    for n in keys:
        if n - 2 not in sequence:
            continue
        a, b, c = abs(sequence[n - 2]), abs(sequence[n - 1]), abs(sequence[n])
        if Fraction(1) < a < b < c:
            return n, (a, b, c)
    raise AssertionError("no strict escape triple found")


def recurrence_modulo(modulus_poly: sp.Poly, through_m: int, coupling: int = 1) -> dict[int, sp.Poly]:
    E = modulus_poly.gens[0]
    kwargs = {"modulus": modulus_poly.get_modulus()}

    def reduce_poly(expr: sp.Expr | sp.Poly) -> sp.Poly:
        poly = expr if isinstance(expr, sp.Poly) else sp.Poly(expr, E, **kwargs)
        return poly.rem(modulus_poly)

    d: dict[int, sp.Poly] = {
        -2: reduce_poly(2),
        -1: reduce_poly(E),
        0: reduce_poly(E - coupling),
    }
    for j in range(0, through_m):
        d[j + 1] = reduce_poly(d[j] * d[j - 1] - d[j - 2])
    return d


def simultaneous_gcd_degree(k: int, section_value: int, return_time: int, prime: int = PRIME) -> int:
    E, exact = trace_polynomials(k, 1)
    hit = sp.Poly(exact[k] - section_value, E, modulus=prime)
    reduced = recurrence_modulo(hit, return_time, coupling=1)
    targets = (
        reduced[return_time] - reduced[0],
        reduced[return_time - 1] - reduced[-1],
        reduced[return_time - 2] - reduced[-2],
    )
    common = hit
    for target in targets:
        common = sp.gcd(common, target)
    return int(common.degree())


def modular_gcd_audit(max_k: int = 8, prime: int = PRIME) -> list[dict[str, int | str]]:
    lengths = word_lengths(max_k)
    rows: list[dict[str, int | str]] = []
    E, d = trace_polynomials(max_k, 1)
    for k in range(1, max_k + 1):
        for label, value in (("discriminant_zero", 0), ("positive_band_edge", 2), ("negative_band_edge", -2)):
            for clock, return_time in (("renormalization_m_equals_k", k), ("physical_m_equals_qk", lengths[k])):
                degree = simultaneous_gcd_degree(k, value, return_time, prime)
                rows.append(
                    {
                        "k": k,
                        "q_k": lengths[k],
                        "degree_d_k": int(sp.degree(d[k], E)),
                        "section": label,
                        "section_value_d": value,
                        "return_clock": clock,
                        "return_time": return_time,
                        "simultaneous_gcd_degree_mod_p": degree,
                        "prime": prime,
                    }
                )
                if degree != 0:
                    raise AssertionError(f"unexpected common return factor at k={k}, value={value}, m={return_time}")
    return rows


def serialize_fraction(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def build_certificate() -> dict[str, object]:
    E, d = trace_polynomials(8, 1)
    if sp.factor(d[1] - (E * (E - 1) - 2)) != 0:
        raise AssertionError("first approximant polynomial mismatch")

    band = half_trace_sequence(energy=0, coupling=1, through_k=9)
    zero = half_trace_sequence(energy=-1, coupling=1, through_k=9)
    band_escape_at, band_triple = first_escape_triple(band)
    zero_escape_at, zero_triple = first_escape_triple(zero)

    x, y, z, lam = sp.symbols("x y z lambda")
    invariant = x**2 + y**2 + z**2 - 2 * x * y * z - 1
    initial_invariant = sp.factor(invariant.subs({x: (E - lam) / 2, y: E / 2, z: 1}))
    if sp.factor(initial_invariant - lam**2 / 4) != 0:
        raise AssertionError("Fricke invariant check failed")

    return {
        "candidate": "HCS-C13",
        "decision": "KILL_SECTION_HIT_EQUALS_TRACE_MAP_RETURN_AT_M_EQUALS_K_OR_QK",
        "arithmetic": "exact rational/integer polynomial computation; modular certificate over a prime field",
        "definitions": {
            "trace_map": "T(x,y,z)=(2*x*y-z,x,y)",
            "initial_line": "ell_lambda(E)=((E-lambda)/2,E/2,1)",
            "fricke_invariant_on_line": str(initial_invariant),
            "discriminant_recurrence": "d[k+1]=d[k]*d[k-1]-d[k-2]",
            "initial_traces": {"d[-2]": "2", "d[-1]": "E", "d[0]": "E-lambda"},
        },
        "first_nontrivial_approximant": {
            "word": "ab",
            "physical_length": 2,
            "d1": str(d[1]),
            "band_edge_counterexample": {
                "energy": 0,
                "d1_value": int(d[1].subs(E, 0)),
                "half_traces": {str(k): serialize_fraction(v) for k, v in band.items()},
                "escape_triple_ending_at_k": band_escape_at,
                "escape_absolute_values": [serialize_fraction(v) for v in band_triple],
            },
            "discriminant_zero_counterexample": {
                "energy": -1,
                "d1_value": int(d[1].subs(E, -1)),
                "half_traces": {str(k): serialize_fraction(v) for k, v in zero.items()},
                "escape_triple_ending_at_k": zero_escape_at,
                "escape_absolute_values": [serialize_fraction(v) for v in zero_triple],
            },
        },
        "logical_type": {
            "spectral_condition": "finite-time hit: T^k ell(E) lies on x=0,+1,-1",
            "periodic_condition": "three-coordinate return: T^m ell(E)=ell(E)",
            "clock_1": "substitution/renormalization level k",
            "clock_2": "physical word length q_k=F_{k+2}",
            "unweighted_artin_mazur_zeta": "closed-orbit function of z; it is not an energy polynomial",
            "weighted_fredholm_status": "NOT_TESTABLE until an energy-dependent operator, space, weights, variables, and normalization are defined",
            "correct_reframe": "marked finite-time section incidence; a boundary operator is only a provisional model",
            "claim_boundary": "the gcd certificate refutes only the two frozen section-hit/return identifications; it is not a no-go theorem for all weighted Fredholm determinants",
        },
    }


def write_results(out_dir: Path, max_k: int, prime: int) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    product_checks = verify_chronological_products(min(max_k, 5))
    gcd_rows = modular_gcd_audit(max_k=max_k, prime=prime)
    certificate = build_certificate()
    certificate["chronological_product_checks"] = product_checks
    certificate["modular_gcd_summary"] = {
        "max_k": max_k,
        "prime": prime,
        "tests": len(gcd_rows),
        "all_gcd_degrees_zero": all(row["simultaneous_gcd_degree_mod_p"] == 0 for row in gcd_rows),
    }

    with (out_dir / "certificate.json").open("w", encoding="utf-8") as handle:
        json.dump(certificate, handle, indent=2, sort_keys=True)
        handle.write("\n")
    with (out_dir / "modular_gcd_audit.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(gcd_rows[0]))
        writer.writeheader()
        writer.writerows(gcd_rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", type=Path, default=Path("results"))
    parser.add_argument("--max-k", type=int, default=8)
    parser.add_argument("--prime", type=int, default=PRIME)
    args = parser.parse_args()
    if not sp.isprime(args.prime):
        parser.error("--prime must be prime")
    if not 1 <= args.max_k <= 10:
        parser.error("--max-k must lie between 1 and 10")
    write_results(args.out_dir, args.max_k, args.prime)
    print(f"wrote exact HCS-C13 audit to {args.out_dir}")


if __name__ == "__main__":
    main()
