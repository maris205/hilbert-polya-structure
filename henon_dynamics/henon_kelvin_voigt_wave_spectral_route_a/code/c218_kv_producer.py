#!/usr/bin/env python3
"""Produce the deterministic C218 Kelvin--Voigt spectral certificate."""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
import math
import os
from pathlib import Path

import mpmath as mp

SOURCE_COMMIT = "077a098ac5811e465b69db71b5e6031a4827eb55"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c218_kv_evidence.json"
MODES = list(range(1, 65))
CASES = [
    ("light", Fraction(1, 4)),
    ("balanced", Fraction(1)),
    ("near_critical", Fraction(3, 2)),
    ("first_critical", Fraction(2)),
    ("strong", Fraction(4)),
    ("undamped_boundary", Fraction(0)),
]
ASYMPTOTIC_MODES = [16, 32, 64]
mp.mp.dps = 60


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def dec(x: mp.mpf) -> str:
    if abs(x) < mp.mpf("1e-55"):
        return "0.0"
    return mp.nstr(x, 40, strip_zeros=False, min_fixed=-40, max_fixed=40)


def roots(b: mp.mpf, n: int) -> tuple[mp.mpc, mp.mpc, mp.mpf]:
    disc = b*b*n**4 - 4*n*n
    root = mp.sqrt(disc)
    return (-b*n*n + root)/2, (-b*n*n - root)/2, disc


def root_record(b: mp.mpf, n: int) -> dict:
    rp, rm, disc = roots(b, n)
    tol = mp.mpf("1e-45")
    if abs(disc) <= tol:
        regime = "critical"
    elif disc < 0:
        regime = "underdamped"
    else:
        regime = "overdamped"
    return {
        "n": n,
        "discriminant": dec(disc),
        "regime": regime,
        "lambda_plus": {"re": dec(mp.re(rp)), "im": dec(mp.im(rp))},
        "lambda_minus": {"re": dec(mp.re(rm)), "im": dec(mp.im(rm))},
        "slow_gap": dec(-mp.re(rp)),
    }


