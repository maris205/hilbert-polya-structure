#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C348."""
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
DEFAULT = ROOT / "results/c348_rwre_evidence.json"
DEFAULT_YAML = ROOT / "evaluations/route_a/HCS-C348/2026-09-03.yaml"
SOURCE = "1af63b945e19b5f94ac1cb76f93af5ac66d3d562"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
YAML_RAW = "a5a1c575b2bd293f9618dbb39b544cce5c74162f1ee4694f1f03e91f17e676f7"
YAML_SEMANTIC = "3e280936e376edb6fffaff9d77f522c5157020ca1c730f649b32724c96a1232b"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
GRID = (Fraction(1, 4), Fraction(1, 3), Fraction(1, 2),
        Fraction(2, 3), Fraction(3, 4))
FLAGS = {
    "claims_target_arithmetic_local_data": False,
    "claims_target_euler_factors": False, "claims_root_number": False,
    "claims_automorphy": False, "claims_target_divisor_or_counting_law": False,
    "claims_target_functional_equation": False, "claims_target_zero_match": False,
    "claims_hilbert_polya_operator": False, "invokes_route_b": False,
}


def duplicate_pairs(items):
    answer = {}
    for key, value in items:
        if key in answer:
            raise ValueError("duplicate JSON key")
        answer[key] = value
    return answer


def strict_json(path):
    value = json.loads(path.read_text(), object_pairs_hook=duplicate_pairs,
                       parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)))
    if type(value) is not dict:
        raise TypeError("JSON root")
    return value


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
            raise ValueError("YAML merge forbidden")
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
            raise ValueError("YAML anchors/aliases forbidden")
    value = yaml.load(raw, Loader=StrictLoader)
    if type(value) is not dict:
        raise TypeError("YAML root")
    return value


def need(condition, label):
    if not condition:
        raise AssertionError(label)


def exact_keys(value, keys, label):
    need(type(value) is dict and set(value) == set(keys), f"{label} keys")


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def as_text(value):
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def bias(p):
    return Fraction(1 - p, p)


def sgn(x):
    return int(x > 0) - int(x < 0)


def classify(log_direction, first, reciprocal):
    if log_direction == 0:
        return "recurrent", Fraction(0)
    if log_direction == -1:
        return (("right_ballistic", (1 - first) / (1 + first))
                if first is not None and first < 1
                else ("right_transient_zero_speed", Fraction(0)))
    return (("left_ballistic", -(1 - reciprocal) / (1 + reciprocal))
            if reciprocal is not None and reciprocal < 1
            else ("left_transient_zero_speed", Fraction(0)))


def harmonic_number(n):
    result = Fraction(0)
    for j in range(1, n + 1):
        result += Fraction(1, j)
    return result


def expected_beta():
    answer = []
    for a in range(1, 21):
        for b in range(1, 21):
            logarithmic = harmonic_number(b - 1) - harmonic_number(a - 1)
            first = Fraction(b, a - 1) if a != 1 else None
            reciprocal = Fraction(a, b - 1) if b != 1 else None
            label, velocity = classify(sgn(logarithmic), first, reciprocal)
            answer.append({"alpha": a, "beta": b,
                "elog_rho_harmonic": as_text(logarithmic),
                "elog_rho_sign": sgn(logarithmic),
                "mean_rho": "INF" if first is None else as_text(first),
                "mean_inverse_rho": "INF" if reciprocal is None else as_text(reciprocal),
                "chamber": label, "speed": as_text(velocity)})
    return answer


def expected_constants():
    answer = []
    for probability in GRID:
        ratio = bias(probability)
        label, velocity = classify(sgn(ratio - 1), ratio, 1 / ratio)
        answer.append({"omega": as_text(probability), "rho": as_text(ratio),
            "elog_rho_sign": sgn(ratio - 1), "chamber": label,
            "solomon_speed": as_text(velocity),
            "homogeneous_speed": as_text(2 * probability - 1)})
    return answer


def expected_atoms():
    answer = []
    for i in range(len(GRID)):
        for j in range(i + 1, len(GRID)):
            left, right = GRID[i], GRID[j]
            left_ratio, right_ratio = bias(left), bias(right)
            for total in range(2, 9):
                for count in range(1, total):
                    weight = Fraction(count, total)
                    multiplicative_test = left_ratio ** count * right_ratio ** (total - count)
                    direction = sgn(multiplicative_test - 1)
                    first = weight * left_ratio + (1 - weight) * right_ratio
                    reciprocal = weight / left_ratio + (1 - weight) / right_ratio
                    label, velocity = classify(direction, first, reciprocal)
                    answer.append({"omega_left": as_text(left), "omega_right": as_text(right),
                        "left_weight": as_text(weight),
                        "rho_product_power": as_text(multiplicative_test),
                        "elog_rho_sign": direction, "mean_rho": as_text(first),
                        "mean_inverse_rho": as_text(reciprocal),
                        "chamber": label, "speed": as_text(velocity)})
    return answer


