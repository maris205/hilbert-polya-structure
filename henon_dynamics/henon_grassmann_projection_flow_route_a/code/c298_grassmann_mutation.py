#!/usr/bin/env python3
"""Hostile mutation suite for C298 JSON and Route-A YAML contracts."""
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
CHECKER = ROOT / "code/c298_grassmann_checker.py"
EVIDENCE = ROOT / "results/c298_grassmann_evidence.json"
YAML_PATH = ROOT / "evaluations/route_a/HCS-C298/2026-09-02.yaml"


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def set_path(data, path, value) -> None:
    cursor = data
    for key in path[:-1]:
        cursor = cursor[key]
    cursor[path[-1]] = value


def get_path(data, path):
    cursor = data
    for key in path:
        cursor = cursor[key]
    return cursor


def checker_run(evidence_text: str, yaml_text: str) -> subprocess.CompletedProcess:
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    with tempfile.TemporaryDirectory(prefix="c298-mutation-") as temporary:
        evidence_path = Path(temporary) / "evidence.json"
        yaml_path = Path(temporary) / "route.yaml"
        evidence_path.write_text(evidence_text)
        yaml_path.write_text(yaml_text)
        return subprocess.run(
            [sys.executable, "-B", str(CHECKER), "--evidence", str(evidence_path), "--yaml", str(yaml_path)],
            env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
        )


