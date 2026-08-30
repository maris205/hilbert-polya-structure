#!/usr/bin/env python3
"""Exact certificate for the linear-rate AIMD jump process.

The process has Xdot=a and jump rate rho*X, with X -> beta*X at a jump.
For beta>0 the jump skeleton is a stationary Markov chain, not an iid
regeneration sequence.  We therefore call the continuous-time occupation
identity a stationary Markov-renewal/Palm reward formula.  The beta=0 face is
the genuine reset/regeneration case.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
import math
import os
from pathlib import Path

SOURCE_COMMIT = "5f357e2d2b78604f6c286bfbd05da922e1d6791f"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FIXED_EPOCH = 1788048000
EVALUATION_DATE = "2026-08-30"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c246_tcp_aimd_evidence.json"
BETAS = (F(1, 2), F(2, 3), F(3, 4))
A_VALUES = (F(1, 2), F(1), F(3, 2))
RHO_VALUES = (F(1, 2), F(1), F(2))
MOMENT_MAX = 8
PRODUCT_TERMS = 12
SPOT_S = (F(1, 2), F(1), F(2))
SKELETON_STEPS = 6


def ftext(q: F | int) -> str:
    q = q if isinstance(q, F) else F(q)
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def z_moments(beta: F, a: F, rho: F, max_order: int = MOMENT_MAX) -> list[F]:
    """Moments of Z=Y^2 for Z'=beta^2 Z + (2a/rho) E, E~Exp(1)."""
    c = F(2) * a / rho
    out = [F(1)]
    for m in range(1, max_order + 1):
        rhs = F(0)
        for j in range(m):
            rhs += F(math.comb(m, j)) * beta ** (2 * j) * c ** (m - j) * out[j] * F(math.factorial(m - j))
        out.append(rhs / (F(1) - beta ** (2 * m)))
    return out


def generator_coefficients(beta: F, a: F, rho: F, max_order: int = MOMENT_MAX) -> list[dict]:
    """Represent M_m as const + mu*mu_coeff, M_0=1, M_1=mu."""
    coeff: list[tuple[F, F]] = [(F(1), F(0)), (F(0), F(1))]
    for m in range(1, max_order):
        prev = coeff[m - 1]
        fac = F(a * m, 1) / (rho * (F(1) - beta ** m))
        # M_{m+1}=fac*M_{m-1} from L x^m=0.
        base = coeff[m - 1]
        coeff.append((fac * base[0], fac * base[1]))
    return [{"order": m, "constant": ftext(c), "mu_coefficient": ftext(k)} for m, (c, k) in enumerate(coeff)]


def product_prefix(beta: F, a: F, rho: F, terms: int = PRODUCT_TERMS) -> list[F]:
    """Coefficients of prod_{j<terms}(1+c beta^(2j) s), ascending in s."""
    c = F(2) * a / rho
    coeff = [F(1)]
    for j in range(terms):
        q = c * beta ** (2 * j)
        nxt = [F(0)] * (len(coeff) + 1)
        for k, v in enumerate(coeff):
            nxt[k] += v
            nxt[k + 1] += v * q
        coeff = nxt
    return coeff


def product_values(beta: F, a: F, rho: F) -> list[dict]:
    c = F(2) * a / rho
    rows = []
    for s in SPOT_S:
        value = F(1)
        for j in range(PRODUCT_TERMS):
            value *= F(1) + c * beta ** (2 * j) * s
        rows.append({"s": ftext(s), "prefix_laplace": ftext(F(1, 1) / value), "terms": PRODUCT_TERMS})
    return rows


def markov_skeleton(beta: F, a: F, rho: F) -> list[dict]:
    """A rational deterministic hazard skeleton, used only to audit rewards."""
    y = F(1)
    rows: list[dict] = []
    for step in range(SKELETON_STEPS):
        increment = F(1)  # choose Y_{n+1}-beta Y_n=1, hence T=1/a
        nxt = beta * y + increment
        hazard = rho * (nxt * nxt - beta * beta * y * y) / (F(2) * a)
        rewards = []
        for m in range(0, 5):
            rewards.append({"order": m, "integral_times_a": ftext((nxt ** (m + 1) - (beta * y) ** (m + 1)) / F(m + 1))})
        rows.append({"step": step, "y_pre": ftext(y), "y_next": ftext(nxt), "jump_hazard_exponential": ftext(hazard), "waiting_time_times_a": ftext(increment), "reward_rows": rewards})
        y = nxt
    return rows


