#!/usr/bin/env python3
"""Independent exact checker for HCS-C321; imports no producer code."""
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
DEFAULT = ROOT / "results/c321_preferential_attachment_evidence.json"
DEFAULT_YAML = ROOT / "evaluations/route_a/HCS-C321/2026-09-03.yaml"
SOURCE = "1ccbfe2d759fe007c6b53c9646e1ab031878b34a"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EVALUATION_RAW = "a8f62dc0ddb1546c7a5174b59e7ecffce201530d3a462e72ecf0ff3644dc9ec5"
EVALUATION_SEMANTIC = "cc1b0fbf9fdc348a592adecbe6682ea789dd1706275ab39916a3fa8731408014"


def strict_json(path: Path):
    def pairs(items):
        out = {}
        for key, value in items:
            if key in out:
                raise ValueError(f"duplicate JSON key {key}")
            out[key] = value
        return out
    value = json.loads(path.read_text(), object_pairs_hook=pairs,
                       parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)))
    if type(value) is not dict:
        raise ValueError("JSON root must be an object")
    return value


class UniqueLoader(yaml.SafeLoader):
    pass


UniqueLoader.yaml_implicit_resolvers = {
    key: [(tag, regexp) for tag, regexp in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def construct_unique(loader, node, deep=False):
    out = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in out:
            raise ValueError("duplicate or non-string YAML key")
        out[key] = loader.construct_object(value_node, deep=deep)
    return out


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_unique)


def strict_yaml(path: Path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML aliases forbidden")
    value = yaml.load(raw, Loader=UniqueLoader)
    if type(value) is not dict:
        raise ValueError("YAML root")
    return value


def frac(text) -> Fraction:
    if type(text) is not str:
        raise TypeError("fraction must be a string")
    value = Fraction(text)
    if fs(value) != text:
        raise ValueError("noncanonical fraction")
    return value


def fs(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def rise(value: int, order: int) -> int:
    answer = 1
    for offset in range(order):
        answer *= value + offset
    return answer


def theoretical(n: int, birth: int, order: int) -> Fraction:
    answer = Fraction(math.factorial(order))
    for time in range(birth, n):
        answer *= Fraction(2 * time - 2 + order, 2 * time - 2)
    return answer


def aggregate_histories(nmax: int):
    """Enumerate every parent history; do not merge until each time ledger is formed."""
    histories = [((1, 1), Fraction(1))]
    ledgers = {}
    for n in range(2, nmax + 1):
        merged = {}
        for degrees, probability in histories:
            merged[degrees] = merged.get(degrees, Fraction(0)) + probability
        ledgers[n] = (histories, merged)
        if n == nmax:
            break
        nxt = []
        for degrees, probability in histories:
            if sum(degrees) != 2 * (n - 1):
                raise AssertionError("degree conservation")
            for chosen, degree in enumerate(degrees):
                child = list(degrees)
                child[chosen] += 1
                child.append(1)
                nxt.append((tuple(child), probability * Fraction(degree, 2 * (n - 1))))
        histories = nxt
    return ledgers


def leaves(value) -> int:
    if type(value) is dict:
        return sum(leaves(v) for v in value.values())
    if type(value) is list:
        return sum(leaves(v) for v in value)
    return 1


def exact_keys(value, expected, label):
    if type(value) is not dict or set(value) != set(expected):
        raise AssertionError(f"{label} keys")


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C321 checker refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_YAML)
    args = parser.parse_args()
    data = strict_json(args.evidence)
    checks = 0

    exact_keys(data, {"schema", "candidate_id", "obstruction_id", "evaluation_date", "fixed_epoch",
                      "source_commit", "scope_literal", "evaluator", "model", "theorem_contract",
                      "finite_grid", "time_rows", "terminal_degree_vector_distribution", "profile_rows",
                      "route_a_yaml", "collision_boundary", "route_a", "scope_flags", "nonclaims",
                      "references", "audited_leaf_count", "payload_sha256"}, "evidence root")

    required = {
        "schema": "hcs-c321-preferential-attachment-v1",
        "candidate_id": "HCS-C321",
        "obstruction_id": "HEN-O305",
        "evaluation_date": "2026-09-03",
        "source_commit": SOURCE,
        "scope_literal": SCOPE,
        "fixed_epoch": 1788393600,
    }
    for key, value in required.items():
        if data.get(key) != value:
            raise AssertionError(key)
        checks += 1
    if data.get("evaluator") != {"version": "0.2.0", "sha256": EVALUATOR}:
        raise AssertionError("evaluator")
    checks += 1
    body = dict(data)
    supplied = body.pop("payload_sha256")
    semantic = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"),
                                           ensure_ascii=False).encode()).hexdigest()
    if supplied != semantic:
        raise AssertionError("payload hash")
    counted = dict(data)
    counted.pop("payload_sha256")
    if data["audited_leaf_count"] != leaves(counted):
        raise AssertionError("leaf count")
    checks += 2

    model = data["model"]
    exact_model = {
        "initial_tree": "T_2 is the single edge {1,2}",
        "self_loops": False,
        "multiple_edges": False,
        "update": "vertex n+1 attaches to old v with probability d_v(n)/(2(n-1))",
        "clock": "n equals the number of vertices",
        "fixed_observable": "D_i(n) is the degree of one fixed labeled vertex",
        "population_observable": "N_k(n) counts all degree-k vertices",
    }
    if model != exact_model:
        raise AssertionError("frozen model")
    expected_theorem = {
        "fixed_moments": "all integer rising-factorial orders with the s_i birth-time split",
        "fixed_limit": "D_i(n)/sqrt(n) converges almost surely and in every finite Lp",
        "limit_moments": "r! Gamma(s_i-1)/Gamma(s_i-1+r/2), moment determinate by Carleman",
        "population_limit": "for fixed k, N_k(n)/n converges in L2 to 4/[k(k+1)(k+2)]",
        "excluded": "no maximum-degree, joint-hub, m>1, self-loop, or uniform-in-k theorem",
        "evidence_boundary": "finite exact enumeration is regression evidence only",
    }
    if data["theorem_contract"] != expected_theorem:
        raise AssertionError("theorem contract")
    exact_keys(data["finite_grid"], {"n_min", "n_max", "rising_order_max", "terminal_parent_histories"}, "grid")
    exact_keys(data["route_a_yaml"], {"relative_path", "raw_sha256", "semantic_sha256"}, "YAML lock")
    exact_keys(data["route_a"], {"tuple", "overall", "route_b_invocation_allowed"}, "route")
    exact_keys(data["scope_flags"], {"claims_target_arithmetic_local_data", "claims_target_euler_factors",
                                     "claims_root_number", "claims_automorphy",
                                     "claims_target_divisor_or_counting_law",
                                     "claims_target_functional_equation", "claims_target_zero_match",
                                     "claims_hilbert_polya_operator", "invokes_route_b"}, "scope flags")
    if data["theorem_contract"]["excluded"] != "no maximum-degree, joint-hub, m>1, self-loop, or uniform-in-k theorem":
        raise AssertionError("exclusions")
    if data["route_a"] != {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
                            "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}:
        raise AssertionError("route")
    if any(data["scope_flags"].values()):
        raise AssertionError("scope flags")
    if data["collision_boundary"] != {
        "C263": "a fixed-color Polya urn is exchangeable; attachment evolves a labeled tree and a degree population",
        "C276": "a uniform random mapping is sampled at fixed size; preferential attachment is sequential reinforced growth",
        "C307": "Erdos--Renyi connectivity uses independent edges; preferential attachment uses degree-biased dependent edges",
    }:
        raise AssertionError("collisions")
    if data["nonclaims"] != [
        "No finite computation is presented as an asymptotic proof.",
        "No theorem about maximum degree or a joint hub law is asserted.",
        "No result for a self-loop seed, the LCD convention, or m greater than one is asserted.",
        "No target arithmetic datum, Euler factor, root number, automorphy, target divisor, functional equation, zero match, or Hilbert--Polya operator is asserted.",
        "No literature-priority claim is made.",
    ]:
        raise AssertionError("nonclaims")
    checks += 4

    evaluation = strict_yaml(args.evaluation)
    yaml_keys = {"schema", "candidate_id", "title", "evaluation_date", "source_commit", "fixed_epoch",
                 "scope_literal", "evaluator_authority", "evaluator_version", "evaluator_authority_sha256",
                 "obstruction_id", "candidate_definition", "family", "phase_space", "dynamics", "parameters",
                 "parameter_provenance", "arithmetic_origin", "clock", "normalization", "determinant_convention",
                 "orbit_cutoff", "precision", "training_data", "forbidden_data", "artifact_paths", "a0", "a1",
                 "a2", "a3", "a4", "tuple", "overall_verdict", "route_b_invocation_allowed",
                 "route_b_lock_reason", "scope_flags", "theorem_status", "finite_evidence_role",
                 "source_owner_tokens"}
    exact_keys(evaluation, yaml_keys, "evaluation root")
    for branch in ("a0", "a1", "a2", "a3", "a4"):
        exact_keys(evaluation[branch], {"verdict", "evidence_status", "strongest_evidence", "strongest_failure"}, branch)
    exact_keys(evaluation["scope_flags"], data["scope_flags"], "evaluation scope flags")
    route_lock = data["route_a_yaml"]
    if route_lock["relative_path"] != "evaluations/route_a/HCS-C321/2026-09-03.yaml":
        raise AssertionError("YAML relative path")
    if hashlib.sha256(args.evaluation.read_bytes()).hexdigest() != route_lock["raw_sha256"] or route_lock["raw_sha256"] != EVALUATION_RAW:
        raise AssertionError("YAML raw hash")
    yaml_semantic = hashlib.sha256(json.dumps(evaluation, sort_keys=True, separators=(",", ":"),
                                                ensure_ascii=False).encode()).hexdigest()
    if yaml_semantic != route_lock["semantic_sha256"] or route_lock["semantic_sha256"] != EVALUATION_SEMANTIC:
        raise AssertionError("YAML semantic hash")
    if evaluation["candidate_id"] != "HCS-C321" or evaluation["source_commit"] != SOURCE:
        raise AssertionError("YAML identity")
    if evaluation["evaluator_authority"] != "flow_systems/skills/route-a-evaluator.md":
        raise AssertionError("YAML evaluator authority")
    if evaluation["tuple"] != ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"]:
        raise AssertionError("YAML tuple")
    if evaluation["overall_verdict"] != "ROUTE_A_REJECTED" or evaluation["route_b_invocation_allowed"] is not False:
        raise AssertionError("YAML verdict")
    if any(evaluation["scope_flags"].values()):
        raise AssertionError("YAML flags")
    if [evaluation[key]["evidence_status"] for key in ("a0", "a1", "a2", "a3", "a4")] != [
            "PROVED", "PROVED", "STOP_SCOPED", "STOP_SCOPED", "STOP_SCOPED"]:
        raise AssertionError("YAML evidence status")
    if evaluation["fixed_epoch"] != 1788393600 or type(evaluation["fixed_epoch"]) is not int:
        raise AssertionError("YAML typed epoch")
    if evaluation["training_data"] != "none" or type(evaluation["route_b_invocation_allowed"]) is not bool:
        raise AssertionError("YAML typed invariants")
    if evaluation["evaluator_authority_sha256"] != EVALUATOR or evaluation["scope_literal"] != SCOPE:
        raise AssertionError("YAML authority/scope")
    if evaluation["source_owner_tokens"] != ["10.1126/science.286.5439.509", "10.1002/rsa.1009", "10.1214/ECP.v16-1598"]:
        raise AssertionError("YAML source tokens")
    if data["references"] != [
        {"identifier": "10.1126/science.286.5439.509", "role": "historical preferential-attachment model"},
        {"identifier": "10.1002/rsa.1009", "role": "rigorous degree-sequence lineage with a distinct convention"},
        {"identifier": "10.1214/ECP.v16-1598", "role": "fixed-vertex degree-limit lineage with convention audit"},
    ]:
        raise AssertionError("references")
    checks += 6

    grid = data["finite_grid"]
    if grid != {"n_min": 2, "n_max": 9, "rising_order_max": 8,
                "terminal_parent_histories": 40320}:
        raise AssertionError("grid")
    ledgers = aggregate_histories(9)
    rows = data["time_rows"]
    if [row["n"] for row in rows] != list(range(2, 10)):
        raise AssertionError("time keys")
    for row in rows:
        exact_keys(row, {"n", "state_count", "labeled_parent_history_count", "total_mass",
                         "vertex_count_identity", "degree_sum_identity", "conditional_drift_cells_checked",
                         "fixed_vertex_moments", "degree_population_moments"}, "time row")
        n = row["n"]
        histories, merged = ledgers[n]
        if row["state_count"] != len(merged) or row["labeled_parent_history_count"] != math.factorial(n - 1):
            raise AssertionError("state/history count")
        if frac(row["total_mass"]) != 1 or len(histories) != math.factorial(n - 1):
            raise AssertionError("history mass")
        if row["vertex_count_identity"] != n or row["degree_sum_identity"] != 2 * (n - 1):
            raise AssertionError("conservation metadata")
        for degrees in merged:
            if len(degrees) != n or sum(degrees) != 2 * (n - 1):
                raise AssertionError("state conservation")
        expected_fixed = n * 8
        if len(row["fixed_vertex_moments"]) != expected_fixed:
            raise AssertionError("fixed row count")
        if [(cell.get("vertex"), cell.get("order")) for cell in row["fixed_vertex_moments"]] != [
                (i, r) for i in range(1, n + 1) for r in range(1, 9)]:
            raise AssertionError("fixed coordinates")
        for cell in row["fixed_vertex_moments"]:
            exact_keys(cell, {"vertex", "birth_time", "order", "observed", "formula"}, "fixed cell")
            i, birth, order = cell["vertex"], cell["birth_time"], cell["order"]
            if birth != (2 if i <= 2 else i) or not (1 <= i <= n and 1 <= order <= 8):
                raise AssertionError("birth/order")
            observed = sum((probability * rise(degrees[i - 1], order)
                            for degrees, probability in merged.items()), Fraction(0))
            formula = theoretical(n, birth, order)
            if frac(cell["observed"]) != observed or frac(cell["formula"]) != formula or observed != formula:
                raise AssertionError("fixed moment")
            checks += 3
        if len(row["degree_population_moments"]) != n - 1:
            raise AssertionError("population row count")
        if [cell.get("degree") for cell in row["degree_population_moments"]] != list(range(1, n)):
            raise AssertionError("population coordinates")
        for cell in row["degree_population_moments"]:
            exact_keys(cell, {"degree", "mean", "second_moment", "variance"}, "population cell")
            k = cell["degree"]
            values = [(sum(degree == k for degree in degrees), probability)
                      for degrees, probability in merged.items()]
            mean = sum((count * probability for count, probability in values), Fraction(0))
            second = sum((count * count * probability for count, probability in values), Fraction(0))
            if frac(cell["mean"]) != mean or frac(cell["second_moment"]) != second:
                raise AssertionError("population moments")
            if frac(cell["variance"]) != second - mean * mean:
                raise AssertionError("population variance")
            checks += 3
        if row["conditional_drift_cells_checked"] != len(merged) * (n - 1):
            raise AssertionError("drift cell count")
        checks += 6

    terminal_rows = data["terminal_degree_vector_distribution"]
    if type(terminal_rows) is not list or len(terminal_rows) != 1430:
        raise AssertionError("terminal row count")
    for cell in terminal_rows:
        exact_keys(cell, {"degrees", "probability"}, "terminal cell")
        if type(cell["degrees"]) is not list or len(cell["degrees"]) != 9 or any(type(x) is not int for x in cell["degrees"]):
            raise AssertionError("terminal degree tuple")
    terminal_coordinates = [tuple(cell["degrees"]) for cell in terminal_rows]
    if len(set(terminal_coordinates)) != len(terminal_coordinates):
        raise AssertionError("duplicate terminal coordinate")
    terminal = {tuple(cell["degrees"]): frac(cell["probability"]) for cell in terminal_rows}
    if terminal != ledgers[9][1]:
        raise AssertionError("terminal distribution")
    checks += len(terminal)

    if type(data["profile_rows"]) is not list or len(data["profile_rows"]) != 12:
        raise AssertionError("profile row count")
    if [row.get("degree") for row in data["profile_rows"]] != list(range(1, 13)):
        raise AssertionError("profile coordinates")
    cumulative = Fraction(0)
    weighted = Fraction(0)
    previous = Fraction(0)
    for k, row in enumerate(data["profile_rows"], 1):
        exact_keys(row, {"degree", "p_k", "recurrence_rhs", "partial_mass", "partial_mean_degree"}, "profile cell")
        if row["degree"] != k:
            raise AssertionError("profile key")
        p = Fraction(4, k * (k + 1) * (k + 2))
        rhs = Fraction(int(k == 1)) + (k - 1) * previous / 2 - k * p / 2
        cumulative += p
        weighted += k * p
        if [frac(row[name]) for name in ("p_k", "recurrence_rhs", "partial_mass", "partial_mean_degree")] != [p, rhs, cumulative, weighted]:
            raise AssertionError("profile")
        previous = p
        checks += 5

    print(f"C321 independent checker: PASS ({checks} checks, {len(ledgers[9][0])} weighted histories)")


if __name__ == "__main__":
    main()
