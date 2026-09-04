#!/usr/bin/env python3
"""Deterministic exact evidence producer for HCS-C359."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction as Q
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c359_pais_uhlenbeck_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C359/2026-09-04.yaml"
SOURCE = "05ca5f96b2c69a6ad6ba153d1084df750d7722c0"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EVAL_RAW = "7e46f2ada7433620bf08d1e0fcfe0da43e48455985312c30cc474425aee61156"
EVAL_SEMANTIC = "a15b1abe7eb8b34cdaf979485a1bcace0cd14de24289b4ed3fee7ecc7b4c9f64"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788480000

FLAGS = {
    "claims_target_arithmetic_local_data": False,
    "claims_target_euler_factors": False,
    "claims_root_number": False,
    "claims_automorphy": False,
    "claims_target_divisor_or_counting_law": False,
    "claims_target_functional_equation": False,
    "claims_target_zero_match": False,
    "claims_hilbert_polya_operator": False,
    "invokes_route_b": False,
}
MODEL = {
    "lagrangian": "L=(x_ddot^2-(omega1^2+omega2^2)*x_dot^2+omega1^2*omega2^2*x^2)/2",
    "equation": "(D^2+omega1^2)*(D^2+omega2^2)*x=0",
    "ostrogradsky": "q0=x,q1=x_dot,p1=x_ddot,p0=-(omega1^2+omega2^2)*x_dot-x_triple_dot",
    "hamiltonian": "H=p0*q1+p1^2/2+(omega1^2+omega2^2)*q1^2/2-omega1^2*omega2^2*q0^2/2",
    "distinct_positive_normal_form": "H=-(P1^2+omega1^2*Q1^2)/2+(P2^2+omega2^2*Q2^2)/2",
    "quantum_operator": "Hhat=-h_omega1 tensor I+I tensor h_omega2 on the Hermite tensor basis",
    "quantum_domain": "hbar=1; c in l2(N0^2) and lambda*c in l2(N0^2)",
}
THEOREM = {
    "canonical": "for 0<omega1<omega2 the displayed linear transform is symplectic and gives one negative and one positive oscillator",
    "classical_resonance": "if omega1/omega2 is rational every orbit is periodic; if irrational only equilibrium and single-mode trajectories are periodic, while every double-mode trajectory is dense on its invariant two-torus",
    "equal_frequency": "at omega1=omega2=omega>0 the characteristic matrix has size-two Jordan blocks at plus and minus i*omega and x=(a+b*t)cos(omega*t)+(c+d*t)sin(omega*t)",
    "zero_negative_faces": "zero and negative squared-frequency faces are completely separated into polynomial, oscillatory, and hyperbolic solution classes",
    "quantum": "in the distinct positive chamber at hbar=1 the maximal Hermite domain c in l2 and lambda*c in l2 is self-adjoint and unbounded both above and below; rational ratios give a lattice of infinite-multiplicity eigenvalues, irrational ratios give simple dense eigenvalues with pure-point spectral measures and spectrum R",
}
BOUNDARIES = {
    "equal_positive": "the distinct-frequency canonical map is singular; secular terms occur generically and only the b=d=0 subfamily is periodic",
    "one_zero": "D^2*(D^2+omega^2)x=0 gives a+b*t+c*cos(omega*t)+d*sin(omega*t); bounded and periodic iff b=0",
    "double_zero": "D^4*x=0 gives a+b*t+c*t^2+d*t^3; only constants are bounded or periodic",
    "one_negative": "a factor D^2-nu^2 supplies exponential hyperbolic directions; all-time bounded and periodic solutions have zero hyperbolic component",
    "double_negative": "two negative squared frequencies give only hyperbolic factors, with polynomial times exponential terms on the repeated face; only zero is bounded or periodic",
    "quantum_degeneracy": "the quantum theorem is restricted to distinct positive frequencies; no equal-frequency limit of the singular normal coordinates is asserted",
}
REFERENCES = [
    {"identifier": "10.1103/PhysRev.79.145", "role": "original Pais--Uhlenbeck higher-derivative oscillator source"},
    {"identifier": "10.1016/j.nuclphysb.2004.10.037", "role": "primary analysis of benign and malicious higher-derivative ghost dynamics"},
    {"identifier": "https://arxiv.org/abs/quant-ph/0501024", "role": "primary Hamiltonian-structure analysis for the Pais--Uhlenbeck oscillator"},
]
COLLISIONS = {
    "C334": "Morse owns a one-dimensional semibounded bound spectrum and energy-dependent classical action, not a fourth-order indefinite oscillator",
    "C349": "Neumann--Uhlenbeck owns compact-sphere Liouville tori, not Ostrogradsky resonance or a difference spectrum",
    "C357": "the bilinear oscillator is a second-order nonsmooth isochronous system with a semibounded Friedrichs operator",
}
NONCLAIMS = [
    "No priority claim is made for the Pais--Uhlenbeck equation, its Hamiltonian forms, or its quantization.",
    "Frequency commensurability is source resonance and is not a rational-prime dictionary.",
    "Pure-point spectral type with dense eigenvalues does not mean discrete spectrum or compact resolvent.",
    "The self-adjoint difference operator is unbounded below and is not a Hilbert--Polya operator.",
    "No target arithmetic datum, Euler factor, root number, automorphy, target divisor, functional equation, target-zero match, or Route-B input is claimed.",
]
RATIONAL = [
    (Q(1), 1, 2), (Q(1), 2, 3), (Q(1), 3, 5), (Q(1, 2), 1, 3),
    (Q(2, 3), 2, 5), (Q(3, 2), 1, 4), (Q(2), 3, 7), (Q(5, 3), 4, 9),
]
SUPPORTS = [
    (Q(0), Q(0)), (Q(1), Q(0)), (Q(0), Q(1)), (Q(1), Q(1)),
    (Q(1, 4), Q(9, 4)), (Q(2), Q(3)), (Q(5, 2), Q(7, 3)),
    (Q(9), Q(1, 9)), (Q(11, 5), Q(13, 7)),
]
IRRATIONAL = [(1, 2, "sqrt(1/2)"), (2, 3, "sqrt(2/3)"), (1, 5, "sqrt(1/5)")]


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def qstr(x: Q) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def leaves(value) -> int:
    if type(value) is dict:
        return sum(leaves(v) for v in value.values())
    if type(value) is list:
        return sum(leaves(v) for v in value)
    return 1


def canonical_rows():
    rows = []
    poisson = [["0", "1", "0", "0"], ["-1", "0", "0", "0"],
               ["0", "0", "0", "1"], ["0", "0", "-1", "0"]]
    for i, (g, m, n) in enumerate(RATIONAL):
        w1, w2 = g*m, g*n
        rows.append({
            "frequency_index": i, "scale": qstr(g), "m": m, "n": n,
            "omega1": qstr(w1), "omega2": qstr(w2),
            "delta": qstr(w2*w2-w1*w1), "poisson_matrix": poisson,
            "mode1_energy_sign": -1, "mode2_energy_sign": 1,
            "characteristic_c2": qstr(w1*w1+w2*w2),
            "characteristic_c0": qstr(w1*w1*w2*w2),
            "common_period_over_2pi": qstr(1/g),
        })
    return rows


def orbit_rows():
    rows = []
    for fi, (g, m, n) in enumerate(RATIONAL):
        for si, (r1, r2) in enumerate(SUPPORTS):
            if r1 == 0 and r2 == 0:
                kind = "equilibrium"
            elif r1 == 0 or r2 == 0:
                kind = "single_mode"
            else:
                kind = "double_mode_resonant"
            rows.append({
                "frequency_index": fi, "support_index": si,
                "radius1_squared": qstr(r1), "radius2_squared": qstr(r2),
                "orbit_type": kind, "periodic": True,
                "common_period_over_2pi": qstr(1/g),
                "phase1_turns": m, "phase2_turns": n,
            })
    return rows


def quantum_rows():
    rows = []
    for fi, (g, m, n) in enumerate(RATIONAL):
        for n1 in range(16):
            for n2 in range(16):
                k = n*n2-m*n1
                energy = g*(Q(k)+Q(n-m, 2))
                rows.append({
                    "frequency_index": fi, "n1": n1, "n2": n2,
                    "lattice_coordinate": k, "energy": qstr(energy),
                    "energy_over_scale": qstr(Q(k)+Q(n-m, 2)),
                })
    return rows


def irrational_rows():
    rows = []
    for i, (s1, s2, ratio) in enumerate(IRRATIONAL):
        found = any(a*a*s2 == b*b*s1 for a in range(1, 65) for b in range(1, 65))
        rows.append({
            "irrational_index": i, "omega1_squared": str(s1),
            "omega2_squared": str(s2), "ratio": ratio,
            "squarefree_distinct": True, "search_bound": 64,
            "nonzero_integer_relation_found": found,
            "double_mode_closure": False, "double_mode_orbit": "dense_two_torus",
            "quantum_eigenvalues": "simple_dense_pure_point_spectrum_R",
        })
    return rows


def boundary_rows():
    return [
        {"face": "equal_positive", "factorization": "(D^2+omega^2)^2", "solution_basis": ["cos", "sin", "t*cos", "t*sin"], "generic_growth": "linear", "bounded_entire_subspace": "span(cos,sin)", "periodic_subspace": "span(cos,sin)", "quantum_claimed": False},
        {"face": "one_zero", "factorization": "D^2*(D^2+omega^2)", "solution_basis": ["1", "t", "cos", "sin"], "generic_growth": "linear", "bounded_entire_subspace": "span(1,cos,sin)", "periodic_subspace": "span(1,cos,sin)", "quantum_claimed": False},
        {"face": "double_zero", "factorization": "D^4", "solution_basis": ["1", "t", "t^2", "t^3"], "generic_growth": "cubic", "bounded_entire_subspace": "span(1)", "periodic_subspace": "span(1)", "quantum_claimed": False},
        {"face": "one_negative", "factorization": "(D^2-nu^2)*(D^2+omega^2)", "solution_basis": ["exp_plus", "exp_minus", "cos", "sin"], "generic_growth": "exponential", "bounded_entire_subspace": "span(cos,sin)", "periodic_subspace": "span(cos,sin)", "quantum_claimed": False},
        {"face": "negative_zero", "factorization": "(D^2-nu^2)*D^2", "solution_basis": ["exp_plus", "exp_minus", "1", "t"], "generic_growth": "exponential", "bounded_entire_subspace": "span(1)", "periodic_subspace": "span(1)", "quantum_claimed": False},
        {"face": "double_negative", "factorization": "(D^2-nu1^2)*(D^2-nu2^2)", "solution_basis": ["exp_nu1_plus", "exp_nu1_minus", "exp_nu2_plus", "exp_nu2_minus"], "generic_growth": "exponential", "bounded_entire_subspace": "{0}", "periodic_subspace": "{0}", "quantum_claimed": False},
        {"face": "equal_negative", "factorization": "(D^2-nu^2)^2", "solution_basis": ["exp_plus", "t*exp_plus", "exp_minus", "t*exp_minus"], "generic_growth": "linear_times_exponential", "bounded_entire_subspace": "{0}", "periodic_subspace": "{0}", "quantum_claimed": False},
    ]


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C359 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    raw_eval = EVALUATION.read_bytes()
    semantic = sha(json.dumps(yaml.safe_load(raw_eval), sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode())
    if sha(raw_eval) != EVAL_RAW or semantic != EVAL_SEMANTIC:
        raise AssertionError("evaluation lock mismatch")
    data = {
        "schema": "hcs-c359-pais-uhlenbeck-evidence-v1",
        "candidate_id": "HCS-C359", "obstruction_id": "HEN-O343",
        "evaluation_date": "2026-09-04", "source_commit": SOURCE,
        "fixed_epoch": EPOCH, "scope_literal": SCOPE,
        "evaluator": {"authority": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR},
        "evaluation_lock": {"relative_path": "evaluations/route_a/HCS-C359/2026-09-04.yaml", "raw_sha256": EVAL_RAW, "semantic_sha256": EVAL_SEMANTIC},
        "model": MODEL, "theorem_contract": THEOREM, "boundary_atlas": BOUNDARIES,
        "references": REFERENCES, "collision_boundary": COLLISIONS,
        "nonclaims": NONCLAIMS,
        "route_a": {"tuple": ["A0_FAIL", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"], "overall": "ROUTE_A_REJECTED", "route_b": False},
        "scope_flags": FLAGS, "rational_frequency_grid": [[qstr(g), m, n] for g, m, n in RATIONAL],
        "support_grid": [[qstr(a), qstr(b)] for a, b in SUPPORTS],
        "canonical_rows": canonical_rows(), "orbit_rows": orbit_rows(),
        "irrational_rows": irrational_rows(), "quantum_rows": quantum_rows(),
        "boundary_rows": boundary_rows(),
    }
    data["enumeration"] = {
        "rational_frequencies": len(RATIONAL), "supports": len(SUPPORTS),
        "canonical_rows": len(data["canonical_rows"]), "orbit_rows": len(data["orbit_rows"]),
        "irrational_rows": len(data["irrational_rows"]), "quantum_rows": len(data["quantum_rows"]),
        "boundary_rows": len(data["boundary_rows"]), "leaf_count_without_payload_hash": leaves(data),
    }
    raw = json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    data["payload_sha256"] = sha(raw)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n")
    print("C359_PRODUCER_PASS " + json.dumps({
        "canonical": len(data["canonical_rows"]), "orbits": len(data["orbit_rows"]),
        "irrational": len(data["irrational_rows"]), "quantum": len(data["quantum_rows"]),
        "boundaries": len(data["boundary_rows"]), "leaves": leaves(data),
        "payload": data["payload_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