def parameter_row(beta: F, a: F, rho: F) -> dict:
    zm = z_moments(beta, a, rho)
    coeff = generator_coefficients(beta, a, rho)
    return {
        "beta": ftext(beta), "a": ftext(a), "rho": ftext(rho), "c": ftext(F(2) * a / rho),
        "embedded_square_moments": [{"order": i, "value": ftext(v)} for i, v in enumerate(zm)],
        "generator_moment_coefficients": coeff,
        "q_product": {"variable": "s", "factor_formula": "(1 + (2*a/rho)*beta^(2*j)*s)^(-1)", "terms": PRODUCT_TERMS, "prefix_coefficients": [ftext(v) for v in product_prefix(beta, a, rho)]},
        "q_product_spot_values": product_values(beta, a, rho),
        "stationary_markov_renewal_occupation": {
            "formula": "M_m=(1-beta^(m+1))*E_pi[Y^(m+1)]/((m+1)*(1-beta)*E_pi[Y])",
            "mean_symbol": "mu=M_1=a/(rho*(1-beta)*E_pi[Y])",
            "not_iid_regeneration_for_beta_positive": True,
        },
        "deterministic_hazard_skeleton": markov_skeleton(beta, a, rho),
        "contraction_factor": ftext(beta ** 2),
    }


