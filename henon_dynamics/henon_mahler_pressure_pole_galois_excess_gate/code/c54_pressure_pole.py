#!/usr/bin/env python3
"""Build the HCS-P54 pressure-pole/Galois-excess certificate.

The infinite pressure-pole statement is proved in ``PROOF_PACKAGE.md`` from
the hash-locked H6 suspension theorem and Parry--Pollicott's zeta theorem.
This executable independently records the exact three-orbit Galois excess,
the residue interval forced by the certified pressure root, and finite Euler
log-derivative identities.  It does not numerically manufacture an infinite
pressure singularity.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

import mpmath as mp
import sympy as sp


PROJECT = Path(__file__).resolve().parents[1]
TRACK = PROJECT.parent
DEFAULT_OUTPUT = PROJECT / "results" / "c54_certificate.json"
T = sp.symbols("T")

H_LOWER = "0.277980"
H_UPPER = "0.277987"

DEPENDENCIES = {
    "p45_readme": (
        TRACK / "henon_pressure_normalized_prime_orbit_bridge" / "README.md",
        "45cb4c5b8c735bfb5c3a497cfecef21fc81140b3c77f56c866249df8715e5ba1",
    ),
    "p45_certificate": (
        TRACK / "henon_pressure_normalized_prime_orbit_bridge" / "results" / "c45_certificate.json",
        "962e0f6aca53b8e1c8786caa291af7bb318efd631b86b7f70702c1d2bea603f7",
    ),
    "p48_certificate": (
        TRACK / "henon_pressure_label_six_exponentials_obstruction" / "results" / "c48_certificate.json",
        "7134167226aa6bd22596675bf21826b8303a2a731f087d6ad7405d7137a51234",
    ),
    "p53_readme": (
        TRACK / "henon_pressure_weighted_all_orbit_abel_law" / "README.md",
        "b719c290b278b874d6180ab14479a5adb743f8c9b43fc75dac55c778516586b0",
    ),
    "p53_proof": (
        TRACK / "henon_pressure_weighted_all_orbit_abel_law" / "PROOF_PACKAGE.md",
        "0270d20fb8b4438bd31ba504c7a9fd10b9dc49aef39620091fe66894e770276b",
    ),
    "p53_certificate": (
        TRACK / "henon_pressure_weighted_all_orbit_abel_law" / "results" / "c53_certificate.json",
        "52b1b502cd0283e01ee6de9e58a2bddbe7d7dff5538ed652cca905226c96b459",
    ),
    "p31_theorem": (
        TRACK / "henon_bowen_pressure_gate" / "THEOREM_PACKAGE.md",
        "5f2ae3d86094a80c89822f91af935ef09efa3893cbc50326f56174f154f721ee",
    ),
    "instability_roof_readme": (
        TRACK / "henon_instability_roof_zeta" / "README.md",
        "c2a63ba68fe4d7092d5304008ab5745172269c23bbc30faf93f1423ae96f798e",
    ),
}


ORBIT_SPECS: dict[str, dict[str, Any]] = {
    "period_1": {
        "period": 1,
        "trace_polynomial": sp.Poly(T**2 - 4 * T - 24, T),
        "trace_roots": (2 + 2 * sp.sqrt(7), 2 - 2 * sp.sqrt(7)),
        "physical_trace_index": 0,
        "excess_formula": "acosh(sqrt(7)-1)",
    },
    "period_3": {
        "period": 3,
        "trace_polynomial": sp.Poly(T**2 + 76 * T - 7376, T),
        "trace_roots": (-38 - 42 * sp.sqrt(5), -38 + 42 * sp.sqrt(5)),
        "physical_trace_index": 0,
        "excess_formula": "acosh(21*sqrt(5)-19)",
    },
    "period_4": {
        "period": 4,
        "trace_polynomial": sp.Poly(T - 578, T),
        "trace_roots": (sp.Integer(578),),
        "physical_trace_index": 0,
        "excess_formula": "0",
    },
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_sha(payload: object) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def dependency_locks() -> dict[str, dict[str, str]]:
    locks: dict[str, dict[str, str]] = {}
    for label, (path, expected) in DEPENDENCIES.items():
        observed = sha256(path)
        if observed != expected:
            raise RuntimeError(
                f"dependency hash changed for {label}: expected {expected}, observed {observed}"
            )
        locks[label] = {"path": str(path.relative_to(TRACK)), "sha256": observed}
    return locks


def real_pair_log(trace: sp.Expr) -> mp.mpf:
    value = mp.mpf(str(sp.N(trace, 90)))
    if abs(value) <= 2:
        return mp.mpf("0")
    return mp.acosh(abs(value) / 2)


def exact_orbit_row(name: str, spec: dict[str, Any]) -> dict[str, Any]:
    roots = tuple(spec["trace_roots"])
    if sp.Poly(sp.prod(T - root for root in roots), T) != spec["trace_polynomial"]:
        raise ArithmeticError(f"trace polynomial factorization changed for {name}")
    pair_logs = [real_pair_log(root) for root in roots]
    physical_index = int(spec["physical_trace_index"])
    physical = pair_logs[physical_index]
    height = mp.fsum(pair_logs)
    excess = height - physical
    formula = sp.sympify(spec["excess_formula"])
    formula_value = mp.mpf(str(sp.N(formula, 90)))
    if abs(excess - formula_value) > mp.mpf("1e-70"):
        raise ArithmeticError(f"exact excess formula changed for {name}")
    if excess < -mp.mpf("1e-70"):
        raise ArithmeticError(f"negative Galois excess for {name}")
    return {
        "period": int(spec["period"]),
        "trace_polynomial": str(spec["trace_polynomial"].as_expr()),
        "trace_roots": [str(root) for root in roots],
        "physical_trace": str(roots[physical_index]),
        "reciprocal_pair_logs": [mp.nstr(value, 60) for value in pair_logs],
        "physical_instability_length": mp.nstr(physical, 60),
        "mahler_spectral_height": mp.nstr(height, 60),
        "galois_excess": mp.nstr(excess, 60),
        "galois_excess_formula": spec["excess_formula"],
        "height_over_physical_length": mp.nstr(height / physical, 60),
        "excess_positive": bool(excess > mp.mpf("1e-50")),
        "excess_zero": bool(abs(excess) < mp.mpf("1e-50")),
    }


def pressure_residue_interval() -> dict[str, str]:
    h_lower = mp.mpf(H_LOWER)
    h_upper = mp.mpf(H_UPPER)
    lower = 3 / (mp.pi**2 * h_upper)
    upper = 3 / (mp.pi**2 * h_lower)
    midpoint = 3 / (mp.pi**2 * ((h_lower + h_upper) / 2))
    if not lower < midpoint < upper:
        raise ArithmeticError("pressure residue interval orientation changed")
    return {
        "formula": "3/(pi^2*h_star)",
        "h_star_open_interval": "(0.277980,0.277987)",
        "residue_open_interval": f"({mp.nstr(lower, 50)},{mp.nstr(upper, 50)})",
        "midpoint_value": mp.nstr(midpoint, 50),
    }


def finite_log_derivative_fixture(rows: dict[str, dict[str, Any]]) -> dict[str, Any]:
    h_mid = (mp.mpf(H_LOWER) + mp.mpf(H_UPPER)) / 2
    s = mp.mpf("1.25")
    fixtures = []
    for name, row in rows.items():
        ell = mp.mpf(row["physical_instability_length"])
        normalized = h_mid * ell
        primitive = normalized * mp.e ** (-s * normalized)
        full_repetition = normalized / (mp.e ** (s * normalized) - 1)
        tail = mp.fsum(
            normalized * mp.e ** (-s * k * normalized) for k in range(2, 400)
        )
        if abs(full_repetition - primitive - tail) > mp.mpf("1e-60"):
            raise ArithmeticError(f"Euler log-derivative identity failed for {name}")
        fixtures.append(
            {
                "orbit": name,
                "normalized_length": mp.nstr(normalized, 50),
                "s": "1.25",
                "primitive_term": mp.nstr(primitive, 50),
                "all_repetitions_term": mp.nstr(full_repetition, 50),
                "repetition_tail": mp.nstr(tail, 50),
                "identity_abs_error": mp.nstr(abs(full_repetition - primitive - tail), 8),
            }
        )
    return {
        "identity": "-zeta'/zeta = primitive logarithmic derivative + k>=2 tail",
        "fixtures": fixtures,
    }


def build_certificate() -> dict[str, Any]:
    mp.mp.dps = 90
    rows = {name: exact_orbit_row(name, spec) for name, spec in ORBIT_SPECS.items()}
    if not rows["period_1"]["excess_positive"]:
        raise ArithmeticError("period-one positive excess witness disappeared")
    if not rows["period_3"]["excess_positive"]:
        raise ArithmeticError("period-three positive excess witness disappeared")
    if not rows["period_4"]["excess_zero"]:
        raise ArithmeticError("period-four zero excess witness disappeared")

    # If H_gamma-c*ell_gamma were a periodic coboundary, period four forces
    # c=1, while period one leaves the strictly positive Galois excess.
    forced_c = mp.mpf(rows["period_4"]["mahler_spectral_height"]) / mp.mpf(
        rows["period_4"]["physical_instability_length"]
    )
    period_one_residual = mp.mpf(rows["period_1"]["mahler_spectral_height"]) - forced_c * mp.mpf(
        rows["period_1"]["physical_instability_length"]
    )
    if abs(forced_c - 1) > mp.mpf("1e-70") or period_one_residual <= 0:
        raise ArithmeticError("scalar-roof cohomology obstruction changed")

    core = {
        "candidate_id": "HCS-P54",
        "claim_status": "PROVED_PLUS_CONDITIONAL_THEOREM",
        "arithmetic_advance": "PARTIAL_ANALYTIC_STRUCTURE_ONLY",
        "route_b_authorized": False,
        "source_object": "certified mixing H6 four-state survivor with normalized instability roof",
        "mahler_decomposition": {
            "identity": "H_gamma=ell_gamma+E_gamma",
            "physical_length": "ell_gamma=log|Lambda_gamma|",
            "galois_excess": "sum over nonphysical reciprocal conjugate pairs outside the unit circle",
            "galois_excess_nonnegative": True,
        },
        "physical_pressure_pole": {
            "primitive_amplitude": "(3/pi^2) sum_gamma ell_gamma exp(-s*h_star*ell_gamma)",
            "meromorphic_germ_at_s_1": True,
            "simple_pole": True,
            "residue": "3/(pi^2*h_star)",
            "proof_engine": "Parry-Pollicott Theorem 6.3 and Corollary 6.3.1 plus analytic repetition tail",
            "residue_certificate": pressure_residue_interval(),
        },
        "conditional_holder_completion": {
            "hypothesis": "E_gamma=S_m psi for one Holder psi on the frozen SFT",
            "conclusion": "full Mahler amplitude has a meromorphic simple-pole germ at s=1",
            "residue": "(3/pi^2)*integral(tau+psi)dmu/integral(h_star*tau)dmu",
            "proof_engine": "Parry-Pollicott Theorem 6.4 and Corollary 6.4.1",
            "status": "CONDITIONAL_THEOREM",
        },
        "excess_abscissa_trichotomy": {
            "sigma_E_definition": "abscissa of absolute convergence of sum E_gamma exp(-s*h_star*ell_gamma)",
            "certified_upper_bound": "sigma_E<=log(2*golden_ratio)/(h_star*log(J_star))<3.125207",
            "sigma_E_lt_1": "physical simple pole is the full amplitude pole with residue 3/(pi^2*h_star)",
            "sigma_E_eq_1": "critical excess must be analyzed by a weighted thermodynamic theorem",
            "sigma_E_gt_1": "the defining positive excess series blocks access to the physical pressure line",
        },
        "exact_orbits": rows,
        "scalar_roof_cohomology_obstruction": {
            "hypothesis_refuted": "H_gamma-c*ell_gamma is a periodic coboundary for one constant c",
            "period_four_forces_c": mp.nstr(forced_c, 30),
            "period_one_residual": mp.nstr(period_one_residual, 50),
            "conclusion": "no constant rescaling of the instability roof, even modulo coboundary, realizes Mahler height",
        },
        "finite_log_derivative_fixture": finite_log_derivative_fixture(rows),
        "source_theorem_map": {
            "Parry_Pollicott_6_3": "normalized weak-mixing suspension zeta has a simple pole at s=1",
            "Parry_Pollicott_cor_6_3_1": "-zeta'/zeta has principal part 1/(s-1)",
            "Parry_Pollicott_6_4_cor_6_4_1": "two-parameter weighted zeta derivative has equilibrium-average residue",
            "Parry_Pollicott_6_9": "primitive orbit count is asymptotic to exp(T)/T",
        },
        "strongest_positive_result": "the physical part of the P53 Mahler amplitude has an exact pressure-pole germ and universal certified residue",
        "strongest_obstruction": "the full Mahler height is not a scalar instability roof modulo coboundary; its Galois excess has no proved Holder realization",
        "open_theorem": "realize E_gamma as a Holder/asymptotically additive periodic observable or determine its pressure abscissa sigma_E",
        "claim_boundary": "no continuation of the actual Galois-excess series, rational-prime trace, completed determinant, or Hilbert-Polya operator is proved",
    }
    return {
        **core,
        "core_sha256": canonical_sha(core),
        "dependency_locks": dependency_locks(),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    certificate = build_certificate()
    if args.check:
        print(
            json.dumps(
                {
                    "candidate_id": certificate["candidate_id"],
                    "check": True,
                    "core_sha256": certificate["core_sha256"],
                    "dependency_lock_count": len(certificate["dependency_locks"]),
                    "exact_orbit_count": len(certificate["exact_orbits"]),
                    "status": "PASS",
                },
                sort_keys=True,
            )
        )
        return 0
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "candidate_id": certificate["candidate_id"],
                "core_sha256": certificate["core_sha256"],
                "exact_orbits": len(certificate["exact_orbits"]),
                "status": "PASS",
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
