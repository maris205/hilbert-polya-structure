#!/usr/bin/env python3
"""Produce the deterministic HCS-C282 exponential-claim ruin certificate."""
from __future__ import annotations

import hashlib
import itertools
import json
import os
from fractions import Fraction as Q
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(os.environ.get("C282_EVIDENCE_OUT", ROOT / "results/c282_ruin_evidence.json"))
SOURCE = "51fb3d46f96b854314811c1ad62d3103cd5d54e5"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788220800
mp.mp.dps = 90

CASES = {
    "profitable_light": (Q(1), Q(2), Q(2)),
    "profitable_near": (Q(3), Q(2), Q(2)),
    "profitable_unit": (Q(1), Q(2), Q(1)),
    "critical": (Q(2), Q(1), Q(2)),
    "adverse": (Q(3), Q(1), Q(2)),
    "adverse_strong": (Q(4), Q(1), Q(1)),
    "no_claims": (Q(0), Q(2), Q(1)),
}
US = (Q(0), Q(1, 3), Q(1), Q(3))
QS = (Q(0), Q(1, 5), Q(1), Q(3))
SS = (Q(0), Q(1, 2), Q(2), Q(5))


def qstr(x: Q) -> str:
    return f"{x.numerator}/{x.denominator}"


def mq(x: Q) -> mp.mpf:
    return mp.mpf(x.numerator) / x.denominator


def ds(x) -> str:
    x = mq(x) if isinstance(x, Q) else mp.mpf(x)
    if abs(x) < mp.mpf("1e-82"): x = mp.mpf(0)
    return mp.nstr(x, 76, strip_zeros=False)


