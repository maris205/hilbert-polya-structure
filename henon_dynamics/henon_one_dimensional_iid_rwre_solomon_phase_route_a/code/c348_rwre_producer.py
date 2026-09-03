#!/usr/bin/env python3
"""Canonical exact-evidence producer for HCS-C348."""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c348_rwre_evidence.json"
DEFAULT_YAML = ROOT / "evaluations/route_a/HCS-C348/2026-09-03.yaml"
SOURCE = "1af63b945e19b5f94ac1cb76f93af5ac66d3d562"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
YAML_RAW = "a5a1c575b2bd293f9618dbb39b544cce5c74162f1ee4694f1f03e91f17e676f7"
YAML_SEMANTIC = "3e280936e376edb6fffaff9d77f522c5157020ca1c730f649b32724c96a1232b"
ALPHABET = (Fraction(1, 4), Fraction(1, 3), Fraction(1, 2),
            Fraction(2, 3), Fraction(3, 4))


def duplicate_pairs(items):
    answer = {}
    for key, value in items:
        if key in answer:
            raise ValueError("duplicate key")
        answer[key] = value
    return answer


class StrictLoader(yaml.SafeLoader):
    pass


StrictLoader.yaml_implicit_resolvers = {
    key: [(tag, rx) for tag, rx in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def strict_mapping(loader, node, deep=False):
    answer = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("merge key")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in answer:
            raise ValueError("duplicate/non-string YAML key")
        answer[key] = loader.construct_object(value_node, deep=deep)
    return answer


StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, strict_mapping)


def strict_yaml(path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("anchors forbidden")
    value = yaml.load(raw, Loader=StrictLoader)
    if type(value) is not dict:
        raise TypeError("YAML root")
    return value


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def fstr(value):
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def rho(p):
    return (1 - p) / p


def sign(value):
    return (value > 0) - (value < 0)


def chamber(log_sign, mean_rho, mean_inverse):
    if log_sign == 0:
        return "recurrent", Fraction(0)
    if log_sign < 0:
        if mean_rho is not None and mean_rho < 1:
            return "right_ballistic", (1 - mean_rho) / (1 + mean_rho)
        return "right_transient_zero_speed", Fraction(0)
    if mean_inverse is not None and mean_inverse < 1:
        return "left_ballistic", -(1 - mean_inverse) / (1 + mean_inverse)
    return "left_transient_zero_speed", Fraction(0)


def harmonic(n):
    return sum((Fraction(1, k) for k in range(1, n + 1)), Fraction(0))


def beta_rows():
    rows = []
    for alpha in range(1, 21):
        for beta in range(1, 21):
            log_value = harmonic(beta - 1) - harmonic(alpha - 1)
            mean_rho = Fraction(beta, alpha - 1) if alpha > 1 else None
            mean_inverse = Fraction(alpha, beta - 1) if beta > 1 else None
            name, speed = chamber(sign(log_value), mean_rho, mean_inverse)
            rows.append({
                "alpha": alpha, "beta": beta,
                "elog_rho_harmonic": fstr(log_value),
                "elog_rho_sign": sign(log_value),
                "mean_rho": "INF" if mean_rho is None else fstr(mean_rho),
                "mean_inverse_rho": "INF" if mean_inverse is None else fstr(mean_inverse),
                "chamber": name, "speed": fstr(speed),
            })
    return rows


def constant_rows():
    rows = []
    for p in ALPHABET:
        r = rho(p)
        log_sign = sign(r - 1)
        name, speed = chamber(log_sign, r, 1 / r)
        rows.append({"omega": fstr(p), "rho": fstr(r), "elog_rho_sign": log_sign,
                     "chamber": name, "solomon_speed": fstr(speed),
                     "homogeneous_speed": fstr(2 * p - 1)})
    return rows


def two_atom_rows():
    rows = []
    for left_index, p_left in enumerate(ALPHABET):
        for p_right in ALPHABET[left_index + 1:]:
            r_left, r_right = rho(p_left), rho(p_right)
            for denominator in range(2, 9):
                for numerator in range(1, denominator):
                    weight = Fraction(numerator, denominator)
                    product = r_left ** numerator * r_right ** (denominator - numerator)
                    log_sign = sign(product - 1)
                    mean_rho = weight * r_left + (1 - weight) * r_right
                    mean_inverse = weight / r_left + (1 - weight) / r_right
                    name, speed = chamber(log_sign, mean_rho, mean_inverse)
                    rows.append({
                        "omega_left": fstr(p_left), "omega_right": fstr(p_right),
                        "left_weight": fstr(weight),
                        "rho_product_power": fstr(product),
                        "elog_rho_sign": log_sign,
                        "mean_rho": fstr(mean_rho),
                        "mean_inverse_rho": fstr(mean_inverse),
                        "chamber": name, "speed": fstr(speed),
                    })
    return rows


def interval_rows():
    environments, hits = [], []
    environment_id = 0
    for length in range(1, 5):
        for word in itertools.product(ALPHABET, repeat=length):
            scale = [Fraction(1)]
            for p in word:
                scale.append(scale[-1] * rho(p))
            denominator = sum(scale, Fraction(0))
            environments.append({
                "environment_id": environment_id, "interior_length": length,
                "omega_word": [fstr(p) for p in word],
                "scale_weights": [fstr(value) for value in scale],
                "scale_denominator": fstr(denominator),
            })
            numerator = Fraction(0)
            for start in range(1, length + 1):
                numerator += scale[start - 1]
                probability = numerator / denominator
                hits.append({
                    "environment_id": environment_id, "start": start,
                    "left_boundary": 0, "right_boundary": length + 1,
                    "probability_hit_right_first": fstr(probability),
                    "harmonic_residual": "0",
                })
            environment_id += 1
    return environments, hits


def digest(rows):
    return hashlib.sha256(canonical(rows)).hexdigest()


def build(evaluation):
    raw = evaluation.read_bytes()
    semantic = strict_yaml(evaluation)
    if hashlib.sha256(raw).hexdigest() != YAML_RAW:
        raise AssertionError("evaluation raw hash")
    if hashlib.sha256(canonical(semantic)).hexdigest() != YAML_SEMANTIC:
        raise AssertionError("evaluation semantic hash")
    beta = beta_rows()
    constants = constant_rows()
    atoms = two_atom_rows()
    environments, hits = interval_rows()
    body = {
        "schema": "hcs-c348-rwre-evidence-v1",
        "candidate_id": "HCS-C348", "obstruction_id": "HEN-O332",
        "evaluation_date": "2026-09-03", "source_commit": SOURCE,
        "fixed_epoch": 1788393600, "scope_literal": SCOPE,
        "evaluator": {"authority": "flow_systems/skills/route-a-evaluator.md",
                      "version": "0.2.0", "sha256": EVALUATOR},
        "route_a_yaml": {
            "relative_path": "evaluations/route_a/HCS-C348/2026-09-03.yaml",
            "raw_sha256": YAML_RAW, "semantic_sha256": YAML_SEMANTIC},
        "model": {
            "environment": "iid omega_x in the open unit interval",
            "rho": "rho_x=(1-omega_x)/omega_x",
            "integrability": "E[abs(log rho_0)]<infinity",
            "quenched_law": "condition on the complete frozen environment",
            "annealed_law": "average the quenched path law over the iid environment",
            "step_rule": "from x move right with omega_x and left with 1-omega_x"},
        "theorem_contract": {
            "finite_interval": "exact quenched scale-function hitting probability",
            "direction": "sign of E[log rho_0] gives right transience, recurrence, or left transience",
            "speed": "annealed almost-sure LLN including both transient zero-speed chambers",
            "beta": "complete positive-parameter Beta environment direction and speed atlas",
            "constant": "homogeneous environment reduces to speed 2p-1",
            "proof_owner": "analytic scale-function plus stationary-ergodic crossing-time proof"},
        "finite_grid": {
            "omega_alphabet": [fstr(p) for p in ALPHABET],
            "maximum_interval_interior_length": 4,
            "interval_environment_rows": len(environments), "hitting_rows": len(hits),
            "beta_rows": len(beta), "two_atom_rows": len(atoms),
            "constant_rows": len(constants)},
        "collision_boundary": {
            "C342": "finite directed Dirichlet rows and annealed reinforcement, not a static iid environment on Z",
            "C273": "homogeneous iid increments, not quenched spatial disorder",
            "C253": "finite Moran absorption, not infinite-line directional speed"},
        "nonclaims": [
            "no theorem for non-iid, dynamic, higher-dimensional, or non-nearest-neighbour environments",
            "no central limit, slowdown exponent, large-deviation, or localization theorem",
            "no target arithmetic local data or Euler-factor interpretation",
            "no root number, automorphy, target zero match, Hilbert-Polya operator, or Route B"],
        "references": [
            {"authors": "Fred Solomon", "year": 1975,
             "identifier": "DOI:10.1214/AOP/1176996444",
             "role": "primary one-dimensional iid RWRE direction and speed theorem"},
            {"authors": "Fred Solomon", "year": 1975,
             "identifier": "Project-Euclid:aop/1176996444",
             "role": "publisher-hosted primary article record and text"},
            {"authors": "Ofer Zeitouni", "year": 2004,
             "identifier": "DOI:10.1007/978-3-540-39874-5_2",
             "role": "authoritative review and crossing-time formulation"}],
        "route_a": {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
                    "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False},
        "scope_flags": {
            "claims_target_arithmetic_local_data": False,
            "claims_target_euler_factors": False, "claims_root_number": False,
            "claims_automorphy": False,
            "claims_target_divisor_or_counting_law": False,
            "claims_target_functional_equation": False,
            "claims_target_zero_match": False,
            "claims_hilbert_polya_operator": False, "invokes_route_b": False},
        "beta_rows": beta, "constant_rows": constants, "two_atom_rows": atoms,
        "interval_environment_rows": environments, "hitting_rows": hits,
        "enumeration": {
            "all_arithmetic_exact": True, "floating_point_used": False,
            "finite_evidence_proves_infinite_theorem": False,
            "beta_sha256": digest(beta), "constant_sha256": digest(constants),
            "two_atom_sha256": digest(atoms),
            "interval_environment_sha256": digest(environments),
            "hitting_sha256": digest(hits)},
    }
    body["payload_sha256"] = hashlib.sha256(canonical(body)).hexdigest()
    return body


def main():
    if sys.flags.optimize:
        raise RuntimeError("C348 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_YAML)
    args = parser.parse_args()
    result = build(args.evaluation)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(f"C348_PRODUCER_PASS beta={len(result['beta_rows'])} "
          f"atoms={len(result['two_atom_rows'])} intervals={len(result['interval_environment_rows'])} "
          f"hits={len(result['hitting_rows'])} payload={result['payload_sha256']}")


if __name__ == "__main__":
    main()
