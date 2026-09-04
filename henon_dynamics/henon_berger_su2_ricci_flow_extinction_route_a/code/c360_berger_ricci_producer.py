#!/usr/bin/env python3
"""Canonical finite-evidence producer for the HCS-C360 Berger-flow atlas."""
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
DEFAULT_OUTPUT = ROOT / "results/c360_berger_ricci_evidence.json"
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


def strict_yaml(path: Path):
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
    return (str(value.numerator) if value.denominator == 1
            else f"{value.numerator}/{value.denominator}")


def decimal(value: float) -> str:
    return format(value, ".17g")


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def flow(A, C):
    r = C / A
    return -8 + 4 * r, -4 * r * r, 8 * r * (1 - r) / A


def curvature_rows():
    rows = []
    for raw_A, raw_C in METRICS:
        A, C = F(raw_A), F(raw_C)
        r = C / A
        Ad, Cd, rd = flow(A, C)
        rows.append({
            "A": s(A), "C": s(C), "r": s(r),
            "ricci_horizontal": s(4/A - 2*C/A**2),
            "ricci_vertical": s(2*C/A**2),
            "sectional_horizontal": s((4*A - 3*C)/A**2),
            "sectional_mixed": s(C/A**2),
            "scalar_curvature": s((8*A - 2*C)/A**2),
            "A_dot": s(Ad), "C_dot": s(Cd), "r_dot": s(rd),
            "log_volume_dot": s(Ad/A + Cd/(2*C)),
            "minus_scalar": s(-(8*A - 2*C)/A**2),
        })
    return rows


def ratio_rows():
    rows = []
    for raw_k, raw_u in SQUASHED:
        k, u = F(raw_k), F(raw_u)
        r = 1-u*u
        A, C = k*u/r, k*u
        Ad, Cd, rd = flow(A, C)
        dJ2 = 2*C*Cd/(1-r) + C*C*rd/(1-r)**2
        rows.append({"chamber": "squashed", "k": s(k), "chart": s(u),
                     "A": s(A), "C": s(C), "r": s(r),
                     "A_dot": s(Ad), "C_dot": s(Cd), "r_dot": s(rd),
                     "first_integral_squared": s(C*C/(1-r)),
                     "first_integral_squared_dot": s(dJ2)})
    for raw_k, raw_v in STRETCHED:
        k, v = F(raw_k), F(raw_v)
        r = 1+v*v
        A, C = k*v/r, k*v
        Ad, Cd, rd = flow(A, C)
        dJ2 = 2*C*Cd/(r-1) - C*C*rd/(r-1)**2
        rows.append({"chamber": "stretched", "k": s(k), "chart": s(v),
                     "A": s(A), "C": s(C), "r": s(r),
                     "A_dot": s(Ad), "C_dot": s(Cd), "r_dot": s(rd),
                     "first_integral_squared": s(C*C/(r-1)),
                     "first_integral_squared_dot": s(dJ2)})
    return rows


def lifespan_rows():
    rows = []
    for raw_k, raw_u in SQUASHED:
        k, u = F(raw_k), F(raw_u)
        primitive = float(u/(1-u*u)) + math.atanh(float(u))
        rows.append({"chamber": "squashed", "k": s(k), "chart": s(u),
                     "forward_lifespan": decimal(float(k)*primitive/8),
                     "backward_lifespan": "infinite",
                     "primitive_derivative_identity": "2/(1-u^2)^2"})
    for raw_k, raw_v in STRETCHED:
        k, v = F(raw_k), F(raw_v)
        primitive = float(v/(1+v*v)) + math.atan(float(v))
        rows.append({"chamber": "stretched", "k": s(k), "chart": s(v),
                     "forward_lifespan": decimal(float(k)*primitive/8),
                     "backward_lifespan": decimal(float(k)*(math.pi/2-primitive)/8),
                     "primitive_derivative_identity": "2/(1+v^2)^2"})
    for raw_A in ("1/2", "1", "2", "5"):
        A = F(raw_A)
        rows.append({"chamber": "round", "A": s(A), "C": s(A),
                     "forward_lifespan": s(A/4), "backward_lifespan": "infinite",
                     "solution": "A(t)=C(t)=A0-4t"})
    return rows


def normalized_rows():
    rows = []
    for raw_A, raw_C in METRICS:
        A, C = F(raw_A), F(raw_C)
        r = C/A
        Ad = F(8, 3)*(r-1)
        Cd = F(16, 3)*r*(1-r)
        rd = 8*r*(1-r)/A
        rows.append({"A": s(A), "C": s(C), "r": s(r),
                     "A_dot_normalized": s(Ad), "C_dot_normalized": s(Cd),
                     "r_dot_normalized": s(rd),
                     "volume_squared": s(A*A*C),
                     "volume_squared_dot": s(2*A*Ad*C+A*A*Cd),
                     "rounding_sign": "up" if r < 1 else ("fixed" if r == 1 else "down")})
    return rows


def boundary_rows():
    return [
        {"boundary": "r=1", "classification": "round ray; exact ancient shrinker A=C=A0-4t"},
        {"boundary": "r=4/3", "classification": "horizontal sectional-curvature sign wall K12=0"},
        {"boundary": "r=2", "classification": "horizontal Ricci-curvature sign wall Ric11=Ric22=0"},
        {"boundary": "r=4", "classification": "scalar-curvature sign wall R=0"},
        {"boundary": "C=0", "classification": "degenerate non-Riemannian face; excluded from the metric theorem"},
        {"boundary": "A=0", "classification": "singular reduced equation; excluded from the metric theorem"},
        {"boundary": "finite left quotient", "classification": "local formulas descend whenever the left-invariant metric descends"},
    ]


