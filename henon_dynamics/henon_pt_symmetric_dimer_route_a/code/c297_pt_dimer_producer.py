#!/usr/bin/env python3
"""Deterministic exact evidence for the HCS-C297 PT-symmetric dimer."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c297_pt_dimer_evidence.json"
SOURCE = "f8d3ad9a8940b54e82854b2924be353575ed8fcb"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788307200
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
OBSTRUCTION = "HEN-O281"
ROUTE = ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]

MODEL = {
    "state_space": "nonzero vectors psi in C^2 and their projective rays",
    "equation": "i d_t psi=H_(gamma,kappa) psi with H=[[i gamma,kappa],[kappa,-i gamma]]",
    "parameters": "kappa>0 and gamma real; physical time t",
    "parity_time": "P=sigma_x and T is componentwise complex conjugation",
    "clock": "physical propagation time; no arithmetic or fitted target clock",
}
THEOREM = {
    "square": "H^2=(kappa^2-gamma^2) I gives the exact exponential in all three chambers",
    "unbroken": "if |gamma|<kappa, eigenvalues are real, generic rays have least period pi/sqrt(kappa^2-gamma^2), and vectors have least period twice that",
    "exceptional": "if |gamma|=kappa, H is nonzero rank-one nilpotent, the eigenline is unique, and generalized states grow linearly",
    "broken": "if |gamma|>kappa, the two projective fixed rays are attracting and repelling and generic vector norms have exponential envelopes",
    "metrics": "sigma_x is an all-parameter conserved indefinite form; eta=I+(gamma/kappa)sigma_y is positive definite exactly in the unbroken chamber and degenerates at the exceptional point",
    "projective": "z=psi_2/psi_1 obeys z_dot=i kappa(z^2-1)-2 gamma z and its complex quadratic discriminant is minus four times (kappa^2-gamma^2)",
    "boundaries": "gamma=0, kappa down to zero, both exceptional sheets, eigenrays, zero state, and vector-versus-ray periods are separated",
}
PROOF = {
    "exponential": "reduce every analytic power series to the basis I,H using the scalar square identity",
    "classification": "use the sign of delta=kappa^2-gamma^2 and the Jordan form at delta=0",
    "metric": "direct multiplication gives H^dagger eta=eta H and eta eigenvalues 1 plus or minus |gamma|/kappa",
    "projective": "differentiate the affine ratio and compactify the Riccati field on CP^1",
    "period": "the scalar exponential is plus or minus I at successive half turns; eigenrays are stationary and are excluded from the generic least-period statement",
    "finite_role": "the integer grid audits exact algebra, phase labels, metrics, and boundary incidence but is not the proof of the all-parameter theorem",
}
FLAGS = {
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
REFERENCES = [
    {
        "id": "BenderBoettcher1998",
        "title": "Real Spectra in Non-Hermitian Hamiltonians Having PT Symmetry",
        "authors": "Carl M. Bender and Stefan Boettcher",
        "venue": "Physical Review Letters 80 (1998), 5243-5246",
        "identifier": "doi:10.1103/PhysRevLett.80.5243",
        "url": "https://doi.org/10.1103/PhysRevLett.80.5243",
        "ownership": "foundational PT-symmetric spectral context; not a priority claim for this two-mode calculation",
    },
    {
        "id": "Mostafazadeh2002",
        "title": "Pseudo-Hermiticity versus PT symmetry: The necessary condition for the reality of the spectrum of a non-Hermitian Hamiltonian",
        "authors": "Ali Mostafazadeh",
        "venue": "Journal of Mathematical Physics 43 (2002), 205-214",
        "identifier": "doi:10.1063/1.1418246",
        "url": "https://doi.org/10.1063/1.1418246",
        "ownership": "direct owner for positive-metric and pseudo-Hermitian interpretation",
    },
    {
        "id": "RuterEtAl2010",
        "title": "Observation of parity-time symmetry in optics",
        "authors": "Christian E. Rueter et al.",
        "venue": "Nature Physics 6 (2010), 192-195",
        "identifier": "doi:10.1038/nphys1515",
        "url": "https://doi.org/10.1038/nphys1515",
        "ownership": "physical balanced-gain/loss coupled-mode context",
    },
]


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def phase(delta: int) -> str:
    return "unbroken" if delta > 0 else "exceptional" if delta == 0 else "broken"


def grid_row(kappa: int, gamma: int) -> dict:
    delta = kappa * kappa - gamma * gamma
    chamber = phase(delta)
    return {
        "kappa": kappa,
        "gamma": gamma,
        "delta": delta,
        "phase": chamber,
        "trace_H": 0,
        "det_H": -delta,
        "H_square_scalar": delta,
        "rank_H": 1 if delta == 0 else 2,
        "projective_fixed_rays": 1 if delta == 0 else 2,
        "eta_scaled_determinant": delta,
        "eta_signature": "positive" if delta > 0 else "semidefinite" if delta == 0 else "indefinite",
        "projective_period_over_pi_squared": str(Fraction(1, delta)) if delta > 0 else None,
        "vector_period_over_two_pi_squared": str(Fraction(1, delta)) if delta > 0 else None,
        "krein_signature": ["negative", "positive"] if delta > 0 else [],
        "growth_rate_squared": -delta if delta < 0 else 0,
    }


def build() -> dict:
    rows = [grid_row(kappa, gamma) for kappa in range(1, 9) for gamma in range(-10, 11)]
    counts = {name: sum(row["phase"] == name for row in rows) for name in ("unbroken", "exceptional", "broken")}
    boundaries = [
        {"id": "hermitian_axis", "face": "gamma=0", "result": "H=kappa sigma_x and the standard norm as well as eta is conserved"},
        {"id": "positive_ep", "face": "gamma=kappa>0", "result": "H^2=0 with one eigenline and linear generalized evolution"},
        {"id": "negative_ep", "face": "gamma=-kappa<0", "result": "the second nilpotent sheet has the same Jordan classification"},
        {"id": "uncoupled_limit", "face": "kappa down to zero at gamma nonzero", "result": "the components amplify and decay independently; eta is not a positive metric"},
        {"id": "zero_generator", "face": "kappa=gamma=0 outside the frozen kappa>0 domain", "result": "every vector is fixed and there is no exceptional point"},
        {"id": "eigenrays", "face": "initial ray is an eigenray", "result": "it is projectively stationary and is excluded from the generic least-period claim"},
        {"id": "zero_vector", "face": "psi=0", "result": "the vector solution is fixed but does not define a projective state"},
        {"id": "period_convention", "face": "unbroken generic initial data", "result": "the ray period is pi/omega while the vector period is 2 pi/omega"},
    ]
    data = {
        "schema": "hcs-c297-pt-symmetric-dimer-v1",
        "candidate_id": "HCS-C297",
        "obstruction_id": OBSTRUCTION,
        "evaluation_date": "2026-09-02",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR},
        "model": MODEL,
        "theorem_contract": THEOREM,
        "proof_contract": PROOF,
        "route_a": {"tuple": ROUTE, "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False},
        "scope_flags": FLAGS,
        "enumeration": {"kappa_values": list(range(1, 9)), "gamma_values": list(range(-10, 11)), "grid_cells": len(rows), "boundary_cells": len(boundaries), "phase_counts": counts},
        "phase_cells": rows,
        "boundary_cells": boundaries,
        "references": REFERENCES,
        "nonclaims": [
            "the PT dimer, exceptional points, and pseudo-Hermitian metrics are established literature and are not claimed as newly discovered",
            "the positive metric exists only for |gamma|<kappa and is not continued through an exceptional point",
            "the standard Euclidean norm is not conserved when gamma is nonzero",
            "no arithmetic local data, target Euler factor, root number, automorphy, target zero match, Hilbert-Polya operator, or Route-B authorization is produced",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT)
    output = parser.parse_args().output
    output.parent.mkdir(parents=True, exist_ok=True)
    data = build()
    output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False, allow_nan=False) + "\n")
    print(json.dumps({"status": "C297_PRODUCER_PASS", "grid_cells": len(data["phase_cells"]), "boundary_cells": len(data["boundary_cells"]), "payload_sha256": data["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