def main() -> None:
    raw = EVIDENCE.read_text()
    yaml_text = YAML_PATH.read_text()
    baseline = checker_run(raw, yaml_text)
    if baseline.returncode != 0:
        raise AssertionError(f"baseline checker failed:\n{baseline.stdout}\n{baseline.stderr}")
    base = json.loads(raw)
    mutations = []
    semantic = [
        (("schema",), "wrong"),
        (("candidate_id",), "HCS-C999"),
        (("obstruction_id",), "HEN-O999"),
        (("evaluation_date",), "1900-01-01"),
        (("source_commit",), "0" * 40),
        (("fixed_epoch",), 0),
        (("scope_literal",), "ALLOW_BAD_EULER"),
        (("evaluator", "sha256"), "0" * 64),
        (("model", "flow"), "dot(P)=0"),
        (("model", "exact_range"), "Ran(P(t))=Ran(P0)"),
        (("theorem_contract", "global_solution"), "finite time only"),
        (("theorem_contract", "simple_rate"), "ambient gap"),
        (("theorem_contract", "repeated_spectrum"), "one coordinate"),
        (("proof_contract", "matroid_guard"), "assume subset sums distinct"),
        (("proof_contract", "tie_guard"), "ties forbidden"),
        (("proof_contract", "rate_guard"), "ambient support"),
        (("proof_contract", "finite_role"), "finite cases prove theorem"),
        (("enumeration", "simple_cases", 1, "greedy_leading_subset"), [1, 4]),
        (("enumeration", "simple_cases", 1, "leading_weight"), 4),
        (("enumeration", "simple_cases", 1, "exact_rate_gap"), 3),
        (("enumeration", "simple_cases", 2, "plucker_support", 0, "minor"), 999),
        (("enumeration", "simple_cases", 4, "linear_modes", 0, "rate_lambda_j_minus_lambda_i"), 0),
        (("enumeration", "simple_cases", 0, "rational_initial_data", "commutator_frobenius_square"), "0"),
        (("enumeration", "repeated_cases", 0, "associated_graded_occupancies"), [0, 2]),
        (("enumeration", "repeated_cases", 3, "top_plucker_weight"), 5),
        (("enumeration", "repeated_cases", 4, "top_weight_coordinate_count"), 1),
        (("enumeration", "repeated_cases", 5, "filtration_intersection_dimensions"), [0, 0, 2]),
        (("enumeration", "morse_bott_atlases", 1, "components", 0, "stable_normal_dimension"), 999),
        (("enumeration", "audited_cell_count"), 188),
        (("route_a", "tuple", 4), "A4_NATURAL_QUANTIZATION"),
        (("route_a", "overall"), "ROUTE_A_STRONG_CANDIDATE"),
        (("route_a", "route_b_invocation_allowed"), True),
        (("route_a", "route_b_invocation_allowed"), 0),
        (("scope_flags", "claims_hilbert_polya_operator"), True),
        (("scope_flags", "claims_target_euler_factors"), 0),
        (("collision_boundary", "C185"), "same system"),
        (("references", 2, "identifier"), "fake"),
    ]
    for index, (path, value) in enumerate(semantic):
        mutant = copy.deepcopy(base)
        set_path(mutant, path, value)
        mutant["payload_sha256"] = payload_hash(mutant)
        mutations.append((f"json-semantic-{index}", json.dumps(mutant, sort_keys=True, indent=2) + "\n", yaml_text))

    scope_escalation = copy.deepcopy(base)
    scope_escalation["nonclaims"][0] = "We construct target Euler factors and certify their root numbers."
    scope_escalation["payload_sha256"] = payload_hash(scope_escalation)
    mutations.append(("json-nonclaim-scope-escalation", json.dumps(scope_escalation, sort_keys=True, indent=2) + "\n", yaml_text))

    boundary_forgery = copy.deepcopy(base)
    boundary_forgery["collision_boundary"]["subset_sum_warning"] = "FORGED"
    boundary_forgery["payload_sha256"] = payload_hash(boundary_forgery)
    mutations.append(("json-boundary-text-forgery", json.dumps(boundary_forgery, sort_keys=True, indent=2) + "\n", yaml_text))

    # Three independently reported Python bool/int equality escapes are kept
    # as named regressions.  Each attack repairs the payload hash.
    explicit_bool_int = [
        ("simple-k-one-to-true", ("enumeration", "simple_cases", 0, "k")),
        ("plucker-subset-index-one-to-true", ("enumeration", "simple_cases", 0, "plucker_support", 0, "subset", 0)),
        ("simple-eigenvalue-one-to-true", ("enumeration", "simple_cases", 1, "eigenvalues_strictly_increasing", 1)),
    ]
    for name, path in explicit_bool_int:
        mutant = copy.deepcopy(base)
        assert type(get_path(mutant, path)) is int
        set_path(mutant, path, True)
        mutant["payload_sha256"] = payload_hash(mutant)
        mutations.append((f"json-bool-int-{name}", json.dumps(mutant, sort_keys=True, indent=2) + "\n", yaml_text))

    # Systematically cover every structural path class containing a numeric
    # 0/1 leaf.  List indices are wildcarded, so large matrices do not create
    # redundant attacks while every field shape is represented.
    numeric_path_representatives = {}

    def collect_numeric_paths(value, path=()):
        if type(value) is dict:
            for key, item in value.items():
                collect_numeric_paths(item, path + (key,))
        elif type(value) is list:
            for index, item in enumerate(value):
                collect_numeric_paths(item, path + (index,))
        elif type(value) is int and value in (0, 1):
            pattern = tuple("*" if type(item) is int else item for item in path)
            numeric_path_representatives.setdefault(pattern, path)

    collect_numeric_paths(base)
    assert len(numeric_path_representatives) == 36
    for index, (pattern, path) in enumerate(sorted(numeric_path_representatives.items(), key=lambda item: repr(item[0]))):
        mutant = copy.deepcopy(base)
        cursor = get_path(mutant, path)
        assert type(cursor) is int and cursor in (0, 1)
        set_path(mutant, path, bool(cursor))
        mutant["payload_sha256"] = payload_hash(mutant)
        mutations.append((f"json-bool-int-class-{index}-{'/'.join(map(str, pattern))}", json.dumps(mutant, sort_keys=True, indent=2) + "\n", yaml_text))

    stale = copy.deepcopy(base)
    stale["candidate_id"] = "HCS-C999"
    mutations.append(("json-stale-hash", json.dumps(stale, sort_keys=True, indent=2) + "\n", yaml_text))
    missing = copy.deepcopy(base)
    missing.pop("proof_contract")
    missing["payload_sha256"] = payload_hash(missing)
    mutations.append(("json-missing", json.dumps(missing, sort_keys=True, indent=2) + "\n", yaml_text))
    unknown = copy.deepcopy(base)
    unknown["unknown"] = 1
    unknown["payload_sha256"] = payload_hash(unknown)
    mutations.append(("json-unknown", json.dumps(unknown, sort_keys=True, indent=2) + "\n", yaml_text))
    nested_unknown = copy.deepcopy(base)
    nested_unknown["route_a"]["unknown_nested"] = False
    nested_unknown["payload_sha256"] = payload_hash(nested_unknown)
    mutations.append(("json-nested-unknown", json.dumps(nested_unknown, sort_keys=True, indent=2) + "\n", yaml_text))
    mutations.append(("json-duplicate", raw.replace('  "candidate_id": "HCS-C298",', '  "candidate_id": "HCS-C298",\n  "candidate_id": "HCS-C298",', 1), yaml_text))
    mutations.append(("json-nonfinite", raw.replace('"audited_cell_count": 189', '"audited_cell_count": NaN', 1), yaml_text))

    yaml_replacements = [
        ("candidate_id: HCS-C298", "candidate_id: HCS-C999"),
        ("obstruction_id: HEN-O282", "obstruction_id: HEN-O999"),
        (f"source_commit: {base['source_commit']}", "source_commit: " + "0" * 40),
        ("fixed_epoch: 1788307200", "fixed_epoch: '1788307200'"),
        ("scope_literal: NO_BAD_EULER_OR_ROOT_NUMBER", "scope_literal: BAD"),
        ("evaluator_authority_sha256: 6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c", "evaluator_authority_sha256: " + "0" * 64),
        ("verdict: A0_FAIL", "verdict: A0_PASS"),
        ("verdict: A4_FORMAL_HINT", "verdict: A4_NATURAL_QUANTIZATION"),
        ("overall_verdict: ROUTE_A_REJECTED", "overall_verdict: ROUTE_A_STRONG_CANDIDATE"),
        ("route_b_invocation_allowed: false", "route_b_invocation_allowed: true"),
        ("route_b_invocation_allowed: false", "route_b_invocation_allowed: 0"),
        ("  claims_target_euler_factors: false", "  claims_target_euler_factors: 0"),
        ("theorem_status: PROVABLE_AS_STATED", "theorem_status: HEURISTIC"),
        ("family: Grassmann gradient and continuous subspace power flow", "family: altered family"),
        ("finite_evidence_role: regression evidence only; global solution, limits, and Morse--Bott structure are analytic", "finite_evidence_role: finite cases prove the global theorem"),
        ("route_b_lock_reason: no bad-prime, Euler-factor, or root-number datum exists under the frozen scope", "route_b_lock_reason: altered lock"),
        ("  evidence_status: strict Lyapunov obstruction", "  evidence_status: exact negative classification"),
        ("  strongest_evidence: every orbit has an exact invariant-subspace limit", "  strongest_evidence: altered axis evidence"),
        ("  strongest_failure: time is not an arithmetic clock or logarithmic prime norm", "  strongest_failure: altered axis failure"),
        ("  artifacts: [THEOREM_PACKAGE.md]", "  artifacts: [paper/main.pdf]"),
        ("  - results/c298_grassmann_evidence.json", "  - results/altered.json"),
        ("  - hdl:2078.5/90452", "  - hdl:fake"),
    ]
    for index, (old, new) in enumerate(yaml_replacements):
        assert old in yaml_text, old
        mutations.append((f"yaml-semantic-{index}", raw, yaml_text.replace(old, new, 1)))
    mutations.append(("yaml-duplicate", raw, yaml_text + "candidate_id: HCS-C298\n"))
    mutations.append(("yaml-unknown", raw, yaml_text + "unknown_top_key: 1\n"))
    mutations.append(("yaml-missing", raw, yaml_text.replace("obstruction_id: HEN-O282\n", "", 1)))
    mutations.append(("yaml-nested-missing", raw, yaml_text.replace("  strongest_evidence: exterior-power coordinates give finite exponential sums\n", "", 1)))
    mutations.append(("yaml-nested-unknown", raw, yaml_text.replace("a3:\n", "a3:\n  unknown_nested: forbidden\n", 1)))
    mutations.append(("yaml-axis-type", raw, yaml_text.replace("  evidence_status: analogy only", "  evidence_status: 0", 1)))
    mutations.append(("yaml-anchor", raw, yaml_text + "anchored: &forbidden 1\n"))
    mutations.append(("yaml-alias", raw, yaml_text + "aliased: *forbidden\n"))
    mutations.append(("yaml-merge", raw, yaml_text.replace("a0:\n", "a0:\n  <<: {extra: 1}\n", 1)))
    mutations.append(("yaml-nonstring-key", raw, yaml_text + "1: forbidden\n"))

    passed = 0
    for name, evidence_text, candidate_yaml in mutations:
        run = checker_run(evidence_text, candidate_yaml)
        if run.returncode == 0:
            raise AssertionError(f"mutation survived: {name}")
        passed += 1
    print(f"C298 hostile mutation suite: PASS {passed}/{len(mutations)} (baseline control accepted)")


if __name__ == "__main__":
    main()
