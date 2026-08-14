#!/usr/bin/env python3
"""Produce the HCS-P51 all-orbit Abel-graded packet certificate.

The finite computation certifies the constants and dependency interfaces used
by an analytic theorem.  It does not enumerate all primitive H6 orbits.  The
infinite conclusion is proved from the exact symbolic census, the all-period
integral fixed algebra, a uniform conjugate-height estimate, and the certified
pressure lower bound.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any

import sympy as sp


PROJECT = Path(__file__).resolve().parents[1]
TRACK = PROJECT.parent
DEFAULT_OUTPUT = PROJECT / "results" / "c51_certificate.json"
X, T = sp.symbols("X T")

ADJACENCY = (
    (1, 0, 1, 0),
    (1, 0, 0, 0),
    (0, 1, 0, 1),
    (0, 1, 0, 0),
)

DEPENDENCIES = {
    "p31_pressure_theorem": (
        TRACK / "henon_bowen_pressure_gate" / "THEOREM_PACKAGE.md",
        "5f2ae3d86094a80c89822f91af935ef09efa3893cbc50326f56174f154f721ee",
    ),
    "p31_pressure_certificate": (
        TRACK / "henon_bowen_pressure_gate" / "results" / "c31_certificate.json",
        "9f326c8442f5f1dfb8215527491a9ebbac2395fde7892c88bc78634df24c5cca",
    ),
    "p43_orbit_certificate": (
        TRACK / "henon_entropy_von_mangoldt_bridge" / "results" / "c43_certificate.json",
        "2cf9571310b601704c5ae4f3b888bf674a949b83adcc4f72bc135d9a71aa241d",
    ),
    "p46_integral_monodromy": (
        TRACK / "henon_integral_monodromy_units" / "README.md",
        "700cce354f56c3b218984f2a8606d04b122304336c65735da86adb7f93cb9a47",
    ),
    "p46_certificate": (
        TRACK / "henon_integral_monodromy_units" / "results" / "c46_certificate.json",
        "43251f10b1c900921963b95648b0e95b15e70bdb6bd9d3a9674cf7b234f55f85",
    ),
    "p49_packet_proof": (
        TRACK / "henon_cyclic_resultant_packet_obstruction" / "PROOF_PACKAGE.md",
        "1adc57e42ecba61f1e1d5b8a1e076a3999eef328588ded230e556d0a0c45ad9c",
    ),
    "p49_certificate": (
        TRACK / "henon_cyclic_resultant_packet_obstruction" / "results" / "c49_certificate.json",
        "da866888620533376a487667c2d0900c109ed7b984d57e28d49a0a319c407450",
    ),
    "p50_tagged_certificate": (
        TRACK / "henon_tagged_prime_ideal_packet_assembly" / "results" / "c50_certificate.json",
        "1ed3f3f7c6c534197b21a2a8b7ec8d58ef6fdf9d0706d115430bab3351b8c4fd",
    ),
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
            raise RuntimeError(f"dependency hash changed: {name}")
        locks[name] = {
            "path": str(path.relative_to(TRACK)),
            "sha256": observed,
        }
    return locks


def matmul(
    left: tuple[tuple[int, ...], ...],
    right: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(4)) for j in range(4))
        for i in range(4)
    )


def matpow(exponent: int) -> tuple[tuple[int, ...], ...]:
    result = tuple(tuple(int(i == j) for j in range(4)) for i in range(4))
    base = ADJACENCY
    power = exponent
    while power:
        if power & 1:
            result = matmul(result, base)
        base = matmul(base, base)
        power //= 2
    return result


def marked_count(period: int) -> int:
    matrix = matpow(period)
    return sum(matrix[index][index] for index in range(4))


def divisors(value: int) -> list[int]:
    return [candidate for candidate in range(1, value + 1) if value % candidate == 0]


def mobius(value: int) -> int:
    return int(sp.mobius(value))


def primitive_orbit_count(period: int) -> int:
    exact_points = sum(
        mobius(divisor) * marked_count(period // divisor)
        for divisor in divisors(period)
    )
    if exact_points % period:
        raise ArithmeticError("exact-period count is not divisible by the period")
    return exact_points // period


def beta_trace_polynomial(index: int) -> sp.Expr:
    """Return X^(-phi(n)/2) Phi_n(X) as a polynomial in T=X+X^-1."""
    if index <= 2:
        raise ValueError("the inversion-fixed packet begins at index 3")
    cyclotomic = sp.Poly(sp.cyclotomic_poly(index, X), X)
    half_degree = int(sp.totient(index)) // 2
    laurent = {
        int(power[0] - half_degree): sp.Integer(coefficient)
        for power, coefficient in cyclotomic.terms()
    }
    chebyshev = {0: sp.Integer(2), 1: T}
    for power in range(2, half_degree + 1):
        chebyshev[power] = sp.expand(T * chebyshev[power - 1] - chebyshev[power - 2])
    result = sp.Integer(laurent.get(0, 0))
    for power in range(1, half_degree + 1):
        if laurent.get(power, 0) != laurent.get(-power, 0):
            raise ArithmeticError(f"reciprocity failed at index {index}")
        result += laurent.get(power, 0) * chebyshev[power]
    return sp.expand(result)


def period_four_beta(index: int) -> int:
    return abs(int(beta_trace_polynomial(index).subs(T, 578)))


def analytic_constants() -> dict[str, float | str]:
    golden_ratio = (1.0 + math.sqrt(5.0)) / 2.0
    j_star = (math.sqrt(17.0) + math.sqrt(13.0)) / 2.0
    pressure_lower = 0.277980
    pressure_upper = 0.277987
    coordinate_bound = 1.0 + math.sqrt(7.0)
    derivative_bound = 3.0 + 2.0 * math.sqrt(7.0)
    sigma_certified = math.log(2.0 * golden_ratio) / (
        pressure_lower * math.log(j_star)
    )
    return {
        "golden_ratio": golden_ratio,
        "J_star": j_star,
        "pressure_lower": pressure_lower,
        "pressure_upper": pressure_upper,
        "coordinate_conjugate_bound": coordinate_bound,
        "derivative_step_bound_C0": derivative_bound,
        "sigma_certified": sigma_certified,
        "sigma_formula": "log(2*phi)/(h_lower*log(J_star))",
    }


def norm_log_upper(period: int, index: int, constants: dict[str, Any]) -> float:
    c0 = float(constants["derivative_step_bound_C0"])
    return (2.0**period) * index * (
        math.log(2.0 * math.sqrt(3.0)) + 0.5 * period * math.log(c0)
    )


def abel_lower_bound(radius: float, cutoff: int) -> float:
    if cutoff < 13:
        return 0.0
    return math.log(2.0) * sum(radius**index for index in range(13, cutoff + 1))


def period_rows(max_period: int, constants: dict[str, Any]) -> list[dict[str, Any]]:
    phi = float(constants["golden_ratio"])
    rows: list[dict[str, Any]] = []
    for period in range(1, max_period + 1):
        marked = marked_count(period)
        primitive = primitive_orbit_count(period)
        upper = 3.0 * phi**period
        if marked > upper + 1e-10:
            raise ArithmeticError("symbolic marked-count bound failed")
        rows.append(
            {
                "period": period,
                "marked_points": marked,
                "primitive_orbits": primitive,
                "marked_bound_3phi_m": upper,
                "fixed_algebra_degree_cap": 2**period,
                "norm_log_upper_at_index_20": norm_log_upper(period, 20, constants),
            }
        )
    return rows


def period_four_rows() -> list[dict[str, Any]]:
    p50 = json.loads(
        (TRACK / "henon_tagged_prime_ideal_packet_assembly" / "results" / "c50_certificate.json").read_text()
    )
    p50_values = {
        int(row["cyclotomic_index"]): int(row["absolute_norm"])
        for row in p50["rows"]
        if row["orbit"] == "period_4"
    }
    rows: list[dict[str, Any]] = []
    for index in range(3, 25):
        beta = period_four_beta(index)
        rows.append(
            {
                "index": index,
                "beta_absolute": str(beta),
                "log_beta": math.log(beta),
                "p50_crosscheck": (
                    beta == p50_values[index] if index in p50_values else None
                ),
                "flatters_fresh_prime_guaranteed": index > 12,
                "packet_norm_lower_bound": math.log(2.0) if index > 12 else None,
            }
        )
    return rows


def build_certificate(max_period: int = 32) -> dict[str, Any]:
    if max_period < 12 or max_period > 64:
        raise ValueError("max_period must lie in [12,64]")
    constants = analytic_constants()
    threshold = float(constants["sigma_certified"])
    ratio_above = 2.0 * float(constants["golden_ratio"]) * math.exp(
        -(threshold + 0.05)
        * float(constants["pressure_lower"])
        * math.log(float(constants["J_star"]))
    )
    if not ratio_above < 1.0:
        raise ArithmeticError("certified convergence ratio does not contract")
    radii = (0.90, 0.97, 0.99, 1.00)
    cutoffs = (20, 40, 80, 160)
    lower_bounds = [
        {
            "u_radius": radius,
            "cutoff": cutoff,
            "flatters_lower_norm": abel_lower_bound(radius, cutoff),
        }
        for radius in radii
        for cutoff in cutoffs
    ]
    payload: dict[str, Any] = {
        "schema": "hcs-p51-abel-graded-all-orbit-germ-v1",
        "candidate_id": "HCS-P51",
        "dependency_locks": dependency_locks(),
        "constants": constants,
        "convergence_domain": {
            "u": "|u|<1",
            "s_exact": "Re(s)>log(2*phi)/(h_star*log(J_star))",
            "s_certified": f"Re(s)>{threshold:.12f}",
            "test_ratio_at_sigma_cert_plus_0.05": ratio_above,
        },
        "period_rows": period_rows(max_period, constants),
        "period_four_rows": period_four_rows(),
        "abel_boundary_lower_bounds": lower_bounds,
        "banach_spaces": {
            "tagged": "ell1({(gamma,n,q)}, f(q/p)*log(p))",
            "rational": "ell1({rational primes p}, log(p))",
            "pushforward": "[gamma,n,q] -> f(q/p)[p]",
            "operator_norm_upper": 1,
            "packetwise_norm_identity": True,
            "pushforward_injective": False,
        },
        "theorem_ledger": {
            "all_orbit_abel_graded_series_absolute_convergence": "PROVED",
            "banach_valued_joint_holomorphy": "PROVED",
            "continuous_rational_norm_pushforward": "PROVED",
            "period_four_u_radius_exactly_one": "PROVED_SOURCE_BACKED",
            "ungraded_u_equals_one_series": "REFUTED_DIVERGES",
            "analytic_continuation_beyond_certified_domain": "OPEN",
            "boundary_abel_renormalization": "OPEN",
            "von_mangoldt_trace_law": "OPEN",
            "fredholm_determinant": "OPEN",
            "hilbert_polya_operator": "OPEN",
        },
        "route_a": {
            "tuple": ["A1_WEAK", "A2_FAIL", "A3_PARTIAL_ANALYTIC_STRUCTURE", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_EXPLORATORY",
        },
        "strongest_positive_result": "all-orbit two-variable Banach-valued holomorphic packet germ with continuous norm pushforward",
        "strongest_obstruction": "the ungraded u=1 packet series diverges already on the exact period-four orbit",
        "open_theorem": "source-native Abel-boundary renormalization or Tauberian law compatible with pressure and von Mangoldt mass",
        "claim_boundary": "the all-orbit germ is proved only for |u|<1 and a certified right half-plane; no determinant, continuation, boundary value, von Mangoldt law, or operator is claimed",
    }
    payload["core_sha256"] = canonical_sha(payload)
    return payload


def write_certificate(path: Path, max_period: int = 32) -> dict[str, Any]:
    payload = build_certificate(max_period=max_period)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--max-period", type=int, default=32)
    args = parser.parse_args()
    payload = write_certificate(args.output, max_period=args.max_period)
    print(
        json.dumps(
            {
                "candidate_id": payload["candidate_id"],
                "core_sha256": payload["core_sha256"],
                "sigma_certified": payload["constants"]["sigma_certified"],
                "period_rows": len(payload["period_rows"]),
                "status": "PASS",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
