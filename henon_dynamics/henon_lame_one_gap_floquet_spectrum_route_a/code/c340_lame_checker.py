#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C340."""
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
DEFAULT_EVIDENCE = ROOT / "results/c340_lame_evidence.json"
DEFAULT_EVALUATION = ROOT / "evaluations/route_a/HCS-C340/2026-09-03.yaml"
SOURCE = "e2d94f886963cbe3d42b83f6ef542413a163d3a4"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EVAL_RAW = "f6149419b1d37a0f59783ee126eb44af0f5f431830cc1aa0ff3a1e6bec2e1ae1"
EVAL_SEMANTIC = "25b3b7d6519637670c59ef0def0de5463e6655a4bd22fbfa3f8a3b184cf7eccb"
EXPECTED_PAYLOAD = "e517efba41783977fc073ec0d05680d8916c3d4dddfd7b086bc5e6608846687c"
EXPECTED_TOP = {
    "boundary_atlas", "candidate_id", "collision_boundary", "enumeration", "evaluation_date",
    "evaluator", "fixed_epoch", "model", "nonclaims", "obstruction_id", "payload_sha256",
    "rational_modulus_rows", "references", "route_a", "route_a_yaml", "schema", "scope_flags",
    "scope_literal", "source_commit", "theorem_contract", "universal_symbolic_receipts",
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


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def payload_hash(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    return digest(body)


def fraction(text):
    if type(text) is not str:
        raise TypeError("rational receipt must be a string")
    value = Fraction(text)
    canonical = str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"
    if text != canonical:
        raise ValueError(f"noncanonical rational {text}")
    return value


def leaf_count(value):
    if type(value) is dict:
        return sum(leaf_count(child) for child in value.values())
    if type(value) is list:
        return sum(leaf_count(child) for child in value)
    return 1


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def coordinates():
    return [(p, q) for q in range(2, 26) for p in range(1, q) if math.gcd(p, q) == 1]


def polynomial_value(coefficients, energy):
    value = Fraction(0)
    for coefficient in coefficients:
        value = value * energy + coefficient
    return value


def main():
    if sys.flags.optimize:
        raise RuntimeError("C340 checker refuses optimized Python")
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
    require(digest(evaluation) == EVAL_SEMANTIC, "evaluation semantic digest mismatch"); checks += 1
    require(data["route_a_yaml"] == {"relative_path": "evaluations/route_a/HCS-C340/2026-09-03.yaml", "raw_sha256": EVAL_RAW, "semantic_sha256": EVAL_SEMANTIC}, "YAML lock mismatch"); checks += 3
    require(evaluation["candidate_id"] == "HCS-C340" and evaluation["obstruction_id"] == "HEN-O324", "owner mismatch"); checks += 2
    require(evaluation["source_commit"] == SOURCE and evaluation["fixed_epoch"] == 1788393600, "provenance mismatch"); checks += 2
    require(evaluation["evaluator_authority"] == "flow_systems/skills/route-a-evaluator.md", "authority mismatch"); checks += 1
    require(evaluation["evaluator_authority_sha256"] == EVALUATOR and evaluation["evaluator_version"] == "0.2.0", "evaluator mismatch"); checks += 2
    require(evaluation["artifact_paths"] == ["results/c340_lame_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"], "artifact path schema mismatch"); checks += 3
    require(evaluation["source_owner_tokens"] == ["10.1017/S0370164600020058", "10.1017/S0370164600020071", "https://dlmf.nist.gov/29", "10.1090/bull/1528"], "source owner tokens mismatch"); checks += 4
    expected_tuple = ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"]
    require(evaluation["tuple"] == expected_tuple and data["route_a"]["tuple"] == expected_tuple, "Route-A tuple mismatch"); checks += 10
    for index, key in enumerate(("a0", "a1", "a2", "a3", "a4")):
        require(set(evaluation[key]) == {"verdict", "evidence_status", "strongest_evidence", "strongest_failure"}, f"{key} schema mismatch"); checks += 4
        require(evaluation[key]["verdict"] == expected_tuple[index], f"{key} verdict mismatch"); checks += 1
    require(evaluation["overall_verdict"] == "ROUTE_A_REJECTED" and evaluation["route_b_invocation_allowed"] is False, "release decision mismatch"); checks += 2
    require(evaluation["scope_flags"] == FLAGS and data["scope_flags"] == FLAGS, "scope firewall mismatch"); checks += 18
    require(data["source_commit"] == SOURCE and data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "evidence provenance mismatch"); checks += 2

    rows = data["rational_modulus_rows"]
    grid = coordinates()
    require(len(rows) == len(grid) == 199, "rational modulus grid mismatch"); checks += 2
    keys = {"p", "q", "m", "lower_band", "finite_gap", "upper_band_start", "gap_width",
            "spectral_curve_coefficients_descending", "spectral_signs", "band_edge_modes"}
    for row, (p, q) in zip(rows, grid):
        require(set(row) == keys, "row schema mismatch"); checks += len(keys)
        require((row["p"], row["q"]) == (p, q), "row coordinate mismatch"); checks += 2
        m = Fraction(p, q)
        require(fraction(row["m"]) == m and 0 < m < 1, "modulus mismatch"); checks += 3
        require([fraction(value) for value in row["lower_band"]] == [m, Fraction(1)], "lower band mismatch"); checks += 2
        require([fraction(value) for value in row["finite_gap"]] == [Fraction(1), 1+m], "gap mismatch"); checks += 2
        require(fraction(row["upper_band_start"]) == 1+m and fraction(row["gap_width"]) == m, "upper edge mismatch"); checks += 2
        coefficients = [fraction(value) for value in row["spectral_curve_coefficients_descending"]]
        expected = [Fraction(1), -2*(1+m), 1+3*m+m*m, -m*(1+m)]
        require(coefficients == expected, "spectral polynomial coefficient mismatch"); checks += 4
        for edge in (m, Fraction(1), 1+m):
            require(polynomial_value(coefficients, edge) == 0, "band edge is not a curve root"); checks += 1
        samples = [(m-Fraction(1), -1), ((m+1)/2, 1), (1+m/2, -1), (2+m, 1)]
        for energy, sign in samples:
            value = polynomial_value(coefficients, energy)
            require((value > 0) - (value < 0) == sign, "spectral sign chamber mismatch"); checks += 1
        require(row["spectral_signs"] == {"below_m": -1, "lower_band": 1, "finite_gap": -1, "upper_band": 1}, "sign ledger mismatch"); checks += 4
        require(row["band_edge_modes"] == [
            {"mode": "dn", "energy": row["m"], "fiber": "periodic"},
            {"mode": "cn", "energy": "1", "fiber": "antiperiodic"},
            {"mode": "sn", "energy": row["upper_band_start"], "fiber": "antiperiodic"}], "band-edge mode mismatch"); checks += 9
    require(data["enumeration"] == {"rational_modulus_rows": 199, "q_max": 25, "audited_leaf_count": 5262}, "enumeration mismatch"); checks += 3
    require(leaf_count({key: value for key, value in data.items() if key != "payload_sha256"}) == 5262, "audited leaf count mismatch"); checks += 1
    receipts = data["universal_symbolic_receipts"]
    require(receipts["commutator"] == "[A,H_m]=0", "commutator convention mismatch"); checks += 1
    require(receipts["burchnall_chaundy"] == "A^2+16*(H_m-m)*(H_m-1)*(H_m-1-m)=0", "spectral curve convention mismatch"); checks += 1
    require(data["theorem_contract"]["spectral_type"] == "the real periodic operator has purely absolutely continuous spectrum", "spectral-type theorem drift"); checks += 1
    require(data["model"]["fiber_domain"] == "D(A_theta)=H^3_theta([0,2*K]) with f^(j)(2*K)=exp(i*theta)*f^(j)(0) for j=0,1,2", "fiber domain drift"); checks += 1
    require(data["theorem_contract"]["fiber_skew_adjointness"] == "on D(A_theta)=H^3_theta, periodic coefficients and common quasi-periodic phase cancel every endpoint term, so A_theta is skew-adjoint", "fiber skew-adjointness drift"); checks += 1
    require(data["references"][-1] == {"author": "P. Kuchment", "identifier": "DOI:10.1090/bull/1528", "role": "authoritative Floquet direct-integral and periodic absolutely-continuous spectral theory"}, "Floquet source drift"); checks += 3
    print(f"C340 independent Lame checker: PASS {checks} checks")


if __name__ == "__main__":
    main()
