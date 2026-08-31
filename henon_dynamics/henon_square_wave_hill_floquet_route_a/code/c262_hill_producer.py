#!/usr/bin/env python3
"""Deterministic high-precision transfer evidence for the C262 Hill atlas."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

import mpmath as mp

SOURCE_COMMIT = "98782afe1e754c311ad0736f72ce09dcc7c85c77"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FIXED_EPOCH = 1788048000
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c262_hill_evidence.json"
mp.mp.dps = 90


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def qtext(q: F | int) -> str:
    q = q if isinstance(q, F) else F(q)
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def mpq(q: F | int) -> mp.mpf:
    q = q if isinstance(q, F) else F(q)
    return mp.mpf(q.numerator) / q.denominator


def dec(x: mp.mpf) -> str:
    return mp.nstr(x, 70, strip_zeros=False)


def segment(k: mp.mpf, tau: mp.mpf) -> list[list[mp.mpf]]:
    if k > 0:
        root = mp.sqrt(k)
        C, S = mp.cos(root*tau), mp.sin(root*tau)/root
    elif k < 0:
        root = mp.sqrt(-k)
        C, S = mp.cosh(root*tau), mp.sinh(root*tau)/root
    else:
        C, S = mp.mpf(1), tau
    return [[C, S], [-k*S, C]]


def mul(a: list[list[mp.mpf]], b: list[list[mp.mpf]]) -> list[list[mp.mpf]]:
    return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def sub(a: list[list[mp.mpf]], b: list[list[mp.mpf]]) -> list[list[mp.mpf]]:
    return [[a[i][j]-b[i][j] for j in range(2)] for i in range(2)]


def scale(c: mp.mpf, a: list[list[mp.mpf]]) -> list[list[mp.mpf]]:
    return [[c*a[i][j] for j in range(2)] for i in range(2)]


def norm(a: list[list[mp.mpf]]) -> mp.mpf:
    return max(abs(a[i][j]) for i in range(2) for j in range(2))


I2 = [[mp.mpf(1), mp.mpf(0)], [mp.mpf(0), mp.mpf(1)]]


def chebyshev_u(n: int, x: mp.mpf) -> mp.mpf:
    if n == -1:
        return mp.mpf(0)
    if n == 0:
        return mp.mpf(1)
    prev, curr = mp.mpf(1), 2*x
    for _ in range(1, n):
        prev, curr = curr, 2*x*curr-prev
    return curr


def classify(M: list[list[mp.mpf]]) -> str:
    delta = M[0][0] + M[1][1]
    tol = mp.mpf("1e-65")
    if abs(delta-2) < tol:
        return "parabolic_identity_plus" if norm(sub(M, I2)) < tol else "parabolic_jordan_plus"
    if abs(delta+2) < tol:
        return "parabolic_identity_minus" if norm(sub(M, scale(-1, I2))) < tol else "parabolic_jordan_minus"
    if abs(delta) < 2:
        return "elliptic_bounded"
    return "hyperbolic_exponential"


def grid_row(idx: int, k1q: F, k2q: F, t1q: F, t2q: F) -> dict:
    k1, k2, t1, t2 = map(mpq, (k1q, k2q, t1q, t2q))
    M1, M2 = segment(k1, t1), segment(k2, t2)
    M = mul(M2, M1)
    delta = M[0][0]+M[1][1]
    determinant = M[0][0]*M[1][1]-M[0][1]*M[1][0]
    closed_delta = 2*M1[0][0]*M2[0][0]-(k1+k2)*M1[0][1]*M2[0][1]
    power = I2
    max_cheb = mp.mpf(0)
    for n in range(1, 13):
        power = mul(power, M)
        formula = sub(scale(chebyshev_u(n-1, delta/2), M), scale(chebyshev_u(n-2, delta/2), I2))
        max_cheb = max(max_cheb, norm(sub(power, formula)))
    if abs(delta) > 2:
        exponent = mp.acosh(abs(delta)/2)/(t1+t2) if t1+t2 else mp.inf
        floquet = dec(exponent)
    elif abs(delta) < 2:
        angle = mp.acos(delta/2)/(t1+t2) if t1+t2 else mp.mpf(0)
        floquet = dec(angle)
    else:
        floquet = "0"
    return {
        "row_id": f"G{idx:04d}", "k1": qtext(k1q), "k2": qtext(k2q),
        "tau1": qtext(t1q), "tau2": qtext(t2q),
        "monodromy": [[dec(value) for value in row] for row in M],
        "discriminant": dec(delta), "closed_discriminant": dec(closed_delta),
        "determinant_residual": dec(abs(determinant-1)),
        "class": classify(M), "floquet_angle_or_growth_per_time": floquet,
        "max_chebyshev_power_residual_n1_to_12": dec(max_cheb),
    }


def boundary_rows() -> list[dict]:
    # Exact matrices are supplied independently of the numerical grid.
    return [
        {"row_id": "B1", "parameters": "k1=k2=1,tau1=tau2=pi", "matrix": [["1", "0"], ["0", "1"]], "delta": "2", "class": "parabolic_identity_plus", "growth": "bounded; every solution periodic"},
        {"row_id": "B2", "parameters": "k1=k2=1,tau1=tau2=pi/2", "matrix": [["-1", "0"], ["0", "-1"]], "delta": "-2", "class": "parabolic_identity_minus", "growth": "bounded; every solution antiperiodic over one coefficient period"},
        {"row_id": "B3", "parameters": "k1=0,tau1=1,tau2=0", "matrix": [["1", "1"], ["0", "1"]], "delta": "2", "class": "parabolic_jordan_plus", "growth": "generic linear; one fixed line"},
        {"row_id": "B4", "parameters": "k1=1,tau1=pi;k2=0,tau2=1", "matrix": [["-1", "-1"], ["0", "-1"]], "delta": "-2", "class": "parabolic_jordan_minus", "growth": "generic linear with alternating sign; one antiperiodic line"},
        {"row_id": "B5", "parameters": "tau1=tau2=0", "matrix": [["1", "0"], ["0", "1"]], "delta": "2", "class": "parabolic_identity_plus", "growth": "zero-time identity face"},
        {"row_id": "B6", "parameters": "k1=-1,tau1=log(2),tau2=0", "matrix": [["5/4", "3/4"], ["3/4", "5/4"]], "delta": "5/2", "class": "hyperbolic_exponential", "growth": "multipliers 2 and 1/2"},
    ]


def build() -> dict:
    ks = [F(-4), F(-1), F(0), F(1), F(4), F(9)]
    taus = [F(0), F(1, 4), F(1, 2), F(1), F(3, 2)]
    grid = []
    for k1 in ks:
        for k2 in ks:
            for t1 in taus:
                for t2 in taus:
                    grid.append(grid_row(len(grid)+1, k1, k2, t1, t2))
    classes: dict[str, int] = {}
    for row in grid:
        classes[row["class"]] = classes.get(row["class"], 0)+1
    data = {
        "schema": "hcs-c262-square-wave-hill-floquet-v1",
        "candidate_id": "HCS-C262", "evaluation_date": "2026-08-31",
        "source_commit": SOURCE_COMMIT, "fixed_epoch": FIXED_EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256},
        "headline": "The two-step square-wave Hill oscillator has an exact all-sign monodromy, discriminant, Floquet--Jordan stability atlas, and Chebyshev iterate law.",
        "frozen_object": {
            "equation": "y''+k(t)*y=0 with periodic k1 for tau1 then k2 for tau2",
            "parameters": "real k1,k2 and nonnegative tau1,tau2, with positive total period for the dynamical theorem",
            "phase_space": "R^2 state (y,y') with real symplectic transfer matrices",
            "clock": "physical time and the coefficient-period strobe",
            "arithmetic_origin": "none; coefficients and durations vary continuously",
            "determinant_convention": "source SL(2,R) characteristic polynomial only; no target determinant",
            "forbidden_data": "target primes/zeros, arithmetic local data, Euler factors, root numbers, automorphy, target divisors, Hilbert--Polya operators",
        },
        "theorem": {
            "entire_segments": "C(k,t)=sum_m (-k)^m*t^(2m)/(2m)! and S(k,t)=sum_m (-k)^m*t^(2m+1)/(2m+1)! satisfy C^2+k*S^2=1.",
            "monodromy": "Phi(k,t)=[[C,S],[-k*S,C]] and M=Phi(k2,tau2)*Phi(k1,tau1) lies in SL(2,R).",
            "discriminant": "Delta=tr(M)=2*C1*C2-(k1+k2)*S1*S2.",
            "floquet_classification": "For positive total period: abs(Delta)<2 iff all solutions are bounded; abs(Delta)>2 gives a hyperbolic multiplier pair and generic exponential growth.",
            "parabolic_boundary": "At Delta=+/-2, M=+/-I gives bounded periodic/antiperiodic solutions, while a nontrivial Jordan matrix gives one bounded Floquet line and generic linear growth.",
            "iterate_law": "M^n=U_{n-1}(Delta/2)*M-U_{n-2}(Delta/2)*I for every n>=1, with U_{-1}=0 and U_0=1.",
            "floquet_rates": "Elliptic angle is arccos(Delta/2)/T; hyperbolic growth rate is arcosh(abs(Delta)/2)/T.",
            "faces": "The same entire formulas include positive, zero, and negative k_j, zero-duration faces, constant-coefficient collapse, and swapped segment order; the trace is order-invariant although M need not be.",
        },
        "receipts": {
            "grid_rows": grid, "grid_row_count": len(grid),
            "k_grid": [qtext(x) for x in ks], "tau_grid": [qtext(x) for x in taus],
            "class_counts": classes,
            "boundary_rows": boundary_rows(), "boundary_row_count": 6,
            "working_decimal_digits": 90, "printed_significant_digits": 70,
            "chebyshev_power_max": 12,
            "finite_receipt_boundary": "The 900 grid rows and six exact boundary witnesses test formulas; the continuum Floquet--Jordan classification is proof-driven.",
        },
        "exact_identities": [
            {"id": "segment_identity", "formula": "C(k,t)^2+k*S(k,t)^2=1"},
            {"id": "segment_matrix", "formula": "Phi(k,t)=[[C,S],[-k*S,C]]"},
            {"id": "determinant", "formula": "det(Phi)=det(M)=1"},
            {"id": "discriminant", "formula": "Delta=2*C1*C2-(k1+k2)*S1*S2"},
            {"id": "characteristic", "formula": "M^2-Delta*M+I=0"},
            {"id": "chebyshev", "formula": "M^n=U_{n-1}(Delta/2)*M-U_{n-2}(Delta/2)*I; U_{-1}=0,U_0=1"},
            {"id": "parabolic_split", "formula": "Delta=+/-2 requires testing M=+/-I versus rank(M-/+I)=1"},
            {"id": "order_trace", "formula": "tr(Phi2*Phi1)=tr(Phi1*Phi2)"},
        ],
        "route_a": {
            "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
            "strongest_positive": "An exact SL(2,R) monodromy closes every stability region, multiplier, iterate, and Jordan boundary for the two-step family.",
            "strongest_failure": "There is no intrinsic arithmetic origin, rational-prime orbit carrier, target determinant, or target global analytic structure.",
        },
        "scope_flags": {k: False for k in ["uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"]},
        "citations": [
            {"key": "Hill1886", "claim": "periodic-coefficient oscillator and stability context", "source": "G. W. Hill, Acta Mathematica 8 (1886), 1--36", "url": "https://doi.org/10.1007/BF02417081"},
            {"key": "Golubev1997", "claim": "piecewise-constant monodromy and two-step resonance context", "source": "Y. F. Golubev, Keldysh Institute Preprint 43 (1997)", "url": "https://www.mathnet.ru/eng/ipmp1431"},
        ],
        "nonclaims": [
            "a classification of arbitrary periodic Hill coefficients",
            "that Delta=+/-2 always makes every solution periodic or antiperiodic",
            "that every hyperbolic initial condition grows forward in time",
            "nonlinear stability of a perturbed oscillator",
            "an arithmetic Euler product, target divisor, functional equation, or Hilbert--Polya operator",
            "Route-B input or literature priority for classical Floquet theory",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    data = build()
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps({"status": "C262_PRODUCER_PASS", "grid_rows": data["receipts"]["grid_row_count"], "boundary_rows": 6, "class_counts": data["receipts"]["class_counts"], "payload_sha256": data["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
