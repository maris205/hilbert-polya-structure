#!/usr/bin/env python3
"""Repaired-hash, structural, duplicate-key, and stale-hash attacks for C285."""
from __future__ import annotations

import copy
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "results/c285_gordon_newell_evidence.json"


def ph(data: dict) -> str:
    clean = dict(data)
    clean.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(clean, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def assign(path, value):
    def mutate(data):
        target = data
        for key in path[:-1]:
            target = target[key]
        target[path[-1]] = copy.deepcopy(value)
    return mutate


def run_checker(path: Path) -> bool:
    env = dict(os.environ)
    env["C285_EVIDENCE"] = str(path)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    result = subprocess.run([sys.executable, "-B", str(ROOT / "code/c285_gordon_newell_checker.py")],
                            env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    return result.returncode != 0


base = json.loads(SOURCE.read_text())
mutations = [
    assign(("source_commit",), "0" * 40),
    assign(("fixed_epoch",), 1),
    assign(("scope_literal",), "BROKEN"),
    assign(("evaluator", "sha256"), "0" * 64),
    assign(("headline",), "repaired but false headline"),
    assign(("proof_contract", "status"), "HEURISTIC"),
    assign(("route_a", "tuple", 0), "A0_WEAK_ARITHMETIC_RELATION"),
    assign(("route_a", "overall"), "ROUTE_A_ACCEPTED"),
    assign(("route_a", "route_b_invocation_allowed"), True),
    assign(("scope_flags", "root_numbers"), True),
    assign(("model_contract", "traffic_gauge"), "tampered gauge"),
    assign(("asymptotic_contract", "joint_limit"), "tampered limit"),
    assign(("citation_contract", "classical_owner"), "anonymous owner"),
    assign(("collision_contract", "registry_range"), "HCS-C1 only"),
    assign(("boundary_contract", 0, "status"), "excluded"),
    assign(("nonclaims", 0), "originality claimed"),
    assign(("regression", "counts", "state_rows"), 176),
    assign(("regression", "case_rows", 0, "population"), 1),
    assign(("regression", "case_rows", 1, "routing", 0), []),
    assign(("regression", "case_rows", 2, "service_rates"), []),
    assign(("regression", "case_rows", 3, "traffic", 0), "99/1"),
    assign(("regression", "case_rows", 4, "weights"), []),
    assign(("regression", "case_rows", 5, "bottleneck_indices"), [0]),
    assign(("regression", "state_rows", 1, "state"), []),
    assign(("regression", "state_rows", 2, "unnormalized_weight"), "99/1"),
    assign(("regression", "state_rows", 3, "probability"), "0/1"),
    assign(("regression", "state_rows", 4, "left_balance"), "1/1"),
    assign(("regression", "z_rows", 2, "Z_N_direct"), "99/1"),
    assign(("regression", "z_rows", 3, "Z_N_minus_1"), "99/1"),
    assign(("regression", "z_rows", 4, "three_way_equal"), False),
    assign(("regression", "moment_rows", 2, "means"), []),
    assign(("regression", "moment_rows", 3, "covariance", 0), []),
    assign(("regression", "moment_rows", 1, "factorial_moments_through_degree_three", 0, "alpha"), []),
    assign(("regression", "moment_rows", 2, "factorial_moments_through_degree_three", 0, "value"), "99/1"),
    assign(("regression", "flow_rows", 2, "Z_ratio"), "99/1"),
    assign(("regression", "flow_rows", 3, "utilizations"), []),
    assign(("regression", "flow_rows", 4, "directed_edge_event_flows", 0), []),
    assign(("regression", "flow_rows", 5, "antisymmetric_net_currents", 0, 1), "99/1"),
    assign(("regression", "flow_rows", 6, "flow_conservation_residuals"), []),
    assign(("regression", "reversal_rows", 2, "reversed_routing", 0), []),
    assign(("regression", "reversal_rows", 3, "reversed_traffic"), []),
    assign(("regression", "reversal_rows", 4, "reversal_is_involution"), False),
    assign(("regression", "reversal_rows", 1, "state_process_reversible_for_positive_population"), True),
    assign(("regression", "reversal_rows", 5, "detailed_balance_defects", 0), []),
    assign(("regression", "boundary_rows", 5, "status"), "excluded"),
    assign(("regression", "condensation_rows", 8, "leading_ratio"), "99/1"),
    assign(("regression", "condensation_rows", 8, "bottleneck_scaled_means"), []),
]


def unknown_top(data):
    data["unexpected_top_level"] = "must fail closed"


def duplicate_case(data):
    data["regression"]["case_rows"][-1] = copy.deepcopy(data["regression"]["case_rows"][0])


def drop_replace_state(data):
    data["regression"]["state_rows"][-1] = copy.deepcopy(data["regression"]["state_rows"][0])


def drop_replace_condensation(data):
    data["regression"]["condensation_rows"][-1] = copy.deepcopy(data["regression"]["condensation_rows"][0])


def route_boolean_as_integer(data):
    data["route_a"]["route_b_invocation_allowed"] = 0


def scope_boolean_as_integer(data):
    data["scope_flags"]["root_numbers"] = 0


def rational_string_as_integer(data):
    data["regression"]["z_rows"][0]["Z_N_direct"] = 1


def state_integer_as_boolean(data):
    data["regression"]["state_rows"][0]["state"][0] = False


def case_boolean_as_integer(data):
    data["regression"]["case_rows"][0]["irreducible_routing"] = 1


def population_integer_as_boolean(data):
    data["regression"]["condensation_rows"][0]["population"] = False


def fixed_epoch_integer_as_boolean(data):
    data["fixed_epoch"] = True


def bottleneck_index_integer_as_boolean(data):
    data["regression"]["case_rows"][0]["bottleneck_indices"][0] = False


def noncanonical_fraction_text(data):
    data["regression"]["z_rows"][0]["Z_N_direct"] = "2/2"


def nested_string_as_integer(data):
    data["proof_contract"]["dependencies"][0] = 0


mutations.extend([
    unknown_top,
    duplicate_case,
    drop_replace_state,
    route_boolean_as_integer,
    scope_boolean_as_integer,
    rational_string_as_integer,
    state_integer_as_boolean,
    case_boolean_as_integer,
    population_integer_as_boolean,
    fixed_epoch_integer_as_boolean,
    bottleneck_index_integer_as_boolean,
    noncanonical_fraction_text,
    nested_string_as_integer,
])
assert len(mutations) == 60
rejected = 0
with tempfile.TemporaryDirectory(prefix="c285-gordon-newell-mutations-") as temp:
    directory = Path(temp)
    for index, mutation in enumerate(mutations):
        trial = copy.deepcopy(base)
        mutation(trial)
        trial["payload_sha256"] = ph(trial)
        path = directory / f"repaired-{index:02d}.json"
        path.write_text(json.dumps(trial, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
        rejected += run_checker(path)

    # An independent row-count-preserving condensation drop/replace.
    trial = copy.deepcopy(base)
    drop_replace_condensation(trial)
    trial["payload_sha256"] = ph(trial)
    path = directory / "repaired-condensation-drop-replace.json"
    path.write_text(json.dumps(trial, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    rejected += run_checker(path)

    stale = copy.deepcopy(base)
    stale["headline"] += " stale-hash tamper"
    path = directory / "stale-hash.json"
    path.write_text(json.dumps(stale, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    rejected += run_checker(path)

    duplicate_text = SOURCE.read_text().replace("{\n", "{\n  \"candidate_id\": \"HCS-C999\",\n", 1)
    path = directory / "duplicate-key.json"
    path.write_text(duplicate_text)
    rejected += run_checker(path)

    nested_marker = '        "three_way_equal": true\n'
    assert SOURCE.read_text().count(nested_marker) >= 1
    nested_duplicate = SOURCE.read_text().replace(
        nested_marker,
        '        "three_way_equal": true,\n        "three_way_equal": true\n',
        1,
    )
    path = directory / "nested-duplicate-key.json"
    path.write_text(nested_duplicate)
    rejected += run_checker(path)

total = len(mutations) + 4
assert total == 64
assert rejected == total
print(
    f"C285 hostile mutation audit: PASS {rejected}/{total} "
    "(60 repaired-hash semantic/structural/type attacks, condensation "
    "drop/replace, stale hash, and top/nested duplicate JSON keys)"
)
