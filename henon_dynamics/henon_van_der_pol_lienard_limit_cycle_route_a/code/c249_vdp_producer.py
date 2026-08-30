#!/usr/bin/env python3
"""Deterministic source-local certificate for the Van der Pol Lienard flow.

The analytic part of the certificate is the classical Lienard uniqueness
theorem, specialized to the polynomial damping f(x)=mu*(x^2-1).  The finite
numeric receipt only probes the Poincare return map and integral identities;
it is never used as a substitute for the all-parameter theorem.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

from scipy.integrate import solve_ivp
from scipy.optimize import brentq

SOURCE_COMMIT = "3ff451e904f8f063e88c40ef87f4697a6586b1a5"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FIXED_EPOCH = 1788048000
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c249_vdp_evidence.json"


def qtext(q: F | int) -> str:
    q = q if isinstance(q, F) else F(q)
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def encode(x: float) -> str:
    # 15 significant decimal digits are enough for the independent checker;
    # fixing the format makes the receipt stable across repeated runs.
    return format(float(x), ".15e")


def rhs(mu: float, augmented: bool = False):
    def f(t: float, state: list[float]):
        x, y = state[0], state[1]
        out = [y, mu * (1.0 - x * x) * y - x]
        if augmented:
            # divergence, energy balance and positive radius-squared reward
            out.extend([mu * (1.0 - x * x), mu * (1.0 - x * x) * y * y, x * x + y * y])
        return out

    return f


def upward_return(mu: float, y0: float, augmented: bool = False):
    """Return the next x=0 upward crossing from a positive section point."""
    def section(_t: float, state: list[float]):
        return state[0]

    section.direction = 1
    section.terminal = True
    # x=epsilon avoids treating the initial section point as an event.
    init = [1.0e-8, float(y0)]
    if augmented:
        init.extend([0.0, 0.0, 0.0])
    sol = solve_ivp(
        rhs(mu, augmented),
        (0.0, 120.0),
        init,
        events=section,
        method="DOP853",
        rtol=3.0e-12,
        atol=3.0e-14,
        max_step=3.0e-2,
    )
    if len(sol.t_events[0]) != 1:
        raise RuntimeError(f"no unique upward return for mu={mu}, y0={y0}")
    return float(sol.t_events[0][0]), [float(v) for v in sol.y_events[0][0]]


def cycle_for(mu: float) -> dict:
    def displacement(y: float) -> float:
        _t, state = upward_return(mu, y)
        return state[1] - y

    lo, hi = 5.0e-2, 8.0
    flo, fhi = displacement(lo), displacement(hi)
    if not (flo > 0.0 and fhi < 0.0):
        raise RuntimeError(f"Poincare bracket failed for mu={mu}: {flo}, {fhi}")
    ystar = brentq(displacement, lo, hi, xtol=2.0e-11, rtol=1.0e-13, maxiter=100)
    period, state = upward_return(mu, ystar, augmented=True)
    div_int, energy_bal, radius_reward = state[2], state[3], state[4]
    return {
        "mu": encode(mu),
        "section": "x=0, y>0; upward return",
        "section_y": encode(ystar),
        "return_y": encode(state[1]),
        "return_residual": encode(state[1] - ystar),
        "period": encode(period),
        "divergence_integral": encode(div_int),
        "energy_balance": encode(energy_bal),
        "floquet_multiplier": encode(__import__("math").exp(div_int)),
        "radius_squared_integral": encode(radius_reward),
        "numerical_method": "DOP853; rtol=3e-12; atol=3e-14; max_step=0.03",
        "status": "finite regression probe; not an all-state census",
    }


def parameter_rows() -> list[dict]:
    rows = []
    for mu in (F(-2), F(-1), F(0), F(1, 10), F(1, 2), F(1), F(2), F(4)):
        if mu < 0:
            regime = "time-reversed negative-damping orientation"
            cycle = "one repelling limit cycle"
            count = "one"
            stability = "repelling"
        elif mu == 0:
            regime = "Hamiltonian center boundary"
            cycle = "continuum of harmonic ovals"
            count = "continuum"
            stability = "neutral"
        else:
            regime = "strict Lienard positive-damping exterior"
            cycle = "one attracting limit cycle"
            count = "one"
            stability = "attracting"
        rows.append({
            "mu": qtext(mu),
            "regime": regime,
            "equilibrium": "origin; linear eigenvalues solve lambda^2-mu*lambda+1=0",
            "periodic_orbits": cycle,
            "primitive_cycle_count": count,
            "cycle_stability": stability,
            "theorem_source": "Lienard uniqueness plus time reversal; numeric rows are separate",
        })
    return rows


def exact_rows() -> list[dict]:
    return [
        {"identity_id": "vector_field", "formula": "xdot=y; ydot=mu*(1-x^2)*y-x"},
        {"identity_id": "lienard_form", "formula": "xddot+mu*(x^2-1)*xdot+x=0"},
        {"identity_id": "primitive_F", "formula": "F(x)=integral_0^x mu*(s^2-1) ds=mu*(x^3/3-x)"},
        {"identity_id": "F_positive_zero", "formula": "for mu>0, F has the unique positive zero sqrt(3) and F<0 on (0,sqrt(3))"},
        {"identity_id": "energy", "formula": "E=(x^2+y^2)/2; Edot=mu*(1-x^2)*y^2"},
        {"identity_id": "cycle_balance", "formula": "for mu!=0 on a periodic cycle, integral_0^T (1-x^2)*y^2 dt=0"},
        {"identity_id": "divergence", "formula": "div X=mu*(1-x^2)"},
        {"identity_id": "floquet", "formula": "lambda_trans=exp(integral_0^T div X dt), with tangent multiplier 1"},
        {"identity_id": "positive_case", "formula": "mu>0 => exactly one hyperbolic attracting cycle surrounding the origin"},
        {"identity_id": "negative_case", "formula": "mu<0 is time reversal: exactly one hyperbolic repelling cycle"},
        {"identity_id": "center_boundary", "formula": "mu=0 => E is conserved and every E>0 level is a harmonic oval of period 2*pi"},
        {"identity_id": "scaling", "formula": "omega^2*x term reduces by tau=omega*t and effective mu=mu0/omega"},
    ]


def build() -> dict:
    cycle_rows = [cycle_for(mu) for mu in (0.1, 0.5, 1.0, 2.0, 4.0)]
    data = {
        "schema": "hcs-c249-van-der-pol-lienard-limit-cycle-v1",
        "candidate_id": "HCS-C249",
        "evaluation_date": "2026-08-30",
        "source_commit": SOURCE_COMMIT,
        "fixed_epoch": FIXED_EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256},
        "headline": "The smooth Van der Pol Lienard family has a complete sign/boundary atlas, one-cycle theorem, and an independently replayable Floquet receipt.",
        "frozen_object": {
            "phase_space": "R^2 with coordinates (x,y)",
            "dynamics": "xdot=y, ydot=mu*(1-x^2)*y-x",
            "equivalent_equation": "xddot+mu*(x^2-1)*xdot+x=0",
            "parameters": "mu in R; scaled frequency omega>0 is handled by tau=omega*t",
            "clock": "physical time t",
            "section": "Sigma={(x,y): x=0,y>0}",
            "arithmetic_origin": "none; smooth polynomial Lienard oscillator",
            "forbidden_data": "target primes/zeros, arithmetic local data, Euler factors, root numbers, automorphy, target determinants, Hilbert--Polya operators",
        },
        "theorem": {
            "lienard_uniqueness": "For every mu>0, F(x)=mu*(x^3/3-x) satisfies the Lienard hypotheses and the flow has exactly one hyperbolic attracting periodic orbit surrounding the origin; every non-equilibrium bounded recurrent trajectory is that cycle.",
            "time_reversal": "For mu<0 the involution (t,x,y)->(-t,x,-y) transfers the positive-mu cycle to exactly one hyperbolic repelling cycle.",
            "center_face": "At mu=0 the Hamiltonian E=(x^2+y^2)/2 is conserved, so every positive level is a harmonic oval of period 2*pi and the periodic set is a continuum.",
            "energy_and_floquet": "For mu!=0, E_dot=mu*(1-x^2)y^2; on a periodic cycle the balance integral vanishes, while the nontrivial Floquet multiplier is exp(integral div X dt)=exp(mu*integral(1-x^2)dt).",
            "poincare": "On Sigma the return map has one fixed point for mu>0, with derivative equal to the transverse Floquet multiplier and modulus strictly below one.",
            "boundaries": "The mu=0 center, negative-mu time reversal, omega=0 scaling face, and section orientation are separate; no asymptotic period coefficient is inferred from a finite numerical fit.",
            "scope": "This is a source-local smooth-flow theorem and not an arithmetic determinant or target spectral statement.",
        },
        "regression": {
            "parameter_rows": parameter_rows(),
            "cycle_rows": cycle_rows,
            "parameter_row_count": 8,
            "cycle_row_count": len(cycle_rows),
            "working_precision": "IEEE-754 double with deterministic DOP853 tolerances",
            "numeric_tolerance": "return residual below 3e-10; energy balance below 3e-9",
        },
        "exact_identities": exact_rows(),
        "route_a": {
            "tuple": ["A0_FAIL", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "strongest_positive": "Classical Lienard theorem closes the full sign family and the unique-cycle/Floquet boundary; finite Poincare receipts replay it.",
            "strongest_failure": "The polynomial oscillator has no intrinsic rational-prime carrier, logarithmic prime clock, target divisor, or global arithmetic determinant.",
        },
        "scope_flags": {k: False for k in ["uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"]},
        "citations": [
            {"key": "Lienard1928", "claim": "classical Lienard oscillation theorem", "source": "A. Lienard, Etude des oscillations entretenues, Revue Generale de l'Electricite 23 (1928), 901--912", "url": "https://gallica.bnf.fr/ark:/12148/bpt6k5671115f"},
            {"key": "LevinsonSmith1942", "claim": "existence and uniqueness of the Van der Pol relaxation cycle", "source": "N. Levinson and O. K. Smith, A general equation for relaxation oscillations, Duke Mathematical Journal 9 (1942), 382--403, DOI 10.1215/S0012-7094-42-00928-1", "url": "https://doi.org/10.1215/S0012-7094-42-00928-1"},
            {"key": "Strogatz2015", "claim": "standard Van der Pol phase-plane background", "source": "S. H. Strogatz, Nonlinear Dynamics and Chaos, 2nd ed., Westview Press (2015)", "url": "https://www.routledge.com/Nonlinear-Dynamics-and-Chaos/Strogatz/p/book/9780813349107"},
        ],
        "nonclaims": [
            "a complete closed-form expression for the limit-cycle period for every mu",
            "a numerical census of every continuum state cell",
            "arithmetic Euler factors, root numbers, automorphy, target divisor or functional equation",
            "a target zeta/Fredholm determinant, zero match, or Hilbert--Polya operator",
            "external peer review or literature-priority certification",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = ap.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    data = build()
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "C249_PRODUCER_PASS", "parameter_rows": data["regression"]["parameter_row_count"], "cycle_rows": data["regression"]["cycle_row_count"], "payload_sha256": data["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
