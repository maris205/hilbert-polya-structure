#!/usr/bin/env python3
"""Produce the exact HCS-C145 Rule-90 two-clock certificate."""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c145_rule90_evidence.json"
LIMIT = 24


def degree(polynomial: int) -> int:
    return polynomial.bit_length() - 1


def multiply(left: int, right: int) -> int:
    result = 0
    while right:
        if right & 1:
            result ^= left
        right >>= 1
        left <<= 1
    return result


def power(base: int, exponent: int) -> int:
    result = 1
    while exponent:
        if exponent & 1:
            result = multiply(result, base)
        base = multiply(base, base)
        exponent >>= 1
    return result


def remainder(dividend: int, divisor: int) -> int:
    divisor_degree = degree(divisor)
    while dividend and degree(dividend) >= divisor_degree:
        dividend ^= divisor << (degree(dividend) - divisor_degree)
    return dividend


def polynomial_gcd(left: int, right: int) -> int:
    while right:
        left, right = right, remainder(left, right)
    return left


def mobius(n: int) -> int:
    primes = 0
    p = 2
    remaining = n
    while p * p <= remaining:
        if remaining % p == 0:
            remaining //= p
            primes += 1
            if remaining % p == 0:
                return 0
            while remaining % p == 0:
                remaining //= p
        p += 1
    if remaining > 1:
        primes += 1
    return -1 if primes % 2 else 1


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def gcd_degree(length: int, time: int) -> int:
    spatial = (1 << length) | 1
    cleared = power((1 << 2) | 1, time) ^ (1 << time)
    return degree(polynomial_gcd(spatial, cleared))


def fixed_count(length: int, time: int) -> int:
    return 1 << gcd_degree(length, time)


