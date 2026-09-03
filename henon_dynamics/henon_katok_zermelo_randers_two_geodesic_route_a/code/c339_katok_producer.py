#!/usr/bin/env python3
"""Deterministic exact evidence producer for HCS-C339."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c339_katok_evidence.json"
DEFAULT_EVALUATION = ROOT / "evaluations/route_a/HCS-C339/2026-09-03.yaml"
SOURCE = "e2d94f886963cbe3d42b83f6ef542413a163d3a4"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
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


class UniqueLoader(yaml.SafeLoader):
    pass


UniqueLoader.yaml_implicit_resolvers = {
    key: [(tag, regex) for tag, regex in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in result:
            raise ValueError("duplicate or non-string YAML key")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def strict_yaml(path: Path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchors and aliases forbidden")
    value = yaml.load(raw, Loader=UniqueLoader)
    if type(value) is not dict:
        raise TypeError("YAML root must be a mapping")
    return raw, value


def canonical(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def semantic_sha(value) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def leaf_count(value) -> int:
    if type(value) is dict:
        return sum(leaf_count(child) for child in value.values())
    if type(value) is list:
        return sum(leaf_count(child) for child in value)
    return 1


def rational_rows():
    rows = []
    for q in range(2, 17):
        for p in range(-q + 1, q):
            if p == 0 or math.gcd(abs(p), q) != 1:
                continue
            epsilon = Fraction(p, q)
            plus = Fraction(1, 1) / (1 + epsilon)
            minus = Fraction(1, 1) / (1 - epsilon)
            rows.append({
                "p": p,
                "q": q,
                "epsilon": canonical(epsilon),
                "strong_convexity_margin": canonical(1 - epsilon * epsilon),
                "positive_equator_period_over_2pi": canonical(plus),
                "negative_equator_period_over_2pi": canonical(minus),
                "generic_common_return_over_2pi": q,
                "round_turns_at_common_return": q,
                "wind_turns_at_common_return": p,
                "positive_equator_degenerate": plus.denominator == 1,
                "negative_equator_degenerate": minus.denominator == 1,
            })
    return rows


def build(evaluation_path: Path):
    yaml_raw, evaluation = strict_yaml(evaluation_path)
    if evaluation.get("candidate_id") != "HCS-C339":
        raise AssertionError("wrong evaluation candidate")
    if evaluation.get("source_commit") != SOURCE or evaluation.get("scope_literal") != SCOPE:
        raise AssertionError("evaluation provenance mismatch")
    if evaluation.get("evaluator_authority_sha256") != EVALUATOR:
        raise AssertionError("evaluator digest mismatch")
    rows = rational_rows()
    evidence = {
        "schema": "hcs-c339-katok-evidence-v1",
        "candidate_id": "HCS-C339",
        "obstruction_id": "HEN-O323",
        "evaluation_date": "2026-09-03",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {
            "authority": "flow_systems/skills/route-a-evaluator.md",
            "version": "0.2.0",
            "sha256": EVALUATOR,
        },
        "route_a_yaml": {
            "relative_path": "evaluations/route_a/HCS-C339/2026-09-03.yaml",
            "raw_sha256": hashlib.sha256(yaml_raw.encode()).hexdigest(),
            "semantic_sha256": semantic_sha(evaluation),
        },
        "model": {
            "background": "unit round S2 with sectional curvature one and longitude period 2*pi",
            "wind": "W=epsilon*partial_phi with abs(epsilon)<1",
            "navigation_rule": "gamma_F(t)=Phi_t^W(rho(t)) for every unit round great circle rho",
            "orientation": "oriented Randers geodesics; the metric is nonreversible when epsilon is nonzero",
            "clock": "Randers unit-speed time",
        },
        "theorem_contract": {
            "irrational_ledger": "if epsilon is irrational, exactly two oriented prime closed geodesics exist",
            "prime_periods": "T_plus=2*pi/(1+epsilon) and T_minus=2*pi/(1-epsilon)",
            "exclusion": "in SO(3), return means R_z(epsilon*T)=g*R_z(-T)*g^{-1}; the axes e3 and g*e3 are distinct off the equators, so closure forces T=2*pi*m and epsilon*T=2*pi*n, impossible for irrational epsilon",
            "curvature": "the navigation Randers metric has constant flag curvature one",
            "jacobi": "in the canonical transverse Jacobi trivialization P(T) has characteristic polynomial z^2-2*cos(T)*z+1",
            "poincare_determinant": "det(I-P(T))=2-2*cos(T)=4*sin(T/2)^2",
            "nondegeneracy": "both irrational-wind equators are nondegenerate because T_plus/(2*pi) and T_minus/(2*pi) are irrational",
            "rational_face": "for reduced epsilon=p/q every non-equatorial geodesic returns by time 2*pi*q; special invariant circles may have shorter least period",
            "boundaries": "epsilon=0 is round Zoll; sign reversal swaps orientations; abs(epsilon)=1 loses strong convexity",
        },
        "universal_symbolic_receipts": {
            "transverse_monodromy": [["cos(T)", "sin(T)"], ["-sin(T)", "cos(T)"]],
            "characteristic_polynomial": "z^2-2*cos(T)*z+1",
            "determinant_I_minus_P": "2-2*cos(T)",
            "half_angle_form": "4*sin(T/2)^2",
            "so3_return_equation": "R_z(epsilon*T)=g*R_z(-T)*g^{-1}",
            "rotation_axes": "the left rotation has axis e3 and the conjugated right rotation has axis g*e3; these unoriented axes differ exactly off the equatorial frames",
            "generic_closure_equations": ["T=2*pi*m", "epsilon*T=2*pi*n", "m,n in Z"],
        },
        "irrational_fixtures": [
            {"epsilon": "sqrt(2)/4", "minimal_polynomial": "8*x^2-1", "closure_verdict": "equators_only"},
            {"epsilon": "sqrt(3)/5", "minimal_polynomial": "25*x^2-3", "closure_verdict": "equators_only"},
            {"epsilon": "(sqrt(5)-1)/4", "minimal_polynomial": "4*x^2+2*x-1", "closure_verdict": "equators_only"},
        ],
        "rational_resonance_rows": rows,
        "boundary_atlas": {
            "zero_wind": "epsilon=0 gives the reversible round Zoll sphere and a continuum of period-2*pi great circles",
            "rational_wind": "reduced p/q gives global return at 2*pi*q, without claiming this is every least period",
            "wind_sign": "epsilon maps to -epsilon by longitude reflection and swaps the two oriented equators",
            "convexity_wall": "abs(epsilon)=1 is excluded because the navigation indicatrix ceases to be strongly convex globally",
            "outside_wall": "abs(epsilon)>1 is not a Randers metric on all of S2",
        },
        "collision_boundary": {
            "C242": "irrational ellipsoid Reeb flow has two simple Reeb orbits but is not a Randers geodesic flow",
            "C289": "charged spherical magnetic flow uses a Lorentz force rather than Zermelo navigation",
            "C305": "constant-wind Euclidean navigation is a control-value problem without compact closed-geodesic classification",
            "C313": "the round sphere is a reversible clean Zoll family, not an irrational two-orbit Randers metric",
            "C331": "Dirac-monopole magnetic dynamics and bundle spectrum are not Katok navigation",
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": dict(FLAGS),
        "nonclaims": [
            "no rational prime or prime-power owner is assigned",
            "no target Euler factor, root number, automorphy, divisor, or functional equation is claimed",
            "no target zero match or Hilbert-Polya operator is claimed",
            "the Poincare determinant is source-local and is not a target Fredholm determinant",
            "finite rational rows do not prove the irrational all-period classification",
        ],
        "references": [
            {"author": "A. B. Katok", "identifier": "DOI:10.1070/IM1973v007n03ABEH001958", "role": "original integrable perturbation owner"},
            {"author": "W. Ziller", "identifier": "DOI:10.1017/S0143385700001851", "role": "geometry and closed-geodesic owner for Katok examples"},
            {"author": "D. Bao, C. Robles, and Z. Shen", "identifier": "DOI:10.4310/jdg/1098137838", "role": "Zermelo-navigation and flag-curvature theorem owner"},
        ],
        "enumeration": {
            "rational_rows": len(rows),
            "irrational_fixtures": 3,
            "q_max": 16,
            "audited_leaf_count": 0,
        },
    }
    evidence["enumeration"]["audited_leaf_count"] = leaf_count(evidence)
    digest = semantic_sha(evidence)
    evidence["payload_sha256"] = digest
    return evidence


def main():
    if sys.flags.optimize:
        raise RuntimeError("C339 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_EVALUATION)
    args = parser.parse_args()
    evidence = build(args.evaluation)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(evidence, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(f"C339_PRODUCER_PASS {len(evidence['rational_resonance_rows'])} rational rows {evidence['payload_sha256']}")


if __name__ == "__main__":
    main()
