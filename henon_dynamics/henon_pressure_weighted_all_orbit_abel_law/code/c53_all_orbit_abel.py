#!/usr/bin/env python3
"""Produce the HCS-P53 pressure-weighted all-orbit Abel certificate.

The infinite theorem is proved in ``PROOF_PACKAGE.md``.  This producer checks
the exact trace-field packets on three inherited H6 orbits, stresses the
unit-circle branch on a separate reciprocal Salem polynomial, and records
finite Abel and joint-profile sentinels.  The finite rows illustrate the
proved theorem; they do not replace the all-orbit proof.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any

import mpmath as mp
import sympy as sp


PROJECT = Path(__file__).resolve().parents[1]
TRACK = PROJECT.parent
DEFAULT_OUTPUT = PROJECT / "results" / "c53_certificate.json"
X, T = sp.symbols("X T")

DEPENDENCIES = {
    "p51_readme": (
        TRACK / "henon_abel_graded_all_orbit_packet_germ" / "README.md",
        "f7a74f694aae8007ed1ecd7318efdba4f7afd771f7f8e8cee0ea9445589c97b5",
    ),
    "p51_proof": (
        TRACK / "henon_abel_graded_all_orbit_packet_germ" / "PROOF_PACKAGE.md",
        "e0d6f5ba7b45f1881fc9bd6fafbb919b58276cf29e538a50e1f8ab2ae8594b7d",
    ),
    "p51_certificate": (
        TRACK / "henon_abel_graded_all_orbit_packet_germ" / "results" / "c51_certificate.json",
        "dcb5369c6ba50c0eda2011ba595ed9f1f21ab9bfe0c27d93e8e22d6da38fafaf",
    ),
    "p52_readme": (
        TRACK / "henon_totient_abel_boundary_escape" / "README.md",
        "98de4be39b7a2b8ce98571ca8008e908ea5664c9524098919b95b29f8ec28f01",
    ),
    "p52_proof": (
        TRACK / "henon_totient_abel_boundary_escape" / "PROOF_PACKAGE.md",
        "8743bb1a1fc3c6694d948fd79681825e8cd114ddca299480b162d8f87b7f2f25",
    ),
    "p52_certificate": (
        TRACK / "henon_totient_abel_boundary_escape" / "results" / "c52_certificate.json",
        "4b7fbe8e73791c7562e43d572acabe33db6672187341fa6f6f86084e0f48de1f",
    ),
    "p50_certificate": (
        TRACK / "henon_tagged_prime_ideal_packet_assembly" / "results" / "c50_certificate.json",
        "1ed3f3f7c6c534197b21a2a8b7ec8d58ef6fdf9d0706d115430bab3351b8c4fd",
    ),
}


ORBIT_SPECS: dict[str, dict[str, Any]] = {
    "period_1": {
        "source_native_h6": True,
        "primitive_period": 1,
        "trace_polynomial": sp.Poly(T**2 - 4 * T - 24, T),
        "multiplier_polynomial": sp.Poly(X**4 - 4 * X**3 - 22 * X**2 - 4 * X + 1, X),
        "physical_trace": 2 + 2 * sp.sqrt(7),
    },
    "period_3": {
        "source_native_h6": True,
        "primitive_period": 3,
        "trace_polynomial": sp.Poly(T**2 + 76 * T - 7376, T),
        "multiplier_polynomial": sp.Poly(X**4 + 76 * X**3 - 7374 * X**2 + 76 * X + 1, X),
        "physical_trace": -38 - 42 * sp.sqrt(5),
    },
    "period_4": {
        "source_native_h6": True,
        "primitive_period": 4,
        "trace_polynomial": sp.Poly(T - 578, T),
        "multiplier_polynomial": sp.Poly(X**2 - 578 * X + 1, X),
        "physical_trace": sp.Integer(578),
    },
    # This reciprocal polynomial is not asserted to arise from H6.  Its trace
    # polynomial has one root in (-2,2), so it exercises the unit-circle
    # conjugate branch that the all-orbit proof must allow.
    "abstract_salem_stress": {
        "source_native_h6": False,
        "primitive_period": None,
        "trace_polynomial": sp.Poly(T**2 - T - 3, T),
        "multiplier_polynomial": sp.Poly(X**4 - X**3 - X**2 - X + 1, X),
        "physical_trace": (1 + sp.sqrt(13)) / 2,
    },
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_sha(payload: object) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def dependency_locks() -> dict[str, dict[str, str]]:
    locks: dict[str, dict[str, str]] = {}
    for name, (path, expected) in DEPENDENCIES.items():
        observed = sha256(path)
        if observed != expected:
            raise RuntimeError(
                f"dependency hash changed for {name}: expected {expected}, observed {observed}"
            )
        locks[name] = {"path": str(path.relative_to(TRACK)), "sha256": observed}
    return locks


def beta_trace_polynomial(index: int) -> sp.Expr:
    """Return X^(-phi(n)/2) Phi_n(X) as a polynomial in T=X+X^-1."""
    if index <= 2:
        raise ValueError("the inversion-fixed half packet begins at index 3")
    polynomial = sp.Poly(sp.cyclotomic_poly(index, X), X)
    half = int(sp.totient(index)) // 2
    laurent = {
        int(power[0] - half): sp.Integer(coefficient)
        for power, coefficient in polynomial.terms()
    }
    symmetric = {0: sp.Integer(2), 1: T}
    for power in range(2, half + 1):
        symmetric[power] = sp.expand(T * symmetric[power - 1] - symmetric[power - 2])
    result = sp.Integer(laurent.get(0, 0))
    for power in range(1, half + 1):
        if laurent.get(power, 0) != laurent.get(-power, 0):
            raise ArithmeticError(f"cyclotomic reciprocity failed at n={index}")
        result += laurent.get(power, 0) * symmetric[power]
    return sp.expand(result)


def exact_half_norm(spec: dict[str, Any], index: int) -> int:
    packet = beta_trace_polynomial(index)
    value = int(sp.resultant(spec["trace_polynomial"].as_expr(), packet, T))
    if value == 0:
        raise ArithmeticError(f"zero half packet at n={index}")
    return abs(value)


def complex_roots(poly: sp.Poly, digits: int = 70) -> list[mp.mpc]:
    roots = sp.nroots(poly, n=digits, maxsteps=500)
    return [mp.mpc(str(sp.re(root)), str(sp.im(root))) for root in roots]


def trace_lifts(spec: dict[str, Any]) -> list[mp.mpc]:
    lifts: list[mp.mpc] = []
    for trace in complex_roots(spec["trace_polynomial"]):
        discriminant = mp.sqrt(trace * trace - 4)
        first = (trace + discriminant) / 2
        second = (trace - discriminant) / 2
        chosen = first if abs(first) >= abs(second) else second
        if abs(chosen) < 1 - mp.mpf("1e-45"):
            raise ArithmeticError("reciprocal trace lift has modulus below one")
        lifts.append(chosen)
    return lifts


def spectral_height(spec: dict[str, Any]) -> mp.mpf:
    return mp.fsum(mp.log(max(mp.mpf(1), abs(root))) for root in trace_lifts(spec))


def physical_multiplier(spec: dict[str, Any]) -> mp.mpf:
    trace = mp.mpf(str(sp.N(spec["physical_trace"], 80)))
    discriminant = mp.sqrt(trace * trace - 4)
    first = (trace + discriminant) / 2
    second = (trace - discriminant) / 2
    return max(abs(first), abs(second))


def divisors(value: int) -> list[int]:
    small: list[int] = []
    large: list[int] = []
    candidate = 1
    while candidate * candidate <= value:
        if value % candidate == 0:
            small.append(candidate)
            if candidate * candidate != value:
                large.append(value // candidate)
        candidate += 1
    return small + list(reversed(large))


def mobius(value: int) -> int:
    return int(sp.mobius(value))


def totient(value: int) -> int:
    return int(sp.totient(value))


def log_half_norm_formula(index: int, lifts: list[mp.mpc]) -> mp.mpf:
    """Evaluate the embedding formula, including unit-circle conjugates."""
    total = mp.mpf(0)
    for root in lifts:
        modulus = abs(root)
        if modulus > 1 + mp.mpf("1e-35"):
            total += mp.mpf(totient(index)) * mp.log(modulus) / 2
            total += mp.fsum(
                mp.mpf(mobius(index // divisor))
                * mp.log(abs(1 - root ** (-divisor)))
                for divisor in divisors(index)
            )
        else:
            total += mp.fsum(
                mp.mpf(mobius(index // divisor))
                * mp.log(abs(1 - root**divisor))
                for divisor in divisors(index)
            )
    return total


def packet_rows(spec: dict[str, Any], max_index: int) -> list[dict[str, Any]]:
    lifts = trace_lifts(spec)
    height = spectral_height(spec)
    rows: list[dict[str, Any]] = []
    for index in range(3, max_index + 1):
        norm = exact_half_norm(spec, index)
        direct = mp.log(norm)
        formula = log_half_norm_formula(index, lifts)
        main = mp.mpf(totient(index)) * height / 2
        rows.append(
            {
                "index": index,
                "totient": totient(index),
                "absolute_half_norm": str(norm),
                "log_norm": float(direct),
                "embedding_formula_abs_error": float(abs(direct - formula)),
                "main_term": float(main),
                "remainder": float(direct - main),
                "remainder_over_sqrt_n_log2": float(
                    abs(direct - main) / (mp.sqrt(index) * (1 + mp.log(index)) ** 2)
                ),
            }
        )
    return rows


def finite_abel(spec: dict[str, Any], tau: mp.mpf, cutoff: int) -> mp.mpf:
    lifts = trace_lifts(spec)
    return mp.fsum(
        log_half_norm_formula(index, lifts) * mp.e ** (-tau * index)
        for index in range(3, cutoff + 1)
    )


def abel_rows(spec: dict[str, Any]) -> list[dict[str, Any]]:
    height = spectral_height(spec)
    target = 3 * height / mp.pi**2
    rows: list[dict[str, Any]] = []
    for tau_text in ("0.2", "0.1", "0.05", "0.025"):
        tau = mp.mpf(tau_text)
        cutoff = int(mp.ceil(35 / tau))
        value = finite_abel(spec, tau, cutoff)
        rows.append(
            {
                "tau": float(tau),
                "cutoff": cutoff,
                "tau_squared_Z": float(tau**2 * value),
                "target_3H_over_pi2": float(target),
                "ratio_to_target": float(tau**2 * value / target),
            }
        )
    return rows


def sample_pressure_profile(specs: dict[str, dict[str, Any]]) -> dict[str, Any]:
    p51 = json.loads(
        (TRACK / "henon_abel_graded_all_orbit_packet_germ" / "results" / "c51_certificate.json").read_text()
    )
    sigma = mp.mpf(str(p51["constants"]["sigma_certified"])) + mp.mpf("0.25")
    h_star = mp.mpf(str(p51["constants"]["pressure_lower"]))
    source_names = ["period_1", "period_3", "period_4"]
    weights: dict[str, mp.mpf] = {}
    heights: dict[str, mp.mpf] = {}
    for name in source_names:
        heights[name] = spectral_height(specs[name])
        length = h_star * mp.log(physical_multiplier(specs[name]))
        weights[name] = mp.e ** (-sigma * length)
    target_sum = mp.fsum(weights[name] * heights[name] for name in source_names)
    target = 3 * target_sum / mp.pi**2
    rows: list[dict[str, Any]] = []
    for tau_text in ("0.2", "0.1", "0.05", "0.025"):
        tau = mp.mpf(tau_text)
        cutoff = int(mp.ceil(35 / tau))
        z = mp.fsum(
            weights[name] * finite_abel(specs[name], tau, cutoff)
            for name in source_names
        )
        profiles = []
        for laplace_text in ("0.5", "1", "2"):
            laplace = mp.mpf(laplace_text)
            numerator = mp.fsum(
                weights[name] * finite_abel(specs[name], (1 + laplace) * tau, cutoff)
                for name in source_names
            )
            profiles.append(
                {
                    "r": float(laplace),
                    "observed": float(numerator / z),
                    "target_gamma_2_1": float((1 + laplace) ** -2),
                }
            )
        rows.append(
            {
                "tau": float(tau),
                "cutoff": cutoff,
                "tau_squared_Z": float(tau**2 * z),
                "target": float(target),
                "ratio_to_target": float(tau**2 * z / target),
                "scaled_index_laplace": profiles,
            }
        )
    orbit_weights = {
        name: float(weights[name] * heights[name] / target_sum) for name in source_names
    }
    return {
        "sigma": float(sigma),
        "h_star_used_for_finite_sentinel": float(h_star),
        "orbit_limit_weights": orbit_weights,
        "rows": rows,
    }


def build_certificate(max_index: int = 72) -> dict[str, Any]:
    if max_index < 36 or max_index > 100:
        raise ValueError("max_index must lie in [36,100]")
    mp.mp.dps = 90
    orbit_payload: dict[str, Any] = {}
    for name, spec in ORBIT_SPECS.items():
        height = spectral_height(spec)
        roots = complex_roots(spec["multiplier_polynomial"])
        unit_circle_count = sum(abs(abs(root) - 1) < mp.mpf("1e-25") for root in roots)
        rows = packet_rows(spec, max_index)
        if max(row["embedding_formula_abs_error"] for row in rows) > 1e-55:
            raise ArithmeticError(f"embedding formula failed for {name}")
        orbit_payload[name] = {
            "source_native_h6": spec["source_native_h6"],
            "primitive_period": spec["primitive_period"],
            "trace_polynomial": str(spec["trace_polynomial"].as_expr()),
            "multiplier_polynomial": str(spec["multiplier_polynomial"].as_expr()),
            "trace_degree": spec["trace_polynomial"].degree(),
            "unit_circle_multiplier_conjugates": unit_circle_count,
            "spectral_height_log_mahler": float(height),
            "physical_multiplier_modulus": float(physical_multiplier(spec)),
            "packet_rows": rows,
            "abel_rows": abel_rows(spec),
        }

    p51 = json.loads(
        (TRACK / "henon_abel_graded_all_orbit_packet_germ" / "results" / "c51_certificate.json").read_text()
    )
    sigma_certified = float(p51["constants"]["sigma_certified"])
    payload: dict[str, Any] = {
        "schema": "hcs-p53-pressure-weighted-all-orbit-abel-law-v1",
        "candidate_id": "HCS-P53",
        "dependency_locks": dependency_locks(),
        "source_object": {
            "map": "H_6(q,p)=(1-6q^2-p,q)",
            "primitive_orbits": "all primitive orbits in the certified H6 symbolic survivor",
            "packet_mass": "b_(gamma,n)=log|N_(F_gamma/Q) beta_(gamma,n)|",
            "spectral_height": "H_gamma=log Mahler(f_lambda_gamma)",
            "pressure_length": "ellhat_gamma=h_star*log Lambda_gamma",
        },
        "theorem_constants": {
            "sigma_exact": "log(2*golden_ratio)/(h_star*log(J_star))",
            "sigma_certified": sigma_certified,
            "per_orbit_abel_coefficient": "3*H_gamma/pi^2",
            "totient_laplace_constant": "lim tau^2 sum phi(n)e^(-tau*n)=6/pi^2",
            "unit_circle_error": "O_gamma(sqrt(n)*(1+log n)^2)",
        },
        "orbit_sentinels": orbit_payload,
        "sample_pressure_profile": sample_pressure_profile(ORBIT_SPECS),
        "theorem_ledger": {
            "per_orbit_spectral_height_asymptotic": "PROVED_SOURCE_BACKED",
            "pressure_weighted_all_orbit_abel_interchange": "PROVED_IN_P51_SAFE_HALF_PLANE",
            "locally_uniform_complex_s_limit": "PROVED",
            "joint_orbit_index_product_limit": "PROVED",
            "scaled_index_gamma_2_1_profile": "PROVED",
            "tagged_banach_boundary": "REFUTED_NO_NORM_OR_WEAKLY_CONVERGENT_SUBNET",
            "continuation_to_pressure_boundary": "OPEN",
            "rational_prime_von_mangoldt_trace": "OPEN",
            "fredholm_determinant": "OPEN",
            "hilbert_polya_operator": "OPEN",
        },
        "route_a": {
            "tuple": ["A1_WEAK", "A2_FAIL", "A3_PARTIAL_ANALYTIC_STRUCTURE", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_EXPLORATORY",
        },
        "strongest_positive_result": "pressure-weighted all-orbit scalar Abel boundary and joint orbit-index Gamma product law in the certified right half-plane",
        "strongest_obstruction": "the renormalized source-tagged divisor vector has no norm or weakly convergent boundary subnet",
        "open_theorem": "continue the scalar amplitude to a pressure-critical domain or attach its trace-field packet mass to a rational-prime von Mangoldt law",
        "reusable_structure": "orbitwise Mahler spectral heights are the exact coefficients governing the all-orbit boundary amplitude",
        "round2_clue": "study the pressure Dirichlet series sum_gamma exp(-s*ellhat_gamma) H_gamma as a thermodynamic height observable before any prime pushforward",
        "claim_boundary": "the theorem is confined to the P51 safe half-plane and scalar packet mass; it proves no continuation, pressure-pole law, rational-prime trace, determinant, or operator",
    }
    payload["core_sha256"] = canonical_sha(payload)
    return payload


def write_certificate(path: Path, max_index: int = 72) -> dict[str, Any]:
    payload = build_certificate(max_index=max_index)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--max-index", type=int, default=72)
    args = parser.parse_args()
    payload = write_certificate(args.output, max_index=args.max_index)
    print(
        json.dumps(
            {
                "candidate_id": payload["candidate_id"],
                "core_sha256": payload["core_sha256"],
                "orbit_sentinels": len(payload["orbit_sentinels"]),
                "status": "PASS",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
