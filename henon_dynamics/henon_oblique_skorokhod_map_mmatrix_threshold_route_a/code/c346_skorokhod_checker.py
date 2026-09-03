#!/usr/bin/env python3
"""Producer-independent exact and semantic checker for HCS-C346."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from fractions import Fraction as F
from math import isqrt
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c346_skorokhod_evidence.json"
DEFAULT_EVAL = ROOT / "evaluations/route_a/HCS-C346/2026-09-03.yaml"
SOURCE = "1af63b945e19b5f94ac1cb76f93af5ac66d3d562"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EVAL_RAW = "4cad63c30708b42af42f3ee1f3563e8d31b2de8ae08047170c6b93050474a36c"
EVAL_SEMANTIC = "a9363fdab6fc2cd797ced2beb1d1f277876db3afcd69cbf37a8ad7f9de18fe4a"
CASES = (
    (F(1, 4), F(1, 4), "symmetric_corner", ((0, 0), (-1, 0), (-1, -1), (0, -2), (-3, 1), (1, 1))),
    (F(4, 9), F(1, 4), "asymmetric_corner", ((1, 0), (0, -1), (-2, -1), (1, -3), (-1, 2), (2, 2))),
    (F(9, 16), F(1, 9), "weak_return", ((0, 2), (-1, 1), (-2, -3), (1, -1), (-4, 0), (0, 0))),
    (F(0), F(3, 2), "lower_triangular", ((0, 0), (-1, 0), (0, -2), (-2, -1), (2, -4), (1, 0))),
    (F(2), F(0), "upper_triangular", ((1, 1), (-2, 0), (0, -1), (-3, 2), (1, -4), (0, 0))),
    (F(0), F(0), "normal_reflection", ((0, 0), (-1, 2), (-3, -1), (1, -4), (-2, 0), (2, 2))),
)


def object_pairs(items):
    out = {}
    for key, value in items:
        if key in out:
            raise ValueError(f"duplicate JSON key: {key}")
        out[key] = value
    return out


def strict_json(path: Path):
    return json.loads(path.read_text(), object_pairs_hook=object_pairs,
                      parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))


class UniqueLoader(yaml.SafeLoader):
    pass


UniqueLoader.yaml_implicit_resolvers = {
    key: [(tag, pattern) for tag, pattern in values if tag != "tag:yaml.org,2002:timestamp"]
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
            raise ValueError("YAML anchors and aliases forbidden")
    return yaml.load(raw, Loader=UniqueLoader)


def semantic_hash(value) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return semantic_hash(body)


def leaves(value) -> int:
    if type(value) is dict:
        return sum(leaves(v) for v in value.values())
    if type(value) is list:
        return sum(leaves(v) for v in value)
    return 1


def frac(text) -> F:
    if type(text) is not str or not re.fullmatch(r"-?(?:0|[1-9][0-9]*)(?:/[1-9][0-9]*)?", text):
        raise AssertionError("noncanonical rational syntax")
    value = F(text)
    expected = str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"
    if text != expected:
        raise AssertionError("non-reduced rational")
    return value


def get_pair(raw) -> tuple[F, F]:
    if type(raw) is not list or len(raw) != 2:
        raise AssertionError("pair schema")
    return frac(raw[0]), frac(raw[1])


def state(x, y, rho, sigma):
    return x[0] + y[0] - rho * y[1], x[1] - sigma * y[0] + y[1]


def running_map(nodes, rows, rho, sigma):
    a = b = F(0)
    answer = []
    for x, y in zip(nodes, rows):
        a = max(a, -F(x[0]) + rho * y[1])
        b = max(b, -F(x[1]) + sigma * y[0])
        answer.append((a, b))
    return answer


def active_set_solutions(z0, rho, sigma):
    """Independent exhaustive support solve for the event LCP."""
    answers = set()
    for mask in range(4):
        if mask == 0:
            d = (F(0), F(0))
        elif mask == 1:
            d = (-z0[0], F(0))
        elif mask == 2:
            d = (F(0), -z0[1])
        else:
            det = 1 - rho * sigma
            if det == 0:
                continue
            d = ((-z0[0] - rho * z0[1]) / det,
                 (-sigma * z0[0] - z0[1]) / det)
        z = (z0[0] + d[0] - rho * d[1], z0[1] - sigma * d[0] + d[1])
        if min(d) >= 0 and min(z) >= 0 and d[0] * z[0] == 0 and d[1] * z[1] == 0:
            answers.add(d)
    return answers


def solve_expected(nodes, rho, sigma):
    y = (F(0), F(0))
    out = []
    for index, raw in enumerate(nodes):
        x = (F(raw[0]), F(raw[1]))
        z0 = state(x, y, rho, sigma)
        if index == 0:
            d = (F(0), F(0))
        else:
            candidates = active_set_solutions(z0, rho, sigma)
            if len(candidates) != 1:
                raise AssertionError("fixture event is not uniquely solvable")
            d = next(iter(candidates))
        y = y[0] + d[0], y[1] + d[1]
        out.append(y)
    return out


def rational_sqrt(value: F) -> F:
    p, q = isqrt(value.numerator), isqrt(value.denominator)
    if p * p != value.numerator or q * q != value.denominator:
        raise AssertionError("non-square fixture")
    return F(p, q)


def weighted_norm(rows, w1, w2):
    return max((max(abs(a) / w1, abs(b) / w2) for a, b in rows), default=F(0))


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C346 checker refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_EVAL)
    args = parser.parse_args()
    data = strict_json(args.evidence)
    evaluation = strict_yaml(args.evaluation)
    checks = 0
    if hashlib.sha256(args.evaluation.read_bytes()).hexdigest() != EVAL_RAW or semantic_hash(evaluation) != EVAL_SEMANTIC:
        raise AssertionError("evaluation digest")
    if payload_hash(data) != data.get("payload_sha256"):
        raise AssertionError("payload digest")
    checks += 3
    top = {"schema", "candidate_id", "obstruction_id", "evaluation_date", "fixed_epoch", "source_commit", "scope_literal", "evaluator", "evaluation_lock", "model", "theorem_contract", "case_rows", "threshold_rows", "boundary_atlas", "collision_boundary", "route_a", "scope_flags", "nonclaims", "references", "enumeration", "payload_sha256"}
    if type(data) is not dict or set(data) != top:
        raise AssertionError("top-level schema")
    identity = tuple(data[k] for k in ("schema", "candidate_id", "obstruction_id", "evaluation_date", "fixed_epoch", "source_commit", "scope_literal"))
    if identity != ("hcs-c346-oblique-skorokhod-v1", "HCS-C346", "HEN-O330", "2026-09-03", 1788393600, SOURCE, SCOPE):
        raise AssertionError("identity")
    if data["evaluator"] != {"authority": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR}:
        raise AssertionError("evaluator")
    if data["evaluation_lock"] != {"relative_path": "evaluations/route_a/HCS-C346/2026-09-03.yaml", "raw_sha256": EVAL_RAW, "semantic_sha256": EVAL_SEMANTIC}:
        raise AssertionError("evaluation lock")
    expected_route = {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"], "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}
    if data["route_a"] != expected_route:
        raise AssertionError("Route-A ledger")
    flag_keys = {"claims_target_arithmetic_local_data", "claims_target_euler_factors", "claims_root_number", "claims_automorphy", "claims_target_divisor_or_counting_law", "claims_target_functional_equation", "claims_target_zero_match", "claims_hilbert_polya_operator", "invokes_route_b"}
    if set(data["scope_flags"]) != flag_keys or any(type(v) is not bool or v for v in data["scope_flags"].values()):
        raise AssertionError("scope flags")
    static_lengths = (len(data["model"]), len(data["theorem_contract"]), len(data["boundary_atlas"]), len(data["collision_boundary"]), len(data["nonclaims"]), len(data["references"]))
    if static_lengths != (4, 7, 6, 4, 5, 2):
        raise AssertionError("static theorem/source boundary")
    if data["theorem_contract"]["sharp_threshold"] != "the problem has a unique solution for every input exactly when rho sigma is strictly below one":
        raise AssertionError("sharp threshold semantics")
    if data["theorem_contract"]["fixed_point"] != "y1=L(x1-rho y2) and y2=L(x2-sigma y1), with L(f)(t)=sup over s<=t of [-f(s)] positive part; x(0) nonnegative and rho sigma below one force y(0)=0":
        raise AssertionError("fixed-point initial-value closure")
    if [item["doi"] for item in data["references"]] != ["10.1214/aop/1176994471", "10.1080/17442509108833688"]:
        raise AssertionError("source ownership")
    checks += 18

    eval_top = {"schema", "candidate_id", "title", "evaluation_date", "source_commit", "fixed_epoch", "scope_literal", "evaluator_authority", "evaluator_version", "evaluator_authority_sha256", "obstruction_id", "candidate_definition", "family", "phase_space", "dynamics", "parameters", "parameter_provenance", "arithmetic_origin", "clock", "normalization", "determinant_convention", "orbit_cutoff", "precision", "training_data", "forbidden_data", "artifact_paths", "a0", "a1", "a2", "a3", "a4", "tuple", "overall_verdict", "route_b_invocation_allowed", "route_b_lock_reason", "scope_flags", "theorem_status", "finite_evidence_role", "source_owner_tokens"}
    if type(evaluation) is not dict or set(evaluation) != eval_top:
        raise AssertionError("evaluation schema")
    layer_keys = {"verdict", "evidence_status", "strongest_evidence", "strongest_failure"}
    if any(type(evaluation[k]) is not dict or set(evaluation[k]) != layer_keys for k in ("a0", "a1", "a2", "a3", "a4")):
        raise AssertionError("evaluation layer schema")
    eval_identity = (evaluation["schema"], evaluation["candidate_id"], evaluation["obstruction_id"], evaluation["evaluation_date"], evaluation["source_commit"], evaluation["fixed_epoch"], evaluation["scope_literal"], evaluation["evaluator_authority"], evaluation["evaluator_version"], evaluation["evaluator_authority_sha256"])
    if eval_identity != ("route-a-evaluation-v0.2.0", "HCS-C346", "HEN-O330", "2026-09-03", SOURCE, 1788393600, SCOPE, "flow_systems/skills/route-a-evaluator.md", "0.2.0", EVALUATOR):
        raise AssertionError("evaluation identity")
    if evaluation["artifact_paths"] != ["results/c346_skorokhod_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"]:
        raise AssertionError("artifact paths")
    verdicts = [evaluation[k]["verdict"] for k in ("a0", "a1", "a2", "a3", "a4")]
    if verdicts != expected_route["tuple"] or evaluation["tuple"] != verdicts or evaluation["overall_verdict"] != "ROUTE_A_REJECTED" or evaluation["route_b_invocation_allowed"] is not False:
        raise AssertionError("evaluation verdicts")
    if evaluation["scope_flags"] != data["scope_flags"] or evaluation["theorem_status"] != "PROVABLE_AS_STATED":
        raise AssertionError("evaluation scope/status")
    if evaluation["source_owner_tokens"] != ["10.1214/aop/1176994471", "10.1080/17442509108833688"]:
        raise AssertionError("evaluation owners")
    if evaluation["a0"]["evidence_status"] != "PROVED" or evaluation["a1"]["evidence_status"] != "PROVED" or any(evaluation[k]["evidence_status"] != "STOP_SCOPED" for k in ("a2", "a3", "a4")):
        raise AssertionError("evaluation status discipline")
    checks += 38

    rows = data["case_rows"]
    if type(rows) is not list or len(rows) != len(CASES):
        raise AssertionError("case count")
    event_total = picard_total = 0
    row_keys = {"case_id", "label", "rho", "sigma", "determinant", "well_posed", "event_rows", "fixed_point_check", "stretched_event_count", "pause_reparameterization_check", "picard_rows"}
    event_keys = {"event", "input", "regulator_increment", "regulator", "state", "active_axes", "nonnegative_and_complementary"}
    picard_keys = {"iteration", "successive_norm", "fixed_point_error", "contraction_check"}
    for index, (row, fixture) in enumerate(zip(rows, CASES), 1):
        rho, sigma, label, nodes = fixture
        if type(row) is not dict or set(row) != row_keys:
            raise AssertionError("case schema")
        if (row["case_id"], row["label"], frac(row["rho"]), frac(row["sigma"]), frac(row["determinant"]), row["well_posed"]) != (f"sk-{index:02d}", label, rho, sigma, 1 - rho * sigma, True):
            raise AssertionError("case identity")
        expected_y = solve_expected(nodes, rho, sigma)
        events = row["event_rows"]
        if type(events) is not list or len(events) != len(nodes):
            raise AssertionError("event count")
        previous = (F(0), F(0))
        parsed_y = []
        for j, (event, raw_x, want_y) in enumerate(zip(events, nodes, expected_y)):
            if type(event) is not dict or set(event) != event_keys:
                raise AssertionError("event schema")
            x, d, y, z = get_pair(event["input"]), get_pair(event["regulator_increment"]), get_pair(event["regulator"]), get_pair(event["state"])
            if event["event"] != j or x != (F(raw_x[0]), F(raw_x[1])) or y != want_y:
                raise AssertionError("event identity/solution")
            if d != (y[0] - previous[0], y[1] - previous[1]) or min(d) < 0:
                raise AssertionError("regulator monotonicity")
            if z != state(x, y, rho, sigma) or min(z) < 0 or d[0] * z[0] != 0 or d[1] * z[1] != 0:
                raise AssertionError("state/complementarity")
            active = [axis + 1 for axis, value in enumerate(d) if value > 0]
            if event["active_axes"] != active or event["nonnegative_and_complementary"] is not True:
                raise AssertionError("active ledger")
            if j > 0:
                z0 = state(x, previous, rho, sigma)
                candidates = active_set_solutions(z0, rho, sigma)
                if candidates != {d}:
                    raise AssertionError("event LCP uniqueness")
            previous = y
            parsed_y.append(y)
            checks += 14
        if running_map(nodes, parsed_y, rho, sigma) != parsed_y or row["fixed_point_check"] is not True:
            raise AssertionError("running-supremum fixed point")
        stretched = tuple(node for original in nodes for node in (original, original))
        stretched_y = solve_expected(stretched, rho, sigma)
        if [stretched_y[2 * j + 1] for j in range(len(nodes))] != parsed_y or row["stretched_event_count"] != 2 * len(nodes) or row["pause_reparameterization_check"] is not True:
            raise AssertionError("pause reparameterization")
        pics = row["picard_rows"]
        if rho == 0 or sigma == 0:
            if pics != []:
                raise AssertionError("triangular Picard boundary")
        else:
            if type(pics) is not list or len(pics) != 9:
                raise AssertionError("Picard row count")
            w1, w2, q = rational_sqrt(rho), rational_sqrt(sigma), rational_sqrt(rho * sigma)
            current = [(F(0), F(0)) for _ in nodes]
            previous_delta = None
            for iteration, item in enumerate(pics, 1):
                if type(item) is not dict or set(item) != picard_keys:
                    raise AssertionError("Picard schema")
                nxt = running_map(nodes, current, rho, sigma)
                delta = weighted_norm([(a - c, b - d) for (a, b), (c, d) in zip(nxt, current)], w1, w2)
                error = weighted_norm([(a - c, b - d) for (a, b), (c, d) in zip(parsed_y, nxt)], w1, w2)
                contraction = previous_delta is None or delta <= q * previous_delta
                if (item["iteration"], frac(item["successive_norm"]), frac(item["fixed_point_error"]), item["contraction_check"]) != (iteration, delta, error, contraction) or not contraction:
                    raise AssertionError("Picard contraction ledger")
                current, previous_delta = nxt, delta
                checks += 8
        event_total += len(events)
        picard_total += len(pics)
        checks += 9

    thresholds = data["threshold_rows"]
    if type(thresholds) is not dict or set(thresholds) != {"critical_nonuniqueness", "negative_jump_nonexistence"}:
        raise AssertionError("threshold schema")
    expected_h = ((0, 0, 0), (0, 1, 1), (0, 1, 2))
    for row, h in zip(thresholds["critical_nonuniqueness"], expected_h):
        if row["h"] != [str(x) for x in h] or row["regulator"] != [[str(x), str(x)] for x in h] or row["state"] != [["0", "0"] for _ in h] or row["valid"] is not True:
            raise AssertionError("critical nonuniqueness")
        if any(b < a for a, b in zip(h, h[1:])):
            raise AssertionError("invalid h witness")
        checks += 8
    threshold_params = ((F(1), F(1), "critical"), (F(2), F(1), "supercritical"), (F(1, 2), F(3), "supercritical_asymmetric"))
    for row, (rho, sigma, label) in zip(thresholds["negative_jump_nonexistence"], threshold_params):
        solutions = active_set_solutions((F(-1), F(-1)), rho, sigma)
        if row != {"label": label, "rho": str(rho), "sigma": str(sigma), "product": str(rho * sigma), "negative_jump": ["-1", "-1"], "lcp_candidate_count": 0} or solutions:
            raise AssertionError("threshold no-solution witness")
        checks += 7

    expected_enum = {"case_rows": 6, "event_rows": event_total, "picard_rows": picard_total, "critical_nonunique_witnesses": 3, "no_solution_witnesses": 3}
    enum = data["enumeration"]
    if type(enum) is not dict or set(enum) != set(expected_enum) | {"audited_leaf_count"} or any(enum[k] != v for k, v in expected_enum.items()):
        raise AssertionError("enumeration")
    body = dict(data)
    body.pop("payload_sha256")
    if enum["audited_leaf_count"] != leaves(body):
        raise AssertionError("leaf count")
    checks += 8
    print(f"C346 independent checker: PASS ({checks} checks)")


if __name__ == "__main__":
    main()
