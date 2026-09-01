#!/usr/bin/env python3
"""Producer-independent checker for HCS-C282."""
from __future__ import annotations

import hashlib
import itertools
import json
import os
from fractions import Fraction as Q
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = Path(os.environ.get("C282_EVIDENCE", ROOT / "results/c282_ruin_evidence.json"))
SOURCE = "51fb3d46f96b854314811c1ad62d3103cd5d54e5"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
mp.mp.dps = 90
checks = 0

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


def claim(v: bool) -> None:
    global checks
    assert v; checks += 1


def ph(data: dict) -> str:
    clean = dict(data); clean.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(clean, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def fq(x: str) -> Q: return Q(x)
def mq(x: Q) -> mp.mpf: return mp.mpf(x.numerator)/x.denominator
def close(x: str, y, tol="1e-65") -> bool: return abs(mp.mpf(x)-y) <= mp.mpf(tol)*max(1, abs(y))


def reg(nu: Q, c: Q, beta: Q) -> str:
    if nu == 0: return "no_claims"
    if nu < c*beta: return "profitable"
    if nu == c*beta: return "critical"
    return "adverse"


def rq(nu, c, beta, q):
    return (c*beta-nu-q+mp.sqrt((c*beta-nu-q)**2+4*c*beta*q))/(2*c)


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    claim(data["payload_sha256"] == ph(data))
    claim(data["schema"] == "hcs-c282-cramer-lundberg-exponential-ruin-v1")
    claim(data["candidate_id"] == "HCS-C282" and data["source_commit"] == SOURCE)
    claim(data["evaluation_date"] == "2026-09-01" and data["fixed_epoch"] == 1788220800)
    claim(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER")
    claim(data["evaluator"] == {"version": "0.2.0", "sha256": EVAL})
    claim(data["proof_contract"]["status"] == "PROVABLE AS STATED")
    claim(data["route_a"] == {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
                               "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False})
    claim(all(v is False for v in data["scope_flags"].values()))
    claim(data["transform_contract"]["formula"] == "Phi_{q,s}(u)=(beta-r_q)/(beta+s)*exp(-r_q*u)")
    claim(data["transform_contract"]["root_selection"] == "q>0: boundedness selects the positive root; q=0 and 0<nu<c*beta: Phi(u)->0 selects beta-nu/c; q=0 and nu>=c*beta: boundedness selects 0; nu=0: Phi is identically zero")
    claim(data["transform_contract"]["uniqueness"] == "the convolution state J closes a two-dimensional inhomogeneous linear system; its characteristic polynomial is the root quadratic, J(0)=0 fixes the surviving coefficient, and chamber boundary conditions remove every other mode")
    claim(data["transform_contract"]["u_zero_extension"] == "common-path coupling and continuous claims extend the u>0 equation to strict ruin at u=0")
    claim(data["transform_contract"]["memoryless_factorization"] == "for nu>0, conditional on ruin, D is Exp(beta) and independent of tau; for nu=0 the conditional law is undefined")
    claim(data["model_contract"]["killed_owner"] == "X_t=U_t for t<tau and X_t=Delta for t>=tau; Phi is a first-passage functional of the underlying surplus U")
    claim(data["regime_contract"]["conditional_first_mean_profitable"] == "(1+nu*u/c)/(c*beta-nu)")
    claim(data["regime_contract"]["conditional_first_mean_adverse"] == "(beta*u+1)/(nu-c*beta)")

    rr = data["regression"]["regime_rows"]
    claim(len(rr) == 36)
    seen = set()
    for row in rr:
        nu, c, beta = fq(row["nu"]), fq(row["c"]), fq(row["beta"])
        seen.add((int(nu), int(c), int(beta)))
        regime = reg(nu, c, beta)
        claim(row["regime"] == regime)
        claim(fq(row["rho"]) == nu/(c*beta))
        claim(fq(row["mean_drift"]) == c-nu/beta)
        root0 = beta if nu == 0 else max(Q(0), beta-nu/c)
        claim(fq(row["q0_root"]) == root0)
        if regime == "profitable": claim(root0 > 0)
        elif regime in ("critical", "adverse"): claim(root0 == 0)
        else: claim(root0 == beta)
        p0 = Q(0) if nu == 0 else nu/(c*beta) if regime == "profitable" else Q(1)
        claim(fq(row["ultimate_ruin_at_zero"]) == p0)
    claim(seen == set(itertools.product(range(4), range(1, 4), range(1, 4))))

    tr = data["regression"]["transform_rows"]
    claim(len(tr) == 448)
    seen_tr = set()
    for row in tr:
        nu, c, beta, u, q, s = map(fq, (row["nu"], row["c"], row["beta"], row["u"], row["q"], row["s"]))
        claim(row["case"] in CASES)
        claim((nu, c, beta) == CASES[row["case"]])
        seen_tr.add((row["case"], u, q, s))
        n, cc, be, uu, qq, ss = map(mq, (nu, c, beta, u, q, s))
        r = rq(n, cc, be, qq)
        phi = (be-r)/(be+ss)*mp.exp(-r*uu)
        claim(close(row["root"], r))
        claim(close(row["joint_transform"], phi))
        claim(close(row["overshoot_factor"], be/(be+ss)))
        claim(close(row["ruin_time_factor"], (be-r)/be*mp.exp(-r*uu)))
        claim(abs(mp.mpf(row["quadratic_residual"])) < mp.mpf("1e-65"))
        claim(-mp.mpf("1e-70") <= r <= be+mp.mpf("1e-70"))
    claim(seen_tr == set(itertools.product(CASES, US, QS, SS)))

    means = data["regression"]["first_mean_rows"]
    claim(len(means) == 144)
    seen_means = set()
    for row in means:
        nu, c, beta, u = map(fq, (row["nu"], row["c"], row["beta"], row["u"]))
        seen_means.add((nu, c, beta, u))
        regime = reg(nu, c, beta)
        claim(row["regime"] == regime)
        if regime == "no_claims":
            claim(close(row["ruin_probability"], 0)); claim(row["conditional_mean_ruin_time"] is None); claim(row["conditional_mean_deficit"] is None)
        elif regime == "profitable":
            R = beta-nu/c
            claim(close(row["ruin_probability"], mq(nu/(c*beta))*mp.exp(-mq(R*u))))
            claim(close(row["conditional_mean_ruin_time"], mq((1+nu*u/c)/(c*beta-nu))))
            claim(close(row["conditional_mean_deficit"], mq(1/beta)))
        elif regime == "adverse":
            claim(close(row["ruin_probability"], 1))
            claim(close(row["conditional_mean_ruin_time"], mq((beta*u+1)/(nu-c*beta))))
            claim(close(row["conditional_mean_deficit"], mq(1/beta)))
        else:
            claim(close(row["ruin_probability"], 1)); claim(row["conditional_mean_ruin_time"] == "infinite")
            claim(close(row["conditional_mean_deficit"], mq(1/beta)))
    expected_mean_keys = set(itertools.product(
        (Q(i) for i in range(4)), (Q(i) for i in range(1, 4)),
        (Q(i) for i in range(1, 4)), US))
    claim(seen_means == expected_mean_keys)

    marts = data["regression"]["martingale_rows"]
    claim(len(marts) == 12)
    seen_marts = set()
    for row in marts:
        nu, c, beta, R, u = map(fq, (row["nu"], row["c"], row["beta"], row["adjustment_root"], row["initial_reserve"]))
        claim(row["case"] in CASES)
        claim((nu, c, beta) == CASES[row["case"]])
        claim(Q(0) < nu < c*beta)
        seen_marts.add((row["case"], u))
        claim(R == beta-nu/c)
        claim(fq(row["martingale_exponent"]) == 0)
        rho = nu/(c*beta)
        claim(fq(row["supremum_atom_at_zero"]) == 1-rho)
        claim(close(row["supremum_tail"], mq(rho)*mp.exp(-mq(R*u))))
    profitable_cases = tuple(k for k, (nu, c, beta) in CASES.items() if Q(0) < nu < c*beta)
    claim(seen_marts == set(itertools.product(profitable_cases, US)))
    expected_boundaries = [
        {"face": "profitable", "condition": "c*beta>nu>0", "status": "defective ruin; positive adjustment root"},
        {"face": "critical", "condition": "c*beta=nu>0", "status": "ruin certain; mean ruin time infinite; root has square-root q cusp"},
        {"face": "adverse", "condition": "c*beta<nu", "status": "ruin certain; finite mean ruin time"},
        {"face": "no_claims", "condition": "nu=0", "status": "ruin impossible for c>0"},
        {"face": "zero_reserve", "condition": "u=0", "status": "included; strict ruin occurs only after a claim"},
        {"face": "zero_premium", "condition": "c=0", "status": "outside frozen owner; the displayed root divides by c"},
    ]
    claim(data["regression"]["boundary_rows"] == expected_boundaries)
    claim(data["regression"]["counts"] == {"regime_rows": 36, "transform_rows": 448, "first_mean_rows": 144, "martingale_rows": 12, "boundary_rows": 6})
    print(f"C282 independent checker: PASS ({checks} assertions; producer-independent root and transform reconstruction)")


if __name__ == "__main__": main()