def exact_period_points(length: int, time: int) -> int:
    return sum(mobius(time // d) * fixed_count(length, d) for d in divisors(time))


def row(length: int, time: int) -> dict:
    exact = exact_period_points(length, time)
    assert exact >= 0 and exact % time == 0
    return {
        "spatial_length_L": length,
        "temporal_period_n": time,
        "area_Ln": length * time,
        "gcd_degree": gcd_degree(length, time),
        "fixed_points": fixed_count(length, time),
        "exact_temporal_period_points": exact,
        "primitive_temporal_cycles": exact // time,
    }


def first_area_witness(rows: list[dict], nondegenerate: bool, require_nonzero_exact: bool = False) -> dict:
    selected = [r for r in rows if not nondegenerate or (r["spatial_length_L"] >= 2 and r["temporal_period_n"] >= 2)]
    for area in range(1, LIMIT * LIMIT + 1):
        group = [r for r in selected if r["area_Ln"] == area]
        if len({r["fixed_points"] for r in group}) > 1 and (not require_nonzero_exact or any(r["exact_temporal_period_points"] > 0 for r in group)):
            return {"area": area, "cells": group}
    raise AssertionError("witness not found")


def payload_bytes(data: dict) -> bytes:
    body = dict(data)
    body.pop("payload_sha256", None)
    return json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def build() -> dict:
    rows = [row(length, time) for length in range(1, LIMIT + 1) for time in range(1, LIMIT + 1)]
    lookup = {(r["spatial_length_L"], r["temporal_period_n"]): r for r in rows}
    same_fixed_control = {
        "first_cell": lookup[(5, 3)],
        "second_cell": lookup[(5, 6)],
        "statement": "both fixed-point counts are 16, but n=3 has 15 exact-period points and five primitive cycles whereas n=6 has none",
    }
    assert lookup[(5, 3)]["fixed_points"] == lookup[(5, 6)]["fixed_points"] == 16
    assert lookup[(5, 3)]["exact_temporal_period_points"] == 15
    assert lookup[(5, 6)]["exact_temporal_period_points"] == 0
    full_area = first_area_witness(rows, nondegenerate=False)
    nondegenerate_area = first_area_witness(rows, nondegenerate=True)
    nonzero_area = first_area_witness(rows, nondegenerate=True, require_nonzero_exact=True)
    assert full_area["area"] == 3
    assert nondegenerate_area["area"] == 6
    assert nonzero_area["area"] == 12

    data = {
        "schema": "HCS-C145-v1",
        "candidate_id": "HCS-C145",
        "date_utc": "2026-08-25",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "source_lock": {
            "object": "Rule-90 on the cyclic binary lattice R_L=F_2[x,x^{-1}]/(x^L-1), with F_L multiplication by a=x+x^{-1}",
            "clock": "the ordered pair (spatial circumference L, temporal iterate n)",
            "normalization": "Fix(L,n) counts labeled spatial configurations fixed by F_L^n; exact-period points are divided by n only after temporal Mobius inversion",
            "determinant_convention": "no single-variable determinant is asserted; the frozen object is the exact two-clock fixed-point table",
            "precision": "exact F_2 polynomial arithmetic and exact integers",
            "cutoff": "the theorem is all L,n>=1; the replay ledger is 1<=L,n<=24",
            "allowed_data": "the Rule-90 local rule and computations derived from it",
            "forbidden_data": "external prime or zero tables, arithmetic/local factors, root numbers, automorphy claims, and Route-B inputs",
        },
        "kernel_gcd_theorem": {
            "statement": "#Fix(F_L^n)=2^deg(gcd(x^L+1,(x^2+1)^n+x^n)) for all L,n>=1 over F_2",
            "laurent_clearance": "x^n((x+x^{-1})^n-1)=(x^2+1)^n+x^n in characteristic two; multiplication by x^n is invertible modulo x^L+1",
            "kernel_lemma": "for monic f and h over a field, dim ker(m_h:k[x]/(f)->k[x]/(f))=deg gcd(f,h)",
            "kernel_proof": "writing f=g f_1 and h=g h_1 with gcd(f_1,h_1)=1, the annihilation condition f|hq is equivalent to f_1|q; the residue classes f_1 r with deg r<deg g form a basis",
            "non_squarefree_scope": "the proof uses ideal divisibility, not distinct roots, so it includes every even L for which x^L+1 may be non-squarefree",
            "all_positive_lengths_and_times": True,
        },
        "mobius_orbit_theorem": {
            "exact_period_formula": "P_L(n)=sum_(d|n) mu(n/d) Fix(L,d)",
            "cycle_formula": "C_L(n)=P_L(n)/n",
            "integrality_reason": "F_L acts on a finite set; exact-period-n points are partitioned into temporal cycles of size n",
            "point_cycle_boundary": "Fix(L,n), P_L(n), and C_L(n) are distinct quantities and are never interchanged",
        },
        "two_clock_table": {
            "spatial_limit": LIMIT,
            "temporal_limit": LIMIT,
            "cell_count": len(rows),
            "rows": rows,
            "fixed_point_sum": sum(r["fixed_points"] for r in rows),
            "exact_period_point_sum": sum(r["exact_temporal_period_points"] for r in rows),
            "primitive_cycle_sum": sum(r["primitive_temporal_cycles"] for r in rows),
        },
        "spatiotemporal_torus": {
            "equations": "u_(i,j+1)=u_(i-1,j)+u_(i+1,j) in F_2 with i mod L and j mod n",
            "bijection": "a torus is uniquely determined by its row j=0, and closure in time is exactly F_L^n u=u",
            "torus_count": "the number of labeled L-by-n tori is Fix(L,n)",
        },
        "aspect_ratio_witnesses": {
            "global_positive_domain": {
                "search_domain": "1<=L,n<=24, ordered by increasing area; all positive divisors of each area included",
                "minimal_same_area_with_different_fixed_counts": full_area,
            },
            "nondegenerate_domain": {
                "search_domain": "2<=L,n<=24, ordered by increasing area; all eligible divisors of each area included",
                "minimal_same_area_with_different_fixed_counts": nondegenerate_area,
            },
            "nonzero_exact_period_domain": {
                "search_domain": "2<=L,n<=24 with at least one witness cell having P_L(n)>0",
                "minimal_same_area_with_different_fixed_counts": nonzero_area,
            },
            "same_fixed_count_different_primitive_structure": same_fixed_control,
            "conclusion": "area Ln and a single fixed-point count each lose information retained by the ordered two-clock geometry and its divisor history",
        },
        "even_length_control": {
            "cell": lookup[(6, 2)],
            "factorization": "x^6+1=(x^3+1)^2 over F_2",
            "purpose": "explicit non-squarefree sentinel for the kernel-gcd theorem",
        },
        "progress_and_boundary": {
            "progress": "constructs an all-size exact spatiotemporal periodic table for a local linear cellular automaton and separates points from primitive temporal cycles",
            "two_clock_obstruction": "collapsing (L,n) to area loses aspect ratio, while one fixed count loses divisor-history information",
            "route_a_obstruction": "the family has intrinsic finite-volume periodic structure but no single frozen circumference, clock, or target determinant",
        },
        "route_a": {
            "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall": "ROUTE_A_EXPLORATORY",
            "A1_qualification": "EXACT_INTRINSIC_FINITE_VOLUME_TEMPORAL_CYCLES_WITH_ESSENTIAL_TWO_CLOCK_DEPENDENCE",
            "A2_qualification": "NO_SINGLE_FROZEN_CLOCK_OR_TARGET_DIVISOR_DETERMINANT",
            "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_OR_CONTINUATION_COMPARISON",
            "A4_qualification": "NO_NATURAL_UNITARY_SCATTERING_OR_HAMILTONIAN_LIFT",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": {
            "scope": "NO_BAD_EULER_OR_ROOT_NUMBER",
            "uses_prime_table": False,
            "uses_zero_table": False,
            "claims_arithmetic_euler_factors": False,
            "claims_root_number": False,
            "claims_automorphy": False,
            "claims_hilbert_polya": False,
            "uses_route_b_inputs": False,
        },
        "nonclaims": [
            "a thermodynamic or infinite-volume limit of the two-clock table",
            "that area alone determines spatiotemporal periodic geometry",
            "an arithmetic Euler product or local factorization",
            "a target divisor, functional equation, or counting-law match",
            "a natural self-adjoint Hilbert--Polya operator",
            "Route-B authorization or a solution of the larger program",
        ],
    }
    data["payload_sha256"] = sha256(payload_bytes(data)).hexdigest()
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "C145_PRODUCER_PASS", "output": str(args.output), "payload_sha256": data["payload_sha256"], "cells": data["two_clock_table"]["cell_count"]}, sort_keys=True))


if __name__ == "__main__":
    main()