def expected_intervals():
    environments, probabilities = [], []
    identifier = 0
    for size in range(1, 5):
        for omega in itertools.product(GRID, repeat=size):
            weights = [Fraction(1)]
            for probability in omega:
                weights += [weights[-1] * bias(probability)]
            normalizer = sum(weights, Fraction(0))
            environments.append({"environment_id": identifier,
                "interior_length": size, "omega_word": [as_text(x) for x in omega],
                "scale_weights": [as_text(x) for x in weights],
                "scale_denominator": as_text(normalizer)})
            partial = Fraction(0)
            for initial in range(1, size + 1):
                partial += weights[initial - 1]
                probabilities.append({"environment_id": identifier, "start": initial,
                    "left_boundary": 0, "right_boundary": size + 1,
                    "probability_hit_right_first": as_text(partial / normalizer),
                    "harmonic_residual": "0"})
            identifier += 1
    return environments, probabilities


def row_digest(rows):
    return hashlib.sha256(canonical(rows)).hexdigest()


def check_yaml(evaluation):
    keys = ["schema", "candidate_id", "title", "evaluation_date", "source_commit",
        "fixed_epoch", "scope_literal", "evaluator_authority", "evaluator_version",
        "evaluator_authority_sha256", "obstruction_id", "candidate_definition", "family",
        "phase_space", "dynamics", "parameters", "parameter_provenance", "arithmetic_origin",
        "clock", "normalization", "determinant_convention", "orbit_cutoff", "precision",
        "training_data", "forbidden_data", "artifact_paths", "a0", "a1", "a2", "a3",
        "a4", "tuple", "overall_verdict", "route_b_invocation_allowed",
        "route_b_lock_reason", "scope_flags", "theorem_status", "finite_evidence_role",
        "source_owner_tokens"]
    exact_keys(evaluation, keys, "YAML top")
    need(evaluation["schema"] == "route-a-evaluation-v0.2.0", "YAML schema")
    need(evaluation["candidate_id"] == "HCS-C348" and evaluation["obstruction_id"] == "HEN-O332", "YAML ids")
    need(evaluation["evaluation_date"] == "2026-09-03", "YAML date")
    need(evaluation["source_commit"] == SOURCE and evaluation["fixed_epoch"] == 1788393600, "YAML source")
    need(evaluation["scope_literal"] == SCOPE, "YAML scope")
    need(evaluation["evaluator_authority"] == "flow_systems/skills/route-a-evaluator.md", "YAML authority")
    need(evaluation["evaluator_version"] == "0.2.0" and evaluation["evaluator_authority_sha256"] == EVALUATOR, "YAML evaluator")
    need(evaluation["artifact_paths"] == ["results/c348_rwre_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"], "YAML artifacts")
    expected_verdicts = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"]
    for index, branch in enumerate(("a0", "a1", "a2", "a3", "a4")):
        exact_keys(evaluation[branch], ["verdict", "evidence_status", "strongest_evidence", "strongest_failure"], f"YAML {branch}")
        need(evaluation[branch]["verdict"] == expected_verdicts[index], f"YAML {branch} verdict")
        need(evaluation[branch]["evidence_status"] == ("PROVED" if index < 2 else "STOP_SCOPED"), f"YAML {branch} status")
    need(evaluation["tuple"] == expected_verdicts and evaluation["overall_verdict"] == "ROUTE_A_REJECTED", "YAML verdict")
    need(evaluation["route_b_invocation_allowed"] is False, "YAML Route B")
    need(evaluation["route_b_lock_reason"] == "all Route-A arithmetic, primitive-orbit, determinant, analytic, and operator gates fail", "YAML lock")
    need(evaluation["scope_flags"] == FLAGS, "YAML flags")
    need(evaluation["theorem_status"] == "PROVABLE_AS_STATED", "YAML theorem")
    need(evaluation["finite_evidence_role"] == "convention and implementation receipt, not proof of the infinite-environment theorem", "YAML evidence role")
    need(evaluation["source_owner_tokens"] == ["DOI:10.1214/AOP/1176996444", "Project-Euclid:aop/1176996444", "DOI:10.1007/978-3-540-39874-5_2"], "YAML sources")


