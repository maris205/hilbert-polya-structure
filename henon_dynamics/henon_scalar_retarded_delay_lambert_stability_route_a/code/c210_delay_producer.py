#!/usr/bin/env python3
"""Deterministic source certificate for the scalar retarded delay equation.

The file deliberately records only exact, source-local algebra.  It never
imports a target spectrum or attaches an arithmetic interpretation to a
characteristic root.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from math import factorial, floor
from pathlib import Path

SOURCE_COMMIT = "e8054522273dbd545f9d406978e5d4648c627918"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c210_delay_evidence.json"

# Rational sentinels cover stable, Hopf-side, unstable and all singular edges.
CASE_SPECS = [
    ("a2_b1_tau1", F(2), F(1), F(1)),
    ("a1_b2_tau1_4", F(1), F(2), F(1, 4)),
    ("a1_b2_tau1", F(1), F(2), F(1)),
    ("a1_b2_tau2", F(1), F(2), F(2)),
    ("a1_b1_tau3", F(1), F(1), F(3)),
    ("a0_b2_tau1_4", F(0), F(2), F(1, 4)),
    ("a2_b0_tau1", F(2), F(0), F(1)),
    ("a0_b0_tau2", F(0), F(0), F(2)),
    ("a0_b1_tau1_4", F(0), F(1), F(1, 4)),
    ("a3_b1_tau0", F(3), F(1), F(0)),
    ("a1_b3_tau0", F(1), F(3), F(0)),
    ("a0_b0_tau0", F(0), F(0), F(0)),
]
TIMES = [F(i, 4) for i in range(13)]


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def q(x: F) -> str:
    return str(x)


def method_step_polynomial(a: F, b: F, tau: F, t: F) -> str:
    """Exact symbolic delayed-exponential term, avoiding fake rational exp values."""
    if tau == 0:
        return f"1(t=0); exp(-{q(a + b)}*t)(t>0)"
    terms = []
    nmax = floor(t / tau) if t >= 0 else -1
    for n in range(nmax + 1):
        coeff = (-b) ** n * (t - n * tau) ** n / F(factorial(n))
        terms.append(f"{q(coeff)}*exp(-{q(a)}*({q(t)}-{q(n*tau)}))")
    return "+".join(terms) if terms else "0"


def regime(a: F, b: F, tau: F) -> str:
    if a == 0 and b == 0:
        return "zero_equation"
    if tau == 0:
        return "zero_delay_ode"
    if b == 0:
        return "no_delayed_feedback"
    if a >= b:
        return "exponentially_stable_all_delays"
    return "stable_before_hopf_or_unstable_after"


def build_case(case_id: str, a: F, b: F, tau: F) -> dict:
    return {
        "case_id": case_id,
        "a": q(a), "b": q(b), "tau": q(tau),
        "regime": regime(a, b, tau),
        "characteristic_equation": "lambda+a+b*exp(-lambda*tau)",
        "fundamental_solution_terms_t_quarters": [method_step_polynomial(a, b, tau, t) for t in TIMES],
        "reported_times": [q(t) for t in TIMES],
        "zero_root_condition": q(a + b),
        "lambert_argument_prefactor": q(b * tau),
        "branch_point_condition": "b*tau*exp(a*tau)=exp(-1)",
    }


def build() -> dict:
    cases = [build_case(*spec) for spec in CASE_SPECS]
    data = {
        "schema": "hcs-c210-scalar-retarded-delay-v1",
        "candidate_id": "HCS-C210",
        "evaluation_date": "2026-08-28",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "evaluator": {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256},
        "headline": "The scalar retarded delay semigroup has a complete Lambert-W characteristic atlas and exact stability/Hopf boundaries",
        "frozen_object": {
            "phase_space": "X=C([-tau,0],C) for tau>0; X=C({0},C) when tau=0",
            "equation": "x'(t)=-a*x(t)-b*x(t-tau), a>=0,b>=0,tau>=0",
            "generator": "A phi=phi'; D(A)={phi in C^1: phi'(0)=-a phi(0)-b phi(-tau)}",
            "parameters": "real a,b,tau>=0 and continuous initial history phi",
            "clock": "physical elapsed time t; no fitted or logarithmic clock",
            "normalization": "history norm ||phi||_infty and fundamental solution r(0)=1, r(t<0)=0",
            "determinant_convention": "source characteristic determinant Delta(lambda)=lambda+a+b*exp(-lambda*tau); not a target or Fredholm determinant",
            "arithmetic_origin": "none; this is a scope-locked non-arithmetic control",
            "allowed_data": "exact rational parameter sentinels and source-local symbolic identities",
            "forbidden_data": "prime/zero tables, arithmetic labels, fitted parameters, target divisors and external observations",
        },
        "theorem": {
            "characteristic_equation": "Delta(lambda)=lambda+a+b*exp(-lambda*tau)",
            "lambert_w_spectrum": "for tau>0,b>0 every characteristic root is -a+tau^{-1} W_k(-b*tau*exp(a*tau)), with W_0 and W_-1 merged at -1/e",
            "fundamental_solution": "r(t)=sum_{n=0}^{floor(t/tau)}(-b)^n exp(-a*(t-n*tau))*(t-n*tau)^n/n! for t>=0 and tau>0",
            "semigroup": "the history solution operators T(t) form a strongly continuous retarded semigroup and satisfy T(t+s)=T(t)T(s)",
            "eventual_compactness": "T(t) is compact on C([-tau,0]) for every t>tau by the C^1 smoothing and Arzela-Ascoli",
            "spectral_mapping": "for t>tau, sigma(T(t))\\{0}=exp(t*sigma(A)); the algebraic multiplicity at a nonzero mu is the sum of characteristic-root multiplicities over all lambda with exp(t*lambda)=mu (collisions are aggregated)",
            "root_multiplicity": "Delta'=1-b*tau*exp(-lambda*tau); a multiple root is exactly lambda=-a-1/tau and b*tau*exp(a*tau)=exp(-1), and it is at most double",
            "stability_atlas": "if a>=b, all tau are exponentially stable except the zero equation; if b>a, stability holds exactly for 0<=tau<tau_c",
            "hopf_boundary": "for b>a, omega=sqrt(b^2-a^2), tau_c=acos(-a/b)/omega; at tau_c the only imaginary pair is +/-i omega and crossings are to the right",
            "boundary_ledger": "tau=0 gives x'=-(a+b)x; b=0 removes the delay; a=b=0 is the constant equation; a=b>0 stays stable for each finite tau but its gap tends to zero as tau grows",
            "periodic_orbit_status": "linear histories at a Hopf point form a two-dimensional center family, not isolated primitive cycles",
        },
        "regression": {
            "time_grid": [q(t) for t in TIMES],
            "cases": cases,
            "case_count": len(cases),
            "hopf_formula_controls": [
                {"case_id": "a0_b1", "a": "0", "b": "1", "omega": "1", "tau_c": "pi/2"},
                {"case_id": "a1_b2", "a": "1", "b": "2", "omega": "sqrt(3)", "tau_c": "acos(-1/2)/sqrt(3)"},
                {"case_id": "a2_b3", "a": "2", "b": "3", "omega": "sqrt(5)", "tau_c": "acos(-2/3)/sqrt(5)"},
            ],
        },
        "summary": {
            "case_count": len(cases),
            "time_sample_count": len(TIMES),
            "fundamental_symbolic_cell_count": len(cases) * len(TIMES),
            "hopf_control_count": 3,
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "strongest_positive": "Lambert-W branches, exact method-of-steps resolvent, eventual compactness, and a complete nonnegative-parameter Hopf/stability atlas are source-local theorem progress.",
            "strongest_failure": "There is no intrinsic rational-prime carrier, isolated primitive-orbit ledger, target divisor or natural same-clock self-adjoint lift.",
        },
        "scope_flags": {k: False for k in [
            "uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors",
            "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation",
            "claims_hilbert_polya_operator", "invokes_route_b"]},
        "citations": [{
            "key": "HaleVerduynLunel1993", "claim": "retarded semigroup and characteristic-root framework",
            "title": "Introduction to Functional Differential Equations", "authors": "Jack K. Hale; Sjoerd M. Verduyn Lunel",
            "report_number": "Springer Applied Mathematical Sciences 99", "date": "1993",
            "url": "https://link.springer.com/book/10.1007/978-1-4612-4342-7", "persistent_url": "https://doi.org/10.1007/978-1-4612-4342-7"
        }],
        "nonclaims": [
            "priority for delay equations or Lambert-W root theory",
            "a finite rational regression proves the all-parameter semigroup theorem",
            "Delta is a Fredholm determinant or a dynamical zeta",
            "any characteristic root is a Riemann zero or arithmetic local datum",
            "a Hilbert-Polya operator, target divisor, Euler factor, root number, automorphy, external review or Route-B authorization",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(build(), sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "C210_PRODUCER_PASS", "output": str(args.output), "payload_sha256": json.loads(args.output.read_text())["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
