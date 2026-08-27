#!/usr/bin/env python3
"""Produce the deterministic HCS-C206 Couette semigroup certificate."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

import mpmath as mp


SOURCE_COMMIT = "d108ef46fea7a8f62490a69071a83fcbda7c113b"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
DEFAULT_OUTPUT = Path(__file__).resolve().parents[1] / "results/c206_couette_evidence.json"
AS = [F(-2), F(-1, 2), F(0), F(1), F(3)]
NUS = [F(0), F(1, 7), F(2)]
KS = [F(-3), F(-1), F(0), F(1), F(2)]
TIMES = [F(0), F(1, 3), F(2)]
ETAS = [F(-5, 2), F(0), F(7, 3)]
WORKING_DECIMAL_DIGITS = 100
SERIALIZED_SIGNIFICANT_DIGITS = 82


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def mpq(q: F) -> mp.mpf:
    return mp.mpf(q.numerator) / q.denominator


def fmt(x: mp.mpf) -> str:
    return mp.nstr(x, SERIALIZED_SIGNIFICANT_DIGITS, strip_zeros=False)


def build() -> dict:
    mp.mp.dps = WORKING_DECIMAL_DIGITS
    rows = []
    for a in AS:
        for nu in NUS:
            for k in KS:
                for t in TIMES:
                    for eta in ETAS:
                        shift = eta + a * k * t
                        integral = eta * eta * t + a * k * eta * t * t + a * a * k * k * t**3 / 3
                        square = t * (eta + a * k * t / 2) ** 2 + a * a * k * k * t**3 / 12
                        dissipation = k * k * t + integral
                        sector_min = k * k * t + a * a * k * k * t**3 / 12
                        multiplier = mp.e ** (-mpq(nu * dissipation))
                        norm = mp.e ** (-mpq(nu * sector_min))
                        rows.append({
                            "case_id": f"a{a}_nu{nu}_k{k}_t{t}_eta{eta}",
                            "a": str(a), "nu": str(nu), "k": str(k), "t": str(t), "eta": str(eta),
                            "shift": str(shift),
                            "integrated_vertical_frequency": str(integral),
                            "completed_square": str(square),
                            "dissipation_exponent": str(dissipation),
                            "sector_minimum": str(sector_min),
                            "multiplier": fmt(multiplier),
                            "sector_norm": fmt(norm),
                        })

    compositions = []
    for a in [F(-2), F(0), F(3)]:
        for k in [F(-2), F(0), F(1)]:
            for eta in [F(-3, 2), F(2, 3)]:
                for t, s in [(F(0), F(2, 5)), (F(1, 3), F(4, 5)), (F(2), F(1, 7))]:
                    def d(time: F, freq: F) -> F:
                        return k*k*time + freq*freq*time + a*k*freq*time*time + a*a*k*k*time**3/F(3)
                    left = d(t, eta) + d(s, eta + a*k*t)
                    right = d(t+s, eta)
                    compositions.append({
                        "a": str(a), "k": str(k), "eta": str(eta), "t": str(t), "s": str(s),
                        "first_then_second": str(left), "combined": str(right),
                        "final_shift": str(eta+a*k*(t+s)),
                    })

    data = {
        "schema": "hcs-c206-couette-v1",
        "candidate_id": "HCS-C206",
        "evaluation_date": "2026-08-27",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "evaluator": {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256},
        "headline": "The Couette advection-diffusion semigroup has an exact all-parameter Fourier formula, sharp sector norm, and complete inviscid, diffusive, recurrence, and trace-class boundaries",
        "frozen_object": {
            "phase_space": "L2(T_x times R_y), with the streamwise torus of length 2pi",
            "equation": "partial_t f+a y partial_x f=nu(partial_x^2+partial_y^2)f",
            "parameters": "a in R, nu>=0, physical time t>=0",
            "fourier_convention": "f_hat_k(eta)=integral_T integral_R f(x,y) exp(-i(kx+eta y)) dy dx/(2pi)",
            "transformed_equation": "partial_t f_hat_k-a k partial_eta f_hat_k=-nu(k^2+eta^2)f_hat_k",
            "clock": "physical PDE time; no modular, orbit-counting, or fitted clock",
        },
        "theorem": {
            "semigroup": "S_t f_hat_k(eta)=exp(-nu[k^2 t+t(eta+a k t/2)^2+a^2 k^2 t^3/12]) f_hat_k(eta+a k t)",
            "sector_norm": "||S_t|| on the k-sector equals exp(-nu[k^2 t+a^2 k^2 t^3/12])",
            "sector_norm_attainment": "the norm value is exact and sharp; for nu*t>0 no nonzero L2 vector attains it because the unique maximizing frequency is a null set, while frequency-localized packets approach it; for nu*t=0 the evolution is unitary and every nonzero vector attains the norm",
            "composition": "D_t(eta)+D_s(eta+a k t)=D_(t+s)(eta), so S_t S_s=S_(t+s)",
            "enhanced_scale": "for a nonzero and nu>0, nonzero streamwise modes have the sharp cubic exponent and scale (nu a^2)^(-1/3), with ordinary nu^(-1) diffusion retained",
            "inviscid": "nu=0 is the unitary shear group f_k(y,t)=exp(-i a k t y)f_k(y,0); it mixes nonzero k weakly but has no L2 decay",
            "boundaries": "a=0 is ordinary heat, k=0 is one-dimensional heat, t=0 is the identity, and a=nu=0 is the identity group",
            "periodic_states": "if nu>0, S_T f=f in L2 for T>0 implies f=0; if nu=0 and a T is nonzero, the T-periodic states are exactly the streamwise means k=0",
            "trace_stop": "on T times R the semigroup is noncompact and not trace class: the k=0 heat multiplier has essential spectrum and translation witnesses; no ordinary Fredholm determinant is claimed",
            "reversal": "at nu=0, R(x,y)=(-x,y) reverses the same physical shear clock; positive viscosity is a contraction semigroup, not a unitary quantization",
        },
        "regression": {"fourier_cells": rows, "composition_cells": compositions},
        "summary": {
            "fourier_cells": len(rows), "composition_cells": len(compositions),
            "a_values": len(AS), "nu_values": len(NUS), "k_values": len(KS),
            "time_values": len(TIMES), "eta_values": len(ETAS),
            "working_decimal_digits": WORKING_DECIMAL_DIGITS,
            "serialized_significant_digits": SERIALIZED_SIGNIFICANT_DIGITS,
            "serialized_decimal_fields": 2 * len(rows),
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
            "strongest_positive": "The inviscid boundary is a source-native same-clock unitary Koopman shear with an exact viscous deformation.",
            "strongest_failure": "There is no intrinsic rational-prime primitive carrier, isolated periodic ledger, target determinant, or arithmetic analytic bridge.",
        },
        "scope_flags": {
            "uses_target_zero_table": False, "uses_prime_table": False,
            "claims_arithmetic_local_data": False, "claims_euler_factors": False,
            "claims_root_numbers": False, "claims_automorphy": False,
            "claims_target_divisor_or_functional_equation": False,
            "claims_hilbert_polya_operator": False, "invokes_route_b": False,
        },
        "citations": [{
            "key": "BMV2016", "claim": "Couette enhanced-dissipation and inviscid-damping context; not ownership of this package's elementary Fourier derivation",
            "doi": "10.1007/s00205-015-0917-3",
        }],
        "nonclaims": [
            "priority for Couette flow, Kelvin shear coordinates, inviscid damping, or enhanced dissipation",
            "nonlinear stability of Couette flow or a theorem on bounded-wall channels",
            "that finite Fourier regression proves the all-parameter theorem",
            "an ordinary trace or Fredholm determinant on the noncompact channel",
            "a prime-orbit law, arithmetic local datum, Euler factor, root number, automorphy, target divisor, or Hilbert--Polya operator",
            "external peer review, literature exhaustiveness, novelty certification, or an acceptance score",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "C206_PRODUCER_PASS", "fourier_cells": data["summary"]["fourier_cells"], "composition_cells": data["summary"]["composition_cells"], "payload_sha256": data["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
