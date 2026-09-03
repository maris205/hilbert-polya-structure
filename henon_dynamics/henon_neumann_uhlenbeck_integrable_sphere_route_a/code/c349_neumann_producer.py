#!/usr/bin/env python3
"""Deterministic exact evidence producer for HCS-C349."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c349_neumann_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C349/2026-09-03.yaml"
SOURCE = "327fc1172cebcdeb17adfd2d8ad12636fbb94f52"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EVAL_RAW = "273b6f007cf368c1ffe7be1ea8da35d0e95d671be8b0fd6361c1b397570b9b86"
EVAL_SEMANTIC = "2dc2b1ce768e0be31bfcd8cfcce7883abdf4fed32e7928b63ce3df82829dd8b7"
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

PARAMETERS = [
    (Q(0), Q(1), Q(3)), (Q(1), Q(2), Q(5)), (Q(-2), Q(1), Q(4)),
    (Q(1, 2), Q(3, 2), Q(7, 2)), (Q(0), Q(2), Q(7)),
    (Q(2), Q(5), Q(9)), (Q(1, 3), Q(5, 3), Q(10, 3)),
    (Q(3), Q(4), Q(8)), (Q(1), Q(4), Q(10)), (Q(-3), Q(-1), Q(2)),
]
SAMPLES = [
    (Q(1, 2), Q(1, 3), (Q(1), Q(2), Q(3))),
    (Q(2, 3), Q(1, 4), (Q(2), Q(-1), Q(1))),
    (Q(1, 3), Q(2, 5), (Q(3), Q(1), Q(-2))),
    (Q(3, 4), Q(1, 2), (Q(1), Q(-3), Q(2))),
    (Q(1, 5), Q(2, 3), (Q(2), Q(3), Q(-1))),
    (Q(2, 5), Q(3, 5), (Q(-1), Q(2), Q(4))),
]

MODEL = {
    "hamiltonian": "H=(norm(p)^2+x^T A x)/2 on norm(x)^2=1 and x dot p=0",
    "equations": "x_dot=p; p_dot=-A*x+(x^T A x-norm(p)^2)*x",
    "dirac_bracket": "{x_i,p_j}=delta_ij-x_i*x_j; {p_i,p_j}=x_j*p_i-x_i*p_j",
    "uhlenbeck": "F_i=x_i^2+sum_(j!=i) (x_i*p_j-x_j*p_i)^2/(a_i-a_j)",
    "lax": "L=[[V,U],[-W,-V]], M=[[0,1],[alpha-lambda,0]]",
    "quantization": "for hbar>0, -hbar^2 Delta_S2/2+x^T A x/2 on H2(S2) subset L2(S2)",
}
THEOREM = {
    "global": "the constrained Neumann flow is complete for every initial state",
    "integrals": "the three Uhlenbeck integrals are conserved and pairwise Dirac-Poisson commuting with sum F_i=1 and sum a_i F_i=2H",
    "resolvent": "det L(lambda)=U(lambda)W(lambda)-V(lambda)^2=sum F_i/(lambda-a_i) and L_dot=[L,M]",
    "regular_fibers": "every connected regular compact common fiber is a Liouville two-torus and the physical flow closes iff its frequency vector has a common period",
    "boundaries": "axial linear types, invariant coordinate circles, the repeated-spectrum commuting pair with its energy identity and open-set independence witness, and the isotropic great-circle face are separate",
    "quantum_boundary": "for hbar>0 the natural compact Schrodinger quantization on H2(S2) is self-adjoint with compact resolvent but no closed anisotropic spectrum or target-zero claim is made",
}
REFERENCES = [
    {"identifier": "10.1515/crll.1859.56.46", "role": "original Neumann mechanical problem"},
    {"identifier": "10.1007/978-1-4613-8109-9_7", "role": "authoritative quadrics and spectral-theory lineage"},
    {"identifier": "10.1515/crll.1982.334.69", "role": "geodesic-on-quadrics correspondence lineage"},
]
COLLISIONS = {
    "C186": "Euler top is a Lie-Poisson kinetic system, not a holonomic anisotropic sphere potential",
    "C244": "spherical pendulum has a linear height potential and focus-focus monodromy, not Uhlenbeck resolvent integrals",
    "C313": "round-sphere geodesics are the isotropic boundary, not the distinct-spectrum Neumann system",
    "C344": "resonant triad has a cubic intensity reduction, not the Neumann constrained Lax generator",
}
NONCLAIMS = [
    "No priority claim is made for the Neumann problem, Uhlenbeck integrals, Lax representation, quadrics correspondence, or Liouville integrability.",
    "No explicit genus-two Abel inversion or complete singular-fiber topology is claimed.",
    "No closed-form anisotropic quantum spectrum is claimed.",
    "No target arithmetic datum, Euler factor, root number, automorphy, target divisor, functional equation, target-zero match, Hilbert-Polya operator, or Route-B input is claimed.",
]
BOUNDARIES = {
    "axes": "plus or minus e1 are elliptic-elliptic, plus or minus e2 are saddle-center, and plus or minus e3 are saddle-saddle",
    "coordinate_faces": "x_i=p_i=0 is an invariant T-star S1 Neumann subsystem",
    "double_spectrum": "the SO(2) angular momentum and the simple-axis Uhlenbeck integral commute, satisfy the exact energy identity, and are independent on a nonempty open set",
    "isotropic": "zero speed gives the equilibrium sphere and nonzero speed gives great circles of least period 2*pi/speed",
    "regular_only": "Liouville two-torus topology is asserted only on connected regular common fibers",
    "singular_fibers": "no exhaustive topology is claimed beyond the explicitly declared axial, coordinate, and spectrum-degenerate faces",
    "quantum": "natural compact quantization does not imply a target-zero operator",
}


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def qstr(value: Q) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def leaves(value) -> int:
    if type(value) is dict:
        return sum(leaves(child) for child in value.values())
    if type(value) is list:
        return sum(leaves(child) for child in value)
    return 1


def semantic_yaml_hash(raw: bytes) -> str:
    value = yaml.safe_load(raw)
    canonical = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha(canonical)


def dot(left, right):
    return sum((a*b for a, b in zip(left, right)), Q(0))


def cross(left, right):
    return (
        left[1]*right[2]-left[2]*right[1],
        left[2]*right[0]-left[0]*right[2],
        left[0]*right[1]-left[1]*right[0],
    )


def sphere_state(u: Q, v: Q, seed):
    denominator = 1+u*u+v*v
    x = (2*u/denominator, 2*v/denominator, (1-u*u-v*v)/denominator)
    p = cross(x, seed)
    if dot(p, p) == 0:
        raise AssertionError("degenerate tangent sample")
    return x, p


def angular(x, p, i, j):
    return x[i]*p[j]-x[j]*p[i]


def integrals(a, x, p):
    values = []
    for i in range(3):
        value = x[i]*x[i]
        for j in range(3):
            if i != j:
                value += angular(x, p, i, j)**2/(a[i]-a[j])
        values.append(value)
    return values


def gradients(a, x, p, index):
    gx, gp = [], []
    for k in range(3):
        dx = 2*x[index] if k == index else Q(0)
        dp = Q(0)
        for j in range(3):
            if j == index:
                continue
            lij = angular(x, p, index, j)
            den = a[index]-a[j]
            dx += 2*lij*((p[j] if k == index else 0)-(p[index] if k == j else 0))/den
            dp += 2*lij*((x[index] if k == j else 0)-(x[j] if k == index else 0))/den
        gx.append(dx)
        gp.append(dp)
    return gx, gp


def dirac(gf, gg, x, p):
    fx, fp = gf
    gx, gp = gg
    return (
        dot(fx, gp)-dot(fp, gx)-dot(fx, x)*dot(x, gp)+dot(fp, x)*dot(x, gx)
        +dot(fp, p)*dot(gp, x)-dot(fp, x)*dot(gp, p)
    )


def lax_probe(a, x, p, alpha, parameter):
    inv = [Q(1)/(parameter-value) for value in a]
    u = sum((x[i]*x[i]*inv[i] for i in range(3)), Q(0))
    v = sum((x[i]*p[i]*inv[i] for i in range(3)), Q(0))
    w = 1+sum((p[i]*p[i]*inv[i] for i in range(3)), Q(0))
    pdot = [(-a[i]+alpha)*x[i] for i in range(3)]
    direct_du = 2*sum((x[i]*p[i]*inv[i] for i in range(3)), Q(0))
    direct_dv = sum(((p[i]*p[i]+x[i]*pdot[i])*inv[i] for i in range(3)), Q(0))
    direct_dw = 2*sum((p[i]*pdot[i]*inv[i] for i in range(3)), Q(0))
    fs = integrals(a, x, p)
    residue_sum = sum((fs[i]*inv[i] for i in range(3)), Q(0))
    return {
        "lambda": qstr(parameter), "U": qstr(u), "V": qstr(v), "W": qstr(w),
        "determinant": qstr(u*w-v*v), "residue_sum": qstr(residue_sum),
        "direct_U_dot": qstr(direct_du), "lax_U_dot": qstr(2*v),
        "direct_V_dot": qstr(direct_dv), "lax_V_dot": qstr(w+(alpha-parameter)*u),
        "direct_W_dot": qstr(direct_dw), "lax_W_dot": qstr(2*(alpha-parameter)*v),
    }


def state_rows():
    rows = []
    for parameter_index, a in enumerate(PARAMETERS):
        for sample_index, (u, v, seed) in enumerate(SAMPLES):
            x, p = sphere_state(u, v, seed)
            kinetic = dot(p, p)
            potential = sum((a[i]*x[i]*x[i] for i in range(3)), Q(0))
            energy = (kinetic+potential)/2
            alpha = potential-kinetic
            fs = integrals(a, x, p)
            fdot = []
            for i in range(3):
                derivative = 2*x[i]*p[i]
                for j in range(3):
                    if i != j:
                        derivative += 2*angular(x, p, i, j)*x[i]*x[j]
                fdot.append(derivative)
            grads = [gradients(a, x, p, i) for i in range(3)]
            brackets = [dirac(grads[0], grads[1], x, p),
                        dirac(grads[0], grads[2], x, p),
                        dirac(grads[1], grads[2], x, p)]
            probes = [lax_probe(a, x, p, alpha, a[2]+Q(1)),
                      lax_probe(a, x, p, alpha, a[2]+Q(2))]
            rows.append({
                "parameter_index": parameter_index, "sample_index": sample_index,
                "a": [qstr(z) for z in a], "x": [qstr(z) for z in x],
                "p": [qstr(z) for z in p], "sphere_norm": qstr(dot(x, x)),
                "tangent_dot": qstr(dot(x, p)), "kinetic_norm": qstr(kinetic),
                "potential": qstr(potential), "energy": qstr(energy),
                "alpha": qstr(alpha), "F": [qstr(z) for z in fs],
                "sum_F": qstr(sum(fs, Q(0))),
                "weighted_F": qstr(sum((a[i]*fs[i] for i in range(3)), Q(0))),
                "F_dot": [qstr(z) for z in fdot],
                "dirac_pairs": [qstr(z) for z in brackets], "lax_probes": probes,
            })
    return rows


def equilibrium_rows():
    rows = []
    names = ["elliptic-elliptic", "saddle-center", "saddle-saddle"]
    for parameter_index, a in enumerate(PARAMETERS):
        for axis in range(3):
            squares = [a[j]-a[axis] for j in range(3) if j != axis]
            rows.append({
                "parameter_index": parameter_index, "axis": axis+1,
                "a": [qstr(z) for z in a],
                "linear_frequency_squares": [qstr(z) for z in squares],
                "type": names[axis], "copies": 2,
            })
    return rows


def coordinate_rows():
    rows = []
    for parameter_index, a in enumerate(PARAMETERS):
        for missing in range(3):
            remain = [j for j in range(3) if j != missing]
            rows.append({
                "parameter_index": parameter_index, "missing_axis": missing+1,
                "remaining_axes": [j+1 for j in remain],
                "potential_coefficients": [qstr(a[j]) for j in remain],
                "equation": "theta_ddot=-(a_second-a_first)*sin(theta)*cos(theta)",
                "invariance_receipt": "x_i_dot=p_i=0 and p_i_dot=(-a_i+alpha)*x_i=0",
            })
    return rows


def single_integral(a, x, p, index):
    value = x[index]*x[index]
    for j in range(3):
        if j != index:
            value += angular(x, p, index, j)**2/(a[index]-a[j])
    return value


def angular_gradient(x, p, i, j):
    gx = [Q(0), Q(0), Q(0)]
    gp = [Q(0), Q(0), Q(0)]
    gx[i], gx[j] = p[j], -p[i]
    gp[i], gp[j] = -x[j], x[i]
    return gx, gp


def differential(gradient, dx, dp):
    return dot(gradient[0], dx)+dot(gradient[1], dp)


def repeated_rows():
    rows = []
    for repeated_value, simple_value in ((Q(0), Q(3)), (Q(-2), Q(5))):
        for pair in ((0, 1), (0, 2), (1, 2)):
            simple = next(i for i in range(3) if i not in pair)
            a = [simple_value, simple_value, simple_value]
            a[pair[0]] = repeated_value
            a[pair[1]] = repeated_value
            first, second = pair
            x = [Q(0), Q(0), Q(0)]
            p = [Q(0), Q(0), Q(0)]
            x[first], x[simple], p[second] = Q(3, 5), Q(4, 5), Q(1)
            direction_1_x = [Q(0), Q(0), Q(0)]
            direction_1_x[first], direction_1_x[simple] = Q(-4, 5), Q(3, 5)
            direction_1_p = [Q(0), Q(0), Q(0)]
            direction_2_x = [Q(0), Q(0), Q(0)]
            direction_2_p = [Q(0), Q(0), Q(0)]
            direction_2_p[second] = Q(1)
            j_gradient = angular_gradient(x, p, first, second)
            f_gradient = gradients(a, x, p, simple)
            d_j = [differential(j_gradient, direction_1_x, direction_1_p),
                   differential(j_gradient, direction_2_x, direction_2_p)]
            d_f = [differential(f_gradient, direction_1_x, direction_1_p),
                   differential(f_gradient, direction_2_x, direction_2_p)]
            wedge = d_j[0]*d_f[1]-d_j[1]*d_f[0]
            j_value = angular(x, p, first, second)
            f_value = single_integral(a, x, p, simple)
            twice_energy = dot(p, p)+sum((a[i]*x[i]*x[i] for i in range(3)), Q(0))
            energy_rhs = repeated_value+j_value*j_value+(simple_value-repeated_value)*f_value
            rows.append({
                "a": [qstr(z) for z in a], "repeated_axes": [pair[0]+1, pair[1]+1],
                "simple_axis": simple+1, "noether_momentum": f"L_{pair[0]+1}{pair[1]+1}",
                "momentum_derivative": "0", "symmetry": "SO(2)",
                "commuting_pair": [f"J_{first+1}{second+1}", f"F_{simple+1}"],
                "dirac_bracket": qstr(dirac(j_gradient, f_gradient, x, p)),
                "energy_identity": f"2H=a+J_{first+1}{second+1}^2+(b-a)*F_{simple+1}",
                "energy_lhs": qstr(twice_energy), "energy_rhs": qstr(energy_rhs),
                "independence_witness": {
                    "x": [qstr(z) for z in x], "p": [qstr(z) for z in p],
                    "direction_1_x": [qstr(z) for z in direction_1_x],
                    "direction_1_p": [qstr(z) for z in direction_1_p],
                    "direction_2_x": [qstr(z) for z in direction_2_x],
                    "direction_2_p": [qstr(z) for z in direction_2_p],
                    "dJ": [qstr(z) for z in d_j], "dF": [qstr(z) for z in d_f],
                    "wedge": qstr(wedge)},
                "uhlenbeck_boundary": "individual repeated-axis fractions are not evaluated",
            })
    return rows


def isotropic_rows():
    rows = []
    for speed in (Q(0), Q(1, 2), Q(1), Q(3, 2), Q(2)):
        rows.append({
            "speed": qstr(speed),
            "class": "equilibrium_sphere" if speed == 0 else "great_circle",
            "equation": "p_dot=-speed^2*x",
            "least_period": None if speed == 0 else f"2*pi/({qstr(speed)})",
            "period_times_speed": None if speed == 0 else "2*pi",
        })
    return rows


def make_data():
    raw_yaml = EVALUATION.read_bytes()
    if sha(raw_yaml) != EVAL_RAW or semantic_yaml_hash(raw_yaml) != EVAL_SEMANTIC:
        raise AssertionError("evaluation lock mismatch")
    states = state_rows()
    equilibria = equilibrium_rows()
    coordinates = coordinate_rows()
    repeated = repeated_rows()
    isotropic = isotropic_rows()
    data = {
        "schema": "hcs-c349-neumann-uhlenbeck-v1", "candidate_id": "HCS-C349",
        "obstruction_id": "HEN-O333", "evaluation_date": "2026-09-03",
        "source_commit": SOURCE, "fixed_epoch": EPOCH, "scope_literal": SCOPE,
        "evaluator": {"authority": "flow_systems/skills/route-a-evaluator.md",
                      "version": "0.2.0", "sha256": EVALUATOR},
        "evaluation": {"path": "evaluations/route_a/HCS-C349/2026-09-03.yaml",
                       "raw_sha256": EVAL_RAW, "semantic_sha256": EVAL_SEMANTIC},
        "model": MODEL, "theorem_contract": THEOREM, "references": REFERENCES,
        "collision_boundary": COLLISIONS, "nonclaims": NONCLAIMS,
        "route_a": {"tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
                    "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False},
        "scope_flags": FLAGS,
        "parameter_grid": {
            "ordered_triples": [[qstr(z) for z in row] for row in PARAMETERS],
            "rational_sphere_parameters": [[qstr(u), qstr(v)] for u, v, _ in SAMPLES],
            "tangent_seeds": [[qstr(z) for z in seed] for _, _, seed in SAMPLES],
            "lax_probes_per_state": 2,
            "evidence_role": "exact finite convention receipt, not proof by sampling",
        },
        "state_rows": states, "equilibrium_rows": equilibria,
        "coordinate_face_rows": coordinates, "repeated_spectrum_rows": repeated,
        "isotropic_rows": isotropic, "boundary_atlas": BOUNDARIES,
        "enumeration": {
            "parameter_triples": len(PARAMETERS), "state_rows": len(states),
            "lax_probe_rows": 2*len(states), "equilibrium_rows": len(equilibria),
            "coordinate_face_rows": len(coordinates),
            "repeated_spectrum_rows": len(repeated), "isotropic_rows": len(isotropic),
            "audited_leaf_count": 0,
        },
    }
    data["enumeration"]["audited_leaf_count"] = leaves(data)
    data["payload_sha256"] = sha(json.dumps(
        data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode())
    return data


def main():
    if sys.flags.optimize:
        raise RuntimeError("C349 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    raw = json.dumps(make_data(), sort_keys=True, indent=2, ensure_ascii=False)+"\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(raw)
    print(f"C349_PRODUCER_PASS {sha(raw.encode())}")


if __name__ == "__main__":
    main()
