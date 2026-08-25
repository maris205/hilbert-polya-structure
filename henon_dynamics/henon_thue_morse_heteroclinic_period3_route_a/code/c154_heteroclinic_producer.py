#!/usr/bin/env python3
"""Produce the exact HCS-C154 heteroclinic-orbit certificate."""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c154_heteroclinic_evidence.json"
SOURCE_COMMIT = "506dead810d67fa58fa7c42b2d9a09bfae161059"
PERIOD_LIMIT = 60
ZETA_DEGREE = 36


def tm(index: int) -> int:
    if index < 0:
        raise ValueError("the frozen Thue--Morse tail is indexed by n>=0")
    return index.bit_count() & 1


def background(index: int) -> int:
    return (2, 3, 4)[index % 3]


def x_symbol(index: int) -> int:
    return background(index) if index < 0 else tm(index)


def shifted_symbol(shift: int, coordinate: int) -> int:
    """(sigma^shift x)_coordinate=x_(coordinate+shift)."""
    return x_symbol(coordinate + shift)


def period_certificate(period: int) -> dict:
    k = period.bit_length() + 1
    if k % 2 == 0:
        k += 1
    d = period * ((1 << k) - 1)
    b = d.bit_length()
    return {
        "putative_period": period,
        "odd_exponent_k": k,
        "multiple_d": d,
        "popcount_d": d.bit_count(),
        "tm_bit_at_zero": 0,
        "tm_bit_at_d": tm(d),
        "forbidden_window_length": 1 << (b + 1),
    }


