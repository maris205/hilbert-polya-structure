#!/usr/bin/env python3
"""Producer-independent strict checker for HCS-C359."""
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
EVIDENCE = ROOT / "results/c359_pais_uhlenbeck_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C359/2026-09-04.yaml"
SOURCE = "05ca5f96b2c69a6ad6ba153d1084df750d7722c0"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EVAL_RAW = "7e46f2ada7433620bf08d1e0fcfe0da43e48455985312c30cc474425aee61156"
EVAL_SEMANTIC = "a15b1abe7eb8b34cdaf979485a1bcace0cd14de24289b4ed3fee7ecc7b4c9f64"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788480000
CHECKS = 0

FLAGS = {
    "claims_target_arithmetic_local_data": False, "claims_target_euler_factors": False,
    "claims_root_number": False, "claims_automorphy": False,
    "claims_target_divisor_or_counting_law": False, "claims_target_functional_equation": False,
    "claims_target_zero_match": False, "claims_hilbert_polya_operator": False,
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
RATIONAL = [(Q(1), 1, 2), (Q(1), 2, 3), (Q(1), 3, 5), (Q(1, 2), 1, 3),
            (Q(2, 3), 2, 5), (Q(3, 2), 1, 4), (Q(2), 3, 7), (Q(5, 3), 4, 9)]
SUPPORTS = [(Q(0), Q(0)), (Q(1), Q(0)), (Q(0), Q(1)), (Q(1), Q(1)),
            (Q(1, 4), Q(9, 4)), (Q(2), Q(3)), (Q(5, 2), Q(7, 3)),
            (Q(9), Q(1, 9)), (Q(11, 5), Q(13, 7))]
IRRATIONAL = [(1, 2, "sqrt(1/2)"), (2, 3, "sqrt(2/3)"), (1, 5, "sqrt(1/5)")]

TOP_KEYS = {"schema", "candidate_id", "obstruction_id", "evaluation_date", "source_commit", "fixed_epoch", "scope_literal", "evaluator", "evaluation_lock", "model", "theorem_contract", "boundary_atlas", "references", "collision_boundary", "nonclaims", "route_a", "scope_flags", "rational_frequency_grid", "support_grid", "canonical_rows", "orbit_rows", "irrational_rows", "quantum_rows", "boundary_rows", "enumeration", "payload_sha256"}
CANONICAL_KEYS = {"frequency_index", "scale", "m", "n", "omega1", "omega2", "delta", "poisson_matrix", "mode1_energy_sign", "mode2_energy_sign", "characteristic_c2", "characteristic_c0", "common_period_over_2pi"}
ORBIT_KEYS = {"frequency_index", "support_index", "radius1_squared", "radius2_squared", "orbit_type", "periodic", "common_period_over_2pi", "phase1_turns", "phase2_turns"}
IRRATIONAL_KEYS = {"irrational_index", "omega1_squared", "omega2_squared", "ratio", "squarefree_distinct", "search_bound", "nonzero_integer_relation_found", "double_mode_closure", "double_mode_orbit", "quantum_eigenvalues"}
QUANTUM_KEYS = {"frequency_index", "n1", "n2", "lattice_coordinate", "energy", "energy_over_scale"}
BOUNDARY_KEYS = {"face", "factorization", "solution_basis", "generic_growth", "bounded_entire_subspace", "periodic_subspace", "quantum_claimed"}


def need(condition, label):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def unique(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError("duplicate JSON key")
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
            raise ValueError("YAML alias or anchor")
    value = yaml.load(raw, Loader=UniqueLoader)
    if type(value) is not dict:
        raise ValueError("YAML root")
    return value


def q(value):
    need(type(value) is str, "rational type")
    try:
        out = Q(value)
    except Exception as exc:
        raise AssertionError("invalid rational") from exc
    canonical = str(out.numerator) if out.denominator == 1 else f"{out.numerator}/{out.denominator}"
    need(value == canonical, "canonical rational")
    return out


def qstr(value):
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def leaves(value):
    if type(value) is dict:
        return sum(leaves(v) for v in value.values())
    if type(value) is list:
        return sum(leaves(v) for v in value)
    return 1


def check_evaluation(raw):
    need(sha(raw) == EVAL_RAW, "evaluation raw")
    value = parse_yaml(raw)
    semantic = sha(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode())
    need(semantic == EVAL_SEMANTIC, "evaluation semantic")
    keys = {"schema", "candidate_id", "title", "evaluation_date", "source_commit", "fixed_epoch", "scope_literal", "evaluator_authority", "evaluator_version", "evaluator_authority_sha256", "obstruction_id", "candidate_definition", "family", "phase_space", "dynamics", "parameters", "parameter_provenance", "arithmetic_origin", "clock", "normalization", "determinant_convention", "orbit_cutoff", "precision", "training_data", "forbidden_data", "artifact_paths", "a0", "a1", "a2", "a3", "a4", "tuple", "overall_verdict", "route_b_invocation_allowed", "route_b_lock_reason", "scope_flags", "theorem_status", "finite_evidence_role", "source_owner_tokens"}
    need(set(value) == keys, "evaluation keys")
    need((value["schema"], value["candidate_id"], value["obstruction_id"], value["evaluation_date"]) == ("route-a-evaluation-v0.2.0", "HCS-C359", "HEN-O343", "2026-09-04"), "evaluation identity")
    need(value["source_commit"] == SOURCE and value["fixed_epoch"] == EPOCH and value["scope_literal"] == SCOPE, "evaluation provenance")
    need(value["evaluator_authority"] == "flow_systems/skills/route-a-evaluator.md" and value["evaluator_version"] == "0.2.0" and value["evaluator_authority_sha256"] == EVALUATOR, "evaluation authority")
    need(value["artifact_paths"] == ["results/c359_pais_uhlenbeck_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"], "artifact paths")
    verdicts = ["A0_FAIL", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"]
    statuses = ["PROVED", "PROVED", "STOP_SCOPED", "STOP_SCOPED", "PROVED"]
    for i, key in enumerate(("a0", "a1", "a2", "a3", "a4")):
        need(set(value[key]) == {"verdict", "evidence_status", "strongest_evidence", "strongest_failure"}, f"{key} keys")
        need(value[key]["verdict"] == verdicts[i] and value[key]["evidence_status"] == statuses[i], f"{key} lock")
        need(type(value[key]["strongest_evidence"]) is str and type(value[key]["strongest_failure"]) is str, f"{key} prose")
    need(value["tuple"] == verdicts and value["overall_verdict"] == "ROUTE_A_REJECTED", "evaluation tuple")
    need(value["route_b_invocation_allowed"] is False and value["scope_flags"] == FLAGS, "evaluation firewall")
    need(value["theorem_status"] == "PROVABLE_AS_STATED" and len(value["finite_evidence_role"]) > 100, "evaluation status")
    need(value["source_owner_tokens"] == ["10.1103/PhysRev.79.145", "10.1016/j.nuclphysb.2004.10.037", "https://arxiv.org/abs/quant-ph/0501024"], "evaluation sources")


def check(path, evaluation):
    check_evaluation(evaluation.read_bytes())
    data = json.loads(path.read_text(), object_pairs_hook=unique,
                      parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)))
    need(set(data) == TOP_KEYS, "top keys")
    claimed = data["payload_sha256"]
    need(type(claimed) is str and len(claimed) == 64, "payload hash type")
    payload = dict(data); payload.pop("payload_sha256")
    need(claimed == sha(json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()), "payload hash")
    need(data["schema"] == "hcs-c359-pais-uhlenbeck-evidence-v1", "schema")
    need((data["candidate_id"], data["obstruction_id"], data["evaluation_date"]) == ("HCS-C359", "HEN-O343", "2026-09-04"), "identity")
    need(data["source_commit"] == SOURCE and data["fixed_epoch"] == EPOCH and data["scope_literal"] == SCOPE, "provenance")
    need(data["evaluator"] == {"authority": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR}, "evaluator")
    need(data["evaluation_lock"] == {"relative_path": "evaluations/route_a/HCS-C359/2026-09-04.yaml", "raw_sha256": EVAL_RAW, "semantic_sha256": EVAL_SEMANTIC}, "evaluation lock")
    need(data["model"] == MODEL and data["theorem_contract"] == THEOREM, "model theorem")
    need(data["boundary_atlas"] == BOUNDARIES and data["references"] == REFERENCES, "boundaries refs")
    need(data["collision_boundary"] == COLLISIONS and data["nonclaims"] == NONCLAIMS, "collisions nonclaims")
    route = {"tuple": ["A0_FAIL", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"], "overall": "ROUTE_A_REJECTED", "route_b": False}
    need(data["route_a"] == route and data["scope_flags"] == FLAGS, "route firewall")
    need(data["rational_frequency_grid"] == [[qstr(g), m, n] for g, m, n in RATIONAL], "rational grid")
    need(data["support_grid"] == [[qstr(a), qstr(b)] for a, b in SUPPORTS], "support grid")

    crows = data["canonical_rows"]
    need(type(crows) is list and len(crows) == len(RATIONAL), "canonical count")
    coords = []
    J4 = [["0", "1", "0", "0"], ["-1", "0", "0", "0"], ["0", "0", "0", "1"], ["0", "0", "-1", "0"]]
    for row in crows:
        need(set(row) == CANONICAL_KEYS, "canonical keys")
        i = row["frequency_index"]; need(type(i) is int and 0 <= i < len(RATIONAL), "canonical coordinate")
        coords.append(i); g, m, n = RATIONAL[i]; w1, w2 = g*m, g*n
        need(q(row["scale"]) == g and row["m"] == m and row["n"] == n, "canonical frequency labels")
        need(q(row["omega1"]) == w1 and q(row["omega2"]) == w2 and q(row["delta"]) == w2*w2-w1*w1, "canonical frequencies")
        need(row["poisson_matrix"] == J4 and row["mode1_energy_sign"] == -1 and row["mode2_energy_sign"] == 1, "canonical signs")
        need(q(row["characteristic_c2"]) == w1*w1+w2*w2 and q(row["characteristic_c0"]) == w1*w1*w2*w2, "characteristic")
        need(q(row["common_period_over_2pi"]) == 1/g, "common period")
    need(coords == list(range(len(RATIONAL))), "canonical enumeration")

    orows = data["orbit_rows"]
    need(type(orows) is list and len(orows) == len(RATIONAL)*len(SUPPORTS), "orbit count")
    ocoords = []
    for row in orows:
        need(set(row) == ORBIT_KEYS, "orbit keys")
        fi, si = row["frequency_index"], row["support_index"]
        need(type(fi) is int and type(si) is int and 0 <= fi < len(RATIONAL) and 0 <= si < len(SUPPORTS), "orbit coordinate")
        ocoords.append((fi, si)); g, m, n = RATIONAL[fi]; r1, r2 = SUPPORTS[si]
        expected_kind = "equilibrium" if r1 == r2 == 0 else ("single_mode" if r1 == 0 or r2 == 0 else "double_mode_resonant")
        need(q(row["radius1_squared"]) == r1 and q(row["radius2_squared"]) == r2, "orbit radii")
        need(row["orbit_type"] == expected_kind and row["periodic"] is True, "orbit type")
        need(q(row["common_period_over_2pi"]) == 1/g and row["phase1_turns"] == m and row["phase2_turns"] == n, "orbit closure")
    need(ocoords == [(i, j) for i in range(len(RATIONAL)) for j in range(len(SUPPORTS))], "orbit enumeration")

    irows = data["irrational_rows"]
    need(type(irows) is list and len(irows) == len(IRRATIONAL), "irrational count")
    for index, (row, expected) in enumerate(zip(irows, IRRATIONAL)):
        need(set(row) == IRRATIONAL_KEYS and row["irrational_index"] == index, "irrational keys coordinate")
        a, b, label = expected
        need((row["omega1_squared"], row["omega2_squared"], row["ratio"]) == (str(a), str(b), label), "irrational parameters")
        relation = any(u*u*b == v*v*a for u in range(1, 65) for v in range(1, 65))
        need(row["squarefree_distinct"] is True and row["search_bound"] == 64 and row["nonzero_integer_relation_found"] is relation is False, "irrational receipt")
        need(row["double_mode_closure"] is False and row["double_mode_orbit"] == "dense_two_torus", "irrational classical")
        need(row["quantum_eigenvalues"] == "simple_dense_pure_point_spectrum_R", "irrational quantum")

    qrows = data["quantum_rows"]
    need(type(qrows) is list and len(qrows) == len(RATIONAL)*16*16, "quantum count")
    qcoords = []
    for row in qrows:
        need(set(row) == QUANTUM_KEYS, "quantum keys")
        fi, n1, n2 = row["frequency_index"], row["n1"], row["n2"]
        need(type(fi) is int and type(n1) is int and type(n2) is int and 0 <= fi < len(RATIONAL) and 0 <= n1 < 16 and 0 <= n2 < 16, "quantum coordinate")
        qcoords.append((fi, n1, n2)); g, m, n = RATIONAL[fi]
        k = n*n2-m*n1; normalized = Q(k)+Q(n-m, 2)
        need(row["lattice_coordinate"] == k and q(row["energy_over_scale"]) == normalized, "quantum lattice")
        need(q(row["energy"]) == g*normalized, "quantum energy")
    need(qcoords == [(i, a, b) for i in range(len(RATIONAL)) for a in range(16) for b in range(16)], "quantum enumeration")

    expected_boundaries = [
        ("equal_positive", "(D^2+omega^2)^2", ["cos", "sin", "t*cos", "t*sin"], "linear", "span(cos,sin)", "span(cos,sin)"),
        ("one_zero", "D^2*(D^2+omega^2)", ["1", "t", "cos", "sin"], "linear", "span(1,cos,sin)", "span(1,cos,sin)"),
        ("double_zero", "D^4", ["1", "t", "t^2", "t^3"], "cubic", "span(1)", "span(1)"),
        ("one_negative", "(D^2-nu^2)*(D^2+omega^2)", ["exp_plus", "exp_minus", "cos", "sin"], "exponential", "span(cos,sin)", "span(cos,sin)"),
        ("negative_zero", "(D^2-nu^2)*D^2", ["exp_plus", "exp_minus", "1", "t"], "exponential", "span(1)", "span(1)"),
        ("double_negative", "(D^2-nu1^2)*(D^2-nu2^2)", ["exp_nu1_plus", "exp_nu1_minus", "exp_nu2_plus", "exp_nu2_minus"], "exponential", "{0}", "{0}"),
        ("equal_negative", "(D^2-nu^2)^2", ["exp_plus", "t*exp_plus", "exp_minus", "t*exp_minus"], "linear_times_exponential", "{0}", "{0}"),
    ]
    brows = data["boundary_rows"]
    need(type(brows) is list and len(brows) == len(expected_boundaries), "boundary count")
    for row, expected in zip(brows, expected_boundaries):
        need(set(row) == BOUNDARY_KEYS, "boundary keys")
        need((row["face"], row["factorization"], row["solution_basis"], row["generic_growth"]) == expected[:4], "boundary row")
        need((row["bounded_entire_subspace"], row["periodic_subspace"]) == expected[4:], "boundary invariant subspaces")
        need(row["quantum_claimed"] is False, "boundary quantum stop")

    enum = data["enumeration"]
    need(set(enum) == {"rational_frequencies", "supports", "canonical_rows", "orbit_rows", "irrational_rows", "quantum_rows", "boundary_rows", "leaf_count_without_payload_hash"}, "enumeration keys")
    expected_enum = {"rational_frequencies": len(RATIONAL), "supports": len(SUPPORTS), "canonical_rows": len(crows), "orbit_rows": len(orows), "irrational_rows": len(irows), "quantum_rows": len(qrows), "boundary_rows": len(brows), "leaf_count_without_payload_hash": leaves(payload)-8}
    need(enum == expected_enum, "enumeration")
    print(f"C359 independent Pais--Uhlenbeck checker: PASS ({CHECKS} checks)")


def main():
    if sys.flags.optimize:
        raise RuntimeError("C359 checker refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=EVIDENCE)
    parser.add_argument("--evaluation", type=Path, default=EVALUATION)
    args = parser.parse_args()
    check(args.evidence, args.evaluation)


if __name__ == "__main__":
    main()
