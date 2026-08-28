#!/usr/bin/env python3
"""Deterministic Fourier-block certificate for the circular telegraph process."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import mpmath as mp

SOURCE_COMMIT = "e8054522273dbd545f9d406978e5d4648c627918"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c213_telegraph_evidence.json"
C_VALUES = [F(0), F(1, 2), F(1), F(2), F(3)]
LAMBDA_VALUES = [F(0), F(1, 2), F(1), F(2), F(3)]
K_VALUES = list(range(-3, 4))
TIMES = [F(0), F(1, 3), F(1), F(2)]
WORKING_DECIMAL_DIGITS = 100
SERIALIZED_SIGNIFICANT_DIGITS = 82


def payload_hash(data: dict) -> str:
    body = dict(data); body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def mpq(x: F) -> mp.mpf:
    return mp.mpf(x.numerator) / x.denominator


def fmt(x: mp.mpf) -> str:
    return mp.nstr(x, SERIALIZED_SIGNIFICANT_DIGITS, strip_zeros=False)


def complex_pair(z: mp.mpc) -> list[str]:
    return [fmt(mp.re(z)), fmt(mp.im(z))]


def mode_label(c: F, lam: F) -> str:
    if c == 0 and lam == 0: return "static_all_modes"
    if c == 0: return "velocity_mixing_no_spatial_decay"
    if lam == 0: return "ballistic_unitary"
    if lam <= c: return "oscillatory_or_critical_gap_lambda"
    return "hypocoercive_diffusive_gap"


def gap_expression(c: F, lam: F) -> str:
    if c == 0 or lam == 0: return "0"
    if lam <= c: return str(lam)
    return f"{lam}-sqrt({lam*lam-c*c})"


def block(c: F, lam: F, k: int, t: F) -> dict:
    mp.mp.dps = WORKING_DECIMAL_DIGITS
    ck = c * k
    d2 = lam * lam - ck * ck
    d = mp.sqrt(mpq(d2))
    tt = mpq(t)
    if abs(d) == 0:
        h = mp.mpf(1); q = tt
    else:
        h = mp.cosh(d * tt); q = mp.sinh(d * tt) / d
    e = mp.exp(-mpq(lam) * tt)
    ik = mp.j * mpq(ck)
    nmat = [[ik, mpq(lam)], [mpq(lam), -ik]]
    emat = [[e * (h + q * nmat[0][0]), e * q * nmat[0][1]],
            [e * q * nmat[1][0], e * (h + q * nmat[1][1])]]
    roots = [-mpq(lam) + d, -mpq(lam) - d]
    return {
        "case_id": f"c{c}_lambda{lam}_k{k}_t{t}",
        "c": str(c), "lambda": str(lam), "k": k, "t": str(t),
        "delta_square": str(d2), "generator_trace": str(-2 * lam),
        "generator_determinant": str(c * c * k * k), "mode": mode_label(c, lam),
        "eigenvalues": [complex_pair(r) for r in roots],
        "exponential_matrix": [[complex_pair(emat[i][j]) for j in range(2)] for i in range(2)],
    }


def gap_row(c: F, lam: F) -> dict:
    # At c=0 positions are frozen, so every spatial profile shared by the
    # two velocities is stationary.  At lambda=0 and c>0 each velocity-wise
    # spatial constant is stationary (dimension two).  Positive c and lambda
    # leave only the invariant constant density.
    if c == 0:
        stationary = "infinite"
    elif lam == 0:
        stationary = "2"
    else:
        stationary = "1"
    essential = "1" if c == 0 else "exp(-lambda*t)"
    return {"case_id": f"c{c}_lambda{lam}", "c": str(c), "lambda": str(lam),
            "gap_expression": gap_expression(c, lam), "stationary_dimension": stationary,
            "essential_norm_expression": essential, "mode": mode_label(c, lam)}


def build() -> dict:
    rows = [block(c, lam, k, t) for c in C_VALUES for lam in LAMBDA_VALUES for k in K_VALUES for t in TIMES]
    gaps = [gap_row(c, lam) for c in C_VALUES for lam in LAMBDA_VALUES]
    data = {
        "schema": "hcs-c213-circle-telegraph-v1", "candidate_id": "HCS-C213", "evaluation_date": "2026-08-28",
        "source_commit": SOURCE_COMMIT, "scope_literal": SCOPE,
        "evaluator": {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256},
        "headline": "The circular telegraph process has exact Fourier blocks, a sharp spectral-gap atlas and a noncompactness boundary",
        "frozen_object": {
            "phase_space": "L2(T_{2pi} x {+1,-1}, dx/(2pi) times uniform velocity law)",
            "process": "dx/dt=c*v modulo 2pi; velocity flips sign at Poisson rate lambda",
            "generator": "L f(x,v)=c*v*partial_x f(x,v)+lambda*(f(x,-v)-f(x,v))",
            "parameters": "c>=0, lambda>=0, physical t>=0",
            "clock": "physical elapsed time; no fitted or logarithmic clock",
            "normalization": "uniform invariant measure on the circle and two velocities",
            "determinant_convention": "finite 2x2 Fourier characteristic polynomial only; no Fredholm or target determinant",
            "arithmetic_origin": "none; this is a scope-locked non-arithmetic control",
            "allowed_data": "exact rational c,lambda,k,t sentinels and source-local Fourier algebra",
            "forbidden_data": "prime/zero tables, target labels, fitted phases and external observations",
        },
        "theorem": {
            "fourier_block": "G_k=[[-lambda+i*c*k,lambda],[lambda,-lambda-i*c*k]]",
            "nilpotent_square": "(G_k+lambda I)^2=(lambda^2-c^2*k^2)I",
            "matrix_exponential": "exp(tG_k)=exp(-lambda*t)[cosh(delta_k*t)I+sinh(delta_k*t)(G_k+lambda I)/delta_k], delta_k^2=lambda^2-c^2*k^2; delta=0 uses I+tN",
            "eigenvalues": "rho_{k,+/-}=-lambda +/- sqrt(lambda^2-c^2*k^2)",
            "telegraph_equation": "rho_tt+2*lambda*rho_t=c^2*rho_xx for rho=f_++f_-",
            "spectral_gap": "sharp spectral-abscissa gap (not a constant-free L2 operator-norm decay): for c>0,lambda>0 gap=lambda when lambda<=c and gap=lambda-sqrt(lambda^2-c^2) when lambda>c; gap=0 when c=0 or lambda=0",
            "critical_blocks": "lambda=c*|k|>0 gives a single Jordan block at -lambda; k=0 has eigenvalues 0 and -2lambda",
            "stationary_boundary": "c>0,lambda>0 has only constants; c=0,lambda>0 has an infinite spatial stationary subspace; lambda=0 has two velocity constants",
            "essential_boundary": "for c>0,lambda>0 the essential norm of P_t on the complement of constants is the |k|->infinity block limit exp(-lambda*t), still nonzero; for c=0 or lambda=0 it is 1",
            "ballistic_boundary": "lambda=0 is the same-clock unitary pair of translations; c=0 is velocity-only mixing with no spatial decay",
        },
        "regression": {"c_values": [str(x) for x in C_VALUES], "lambda_values": [str(x) for x in LAMBDA_VALUES], "k_values": K_VALUES, "time_values": [str(x) for x in TIMES], "block_rows": rows, "gap_rows": gaps},
        "summary": {"block_row_count": len(rows), "gap_row_count": len(gaps), "matrix_entry_count": len(rows) * 4, "parameter_pair_count": len(gaps)},
        "route_a": {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False, "strongest_positive": "The source Markov semigroup has an exact all-mode Fourier matrix exponential, sharp gap regimes, Jordan boundaries and an essential-spectrum obstruction.", "strongest_failure": "There is no intrinsic rational-prime carrier, isolated primitive-orbit owner, target divisor or nontrivial same-clock self-adjoint lift."},
        "scope_flags": {k: False for k in ["uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"]},
        "citations": [{"key": "Kac1974", "claim": "telegraph-process origin and velocity-switching framework", "title": "A stochastic model related to the telegrapher's equation", "authors": "Mark Kac", "report_number": "Rocky Mountain Journal of Mathematics 4(3), 497--509", "date": "1974", "url": "https://doi.org/10.1216/RMJ-1974-4-3-497", "persistent_url": "https://doi.org/10.1216/RMJ-1974-4-3-497"}],
        "nonclaims": ["priority for the telegraph process or its Fourier solution", "a finite block ledger proves the infinite semigroup theorem", "Fourier characteristic polynomials are Fredholm determinants or dynamical zeta functions", "any spectral value is an arithmetic or target zero", "a Hilbert-Polya operator, target divisor, Euler factor, root number, automorphy, external review or Route-B authorization"],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    ap = argparse.ArgumentParser(); ap.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    out = ap.parse_args().output; out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(build(), sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    obj = json.loads(out.read_text()); print(json.dumps({"status": "C213_PRODUCER_PASS", "output": str(out), "payload_sha256": obj["payload_sha256"], "rows": obj["summary"]["block_row_count"]}, sort_keys=True))


if __name__ == "__main__": main()
