#!/usr/bin/env python3
"""Deterministic exact evidence producer for HCS-C354."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

import sympy as sp
import yaml

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c354_lagrange_top_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C354/2026-09-03.yaml"
SOURCE = "140c8714b74de666d56f441ddfb712026955901a"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EVAL_RAW = "4af99b49987c3f29c85fb4e7caf7ba5c8881e45c36bbff20cb816c24478b403c"
EVAL_SEMANTIC = "e13efe34d72f2daa91dbd177462da782abbc44f4ed82a72fb4226b97a9781098"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600

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
    "hamiltonian": "H=p_theta^2/(2A)+(L-G*cos(theta))^2/(2A*sin(theta)^2)+G^2/(2C)+gamma*cos(theta)",
    "reduced_cubic": "A^2*u_dot^2=P(u)=2A*(E-G^2/(2C)-gamma*u)*(1-u^2)-(L-G*u)^2",
    "reconstruction": "phi_dot=(L-G*u)/(A*(1-u^2)); psi_dot=G/C-u*phi_dot",
    "regular_chart": "u=cos(theta) with -1<u<1 and z-y-z Euler angles modulo 2*pi",
    "quantization": "the positive elliptic rigid-body kinetic operator plus bounded gamma*cos(theta) on compact SO(3)",
}
THEOREM = {
    "global": "the positive-inertia Lagrange-top Hamiltonian flow is complete on T-star SO(3)",
    "root_chambers": "regular nonsteady nutation is exactly a compact positive component of the reduced cubic in (-1,1), necessarily bounded by two simple roots",
    "elliptic_solution": "when P=2*A*gamma*(u-r1)*(u-r2)*(u-r3) with -1<r1<r2<1<r3, u=r1+(r2-r1)*sn(nu*(t-t0),k)^2 with k^2=(r2-r1)/(r3-r1) and nu^2=gamma*(r3-r1)/(2A)",
    "phase_closure": "the two reconstruction increments are explicit complete third-kind elliptic integrals and the regular SO(3) orbit closes iff both increments divided by 2*pi are rational",
    "boundaries": "pole compatibility, steady precession, separatrix, sleeping, zero-spin, free-top, and spherical-inertia faces are stated separately",
    "quantum_boundary": "the compact natural quantization is self-adjoint with compact resolvent, but no closed quantum spectrum or target-zero identification is claimed",
}
BOUNDARIES = {
    "north_pole": "u=1 is reachable only if L=G; Euler reconstruction is replaced by a regular group chart",
    "south_pole": "u=-1 is reachable only if L=-G; Euler reconstruction is replaced by a regular group chart",
    "steady": "P(u0)=P'(u0)=0 gives constant inclination; closure is the rational ratio test for its two constant group angular velocities",
    "separatrix": "a nonconstant orbit approaching an interior double root has infinite physical time and is not assigned a finite nutation period",
    "free": "gamma=0 lowers the reduced polynomial degree and is the free symmetric-top boundary, not an elliptic cubic chamber",
    "spherical": "A=C is a symmetry enhancement but does not invalidate the regular reconstruction formulas",
    "sleeping": "u=plus or minus one with zero transverse velocity is handled directly on SO(3)",
    "regular_only": "the two-phase iff uses only trajectories staying in the regular Euler chart",
}
REFERENCES = [
    {"identifier": "10.1007/978-3-0348-0918-4", "role": "authoritative Lagrange-top reduction and global integrable-systems lineage"},
    {"identifier": "https://assets.cambridge.org/97805215/61297/excerpt/9780521561297_excerpt.pdf", "role": "Cambridge publisher excerpt identifying Audin's authoritative spinning-top text"},
]
COLLISIONS = {
    "C186": "Euler top is the gravity-free Lie-Poisson boundary and has no two-angle heavy-top reconstruction",
    "C244": "spherical pendulum has no axial spin momentum and owns a different focus-focus theorem",
    "C344": "resonant triad has elliptic intensity and two phases but a different complex-amplitude Poisson owner",
    "C349": "Neumann dynamics is a holonomic sphere oscillator with Uhlenbeck integrals, not a rigid body on SO(3)",
}
NONCLAIMS = [
    "This is a source-local reconstruction and makes no literature-priority claim.",
    "No exhaustive singular-fiber topology beyond the declared faces is claimed.",
    "Finite receipts test conventions and algebra; they do not prove the continuum completeness theorem.",
    "No target arithmetic datum, Euler factor, root number, automorphy, target divisor, functional equation, target-zero match, Hilbert-Polya operator, or Route-B input is claimed.",
]
PARAMETERS = [
    (Q(1), Q(2), Q(1), Q(1), Q(0), Q(2)),
    (Q(1), Q(2), Q(1), Q(0), Q(1), Q(1)),
    (Q(2), Q(1), Q(3), Q(1), Q(2), Q(4)),
    (Q(3), Q(2), Q(1), Q(1), Q(-1), Q(2)),
    (Q(1), Q(2), Q(1), Q(1), Q(1), Q(1)),
    (Q(1), Q(1), Q(8), Q(3), Q(0), Q(2)),
    (Q(2), Q(3), Q(1), Q(1), Q(1), Q(2)),
    (Q(3), Q(5), Q(2), Q(2), Q(1), Q(3)),
    (Q(4), Q(3), Q(1), Q(-1), Q(2), Q(3)),
    (Q(2), Q(5), Q(4), Q(3), Q(-2), Q(5)),
    (Q(1), Q(4), Q(2), Q(0), Q(0), Q(0)),
    (Q(5), Q(2), Q(3), Q(2), Q(3), Q(6)),
]
PROBES = (Q(-3, 4), Q(-1, 3), Q(0), Q(2, 5), Q(4, 5))
ELLIPTIC = [
    (Q(1), Q(1), Q(-3, 4), Q(1, 4), Q(3, 2)),
    (Q(2), Q(3), Q(-2, 3), Q(1, 3), Q(5, 3)),
    (Q(3), Q(2), Q(-1, 2), Q(1, 2), Q(2)),
    (Q(5, 2), Q(4), Q(-4, 5), Q(1, 5), Q(6, 5)),
]


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def qstr(value: Q) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def leaves(value) -> int:
    if type(value) is dict:
        return sum(leaves(v) for v in value.values())
    if type(value) is list:
        return sum(leaves(v) for v in value)
    return 1


def coeffs(A: Q, C: Q, gamma: Q, L: Q, G: Q, E: Q) -> tuple[Q, ...]:
    h0 = E-G*G/(2*C)
    return (2*A*h0-L*L, -2*A*gamma+2*L*G,
            -2*A*h0-G*G, 2*A*gamma)


def peval(cs: tuple[Q, ...], u: Q) -> Q:
    return sum((c*u**i for i, c in enumerate(cs)), Q(0))


def discriminant(cs: tuple[Q, ...]) -> Q:
    d, c, b, a = cs
    return b*b*c*c-4*a*c*c*c-4*b*b*b*d-27*a*a*d*d+18*a*b*c*d


def interval_rows(cs: tuple[Q, ...]):
    u = sp.symbols("u")
    poly = sum(sp.Rational(c.numerator, c.denominator)*u**i for i, c in enumerate(cs))
    rows = []
    for (left, right), multiplicity in sp.polys.polytools.intervals(poly, eps=sp.Rational(1, 4096)):
        left, right = Q(left), Q(right)
        rows.append({"left": qstr(left), "right": qstr(right), "multiplicity": int(multiplicity)})
    return rows


def parameter_rows():
    rows = []
    for index, values in enumerate(PARAMETERS):
        A, C, gamma, L, G, E = values
        cs = coeffs(*values)
        probes = []
        for u in PROBES:
            effective = G*G/(2*C)+gamma*u+(L-G*u)**2/(2*A*(1-u*u))
            phi = (L-G*u)/(A*(1-u*u))
            psi = G/C-u*phi
            probes.append({
                "u": qstr(u), "P_polynomial": qstr(peval(cs, u)),
                "P_energy": qstr(2*A*(1-u*u)*(E-effective)),
                "effective_potential": qstr(effective),
                "phi_dot": qstr(phi), "psi_dot": qstr(psi),
                "momentum_reconstruction": qstr(A*(1-u*u)*phi+G*u),
                "spin_reconstruction": qstr(C*(psi+u*phi)),
            })
        rows.append({
            "index": index, "A": qstr(A), "C": qstr(C), "gamma": qstr(gamma),
            "L": qstr(L), "G": qstr(G), "E": qstr(E),
            "coefficients_low_to_high": [qstr(c) for c in cs],
            "discriminant": qstr(discriminant(cs)),
            "P_minus_one": qstr(peval(cs, Q(-1))), "P_plus_one": qstr(peval(cs, Q(1))),
            "root_intervals": interval_rows(cs), "probes": probes,
        })
    return rows


def elliptic_rows():
    rows = []
    for index, (A, gamma, r1, r2, r3) in enumerate(ELLIPTIC):
        gap = r2-r1
        outer = r3-r1
        k2 = gap/outer
        nu2 = gamma*outer/(2*A)
        # Coefficients in z of both sides after u=r1+gap*z and z_dot^2=4 nu^2 z(1-z)(1-k^2 z).
        left = (Q(0), 4*A*A*gap*gap*nu2,
                -4*A*A*gap*gap*nu2*(1+k2),
                4*A*A*gap*gap*nu2*k2)
        alpha = 2*A*gamma
        right = (Q(0), alpha*gap*gap*outer,
                 -alpha*gap*gap*(outer+gap), alpha*gap*gap*gap)
        rows.append({
            "index": index, "A": qstr(A), "gamma": qstr(gamma),
            "r1": qstr(r1), "r2": qstr(r2), "r3": qstr(r3),
            "gap": qstr(gap), "outer_gap": qstr(outer),
            "k_squared": qstr(k2), "nu_squared": qstr(nu2),
            "period_prefactor_squared": qstr(8*A/(gamma*outer)),
            "pi_characteristic_north": qstr(gap/(1-r1)),
            "pi_characteristic_south": qstr(-gap/(1+r1)),
            "north_prefactor_squared": qstr(4/(2*A*gamma*outer*(1-r1)**2)),
            "south_prefactor_squared": qstr(4/(2*A*gamma*outer*(1+r1)**2)),
            "substitution_lhs": [qstr(c) for c in left],
            "substitution_rhs": [qstr(c) for c in right],
        })
    return rows


def steady_rows():
    # The first row is an exact interior double root; the next two lock pole factors.
    A, C, gamma, L, G, E, u0 = Q(1), Q(1), Q(8), Q(3), Q(0), Q(2), Q(-1, 2)
    cs = coeffs(A, C, gamma, L, G, E)
    derivative = tuple((i*cs[i] for i in range(1, 4)))
    return [
        {"kind": "interior_double_root", "u": qstr(u0), "P": qstr(peval(cs, u0)),
         "P_prime": qstr(peval(derivative, u0)), "P_second": qstr(2*cs[2]+6*cs[3]*u0)},
        {"kind": "north_pole", "formula_value": qstr(peval(coeffs(Q(2), Q(3), Q(5), Q(7), Q(7), Q(11)), Q(1))),
         "expected": "0", "compatibility": "L=G"},
        {"kind": "south_pole", "formula_value": qstr(peval(coeffs(Q(2), Q(3), Q(5), Q(7), Q(-7), Q(11)), Q(-1))),
         "expected": "0", "compatibility": "L=-G"},
    ]


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C354 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    raw_eval = EVALUATION.read_bytes()
    semantic = sha(json.dumps(yaml.safe_load(raw_eval), sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode())
    if sha(raw_eval) != EVAL_RAW or semantic != EVAL_SEMANTIC:
        raise AssertionError("evaluation lock mismatch")
    data = {
        "schema": "hcs-c354-lagrange-top-evidence-v1", "candidate_id": "HCS-C354",
        "obstruction_id": "HEN-O338", "evaluation_date": "2026-09-03",
        "source_commit": SOURCE, "fixed_epoch": EPOCH, "scope_literal": SCOPE,
        "evaluator": {"authority": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR},
        "evaluation_lock": {"relative_path": "evaluations/route_a/HCS-C354/2026-09-03.yaml", "raw_sha256": EVAL_RAW, "semantic_sha256": EVAL_SEMANTIC},
        "model": MODEL, "theorem_contract": THEOREM, "boundary_atlas": BOUNDARIES,
        "references": REFERENCES, "collision_boundary": COLLISIONS, "nonclaims": NONCLAIMS,
        "route_a": {"tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"], "overall": "ROUTE_A_REJECTED", "route_b": False},
        "scope_flags": FLAGS, "parameter_grid": [[qstr(v) for v in row] for row in PARAMETERS],
        "parameter_rows": parameter_rows(), "elliptic_rows": elliptic_rows(), "steady_and_pole_rows": steady_rows(),
    }
    data["enumeration"] = {
        "parameter_rows": len(data["parameter_rows"]), "probe_rows": len(PARAMETERS)*len(PROBES),
        "root_intervals": sum(len(r["root_intervals"]) for r in data["parameter_rows"]),
        "elliptic_rows": len(data["elliptic_rows"]), "steady_and_pole_rows": len(data["steady_and_pole_rows"]),
        "leaf_count_without_payload_hash": leaves(data),
    }
    canonical = json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    data["payload_sha256"] = sha(canonical)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False)+"\n")
    print(f"C354_PRODUCER_PASS rows={len(data['parameter_rows'])} leaves={leaves(data)} payload={data['payload_sha256']}")


if __name__ == "__main__":
    main()
