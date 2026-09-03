#!/usr/bin/env python3
"""Hostile repaired-hash and parser mutations for HCS-C337."""
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
EVIDENCE = ROOT / "results/c337_kicked_rotor_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C337/2026-09-03.yaml"
CHECKER = ROOT / "code/c337_kicked_rotor_checker.py"


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
    if type(value) is str:
        return value+"__MUTATED"
    raise TypeError(type(value))


def repaired_json(data):
    data["payload_sha256"] = payload_hash(data)
    return json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False)+"\n"


def repaired_yaml_carrier(data, raw_yaml, semantic):
    mutated = copy.deepcopy(data)
    mutated["evaluation"]["raw_sha256"] = hashlib.sha256(raw_yaml.encode()).hexdigest()
    mutated["evaluation"]["semantic_sha256"] = hashlib.sha256(json.dumps(
        semantic, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    return repaired_json(mutated)


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C337 mutation lane refuses optimized Python")
    data = json.loads(EVIDENCE.read_text())
    json_raw = EVIDENCE.read_text()
    yaml_raw = EVALUATION.read_text()
    attacks = []

    semantic_attacks = [
        (("candidate_id",), "HCS-C000"),
        (("obstruction_id",), "HEN-O000"),
        (("source_commit",), "0"*40),
        (("fixed_epoch",), 0),
        (("scope_literal",), "EXPANDED"),
        (("evaluator", "authority"), "route-a-evaluator"),
        (("evaluator", "version"), "9.9.9"),
        (("evaluator", "sha256"), "0"*64),
        (("evaluation", "raw_sha256"), "0"*64),
        (("evaluation", "semantic_sha256"), "0"*64),
        (("model", "floquet_order"), "reversed"),
        (("model", "resonance_sheet"), "all rational tau"),
        (("theorem_contract", "even_kernel"), "wrong phase"),
        (("theorem_contract", "characteristic"), "wrong nome"),
        (("theorem_contract", "odd_involution"), "U^3=I"),
        (("references", 0, "identifier"), "10.0000/fake"),
        (("collision_boundary", "C224"), "same owner"),
        (("nonclaims", 1), "general rational resonance proved"),
        (("route_a", "tuple", 4), "A4_ROUTE_B_READY"),
        (("route_a", "overall"), "ROUTE_A_ACCEPTED"),
        (("route_a", "route_b_invocation_allowed"), True),
        (("scope_flags", "claims_target_zero_match"), True),
        (("parameter_grid", "formal_degree"), "0..13"),
        (("parity_rows", 0, "free_phase"), -1),
        (("parity_rows", 33, "operator_face"), "half_turn"),
        (("formal_kernel_coefficients", 0, "direct_exponential", 0), "7"),
        (("formal_kernel_coefficients", 210, "bessel_formula", 1), "1"),
        (("moment_rows", 0, "effective_bessel_argument"), "1"),
        (("moment_rows", 100, "central_moments_0_to_6", 2), "9"),
        (("moment_rows", 500, "raw_moments_0_to_6", 4), "9"),
        (("moment_rows", 700, "kinetic_energy"), "9"),
        (("operator_rows", 0, "power_reduction"), "K_kappa"),
        (("operator_rows", 1, "amplitude_phase"), "missing R"),
        (("numeric_rows", 0, "evidence_status"), "PROVED"),
        (("numeric_rows", 2, "characteristic_error"), "0"),
        (("boundary_rows", "operator_order"), "either order"),
        (("enumeration", "moment_rows"), 0),
        (("enumeration", "audited_leaf_count"), 0),
    ]
    for path, value in semantic_attacks:
        mutated = copy.deepcopy(data)
        set_path(mutated, path, value)
        attacks.append(("evidence-"+".".join(map(str, path)), repaired_json(mutated), yaml_raw))

    extra = copy.deepcopy(data)
    extra["unowned"] = "survive"
    attacks.append(("extra-top-key", repaired_json(extra), yaml_raw))
    extra_row = copy.deepcopy(data)
    extra_row["moment_rows"][0]["unowned"] = "survive"
    attacks.append(("extra-row-key", repaired_json(extra_row), yaml_raw))
    missing = copy.deepcopy(data)
    del missing["theorem_contract"]
    attacks.append(("missing-top-key", repaired_json(missing), yaml_raw))
    attacks.extend([
        ("duplicate-json", json_raw.replace("{\n", '{\n  "schema": "duplicate",\n', 1), yaml_raw),
        ("nan-json", json_raw.replace('"fixed_epoch": 1788393600', '"fixed_epoch": NaN', 1), yaml_raw),
        ("json-root-array", "[]\n", yaml_raw),
        ("stale-payload", json_raw.replace('"candidate_id": "HCS-C337"', '"candidate_id": "HCS-C000"', 1), yaml_raw),
    ])

    yaml_attacks = [
        ("yaml-duplicate", yaml_raw+"candidate_id: HCS-C337\n"),
        ("yaml-anchor", yaml_raw.replace("candidate_id: HCS-C337", "candidate_id: &owner HCS-C337", 1)),
        ("yaml-alias", "base: &b HCS-C337\nalias: *b\n"+yaml_raw),
        ("yaml-merge", "base: &b {x: 1}\nmerged:\n  <<: *b\n"+yaml_raw),
        ("yaml-nonstring-key", "1: invalid\n"+yaml_raw),
        ("yaml-root-array", "- invalid\n"),
        ("yaml-authority-rewrite", yaml_raw.replace(
            "evaluator_authority: flow_systems/skills/route-a-evaluator.md",
            "evaluator_authority: route-a-evaluator", 1)),
        ("yaml-authority-delete", yaml_raw.replace(
            "evaluator_authority: flow_systems/skills/route-a-evaluator.md\n", "", 1)),
        ("yaml-status-proved", yaml_raw.replace("  evidence_status: PROVED", "  evidence_status: STOP_SCOPED", 1)),
        ("yaml-status-scoped", yaml_raw.replace("  evidence_status: STOP_SCOPED", "  evidence_status: PROVED", 1)),
        ("yaml-status-delete", yaml_raw.replace("  evidence_status: PROVED\n", "", 1)),
        ("yaml-route-b", yaml_raw.replace("route_b_invocation_allowed: false", "route_b_invocation_allowed: true", 1)),
        ("yaml-a4", yaml_raw.replace("  verdict: A4_NATURAL_QUANTIZATION", "  verdict: A4_ROUTE_B_READY", 1)),
        ("yaml-flag", yaml_raw.replace("  claims_target_zero_match: false", "  claims_target_zero_match: true", 1)),
        ("yaml-date-type", yaml_raw.replace("evaluation_date: '2026-09-03'", "evaluation_date: 2026-09-03", 1)),
        ("yaml-epoch-type", yaml_raw.replace("fixed_epoch: 1788393600", 'fixed_epoch: "1788393600"', 1)),
        ("yaml-unknown", yaml_raw+"unknown_field: forbidden\n"),
        ("yaml-whitespace", yaml_raw+"\n"),
    ]
    for name, changed in yaml_attacks:
        try:
            semantic = yaml.safe_load(changed)
            carried = repaired_yaml_carrier(data, changed, semantic)
        except Exception:
            carried = json_raw
        attacks.append((name, carried, changed))

    evaluation_value = yaml.safe_load(yaml_raw)
    for path, value in leaf_paths(evaluation_value):
        changed = copy.deepcopy(evaluation_value)
        set_path(changed, path, changed_leaf(value))
        rendered = yaml.safe_dump(changed, sort_keys=False, allow_unicode=True)
        carried = repaired_yaml_carrier(data, rendered, changed)
        attacks.append(("yaml-repaired-leaf-"+".".join(map(str, path)), carried, rendered))

    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c337-mutation-") as directory:
        work = Path(directory)
        for index, (name, raw_json, raw_yaml) in enumerate(attacks):
            evidence = work/f"attack-{index}.json"
            evaluation = work/f"attack-{index}.yaml"
            evidence.write_text(raw_json)
            evaluation.write_text(raw_yaml)
            process = subprocess.run(
                [sys.executable, "-B", str(CHECKER), "--evidence", str(evidence), "--evaluation", str(evaluation)],
                env=environment, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
            )
            if process.returncode == 0:
                raise AssertionError(f"hostile attack survived: {name}-{index}")
            rejected += 1
    print(f"C337 hostile mutation suite: PASS {rejected}/{len(attacks)}")


if __name__ == "__main__":
    main()
