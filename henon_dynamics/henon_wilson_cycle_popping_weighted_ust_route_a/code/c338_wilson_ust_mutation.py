#!/usr/bin/env python3
"""Hostile repaired-hash and strict-parser attacks for HCS-C338."""
from __future__ import annotations

import copy
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c338_wilson_ust_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C338/2026-09-03.yaml"
CHECKER = ROOT / "code/c338_wilson_ust_checker.py"


def payload_hash(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(
        body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def set_path(data, path, value):
    cursor = data
    for key in path[:-1]:
        cursor = cursor[key]
    cursor[path[-1]] = value


def leaf_paths(value, prefix=()):
    if type(value) is dict:
        for key, child in value.items():
            yield from leaf_paths(child, prefix + (key,))
    elif type(value) is list:
        for index, child in enumerate(value):
            yield from leaf_paths(child, prefix + (index,))
    else:
        yield prefix, value


def changed_leaf(value):
    if type(value) is bool:
        return not value
    if type(value) is int:
        return value + 1
    if type(value) is str:
        return value + "__MUTATED"
    raise TypeError(type(value))


def repaired_yaml_evidence(data, raw_yaml, semantic):
    mutated = copy.deepcopy(data)
    mutated["route_a_yaml"]["raw_sha256"] = hashlib.sha256(raw_yaml.encode()).hexdigest()
    mutated["route_a_yaml"]["semantic_sha256"] = hashlib.sha256(json.dumps(
        semantic, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    mutated["payload_sha256"] = payload_hash(mutated)
    return json.dumps(mutated, sort_keys=True, indent=2, ensure_ascii=False) + "\n"


def main():
    if sys.flags.optimize:
        raise RuntimeError("C338 mutation lane refuses optimized Python")
    data = json.loads(EVIDENCE.read_text())
    json_raw = EVIDENCE.read_text()
    yaml_raw = EVALUATION.read_text()
    attacks = []
    semantic_attacks = [
        (("candidate_id",), "HCS-C000"),
        (("obstruction_id",), "HEN-O000"),
        (("evaluation_date",), "2099-01-01"),
        (("source_commit",), "0" * 40),
        (("scope_literal",), "EXPANDED"),
        (("evaluator", "authority"), "route-a-evaluator"),
        (("evaluator", "version"), "9.9.9"),
        (("evaluator", "sha256"), "0" * 64),
        (("route_a_yaml", "relative_path"), "evaluation.yaml"),
        (("route_a_yaml", "raw_sha256"), "0" * 64),
        (("route_a_yaml", "semantic_sha256"), "0" * 64),
        (("model", "graph"), "directed graph"),
        (("model", "conductances"), "negative weights allowed"),
        (("model", "stack_law"), "dependent stacks"),
        (("model", "edge_orientation"), "orientation forgotten"),
        (("model", "transfer_current"), "unweighted adjacency kernel"),
        (("theorem_contract", "abelian"), "one schedule only"),
        (("theorem_contract", "termination"), "deterministic termination"),
        (("theorem_contract", "lerw"), "ordinary walk"),
        (("theorem_contract", "tree_law"), "uniform after forgetting weights"),
        (("theorem_contract", "matrix_tree"), "wrong cofactor"),
        (("theorem_contract", "transfer_current"), "singleton edges only"),
        (("theorem_contract", "boundaries"), "simple graphs only"),
        (("finite_grid", "weighted_cases"), 23),
        (("collision_boundary", "C181"), "same owner"),
        (("nonclaims", 0), "the tree polynomial is a target Euler factor"),
        (("references", 1, "identifier"), "DOI:10.1214/aop/1176989016"),
        (("route_a", "tuple", 4), "A4_ROUTE_B_READY"),
        (("route_a", "overall"), "ROUTE_A_ACCEPTED"),
        (("route_a", "route_b_invocation_allowed"), True),
        (("scope_flags", "claims_target_euler_factors"), True),
        (("graph_rows", 0, "tree_partition"), 2),
        (("graph_rows", 771, "transfer_current_kernel", 0, 0), "0"),
        (("graph_rows", 771, "all_subset_inclusion_numerators", 1), 0),
        (("weighted_case_rows", 0, "tree_partition"), 8),
        (("weighted_case_rows", 0, "oriented_labelled_edges", 1, 3), 7),
        (("stack_audit_rows", 3, "abelian_failures"), 1),
        (("stack_audit_rows", 3, "terminating_tables"), 9119),
        (("enumeration", "connected_simple_graphs"), 771),
        (("enumeration", "audited_leaf_count"), 0),
    ]
    for path, value in semantic_attacks:
        mutated = copy.deepcopy(data)
        set_path(mutated, path, value)
        mutated["payload_sha256"] = payload_hash(mutated)
        attacks.append(("semantic-" + ".".join(map(str, path)),
                        json.dumps(mutated, sort_keys=True, indent=2, ensure_ascii=False) + "\n", yaml_raw))

    for section, row in (("graph_rows", 0), ("weighted_case_rows", 0), ("stack_audit_rows", 0)):
        extra = copy.deepcopy(data)
        extra[section][row]["unowned"] = "survive"
        extra["payload_sha256"] = payload_hash(extra)
        attacks.append((f"nested-extra-{section}", json.dumps(extra, sort_keys=True, indent=2) + "\n", yaml_raw))
        omitted = copy.deepcopy(data)
        omitted[section].pop(row)
        omitted["payload_sha256"] = payload_hash(omitted)
        attacks.append((f"row-omit-{section}", json.dumps(omitted, sort_keys=True, indent=2) + "\n", yaml_raw))
        duplicate = copy.deepcopy(data)
        duplicate[section].insert(row, copy.deepcopy(duplicate[section][row]))
        duplicate["payload_sha256"] = payload_hash(duplicate)
        attacks.append((f"row-duplicate-{section}", json.dumps(duplicate, sort_keys=True, indent=2) + "\n", yaml_raw))

    missing = copy.deepcopy(data)
    del missing["theorem_contract"]
    missing["payload_sha256"] = payload_hash(missing)
    attacks.append(("missing-top-key", json.dumps(missing, sort_keys=True, indent=2) + "\n", yaml_raw))
    attacks.extend([
        ("duplicate-json", json_raw.replace("{\n", '{\n  "schema": "duplicate",\n', 1), yaml_raw),
        ("nan-json", json_raw.replace('"fixed_epoch": 1788393600', '"fixed_epoch": NaN', 1), yaml_raw),
        ("json-root-array", "[]\n", yaml_raw),
    ])

    yaml_attacks = [
        ("yaml-duplicate", yaml_raw + "candidate_id: HCS-C338\n"),
        ("yaml-anchor", yaml_raw.replace("candidate_id: HCS-C338", "candidate_id: &owner HCS-C338", 1)),
        ("yaml-alias", "owner: &o HCS-C338\ncandidate_id: *o\n" + yaml_raw),
        ("yaml-merge", "base: &b {x: 1}\nmerged:\n  <<: *b\n" + yaml_raw),
        ("yaml-nonstring-key", "1: invalid\n" + yaml_raw),
        ("yaml-implicit-timestamp", yaml_raw.replace("evaluation_date: '2026-09-03'", "evaluation_date: 2026-09-03", 1)),
        ("yaml-unknown-field", yaml_raw + "unknown_field: forbidden\n"),
        ("yaml-type-mutation", yaml_raw.replace("fixed_epoch: 1788393600", 'fixed_epoch: "1788393600"', 1)),
        ("yaml-authority", yaml_raw.replace("evaluator_authority: flow_systems/skills/route-a-evaluator.md", "evaluator_authority: route-a-evaluator", 1)),
        ("yaml-source", yaml_raw.replace(SOURCE_LINE := "source_commit: db2c816b7b6bd450f51f79b91842cb882b0bd773", "source_commit: 0000000000000000000000000000000000000000", 1)),
        ("yaml-status-proved", yaml_raw.replace("  evidence_status: PROVED", "  evidence_status: STOP_SCOPED", 1)),
        ("yaml-status-scoped", yaml_raw.replace("  evidence_status: STOP_SCOPED", "  evidence_status: PROVED", 1)),
        ("yaml-status-delete", yaml_raw.replace("  evidence_status: PROVED\n", "", 1)),
        ("yaml-route-b", yaml_raw.replace("route_b_invocation_allowed: false", "route_b_invocation_allowed: true", 1)),
        ("yaml-a4", yaml_raw.replace("  verdict: A4_FORMAL_HINT", "  verdict: A4_ROUTE_B_READY", 1)),
        ("yaml-root-array", "- invalid\n"),
        ("yaml-equivalent-whitespace", yaml_raw + "\n"),
    ]
    attacks.extend((name, json_raw, changed) for name, changed in yaml_attacks)

    semantic = yaml.safe_load(yaml_raw)
    for path, value in leaf_paths(semantic):
        changed = copy.deepcopy(semantic)
        set_path(changed, path, changed_leaf(value))
        rendered = yaml.safe_dump(changed, sort_keys=False, allow_unicode=True)
        attacks.append(("yaml-repaired-leaf-" + ".".join(map(str, path)),
                        repaired_yaml_evidence(data, rendered, changed), rendered))

    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c338-mutation-") as directory:
        directory = Path(directory)
        for index, (name, evidence_raw, evaluation_raw) in enumerate(attacks):
            evidence = directory / f"attack-{index}.json"
            evaluation = directory / f"attack-{index}.yaml"
            evidence.write_text(evidence_raw)
            evaluation.write_text(evaluation_raw)
            process = subprocess.run(
                [sys.executable, "-B", str(CHECKER), "--evidence", str(evidence),
                 "--evaluation", str(evaluation)],
                env=environment, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
            )
            if process.returncode == 0:
                raise AssertionError(f"hostile attack survived: {name}-{index}")
            rejected += 1
    print(f"C338 hostile mutation suite: PASS {rejected}/{len(attacks)}")


if __name__ == "__main__":
    main()
