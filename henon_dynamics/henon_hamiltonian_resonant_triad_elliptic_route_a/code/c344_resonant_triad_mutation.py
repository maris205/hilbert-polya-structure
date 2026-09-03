#!/usr/bin/env python3
"""Repaired-hash parser, theorem, phase, and evaluator attacks for HCS-C344."""
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
EVIDENCE = ROOT / "results/c344_resonant_triad_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C344/2026-09-03.yaml"
CHECKER = ROOT / "code/c344_resonant_triad_checker.py"


def leaves(value) -> int:
    if type(value) is dict:
        return sum(leaves(child) for child in value.values())
    if type(value) is list:
        return sum(leaves(child) for child in value)
    return 1


def payload_hash(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(
        body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def repair(data, recount=True):
    body = dict(data)
    body.pop("payload_sha256", None)
    if recount and "enumeration" in body and type(body["enumeration"]) is dict and "audited_leaf_count" in body["enumeration"]:
        body["enumeration"]["audited_leaf_count"] = leaves(body)
    body["payload_sha256"] = payload_hash(body)
    return json.dumps(body, sort_keys=True, indent=2, ensure_ascii=False)+"\n"


def set_path(data, path, value):
    cursor = data
    for key in path[:-1]:
        cursor = cursor[key]
    cursor[path[-1]] = value


def repaired_yaml_carrier(data, raw_yaml, semantic):
    mutated = copy.deepcopy(data)
    mutated["evaluation"]["raw_sha256"] = hashlib.sha256(raw_yaml.encode()).hexdigest()
    mutated["evaluation"]["semantic_sha256"] = hashlib.sha256(json.dumps(
        semantic, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    return repair(mutated)


def leaf_paths(value, prefix=()):
    if type(value) is dict:
        for key, child in value.items():
            yield from leaf_paths(child, prefix+(key,))
    elif type(value) is list:
        for index, child in enumerate(value):
            yield from leaf_paths(child, prefix+(index,))
    else:
        yield prefix, value


def changed_leaf(value):
    if type(value) is bool:
        return not value
    if type(value) is int:
        return value+1
    if value is None:
        return "MUTATED"
    if type(value) is str:
        return value+"__MUTATED"
    raise TypeError(type(value))


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C344 mutation lane refuses optimized Python")
    data = json.loads(EVIDENCE.read_text())
    json_raw = EVIDENCE.read_text()
    yaml_raw = EVALUATION.read_text()
    attacks = []
    semantic_attacks = [
        (("candidate_id",), "HCS-C000"), (("obstruction_id",), "HEN-O000"),
        (("source_commit",), "0"*40), (("fixed_epoch",), 0), (("scope_literal",), "EXPANDED"),
        (("evaluator", "authority"), "route-a-evaluator"), (("evaluator", "version"), "9.9.9"),
        (("evaluator", "sha256"), "0"*64), (("evaluation", "raw_sha256"), "0"*64),
        (("evaluation", "semantic_sha256"), "0"*64), (("model", "equations"), "wrong sign"),
        (("model", "poisson_bracket"), "wrong bracket"), (("model", "reduction"), "wrong cubic"),
        (("theorem_contract", "regular_solution"), "elementary trigonometric orbit"),
        (("theorem_contract", "phase_return"), "one phase is sufficient"),
        (("theorem_contract", "zero_h_boundary"), "intensity and full periods coincide"),
        (("theorem_contract", "double_root_boundary"), "every relative equilibrium is periodic"),
        (("references", 0, "identifier"), "10.0000/fake"),
        (("collision_boundary", "C211"), "same owner"), (("nonclaims", 1), "intensity implies full return"),
        (("route_a", "tuple", 0), "A0_STRUCTURAL_ARITHMETIC_RELATION"),
        (("route_a", "tuple", 4), "A4_NATURAL_QUANTIZATION"),
        (("route_a", "overall"), "ROUTE_A_ACCEPTED"),
        (("route_a", "route_b_invocation_allowed"), True),
        (("scope_flags", "claims_target_zero_match"), True),
        (("parameter_grid", "root_bracket_iterations"), 8),
        (("regular_rows", 0, "h_sign"), 1), (("regular_rows", 0, "h_squared"), "1/2"),
        (("regular_rows", 0, "root_sum"), "6/2"),
        (("regular_rows", 0, "roots_decimal", 0), "nan"),
        (("regular_rows", 0, "root_intervals", 0, 0), "0"),
        (("regular_rows", 0, "intensity_period"), "1.00000000000000000000000000000000000000000000000000000000000"),
        (("regular_rows", 0, "phase_increment_1"), data["regular_rows"][0]["phase_increment_2"]),
        (("regular_rows", 0, "closure_rule"), "one phase suffices"),
        (("zero_hamiltonian_rows", 0, "full_state_period"), data["zero_hamiltonian_rows"][0]["intensity_period"]),
        (("zero_hamiltonian_rows", 8, "face"), "periodic"),
        (("relative_equilibrium_rows", 0, "phase_lock"), "omega3=omega1-omega2"),
        (("relative_equilibrium_rows", 20, "closure_classification"), "generic periodic"),
        (("boundary_atlas", "h_zero_equal"), "finite period"),
        (("boundary_atlas", "formal_quantization"), "complete quantum spectrum"),
        (("enumeration", "regular_rows"), 0), (("enumeration", "audited_leaf_count"), 0),
    ]
    for path, value in semantic_attacks:
        mutated = copy.deepcopy(data)
        set_path(mutated, path, value)
        attacks.append(("evidence-"+".".join(map(str, path)),
                        repair(mutated, recount=path != ("enumeration", "audited_leaf_count")), yaml_raw))

    extra = copy.deepcopy(data)
    extra["unowned"] = "survive"
    attacks.append(("extra-top-key", repair(extra), yaml_raw))
    extra_row = copy.deepcopy(data)
    extra_row["regular_rows"][0]["unowned"] = "survive"
    attacks.append(("extra-nested-key", repair(extra_row), yaml_raw))
    duplicated = copy.deepcopy(data)
    duplicated["regular_rows"].insert(0, copy.deepcopy(duplicated["regular_rows"][0]))
    duplicated["enumeration"]["regular_rows"] += 1
    attacks.append(("duplicate-regular-coordinate", repair(duplicated), yaml_raw))
    omitted = copy.deepcopy(data)
    omitted["relative_equilibrium_rows"].pop()
    omitted["enumeration"]["relative_equilibrium_rows"] -= 1
    attacks.append(("omit-relative-coordinate", repair(omitted), yaml_raw))
    reordered = copy.deepcopy(data)
    reordered["zero_hamiltonian_rows"][0], reordered["zero_hamiltonian_rows"][1] = (
        reordered["zero_hamiltonian_rows"][1], reordered["zero_hamiltonian_rows"][0])
    attacks.append(("reorder-zero-H-coordinates", repair(reordered), yaml_raw))
    missing = copy.deepcopy(data)
    del missing["theorem_contract"]
    attacks.append(("missing-top-key", repair(missing), yaml_raw))
    attacks.extend([
        ("duplicate-json", json_raw.replace("{\n", '{\n  "schema": "duplicate",\n', 1), yaml_raw),
        ("nan-json", json_raw.replace('"fixed_epoch": 1788393600', '"fixed_epoch": NaN', 1), yaml_raw),
        ("json-root-array", "[]\n", yaml_raw),
        ("stale-payload-hash-control", json_raw.replace('"candidate_id": "HCS-C344"', '"candidate_id": "HCS-C000"', 1), yaml_raw),
    ])

    yaml_attacks = [
        ("yaml-duplicate", yaml_raw+"candidate_id: HCS-C344\n"),
        ("yaml-anchor", yaml_raw.replace("candidate_id: HCS-C344", "candidate_id: &owner HCS-C344", 1)),
        ("yaml-alias", "base: &b HCS-C344\nalias: *b\n"+yaml_raw),
        ("yaml-merge", "base: &b {x: 1}\nmerged:\n  <<: *b\n"+yaml_raw),
        ("yaml-nonstring-key", "1: invalid\n"+yaml_raw), ("yaml-root-array", "- invalid\n"),
        ("yaml-authority-rewrite", yaml_raw.replace(
            "evaluator_authority: flow_systems/skills/route-a-evaluator.md",
            "evaluator_authority: route-a-evaluator", 1)),
        ("yaml-authority-delete", yaml_raw.replace(
            "evaluator_authority: flow_systems/skills/route-a-evaluator.md\n", "", 1)),
        ("yaml-a1-verdict", yaml_raw.replace("  verdict: A1_WEAK", "  verdict: A1_PASS_ANALYTIC", 1)),
        ("yaml-status-proved", yaml_raw.replace("  evidence_status: PROVED", "  evidence_status: STOP_SCOPED", 1)),
        ("yaml-status-scoped", yaml_raw.replace("  evidence_status: STOP_SCOPED", "  evidence_status: PROVED", 1)),
        ("yaml-status-delete", yaml_raw.replace("  evidence_status: PROVED\n", "", 1)),
        ("yaml-route-b", yaml_raw.replace("route_b_invocation_allowed: false", "route_b_invocation_allowed: true", 1)),
        ("yaml-a4", yaml_raw.replace("  verdict: A4_FORMAL_HINT", "  verdict: A4_NATURAL_QUANTIZATION", 1)),
        ("yaml-flag", yaml_raw.replace("  claims_target_zero_match: false", "  claims_target_zero_match: true", 1)),
        ("yaml-date-type", yaml_raw.replace("evaluation_date: '2026-09-03'", "evaluation_date: 2026-09-03", 1)),
        ("yaml-epoch-type", yaml_raw.replace("fixed_epoch: 1788393600", 'fixed_epoch: "1788393600"', 1)),
        ("yaml-unknown", yaml_raw+"unknown_field: forbidden\n"), ("yaml-whitespace", yaml_raw+"\n"),
    ]
    for name, changed in yaml_attacks:
        try:
            semantic = yaml.safe_load(changed)
            carrier = repaired_yaml_carrier(data, changed, semantic)
        except Exception:
            carrier = json_raw
        attacks.append((name, carrier, changed))

    evaluation_value = yaml.safe_load(yaml_raw)
    for path, value in leaf_paths(evaluation_value):
        changed = copy.deepcopy(evaluation_value)
        set_path(changed, path, changed_leaf(value))
        rendered = yaml.safe_dump(changed, sort_keys=False, allow_unicode=True)
        carrier = repaired_yaml_carrier(data, rendered, changed)
        attacks.append(("yaml-repaired-leaf-"+".".join(map(str, path)), carrier, rendered))

    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c344-mutation-") as directory:
        work = Path(directory)
        for index, (name, raw_json, raw_yaml) in enumerate(attacks):
            evidence = work/f"attack-{index}.json"
            evaluation = work/f"attack-{index}.yaml"
            evidence.write_text(raw_json)
            evaluation.write_text(raw_yaml)
            process = subprocess.run(
                [sys.executable, "-B", str(CHECKER), "--evidence", str(evidence),
                 "--evaluation", str(evaluation)], env=environment,
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
            )
            if process.returncode == 0:
                raise AssertionError(f"hostile attack survived: {name}-{index}")
            rejected += 1
    print(f"C344 hostile mutation suite: PASS {rejected}/{len(attacks)}")


if __name__ == "__main__":
    main()
