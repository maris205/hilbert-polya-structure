#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C325."""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c325_moser_tardos_evidence.json"
DEFAULT_YAML = ROOT / "evaluations/route_a/HCS-C325/2026-09-03.yaml"
SOURCE = "1aba1f6fd0cf81baa7c137a2ce7ce3d097ba63fc"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
YAML_RAW = "4f58fde8b9b70c5f3381a78fb357f2cc0c41e5f8bf64c8551843ddaa60b2084e"
YAML_SEMANTIC = "623e0eb35ba5330ec93243c163d9fabc754183008b0f37c384610bdc5c6690ee"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FLAGS = {"claims_target_arithmetic_local_data": False, "claims_target_euler_factors": False,
         "claims_root_number": False, "claims_automorphy": False,
         "claims_target_divisor_or_counting_law": False,
         "claims_target_functional_equation": False, "claims_target_zero_match": False,
         "claims_hilbert_polya_operator": False, "invokes_route_b": False}


def pairs(items):
    out = {}
    for key, value in items:
        if key in out:
            raise ValueError("duplicate JSON key")
        out[key] = value
    return out


def strict_json(path):
    value = json.loads(path.read_text(), object_pairs_hook=pairs,
                       parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)))
    if type(value) is not dict:
        raise TypeError("JSON root")
    return value


class Loader(yaml.SafeLoader):
    pass


