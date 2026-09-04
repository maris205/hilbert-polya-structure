#!/usr/bin/env python3
"""Producer-independent strict checker for HCS-C354."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction as Q
from pathlib import Path

import yaml
from yaml.tokens import AliasToken, AnchorToken

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c354_lagrange_top_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C354/2026-09-03.yaml"
SOURCE = "140c8714b74de666d56f441ddfb712026955901a"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EVAL_RAW = "4af99b49987c3f29c85fb4e7caf7ba5c8881e45c36bbff20cb816c24478b403c"
EVAL_SEMANTIC = "e13efe34d72f2daa91dbd177462da782abbc44f4ed82a72fb4226b97a9781098"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600
CHECKS = 0

FLAGS = {
    "claims_target_arithmetic_local_data": False, "claims_target_euler_factors": False,
    "claims_root_number": False, "claims_automorphy": False,
    "claims_target_divisor_or_counting_law": False, "claims_target_functional_equation": False,
    "claims_target_zero_match": False, "claims_hilbert_polya_operator": False,
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
    (Q(1), Q(2), Q(1), Q(1), Q(0), Q(2)), (Q(1), Q(2), Q(1), Q(0), Q(1), Q(1)),
    (Q(2), Q(1), Q(3), Q(1), Q(2), Q(4)), (Q(3), Q(2), Q(1), Q(1), Q(-1), Q(2)),
    (Q(1), Q(2), Q(1), Q(1), Q(1), Q(1)), (Q(1), Q(1), Q(8), Q(3), Q(0), Q(2)),
    (Q(2), Q(3), Q(1), Q(1), Q(1), Q(2)), (Q(3), Q(5), Q(2), Q(2), Q(1), Q(3)),
    (Q(4), Q(3), Q(1), Q(-1), Q(2), Q(3)), (Q(2), Q(5), Q(4), Q(3), Q(-2), Q(5)),
    (Q(1), Q(4), Q(2), Q(0), Q(0), Q(0)), (Q(5), Q(2), Q(3), Q(2), Q(3), Q(6)),
]
PROBES = (Q(-3, 4), Q(-1, 3), Q(0), Q(2, 5), Q(4, 5))
ELLIPTIC = [
    (Q(1), Q(1), Q(-3, 4), Q(1, 4), Q(3, 2)),
    (Q(2), Q(3), Q(-2, 3), Q(1, 3), Q(5, 3)),
    (Q(3), Q(2), Q(-1, 2), Q(1, 2), Q(2)),
    (Q(5, 2), Q(4), Q(-4, 5), Q(1, 5), Q(6, 5)),
]

TOP_KEYS = {"schema", "candidate_id", "obstruction_id", "evaluation_date", "source_commit", "fixed_epoch", "scope_literal", "evaluator", "evaluation_lock", "model", "theorem_contract", "boundary_atlas", "references", "collision_boundary", "nonclaims", "route_a", "scope_flags", "parameter_grid", "parameter_rows", "elliptic_rows", "steady_and_pole_rows", "enumeration", "payload_sha256"}
PARAM_KEYS = {"index", "A", "C", "gamma", "L", "G", "E", "coefficients_low_to_high", "discriminant", "P_minus_one", "P_plus_one", "root_intervals", "probes"}
ROOT_KEYS = {"left", "right", "multiplicity"}
PROBE_KEYS = {"u", "P_polynomial", "P_energy", "effective_potential", "phi_dot", "psi_dot", "momentum_reconstruction", "spin_reconstruction"}
ELLIPTIC_KEYS = {"index", "A", "gamma", "r1", "r2", "r3", "gap", "outer_gap", "k_squared", "nu_squared", "period_prefactor_squared", "pi_characteristic_north", "pi_characteristic_south", "north_prefactor_squared", "south_prefactor_squared", "substitution_lhs", "substitution_rhs"}
STEADY_KEYS = {"kind", "u", "P", "P_prime", "P_second"}
POLE_KEYS = {"kind", "formula_value", "expected", "compatibility"}


def need(condition, label):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def unique(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError(f"duplicate JSON key: {key}")
        out[key] = value
    return out


class UniqueLoader(yaml.SafeLoader):
    pass


def construct_mapping(loader, node, deep=False):
    out = {}
    for kn, vn in node.value:
        key = loader.construct_object(kn, deep=deep)
        if type(key) is not str or key in out:
            raise ValueError("non-string or duplicate YAML key")
        out[key] = loader.construct_object(vn, deep=deep)
    return out


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_mapping)


def parse_yaml(raw):
    for token in yaml.scan(raw):
        if isinstance(token, (AliasToken, AnchorToken)):
            raise ValueError("YAML aliases forbidden")
    value = yaml.load(raw, Loader=UniqueLoader)
    if type(value) is not dict:
        raise ValueError("YAML root")
    return value


def q(value) -> Q:
    need(type(value) is str, "rational type")
    result = Q(value)
    canonical = str(result.numerator) if result.denominator == 1 else f"{result.numerator}/{result.denominator}"
    need(value == canonical, "canonical rational")
    return result


def leaves(value):
    if type(value) is dict:
        return sum(leaves(v) for v in value.values())
    if type(value) is list:
        return sum(leaves(v) for v in value)
    return 1


def coeffs(A, C, gamma, L, G, E):
    # Independent expansion through the effective-potential numerator.
    return (2*A*E-A*G*G/C-L*L, 2*(L*G-A*gamma), A*G*G/C-2*A*E-G*G, 2*A*gamma)


def peval(cs, x):
    out = Q(0)
    for c in reversed(cs):
        out = out*x+c
    return out


def disc(cs):
    d, c, b, a = cs
    return b*b*c*c-4*a*c**3-4*b**3*d-27*a*a*d*d+18*a*b*c*d


def poly_derivative(cs):
    return tuple(i*cs[i] for i in range(1, len(cs)))


def poly_trim(cs):
    cs = list(cs)
    while cs and cs[-1] == 0:
        cs.pop()
    return tuple(cs)


def poly_divrem(a, b):
    a, b = list(poly_trim(a)), poly_trim(b)
    if not b:
        raise ZeroDivisionError
    while len(a) >= len(b):
        factor = a[-1]/b[-1]
        shift = len(a)-len(b)
        for i, value in enumerate(b):
            a[i+shift] -= factor*value
        while a and a[-1] == 0:
            a.pop()
    return tuple(a)


def sturm(cs):
    seq = [poly_trim(cs), poly_trim(poly_derivative(cs))]
    while seq[-1]:
        rem = poly_divrem(seq[-2], seq[-1])
        if not rem:
            break
        seq.append(tuple(-v for v in rem))
    return seq


def variations(seq, x):
    signs = []
    for p in seq:
        value = peval(p, x)
        if value:
            signs.append(1 if value > 0 else -1)
    return sum(a != b for a, b in zip(signs, signs[1:]))


def root_count(seq, left, right):
    need(all(peval(p, left) != 0 for p in seq[:1]), "left endpoint root")
    need(all(peval(p, right) != 0 for p in seq[:1]), "right endpoint root")
    return variations(seq, left)-variations(seq, right)


def check_evaluation(raw):
    need(sha(raw) == EVAL_RAW, "evaluation raw hash")
    value = parse_yaml(raw)
    semantic = sha(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode())
    need(semantic == EVAL_SEMANTIC, "evaluation semantic hash")
    required = {"schema", "candidate_id", "title", "evaluation_date", "source_commit", "fixed_epoch", "scope_literal", "evaluator_authority", "evaluator_version", "evaluator_authority_sha256", "obstruction_id", "candidate_definition", "family", "phase_space", "dynamics", "parameters", "parameter_provenance", "arithmetic_origin", "clock", "normalization", "determinant_convention", "orbit_cutoff", "precision", "training_data", "forbidden_data", "artifact_paths", "a0", "a1", "a2", "a3", "a4", "tuple", "overall_verdict", "route_b_invocation_allowed", "route_b_lock_reason", "scope_flags", "theorem_status", "finite_evidence_role", "source_owner_tokens"}
    need(set(value) == required, "evaluation exact keys")
    need(value["candidate_id"] == "HCS-C354" and value["obstruction_id"] == "HEN-O338", "evaluation IDs")
    need(value["evaluation_date"] == "2026-09-03" and value["source_commit"] == SOURCE, "evaluation provenance")
    need(value["fixed_epoch"] == EPOCH and value["scope_literal"] == SCOPE, "evaluation epoch scope")
    need(value["evaluator_authority"] == "flow_systems/skills/route-a-evaluator.md" and value["evaluator_version"] == "0.2.0" and value["evaluator_authority_sha256"] == EVALUATOR, "evaluation authority")
    need(value["artifact_paths"] == ["results/c354_lagrange_top_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"], "evaluation paths")
    verdicts = ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"]
    statuses = ["PROVED", "PROVED", "STOP_SCOPED", "STOP_SCOPED", "PROVED"]
    for i, key in enumerate(("a0", "a1", "a2", "a3", "a4")):
        need(set(value[key]) == {"verdict", "evidence_status", "strongest_evidence", "strongest_failure"}, f"{key} keys")
        need(value[key]["verdict"] == verdicts[i] and value[key]["evidence_status"] == statuses[i], f"{key} lock")
    need(value["tuple"] == verdicts and value["overall_verdict"] == "ROUTE_A_REJECTED", "evaluation tuple")
    need(value["route_b_invocation_allowed"] is False and value["scope_flags"] == FLAGS, "evaluation firewall")
    need(value["theorem_status"] == "PROVABLE_AS_STATED", "theorem status")
    need(type(value["finite_evidence_role"]) is str and len(value["finite_evidence_role"]) > 80, "finite evidence role")
    need(value["source_owner_tokens"] == ["10.1007/978-3-0348-0918-4", "https://assets.cambridge.org/97805215/61297/excerpt/9780521561297_excerpt.pdf"], "source owners")


def check(path, evaluation):
    raw_eval = evaluation.read_bytes()
    check_evaluation(raw_eval)
    data = json.loads(path.read_text(), object_pairs_hook=unique,
                      parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)))
    need(set(data) == TOP_KEYS, "top keys")
    claimed = data["payload_sha256"]
    need(type(claimed) is str and len(claimed) == 64, "payload hash type")
    payload = dict(data); payload.pop("payload_sha256")
    computed = sha(json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode())
    need(claimed == computed, "payload hash")
    need(data["schema"] == "hcs-c354-lagrange-top-evidence-v1", "schema")
    need((data["candidate_id"], data["obstruction_id"], data["evaluation_date"]) == ("HCS-C354", "HEN-O338", "2026-09-03"), "identity")
    need(data["source_commit"] == SOURCE and data["fixed_epoch"] == EPOCH and data["scope_literal"] == SCOPE, "provenance")
    need(data["evaluator"] == {"authority": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR}, "evaluator")
    need(data["evaluation_lock"] == {"relative_path": "evaluations/route_a/HCS-C354/2026-09-03.yaml", "raw_sha256": EVAL_RAW, "semantic_sha256": EVAL_SEMANTIC}, "evaluation lock")
    need(data["model"] == MODEL and data["theorem_contract"] == THEOREM, "model theorem")
    need(data["boundary_atlas"] == BOUNDARIES and data["references"] == REFERENCES, "boundaries references")
    need(data["collision_boundary"] == COLLISIONS and data["nonclaims"] == NONCLAIMS, "collisions nonclaims")
    need(data["route_a"] == {"tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"], "overall": "ROUTE_A_REJECTED", "route_b": False}, "route a")
    need(data["scope_flags"] == FLAGS, "scope flags")
    need(data["parameter_grid"] == [[str(v.numerator) if v.denominator == 1 else f"{v.numerator}/{v.denominator}" for v in row] for row in PARAMETERS], "grid")
    rows = data["parameter_rows"]
    need(type(rows) is list and len(rows) == len(PARAMETERS), "parameter rows")
    root_total = 0
    for index, (row, values) in enumerate(zip(rows, PARAMETERS)):
        need(set(row) == PARAM_KEYS and row["index"] == index, "parameter row shape")
        A, C, gamma, L, G, E = values
        need([q(row[k]) for k in ("A", "C", "gamma", "L", "G", "E")] == list(values), "parameter values")
        cs = coeffs(*values)
        need([q(x) for x in row["coefficients_low_to_high"]] == list(cs), "coefficients")
        need(q(row["discriminant"]) == disc(cs), "discriminant")
        need(q(row["P_minus_one"]) == -(L+G)**2 and q(row["P_plus_one"]) == -(L-G)**2, "pole factors")
        intervals = row["root_intervals"]
        need(type(intervals) is list and 1 <= len(intervals) <= 3, "root interval list")
        seq = sturm(cs)
        prior = None
        multiplicity_total = 0
        for item in intervals:
            need(set(item) == ROOT_KEYS and type(item["multiplicity"]) is int, "root interval shape")
            left, right, mult = q(item["left"]), q(item["right"]), item["multiplicity"]
            need(left <= right and mult in (1, 2, 3), "root interval values")
            if prior is not None:
                need(prior < left, "root intervals disjoint")
            prior = right
            if left == right:
                need(peval(cs, left) == 0, "point root")
                deriv = cs
                actual = 0
                while deriv and peval(deriv, left) == 0:
                    actual += 1; deriv = poly_derivative(deriv)
                need(actual == mult, "point multiplicity")
            else:
                need(root_count(seq, left, right) == 1 and mult == 1, "isolating interval")
            multiplicity_total += mult
        need(multiplicity_total == 3, "complete cubic roots")
        root_total += len(intervals)
        probes = row["probes"]
        need(type(probes) is list and len(probes) == len(PROBES), "probe count")
        for probe, u in zip(probes, PROBES):
            need(set(probe) == PROBE_KEYS and q(probe["u"]) == u, "probe shape")
            effective = G*G/(2*C)+gamma*u+(L-G*u)**2/(2*A*(1-u*u))
            phi = (L-G*u)/(A*(1-u*u)); psi = G/C-u*phi
            need(q(probe["P_polynomial"]) == peval(cs, u), "probe polynomial")
            need(q(probe["P_energy"]) == 2*A*(1-u*u)*(E-effective), "probe energy")
            need(q(probe["effective_potential"]) == effective, "effective potential")
            need(q(probe["phi_dot"]) == phi and q(probe["psi_dot"]) == psi, "rates")
            need(q(probe["momentum_reconstruction"]) == L and q(probe["spin_reconstruction"]) == G, "momentum reconstruction")
    erows = data["elliptic_rows"]
    need(type(erows) is list and len(erows) == len(ELLIPTIC), "elliptic count")
    for index, (row, values) in enumerate(zip(erows, ELLIPTIC)):
        need(set(row) == ELLIPTIC_KEYS and row["index"] == index, "elliptic shape")
        A, gamma, r1, r2, r3 = values
        need([q(row[k]) for k in ("A", "gamma", "r1", "r2", "r3")] == list(values), "elliptic values")
        d, out = r2-r1, r3-r1; k2 = d/out; nu2 = gamma*out/(2*A)
        need(q(row["gap"]) == d and q(row["outer_gap"]) == out, "gaps")
        need(q(row["k_squared"]) == k2 and q(row["nu_squared"]) == nu2, "elliptic scales")
        need(q(row["period_prefactor_squared"]) == 8*A/(gamma*out), "period prefactor")
        need(q(row["pi_characteristic_north"]) == d/(1-r1) and q(row["pi_characteristic_south"]) == -d/(1+r1), "Pi chars")
        need(q(row["north_prefactor_squared"]) == 4/(2*A*gamma*out*(1-r1)**2), "north prefactor")
        need(q(row["south_prefactor_squared"]) == 4/(2*A*gamma*out*(1+r1)**2), "south prefactor")
        need([q(x) for x in row["substitution_lhs"]] == [q(x) for x in row["substitution_rhs"]], "Jacobi substitution")
    steady = data["steady_and_pole_rows"]
    need(type(steady) is list and len(steady) == 3, "steady count")
    need(set(steady[0]) == STEADY_KEYS and steady[0]["kind"] == "interior_double_root", "steady shape")
    need(q(steady[0]["u"]) == Q(-1, 2) and q(steady[0]["P"]) == 0 and q(steady[0]["P_prime"]) == 0 and q(steady[0]["P_second"]) != 0, "double root")
    for row, kind, compatibility in zip(steady[1:], ("north_pole", "south_pole"), ("L=G", "L=-G")):
        need(set(row) == POLE_KEYS and row["kind"] == kind and row["compatibility"] == compatibility, "pole row")
        need(q(row["formula_value"]) == 0 and q(row["expected"]) == 0, "pole zero")
    enum = data["enumeration"]
    need(set(enum) == {"parameter_rows", "probe_rows", "root_intervals", "elliptic_rows", "steady_and_pole_rows", "leaf_count_without_payload_hash"}, "enumeration keys")
    expected_enum = {"parameter_rows": len(PARAMETERS), "probe_rows": len(PARAMETERS)*len(PROBES), "root_intervals": root_total, "elliptic_rows": len(ELLIPTIC), "steady_and_pole_rows": 3, "leaf_count_without_payload_hash": leaves(payload)-6}
    need(enum == expected_enum, "enumeration exact")
    print(f"C354 independent Lagrange-top checker: PASS ({CHECKS} checks)")


def main():
    if sys.flags.optimize:
        raise RuntimeError("C354 checker refuses optimized Python")
    parser = argparse.ArgumentParser(); parser.add_argument("--evidence", type=Path, default=EVIDENCE); parser.add_argument("--evaluation", type=Path, default=EVALUATION)
    args = parser.parse_args(); check(args.evidence, args.evaluation)


if __name__ == "__main__":
    main()
