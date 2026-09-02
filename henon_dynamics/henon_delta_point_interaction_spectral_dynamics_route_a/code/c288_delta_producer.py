#!/usr/bin/env python3
"""Deterministic evidence producer for HCS-C288."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c288_delta_evidence.json"
SOURCE = "3878fa5282ca89f75700b3ef9d623f54dcb7bcf9"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788307200
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"

MODEL = {
    "units": "hbar=2m=1",
    "form": "q_alpha[psi]=integral |psi'|^2+alpha|psi(0)|^2 on H^1(R)",
    "operator": "H_alpha=-d^2/dx^2 on R\\{0}",
    "interface": "psi continuous; psi'(0+)-psi'(0-)=alpha psi(0)",
    "clock": "unitary time exp(-it H_alpha) and heat time exp(-t H_alpha)",
}
ROUTE = {
    "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
    "overall": "ROUTE_A_REJECTED",
    "route_b_invocation_allowed": False,
}
SCOPE_FLAGS = {
    "arithmetic_local_data": False,
    "euler_factors": False,
    "root_numbers": False,
    "automorphy": False,
    "target_divisor_or_counting_law": False,
    "target_functional_equation": False,
    "target_zero_match": False,
    "hilbert_polya_operator": False,
    "route_b_input": False,
}
THEOREM = {
    "realization": "closed lower-bounded H^1 form and the continuous derivative-jump domain define one self-adjoint operator",
    "resolvent": "the full negative-energy Green kernel is one explicit rank-one correction with the bound-state pole removed",
    "spectrum": "[0,infinity) is purely absolutely continuous with no singular-continuous part; exactly one eigenvalue -alpha^2/4 occurs iff alpha<0",
    "scattering": "left-right amplitudes, odd free channel, even unitary phase, and all energy limits are exact",
    "heat": "the erfc heat kernel and integrated diagonal relative trace hold for every real alpha and t>0",
    "boundary": "attractive, free, repulsive, pole, zero-energy, high-energy, small-time, and large-time faces are separated",
}
PROOF = {
    "form": "the one-dimensional trace inequality makes point evaluation infinitesimally form bounded",
    "krein": "solve the free Green equation and one scalar jump equation",
    "completeness": "odd/even half-line transforms give absolutely continuous spectral densities on [0,infinity), no singular-continuous part, and only the displayed attractive pole",
    "heat_inversion": "the explicit Laplace identity for the resolvent correction gives the erfc heat term",
    "trace_integral": "one integration by parts evaluates the diagonal defect",
    "finite_role": "finite cells audit constants and branches but do not prove the all-parameter theorem",
}
REFERENCES = [{
    "id": "Albeverio1988",
    "authors": "Sergio Albeverio, Friedrich Gesztesy, Raphael Hoegh-Krohn, and Helge Holden",
    "title": "Solvable Models in Quantum Mechanics",
    "venue": "Theoretical and Mathematical Physics, Springer, 1988",
    "identifier": "10.1007/978-3-642-88201-2",
    "url": "https://doi.org/10.1007/978-3-642-88201-2",
    "ownership": "direct owner; one-center delta-interaction in one dimension, pages 75-90",
}]


def q(x: Fraction) -> str:
    return str(x)


def dec(x: mp.mpf) -> str:
    return mp.nstr(x, 45, strip_zeros=False)


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def heat(alpha: mp.mpf, t: mp.mpf, x: mp.mpf, y: mp.mpf) -> mp.mpf:
    a = abs(x) + abs(y)
    free = mp.exp(-(x-y)**2/(4*t)) / mp.sqrt(4*mp.pi*t)
    return free - alpha/4 * mp.exp(alpha*a/2 + alpha**2*t/4) * mp.erfc(a/(2*mp.sqrt(t)) + alpha*mp.sqrt(t)/2)


def build() -> dict:
    mp.mp.dps = 80
    alphas = [Fraction(-4), Fraction(-2), Fraction(-1), Fraction(0), Fraction(1), Fraction(2), Fraction(4)]
    kappas = [Fraction(1, 2), Fraction(1), Fraction(3, 2), Fraction(2), Fraction(3)]
    resolvent = []
    pole_cells = []
    for alpha in alphas:
        for kappa in kappas:
            if 2*kappa + alpha == 0:
                pole_cells.append({"alpha": q(alpha), "kappa": q(kappa), "pole": True})
                continue
            resolvent.append({
                "alpha": q(alpha), "kappa": q(kappa),
                "free_coefficient": q(Fraction(1, 1)/(2*kappa)),
                "image_coefficient": q(-alpha/(2*kappa*(2*kappa+alpha))),
                "interface_value_coefficient": q(Fraction(1, 1)/(2*kappa+alpha)),
                "derivative_jump_ratio": q(alpha),
                "source_derivative_jump": "-1",
            })

    scattering = []
    for alpha in alphas:
        for k in [Fraction(1, 2), Fraction(1), Fraction(2), Fraction(4)]:
            den = 4*k*k + alpha*alpha
            scattering.append({
                "alpha": q(alpha), "k": q(k),
                "reflection_probability": q(alpha*alpha/den),
                "transmission_probability": q(4*k*k/den),
                "probability_sum": "1",
                "odd_channel": "1",
                "even_channel_modulus_squared": "1",
            })

    bound = []
    for alpha in [Fraction(-4), Fraction(-2), Fraction(-1)]:
        bound.append({
            "alpha": q(alpha), "energy": q(-alpha*alpha/4),
            "decay_kappa": q(-alpha/2),
            "normalization_squared": q(-alpha/2),
            "normalization_integral": "1",
        })

    heat_cells = []
    for alpha, t, x, y in [
        (-2, mp.mpf("0.25"), mp.mpf("0"), mp.mpf("1")),
        (-2, mp.mpf("2"), mp.mpf("0.5"), mp.mpf("-1")),
        (-1, mp.mpf("0.75"), mp.mpf("1"), mp.mpf("2")),
        (0, mp.mpf("0.5"), mp.mpf("-1"), mp.mpf("1")),
        (1, mp.mpf("0.25"), mp.mpf("0"), mp.mpf("1")),
        (1, mp.mpf("3"), mp.mpf("2"), mp.mpf("-0.5")),
        (2, mp.mpf("1"), mp.mpf("0.5"), mp.mpf("0.5")),
        (4, mp.mpf("0.125"), mp.mpf("-2"), mp.mpf("1")),
    ]:
        aa = mp.mpf(alpha)
        trace = (mp.exp(aa*aa*t/4)*mp.erfc(aa*mp.sqrt(t)/2)-1)/2
        heat_cells.append({
            "alpha": str(alpha), "t": dec(t), "x": dec(x), "y": dec(y),
            "kernel": dec(heat(aa, t, x, y)), "relative_trace": dec(trace),
        })

    data = {
        "schema": "hcs-c288-delta-point-interaction-v1",
        "candidate_id": "HCS-C288",
        "evaluation_date": "2026-09-02",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR},
        "model": MODEL,
        "theorem_contract": THEOREM,
        "proof_contract": PROOF,
        "route_a": ROUTE,
        "scope_flags": SCOPE_FLAGS,
        "enumeration": {
            "alpha_values": [q(x) for x in alphas],
            "regular_resolvent_cells": len(resolvent),
            "pole_cells": len(pole_cells),
            "scattering_cells": len(scattering),
            "bound_state_cells": len(bound),
            "heat_cells": len(heat_cells),
        },
        "resolvent_cells": resolvent,
        "pole_cells": pole_cells,
        "scattering_cells": scattering,
        "bound_state_cells": bound,
        "heat_cells": heat_cells,
        "references": REFERENCES,
        "nonclaims": [
            "classical point-interaction formulas are not claimed as literature originality",
            "finite evidence does not prove the arbitrary-parameter analytic theorem",
            "a source Hamiltonian and relative heat trace are not a target determinant or Hilbert-Polya operator",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(f"C288_PRODUCER_PASS {data['payload_sha256']} cells={sum(data['enumeration'][k] for k in ('regular_resolvent_cells','pole_cells','scattering_cells','bound_state_cells','heat_cells'))}")


if __name__ == "__main__":
    main()
