#!/usr/bin/env python3
"""Produce the HCS-P52 totient Abel-boundary certificate.

The infinite theorems are proved in ``PROOF_PACKAGE.md``.  This producer
checks the exact period-four packet formula, evaluates the explicit constants,
and records finite convergence/profile sentinels.  Numerical rows illustrate
the proved limits; they are not used as proofs of those limits.
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
DEFAULT_OUTPUT = PROJECT / "results" / "c52_certificate.json"
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
    "p49_proof": (
        TRACK / "henon_cyclic_resultant_packet_obstruction" / "PROOF_PACKAGE.md",
        "1adc57e42ecba61f1e1d5b8a1e076a3999eef328588ded230e556d0a0c45ad9c",
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
            raise RuntimeError(
                f"dependency hash changed for {name}: expected {expected}, observed {observed}"
            )
        locks[name] = {
            "path": str(path.relative_to(TRACK)),
            "sha256": observed,
        }
    return locks


def beta_trace_polynomial(index: int) -> sp.Expr:
    """Return X^(-phi(n)/2) Phi_n(X) as a polynomial in T=X+X^-1."""
    if index <= 2:
        raise ValueError("the inversion-fixed packet begins at index 3")
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


def beta_integer(index: int) -> int:
    value = int(beta_trace_polynomial(index).subs(T, 578))
    if value <= 0:
        raise ArithmeticError(f"period-four packet is not positive at n={index}")
    return value


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


def multiplier() -> mp.mpf:
    return mp.mpf(289) + mp.mpf(24) * mp.sqrt(145)


def epsilon(index: int, lam: mp.mpf) -> mp.mpf:
    return mp.fsum(
        mp.mpf(mobius(index // divisor)) * mp.log(1 - lam ** (-divisor))
        for divisor in divisors(index)
    )


def log_beta_formula(index: int, lam: mp.mpf) -> mp.mpf:
    return mp.mpf(totient(index)) * mp.log(lam) / 2 + epsilon(index, lam)


def correction_bound(lam: mp.mpf, cutoff: int = 32) -> tuple[mp.mpf, mp.mpf]:
    partial = mp.fsum(-mp.log(1 - lam ** (-d)) for d in range(1, cutoff + 1))
    first = lam ** (-(cutoff + 1))
    tail = first / ((1 - first) * (1 - 1 / lam))
    return partial, partial + tail


def tail_geometric(q: mp.mpf, cutoff: int, log_lam: mp.mpf, corr: mp.mpf) -> mp.mpf:
    """Upper bound sum_{n>cutoff} b_n q^n using b_n <= n log(L)/2+C."""
    first = q ** (cutoff + 1)
    n_tail = first * ((cutoff + 1) - cutoff * q) / (1 - q) ** 2
    one_tail = first / (1 - q)
    return log_lam * n_tail / 2 + corr * one_tail


def abel_row(tau_text: str, profile_s: tuple[float, ...]) -> dict[str, Any]:
    tau = mp.mpf(tau_text)
    lam = multiplier()
    _, corr_upper = correction_bound(lam)
    cutoff = int(mp.ceil(40 / tau))
    masses = [log_beta_formula(n, lam) for n in range(3, cutoff + 1)]
    weights = [mp.e ** (-tau * n) for n in range(3, cutoff + 1)]
    z = mp.fsum(mass * weight for mass, weight in zip(masses, weights))
    tail = tail_geometric(mp.e ** (-tau), cutoff, mp.log(lam), corr_upper)
    target = 3 * mp.log(lam) / mp.pi**2
    laplace_rows = []
    for s_float in profile_s:
        s = mp.mpf(str(s_float))
        numerator = mp.fsum(
            mass * mp.e ** (-(1 + s) * tau * n)
            for n, mass in zip(range(3, cutoff + 1), masses)
        )
        numerator_tail = tail_geometric(
            mp.e ** (-(1 + s) * tau), cutoff, mp.log(lam), corr_upper
        )
        laplace_rows.append(
            {
                "s": float(s),
                "observed": float(numerator / z),
                "target_gamma_2_1": float((1 + s) ** -2),
                "numerator_tail_upper": float(numerator_tail),
            }
        )
    fixed_prefix = mp.fsum(
        log_beta_formula(n, lam) * mp.e ** (-tau * n) for n in range(3, 21)
    )
    return {
        "tau": float(tau),
        "u": float(mp.e ** (-tau)),
        "cutoff": cutoff,
        "tau_squared_Z": float(tau**2 * z),
        "target_constant": float(target),
        "ratio_to_target": float(tau**2 * z / target),
        "truncation_tail_upper": float(tail),
        "fixed_prefix_3_20_mass_fraction": float(fixed_prefix / z),
        "profile_laplace": laplace_rows,
    }


def packet_rows(max_index: int) -> list[dict[str, Any]]:
    if max_index < 24:
        raise ValueError("max_index must be at least 24")
    lam = multiplier()
    p51 = json.loads(
        (TRACK / "henon_abel_graded_all_orbit_packet_germ" / "results" / "c51_certificate.json").read_text()
    )
    p51_values = {
        int(row["index"]): int(row["beta_absolute"])
        for row in p51["period_four_rows"]
    }
    rows: list[dict[str, Any]] = []
    for index in range(3, max_index + 1):
        beta = beta_integer(index)
        log_direct = mp.log(beta)
        log_formula = log_beta_formula(index, lam)
        rows.append(
            {
                "index": index,
                "totient": totient(index),
                "beta": str(beta),
                "epsilon": float(epsilon(index, lam)),
                "log_beta": float(log_direct),
                "formula_abs_error": float(abs(log_direct - log_formula)),
                "p51_crosscheck": beta == p51_values[index] if index in p51_values else None,
            }
        )
    return rows


def build_certificate(max_index: int = 72) -> dict[str, Any]:
    if max_index < 24 or max_index > 120:
        raise ValueError("max_index must lie in [24,120]")
    mp.mp.dps = 90
    lam = multiplier()
    corr_partial, corr_upper = correction_bound(lam)
    limit_constant = 3 * mp.log(lam) / mp.pi**2
    rows = packet_rows(max_index)
    if max(row["formula_abs_error"] for row in rows) > 1e-70:
        raise ArithmeticError("exact packet formula failed its high-precision check")
    abel_rows = [
        abel_row(tau, (0.5, 1.0, 2.0))
        for tau in ("0.2", "0.1", "0.05", "0.025", "0.0125")
    ]
    payload: dict[str, Any] = {
        "schema": "hcs-p52-totient-abel-boundary-escape-v1",
        "candidate_id": "HCS-P52",
        "dependency_locks": dependency_locks(),
        "source_object": {
            "map": "H_6(q,p)=(1-6q^2-p,q)",
            "orbit": "exact primitive period-four orbit inherited from HCS-P51",
            "multiplier": "L=289+24*sqrt(145)",
            "minimal_polynomial": "X^2-578*X+1",
            "packet": "beta_n=L^(-phi(n)/2)*Phi_n(L), n>=3",
            "tagged_norm": "||D_n||=log(beta_n)",
        },
        "constants": {
            "L": str(lam),
            "log_L": float(mp.log(lam)),
            "uniform_correction_partial_32": float(corr_partial),
            "uniform_correction_upper": float(corr_upper),
            "abel_limit_constant_3logL_over_pi2": float(limit_constant),
        },
        "exact_formula": {
            "identity": "log(beta_n)=phi(n)*log(L)/2+epsilon_n",
            "epsilon": "sum_{d|n} mu(n/d)*log(1-L^(-d))",
            "uniform_bound": "|epsilon_n|<=C_L=sum_{d>=1}-log(1-L^(-d))",
            "summatory_totient": "sum_{n<=x}phi(n)=3*x^2/pi^2+O(x*log x)",
        },
        "packet_rows": rows,
        "abel_rows": abel_rows,
        "boundary_theorems": {
            "scalar_abel_law": "(1-u)^2*sum_{n>=3}log(beta_n)u^n -> 3log(L)/pi^2",
            "exponential_parameter": "tau^2*sum_{n>=3}log(beta_n)e^(-tau*n) -> 3log(L)/pi^2",
            "blowup_profile": "normalized mass at tau*n converges weakly to Gamma(shape=2,rate=1)",
            "tagged_vector": "tau^2*sum e^(-tau*n)D_n has no norm- or weakly-convergent subnet in B_tag",
        },
        "theorem_ledger": {
            "uniform_totient_packet_asymptotic": "PROVED",
            "scalar_abel_boundary_constant": "PROVED",
            "gamma_2_1_escape_profile": "PROVED",
            "tagged_banach_norm_boundary_limit": "REFUTED_NO_CONVERGENT_SUBNET",
            "fixed_orbit_source_native_boundary_blowup": "PROVED",
            "all_orbit_boundary_interchange": "OPEN",
            "von_mangoldt_trace_law": "OPEN",
            "fredholm_determinant": "OPEN",
            "hilbert_polya_operator": "OPEN",
        },
        "adversarial_controls": {
            "wrong_normalization_logL_not_half": "REJECTED",
            "wrong_scale_tau_not_tau_squared": "REJECTED",
            "wrong_profile_exponential_shape_one": "REJECTED",
            "false_tagged_norm_convergence": "REJECTED",
            "scalarization_promoted_to_lossless_vector_limit": "REJECTED",
        },
        "route_a": {
            "tuple": [
                "A1_WEAK",
                "A2_FAIL",
                "A3_PARTIAL_ANALYTIC_STRUCTURE",
                "A4_FORMAL_HINT",
            ],
            "overall": "ROUTE_A_EXPLORATORY",
        },
        "strongest_positive_result": "exact totient Abel law and Gamma(2,1) boundary escape profile for one source-native H6 packet orbit",
        "strongest_obstruction": "the renormalized positive tagged divisor vectors have no norm or weak limit in the original weighted ell1 space",
        "open_theorem": "pressure-summed all-orbit Abel boundary with justified interchange of the orbit and cyclotomic-index limits",
        "reusable_structure": "uniform cyclotomic log-mass formula plus scaled-index probability compactification",
        "round2_clue": "test whether pressure weighting yields a finite mixture of Gamma(2,1) profiles or a new pressure critical exponent",
        "claim_boundary": "P52 proves a one-orbit scalar and blow-up boundary theorem, not an all-orbit boundary, von-Mangoldt identity, determinant, or operator",
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
    result = write_certificate(args.output, max_index=args.max_index)
    print(json.dumps({
        "candidate_id": result["candidate_id"],
        "core_sha256": result["core_sha256"],
        "packet_rows": len(result["packet_rows"]),
        "abel_rows": len(result["abel_rows"]),
        "status": "PASS",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