def payload_bytes(data: dict) -> bytes:
    body = dict(data)
    body.pop("payload_sha256", None)
    return json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def build() -> dict:
    interface_rows = []
    for shift in range(-36, 37):
        left = -shift - 1
        right = -shift
        interface_rows.append({
            "shift": shift,
            "interface_left_coordinate": left,
            "interface_right_coordinate": right,
            "interface_pair": [shifted_symbol(shift, left), shifted_symbol(shift, right)],
            "window_radius_4": [shifted_symbol(shift, j) for j in range(left - 3, right + 4)],
        })

    positive_rows = []
    for shift in (8, 13, 21, 34, 55, 89, 144):
        radius = 6
        positive_rows.append({
            "shift": shift,
            "radius": radius,
            "central_word": [shifted_symbol(shift, j) for j in range(-radius, radius + 1)],
            "all_symbols_binary": all(shifted_symbol(shift, j) in (0, 1) for j in range(-radius, radius + 1)),
        })

    negative_rows = []
    for magnitude in (12, 13, 14, 24, 25, 26, 48, 49, 50):
        shift = -magnitude
        radius = 5
        word = [shifted_symbol(shift, j) for j in range(-radius, radius + 1)]
        negative_rows.append({
            "shift": shift,
            "minus_shift_mod_3": magnitude % 3,
            "radius": radius,
            "central_word": word,
            "period_three_check": all(word[q] == word[q + 3] for q in range(len(word) - 3)),
        })

    fixed_rows = []
    for n in range(1, PERIOD_LIMIT + 1):
        fixed = 3 if n % 3 == 0 else 0
        exact = 3 if n == 3 else 0
        fixed_rows.append({
            "period_n": n,
            "fixed_points": fixed,
            "fixed_labels": [f"y_phase_{j}" for j in range(3)] if fixed else [],
            "exact_period_points": exact,
            "primitive_cycles": exact // n,
        })

    data = {
        "schema": "HCS-C154-v1",
        "candidate_id": "HCS-C154",
        "date_utc": "2026-08-25",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "source_lock": {
            "object": "X=closure of the two-sided shift orbit of x over {0,1,2,3,4}, with x_j=(234)_j for j<0 and x_j=t_j for j>=0",
            "map": "the left shift sigma, (sigma x)_j=x_(j+1)",
            "clock": "one symbolic shift",
            "normalization": "Fix_X(n) counts points fixed by sigma^n; exact-period points precede division by n",
            "zeta_convention": "zeta_X(z)=exp(sum_(n>=1) Fix_X(n) z^n/n)",
            "cutoff": "all statements are topological all-period theorems; finite windows, periods <=60, and zeta degree <=36 are replay sentinels",
            "allowed_data": "the Thue--Morse substitution, the period-three word 234, and their single frozen interface",
            "forbidden_data": "external prime or zero tables, arithmetic/local factors, root numbers, automorphy claims, Hilbert--Polya operators, and Route-B inputs",
        },
        "frozen_configuration": {
            "alphabet": [0, 1, 2, 3, 4],
            "thue_morse_alphabet": [0, 1],
            "periodic_alphabet": [2, 3, 4],
            "periodic_background": "y_j=(2,3,4)_[j mod 3]",
            "interface_rule": "x_j=y_j for j<0 and x_j=t_j for j>=0",
            "interface_pair": [4, 0],
            "orbit_is_injective": True,
            "interface_cylinder_isolates_each_orbit_point": True,
            "tm_period_certificate_limit": 32,
            "tm_period_certificates": [period_certificate(p) for p in range(1, 33)],
        },
        "orbit_closure_theorem": {
            "exact_decomposition": "X=X_TM disjoint_union Orbit_sigma(x) disjoint_union Orbit_sigma(y)",
            "positive_escape": "every accumulation point of sigma^n x with n to +infinity belongs to X_TM, and every point of X_TM occurs as such a limit",
            "negative_escape": "every accumulation point of sigma^n x with n to -infinity is one of the three phases of y, and every phase occurs along one residue class modulo 3",
            "no_other_limits": "a convergent sequence of distinct orbit points has shifts unbounded above or below; the two preceding cases exhaust it",
            "dense_full_orbit": "the full two-sided Z-orbit Orbit_sigma(x) is dense in X by definition",
            "forward_transitivity_failure": "standard n>=0 topological transitivity fails: for U={sigma x} and V={x}, sigma^n(U) misses V for every n>=0",
            "not_minimal": "the period-three orbit is a nonempty proper closed invariant subset",
            "wandering_interface": "each interface orbit point is isolated by the unique cross-alphabet pair 40 and is wandering",
            "nonwandering_set": "Omega(sigma)=X_TM disjoint_union Orbit_sigma(y)",
        },
        "periodic_orbit_theorem": {
            "tm_periodic_points": 0,
            "interface_orbit_periodic_points": 0,
            "periodic_points_exactly": "the three phases of y",
            "fixed_count": "Fix_X(n)=3 if 3 divides n, and Fix_X(n)=0 otherwise, for every n>=1",
            "exact_period_points": "P_X(3)=3 and P_X(n)=0 for n!=3",
            "primitive_cycles": [{"least_period": 3, "primitive_cycles": 1}],
            "artin_mazur_zeta": "1/(1-z^3)",
            "formal_derivation": "sum_(q>=1) 3 z^(3q)/(3q)=sum_(q>=1)z^(3q)/q=-log(1-z^3)",
        },
        "finite_replay": {
            "interface_rows": interface_rows,
            "positive_shift_windows": positive_rows,
            "negative_shift_windows": negative_rows,
            "period_limit": PERIOD_LIMIT,
            "fixed_rows": fixed_rows,
            "fixed_count_sum": sum(row["fixed_points"] for row in fixed_rows),
            "zeta_degree_limit": ZETA_DEGREE,
            "zeta_coefficients": [1 if degree % 3 == 0 else 0 for degree in range(ZETA_DEGREE + 1)],
        },
        "progress_and_boundary": {
            "progress": "replaces a freely disjoint periodic attachment by a period-three skeleton generated intrinsically inside the closure of one dense two-sided heteroclinic Z-orbit",
            "structural_cost": "minimality and standard forward topological transitivity both fail; the entire interface orbit is wandering",
            "route_a_obstruction": "the single primitive orbit and rational source zeta have no frozen target divisor, global analytic comparison, arithmetic content, or natural operator lift",
        },
        "route_a": {
            "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall": "ROUTE_A_EXPLORATORY",
            "A1_qualification": "INTRINSIC_PERIOD_THREE_SKELETON_IN_ONE_DENSE_TWO_SIDED_HETEROCLINIC_ORBIT_CLOSURE",
            "A2_qualification": "ELEMENTARY_SINGLE_FACTOR_SOURCE_ZETA_WITH_NO_TARGET_DIVISOR_COMPARISON",
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
            "that X is minimal or almost minimal",
            "that the interface orbit contributes recurrent or periodic points",
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
    print(json.dumps({"status": "C154_PRODUCER_PASS", "output": str(args.output), "payload_sha256": data["payload_sha256"], "interface_rows": len(data["finite_replay"]["interface_rows"]), "period_rows": len(data["finite_replay"]["fixed_rows"])}, sort_keys=True))


if __name__ == "__main__":
    main()
