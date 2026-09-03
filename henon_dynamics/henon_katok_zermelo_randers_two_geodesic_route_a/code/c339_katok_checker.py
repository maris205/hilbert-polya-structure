#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C339."""
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
DEFAULT_EVIDENCE = ROOT / "results/c339_katok_evidence.json"
DEFAULT_EVALUATION = ROOT / "evaluations/route_a/HCS-C339/2026-09-03.yaml"
SOURCE = "e2d94f886963cbe3d42b83f6ef542413a163d3a4"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EVAL_RAW = "606a3a70932613ca8a42d2c964707a2788ed612c2ade624f490b51eeaacca9b0"
EVAL_SEMANTIC = "1e772f9884eb5e25af36001683ded882c1737115cc5e7129515c369b518cf83a"
EXPECTED_PAYLOAD = "08773e07bb695a3cbaaac43968480efdc0e96bfdd770a1cc550b928771cf3a64"
EXPECTED_TOP = {
    "boundary_atlas", "candidate_id", "collision_boundary", "enumeration",
    "evaluation_date", "evaluator", "fixed_epoch", "irrational_fixtures",
    "model", "nonclaims", "obstruction_id", "payload_sha256", "rational_resonance_rows",
    "references", "route_a", "route_a_yaml", "schema", "scope_flags", "scope_literal",
    "source_commit", "theorem_contract", "universal_symbolic_receipts",
}
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


def duplicate_pairs(pairs):
    result = {}
    for key, value in pairs:
        if type(key) is not str or key in result:
            raise ValueError("duplicate or non-string JSON key")
        result[key] = value
    return result


def strict_json(path: Path):
    data = json.loads(path.read_text(), object_pairs_hook=duplicate_pairs,
                      parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)))
    if type(data) is not dict:
        raise TypeError("JSON root must be a mapping")
    return data


class StrictLoader(yaml.SafeLoader):
    pass