def payload_hash(data: dict) -> str:
    clean = dict(data); clean.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(clean, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def regime(nu: Q, c: Q, beta: Q) -> str:
    if nu == 0: return "no_claims"
    if nu < c*beta: return "profitable"
    if nu == c*beta: return "critical"
    return "adverse"


def root(nu: mp.mpf, c: mp.mpf, beta: mp.mpf, q: mp.mpf) -> mp.mpf:
    return (c*beta-nu-q+mp.sqrt((c*beta-nu-q)**2+4*c*beta*q))/(2*c)


def regime_rows() -> list[dict]:
    rows = []
    for nu0, c0, beta0 in itertools.product(range(4), range(1, 4), range(1, 4)):
        nu, c, beta = Q(nu0), Q(c0), Q(beta0)
        reg = regime(nu, c, beta)
        rho = nu/(c*beta)
        R = max(Q(0), beta-nu/c) if nu else beta
        rows.append({
            "nu": qstr(nu), "c": qstr(c), "beta": qstr(beta), "rho": qstr(rho),
            "regime": reg, "q0_root": qstr(R),
            "ultimate_ruin_at_zero": qstr(Q(0) if nu == 0 else rho if reg == "profitable" else Q(1)),
            "mean_drift": qstr(c-nu/beta),
        })
    return rows


def transform_rows() -> list[dict]:
    rows = []
    for name, (nuq, cq, betaq) in CASES.items():
        nu, c, beta = map(mq, (nuq, cq, betaq))
        for uq, qq, sq in itertools.product(US, QS, SS):
            u, q, s = map(mq, (uq, qq, sq))
            rq = root(nu, c, beta, q)
            phi = (beta-rq)/(beta+s)*mp.exp(-rq*u)
            polynomial = c*rq*rq-(c*beta-nu-q)*rq-q*beta
            rows.append({
                "case": name, "nu": qstr(nuq), "c": qstr(cq), "beta": qstr(betaq),
                "u": qstr(uq), "q": qstr(qq), "s": qstr(sq), "root": ds(rq),
                "joint_transform": ds(phi), "quadratic_residual": ds(polynomial),
                "overshoot_factor": ds(beta/(beta+s)),
                "ruin_time_factor": ds((beta-rq)/beta*mp.exp(-rq*u)),
            })
    return rows


def first_mean_rows() -> list[dict]:
    rows = []
    for nu0, c0, beta0 in itertools.product(range(4), range(1, 4), range(1, 4)):
        nuq, cq, betaq = Q(nu0), Q(c0), Q(beta0)
        reg = regime(nuq, cq, betaq)
        for uq in US:
            if reg == "no_claims":
                prob, mean, deficit = Q(0), None, None
            elif reg == "profitable":
                R = betaq-nuq/cq
                prob = mq(nuq/(cq*betaq))*mp.exp(-mq(R*uq))
                mean = mq((1+nuq*uq/cq)/(cq*betaq-nuq))
                deficit = mq(1/betaq)
            elif reg == "adverse":
                prob = mp.mpf(1)
                mean = mq((betaq*uq+1)/(nuq-cq*betaq))
                deficit = mq(1/betaq)
            else:
                prob, mean, deficit = mp.mpf(1), "infinite", mq(1/betaq)
            rows.append({
                "nu": qstr(nuq), "c": qstr(cq), "beta": qstr(betaq), "u": qstr(uq),
                "regime": reg, "ruin_probability": ds(prob),
                "conditional_mean_ruin_time": mean if mean in (None, "infinite") else ds(mean),
                "conditional_mean_deficit": None if deficit is None else ds(deficit),
            })
    return rows


def martingale_rows() -> list[dict]:
    rows = []
    for name, (nuq, cq, betaq) in CASES.items():
        if not (Q(0) < nuq < cq*betaq): continue
        R = betaq-nuq/cq
        exponent = nuq*(betaq/(betaq-R)-1)-cq*R
        rho = nuq/(cq*betaq)
        for uq in US:
            rows.append({
                "case": name, "nu": qstr(nuq), "c": qstr(cq), "beta": qstr(betaq),
                "adjustment_root": qstr(R), "martingale_exponent": qstr(exponent),
                "initial_reserve": qstr(uq), "supremum_atom_at_zero": qstr(1-rho),
                "supremum_tail": ds(mq(rho)*mp.exp(-mq(R*uq))),
            })
    return rows


def boundary_rows() -> list[dict]:
    return [
        {"face": "profitable", "condition": "c*beta>nu>0", "status": "defective ruin; positive adjustment root"},
        {"face": "critical", "condition": "c*beta=nu>0", "status": "ruin certain; mean ruin time infinite; root has square-root q cusp"},
        {"face": "adverse", "condition": "c*beta<nu", "status": "ruin certain; finite mean ruin time"},
        {"face": "no_claims", "condition": "nu=0", "status": "ruin impossible for c>0"},
        {"face": "zero_reserve", "condition": "u=0", "status": "included; strict ruin occurs only after a claim"},
        {"face": "zero_premium", "condition": "c=0", "status": "outside frozen owner; the displayed root divides by c"},
    ]


def main() -> None:
    regression = {"regime_rows": regime_rows(), "transform_rows": transform_rows(),
                  "first_mean_rows": first_mean_rows(), "martingale_rows": martingale_rows(),
                  "boundary_rows": boundary_rows()}
    regression["counts"] = {k: len(v) for k, v in regression.items()}
    data = {
        "schema": "hcs-c282-cramer-lundberg-exponential-ruin-v1", "candidate_id": "HCS-C282",
        "evaluation_date": "2026-09-01", "source_commit": SOURCE, "fixed_epoch": EPOCH,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "The exponential-claim Cramer-Lundberg process has one exact joint discount-deficit transform that closes defective, critical, adverse, no-claim, conditional-first-mean, overshoot, adjustment-martingale, and supremum chambers.",
        "evaluator": {"version": "0.2.0", "sha256": EVAL},
        "model_contract": {
            "surplus": "U_t=u+c*t-sum_{i=1}^{N_t}Y_i", "parameters": "u>=0,c>0,nu>=0,beta>0",
            "claims": "N is Poisson with rate nu; Y_i are iid Exp(beta), independent of N",
            "ruin": "tau=inf{t>=0:U_t<0}; deficit D=-U_tau on tau<infinity", "clock": "physical time",
            "killed_owner": "X_t=U_t for t<tau and X_t=Delta for t>=tau; Phi is a first-passage functional of the underlying surplus U",
        },
        "transform_contract": {
            "object": "Phi_{q,s}(u)=E_u[exp(-q*tau-s*D);tau<infinity]",
            "root": "r_q=(c*beta-nu-q+sqrt((c*beta-nu-q)^2+4*c*beta*q))/(2*c)",
            "formula": "Phi_{q,s}(u)=(beta-r_q)/(beta+s)*exp(-r_q*u)",
            "domain": "q,s,u>=0,c,beta>0,nu>=0; c=0 is explicitly outside",
            "root_selection": "q>0: boundedness selects the positive root; q=0 and 0<nu<c*beta: Phi(u)->0 selects beta-nu/c; q=0 and nu>=c*beta: boundedness selects 0; nu=0: Phi is identically zero",
            "uniqueness": "the convolution state J closes a two-dimensional inhomogeneous linear system; its characteristic polynomial is the root quadratic, J(0)=0 fixes the surviving coefficient, and chamber boundary conditions remove every other mode",
            "u_zero_extension": "common-path coupling and continuous claims extend the u>0 equation to strict ruin at u=0",
            "memoryless_factorization": "for nu>0, conditional on ruin, D is Exp(beta) and independent of tau; for nu=0 the conditional law is undefined",
        },
        "regime_contract": {
            "profitable": "rho=nu/(c*beta)<1: psi(u)=rho*exp(-(beta-nu/c)u)",
            "critical_or_adverse": "rho>=1: psi(u)=1",
            "conditional_first_mean_profitable": "(1+nu*u/c)/(c*beta-nu)",
            "conditional_first_mean_adverse": "(beta*u+1)/(nu-c*beta)",
            "critical_mean": "infinite", "mean_deficit": "1/beta in every nontrivial ruin chamber",
            "supremum": "in the profitable chamber, claim-minus-premium supremum has atom 1-rho at zero and tail rho*exp(-R*u)",
        },
        "proof_contract": {
            "status": "PROVABLE AS STATED",
            "dependencies": ["compound-Poisson first-jump equation", "two-dimensional convolution-state linear system", "memorylessness of exponential claims", "quadratic root analysis", "strong-law boundary at infinite reserve"],
            "scope": "classical compound-Poisson surplus with exponential claims and c>0 only; no investment, diffusion, dependence, heavy tails, finite-horizon inversion, control, or empirical solvency claim",
            "novelty_boundary": "complete frozen-convention synthesis; no invention or literature-priority claim",
        },
        "analytic_proof_obligations": [
            "derive the inhomogeneous Gerber-Shiu equation and close it with the convolution state J", "prove that the two homogeneous modes exhaust the solution space and that J(0)=0 plus chamber boundaries select one coefficient",
            "prove the selected root, probability boundary, and u=0 extension on every loading chamber", "prove memoryless overshoot independence", "differentiate the transform for both finite conditional first means and the critical divergence",
            "derive the adjustment martingale and supremum mixture", "separate no-claim and forbidden zero-premium boundaries",
        ],
        "regression": regression,
        "route_a": {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
                    "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False},
        "scope_flags": {"arithmetic_local_data": False, "euler_factors": False, "root_numbers": False,
                        "automorphy": False, "target_divisor_or_counting_law": False,
                        "target_functional_equation": False, "target_zero_match": False,
                        "hilbert_polya_operator": False, "route_b_authorization": False},
        "nonclaims": [
            "The killed PDMP/Markov semigroup has no intrinsic deterministic, enumerable primitive-periodic-orbit owner.",
            "No rational-prime carrier, logarithmic prime clock, target determinant, or target zero match is asserted.",
            "The workload/supremum identity is source-local and is not a new queueing owner or a target spectral bridge.",
            "Finite regression rows do not prove the continuous-parameter theorem.",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps({"status": "C282_PRODUCER_PASS", "counts": regression["counts"],
                      "payload_sha256": data["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__": main()
