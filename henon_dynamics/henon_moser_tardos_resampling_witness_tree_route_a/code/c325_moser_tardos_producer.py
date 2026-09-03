#!/usr/bin/env python3
"""Deterministic exact evidence producer for HCS-C325."""
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
OUTPUT = ROOT / "results/c325_moser_tardos_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C325/2026-09-03.yaml"
SOURCE = "1aba1f6fd0cf81baa7c137a2ce7ce3d097ba63fc"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EVALUATION_RAW = "4f58fde8b9b70c5f3381a78fb357f2cc0c41e5f8bf64c8551843ddaa60b2084e"
EVALUATION_SEMANTIC = "623e0eb35ba5330ec93243c163d9fabc754183008b0f37c384610bdc5c6690ee"
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
    key: [(tag, regexp) for tag, regexp in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def unique_mapping(loader, node, deep=False):
    out = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in out:
            raise ValueError("duplicate or non-string YAML key")
        out[key] = loader.construct_object(value_node, deep=deep)
    return out


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def strict_yaml(path: Path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchors/aliases forbidden")
    value = yaml.load(raw, Loader=UniqueLoader)
    if type(value) is not dict:
        raise TypeError("YAML root")
    return value


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def poly_mul(left, right, degree):
    out = [Fraction(0)] * (degree + 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j <= degree:
                out[i + j] += a * b
    return out


def solve(matrix, rhs):
    n = len(rhs)
    aug = [list(matrix[i]) + [rhs[i]] for i in range(n)]
    for col in range(n):
        pivot = next(row for row in range(col, n) if aug[row][col])
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [value / scale for value in aug[col]]
        for row in range(n):
            if row != col and aug[row][col]:
                scale = aug[row][col]
                aug[row] = [a - scale * b for a, b in zip(aug[row], aug[col])]
    return [aug[i][-1] for i in range(n)]


def specifications():
    return [
        ("two_overlap", 5, [
            ("A", (0, 1, 2), (0, 0, 0), Fraction(1, 4)),
            ("B", (2, 3, 4), (1, 1, 1), Fraction(1, 4)),
        ]),
        ("triangle_overlap", 6, [
            ("A", (0, 1, 2), (0, 0, 0), Fraction(1, 4)),
            ("B", (2, 3, 4), (1, 1, 1), Fraction(1, 4)),
            ("C", (4, 5, 0), (0, 0, 0), Fraction(1, 4)),
        ]),
        ("disjoint_mixed", 4, [
            ("A", (0,), (1,), Fraction(2, 3)),
            ("B", (2, 3), (0, 0), Fraction(1, 3)),
        ]),
    ]


def violated(state, event):
    return all(state[index] == bit for index, bit in zip(event[1], event[2]))


def instance_row(name, variable_count, events):
    labels = [event[0] for event in events]
    by_label = {event[0]: event for event in events}
    dependencies = {
        label: sorted(other for other in labels if other != label and
                      set(by_label[label][1]) & set(by_label[other][1]))
        for label in labels
    }
    states = list(itertools.product((0, 1), repeat=variable_count))
    transitions = []
    transient = []
    chosen_by_state = {}
    kernels = {}
    for state_index, state in enumerate(states):
        chosen = next((event for event in events if violated(state, event)), None)
        chosen_by_state[state_index] = None if chosen is None else chosen[0]
        targets = {}
        if chosen is not None:
            transient.append(state_index)
            variables = chosen[1]
            for replacement in itertools.product((0, 1), repeat=len(variables)):
                target = list(state)
                for index, bit in zip(variables, replacement):
                    target[index] = bit
                target_index = states.index(tuple(target))
                targets[target_index] = targets.get(target_index, 0) + 1
        denominator = 1 if chosen is None else 2 ** len(chosen[1])
        kernel = [(target, Fraction(count, denominator)) for target, count in sorted(targets.items())]
        kernels[state_index] = kernel
        transitions.append({
            "state": "".join(map(str, state)),
            "chosen_event": None if chosen is None else chosen[0],
            "targets": [{"state": "".join(map(str, states[target])), "probability": q(probability)}
                        for target, probability in kernel],
        })
    position = {state: index for index, state in enumerate(transient)}
    matrix = [[Fraction(int(i == j)) for j in range(len(transient))]
              for i in range(len(transient))]
    for state in transient:
        row = position[state]
        for target, probability in kernels[state]:
            if target in position:
                matrix[row][position[target]] -= probability
    expected = []
    for label in labels:
        rhs = [Fraction(chosen_by_state[state] == label) for state in transient]
        values = solve(matrix, rhs)
        initial = sum(values) / len(states)
        expected.append(initial)
    degree = 6
    series = {label: [Fraction(0)] * (degree + 1) for label in labels}
    probabilities = {event[0]: Fraction(1, 2 ** len(event[1])) for event in events}
    for _ in range(degree):
        updated = {}
        for label in labels:
            product = [Fraction(1)] + [Fraction(0)] * degree
            for child in [label] + dependencies[label]:
                factor = list(series[child])
                factor[0] += 1
                product = poly_mul(product, factor, degree)
            updated[label] = [Fraction(0)] + [probabilities[label] * value for value in product[:-1]]
        series = updated
    event_rows = []
    for event in events:
        label, variables, pattern, witness = event
        rhs = witness * math.prod(1 - by_label[neighbor][3] for neighbor in dependencies[label])
        event_rows.append({
            "label": label,
            "variables": list(variables),
            "pattern": list(pattern),
            "probability": q(probabilities[label]),
            "witness_x": q(witness),
            "dependencies": dependencies[label],
            "lll_rhs": q(rhs),
            "expectation_bound": q(witness / (1 - witness)),
            "witness_tree_weight_by_size_1_to_6": [q(value) for value in series[label][1:]],
        })
    return {
        "name": name,
        "variable_count": variable_count,
        "event_rows": event_rows,
        "valid_assignment_count": sum(chosen_by_state[index] is None for index in range(len(states))),
        "expected_resamplings_by_event": [
            {"label": label, "value": q(value)} for label, value in zip(labels, expected)
        ],
        "expected_total_resamplings": q(sum(expected)),
        "transition_rows": transitions,
    }


def leaves(value):
    if type(value) is dict:
        return sum(leaves(item) for item in value.values())
    if type(value) is list:
        return sum(leaves(item) for item in value)
    return 1


def produce():
    evaluation = strict_yaml(EVALUATION)
    data = {
        "schema": "hcs-c325-moser-tardos-v1",
        "candidate_id": "HCS-C325",
        "obstruction_id": "HEN-O309",
        "evaluation_date": "2026-09-03",
        "fixed_epoch": EPOCH,
        "source_commit": SOURCE,
        "scope_literal": SCOPE,
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR,
                      "authority": "flow_systems/skills/route-a-evaluator.md"},
        "model": {
            "variable_model": "finite mutually independent variables with finite domains",
            "dependence": "two distinct bad events are adjacent exactly when they share a variable",
            "randomness": "independent infinite resampling table for every variable",
            "selection_rule": "arbitrary legal currently violated event; finite evidence uses lexicographic order",
        },
        "theorem_contract": {
            "criterion": "P(A)<=x_A product_{B in Gamma(A)}(1-x_B), with every x_A in (0,1)",
            "termination": "almost sure finite termination for every legal sequential violated-event rule",
            "output": "the terminal assignment avoids every bad event",
            "per_event_bound": "E[N_A]<=x_A/(1-x_A)",
            "total_bound": "E[sum_A N_A]<=sum_A x_A/(1-x_A)",
            "proof": "resampling-table witness lemma plus proper-tree branching-process bound",
        },
        "finite_grid": {"instances": 3, "max_variables": 6, "witness_tree_size_max": 6,
                        "domains": "binary fair variables"},
        "instance_rows": [instance_row(*specification) for specification in specifications()],
        "route_a_yaml": {
            "relative_path": "evaluations/route_a/HCS-C325/2026-09-03.yaml",
            "raw_sha256": hashlib.sha256(EVALUATION.read_bytes()).hexdigest(),
            "semantic_sha256": hashlib.sha256(json.dumps(
                evaluation, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest(),
        },
        "collision_boundary": {
            "C192": "a fixed hyperplane chamber walk is not an adaptive bad-event resampling algorithm",
            "C302": "Quicksort has a recursive cost contraction, not shared-variable witness trees",
            "C317": "Newton--Schulz is deterministic matrix iteration, not randomized constraint repair",
        },
        "route_a": {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
                    "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False},
        "scope_flags": FLAGS,
        "nonclaims": [
            "Finite assignment chains and size-six witness trees do not prove the general theorem.",
            "No lopsided, permutation, parallel, or outside-criterion resampling theorem is asserted.",
            "No literature-priority claim is made.",
            "No target arithmetic datum, Euler factor, root number, automorphy, target divisor, functional equation, target zero match, or Hilbert--Polya operator is asserted.",
        ],
        "references": [
            {"authors": "Robin A. Moser and Gabor Tardos",
             "title": "A constructive proof of the general Lovasz Local Lemma",
             "identifier": "10.1145/1667053.1667060"},
            {"authors": "Robin A. Moser and Gabor Tardos", "title": "author preprint",
             "identifier": "arXiv:0903.0544"},
        ],
    }
    counted = dict(data)
    data["enumeration"] = {
        "instance_rows": len(data["instance_rows"]),
        "state_rows": sum(len(row["transition_rows"]) for row in data["instance_rows"]),
        "event_rows": sum(len(row["event_rows"]) for row in data["instance_rows"]),
        "audited_leaf_count": leaves(counted),
    }
    body = dict(data)
    data["payload_sha256"] = hashlib.sha256(json.dumps(
        body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    return data


def main():
    if sys.flags.optimize:
        raise RuntimeError("C325 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    data = produce()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(f"C325_PRODUCER_PASS {data['payload_sha256']} {data['enumeration']['state_rows']}")


if __name__ == "__main__":
    main()