StrictLoader.yaml_implicit_resolvers = {
    key: [(tag, regex) for tag, regex in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def strict_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in result:
            raise ValueError("duplicate or non-string YAML key")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, strict_mapping)


def strict_yaml(path: Path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchors and aliases forbidden")
    value = yaml.load(raw, Loader=StrictLoader)
    if type(value) is not dict:
        raise TypeError("YAML root must be a mapping")
    return raw, value


def payload_hash(data) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def semantic_hash(data) -> str:
    raw = json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def fraction(text) -> Fraction:
    if type(text) is not str:
        raise TypeError("rational receipt must be a string")
    value = Fraction(text)
    canonical = str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"
    if text != canonical:
        raise ValueError(f"noncanonical rational {text}")
    return value


def leaf_count(value) -> int:
    if type(value) is dict:
        return sum(leaf_count(child) for child in value.values())
    if type(value) is list:
        return sum(leaf_count(child) for child in value)
    return 1


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def expected_rational_coordinates():
    return [(p, q) for q in range(2, 17) for p in range(-q + 1, q)
            if p != 0 and math.gcd(abs(p), q) == 1]


def main():
    if sys.flags.optimize:
        raise RuntimeError("C339 checker refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_EVALUATION)
    args = parser.parse_args()
    data = strict_json(args.evidence)
    yaml_raw, evaluation = strict_yaml(args.evaluation)
    checks = 0

    require(set(data) == EXPECTED_TOP, "evidence top-level schema mismatch"); checks += len(EXPECTED_TOP)
    require(payload_hash(data) == data["payload_sha256"], "stale payload hash"); checks += 1
    require(data["payload_sha256"] == EXPECTED_PAYLOAD, "unexpected repaired evidence payload"); checks += 1
    require(hashlib.sha256(yaml_raw.encode()).hexdigest() == EVAL_RAW, "evaluation raw digest mismatch"); checks += 1
    require(semantic_hash(evaluation) == EVAL_SEMANTIC, "evaluation semantic digest mismatch"); checks += 1
    require(data["route_a_yaml"] == {
        "relative_path": "evaluations/route_a/HCS-C339/2026-09-03.yaml",
        "raw_sha256": EVAL_RAW, "semantic_sha256": EVAL_SEMANTIC}, "YAML evidence lock mismatch"); checks += 3
    require(evaluation["candidate_id"] == "HCS-C339" and evaluation["obstruction_id"] == "HEN-O323", "evaluation owner mismatch"); checks += 2
    require(evaluation["source_commit"] == SOURCE and evaluation["fixed_epoch"] == 1788393600, "evaluation provenance mismatch"); checks += 2
    require(evaluation["evaluator_authority"] == "flow_systems/skills/route-a-evaluator.md", "evaluator authority mismatch"); checks += 1
    require(evaluation["evaluator_authority_sha256"] == EVALUATOR and evaluation["evaluator_version"] == "0.2.0", "evaluator identity mismatch"); checks += 2
    require(evaluation["artifact_paths"] == ["results/c339_katok_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"], "artifact path schema mismatch"); checks += 3
    expected_tuple = ["A0_FAIL", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
    require(evaluation["tuple"] == expected_tuple and data["route_a"]["tuple"] == expected_tuple, "Route-A tuple mismatch"); checks += 10
    for index, key in enumerate(("a0", "a1", "a2", "a3", "a4")):
        require(evaluation[key]["verdict"] == expected_tuple[index], f"{key} verdict mismatch"); checks += 1
        require(set(evaluation[key]) == {"verdict", "evidence_status", "strongest_evidence", "strongest_failure"}, f"{key} schema mismatch"); checks += 4
    require(evaluation["overall_verdict"] == "ROUTE_A_REJECTED" and evaluation["route_b_invocation_allowed"] is False, "Route-A release decision mismatch"); checks += 2
    require(evaluation["scope_flags"] == FLAGS and data["scope_flags"] == FLAGS, "scope firewall mismatch"); checks += 18
    require(data["source_commit"] == SOURCE and data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "evidence provenance mismatch"); checks += 2
    require(data["theorem_contract"]["exclusion"] == "in SO(3), return means R_z(epsilon*T)=g*R_z(-T)*g^{-1}; the axes e3 and g*e3 are distinct off the equators, so closure forces T=2*pi*m and epsilon*T=2*pi*n, impossible for irrational epsilon", "SO(3) exclusion theorem drift"); checks += 1

    coordinates = expected_rational_coordinates()
    rows = data["rational_resonance_rows"]
    require(len(rows) == len(coordinates) == 158, "rational grid size mismatch"); checks += 2
    expected_keys = {"p", "q", "epsilon", "strong_convexity_margin",
                     "positive_equator_period_over_2pi", "negative_equator_period_over_2pi",
                     "generic_common_return_over_2pi", "round_turns_at_common_return",
                     "wind_turns_at_common_return", "positive_equator_degenerate",
                     "negative_equator_degenerate"}
    for row, (p, q) in zip(rows, coordinates):
        require(set(row) == expected_keys, "rational row schema mismatch"); checks += len(expected_keys)
        require((row["p"], row["q"]) == (p, q), "rational coordinate mismatch"); checks += 2
        epsilon = Fraction(p, q)
        plus = 1 / (1 + epsilon)
        minus = 1 / (1 - epsilon)
        require(fraction(row["epsilon"]) == epsilon, "epsilon mismatch"); checks += 1
        require(fraction(row["strong_convexity_margin"]) == 1 - epsilon * epsilon > 0, "convexity mismatch"); checks += 2
        require(fraction(row["positive_equator_period_over_2pi"]) == plus, "positive period mismatch"); checks += 1
        require(fraction(row["negative_equator_period_over_2pi"]) == minus, "negative period mismatch"); checks += 1
        require(row["generic_common_return_over_2pi"] == q, "common return mismatch"); checks += 1
        require(row["round_turns_at_common_return"] == q and row["wind_turns_at_common_return"] == p, "turn ledger mismatch"); checks += 2
        require(row["positive_equator_degenerate"] is (plus.denominator == 1), "positive degeneracy mismatch"); checks += 1
        require(row["negative_equator_degenerate"] is (minus.denominator == 1), "negative degeneracy mismatch"); checks += 1
        require(epsilon * q == p, "closure relation mismatch"); checks += 1

    fixtures = data["irrational_fixtures"]
    require(fixtures == [
        {"epsilon": "sqrt(2)/4", "minimal_polynomial": "8*x^2-1", "closure_verdict": "equators_only"},
        {"epsilon": "sqrt(3)/5", "minimal_polynomial": "25*x^2-3", "closure_verdict": "equators_only"},
        {"epsilon": "(sqrt(5)-1)/4", "minimal_polynomial": "4*x^2+2*x-1", "closure_verdict": "equators_only"},
    ], "irrational fixture mismatch"); checks += 9
    for discriminant in (32, 300, 20):
        require(math.isqrt(discriminant) ** 2 != discriminant, "fixture accidentally rational"); checks += 1
    monodromy = data["universal_symbolic_receipts"]
    require(monodromy["transverse_monodromy"] == [["cos(T)", "sin(T)"], ["-sin(T)", "cos(T)"]], "monodromy convention mismatch"); checks += 4
    require(monodromy["determinant_I_minus_P"] == "2-2*cos(T)" and monodromy["half_angle_form"] == "4*sin(T/2)^2", "determinant identity text mismatch"); checks += 2
    require(monodromy["so3_return_equation"] == "R_z(epsilon*T)=g*R_z(-T)*g^{-1}", "SO(3) return equation mismatch"); checks += 1
    require(monodromy["rotation_axes"] == "the left rotation has axis e3 and the conjugated right rotation has axis g*e3; these unoriented axes differ exactly off the equatorial frames", "SO(3) rotation-axis mismatch"); checks += 1
    require(data["enumeration"] == {"rational_rows": 158, "irrational_fixtures": 3, "q_max": 16, "audited_leaf_count": 1830}, "enumeration mismatch"); checks += 4
    require(leaf_count({key: value for key, value in data.items() if key != "payload_sha256"}) == 1830, "audited leaf count mismatch"); checks += 1
    print(f"C339 independent Katok checker: PASS {checks} checks")


if __name__ == "__main__":
    main()
