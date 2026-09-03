#!/usr/bin/env python3
"""Deterministic finite receipts for HCS-C328."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c328_run_tumble_evidence.json"
SOURCE = "1aba1f6fd0cf81baa7c137a2ce7ce3d097ba63fc"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600
EVAL_RAW = "d95689db325195f9c14bb38f739c66003d53eb3e53a08bf98de78ad7b045787f"
EVAL_SEMANTIC = "64a9be4c652799d46ed59bbfb91e8835e0ff20726d3b00f38d33019a1d6963b8"
FILTER_DEGREE = 8
mp.mp.dps = 100

PARAMETERS = (
    (Fraction(1), Fraction(1), Fraction(1, 2)),
    (Fraction(1), Fraction(2), Fraction(1)),
    (Fraction(2), Fraction(3), Fraction(3)),
    (Fraction(2), Fraction(5), Fraction(4)),
    (Fraction(3), Fraction(4), Fraction(15, 2)),
    (Fraction(4), Fraction(7), Fraction(12)),
    (Fraction(1), Fraction(3), Fraction(1, 3)),
    (Fraction(2), Fraction(1), Fraction(1, 2)),
    (Fraction(3), Fraction(5), Fraction(2)),
    (Fraction(5), Fraction(2), Fraction(7, 2)),
    (Fraction(6), Fraction(11), Fraction(5, 2)),
    (Fraction(7), Fraction(13), Fraction(9, 2)),
)
TIMES = (Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(1), Fraction(2))
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


def dec(value: mp.mpf) -> str:
    return mp.nstr(value, 72, strip_zeros=False, min_fixed=-90, max_fixed=90)


def mpq(value: Fraction) -> mp.mpf:
    return mp.mpf(value.numerator) / value.denominator


def rising(value: Fraction, n: int) -> Fraction:
    out = Fraction(1)
    for j in range(n):
        out *= value + j
    return out


def leaves(value) -> int:
    if type(value) is dict:
        return sum(leaves(v) for v in value.values())
    if type(value) is list:
        return sum(leaves(v) for v in value)
    return 1


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def parameter_row(index: int, mu: Fraction, speed: Fraction, lam: Fraction) -> dict:
    alpha = lam / mu
    scale = speed / mu
    alpha_mp = mpq(alpha)
    scale_mp = mpq(scale)
    normal_y = mp.gamma(alpha_mp + mp.mpf("0.5")) / (mp.sqrt(mp.pi) * mp.gamma(alpha_mp))
    moments = []
    for n in range(FILTER_DEGREE + 1):
        unit_even = rising(Fraction(1, 2), n) / rising(alpha + Fraction(1, 2), n)
        position_even = scale ** (2 * n) * unit_even
        unit_next = rising(Fraction(1, 2), n + 1) / rising(alpha + Fraction(1, 2), n + 1)
        sigma_odd = scale ** (2 * n + 1) * unit_next
        moments.append({
            "n": n,
            "even_position_moment": rat(position_even),
            "odd_position_moment": "0",
            "sigma_even_position_moment": "0",
            "sigma_odd_position_moment": rat(sigma_odd),
        })

    mu_mp, speed_mp, lam_mp = mpq(mu), mpq(speed), mpq(lam)
    covariance = {
        "xx": speed_mp**2 / (mu_mp * (mu_mp + 2 * lam_mp)),
        "x_sigma": speed_mp / (mu_mp + 2 * lam_mp),
        "sigma_x": speed_mp / (mu_mp + 2 * lam_mp),
        "sigma_sigma": mp.mpf(1),
    }
    correlations = []
    jordan = mu == 2 * lam
    for time in TIMES:
        tt = mpq(time)
        e_mu = mp.exp(-mu_mp * tt)
        e_lam = mp.exp(-2 * lam_mp * tt)
        off = speed_mp * tt * e_mu if jordan else speed_mp * (e_lam - e_mu) / (mu_mp - 2 * lam_mp)
        correlations.append({
            "time": rat(time),
            "xx": dec(e_mu * covariance["xx"] + off * covariance["x_sigma"]),
            "x_sigma": dec(e_mu * covariance["x_sigma"] + off),
            "sigma_x": dec(e_lam * covariance["sigma_x"]),
            "sigma_sigma": dec(e_lam),
        })

    spectral_cells = []
    for n in range(FILTER_DEGREE + 1):
        spectral_cells.append({"sector": "A", "degree": n, "diagonal_eigenvalue": rat(-n * mu)})
        spectral_cells.append({"sector": "B", "degree": n, "diagonal_eigenvalue": rat(-n * mu - 2 * lam)})
    ratio = 2 * lam / mu
    resonances = []
    if ratio.denominator == 1:
        k = ratio.numerator
        for n in range(k, FILTER_DEGREE + 1):
            resonances.append({
                "a_degree": n,
                "b_degree": n - k,
                "eigenvalue": rat(-n * mu),
                "algebraic_multiplicity": 2,
                "geometric_multiplicity": 1 if k % 2 else 2,
                "jordan_class": "one_size_2_block" if k % 2 else "two_size_1_blocks",
            })
        resonance_class = "odd_integer_jordan" if k % 2 else "even_integer_semisimple"
    else:
        k = None
        resonance_class = "noninteger_nonresonant"

    return {
        "parameter_id": f"rt-{index:02d}",
        "mu": rat(mu),
        "speed_v": rat(speed),
        "lambda": rat(lam),
        "alpha_lambda_over_mu": rat(alpha),
        "support_half_width": rat(scale),
        "beta_normalization_y": dec(normal_y),
        "beta_normalization_x": dec(normal_y / scale_mp),
        "endpoint_exponent_marginal": rat(alpha - 1),
        "endpoint_exponent_suppressed_component": rat(alpha),
        "component_masses": ["1/2", "1/2"],
        "moments": moments,
        "stationary_covariance": {name: dec(value) for name, value in covariance.items()},
        "correlations": correlations,
        "filter_degree": FILTER_DEGREE,
        "spectral_cells": spectral_cells,
        "resonance_integer": k,
        "resonance_class": resonance_class,
        "resonances": resonances,
    }


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C328 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    rows = [parameter_row(i + 1, *params) for i, params in enumerate(PARAMETERS)]
    data = {
        "schema": "hcs-c328-harmonic-run-tumble-v1",
        "candidate_id": "HCS-C328",
        "obstruction_id": "HEN-O312",
        "evaluation_date": "2026-09-03",
        "fixed_epoch": EPOCH,
        "source_commit": SOURCE,
        "scope_literal": SCOPE,
        "evaluator": {
            "authority": "flow_systems/skills/route-a-evaluator.md",
            "version": "0.2.0",
            "sha256": EVALUATOR,
        },
        "evaluation_lock": {
            "relative_path": "evaluations/route_a/HCS-C328/2026-09-03.yaml",
            "raw_sha256": EVAL_RAW,
            "semantic_sha256": EVAL_SEMANTIC,
        },
        "model": {
            "state": "(x,sigma) in [-v/mu,v/mu] times {-1,+1}",
            "deterministic_motion": "dx/dt=v*sigma-mu*x",
            "jump_rule": "sigma flips sign at rate lambda",
            "generator": "L f_sigma=(v*sigma-mu*x)*partial_x f_sigma+lambda*(f_-sigma-f_sigma)",
            "parameters": "mu,v,lambda strictly positive",
        },
        "theorem_contract": {
            "stationary_marginal": "scaled y=mu*x/v has density Gamma(alpha+1/2)/(sqrt(pi)Gamma(alpha))*(1-y^2)^(alpha-1)",
            "stationary_components": "p_+=(1+y)p/2 and p_-=(1-y)p/2",
            "moments": "all odd x moments and all E[sigma*x^(2n)] vanish; E[x^(2n)]=(v/mu)^(2n)*(1/2)_n/(alpha+1/2)_n",
            "correlation": "for t>=0 the complete stationary (x,sigma) correlation matrix is R(t)=exp(A t)Sigma, with a Jordan limit at mu=2lambda; R(-t)=R(t)^T",
            "polynomial_filter": "P_N=span{x^n,sigma*x^n:0<=n<=N} is invariant with two triangular eigenvalue ladders",
            "resonance": "for v>0 and 2lambda/mu=k integer, repeated eigenvalues are size-two Jordan blocks iff k is odd and are semisimple iff k is even",
            "spectrum_boundary": "the claim concerns every finite polynomial filter and not the full L2 spectrum",
        },
        "parameter_rows": rows,
        "boundary_atlas": [
            {"face": "mu=0", "status": "unconfined integrated telegraph motion; no compact stationary probability on the line"},
            {"face": "lambda=0", "status": "orientation sectors do not communicate and arbitrary mixtures of the two attracting endpoint atoms are stationary"},
            {"face": "v=0 with lambda>0", "status": "the joint stationary law is delta_0 tensor the uniform orientation law and all repeated polynomial eigenvalues are semisimple because couplings vanish"},
            {"face": "v=lambda=0", "status": "position contracts to zero while orientation is frozen, so every orientation mixture over delta_0 is stationary"},
            {"face": "mu=2lambda", "status": "first odd resonance with t exp(-mu t) in stationary correlations"},
            {"face": "alpha<1, alpha=1, alpha>1", "status": "marginal density respectively diverges, is uniform, or vanishes at the support endpoints"},
            {"face": "support endpoints", "status": "open-interval densities may be integrably singular but carry no atoms for positive rates"},
            {"face": "full L2 generator", "status": "not classified; only invariant finite polynomial filters are claimed"},
        ],
        "collision_boundary": {
            "C213": "the circular telegraph process is unconfined in position and closes Fourier blocks rather than a harmonic beta law",
            "C237": "harmonic Kramers--Langevin has Gaussian Mehler dynamics rather than compact beta support",
            "C265": "exponential Hawkes dynamics is a self-exciting affine jump process rather than a symmetric two-velocity PDMP",
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": FLAGS,
        "nonclaims": [
            "No priority is claimed for harmonic run-and-tumble stationary laws or telegraph-noise calculations.",
            "No full L2 spectrum, completeness theorem, or spectral expansion of arbitrary observables is claimed.",
            "Finite parameter and degree-eight receipts do not prove the all-parameter finite-filter theorem.",
            "The Markov generator is not self-adjoint here and is not a Hilbert--Polya operator.",
            "No target arithmetic local data, Euler factors, root numbers, automorphy, target divisor, functional equation, or target-zero match is asserted.",
        ],
        "references": [
            {"doi": "10.1103/PhysRevE.99.032132", "role": "one-dimensional confined run-and-tumble stationary and relaxation source"},
            {"doi": "10.1088/1742-5468/ac014d", "role": "harmonic run-and-tumble field-theory and stationary component source"},
        ],
    }
    data["enumeration"] = {
        "parameter_rows": len(rows),
        "moment_rows": sum(len(row["moments"]) for row in rows),
        "correlation_rows": sum(len(row["correlations"]) for row in rows),
        "spectral_cells": sum(len(row["spectral_cells"]) for row in rows),
        "resonance_rows": sum(len(row["resonances"]) for row in rows),
    }
    data["enumeration"]["audited_leaf_count"] = leaves(data) + 1
    data["payload_sha256"] = payload_hash(data)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(f"C328_PRODUCER_PASS {data['payload_sha256']} {data['enumeration']['audited_leaf_count']}")


if __name__ == "__main__":
    main()