Loader.yaml_implicit_resolvers = {
    key: [(tag, rx) for tag, rx in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def mapping(loader, node, deep=False):
    out = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("merge")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in out:
            raise ValueError("duplicate/non-string")
        out[key] = loader.construct_object(value_node, deep=deep)
    return out


Loader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)


def strict_yaml(path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("alias")
    value = yaml.load(raw, Loader=Loader)
    if type(value) is not dict:
        raise TypeError("YAML root")
    return value


def need(condition, label):
    if not condition:
        raise AssertionError(label)


def exact_keys(value, keys, label):
    need(type(value) is dict and set(value) == set(keys), f"{label} keys")


def canon(value):
    if type(value) is not str:
        raise TypeError("rational string")
    number = Fraction(value)
    expected = str(number.numerator) if number.denominator == 1 else f"{number.numerator}/{number.denominator}"
    need(value == expected, "canonical rational")
    return number


def format_q(number):
    return str(number.numerator) if number.denominator == 1 else f"{number.numerator}/{number.denominator}"


def specs():
    return [
        ("two_overlap", 5, [("A", (0, 1, 2), (0, 0, 0), Fraction(1, 4)),
                            ("B", (2, 3, 4), (1, 1, 1), Fraction(1, 4))]),
        ("triangle_overlap", 6, [("A", (0, 1, 2), (0, 0, 0), Fraction(1, 4)),
                                 ("B", (2, 3, 4), (1, 1, 1), Fraction(1, 4)),
                                 ("C", (4, 5, 0), (0, 0, 0), Fraction(1, 4))]),
        ("disjoint_mixed", 4, [("A", (0,), (1,), Fraction(2, 3)),
                                ("B", (2, 3), (0, 0), Fraction(1, 3))]),
    ]


def gauss(a, b):
    size = len(b)
    rows = [list(a[i]) + [b[i]] for i in range(size)]
    for column in range(size):
        pivot = next(index for index in range(column, size) if rows[index][column] != 0)
        rows[column], rows[pivot] = rows[pivot], rows[column]
        divisor = rows[column][column]
        for j in range(column, size + 1):
            rows[column][j] /= divisor
        for index in range(size):
            if index == column:
                continue
            multiplier = rows[index][column]
            for j in range(column, size + 1):
                rows[index][j] -= multiplier * rows[column][j]
    return [rows[index][size] for index in range(size)]


def multiply(a, b, cap):
    result = [Fraction(0)] * (cap + 1)
    for i in range(cap + 1):
        for j in range(cap + 1 - i):
            result[i + j] += a[i] * b[j]
    return result


def rebuild(name, width, events):
    labels = [row[0] for row in events]
    lookup = {row[0]: row for row in events}
    adjacent = {label: sorted(other for other in labels if other != label and
                              set(lookup[label][1]).intersection(lookup[other][1])) for label in labels}
    words = [tuple((integer >> (width - 1 - j)) & 1 for j in range(width))
             for integer in range(2 ** width)]
    choices = []
    kernels = []
    transition_rows = []
    for state in words:
        chosen = next((event for event in events if tuple(state[i] for i in event[1]) == event[2]), None)
        choices.append(None if chosen is None else chosen[0])
        targets = {}
        if chosen:
            for fresh in itertools.product((0, 1), repeat=len(chosen[1])):
                target = list(state)
                for coordinate, bit in zip(chosen[1], fresh):
                    target[coordinate] = bit
                target_index = words.index(tuple(target))
                targets[target_index] = targets.get(target_index, 0) + 1
        divisor = 1 if chosen is None else 2 ** len(chosen[1])
        kernel = [(target, Fraction(count, divisor)) for target, count in sorted(targets.items())]
        kernels.append(kernel)
        transition_rows.append({"state": "".join(map(str, state)),
                                "chosen_event": None if chosen is None else chosen[0],
                                "targets": [{"state": "".join(map(str, words[target])),
                                             "probability": format_q(probability)}
                                            for target, probability in kernel]})
    live = [index for index, choice in enumerate(choices) if choice is not None]
    locate = {state: row for row, state in enumerate(live)}
    system = [[Fraction(i == j) for j in range(len(live))] for i in range(len(live))]
    for state in live:
        for target, probability in kernels[state]:
            if target in locate:
                system[locate[state]][locate[target]] -= probability
    expected = []
    for label in labels:
        solution = gauss(system, [Fraction(choices[state] == label) for state in live])
        expected.append(sum(solution) / len(words))
    cap = 6
    tree = {label: [Fraction(0)] * (cap + 1) for label in labels}
    probability = {label: Fraction(1, 2 ** len(lookup[label][1])) for label in labels}
    for _ in range(cap):
        next_tree = {}
        for label in labels:
            product = [Fraction(1)] + [Fraction(0)] * cap
            for child in [label] + adjacent[label]:
                factor = tree[child][:]
                factor[0] += 1
                product = multiply(product, factor, cap)
            next_tree[label] = [Fraction(0)] + [probability[label] * coefficient
                                               for coefficient in product[:-1]]
        tree = next_tree
    event_rows = []
    for label, variables, pattern, witness in events:
        rhs = witness * math.prod(1 - lookup[neighbor][3] for neighbor in adjacent[label])
        event_rows.append({"label": label, "variables": list(variables), "pattern": list(pattern),
                           "probability": format_q(probability[label]), "witness_x": format_q(witness),
                           "dependencies": adjacent[label], "lll_rhs": format_q(rhs),
                           "expectation_bound": format_q(witness / (1 - witness)),
                           "witness_tree_weight_by_size_1_to_6":
                               [format_q(value) for value in tree[label][1:]]})
    return {"name": name, "variable_count": width, "event_rows": event_rows,
            "valid_assignment_count": choices.count(None),
            "expected_resamplings_by_event": [{"label": label, "value": format_q(value)}
                                               for label, value in zip(labels, expected)],
            "expected_total_resamplings": format_q(sum(expected)),
            "transition_rows": transition_rows}


def leaves(value):
    if type(value) is dict:
        return sum(leaves(item) for item in value.values())
    if type(value) is list:
        return sum(leaves(item) for item in value)
    return 1


def main():
    if sys.flags.optimize:
        raise RuntimeError("C325 checker refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_YAML)
    args = parser.parse_args()
    data = strict_json(args.evidence)
    root_keys = {"schema", "candidate_id", "obstruction_id", "evaluation_date", "fixed_epoch",
                 "source_commit", "scope_literal", "evaluator", "model", "theorem_contract",
                 "finite_grid", "instance_rows", "route_a_yaml", "collision_boundary", "route_a",
                 "scope_flags", "nonclaims", "references", "enumeration", "payload_sha256"}
    exact_keys(data, root_keys, "root")
    required = {"schema": "hcs-c325-moser-tardos-v1", "candidate_id": "HCS-C325",
                "obstruction_id": "HEN-O309", "evaluation_date": "2026-09-03",
                "fixed_epoch": 1788393600, "source_commit": SOURCE, "scope_literal": SCOPE}
    for key, value in required.items():
        need(data[key] == value, key)
    need(data["evaluator"] == {"version": "0.2.0", "sha256": EVALUATOR,
                                "authority": "flow_systems/skills/route-a-evaluator.md"}, "evaluator")
    body = dict(data); payload = body.pop("payload_sha256")
    need(payload == hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"),
                                             ensure_ascii=False).encode()).hexdigest(), "payload")
    model = {"variable_model": "finite mutually independent variables with finite domains",
             "dependence": "two distinct bad events are adjacent exactly when they share a variable",
             "randomness": "independent infinite resampling table for every variable",
             "selection_rule": "arbitrary legal currently violated event; finite evidence uses lexicographic order"}
    theorem = {"criterion": "P(A)<=x_A product_{B in Gamma(A)}(1-x_B), with every x_A in (0,1)",
               "termination": "almost sure finite termination for every legal sequential violated-event rule",
               "output": "the terminal assignment avoids every bad event",
               "per_event_bound": "E[N_A]<=x_A/(1-x_A)",
               "total_bound": "E[sum_A N_A]<=sum_A x_A/(1-x_A)",
               "proof": "resampling-table witness lemma plus proper-tree branching-process bound"}
    need(data["model"] == model and data["theorem_contract"] == theorem, "model/theorem")
    need(data["finite_grid"] == {"instances": 3, "max_variables": 6, "witness_tree_size_max": 6,
                                  "domains": "binary fair variables"}, "grid")
    expected = [rebuild(*specification) for specification in specs()]
    need(data["instance_rows"] == expected, "independent instance reconstruction")
    for instance in data["instance_rows"]:
        exact_keys(instance, {"name", "variable_count", "event_rows", "valid_assignment_count",
                              "expected_resamplings_by_event", "expected_total_resamplings",
                              "transition_rows"}, "instance")
        need(len(instance["transition_rows"]) == 2 ** instance["variable_count"], "state coordinates")
        for event in instance["event_rows"]:
            exact_keys(event, {"label", "variables", "pattern", "probability", "witness_x",
                               "dependencies", "lll_rhs", "expectation_bound",
                               "witness_tree_weight_by_size_1_to_6"}, "event")
            need(canon(event["probability"]) <= canon(event["lll_rhs"]), "LLL receipt")
            need(sum(canon(value) for value in event["witness_tree_weight_by_size_1_to_6"])
                 <= canon(event["expectation_bound"]), "truncated tree bound")
        for row in instance["transition_rows"]:
            exact_keys(row, {"state", "chosen_event", "targets"}, "transition")
            for target in row["targets"]:
                exact_keys(target, {"state", "probability"}, "transition target")
            need((not row["targets"] and row["chosen_event"] is None) or
                 sum(canon(target["probability"]) for target in row["targets"]) == 1,
                 "stochastic row")
    evaluation = strict_yaml(args.evaluation)
    yaml_keys = {"schema", "candidate_id", "title", "evaluation_date", "source_commit", "fixed_epoch",
                 "scope_literal", "evaluator_authority", "evaluator_version", "evaluator_authority_sha256",
                 "obstruction_id", "candidate_definition", "family", "phase_space", "dynamics", "parameters",
                 "parameter_provenance", "arithmetic_origin", "clock", "normalization", "determinant_convention",
                 "orbit_cutoff", "precision", "training_data", "forbidden_data", "artifact_paths", "a0", "a1",
                 "a2", "a3", "a4", "tuple", "overall_verdict", "route_b_invocation_allowed",
                 "route_b_lock_reason", "scope_flags", "theorem_status", "finite_evidence_role",
                 "source_owner_tokens"}
    exact_keys(evaluation, yaml_keys, "evaluation")
    gate_objects = {
        "a0": {"verdict": "A0_FAIL", "evidence_status": "PROVED",
               "strongest_evidence": "the variable model and resampling tables are intrinsic",
               "strongest_failure": "there is no rational-prime carrier or arithmetic local datum"},
        "a1": {"verdict": "A1_FAIL", "evidence_status": "PROVED",
               "strongest_evidence": "every resampling log and witness tree is exactly defined",
               "strongest_failure": "terminating randomized logs are not a primitive periodic-orbit ledger"},
        "a2": {"verdict": "A2_FAIL", "evidence_status": "STOP_SCOPED",
               "strongest_evidence": "the expected resampling bounds are analytic",
               "strongest_failure": "there is no dynamical determinant or target divisor"},
        "a3": {"verdict": "A3_FAIL", "evidence_status": "STOP_SCOPED",
               "strongest_evidence": "the theorem is uniform over all legal violated-event rules",
               "strongest_failure": "it supplies no target functional equation or arithmetic continuation"},
        "a4": {"verdict": "A4_FAIL", "evidence_status": "STOP_SCOPED",
               "strongest_evidence": "the algorithm has a canonical resampling-table probability space",
               "strongest_failure": "it has no natural unitary, scattering, Hamiltonian, or self-adjoint quantization"},
    }
    for branch, expected_gate in gate_objects.items():
        exact_keys(evaluation[branch], {"verdict", "evidence_status", "strongest_evidence", "strongest_failure"}, branch)
        need(evaluation[branch] == expected_gate, f"{branch} semantics")
    lock = data["route_a_yaml"]
    exact_keys(lock, {"relative_path", "raw_sha256", "semantic_sha256"}, "YAML lock")
    need(lock["relative_path"] == "evaluations/route_a/HCS-C325/2026-09-03.yaml", "YAML path")
    raw = hashlib.sha256(args.evaluation.read_bytes()).hexdigest()
    semantic = hashlib.sha256(json.dumps(evaluation, sort_keys=True, separators=(",", ":"),
                                            ensure_ascii=False).encode()).hexdigest()
    need(raw == lock["raw_sha256"] == YAML_RAW and semantic == lock["semantic_sha256"] == YAML_SEMANTIC,
         "YAML hashes")
    need(evaluation["candidate_id"] == "HCS-C325" and evaluation["source_commit"] == SOURCE and
         evaluation["fixed_epoch"] == 1788393600 and evaluation["evaluation_date"] == "2026-09-03", "YAML identity")
    need(evaluation["evaluator_authority"] == "flow_systems/skills/route-a-evaluator.md" and
         evaluation["evaluator_version"] == "0.2.0" and evaluation["evaluator_authority_sha256"] == EVALUATOR,
         "YAML evaluator")
    route = {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
             "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}
    need(data["route_a"] == route and evaluation["tuple"] == route["tuple"] and
         evaluation["overall_verdict"] == route["overall"] and evaluation["route_b_invocation_allowed"] is False,
         "route")
    need([evaluation[b]["verdict"] for b in ("a0", "a1", "a2", "a3", "a4")] == route["tuple"], "branch verdicts")
    need([evaluation[b]["evidence_status"] for b in ("a0", "a1", "a2", "a3", "a4")] ==
         ["PROVED", "PROVED", "STOP_SCOPED", "STOP_SCOPED", "STOP_SCOPED"], "branch status")
    need(data["scope_flags"] == FLAGS and evaluation["scope_flags"] == FLAGS and evaluation["training_data"] == "none",
         "scope")
    need(evaluation["theorem_status"] == "PROVABLE_AS_STATED" and
         evaluation["source_owner_tokens"] == ["10.1145/1667053.1667060", "arXiv:0903.0544"], "source/status")
    need(evaluation["finite_evidence_role"] ==
         "regression evidence only; finite assignment chains and truncated witness trees do not prove the general theorem",
         "finite evidence role")
    need(evaluation["route_b_lock_reason"] ==
         "all Route-A layers fail and the frozen scope contains no bad-prime, Euler-factor, or root-number datum",
         "Route B lock reason")
    need(data["collision_boundary"] == {
        "C192": "a fixed hyperplane chamber walk is not an adaptive bad-event resampling algorithm",
        "C302": "Quicksort has a recursive cost contraction, not shared-variable witness trees",
        "C317": "Newton--Schulz is deterministic matrix iteration, not randomized constraint repair"}, "collisions")
    need(data["nonclaims"] == [
        "Finite assignment chains and size-six witness trees do not prove the general theorem.",
        "No lopsided, permutation, parallel, or outside-criterion resampling theorem is asserted.",
        "No literature-priority claim is made.",
        "No target arithmetic datum, Euler factor, root number, automorphy, target divisor, functional equation, target zero match, or Hilbert--Polya operator is asserted."], "nonclaims")
    need(data["references"] == [
        {"authors": "Robin A. Moser and Gabor Tardos", "title": "A constructive proof of the general Lovasz Local Lemma",
         "identifier": "10.1145/1667053.1667060"},
        {"authors": "Robin A. Moser and Gabor Tardos", "title": "author preprint", "identifier": "arXiv:0903.0544"}], "references")
    exact_keys(data["enumeration"], {"instance_rows", "state_rows", "event_rows", "audited_leaf_count"}, "enumeration")
    countable = dict(data); countable.pop("payload_sha256"); enumeration = countable.pop("enumeration")
    need(enumeration == {"instance_rows": 3, "state_rows": 112, "event_rows": 7,
                         "audited_leaf_count": leaves(countable)}, "enumeration values")
    checks = 44 + sum(len(row["transition_rows"]) + 3 * len(row["event_rows"])
                      for row in data["instance_rows"])
    print(f"C325 independent checker: PASS ({checks} checks, 112 exact transition rows)")


if __name__ == "__main__":
    main()
