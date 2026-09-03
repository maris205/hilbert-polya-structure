#!/usr/bin/env python3
"""Repaired-hash hostile evidence and evaluator attacks for HCS-C349."""
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
EVIDENCE = ROOT / "results/c349_neumann_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C349/2026-09-03.yaml"
CHECKER = ROOT / "code/c349_neumann_checker.py"


def leaves(value):
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
    body = copy.deepcopy(data)
    body.pop("payload_sha256", None)
    if recount and type(body.get("enumeration")) is dict:
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
        raise RuntimeError("C349 mutation lane refuses optimized Python")
    data = json.loads(EVIDENCE.read_text())
    json_raw = EVIDENCE.read_text()
    yaml_raw = EVALUATION.read_text()
    attacks = []
    semantic_attacks = [
        (("candidate_id",), "HCS-C000"), (("obstruction_id",), "HEN-O000"),
        (("evaluation_date",), "2026-09-04"), (("source_commit",), "0"*40),
        (("fixed_epoch",), 0), (("scope_literal",), "EXPANDED"),
        (("evaluator", "authority"), "route-a-evaluator"),
        (("evaluator", "version"), "9.9.9"), (("evaluator", "sha256"), "0"*64),
        (("evaluation", "path"), "wrong.yaml"), (("evaluation", "raw_sha256"), "0"*64),
        (("evaluation", "semantic_sha256"), "0"*64),
        (("model", "equations"), "wrong sign"), (("model", "dirac_bracket"), "canonical bracket"),
        (("model", "uhlenbeck"), "wrong denominator"), (("model", "lax"), "wrong matrix"),
        (("model", "quantization"), "hbar unrestricted on the H2 domain"),
        (("theorem_contract", "global"), "local existence only"),
        (("theorem_contract", "integrals"), "numerically conserved"),
        (("theorem_contract", "resolvent"), "trace generator"),
        (("theorem_contract", "regular_fibers"), "all fibers are tori"),
        (("theorem_contract", "boundaries"), "none"),
        (("theorem_contract", "quantum_boundary"), "full quantum spectrum"),
        (("references", 0, "identifier"), "10.0000/fake"),
        (("collision_boundary", "C186"), "same owner"),
        (("nonclaims", 1), "Complete singular topology is claimed."),
        (("route_a", "tuple", 0), "A0_STRUCTURAL_ARITHMETIC_RELATION"),
        (("route_a", "tuple", 4), "A4_FAIL"), (("route_a", "overall"), "ROUTE_A_ACCEPTED"),
        (("route_a", "route_b_invocation_allowed"), True),
        (("scope_flags", "claims_target_zero_match"), True),
        (("parameter_grid", "lax_probes_per_state"), 1),
        (("parameter_grid", "ordered_triples", 0, 0), "0/1"),
        (("state_rows", 0, "sphere_norm"), "2/2"),
        (("state_rows", 0, "tangent_dot"), "1"),
        (("state_rows", 0, "F", 0), "nan"),
        (("state_rows", 0, "sum_F"), "2"),
        (("state_rows", 0, "weighted_F"), "0"),
        (("state_rows", 0, "dirac_pairs", 0), "1"),
        (("state_rows", 0, "lax_probes", 0, "determinant"), "0"),
        (("state_rows", 0, "lax_probes", 0, "direct_V_dot"), "0"),
        (("equilibrium_rows", 0, "type"), "saddle-saddle"),
        (("coordinate_face_rows", 0, "missing_axis"), 2),
        (("repeated_spectrum_rows", 0, "momentum_derivative"), "1"),
        (("repeated_spectrum_rows", 0, "dirac_bracket"), "1"),
        (("repeated_spectrum_rows", 0, "energy_rhs"), "0"),
        (("repeated_spectrum_rows", 0, "independence_witness", "wedge"), "0"),
        (("isotropic_rows", 1, "least_period"), "2*pi"),
        (("boundary_atlas", "regular_only"), "every fiber is regular"),
        (("boundary_atlas", "quantum"), "target-zero operator"),
        (("enumeration", "state_rows"), 0), (("enumeration", "audited_leaf_count"), 0),
    ]
    for path, value in semantic_attacks:
        mutated = copy.deepcopy(data)
        set_path(mutated, path, value)
        attacks.append(("evidence-"+".".join(map(str, path)),
                        repair(mutated, recount=path != ("enumeration", "audited_leaf_count")),
                        yaml_raw))

    extra = copy.deepcopy(data)
    extra["unowned"] = "survive"
    attacks.append(("extra-top-key", repair(extra), yaml_raw))
    extra_row = copy.deepcopy(data)
    extra_row["state_rows"][0]["unowned"] = "survive"
    attacks.append(("extra-nested-key", repair(extra_row), yaml_raw))
    extra_witness = copy.deepcopy(data)
    extra_witness["repeated_spectrum_rows"][0]["independence_witness"]["unowned"] = "survive"
    attacks.append(("extra-repeated-witness-key", repair(extra_witness), yaml_raw))
    duplicated = copy.deepcopy(data)
    duplicated["state_rows"].insert(0, copy.deepcopy(duplicated["state_rows"][0]))
    duplicated["enumeration"]["state_rows"] += 1
    duplicated["enumeration"]["lax_probe_rows"] += 2
    attacks.append(("duplicate-state-coordinate", repair(duplicated), yaml_raw))
    omitted = copy.deepcopy(data)
    omitted["coordinate_face_rows"].pop()
    omitted["enumeration"]["coordinate_face_rows"] -= 1
    attacks.append(("omit-coordinate-face", repair(omitted), yaml_raw))
    reordered = copy.deepcopy(data)
    reordered["equilibrium_rows"][0], reordered["equilibrium_rows"][1] = (
        reordered["equilibrium_rows"][1], reordered["equilibrium_rows"][0])
    attacks.append(("reorder-equilibria", repair(reordered), yaml_raw))
    missing = copy.deepcopy(data)
    del missing["theorem_contract"]
    attacks.append(("missing-top-key", repair(missing), yaml_raw))
    attacks.extend([
        ("duplicate-json", json_raw.replace("{\n", '{\n  "schema": "duplicate",\n', 1), yaml_raw),
        ("nan-json", json_raw.replace('"fixed_epoch": 1788393600', '"fixed_epoch": NaN', 1), yaml_raw),
        ("json-root-array", "[]\n", yaml_raw),
        ("stale-payload-hash-control", json_raw.replace('"candidate_id": "HCS-C349"',
                                                         '"candidate_id": "HCS-C000"', 1), yaml_raw),
    ])

    yaml_attacks = [
        ("yaml-duplicate", yaml_raw+"candidate_id: HCS-C349\n"),
        ("yaml-anchor", yaml_raw.replace("candidate_id: HCS-C349", "candidate_id: &owner HCS-C349", 1)),
        ("yaml-alias", "base: &b HCS-C349\nalias: *b\n"+yaml_raw),
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
        ("yaml-route-b", yaml_raw.replace("route_b_invocation_allowed: false",
                                          "route_b_invocation_allowed: true", 1)),
        ("yaml-a4", yaml_raw.replace("  verdict: A4_NATURAL_QUANTIZATION", "  verdict: A4_FAIL", 1)),
        ("yaml-flag", yaml_raw.replace("  claims_target_zero_match: false",
                                       "  claims_target_zero_match: true", 1)),
        ("yaml-date-type", yaml_raw.replace("evaluation_date: '2026-09-03'",
                                            "evaluation_date: 2026-09-03", 1)),
        ("yaml-epoch-type", yaml_raw.replace("fixed_epoch: 1788393600",
                                             'fixed_epoch: "1788393600"', 1)),
        ("yaml-unknown", yaml_raw+"unknown_field: forbidden\n"),
        ("yaml-whitespace", yaml_raw+"\n"),
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
    with tempfile.TemporaryDirectory(prefix="c349-mutation-") as directory:
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
    print(f"C349 hostile mutation suite: PASS {rejected}/{len(attacks)}")


if __name__ == "__main__":
    main()
