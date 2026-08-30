#!/usr/bin/env python3
"""Producer-independent exact checker for the C246 AIMD receipt."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import json
from hashlib import sha256
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c246_tcp_aimd_evidence.json"
SOURCE_COMMIT = "5f357e2d2b78604f6c286bfbd05da922e1d6791f"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FIXED_EPOCH = 1788048000
EVALUATION_DATE = "2026-08-30"
BETAS = (F(1, 2), F(2, 3), F(3, 4))
A_VALUES = (F(1, 2), F(1), F(3, 2))
RHO_VALUES = (F(1, 2), F(1), F(2))
MOMENT_MAX = 8
PRODUCT_TERMS = 12
SPOT_S = (F(1, 2), F(1), F(2))
SKELETON_STEPS = 6

TOP_KEYS = {"schema", "candidate_id", "evaluation_date", "fixed_epoch", "source_commit", "scope_literal", "evaluator", "headline", "frozen_object", "theorem", "regression", "exact_identities", "route_a", "scope_flags", "citations", "nonclaims", "payload_sha256"}
SCOPE_KEYS = {"uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"}


def ftext(q: F | int) -> str:
    q = q if isinstance(q, F) else F(q)
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def z_moments(beta: F, a: F, rho: F) -> list[F]:
    c = F(2) * a / rho
    out = [F(1)]
    for m in range(1, MOMENT_MAX + 1):
        rhs = F(0)
        for j in range(m):
            rhs += F(math.comb(m, j)) * beta ** (2 * j) * c ** (m - j) * out[j] * F(math.factorial(m - j))
        out.append(rhs / (F(1) - beta ** (2 * m)))
    return out


def gen_coeff(beta: F, a: F, rho: F) -> list[dict]:
    coeff: list[tuple[F, F]] = [(F(1), F(0)), (F(0), F(1))]
    for m in range(1, MOMENT_MAX):
        fac = F(a * m, 1) / (rho * (F(1) - beta ** m))
        coeff.append((fac * coeff[m - 1][0], fac * coeff[m - 1][1]))
    return [{"order": i, "constant": ftext(c), "mu_coefficient": ftext(k)} for i, (c, k) in enumerate(coeff)]


def prefix(beta: F, a: F, rho: F) -> list[F]:
    c = F(2) * a / rho
    out = [F(1)]
    for j in range(PRODUCT_TERMS):
        q = c * beta ** (2 * j)
        nxt = [F(0)] * (len(out) + 1)
        for i, v in enumerate(out):
            nxt[i] += v
            nxt[i + 1] += q * v
        out = nxt
    return out


def spots(beta: F, a: F, rho: F) -> list[dict]:
    c = F(2) * a / rho
    out = []
    for s in SPOT_S:
        den = F(1)
        for j in range(PRODUCT_TERMS):
            den *= F(1) + c * beta ** (2 * j) * s
        out.append({"s": ftext(s), "prefix_laplace": ftext(F(1, 1) / den), "terms": PRODUCT_TERMS})
    return out


def skeleton(beta: F, a: F, rho: F) -> list[dict]:
    y = F(1)
    out = []
    for step in range(SKELETON_STEPS):
        nxt = beta * y + 1
        h = rho * (nxt * nxt - beta * beta * y * y) / (F(2) * a)
        rewards = [{"order": m, "integral_times_a": ftext((nxt ** (m + 1) - (beta * y) ** (m + 1)) / F(m + 1))} for m in range(5)]
        out.append({"step": step, "y_pre": ftext(y), "y_next": ftext(nxt), "jump_hazard_exponential": ftext(h), "waiting_time_times_a": "1", "reward_rows": rewards})
        y = nxt
    return out


def row(beta: F, a: F, rho: F) -> dict:
    return {"beta": ftext(beta), "a": ftext(a), "rho": ftext(rho), "c": ftext(F(2) * a / rho), "embedded_square_moments": [{"order": i, "value": ftext(v)} for i, v in enumerate(z_moments(beta, a, rho))], "generator_moment_coefficients": gen_coeff(beta, a, rho), "q_product": {"variable": "s", "factor_formula": "(1 + (2*a/rho)*beta^(2*j)*s)^(-1)", "terms": PRODUCT_TERMS, "prefix_coefficients": [ftext(v) for v in prefix(beta, a, rho)]}, "q_product_spot_values": spots(beta, a, rho), "stationary_markov_renewal_occupation": {"formula": "M_m=(1-beta^(m+1))*E_pi[Y^(m+1)]/((m+1)*(1-beta)*E_pi[Y])", "mean_symbol": "mu=M_1=a/(rho*(1-beta)*E_pi[Y])", "not_iid_regeneration_for_beta_positive": True}, "deterministic_hazard_skeleton": skeleton(beta, a, rho), "contraction_factor": ftext(beta ** 2)}


def expected() -> tuple[list[dict], list[dict]]:
    rows = [row(b, a, r) for b in BETAS for a in A_VALUES for r in RHO_VALUES]
    bounds = [{"face": "beta=0,a>0,rho>0", "verdict": "RESET_REGENERATION", "law": "post-jump state is zero; successive cycles are iid, Y^2=(2a/rho)E, pre-jump Rayleigh density (rho/a)y*exp(-rho*y^2/(2a)), and continuous occupation f(x)=sqrt(2rho/(pi*a))*exp(-rho*x^2/(2a)) with mean sqrt(2a/(pi*rho))"}, {"face": "beta=1,a>0,rho>0", "verdict": "NO_INVARIANT", "law": "multiplicative jump is identity while positive drift escapes to infinity"}, {"face": "a=0,0<=beta<1,rho>0", "verdict": "DELTA_ZERO_ONLY_ON_CLOSED_HALF_LINE", "law": "zero is the unique invariant atom on [0,infinity); the positive-state model X>0 has no invariant probability"}, {"face": "a=0,beta=1,rho>0", "verdict": "EVERY_LAW_INVARIANT", "law": "jumps leave X unchanged and there is no drift"}, {"face": "a=0,rho=0,0<=beta<=1", "verdict": "EVERY_LAW_INVARIANT", "law": "no drift and no jumps"}, {"face": "rho=0,a>0", "verdict": "NO_INVARIANT", "law": "deterministic linear escape X_t=X_0+a t"}, {"face": "beta=1,a>0,rho=0", "verdict": "NO_INVARIANT", "law": "the rho=0 linear-escape face applies"}]
    return rows, bounds


_CACHE = None


def validate(data: dict) -> int:
    global _CACHE
    checks = 0

    def check(ok: bool, label: str) -> None:
        nonlocal checks
        checks += 1
        if not ok:
            raise AssertionError(label)

    check(set(data) == TOP_KEYS, "top closure")
    check(data["schema"] == "hcs-c246-tcp-aimd-v1" and data["candidate_id"] == "HCS-C246", "schema/candidate")
    check(data["evaluation_date"] == EVALUATION_DATE and data["fixed_epoch"] == FIXED_EPOCH, "date/epoch")
    check(data["source_commit"] == SOURCE_COMMIT and data["scope_literal"] == SCOPE, "source/scope")
    check(data["evaluator"] == {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256}, "evaluator")
    check(data["payload_sha256"] == payload_hash(data), "payload hash")
    check(data["route_a"]["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "route tuple")
    check(data["route_a"]["overall"] == "ROUTE_A_REJECTED" and data["route_a"]["route_b_invocation_allowed"] is False, "route verdict")
    check(set(data["scope_flags"]) == SCOPE_KEYS and all(v is False for v in data["scope_flags"].values()), "scope firewall")
    check(len(data["exact_identities"]) == 10, "identity count")
    check(data["regression"]["beta_values"] == ["1/2", "2/3", "3/4"], "beta grid")
    check(data["regression"]["a_values"] == ["1/2", "1", "3/2"], "a grid")
    check(data["regression"]["rho_values"] == ["1/2", "1", "2"], "rho grid")
    expected_ids = [{"name": "hazard_integral", "formula": "rho*(beta*y*T+a*T^2/2)=E"}, {"name": "square_completion", "formula": "(beta*y+a*T)^2-beta^2*y^2=2*a*E/rho"}, {"name": "perpetuity_fixed_point", "formula": "Z law = beta^2 Z + (2a/rho)E"}, {"name": "q_product_factor", "formula": "Laplace(E)=1/(1+s), scaled factor=(1+(2a/rho)beta^(2j)s)^(-1)"}, {"name": "generator_moment", "formula": "a*m*M_(m-1)+rho*(beta^m-1)*M_(m+1)=0"}, {"name": "occupation_reward", "formula": "int_(beta*y)^(y_next) x^m dx/a=(y_next^(m+1)-(beta*y)^(m+1))/(a*(m+1))"}, {"name": "occupation_ratio", "formula": "M_m=(1-beta^(m+1))*E_pi[Y^(m+1)]/((m+1)*(1-beta)*E_pi[Y])"}, {"name": "stationary_laplace_generator", "formula": "phi'(s)-phi'(beta*s)=(a/rho)*s*phi(s)"}, {"name": "contraction", "formula": "|Z_n-Z'_n|=beta^(2n)|Z_0-Z'_0| under common hazards"}, {"name": "domain", "formula": "a>0, rho>0, 0<beta<1"}]
    check(data["exact_identities"] == expected_ids, "identity values")
    expected_citations = [{"key": "DumasGuilleminRobert2002", "claim": "Markovian analysis and invariant probabilities for additive-increase multiplicative-decrease algorithms", "source": "https://doi.org/10.1239/aap/1019160951", "doi": "10.1239/aap/1019160951"}, {"key": "GuilleminRobertZwart2004", "claim": "AIMD algorithms, exponential functionals, and stationary transform methods", "source": "https://doi.org/10.1214/aoap/1075828048", "doi": "10.1214/aoap/1075828048"}]
    check(data["citations"] == expected_citations, "citation closure")
    check(len(data["nonclaims"]) == 5 and "iid regeneration" in data["nonclaims"][0], "nonclaim closure")
    expected_theorem = {
        "jump_square_recurrence": "Y_{n+1}^2=beta^2 Y_n^2 + 2*a*E_{n+1}/rho for the pre-jump chain",
        "perpetuity": "Z=Y^2 has unique stationary perpetuity Z_d=2a/rho * sum_{j>=0} beta^(2j) E_{-j}",
        "q_product": "psi(s)=prod_{j>=0}(1+2*a*beta^(2j)*s/rho)^(-1), a source-local Laplace product",
        "uniqueness_convergence": "Synchronous coupling contracts squared states by beta^2 each step; E[Z_infty]=(2a/rho)/(1-beta^2)<infinity proves the perpetuity series is finite almost surely, and it gives the unique stationary jump-chain law and convergence from every finite Z_0",
        "generator_identity": "For stationary moments M_m, rho*(1-beta^m)M_{m+1}=a*m*M_{m-1} for m>=1",
        "continuous_laplace_generator": "For phi(s)=E_stat[e^{-sX}], phi'(s)-phi'(beta*s)=(a/rho)*s*phi(s)",
        "all_moment_recursion": "M_0=1, M_1=mu, and the displayed recurrence gives every M_m as an exact affine expression in mu",
        "occupation": "The continuous-time stationary law is the stationary Markov-renewal/Palm reward measure with M_m=(1-beta^(m+1))*E_pi[Y^(m+1)]/((m+1)(1-beta)E_pi[Y])",
        "boundary_scope": "beta=0 is the only iid reset/regeneration face (Rayleigh pre-jump law and half-normal occupation density); beta=1,a=0,rho=0 are separately audited with exact invariant/noninvariant corner statements",
    }
    check(data["theorem"] == expected_theorem, "theorem values")
    if _CACHE is None:
        _CACHE = expected()
    rows, bounds = _CACHE
    reg = data["regression"]
    check(reg["parameter_rows"] == rows, "parameter rows exact")
    check(reg["boundary_rows"] == bounds, "boundary rows exact")
    check(reg["parameter_row_count"] == len(rows) == 27, "row count")
    check(reg["moment_max"] == MOMENT_MAX and reg["product_terms"] == PRODUCT_TERMS and reg["skeleton_steps"] == SKELETON_STEPS, "cutoffs")
    for r in rows:
        check(r["stationary_markov_renewal_occupation"]["not_iid_regeneration_for_beta_positive"] is True, "Markov-renewal wording")
        check(all(x["jump_hazard_exponential"] == ftext(F(x["jump_hazard_exponential"])) for x in r["deterministic_hazard_skeleton"]), "hazard serialization")
    return checks


def quick_preflight(data: dict) -> None:
    assert set(data) == TOP_KEYS and data["payload_sha256"] == payload_hash(data)
    assert data["candidate_id"] == "HCS-C246" and data["fixed_epoch"] == FIXED_EPOCH
    print("C246 quick hostile preflight: PASS")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    ap.add_argument("--quick", action="store_true")
    args = ap.parse_args()
    data = json.loads(args.evidence.read_text())
    if args.quick:
        quick_preflight(data)
    else:
        print(f"C246 independent checker: PASS ({validate(data)} assertions; independent Fraction perpetuity and occupation checks)")


if __name__ == "__main__":
    main()
