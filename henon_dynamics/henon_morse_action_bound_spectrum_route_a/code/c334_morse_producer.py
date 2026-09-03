#!/usr/bin/env python3
"""Deterministic exact receipts for HCS-C334."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c334_morse_evidence.json"
SOURCE = "db2c816b7b6bd450f51f79b91842cb882b0bd773"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EVAL_RAW = "d6bdbb263f89e478bad3b0fb760ae59c400c51df399cf02b28dcea573d04d8c5"
EVAL_SEMANTIC = "243b294744a8fd0ef9ac65480e7fc93dd257b23e238a8d93ded6e1cc07be1e3e"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600
PYTHAGOREAN = ((0, 1), (3, 5), (4, 5), (5, 13), (12, 13),
               (7, 25), (24, 25), (20, 29), (21, 29), (9, 41), (40, 41))
LAMBDAS = tuple(Fraction(k, 4) for k in range(1, 33))
FLAGS = {
    "claims_target_arithmetic_local_data": False,
    "claims_target_euler_factors": False,
    "claims_root_number": False,
    "claims_automorphy": False,
    "claims_target_divisor_or_counting_law": False,
    "claims_target_functional_equation": False,
    "claims_target_zero_match": False,
    "claims_hilbert_polya_operator": False,
    "invokes_route_b": False,
}


def rat(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def generalized_binomial(top: Fraction, k: int) -> Fraction:
    out = Fraction(1)
    for j in range(k):
        out *= (top-j) / (j+1)
    return out


def laguerre_coefficients(n: int, alpha: Fraction) -> list[str]:
    coeffs = []
    factorial = 1
    for k in range(n+1):
        if k:
            factorial *= k
        value = (-1 if k % 2 else 1) * generalized_binomial(Fraction(n)+alpha, n-k) / factorial
        coeffs.append(rat(value))
    return coeffs


def leaves(value) -> int:
    if type(value) is dict:
        return sum(leaves(item) for item in value.values())
    if type(value) is list:
        return sum(leaves(item) for item in value)
    return 1


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C334 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()

    classical = []
    for index, (delta_num, hyp) in enumerate(PYTHAGOREAN, 1):
        delta = Fraction(delta_num, hyp)
        sigma_num = int((hyp*hyp-delta_num*delta_num)**0.5)
        sigma = Fraction(sigma_num, hyp)
        energy = -sigma*sigma
        classical.append({
            "row_id": f"classical-{index:02d}",
            "delta": rat(delta), "sigma": rat(sigma), "energy_over_D": rat(energy),
            "left_y_turn": rat(1+delta), "right_y_turn": rat(1-delta),
            "action_over_sqrt_2mD_over_a": rat(1-sigma),
            "period_times_a_sqrt_D_over_2m_over_pi": rat(1/sigma),
        })

    levels = []
    counts = []
    thresholds = []
    for lam in LAMBDAS:
        allowed = [n for n in range(16) if Fraction(n) < lam-Fraction(1, 2)]
        counts.append({"lambda": rat(lam), "bound_state_count": len(allowed)})
        for n in allowed:
            exponent = lam-Fraction(n)-Fraction(1, 2)
            alpha = 2*exponent
            levels.append({
                "lambda": rat(lam), "n": n, "decay_exponent": rat(exponent),
                "energy_over_scale": rat(-exponent*exponent),
                "laguerre_alpha": rat(alpha),
                "laguerre_coefficients_low_to_high": laguerre_coefficients(n, alpha),
                "node_count": n,
            })
        if (lam-Fraction(1, 2)).denominator == 1 and lam >= Fraction(1, 2):
            thresholds.append({
                "lambda": rat(lam), "formal_n": int(lam-Fraction(1, 2)),
                "decay_exponent": "0", "energy_over_scale": "0",
                "l2_status": "excluded_nonintegrable_constant_tail",
            })

    model = {
        "classical": "H=p^2/(2m)+D(exp(-2ax)-2exp(-ax)), with m,D,a>0",
        "quantum": "the Friedrichs Schrödinger realization on L2(R), with hbar>0",
        "dimensionless_coupling": "lambda=sqrt(2mD)/(a hbar)",
        "action_normalization": "J(E)=(1/(2pi)) integral over the closed energy orbit of p dx",
    }
    theorem = {
        "classical_action": "for -D<E<0, J=sqrt(2mD)/a times (1-sqrt(-E/D))",
        "classical_period": "for -D<E<0, T=2pi/(a sqrt(-2E/m)) and dJ/dE=T/(2pi)",
        "bound_spectrum": "E_n=-(a^2 hbar^2/(2m))(lambda-n-1/2)^2 exactly for integers n>=0 with n<lambda-1/2",
        "eigenfunctions": "z^(lambda-n-1/2) exp(-z/2) L_n^(2lambda-2n-1)(z), z=2lambda exp(-ax), up to normalization",
        "spectral_boundary": "the essential spectrum is [0,infinity), there are no nonnegative L2 eigenfunctions, and equality at n=lambda-1/2 is a non-L2 zero-energy threshold state",
        "completeness": "the displayed negative levels are all and only the L2 point spectrum",
    }
    boundary = [
        {"face": "E=-D", "status": "the unique classical equilibrium and J=0"},
        {"face": "-D<E<0", "status": "periodic well motion with the stated action and period"},
        {"face": "E=0", "status": "dissociation separatrix with infinite period and finite limiting action"},
        {"face": "E>0", "status": "classical scattering and quantum essential spectrum"},
        {"face": "E<-D", "status": "empty classical energy shell"},
        {"face": "lambda<=1/2", "status": "no quantum bound states"},
        {"face": "n=lambda-1/2", "status": "formal zero-energy solution has a constant tail and is not L2"},
        {"face": "positive parameters", "status": "m,D,a,hbar must be strictly positive in the frozen owner"},
    ]
    data = {
        "schema": "hcs-c334-morse-action-spectrum-v1", "candidate_id": "HCS-C334",
        "obstruction_id": "HEN-O318", "evaluation_date": "2026-09-03",
        "fixed_epoch": EPOCH, "source_commit": SOURCE, "scope_literal": SCOPE,
        "evaluator": {"authority": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR},
        "evaluation_lock": {"relative_path": "evaluations/route_a/HCS-C334/2026-09-03.yaml", "raw_sha256": EVAL_RAW, "semantic_sha256": EVAL_SEMANTIC},
        "model": model, "theorem_contract": theorem,
        "classical_rows": classical, "bound_count_rows": counts,
        "bound_level_rows": levels, "threshold_rows": thresholds,
        "boundary_atlas": boundary,
        "collision_boundary": {
            "C216": "Kepler actions have a Coulomb singularity and different threshold geometry",
            "C232": "Duffing has quartic elliptic periods rather than the Morse elementary action",
            "C250": "the isotonic oscillator is confining and has no dissociation threshold",
            "C295": "the isochrone potential has a different radial action and degeneracy",
        },
        "route_a": {"tuple": ["A0_FAIL", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"], "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False},
        "scope_flags": FLAGS,
        "nonclaims": [
            "No priority is claimed for the Morse solution, action, or spectrum.",
            "The consecutive bound-level index is not a rational-prime carrier.",
            "No full target determinant, functional equation, zero match, or Hilbert--Polya operator is asserted.",
            "Finite rows are exact regression receipts and do not replace the analytic proof.",
        ],
        "references": [
            {"url": "https://journals.aps.org/pr/abstract/10.1103/PhysRev.34.57", "doi": "10.1103/PhysRev.34.57", "role": "Morse's primary exact diatomic bound-level source"},
            {"url": "https://dlmf.nist.gov/18.5", "doi": "none", "role": "official generalized-Laguerre normalization reference"},
            {"url": "https://dlmf.nist.gov/13.14", "doi": "none", "role": "official Whittaker-function normalization and endpoint reference"},
        ],
    }
    data["enumeration"] = {
        "classical_rows": len(classical), "bound_count_rows": len(counts),
        "bound_level_rows": len(levels), "threshold_rows": len(thresholds),
        "laguerre_coefficients": sum(len(row["laguerre_coefficients_low_to_high"]) for row in levels),
    }
    data["enumeration"]["audited_leaf_count"] = leaves(data)+1
    data["payload_sha256"] = payload_hash(data)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False)+"\n")
    print(f"C334_PRODUCER_PASS {data['payload_sha256']} {data['enumeration']['audited_leaf_count']}")


if __name__ == "__main__":
    main()