def build() -> dict:
    case_rows = []
    for case_id, bq in CASES:
        b = mp.mpf(bq.numerator) / bq.denominator
        modes = [root_record(b, n) for n in MODES]
        if b == 0:
            gap = None
            bstar = None
        else:
            gap = min(b/2, 1/b)
            bstar = mp.sqrt(2)
        asym = []
        for n in ASYMPTOTIC_MODES:
            rp, rm, _ = roots(b, n)
            asym.append({"n": n, "slow_minus_limit": dec(rp + 1/b) if b else None,
                         "fast_real": dec(mp.re(rm)) if b else None})
        case_rows.append({
            "case_id": case_id,
            "b": str(bq),
            "mode_count": len(modes),
            "modes": modes,
            "spectral_gap": None if gap is None else dec(gap),
            "optimizer": None if bstar is None else dec(bstar),
            "asymptotics": asym,
        })
    data = {
        "schema": "hcs-c218-kelvin-voigt-v1",
        "candidate_id": "HCS-C218",
        "evaluation_date": "2026-08-28",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "evaluator": {
            "path": "flow_systems/skills/route-a-evaluator.md",
            "version": "0.2.0",
            "sha256": EVALUATOR_SHA256,
        },
        "headline": "Dirichlet Kelvin--Voigt damping has an exact under/critical/over root atlas, non-eigenvalue essential accumulation at -1/b, and a uniquely optimized spectral-abscissa gap.",
        "frozen_object": {
            "system": "u_tt-u_xx-b u_txx=0 on (0,pi), u(0)=u(pi)=0",
            "clock": "physical continuous time t",
            "energy": "E=1/2 integral_0^pi (u_t^2+u_x^2) dx",
            "generator_domain": "A(u,v)=(v,(u+bv)_{xx}) on H_0^1 x L^2; D(A)={(u,v) in H_0^1(0,pi) x L^2(0,pi): v in H_0^1(0,pi), u+bv in H^2(0,pi) intersect H_0^1(0,pi)}",
            "mode_pencil": "q_n''+b n^2 q_n'+n^2 q_n=0",
            "parameters": "b>=0; b=0 is the separate unitary boundary",
            "forbidden_data": "target primes/zeros, local arithmetic, Euler factors, root numbers, automorphy, Hilbert-Polya operators",
        },
        "theorem": {
            "roots": "lambda_n,plusminus=(-b n^2 +/- sqrt(b^2 n^4-4 n^2))/2",
            "regimes": "bn<2 underdamped; bn=2 critical defective Jordan; bn>2 overdamped",
            "high_frequency": "lambda_n,plus -> -1/b from below and lambda_n,minus -> -infinity for b>0",
            "essential_point": "-1/b is an essential spectral accumulation point and is not an energy-space eigenvalue: A(u,v)=-(1/b)(u,v) forces b^(-2)u=0 in L^2 and then u=v=0",
            "essential_spectrum_definition": "essential means Weyl singular-sequence spectrum: with e_n=sqrt(2/pi) sin(nx), a_n=(n^2+|lambda_n,+|^2)^(-1/2), w_n=(a_n e_n, lambda_n,+ a_n e_n), one has ||w_n||_E=1, w_n weakly ->0, and ||(A+1/b)w_n||_E=|lambda_n,++1/b| ->0",
            "spectral_abscissa_gap": "gamma(b)=min(b/2,1/b) for b>0",
            "unique_optimizer": "b_star=sqrt(2), gamma_star=1/sqrt(2) on (0,pi)",
            "energy_identity": "E'(t)=-b integral_0^pi |u_tx|^2 dx <=0",
            "operator_boundary": "for t>0, e^(tA)w_n=e^(t lambda_n,+)w_n has norm -> exp(-t/b)>0, so the semigroup is not compact or Schatten; at t=0 it is the noncompact identity",
            "boundary": "b=0 has roots plus/minus i n and a unitary wave group; critical Jordan rates do not imply a uniform exact-rate norm bound",
        },
        "regression": {
            "cases": case_rows,
            "case_count": len(case_rows),
            "modes_per_case": len(MODES),
            "asymptotic_modes": ASYMPTOTIC_MODES,
            "working_decimal_digits": 60,
            "serialized_significant_digits": 40,
        },
        "exact_identities": [
            {"name": "quadratic_pencil", "formula": "lambda^2+b n^2 lambda+n^2=0"},
            {"name": "discriminant", "formula": "Delta_n=b^2 n^4-4n^2"},
            {"name": "slow_rationalization", "formula": "lambda_plus=-2 n^2/(b n^2+sqrt(Delta_n)) when Delta_n>0"},
            {"name": "gap_balance", "formula": "b/2=1/b iff b=sqrt(2)"},
            {"name": "energy", "formula": "E'=-b integral |u_tx|^2"},
            {"name": "critical_jordan", "formula": "Delta_n=0 iff bn=2 and the modal pencil has a double root"},
        ],
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "strongest_positive": "Mixed hyperbolic-parabolic spectral geometry and an exact globally optimized source-native gap.",
            "strongest_failure": "The mode index is a spatial sine label with no arithmetic primitive owner, target determinant, or self-adjoint target quantization.",
        },
        "scope_flags": {
            "uses_target_zero_table": False,
            "uses_prime_table": False,
            "claims_arithmetic_local_data": False,
            "claims_euler_factors": False,
            "claims_root_numbers": False,
            "claims_automorphy": False,
            "claims_target_divisor_or_functional_equation": False,
            "claims_hilbert_polya_operator": False,
            "invokes_route_b": False,
        },
        "citations": [
            {"key": "GuoWangZhang2010", "claim": "Kelvin--Voigt spectral and essential-spectrum context", "title": "Spectral analysis of a wave equation with Kelvin--Voigt damping", "authors": "B. Z. Guo, J. M. Wang, and G. D. Zhang", "venue": "ZAMM", "year": 2010, "doi": "10.1002/zamm.200900275"},
            {"key": "WangWang2014", "claim": "one-dimensional viscoelastic spectral stability context", "title": "Spectral analysis and exponential stability of one-dimensional wave equation with viscoelastic damping", "authors": "Jing Wang and Jun-Min Wang", "venue": "Journal of Mathematical Analysis and Applications", "year": 2014, "doi": "10.1016/j.jmaa.2013.08.034"},
            {"key": "CoxZuazua1994", "claim": "damped-string decay context", "title": "The rate at which energy decays in a damped string", "authors": "S. Cox and E. Zuazua", "venue": "Communications in Partial Differential Equations", "year": 1994, "doi": "10.1080/03605309408821015"},
            {"key": "FreitasLipovsky2019", "claim": "interval damped-wave determinant context only", "title": "Spectral determinant for the damped wave equation on an interval", "authors": "P. Freitas and J. Lipovský", "venue": "Acta Physica Polonica A", "year": 2019, "doi": "10.12693/APhysPolA.136.817"},
        ],
        "nonclaims": [
            "no assertion of a uniform operator-norm decay constant at a critical Jordan parameter",
            "no target prime/zero law, Euler factor, root number, automorphy, functional equation, or Hilbert-Polya operator",
            "no claim that the sine index is an arithmetic primitive owner",
            "no zeta determinant normalization beyond the displayed modal quadratic pencil",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path(os.environ.get("C218_OUTPUT", DEFAULT_OUTPUT)))
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(build(), sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(f"C218 producer: wrote {args.output}")


if __name__ == "__main__":
    main()