def build(evaluation: Path):
    raw = evaluation.read_bytes()
    semantic = strict_yaml(evaluation)
    if hashlib.sha256(raw).hexdigest() != YAML_RAW:
        raise AssertionError("evaluation raw hash")
    if hashlib.sha256(canonical(semantic)).hexdigest() != YAML_SEMANTIC:
        raise AssertionError("evaluation semantic hash")
    curvatures = curvature_rows()
    ratios = ratio_rows()
    lifespans = lifespan_rows()
    normalized = normalized_rows()
    boundaries = boundary_rows()
    body = {
        "schema": "hcs-c360-berger-ricci-evidence-v1",
        "candidate_id": "HCS-C360", "obstruction_id": "HEN-O344",
        "evaluation_date": "2026-09-04", "source_commit": SOURCE,
        "fixed_epoch": 1788480000, "scope_literal": SCOPE,
        "evaluator": {"authority": "flow_systems/skills/route-a-evaluator.md",
                      "version": "0.2.0", "sha256": EVALUATOR},
        "route_a_yaml": {"relative_path": "evaluations/route_a/HCS-C360/2026-09-04.yaml",
                         "raw_sha256": YAML_RAW, "semantic_sha256": YAML_SEMANTIC},
        "model": {
            "metric": "g=A(sigma_1^2+sigma_2^2)+C sigma_3^2",
            "maurer_cartan": "d sigma_1=2 sigma_2 wedge sigma_3 cyclically",
            "unnormalized_flow": ["A'=-8+4C/A", "C'=-4C^2/A^2"],
            "ratio": "r=C/A", "positive_cone": "A>0,C>0",
        },
        "theorem_contract": {
            "curvature": "Ricci and all sectional curvatures are explicit rational functions of A and C",
            "first_integral": "C/sqrt(abs(1-C/A)) is constant away from the round ray",
            "extinction": "every positive metric has finite forward Type-I extinction with A,C asymptotic to 4(T-t), (T-t)R tending to 3/2, and r tending to one",
            "maximal_intervals": "squashed and round solutions are ancient; stretched solutions have a finite anisotropic backward endpoint",
            "lifespans": "atanh and atan primitives give exact forward and backward endpoint times",
            "normalized": "volume-normalized flow is forward complete, preserves A^2 C, and converges to the unique round metric of that volume",
            "boundaries": "curvature walls, round ray, degenerate faces, and compatible finite quotients are explicit",
        },
        "collision_boundary": {
            "C247": "normalized surface Ricci flow, not the three-dimensional Berger cone",
            "C301": "homogeneous mean-curvature dynamics, not intrinsic Ricci flow",
            "C328": "Bianchi cosmology uses Lorentzian Einstein evolution, not Riemannian Ricci flow",
            "C354": "Euler heavy-top flow is Hamiltonian and elliptic, not a metric extinction equation",
        },
        "nonclaims": [
            "no classification of arbitrary left-invariant SU(2) metrics with three unequal axes",
            "no surgery or weak continuation through extinction",
            "no spectral convergence theorem for Laplace eigenvalues",
            "no target arithmetic local data, Euler factors, root number, automorphy, target divisor, functional equation, target-zero match, Hilbert-Polya operator, or Route B",
        ],
        "references": [
            {"identifier": "DOI:10.4310/jdg/1214436922", "role": "Ricci-flow foundation and three-manifold context"},
            {"identifier": "DOI:10.4310/jdg/1214448265", "role": "homogeneous Ricci-flow context"},
        ],
        "curvature_rows": curvatures, "ratio_rows": ratios,
        "lifespan_rows": lifespans, "normalized_rows": normalized,
        "boundary_rows": boundaries,
        "section_hashes": {name: digest(value) for name, value in (
            ("curvature_rows", curvatures), ("ratio_rows", ratios),
            ("lifespan_rows", lifespans), ("normalized_rows", normalized),
            ("boundary_rows", boundaries))},
        "enumeration": {"curvature_rows": len(curvatures), "ratio_rows": len(ratios),
                        "lifespan_rows": len(lifespans), "normalized_rows": len(normalized),
                        "boundary_rows": len(boundaries),
                        "finite_evidence_proves_global_theorem": False},
        "route_a": {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
                    "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False},
        "scope_flags": {"claims_target_arithmetic_local_data": False,
                        "claims_target_euler_factors": False,
                        "claims_root_number": False, "claims_automorphy": False,
                        "claims_target_divisor_or_counting_law": False,
                        "claims_target_functional_equation": False,
                        "claims_target_zero_match": False,
                        "claims_hilbert_polya_operator": False,
                        "invokes_route_b": False},
    }
    body["payload_sha256"] = hashlib.sha256(canonical(body)).hexdigest()
    return body


def main():
    if sys.flags.optimize:
        raise RuntimeError("C360 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_YAML)
    args = parser.parse_args()
    data = build(args.evaluation)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False)+"\n")
    print(f"C360 producer: PASS {data['payload_sha256']}")


if __name__ == "__main__":
    main()
