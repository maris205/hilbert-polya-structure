#!/usr/bin/env python3
"""Canonical numerical certificate for Brownian motion with resetting.

The producer is deliberately source-local: it evaluates a fixed rational grid
of the renewal formulae, but never imports a prime/zero table or a target
quantity.  All decimal values are generated at a fixed precision so that a
clean-process replay is byte-for-byte reproducible.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import mpmath as mp

SOURCE_COMMIT = "077a098ac5811e465b69db71b5e6031a4827eb55"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c214_brownian_evidence.json"

# Positive rational sentinels.  The theorem is all-parameter; these rows are
# regression evidence only and are intentionally independent of any target
# arithmetic data.
D_VALUES = [F(1, 2), F(1), F(2)]
R_VALUES = [F(1, 4), F(1), F(4)]
A_VALUES = [F(1, 2), F(1), F(2)]
X_VALUES = [F(-1), F(0), F(1)]
T_VALUES = [F(1, 5), F(1), F(2)]
S_VALUES = [F(0), F(1, 5), F(1), F(3)]
WORKING_DECIMAL_DIGITS = 100
SERIALIZED_SIGNIFICANT_DIGITS = 82


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    encoded = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(encoded).hexdigest()


def mpq(value: F) -> mp.mpf:
    return mp.mpf(value.numerator) / value.denominator


def fmt(value: mp.mpf) -> str:
    return mp.nstr(value, SERIALIZED_SIGNIFICANT_DIGITS, strip_zeros=False)


def free_density(D: F, x: F, t: F) -> mp.mpf:
    """Heat kernel G(x,t) from the origin."""
    dd, xx, tt = mpq(D), mpq(x), mpq(t)
    return mp.exp(-(xx * xx) / (4 * dd * tt)) / mp.sqrt(4 * mp.pi * dd * tt)


def reset_integral(D: F, r: F, x: F, t: F) -> mp.mpf:
    """I(t)=integral_0^t exp(-r*u)G(x,u)du in closed erfc form."""
    dd, rr, xx, tt = mpq(D), mpq(r), abs(mpq(x)), mpq(t)
    root = mp.sqrt(rr / dd)
    b = xx * root
    u = xx / (2 * mp.sqrt(dd * tt))
    v = mp.sqrt(rr * tt)
    # The x=0 branch avoids cancellation in erfc(-v)-erfc(v).
    if x == 0:
        return mp.erf(v) / (2 * mp.sqrt(dd * rr))
    return (mp.exp(-b) * mp.erfc(u - v) - mp.exp(b) * mp.erfc(u + v)) / (4 * mp.sqrt(dd * rr))


def reset_density(D: F, r: F, x: F, t: F) -> mp.mpf:
    return mp.exp(-mpq(r) * mpq(t)) * free_density(D, x, t) + mpq(r) * reset_integral(D, r, x, t)


def stationary_density(D: F, r: F, x: F) -> mp.mpf:
    root = mp.sqrt(mpq(r) / mpq(D))
    return root * mp.exp(-abs(mpq(x)) * root) / 2


def fpt_laplace(D: F, r: F, a: F, s: F) -> tuple[mp.mpf, mp.mpf]:
    """Return reset FPT and survival Laplace transforms."""
    dd, rr, aa, ss = mpq(D), mpq(r), mpq(a), mpq(s)
    q = ss + rr
    e = mp.exp(-aa * mp.sqrt(q / dd))
    denominator = ss + rr * e
    f = q * e / denominator
    survival = (1 - e) / denominator
    return f, survival


def mfpt(D: F, r: F, a: F) -> mp.mpf:
    z = mpq(a) * mp.sqrt(mpq(r) / mpq(D))
    return mp.expm1(z) / mpq(r)


def optimal_root() -> mp.mpf:
    # The equation also has the boundary root z=0.  The bracket (1,2)
    # selects the unique positive stationary point.
    return mp.findroot(lambda z: z - 2 * (1 - mp.exp(-z)), (mp.mpf("1.2"), mp.mpf("1.9")))


def build() -> dict:
    mp.mp.dps = WORKING_DECIMAL_DIGITS
    propagator_rows = []
    for D in D_VALUES:
        for r in R_VALUES:
            for x in X_VALUES:
                for t in T_VALUES:
                    free = free_density(D, x, t)
                    integral = reset_integral(D, r, x, t)
                    density = mp.exp(-mpq(r) * mpq(t)) * free + mpq(r) * integral
                    propagator_rows.append({
                        "case_id": f"D{D}_r{r}_x{x}_t{t}",
                        "D": str(D), "r": str(r), "x": str(x), "t": str(t),
                        "free_density": fmt(free), "reset_integral": fmt(integral),
                        "reset_density": fmt(density),
                        "stationary_density": fmt(stationary_density(D, r, x)),
                    })

    stationary_rows = []
    normalization_rows = []
    for D in D_VALUES:
        for r in R_VALUES:
            for x in X_VALUES:
                stationary_rows.append({
                    "case_id": f"D{D}_r{r}_x{x}", "D": str(D), "r": str(r), "x": str(x),
                    "density": fmt(stationary_density(D, r, x)),
                })
            # Exact normalization is checked independently by quadrature in
            # the checker; the serialized value records the expected result.
            normalization_rows.append({"case_id": f"D{D}_r{r}", "D": str(D), "r": str(r), "integral": "1"})

    fpt_rows = []
    for D in D_VALUES:
        for r in R_VALUES:
            for a in A_VALUES:
                for s in S_VALUES:
                    f, survival = fpt_laplace(D, r, a, s)
                    fpt_rows.append({
                        "case_id": f"D{D}_r{r}_a{a}_s{s}",
                        "D": str(D), "r": str(r), "a": str(a), "s": str(s),
                        "shifted_free_fpt": fmt(mp.exp(-mpq(a) * mp.sqrt((mpq(s) + mpq(r)) / mpq(D)))),
                        "fpt_laplace": fmt(f), "survival_laplace": fmt(survival),
                    })

    mfpt_rows = []
    for D in D_VALUES:
        for r in R_VALUES:
            for a in A_VALUES:
                z = mpq(a) * mp.sqrt(mpq(r) / mpq(D))
                val = mfpt(D, r, a)
                mfpt_rows.append({
                    "case_id": f"D{D}_r{r}_a{a}", "D": str(D), "r": str(r), "a": str(a),
                    "z": fmt(z), "mfpt": fmt(val),
                    "scaled_mfpt": fmt(val * mpq(D) / (mpq(a) * mpq(a))),
                    "optimal_rate": fmt(mpq(D) * (optimal_root() / mpq(a)) ** 2),
                })

    z_star = optimal_root()
    # Keep boundary behavior explicit and textual: these are limits of the
    # frozen positive-parameter theorem, not rows fed into its denominator.
    boundaries = [
        {"boundary_id": "r_zero", "parameter": "r=0", "statement": "ordinary Brownian motion; no normalizable stationary density; E[T_a]=infinity for a>0"},
        {"boundary_id": "a_zero", "parameter": "a=0", "statement": "the start is already absorbed; T=0, F(s)=1 and the positive-target optimum is not applicable"},
        {"boundary_id": "D_zero", "parameter": "D=0", "statement": "deterministic reset-at-origin path cannot reach a>0; F(s)=0 and E[T_a]=infinity"},
        {"boundary_id": "all_zero_target", "parameter": "a=r=0", "statement": "absorbed at time zero; this is separate from the positive-parameter family"},
    ]

    data = {
        "schema": "hcs-c214-brownian-resetting-v1",
        "candidate_id": "HCS-C214",
        "evaluation_date": "2026-08-28",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "evaluator": {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256},
        "headline": "Brownian resetting has an exact renewal propagator, first-passage transform and universal optimal reset rate",
        "frozen_object": {
            "phase_space": "free realization on R; killed-search realization on (-infinity,a) with absorbing boundary a and reset point 0",
            "process": "free: dX_t=sqrt(2D)dW_t with rate-r resets to 0; search: same dynamics on (-infinity,a), started at 0 and killed at a",
            "generator": "L f(x)=D f''(x)+r(f(0)-f(x)) on R for the free process, with Dirichlet killing at a for the search realization",
            "parameters": "D>0, r>0, a>0; physical t>=0",
            "clock": "physical elapsed time; no fitted or logarithmic clock",
            "normalization": "for t>0 the free propagator and stationary law are absolutely continuous Lebesgue densities on R; the killed search is sub-Markov on (-infinity,a)",
            "determinant_convention": "none; Laplace denominators are renewal resolvents, never dynamical zeta or Fredholm determinants",
            "arithmetic_origin": "none; this is a scope-locked non-arithmetic stochastic control",
            "allowed_data": "exact rational D,r,a,s,x,t sentinels and source-local heat-kernel/renewal algebra",
            "forbidden_data": "prime/zero tables, target labels, fitted rates, Euler factors and external observations",
        },
        "theorem": {
            "free_kernel": "G_D(x,t)=(4*pi*D*t)^(-1/2) exp(-x^2/(4*D*t))",
            "renewal_propagator": "p_r(x,t|0)=exp(-r*t)G_D(x,t)+r*integral_0^t exp(-r*u)G_D(x,u)du",
            "reset_integral": "I_t(x)=[exp(-|x|sqrt(r/D)) erfc(|x|/(2sqrt(Dt))-sqrt(rt))-exp(|x|sqrt(r/D)) erfc(|x|/(2sqrt(Dt))+sqrt(rt))]/(4sqrt(D*r)), with the continuous x=0 branch",
            "stationary_laplace": "p_st(x)=sqrt(r/D) exp(-|x|sqrt(r/D))/2 and integral_R p_st dx=1",
            "fpt_laplace": "F_r(s)=((s+r) exp(-a sqrt((s+r)/D)))/(s+r exp(-a sqrt((s+r)/D)))",
            "survival_laplace": "S_r(s)=(1-exp(-a sqrt((s+r)/D)))/(s+r exp(-a sqrt((s+r)/D)))",
            "mfpt": "E[T_a]=(exp(a sqrt(r/D))-1)/r",
            "optimality": "For z=a sqrt(r/D), (D/a^2)E[T_a]=(exp(z)-1)/z^2; its unique positive minimizer solves z=2(1-exp(-z)), z*=1.5936242600400400923... and r*=D(z*/a)^2",
            "moments": "All moments are finite for D,r,a>0; for every n>=0, (-1)^n F_r^(n)(0)=E[T_a^n] and (-1)^n S_r^(n)(0)=E[T_a^(n+1)]/(n+1)",
            "boundaries": "r=0 has no stationary law and infinite mean hitting time; a=0 gives T=0; D=0 cannot reach a>0 from the reset point",
        },
        "regression": {
            "D_values": [str(x) for x in D_VALUES], "r_values": [str(x) for x in R_VALUES],
            "a_values": [str(x) for x in A_VALUES], "x_values": [str(x) for x in X_VALUES],
            "t_values": [str(x) for x in T_VALUES], "s_values": [str(x) for x in S_VALUES],
            "propagator_rows": propagator_rows, "stationary_rows": stationary_rows,
            "normalization_rows": normalization_rows, "fpt_rows": fpt_rows,
            "mfpt_rows": mfpt_rows, "boundary_rows": boundaries,
            "optimality": {"equation": "z-2*(1-exp(-z))=0", "z_star": fmt(z_star), "equation_residual": fmt(z_star - 2 * (1 - mp.exp(-z_star))), "scaled_optimal_rate": fmt(z_star * z_star)},
        },
        "summary": {
            "propagator_row_count": len(propagator_rows), "stationary_row_count": len(stationary_rows),
            "normalization_row_count": len(normalization_rows), "fpt_row_count": len(fpt_rows),
            "mfpt_row_count": len(mfpt_rows), "boundary_row_count": len(boundaries),
            "serialized_decimal_digits": SERIALIZED_SIGNIFICANT_DIGITS,
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
            "strongest_positive": "An exact nonlocal diffusion-renewal theorem closes propagator, stationary law, first passage, moments, and the universal reset optimum.",
            "strongest_failure": "No intrinsic rational-prime carrier, primitive periodic-orbit clock, arithmetic divisor, or natural Hilbert-Polya lift is present.",
        },
        "scope_flags": {k: False for k in ["uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"]},
        "citations": [
            {"key": "EvansMajumdar2011PRL", "claim": "fixed-point stochastic resetting renewal framework and stationary density", "title": "Diffusion with Stochastic Resetting", "authors": "Martin R. Evans and Satya N. Majumdar", "venue": "Physical Review Letters 106, 160601", "date": "2011", "url": "https://doi.org/10.1103/PhysRevLett.106.160601", "persistent_url": "https://doi.org/10.1103/PhysRevLett.106.160601"},
            {"key": "EvansMajumdar2011JPA", "claim": "optimal resetting first-passage calculation", "title": "Diffusion with Optimal Resetting", "authors": "Martin R. Evans and Satya N. Majumdar", "venue": "Journal of Physics A: Mathematical and Theoretical 44, 435001", "date": "2011", "url": "https://doi.org/10.1088/1751-8113/44/43/435001", "persistent_url": "https://doi.org/10.1088/1751-8113/44/43/435001"},
            {"key": "EvansMajumdarSchehr2020", "claim": "review of resetting renewal and first-passage identities", "title": "Stochastic resetting and applications", "authors": "Martin R. Evans, Satya N. Majumdar and Grégory Schehr", "venue": "Journal of Physics A: Mathematical and Theoretical 53, 193001", "date": "2020", "url": "https://doi.org/10.1088/1751-8121/ab7cfe", "persistent_url": "https://doi.org/10.1088/1751-8121/ab7cfe"},
        ],
        "nonclaims": [
            "priority or novelty for stochastic resetting, its propagator, or its optimum",
            "a finite rational grid proves the all-parameter theorem",
            "the denominator s+r exp(-a sqrt((s+r)/D)) is a dynamical zeta, Fredholm determinant, or Euler factor",
            "any reset optimum or transform has arithmetic or target-zero meaning",
            "a Hilbert-Polya operator, target divisor, Euler factor, root number, automorphy, external review, or Route-B authorization",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    out = ap.parse_args().output
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(build(), sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    obj = json.loads(out.read_text())
    print(json.dumps({"status": "C214_PRODUCER_PASS", "output": str(out), "payload_sha256": obj["payload_sha256"], "propagator_rows": obj["summary"]["propagator_row_count"], "fpt_rows": obj["summary"]["fpt_row_count"]}, sort_keys=True))


if __name__ == "__main__":
    main()
