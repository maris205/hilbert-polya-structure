#!/usr/bin/env python3
"""Producer-independent strict theorem/evidence checker for HCS-C349."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

import yaml
from yaml.tokens import AliasToken, AnchorToken


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c349_neumann_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C349/2026-09-03.yaml"
SOURCE = "327fc1172cebcdeb17adfd2d8ad12636fbb94f52"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EVAL_RAW = "273b6f007cf368c1ffe7be1ea8da35d0e95d671be8b0fd6361c1b397570b9b86"
EVAL_SEMANTIC = "2dc2b1ce768e0be31bfcd8cfcce7883abdf4fed32e7928b63ce3df82829dd8b7"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600
CHECKS = 0

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

TOP_KEYS = {
    "schema", "candidate_id", "obstruction_id", "evaluation_date", "source_commit",
    "fixed_epoch", "scope_literal", "evaluator", "evaluation", "model",
    "theorem_contract", "references", "collision_boundary", "nonclaims", "route_a",
    "scope_flags", "parameter_grid", "state_rows", "equilibrium_rows",
    "coordinate_face_rows", "repeated_spectrum_rows", "isotropic_rows",
    "boundary_atlas", "enumeration", "payload_sha256",
}
STATE_KEYS = {
    "parameter_index", "sample_index", "a", "x", "p", "sphere_norm",
    "tangent_dot", "kinetic_norm", "potential", "energy", "alpha", "F",
    "sum_F", "weighted_F", "F_dot", "dirac_pairs", "lax_probes",
}
PROBE_KEYS = {
    "lambda", "U", "V", "W", "determinant", "residue_sum", "direct_U_dot",
    "lax_U_dot", "direct_V_dot", "lax_V_dot", "direct_W_dot", "lax_W_dot",
}
EQUILIBRIUM_KEYS = {"parameter_index", "axis", "a", "linear_frequency_squares", "type", "copies"}
COORDINATE_KEYS = {"parameter_index", "missing_axis", "remaining_axes", "potential_coefficients", "equation", "invariance_receipt"}
REPEATED_KEYS = {
    "a", "repeated_axes", "simple_axis", "noether_momentum",
    "momentum_derivative", "symmetry", "commuting_pair", "dirac_bracket",
    "energy_identity", "energy_lhs", "energy_rhs", "independence_witness",
    "uhlenbeck_boundary",
}
WITNESS_KEYS = {
    "x", "p", "direction_1_x", "direction_1_p", "direction_2_x",
    "direction_2_p", "dJ", "dF", "wedge",
}
ISOTROPIC_KEYS = {"speed", "class", "equation", "least_period", "period_times_speed"}


def need(condition, label):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def unique(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


class UniqueLoader(yaml.SafeLoader):
    pass


def construct_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in result:
            raise ValueError("non-string or duplicate YAML key")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_mapping)


def parse_yaml(raw: bytes):
    for token in yaml.scan(raw):
        if isinstance(token, (AliasToken, AnchorToken)):
            raise ValueError("YAML aliases and anchors forbidden")
    value = yaml.load(raw, Loader=UniqueLoader)
    if type(value) is not dict:
        raise ValueError("YAML root must be mapping")
    return value


def semantic_yaml_hash(value) -> str:
    return sha(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode())


def leaves(value) -> int:
    if type(value) is dict:
        return sum(leaves(child) for child in value.values())
    if type(value) is list:
        return sum(leaves(child) for child in value)
    return 1


def q(value) -> Q:
    need(type(value) is str, "rational type")
    result = Q(value)
    canonical = str(result.numerator) if result.denominator == 1 else f"{result.numerator}/{result.denominator}"
    need(value == canonical, "canonical rational")
    return result


def qlist(value, length, label):
    need(type(value) is list and len(value) == length, label+" shape")
    return [q(item) for item in value]


def dot(left, right):
    return sum((a*b for a, b in zip(left, right)), Q(0))


def cross(left, right):
    return [left[1]*right[2]-left[2]*right[1],
            left[2]*right[0]-left[0]*right[2],
            left[0]*right[1]-left[1]*right[0]]


def expected_state(u, v, seed):
    den = 1+u*u+v*v
    x = [2*u/den, 2*v/den, (1-u*u-v*v)/den]
    return x, cross(x, list(seed))


def lij(x, p, i, j):
    return x[i]*p[j]-x[j]*p[i]


def uhlenbeck(a, x, p):
    result = []
    for i in range(3):
        value = x[i]**2
        for j in range(3):
            if j != i:
                value += lij(x, p, i, j)**2/(a[i]-a[j])
        result.append(value)
    return result


def derivative_vectors(a, x, p, index):
    gx = [Q(0), Q(0), Q(0)]
    gp = [Q(0), Q(0), Q(0)]
    gx[index] += 2*x[index]
    for j in range(3):
        if j == index:
            continue
        angular_value = lij(x, p, index, j)
        scale = 2*angular_value/(a[index]-a[j])
        gx[index] += scale*p[j]
        gx[j] -= scale*p[index]
        gp[j] += scale*x[index]
        gp[index] -= scale*x[j]
    return gx, gp


def constrained_bracket(first, second, x, p):
    fx, fp = first
    gx, gp = second
    canonical = dot(fx, gp)-dot(fp, gx)
    position_projection = -dot(fx, x)*dot(x, gp)+dot(fp, x)*dot(x, gx)
    momentum_projection = dot(fp, p)*dot(gp, x)-dot(fp, x)*dot(gp, p)
    return canonical+position_projection+momentum_projection


EVAL_KEYS = {
    "schema", "candidate_id", "title", "evaluation_date", "source_commit", "fixed_epoch",
    "scope_literal", "evaluator_authority", "evaluator_version", "evaluator_authority_sha256",
    "obstruction_id", "candidate_definition", "family", "phase_space", "dynamics", "parameters",
    "parameter_provenance", "arithmetic_origin", "clock", "normalization", "determinant_convention",
    "orbit_cutoff", "precision", "training_data", "forbidden_data", "artifact_paths", "a0", "a1",
    "a2", "a3", "a4", "tuple", "overall_verdict", "route_b_invocation_allowed",
    "route_b_lock_reason", "scope_flags", "theorem_status", "finite_evidence_role", "source_owner_tokens",
}
EVAL_FIXED = {
    "schema": "route-a-evaluation-v0.2.0", "candidate_id": "HCS-C349",
    "title": "Neumann Uhlenbeck integrable sphere theorem", "evaluation_date": "2026-09-03",
    "source_commit": SOURCE, "fixed_epoch": EPOCH, "scope_literal": SCOPE,
    "evaluator_authority": "flow_systems/skills/route-a-evaluator.md",
    "evaluator_version": "0.2.0", "evaluator_authority_sha256": EVALUATOR,
    "obstruction_id": "HEN-O333",
    "candidate_definition": "the three-frequency classical Neumann oscillator on the round cotangent sphere with its Uhlenbeck integrals and rational Lax matrix",
    "family": "constrained integrable Hamiltonian mechanics on a compact sphere",
    "phase_space": "real cotangent bundle T-star S2 with the canonical constrained symplectic form",
    "dynamics": "x-dot equals p and p-dot equals minus A x plus (x-transpose A x minus norm-p-squared) x",
    "parameters": "three strictly ordered real oscillator coefficients; repeated coefficients are separately declared symmetry boundaries; the natural quantum boundary fixes hbar positive",
    "parameter_provenance": "source mechanical coefficients only, never target-fitted",
    "arithmetic_origin": "none", "clock": "source Hamiltonian time",
    "normalization": "unit sphere, unit mass, Hamiltonian one-half times kinetic plus quadratic potential",
    "determinant_convention": "only the source two-by-two Lax characteristic determinant is defined; no orbit Euler product or target determinant",
    "orbit_cutoff": "all-state analytic theorem; finite rational state rows are implementation receipts only",
    "precision": "exact rational identities and strict symbolic polynomial verification", "training_data": "none",
    "forbidden_data": "target arithmetic local data, Euler factors, root numbers, automorphy, target divisor or functional equation, target zeros, Hilbert-Polya operators, and Route B",
    "artifact_paths": ["results/c349_neumann_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"],
    "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
    "overall_verdict": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
    "route_b_lock_reason": "natural source quantization cannot repair the absent arithmetic carrier, primitive prime dictionary, or target determinant",
    "scope_flags": FLAGS, "theorem_status": "PROVABLE_AS_STATED",
    "finite_evidence_role": "exact convention, constraint, Uhlenbeck, Dirac-bracket, Lax-resolvent, equilibrium, coordinate-face, and symmetry-boundary receipt only; analytic arguments prove the continuum theorem",
    "source_owner_tokens": ["10.1515/crll.1859.56.46", "10.1007/978-1-4613-8109-9_7", "10.1515/crll.1982.334.69"],
}
GATES = {
    "a0": {"verdict": "A0_FAIL", "evidence_status": "PROVED",
           "strongest_evidence": "the mechanical Hamiltonian, Uhlenbeck integrals, and spectral coefficients are intrinsic source quantities",
           "strongest_failure": "no rational-prime, prime-power, logarithmic-prime, or arithmetic local carrier exists"},
    "a1": {"verdict": "A1_WEAK", "evidence_status": "PROVED",
           "strongest_evidence": "each connected regular compact fiber is a Liouville two-torus with an exact rational-frequency closure criterion",
           "strongest_failure": "periodic tori occur on continuously selected resonance loci rather than as an isolated arithmetic primitive ledger"},
    "a2": {"verdict": "A2_FAIL", "evidence_status": "STOP_SCOPED",
           "strongest_evidence": "the rational two-by-two Lax determinant and all three residues are exact",
           "strongest_failure": "no primitive-orbit Euler product, transfer operator, or arithmetic Fredholm determinant is constructed"},
    "a3": {"verdict": "A3_FAIL", "evidence_status": "STOP_SCOPED",
           "strongest_evidence": "the source integrability and declared degeneration atlas are analytic",
           "strongest_failure": "no target functional equation, divisor, counting law, continuation theorem, or Weil compression exists"},
    "a4": {"verdict": "A4_NATURAL_QUANTIZATION", "evidence_status": "PROVED",
           "strongest_evidence": "for hbar positive the compact sphere Hamiltonian quantizes canonically to a self-adjoint compact-resolvent Schrodinger operator on L2 S2 with domain H2 S2",
           "strongest_failure": "no closed anisotropic spectrum, target-zero match, same-clock arithmetic lift, or Hilbert-Polya interpretation is proved"},
}


def check_evaluation(raw, value):
    need(sha(raw) == EVAL_RAW, "evaluation raw hash")
    need(semantic_yaml_hash(value) == EVAL_SEMANTIC, "evaluation semantic hash")
    need(set(value) == EVAL_KEYS, "evaluation exact keys")
    for key, expected in EVAL_FIXED.items():
        need(value.get(key) == expected, f"evaluation fixed {key}")
    for key, expected in GATES.items():
        need(value.get(key) == expected, f"evaluation gate {key}")


def check_state_rows(rows):
    need(type(rows) is list and len(rows) == 60, "state row count")
    expected_coordinates = [(i, j) for i in range(10) for j in range(6)]
    for row, (parameter_index, sample_index) in zip(rows, expected_coordinates):
        need(type(row) is dict and set(row) == STATE_KEYS, "state exact keys")
        need(type(row["parameter_index"]) is int and type(row["sample_index"]) is int,
             "state integer coordinates")
        need((row["parameter_index"], row["sample_index"]) == (parameter_index, sample_index),
             "state coordinate/order")
        a = qlist(row["a"], 3, "a")
        need(tuple(a) == PARAMETERS[parameter_index] and a[0] < a[1] < a[2], "ordered a")
        x = qlist(row["x"], 3, "x")
        p = qlist(row["p"], 3, "p")
        u, v, seed = SAMPLES[sample_index]
        expected_x, expected_p = expected_state(u, v, seed)
        need(x == expected_x and p == expected_p, "rational state reconstruction")
        need(q(row["sphere_norm"]) == dot(x, x) == 1, "sphere constraint")
        need(q(row["tangent_dot"]) == dot(x, p) == 0, "tangent constraint")
        kinetic = dot(p, p)
        potential = sum((a[i]*x[i]**2 for i in range(3)), Q(0))
        energy = (kinetic+potential)/2
        alpha = potential-kinetic
        need(q(row["kinetic_norm"]) == kinetic, "kinetic")
        need(q(row["potential"]) == potential, "potential")
        need(q(row["energy"]) == energy, "energy")
        need(q(row["alpha"]) == alpha, "alpha")
        fs = uhlenbeck(a, x, p)
        need(qlist(row["F"], 3, "F") == fs, "Uhlenbeck values")
        need(q(row["sum_F"]) == sum(fs, Q(0)) == 1, "sum F")
        need(q(row["weighted_F"]) == sum((a[i]*fs[i] for i in range(3)), Q(0)) == 2*energy,
             "weighted F")
        need(qlist(row["F_dot"], 3, "F dot") == [Q(0)]*3, "F conservation")
        gradients = [derivative_vectors(a, x, p, i) for i in range(3)]
        brackets = [constrained_bracket(gradients[0], gradients[1], x, p),
                    constrained_bracket(gradients[0], gradients[2], x, p),
                    constrained_bracket(gradients[1], gradients[2], x, p)]
        need(qlist(row["dirac_pairs"], 3, "Dirac pairs") == brackets == [Q(0)]*3,
             "Dirac commutation")
        probes = row["lax_probes"]
        need(type(probes) is list and len(probes) == 2, "two Lax probes")
        for probe_index, probe in enumerate(probes):
            need(type(probe) is dict and set(probe) == PROBE_KEYS, "probe exact keys")
            parameter = a[2]+Q(probe_index+1)
            need(q(probe["lambda"]) == parameter, "probe lambda")
            inverse = [Q(1)/(parameter-a[i]) for i in range(3)]
            u_value = sum((x[i]**2*inverse[i] for i in range(3)), Q(0))
            v_value = sum((x[i]*p[i]*inverse[i] for i in range(3)), Q(0))
            w_value = 1+sum((p[i]**2*inverse[i] for i in range(3)), Q(0))
            pdot = [(alpha-a[i])*x[i] for i in range(3)]
            direct = [2*sum((x[i]*p[i]*inverse[i] for i in range(3)), Q(0)),
                      sum(((p[i]**2+x[i]*pdot[i])*inverse[i] for i in range(3)), Q(0)),
                      2*sum((p[i]*pdot[i]*inverse[i] for i in range(3)), Q(0))]
            lax = [2*v_value, w_value+(alpha-parameter)*u_value, 2*(alpha-parameter)*v_value]
            need(q(probe["U"]) == u_value and q(probe["V"]) == v_value and q(probe["W"]) == w_value,
                 "probe UVW")
            determinant = u_value*w_value-v_value**2
            residue = sum((fs[i]*inverse[i] for i in range(3)), Q(0))
            need(q(probe["determinant"]) == determinant == q(probe["residue_sum"]) == residue,
                 "resolvent determinant")
            need([q(probe["direct_U_dot"]), q(probe["direct_V_dot"]), q(probe["direct_W_dot"])] == direct,
                 "direct Lax derivatives")
            need([q(probe["lax_U_dot"]), q(probe["lax_V_dot"]), q(probe["lax_W_dot"])] == lax == direct,
                 "Lax commutator derivatives")


def check_equilibria(rows):
    need(type(rows) is list and len(rows) == 30, "equilibrium count")
    types = ["elliptic-elliptic", "saddle-center", "saddle-saddle"]
    for row, (parameter_index, axis) in zip(rows, [(i, j) for i in range(10) for j in range(3)]):
        need(type(row) is dict and set(row) == EQUILIBRIUM_KEYS, "equilibrium exact keys")
        a = PARAMETERS[parameter_index]
        need(row["parameter_index"] == parameter_index and row["axis"] == axis+1,
             "equilibrium coordinates")
        need(qlist(row["a"], 3, "equilibrium a") == list(a), "equilibrium a")
        expected = [a[j]-a[axis] for j in range(3) if j != axis]
        need(qlist(row["linear_frequency_squares"], 2, "linear squares") == expected,
             "linear squares")
        need(row["type"] == types[axis] and row["copies"] == 2, "equilibrium type")


def check_coordinates(rows):
    need(type(rows) is list and len(rows) == 30, "coordinate face count")
    for row, (parameter_index, missing) in zip(rows, [(i, j) for i in range(10) for j in range(3)]):
        need(type(row) is dict and set(row) == COORDINATE_KEYS, "coordinate exact keys")
        remain = [j for j in range(3) if j != missing]
        need(row["parameter_index"] == parameter_index and row["missing_axis"] == missing+1,
             "coordinate indices")
        need(row["remaining_axes"] == [j+1 for j in remain], "remaining axes")
        need(qlist(row["potential_coefficients"], 2, "face potential") ==
             [PARAMETERS[parameter_index][j] for j in remain], "face potential")
        need(row["equation"] == "theta_ddot=-(a_second-a_first)*sin(theta)*cos(theta)", "face equation")
        need(row["invariance_receipt"] == "x_i_dot=p_i=0 and p_i_dot=(-a_i+alpha)*x_i=0", "face invariance")


def simple_axis_integral(a, x, p, index):
    return x[index]**2+sum(
        (lij(x, p, index, j)**2/(a[index]-a[j])
         for j in range(3) if j != index), Q(0))


def angular_derivatives(x, p, i, j):
    dx = [Q(0), Q(0), Q(0)]
    dp = [Q(0), Q(0), Q(0)]
    dx[i], dx[j] = p[j], -p[i]
    dp[i], dp[j] = -x[j], x[i]
    return dx, dp


def apply_differential(gradient, direction_x, direction_p):
    return dot(gradient[0], direction_x)+dot(gradient[1], direction_p)


def check_repeated(rows):
    need(type(rows) is list and len(rows) == 6, "repeated count")
    expected = []
    for repeated_value, simple_value in ((Q(0), Q(3)), (Q(-2), Q(5))):
        for pair in ((0, 1), (0, 2), (1, 2)):
            simple = next(i for i in range(3) if i not in pair)
            a = [simple_value]*3
            a[pair[0]] = repeated_value
            a[pair[1]] = repeated_value
            expected.append((a, pair, simple))
    for row, (a, pair, simple) in zip(rows, expected):
        need(type(row) is dict and set(row) == REPEATED_KEYS, "repeated exact keys")
        need(qlist(row["a"], 3, "repeated a") == a, "repeated a")
        need(row["repeated_axes"] == [pair[0]+1, pair[1]+1] and row["simple_axis"] == simple+1,
             "repeated coordinates")
        need(row["noether_momentum"] == f"L_{pair[0]+1}{pair[1]+1}", "Noether label")
        need(row["momentum_derivative"] == "0" and row["symmetry"] == "SO(2)", "Noether conservation")
        first, second = pair
        need(row["commuting_pair"] == [f"J_{first+1}{second+1}", f"F_{simple+1}"],
             "repeated commuting-pair labels")
        need(row["energy_identity"] ==
             f"2H=a+J_{first+1}{second+1}^2+(b-a)*F_{simple+1}",
             "repeated energy identity label")
        witness = row["independence_witness"]
        need(type(witness) is dict and set(witness) == WITNESS_KEYS,
             "repeated witness exact keys")
        x = qlist(witness["x"], 3, "repeated witness x")
        p = qlist(witness["p"], 3, "repeated witness p")
        expected_x = [Q(0), Q(0), Q(0)]
        expected_p = [Q(0), Q(0), Q(0)]
        expected_x[first], expected_x[simple], expected_p[second] = Q(3, 5), Q(4, 5), Q(1)
        need(x == expected_x and p == expected_p, "repeated witness state")
        need(dot(x, x) == 1 and dot(x, p) == 0, "repeated witness constraints")
        directions = []
        for number in (1, 2):
            direction_x = qlist(witness[f"direction_{number}_x"], 3,
                                f"repeated direction {number} x")
            direction_p = qlist(witness[f"direction_{number}_p"], 3,
                                f"repeated direction {number} p")
            need(dot(x, direction_x) == 0 and
                 dot(x, direction_p)+dot(p, direction_x) == 0,
                 f"repeated tangent direction {number}")
            directions.append((direction_x, direction_p))
        j_gradient = angular_derivatives(x, p, first, second)
        f_gradient = derivative_vectors(a, x, p, simple)
        bracket = constrained_bracket(j_gradient, f_gradient, x, p)
        need(q(row["dirac_bracket"]) == bracket == 0, "repeated Dirac bracket")
        d_j = [apply_differential(j_gradient, *direction) for direction in directions]
        d_f = [apply_differential(f_gradient, *direction) for direction in directions]
        need(qlist(witness["dJ"], 2, "repeated dJ") == d_j, "repeated dJ values")
        need(qlist(witness["dF"], 2, "repeated dF") == d_f, "repeated dF values")
        wedge = d_j[0]*d_f[1]-d_j[1]*d_f[0]
        need(q(witness["wedge"]) == wedge and wedge != 0,
             "repeated independence wedge")
        j_value = lij(x, p, first, second)
        f_value = simple_axis_integral(a, x, p, simple)
        twice_energy = dot(p, p)+sum((a[i]*x[i]**2 for i in range(3)), Q(0))
        energy_rhs = a[first]+j_value**2+(a[simple]-a[first])*f_value
        need(q(row["energy_lhs"]) == twice_energy, "repeated energy lhs")
        need(q(row["energy_rhs"]) == energy_rhs == twice_energy,
             "repeated energy identity")
        need(row["uhlenbeck_boundary"] == "individual repeated-axis fractions are not evaluated",
             "singular fraction boundary")


def check_isotropic(rows):
    speeds = [Q(0), Q(1, 2), Q(1), Q(3, 2), Q(2)]
    need(type(rows) is list and len(rows) == len(speeds), "isotropic count")
    for row, speed in zip(rows, speeds):
        need(type(row) is dict and set(row) == ISOTROPIC_KEYS, "isotropic exact keys")
        need(q(row["speed"]) == speed and row["equation"] == "p_dot=-speed^2*x", "isotropic data")
        if speed == 0:
            need(row["class"] == "equilibrium_sphere" and row["least_period"] is None and
                 row["period_times_speed"] is None, "zero-speed isotropic")
        else:
            need(row["class"] == "great_circle" and
                 row["least_period"] == f"2*pi/({qstr(speed)})" and
                 row["period_times_speed"] == "2*pi", "great-circle period")


def qstr(value):
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def main():
    if sys.flags.optimize:
        raise RuntimeError("C349 checker refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=EVIDENCE)
    parser.add_argument("--evaluation", type=Path, default=EVALUATION)
    args = parser.parse_args()
    raw = args.evidence.read_bytes()
    data = json.loads(raw, object_pairs_hook=unique,
                      parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)))
    need(type(data) is dict and set(data) == TOP_KEYS, "evidence exact top keys")
    claimed = data["payload_sha256"]
    body = dict(data)
    body.pop("payload_sha256")
    computed = sha(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode())
    need(type(claimed) is str and claimed == computed, "payload hash")
    raw_yaml = args.evaluation.read_bytes()
    evaluation = parse_yaml(raw_yaml)
    check_evaluation(raw_yaml, evaluation)
    need((data["schema"], data["candidate_id"], data["obstruction_id"], data["evaluation_date"],
          data["source_commit"], data["fixed_epoch"], data["scope_literal"]) ==
         ("hcs-c349-neumann-uhlenbeck-v1", "HCS-C349", "HEN-O333", "2026-09-03",
          SOURCE, EPOCH, SCOPE), "identity")
    need(data["evaluator"] == {"authority": "flow_systems/skills/route-a-evaluator.md",
                                "version": "0.2.0", "sha256": EVALUATOR}, "evaluator")
    need(data["evaluation"] == {"path": "evaluations/route_a/HCS-C349/2026-09-03.yaml",
                                 "raw_sha256": EVAL_RAW, "semantic_sha256": EVAL_SEMANTIC}, "evaluation lock")
    need(data["model"] == MODEL and data["theorem_contract"] == THEOREM, "model and theorem")
    need(data["references"] == REFERENCES and data["collision_boundary"] == COLLISIONS, "source and collisions")
    need(data["nonclaims"] == NONCLAIMS and data["boundary_atlas"] == BOUNDARIES, "boundaries and nonclaims")
    need(data["route_a"] == {"tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
                              "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}, "Route A")
    need(data["scope_flags"] == FLAGS, "scope flags")
    expected_grid = {
        "ordered_triples": [[qstr(z) for z in row] for row in PARAMETERS],
        "rational_sphere_parameters": [[qstr(u), qstr(v)] for u, v, _ in SAMPLES],
        "tangent_seeds": [[qstr(z) for z in seed] for _, _, seed in SAMPLES],
        "lax_probes_per_state": 2, "evidence_role": "exact finite convention receipt, not proof by sampling",
    }
    need(data["parameter_grid"] == expected_grid, "parameter grid")
    check_state_rows(data["state_rows"])
    check_equilibria(data["equilibrium_rows"])
    check_coordinates(data["coordinate_face_rows"])
    check_repeated(data["repeated_spectrum_rows"])
    check_isotropic(data["isotropic_rows"])
    expected_enumeration = {
        "parameter_triples": 10, "state_rows": 60, "lax_probe_rows": 120,
        "equilibrium_rows": 30, "coordinate_face_rows": 30,
        "repeated_spectrum_rows": 6, "isotropic_rows": 5,
        "audited_leaf_count": leaves(body),
    }
    need(data["enumeration"] == expected_enumeration, "enumeration and leaves")
    print(f"C349 independent Neumann checker: PASS {CHECKS} assertions")


if __name__ == "__main__":
    main()