def main():
    if sys.flags.optimize:
        raise RuntimeError("C348 checker refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_YAML)
    args = parser.parse_args()
    data = strict_json(args.evidence)
    raw_yaml = args.evaluation.read_bytes()
    evaluation = strict_yaml(args.evaluation)
    need(hashlib.sha256(raw_yaml).hexdigest() == YAML_RAW, "YAML raw digest")
    need(hashlib.sha256(canonical(evaluation)).hexdigest() == YAML_SEMANTIC, "YAML semantic digest")
    check_yaml(evaluation)
    exact_keys(data, ["schema", "candidate_id", "obstruction_id", "evaluation_date",
        "source_commit", "fixed_epoch", "scope_literal", "evaluator", "route_a_yaml",
        "model", "theorem_contract", "finite_grid", "collision_boundary", "nonclaims",
        "references", "route_a", "scope_flags", "beta_rows", "constant_rows",
        "two_atom_rows", "interval_environment_rows", "hitting_rows", "enumeration",
        "payload_sha256"], "top")
    body = dict(data)
    claimed = body.pop("payload_sha256")
    need(type(claimed) is str and claimed == hashlib.sha256(canonical(body)).hexdigest(), "payload hash")
    need(data["schema"] == "hcs-c348-rwre-evidence-v1", "schema")
    need(data["candidate_id"] == "HCS-C348" and data["obstruction_id"] == "HEN-O332", "ids")
    need(data["evaluation_date"] == "2026-09-03" and data["source_commit"] == SOURCE, "source")
    need(data["fixed_epoch"] == 1788393600 and data["scope_literal"] == SCOPE, "scope")
    need(data["evaluator"] == {"authority": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR}, "evaluator")
    need(data["route_a_yaml"] == {"relative_path": "evaluations/route_a/HCS-C348/2026-09-03.yaml", "raw_sha256": YAML_RAW, "semantic_sha256": YAML_SEMANTIC}, "YAML binding")
    need(data["model"] == {"environment": "iid omega_x in the open unit interval", "rho": "rho_x=(1-omega_x)/omega_x", "integrability": "E[abs(log rho_0)]<infinity", "quenched_law": "condition on the complete frozen environment", "annealed_law": "average the quenched path law over the iid environment", "step_rule": "from x move right with omega_x and left with 1-omega_x"}, "model")
    need(data["theorem_contract"] == {"finite_interval": "exact quenched scale-function hitting probability", "direction": "sign of E[log rho_0] gives right transience, recurrence, or left transience", "speed": "annealed almost-sure LLN including both transient zero-speed chambers", "beta": "complete positive-parameter Beta environment direction and speed atlas", "constant": "homogeneous environment reduces to speed 2p-1", "proof_owner": "analytic scale-function plus stationary-ergodic crossing-time proof"}, "contract")
    need(data["collision_boundary"] == {"C342": "finite directed Dirichlet rows and annealed reinforcement, not a static iid environment on Z", "C273": "homogeneous iid increments, not quenched spatial disorder", "C253": "finite Moran absorption, not infinite-line directional speed"}, "collision")
    need(data["nonclaims"] == ["no theorem for non-iid, dynamic, higher-dimensional, or non-nearest-neighbour environments", "no central limit, slowdown exponent, large-deviation, or localization theorem", "no target arithmetic local data or Euler-factor interpretation", "no root number, automorphy, target zero match, Hilbert-Polya operator, or Route B"], "nonclaims")
    need(data["references"] == [{"authors": "Fred Solomon", "year": 1975, "identifier": "DOI:10.1214/AOP/1176996444", "role": "primary one-dimensional iid RWRE direction and speed theorem"}, {"authors": "Fred Solomon", "year": 1975, "identifier": "Project-Euclid:aop/1176996444", "role": "publisher-hosted primary article record and text"}, {"authors": "Ofer Zeitouni", "year": 2004, "identifier": "DOI:10.1007/978-3-540-39874-5_2", "role": "authoritative review and crossing-time formulation"}], "references")
    need(data["route_a"] == {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"], "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}, "Route A")
    need(data["scope_flags"] == FLAGS, "flags")
    beta = expected_beta()
    constants = expected_constants()
    atoms = expected_atoms()
    environments, hits = expected_intervals()
    need(data["beta_rows"] == beta, "beta ledger")
    need(data["constant_rows"] == constants, "constant ledger")
    need(data["two_atom_rows"] == atoms, "two-atom ledger")
    need(data["interval_environment_rows"] == environments, "environment ledger")
    need(data["hitting_rows"] == hits, "hitting ledger")
    need(data["finite_grid"] == {"omega_alphabet": [as_text(p) for p in GRID], "maximum_interval_interior_length": 4, "interval_environment_rows": 780, "hitting_rows": 2930, "beta_rows": 400, "two_atom_rows": 280, "constant_rows": 5}, "grid")
    need(data["enumeration"] == {"all_arithmetic_exact": True, "floating_point_used": False, "finite_evidence_proves_infinite_theorem": False, "beta_sha256": row_digest(beta), "constant_sha256": row_digest(constants), "two_atom_sha256": row_digest(atoms), "interval_environment_sha256": row_digest(environments), "hitting_sha256": row_digest(hits)}, "enumeration")
    print(f"C348 independent RWRE checker: PASS beta={len(beta)} atoms={len(atoms)} "
          f"intervals={len(environments)} hits={len(hits)}")


if __name__ == "__main__":
    main()