def build() -> dict:
    rows = [parameter_row(b, a, r) for b in BETAS for a in A_VALUES for r in RHO_VALUES]
    boundaries = [
        {"face": "beta=0,a>0,rho>0", "verdict": "RESET_REGENERATION", "law": "post-jump state is zero; successive cycles are iid, Y^2=(2a/rho)E, pre-jump Rayleigh density (rho/a)y*exp(-rho*y^2/(2a)), and continuous occupation f(x)=sqrt(2rho/(pi*a))*exp(-rho*x^2/(2a)) with mean sqrt(2a/(pi*rho))"},
        {"face": "beta=1,a>0,rho>0", "verdict": "NO_INVARIANT", "law": "multiplicative jump is identity while positive drift escapes to infinity"},
        {"face": "a=0,0<=beta<1,rho>0", "verdict": "DELTA_ZERO_ONLY_ON_CLOSED_HALF_LINE", "law": "zero is the unique invariant atom on [0,infinity); the positive-state model X>0 has no invariant probability"},
        {"face": "a=0,beta=1,rho>0", "verdict": "EVERY_LAW_INVARIANT", "law": "jumps leave X unchanged and there is no drift"},
        {"face": "a=0,rho=0,0<=beta<=1", "verdict": "EVERY_LAW_INVARIANT", "law": "no drift and no jumps"},
        {"face": "rho=0,a>0", "verdict": "NO_INVARIANT", "law": "deterministic linear escape X_t=X_0+a t"},
        {"face": "beta=1,a>0,rho=0", "verdict": "NO_INVARIANT", "law": "the rho=0 linear-escape face applies"},
    ]
    data = {
        "schema": "hcs-c246-tcp-aimd-v1", "candidate_id": "HCS-C246", "evaluation_date": EVALUATION_DATE, "fixed_epoch": FIXED_EPOCH, "source_commit": SOURCE_COMMIT, "scope_literal": SCOPE,
        "evaluator": {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256},
        "headline": "Exact affine-perpetuity, moment-recursion, and stationary Markov-renewal occupation certificates for a linear-rate AIMD jump process.",
        "frozen_object": {
            "process": "Xdot=a>0; jump intensity rho*X; post-jump X->beta*X",
            "state": "X>0 with right-continuous jump paths",
            "parameters": "beta in {1/2,2/3,3/4}, a in {1/2,1,3/2}, rho in {1/2,1,2}",
            "jump_skeleton": "Y_n is pre-jump; Y_{n+1}=beta*Y_n+a*T_{n+1}",
            "hazard": "rho*(beta*Y_n*T+a*T^2/2)=E_{n+1}, E exponential(1)",
            "clock": "continuous event time and jump count; no arithmetic-prime clock",
            "determinant_convention": "q-product is a source-local Laplace transform, never an Euler factor or target determinant",
            "cutoff": "moment orders 0..8, q-product prefix 12, three rational parameter grids, six-step rational hazard skeleton",
            "forbidden_data": "target primes/zeros, local arithmetic, Euler factors, root numbers, automorphy, target divisors, Hilbert-Polya operators",
        },
        "theorem": {
            "jump_square_recurrence": "Y_{n+1}^2=beta^2 Y_n^2 + 2*a*E_{n+1}/rho for the pre-jump chain",
            "perpetuity": "Z=Y^2 has unique stationary perpetuity Z_d=2a/rho * sum_{j>=0} beta^(2j) E_{-j}",
            "q_product": "psi(s)=prod_{j>=0}(1+2*a*beta^(2j)*s/rho)^(-1), a source-local Laplace product",
            "uniqueness_convergence": "Synchronous coupling contracts squared states by beta^2 each step; E[Z_infty]=(2a/rho)/(1-beta^2)<infinity proves the perpetuity series is finite almost surely, and it gives the unique stationary jump-chain law and convergence from every finite Z_0",
            "generator_identity": "For stationary moments M_m, rho*(1-beta^m)M_{m+1}=a*m*M_{m-1} for m>=1",
            "continuous_laplace_generator": "For phi(s)=E_stat[e^{-sX}], phi'(s)-phi'(beta*s)=(a/rho)*s*phi(s)",
            "all_moment_recursion": "M_0=1, M_1=mu, and the displayed recurrence gives every M_m as an exact affine expression in mu",
            "occupation": "The continuous-time stationary law is the stationary Markov-renewal/Palm reward measure with M_m=(1-beta^(m+1))*E_pi[Y^(m+1)]/((m+1)(1-beta)E_pi[Y])",
            "boundary_scope": "beta=0 is the only iid reset/regeneration face (Rayleigh pre-jump law and half-normal occupation density); beta=1,a=0,rho=0 are separately audited with exact invariant/noninvariant corner statements",
        },
        "regression": {"beta_values": [ftext(x) for x in BETAS], "a_values": [ftext(x) for x in A_VALUES], "rho_values": [ftext(x) for x in RHO_VALUES], "parameter_rows": rows, "parameter_row_count": len(rows), "moment_max": MOMENT_MAX, "product_terms": PRODUCT_TERMS, "skeleton_steps": SKELETON_STEPS, "boundary_rows": boundaries},
        "exact_identities": [
            {"name": "hazard_integral", "formula": "rho*(beta*y*T+a*T^2/2)=E"},
            {"name": "square_completion", "formula": "(beta*y+a*T)^2-beta^2*y^2=2*a*E/rho"},
            {"name": "perpetuity_fixed_point", "formula": "Z law = beta^2 Z + (2a/rho)E"},
            {"name": "q_product_factor", "formula": "Laplace(E)=1/(1+s), scaled factor=(1+(2a/rho)beta^(2j)s)^(-1)"},
            {"name": "generator_moment", "formula": "a*m*M_(m-1)+rho*(beta^m-1)*M_(m+1)=0"},
            {"name": "occupation_reward", "formula": "int_(beta*y)^(y_next) x^m dx/a=(y_next^(m+1)-(beta*y)^(m+1))/(a*(m+1))"},
            {"name": "occupation_ratio", "formula": "M_m=(1-beta^(m+1))*E_pi[Y^(m+1)]/((m+1)*(1-beta)*E_pi[Y])"},
            {"name": "stationary_laplace_generator", "formula": "phi'(s)-phi'(beta*s)=(a/rho)*s*phi(s)"},
            {"name": "contraction", "formula": "|Z_n-Z'_n|=beta^(2n)|Z_0-Z'_0| under common hazards"},
            {"name": "domain", "formula": "a>0, rho>0, 0<beta<1"},
        ],
        "route_a": {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False, "strongest_positive": "exact affine-perpetuity, q-product, generator recurrence, uniqueness/convergence, and stationary Markov-renewal occupation identities", "strongest_failure": "stochastic source has no deterministic primitive orbit atlas or target arithmetic determinant"},
        "scope_flags": {"uses_target_zero_table": False, "uses_prime_table": False, "claims_arithmetic_local_data": False, "claims_euler_factors": False, "claims_root_numbers": False, "claims_automorphy": False, "claims_target_divisor_or_functional_equation": False, "claims_hilbert_polya_operator": False, "invokes_route_b": False},
        "citations": [
            {"key": "DumasGuilleminRobert2002", "claim": "Markovian analysis and invariant probabilities for additive-increase multiplicative-decrease algorithms", "source": "https://doi.org/10.1239/aap/1019160951", "doi": "10.1239/aap/1019160951"},
            {"key": "GuilleminRobertZwart2004", "claim": "AIMD algorithms, exponential functionals, and stationary transform methods", "source": "https://doi.org/10.1214/aoap/1075828048", "doi": "10.1214/aoap/1075828048"},
        ],
        "nonclaims": [
            "For beta>0 the embedded jump sequence is a stationary Markov chain; no iid regeneration claim is made.",
            "The q-product is a source-local Laplace product, not an Euler factor, arithmetic local factor, or target determinant.",
            "Odd continuous-time moments are recorded through the exact generator recurrence and Palm ratio with the symbolic mean mu; no unwarranted elementary closed form for E_pi[Y] is asserted.",
            "The six-step rational hazard skeleton is an audit control, not a sample from an external data set and not a global numerical experiment.",
            "No arithmetic origin, automorphy, target functional equation, Hilbert-Polya operator, or Route-B input is claimed.",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = ap.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    raw = json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    tmp = args.output.with_name(args.output.name + ".tmp")
    tmp.write_text(raw)
    os.replace(tmp, args.output)
    print(json.dumps({"status": "C246_PRODUCER_PASS", "payload_sha256": data["payload_sha256"], "evidence_sha256": sha256(raw.encode()).hexdigest(), "parameter_rows": len(data["regression"]["parameter_rows"]), "moment_max": MOMENT_MAX}, sort_keys=True))


if __name__ == "__main__":
    main()
