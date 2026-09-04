#!/usr/bin/env python3
"""Independent exact checker for HCS-C360; imports no producer code."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c360_berger_ricci_evidence.json"
DEFAULT_YAML = ROOT / "evaluations/route_a/HCS-C360/2026-09-04.yaml"
SOURCE = "05ca5f96b2c69a6ad6ba153d1084df750d7722c0"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
YAML_RAW = "a0ee441fab9c1753e2e028cebeb07e98ba6cfa0a5d417e29e0180e88bbd28602"
YAML_SEMANTIC = "b03caa045dcca6b16cdc649567cc66e5341c481f9dc078b1641992163eebfb58"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
METRICS = (("1", "1/4"), ("1", "1/2"), ("1", "1"), ("1", "4/3"),
           ("1", "2"), ("1", "4"), ("2", "1"), ("2", "2"),
           ("2", "8/3"), ("3", "1"), ("3", "4"), ("4", "16"))
SQUASHED = (("1", "1/4"), ("1", "1/2"), ("1", "3/4"),
            ("2", "1/4"), ("2", "1/2"), ("2", "3/4"))
STRETCHED = (("1", "1/4"), ("1", "1/2"), ("1", "1"), ("1", "2"),
             ("2", "1/4"), ("2", "1/2"), ("2", "1"), ("2", "2"))
TOP_KEYS = {"schema", "candidate_id", "obstruction_id", "evaluation_date",
            "source_commit", "fixed_epoch", "scope_literal", "evaluator",
            "route_a_yaml", "model", "theorem_contract", "collision_boundary",
            "nonclaims", "references", "curvature_rows", "ratio_rows",
            "lifespan_rows", "normalized_rows", "boundary_rows", "section_hashes",
            "enumeration", "route_a", "scope_flags", "payload_sha256"}
YAML_KEYS = {"schema", "candidate_id", "title", "evaluation_date", "source_commit",
             "fixed_epoch", "scope_literal", "evaluator_authority", "evaluator_version",
             "evaluator_authority_sha256", "obstruction_id", "candidate_definition",
             "family", "phase_space", "dynamics", "parameters", "parameter_provenance",
             "arithmetic_origin", "clock", "normalization", "determinant_convention",
             "orbit_cutoff", "precision", "training_data", "forbidden_data",
             "artifact_paths", "a0", "a1", "a2", "a3", "a4", "tuple",
             "overall_verdict", "route_b_invocation_allowed", "route_b_lock_reason",
             "scope_flags", "theorem_status", "finite_evidence_role", "source_owner_tokens"}
FALSE_FLAGS = {"claims_target_arithmetic_local_data", "claims_target_euler_factors",
               "claims_root_number", "claims_automorphy",
               "claims_target_divisor_or_counting_law",
               "claims_target_functional_equation", "claims_target_zero_match",
               "claims_hilbert_polya_operator", "invokes_route_b"}
MODEL = {
    "metric": "g=A(sigma_1^2+sigma_2^2)+C sigma_3^2",
    "maurer_cartan": "d sigma_1=2 sigma_2 wedge sigma_3 cyclically",
    "unnormalized_flow": ["A'=-8+4C/A", "C'=-4C^2/A^2"],
    "ratio": "r=C/A", "positive_cone": "A>0,C>0",
}
THEOREM = {
    "curvature": "Ricci and all sectional curvatures are explicit rational functions of A and C",
    "first_integral": "C/sqrt(abs(1-C/A)) is constant away from the round ray",
    "extinction": "every positive metric has finite forward Type-I extinction with A,C asymptotic to 4(T-t), (T-t)R tending to 3/2, and r tending to one",
    "maximal_intervals": "squashed and round solutions are ancient; stretched solutions have a finite anisotropic backward endpoint",
    "lifespans": "atanh and atan primitives give exact forward and backward endpoint times",
    "normalized": "volume-normalized flow is forward complete, preserves A^2 C, and converges to the unique round metric of that volume",
    "boundaries": "curvature walls, round ray, degenerate faces, and compatible finite quotients are explicit",
}
COLLISIONS = {
    "C247": "normalized surface Ricci flow, not the three-dimensional Berger cone",
    "C301": "homogeneous mean-curvature dynamics, not intrinsic Ricci flow",
    "C328": "Bianchi cosmology uses Lorentzian Einstein evolution, not Riemannian Ricci flow",
    "C354": "Euler heavy-top flow is Hamiltonian and elliptic, not a metric extinction equation",
}
NONCLAIMS = [
    "no classification of arbitrary left-invariant SU(2) metrics with three unequal axes",
    "no surgery or weak continuation through extinction",
    "no spectral convergence theorem for Laplace eigenvalues",
    "no target arithmetic local data, Euler factors, root number, automorphy, target divisor, functional equation, target-zero match, Hilbert-Polya operator, or Route B",
]
REFERENCES = [
    {"identifier": "DOI:10.4310/jdg/1214436922", "role": "Ricci-flow foundation and three-manifold context"},
    {"identifier": "DOI:10.4310/jdg/1214448265", "role": "homogeneous Ricci-flow context"},
]
BOUNDARIES = [
    {"boundary": "r=1", "classification": "round ray; exact ancient shrinker A=C=A0-4t"},
    {"boundary": "r=4/3", "classification": "horizontal sectional-curvature sign wall K12=0"},
    {"boundary": "r=2", "classification": "horizontal Ricci-curvature sign wall Ric11=Ric22=0"},
    {"boundary": "r=4", "classification": "scalar-curvature sign wall R=0"},
    {"boundary": "C=0", "classification": "degenerate non-Riemannian face; excluded from the metric theorem"},
    {"boundary": "A=0", "classification": "singular reduced equation; excluded from the metric theorem"},
    {"boundary": "finite left quotient", "classification": "local formulas descend whenever the left-invariant metric descends"},
]


def pairs(items):
    result = {}
    for key, value in items:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


class StrictLoader(yaml.SafeLoader):
    pass


StrictLoader.yaml_implicit_resolvers = {
    key: [(tag, regex) for tag, regex in values
          if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def strict_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("merge key")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in result:
            raise ValueError("duplicate/non-string YAML key")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
                             strict_mapping)


def load_yaml(path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("anchors forbidden")
    value = yaml.load(raw, Loader=StrictLoader)
    if type(value) is not dict:
        raise TypeError("YAML root")
    return value


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False).encode()


def s(value):
    value = F(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def decimal(value):
    return format(value, ".17g")


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def expected_curvatures():
    answer = []
    for aa, cc in METRICS:
        A, C = F(aa), F(cc)
        r = C/A
        Ad, Cd, rd = -8+4*r, -4*r*r, 8*r*(1-r)/A
        answer.append({"A": s(A), "C": s(C), "r": s(r),
                       "ricci_horizontal": s(4/A-2*C/A**2),
                       "ricci_vertical": s(2*C/A**2),
                       "sectional_horizontal": s((4*A-3*C)/A**2),
                       "sectional_mixed": s(C/A**2),
                       "scalar_curvature": s((8*A-2*C)/A**2),
                       "A_dot": s(Ad), "C_dot": s(Cd), "r_dot": s(rd),
                       "log_volume_dot": s(Ad/A+Cd/(2*C)),
                       "minus_scalar": s(-(8*A-2*C)/A**2)})
    return answer


def expected_ratios():
    answer = []
    for kk, uu in SQUASHED:
        k, u = F(kk), F(uu)
        r, A, C = 1-u*u, k*u/(1-u*u), k*u
        Ad, Cd, rd = -8+4*r, -4*r*r, 8*r*(1-r)/A
        answer.append({"chamber": "squashed", "k": s(k), "chart": s(u),
                       "A": s(A), "C": s(C), "r": s(r), "A_dot": s(Ad),
                       "C_dot": s(Cd), "r_dot": s(rd),
                       "first_integral_squared": s(C*C/(1-r)),
                       "first_integral_squared_dot": s(2*C*Cd/(1-r)+C*C*rd/(1-r)**2)})
    for kk, vv in STRETCHED:
        k, v = F(kk), F(vv)
        r, A, C = 1+v*v, k*v/(1+v*v), k*v
        Ad, Cd, rd = -8+4*r, -4*r*r, 8*r*(1-r)/A
        answer.append({"chamber": "stretched", "k": s(k), "chart": s(v),
                       "A": s(A), "C": s(C), "r": s(r), "A_dot": s(Ad),
                       "C_dot": s(Cd), "r_dot": s(rd),
                       "first_integral_squared": s(C*C/(r-1)),
                       "first_integral_squared_dot": s(2*C*Cd/(r-1)-C*C*rd/(r-1)**2)})
    return answer


def expected_lifespans():
    answer = []
    for kk, uu in SQUASHED:
        k, u = F(kk), F(uu)
        p = float(u/(1-u*u))+math.atanh(float(u))
        answer.append({"chamber": "squashed", "k": s(k), "chart": s(u),
                       "forward_lifespan": decimal(float(k)*p/8),
                       "backward_lifespan": "infinite",
                       "primitive_derivative_identity": "2/(1-u^2)^2"})
    for kk, vv in STRETCHED:
        k, v = F(kk), F(vv)
        p = float(v/(1+v*v))+math.atan(float(v))
        answer.append({"chamber": "stretched", "k": s(k), "chart": s(v),
                       "forward_lifespan": decimal(float(k)*p/8),
                       "backward_lifespan": decimal(float(k)*(math.pi/2-p)/8),
                       "primitive_derivative_identity": "2/(1+v^2)^2"})
    for aa in ("1/2", "1", "2", "5"):
        A = F(aa)
        answer.append({"chamber": "round", "A": s(A), "C": s(A),
                       "forward_lifespan": s(A/4), "backward_lifespan": "infinite",
                       "solution": "A(t)=C(t)=A0-4t"})
    return answer


def expected_normalized():
    answer = []
    for aa, cc in METRICS:
        A, C = F(aa), F(cc)
        r = C/A
        Ad, Cd = F(8,3)*(r-1), F(16,3)*r*(1-r)
        answer.append({"A": s(A), "C": s(C), "r": s(r),
                       "A_dot_normalized": s(Ad), "C_dot_normalized": s(Cd),
                       "r_dot_normalized": s(8*r*(1-r)/A),
                       "volume_squared": s(A*A*C),
                       "volume_squared_dot": s(2*A*Ad*C+A*A*Cd),
                       "rounding_sign": "up" if r < 1 else ("fixed" if r == 1 else "down")})
    return answer


def check(path, evaluation):
    count = 0
    data = json.loads(path.read_text(), object_pairs_hook=pairs,
                      parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)))
    if type(data) is not dict or set(data) != TOP_KEYS:
        raise AssertionError("evidence top-level schema")
    body = dict(data)
    claimed = body.pop("payload_sha256")
    if claimed != hashlib.sha256(canonical(body)).hexdigest():
        raise AssertionError("payload hash")
    count += 2
    identity = (data["schema"], data["candidate_id"], data["obstruction_id"],
                data["evaluation_date"], data["source_commit"], data["fixed_epoch"],
                data["scope_literal"])
    if identity != ("hcs-c360-berger-ricci-evidence-v1", "HCS-C360", "HEN-O344",
                    "2026-09-04", SOURCE, 1788480000, SCOPE):
        raise AssertionError("identity")
    count += 7
    if data["evaluator"] != {"authority": "flow_systems/skills/route-a-evaluator.md",
                             "version": "0.2.0", "sha256": EVALUATOR}:
        raise AssertionError("evaluator")
    if data["route_a_yaml"] != {"relative_path": "evaluations/route_a/HCS-C360/2026-09-04.yaml",
                                 "raw_sha256": YAML_RAW, "semantic_sha256": YAML_SEMANTIC}:
        raise AssertionError("yaml receipt")
    count += 2
    raw = evaluation.read_bytes()
    yml = load_yaml(evaluation)
    if hashlib.sha256(raw).hexdigest() != YAML_RAW or hashlib.sha256(canonical(yml)).hexdigest() != YAML_SEMANTIC:
        raise AssertionError("evaluation digest")
    if set(yml) != YAML_KEYS:
        raise AssertionError("evaluation keys")
    if (yml["schema"], yml["candidate_id"], yml["obstruction_id"], yml["evaluation_date"],
            yml["source_commit"], yml["fixed_epoch"], yml["scope_literal"]) != (
            "route-a-evaluation-v0.2.0", "HCS-C360", "HEN-O344", "2026-09-04",
            SOURCE, 1788480000, SCOPE):
        raise AssertionError("evaluation identity")
    if yml["tuple"] != ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"]:
        raise AssertionError("evaluation tuple")
    if yml["overall_verdict"] != "ROUTE_A_REJECTED" or yml["route_b_invocation_allowed"] is not False:
        raise AssertionError("evaluation verdict")
    if set(yml["scope_flags"]) != FALSE_FLAGS or any(yml["scope_flags"].values()):
        raise AssertionError("evaluation flags")
    if yml["artifact_paths"] != ["results/c360_berger_ricci_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"]:
        raise AssertionError("evaluation artifacts")
    count += 7
    if data["model"] != MODEL or data["theorem_contract"] != THEOREM:
        raise AssertionError("model/theorem")
    if data["collision_boundary"] != COLLISIONS or data["nonclaims"] != NONCLAIMS or data["references"] != REFERENCES:
        raise AssertionError("fixed narrative fields")
    count += 5
    sections = {"curvature_rows": expected_curvatures(), "ratio_rows": expected_ratios(),
                "lifespan_rows": expected_lifespans(), "normalized_rows": expected_normalized(),
                "boundary_rows": BOUNDARIES}
    for name, expected in sections.items():
        if data[name] != expected:
            raise AssertionError(name)
        if data["section_hashes"].get(name) != digest(expected):
            raise AssertionError(name+" hash")
        count += len(expected)+1
    if set(data["section_hashes"]) != set(sections):
        raise AssertionError("section hash keys")
    expected_counts = {name: len(value) for name, value in sections.items()}
    expected_counts["finite_evidence_proves_global_theorem"] = False
    if data["enumeration"] != expected_counts:
        raise AssertionError("enumeration")
    if data["route_a"] != {"tuple": ["A0_FAIL"]*0 + ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
                            "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}:
        raise AssertionError("route A")
    if set(data["scope_flags"]) != FALSE_FLAGS or any(data["scope_flags"].values()):
        raise AssertionError("scope flags")
    count += 4
    return count


def main():
    if sys.flags.optimize:
        raise RuntimeError("C360 checker refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_YAML)
    args = parser.parse_args()
    print(f"C360 independent checker: PASS {check(args.evidence, args.evaluation)} checks")


if __name__ == "__main__":
    main()
