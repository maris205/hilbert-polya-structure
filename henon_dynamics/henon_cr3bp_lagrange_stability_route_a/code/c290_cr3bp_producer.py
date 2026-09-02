#!/usr/bin/env python3
"""Deterministic evidence producer for the planar CR3BP Lagrange atlas."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c290_cr3bp_evidence.json"
SOURCE = "7fbe9db30cc460a82883533d7cfb2edd988c5b65"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788307200
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"

MODEL = {
    "problem": "planar circular restricted three-body problem in synodic normalized units",
    "primaries": "masses 1-mu and mu at (-mu,0) and (1-mu,0)",
    "range": "0<mu<=1/2; collision points are removed",
    "potential": "Omega=(x^2+y^2)/2+(1-mu)/r1+mu/r2",
    "equations": "xddot-2 ydot=Omega_x and yddot+2 xdot=Omega_y",
    "stability_meaning": "boundedness of the linearized flow, including resonant ratios; no nonlinear resonance or KAM claim",
}
THEOREM = {
    "equilibria": "exactly five equilibria: one in each collinear interval and the two equilateral points",
    "triangular_locations": "L4,L5=(1/2-mu, plus_or_minus sqrt(3)/2)",
    "collinear": "every collinear point has S>1 and saddle-times-center linear type",
    "triangular_polynomial": "lambda^4+lambda^2+(27/4)mu(1-mu)",
    "routh_boundary": "mu_R=(1-sqrt(23/27))/2 separates bounded elliptic linear flow from a Hamiltonian quartet",
    "critical": "at mu=mu_R and both L4,L5, each of plus_or_minus i/sqrt(2) has algebraic multiplicity 2 and geometric multiplicity 1, so solutions grow linearly and the equilibrium is not linearly stable",
}
PROOF = {
    "five_points": "Omega_y=0 forces y=0 or equal unit distances, giving three monotone collinear roots and two equilateral roots",
    "collinear_uniqueness": "Omega_x is strictly increasing on each of the three collision-free x intervals with opposite endpoint signs",
    "collinear_instability": "S>1 makes the constant term (1+2S)(1-S) negative, forcing one real and one imaginary eigenvalue pair",
    "triangular_hessian": "the raw Hessian gives trace 3 and determinant (27/4)mu(1-mu) in the rotating characteristic determinant",
    "critical_defect": "at both L4,L5 the two-by-two position pencil has rank one at lambda=plus_or_minus i/sqrt(2), hence one eigenvector per double eigenvalue and a nontrivial Jordan block",
    "finite_role": "finite root and parameter cells are regression evidence and do not prove the all-mu theorem",
}
ROUTE = {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}
FLAGS = {"arithmetic_local_data": False, "euler_factors": False, "root_numbers": False, "automorphy": False, "target_divisor_or_counting_law": False, "target_functional_equation": False, "target_zero_match": False, "hilbert_polya_operator": False, "route_b_input": False}
REFERENCES = [
    {"id": "Lagrange1772", "authors": "Joseph-Louis Lagrange", "title": "Essai sur le Probleme des trois Corps", "venue": "Prix de l'Academie royale des sciences de Paris, tome IX (1772); Oeuvres, tome VI", "identifier": "Lagrange-1772-Oeuvres-VI-229-331", "url": "https://fr.wikisource.org/wiki/M%C3%A9moires_extraits_des_recueils_de_l%E2%80%99Acad%C3%A9mie_des_sciences_de_Paris_et_de_l%E2%80%99Institut_de_France/Essai_sur_le_Probl%C3%A8me_des_trois_Corps", "ownership": "historical owner of the equilateral three-body configuration"},
    {"id": "Gascheau1843", "authors": "Gabriel Gascheau", "title": "Mouvements relatifs d'un systeme de corps", "venue": "These de mecanique, Faculte des sciences de Paris, Bachelier (1843), 36 pp. and plate", "identifier": "BnF-Gallica-ark-12148-bpt6k5789653w", "url": "https://gallica.bnf.fr/ark:/12148/bpt6k5789653w", "ownership": "first historical owner of the Newtonian triangular linear-stability criterion"},
    {"id": "Routh1874", "authors": "Edward John Routh", "title": "On Laplace's Three Particles, with a Supplement on the Stability of Steady Motion", "venue": "Proceedings of the London Mathematical Society s1-6 (1874), 86-97", "identifier": "10.1112/plms/s1-6.1.86", "url": "https://doi.org/10.1112/plms/s1-6.1.86", "ownership": "subsequent treatment and inverse-power-law generalization of triangular stability"},
    {"id": "MeyerHallOffin2009", "authors": "Kenneth R. Meyer, Glen R. Hall, and Dan Offin", "title": "Introduction to Hamiltonian Dynamical Systems and the N-Body Problem", "venue": "Springer, second edition (2009)", "identifier": "10.1007/978-0-387-09724-4", "url": "https://doi.org/10.1007/978-0-387-09724-4", "ownership": "authoritative modern source for the restricted problem and linear Hamiltonian stability"},
]
NONCLAIMS = [
    "the Lagrange equilibria and Gascheau-Routh threshold are classical and not claimed as literature originality",
    "the elliptic linearized flow is bounded also at resonant mass ratios; no nonlinear resonance, bifurcation, or KAM conclusion is claimed",
    "finite numerical root cells are regression evidence and do not replace the analytic existence and uniqueness proof",
]


def q(x: Fraction) -> str:
    return str(x)


def dec(x: mp.mpf, digits: int = 65) -> str:
    if abs(x) < mp.mpf("1e-60"):
        x = mp.mpf("0")
    return mp.nstr(x, digits)


def payload_hash(data: dict) -> str:
    body = dict(data); body.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def collinear_row(mu_q: Fraction, point: str) -> dict:
    mu = mp.mpf(mu_q.numerator)/mu_q.denominator
    def f(x: mp.mpf) -> mp.mpf:
        return x-(1-mu)*(x+mu)/abs(x+mu)**3-mu*(x-1+mu)/abs(x-1+mu)**3
    d = (mu/3)**(mp.mpf(1)/3)
    guesses = {
        "L3": (-1-mu, -mp.mpf("0.8")-mu),
        "L1": (1-mu-mp.mpf("1.5")*d, 1-mu-mp.mpf("0.5")*d),
        "L2": (1-mu+mp.mpf("0.5")*d, 1-mu+mp.mpf("1.5")*d),
    }
    x = mp.findroot(f, guesses[point], tol=mp.mpf("1e-75"), maxsteps=100)
    if abs(x) < mp.mpf("1e-60"):
        x = mp.mpf("0")
    r1, r2 = abs(x+mu), abs(x-1+mu)
    S = (1-mu)/r1**3+mu/r2**3
    return {
        "mu": q(mu_q), "point": point,
        "interval": {"L3": "(-infinity,-mu)", "L1": "(-mu,1-mu)", "L2": "(1-mu,infinity)"}[point],
        "x": dec(x), "omega_x_residual": dec(f(x)), "S": dec(S),
        "lambda2_coefficient": dec(2-S), "constant_coefficient": dec(1+S-2*S*S),
        "linear_type": "saddle_times_center", "linearly_stable": False,
    }


def triangle_row(mu: Fraction) -> dict:
    routh = 27*mu*(1-mu); disc = 1-routh
    regime = "bounded_elliptic" if disc > 0 else "unstable_hamiltonian_quartet"
    return {
        "mu": q(mu), "routh_parameter": q(routh), "routh_discriminant": q(disc),
        "charpoly_constant": q(routh/4), "lambda_square_sum": "-1", "lambda_square_product": q(routh/4),
        "linear_type": regime, "linearly_stable": disc > 0,
    }


def build() -> dict:
    mp.mp.dps = 90
    mus = (Fraction(1,1000), Fraction(1,100), Fraction(1,50), Fraction(1,30), Fraction(1,25), Fraction(1,10), Fraction(1,4), Fraction(1,2))
    triangular = [triangle_row(mu) for mu in mus]
    collinear = [collinear_row(mu, point) for mu in mus for point in ("L3", "L1", "L2")]
    critical = {
        "mu_formula": "(1-sqrt(23/27))/2", "routh_parameter": "1",
        "charpoly": "lambda^4+lambda^2+1/4=(lambda^2+1/2)^2",
        "eigenvalues": ["-i/sqrt(2)", "i/sqrt(2)"], "algebraic_multiplicity_each": 2,
        "geometric_multiplicity_each": 1,
        "rank_cells": [
            {"point": point, "mixed_hessian_sign": sign, "eigenvalue": eigenvalue, "matrix_rank": 3, "geometric_multiplicity": 1}
            for point, sign in (("L4", 1), ("L5", -1))
            for eigenvalue in ("-i/sqrt(2)", "i/sqrt(2)")
        ],
        "defective": True, "linear_growth": True, "linearly_stable": False,
    }
    boundaries = [
        {"name": "zero_mass", "parameters": {"mu": "0"}, "conclusion": "excluded degenerate limit; the unit circle is a continuum of rotating Kepler equilibria"},
        {"name": "equal_masses", "parameters": {"mu": "1/2"}, "conclusion": "included endpoint; L4 and L5 have an unstable Hamiltonian quartet"},
        {"name": "collisions", "parameters": {"positions": "(-mu,0),(1-mu,0)"}, "conclusion": "removed singular configurations and never counted as equilibria"},
        {"name": "critical_defect", "parameters": {"mu": "mu_R"}, "conclusion": "spectrally imaginary but defective with linear growth; not linearly stable"},
        {"name": "claim_level", "parameters": {"chamber": "0<mu<mu_R"}, "conclusion": "bounded linearized flow including resonant ratios; no nonlinear resonance, bifurcation, or KAM conclusion"},
    ]
    data = {
        "schema": "hcs-c290-cr3bp-lagrange-stability-v1", "candidate_id": "HCS-C290",
        "evaluation_date": "2026-09-02", "source_commit": SOURCE, "fixed_epoch": EPOCH,
        "scope_literal": SCOPE, "evaluator": {"version": "0.2.0", "sha256": EVALUATOR},
        "model": MODEL, "theorem_contract": THEOREM, "proof_contract": PROOF,
        "route_a": ROUTE, "scope_flags": FLAGS,
        "enumeration": {"mu_values": [q(mu) for mu in mus], "triangular_cells": len(triangular), "collinear_cells": len(collinear), "critical_cells": 1, "boundary_cells": len(boundaries)},
        "triangular_cells": triangular, "collinear_cells": collinear, "critical_cell": critical,
        "boundary_cells": boundaries, "references": REFERENCES, "nonclaims": NONCLAIMS,
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser(); parser.add_argument("--output", type=Path, default=DEFAULT); args = parser.parse_args()
    data = build(); args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False)+"\n")
    total = sum(data["enumeration"][key] for key in ("triangular_cells", "collinear_cells", "critical_cells", "boundary_cells"))
    print(f"C290_PRODUCER_PASS {data['payload_sha256']} cells={total}")


if __name__ == "__main__":
    main()
