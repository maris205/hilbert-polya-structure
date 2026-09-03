#!/usr/bin/env python3
"""Repaired-hash and parser attacks for the HCS-C333 package."""
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
EVIDENCE = ROOT / "results/c333_gossip_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C333/2026-09-03.yaml"
CHECKER = ROOT / "code/c333_gossip_checker.py"


def payload_hash(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


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
    raise TypeError(f"unsupported evaluator leaf: {type(value)}")


def repaired_yaml_evidence(data, raw_yaml, semantic_value):
    mutated = copy.deepcopy(data)
    mutated["evaluation"]["raw_sha256"] = hashlib.sha256(raw_yaml.encode()).hexdigest()
    mutated["evaluation"]["semantic_sha256"] = hashlib.sha256(
        json.dumps(semantic_value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()
    mutated["payload_sha256"] = payload_hash(mutated)
    return json.dumps(mutated, sort_keys=True, indent=2, ensure_ascii=False) + "\n"


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C333 mutation lane refuses optimized Python")
    data = json.loads(EVIDENCE.read_text())
    json_raw = EVIDENCE.read_text()
    yaml_raw = EVALUATION.read_text()
    attacks = []
    semantic = [
        (("candidate_id",), "HCS-C000"),
        (("obstruction_id",), "HEN-O000"),
        (("source_commit",), "0" * 40),
        (("scope_literal",), "EXPANDED"),
        (("evaluator", "authority"), "route-a-evaluator"),
        (("evaluator", "version"), "9.9.9"),
        (("evaluator", "sha256"), "0" * 64),
        (("evaluation", "raw_sha256"), "0" * 64),
        (("evaluation", "semantic_sha256"), "0" * 64),
        (("model", "edge_law"), "ordered edge"),
        (("model", "update"), "W=I+eta ddT"),
        (("model", "parameter_domain"), "eta real"),
        (("theorem_contract", "mean"), "mean drifts"),
        (("theorem_contract", "decomposition"), "two blocks only"),
        (("theorem_contract", "spectrum"), "wrong multiplicity"),
        (("theorem_contract", "consensus"), "eta=1 reaches consensus"),
        (("theorem_contract", "tail_domain"), "the normalized tail bound includes zero disagreement"),
        (("references", 0, "identifier"), "10.0000/fake"),
        (("collision_boundary", "C183"), "same owner"),
        (("nonclaims", 1), "moment eigenvalues are target zeros"),
        (("route_a", "tuple", 4), "A4_ROUTE_B_READY"),
        (("route_a", "overall"), "ROUTE_A_ACCEPTED"),
        (("route_a", "route_b_invocation_allowed"), True),
        (("scope_flags", "claims_target_zero_match"), True),
        (("parameter_grid", "N_spectral"), "2..8"),
        (("spectral_rows", 0, "edge_count"), 2),
        (("spectral_rows", 3, "mean_multiplier"), "7"),
        (("spectral_rows", 4, "lambda0"), "1"),
        (("spectral_rows", 7, "lambda1"), "0"),
        (("spectral_rows", 14, "lambda2"), "0"),
        (("spectral_rows", 21, "multiplicity2"), 99),
        (("spectral_rows", 0, "block_status"), "distinct_eigenspaces"),
        (("spectral_rows", 0, "distinct_present_eigenvalue_count"), 3),
        (("spectral_rows", 0, "identity_eigenspace_multiplicity"), None),
        (("spectral_rows", 6, "strict_energy_contraction"), True),
        (("projector_rows", 0, "pi2_is_zero"), False),
        (("projector_rows", 1, "rank_targets", 2), 99),
        (("projector_rows", 2, "pi0", 0, 0), "0"),
        (("projector_rows", 3, "pi1", 0, 1), "0"),
        (("projector_rows", 4, "pi2", 0, 0), "1"),
        (("word_rows", 0, "word_count"), 2),
        (("word_rows", 5, "mean_vector", 0), "7"),
        (("word_rows", 10, "second_moment", 0, 0), "0"),
        (("word_rows", 20, "energy"), "0"),
        (("boundary_rows", "eta_one"), "consensus"),
        (("boundary_rows", "eta_zero"), "three distinct eigenspaces"),
        (("enumeration", "spectral_rows"), 0),
        (("enumeration", "exhaustive_edge_words"), 0),
        (("enumeration", "audited_leaf_count"), 0),
    ]
    for path, value in semantic:
        mutated = copy.deepcopy(data)
        set_path(mutated, path, value)
        mutated["payload_sha256"] = payload_hash(mutated)
        attacks.append(("semantic", json.dumps(mutated, sort_keys=True, indent=2) + "\n", yaml_raw))

    extra = copy.deepcopy(data)
    extra["spectral_rows"][0]["unowned"] = "survive"
    extra["payload_sha256"] = payload_hash(extra)
    attacks.append(("extra-row-key", json.dumps(extra, sort_keys=True, indent=2) + "\n", yaml_raw))
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
        ("yaml-duplicate", yaml_raw + "candidate_id: HCS-C333\n"),
        ("yaml-anchor", yaml_raw.replace("candidate_id: HCS-C333", "candidate_id: &owner HCS-C333", 1)),
        ("yaml-source", yaml_raw.replace(
            "source_commit: 5ca65027918c0fce7ef9af82f3faf2e46ed6530c",
            "source_commit: 0000000000000000000000000000000000000000", 1)),
        ("yaml-authority-rewrite", yaml_raw.replace(
            "evaluator_authority: flow_systems/skills/route-a-evaluator.md",
            "evaluator_authority: route-a-evaluator", 1)),
        ("yaml-authority-delete", yaml_raw.replace(
            "evaluator_authority: flow_systems/skills/route-a-evaluator.md\n", "", 1)),
        ("yaml-status-rewrite-proved", yaml_raw.replace("  evidence_status: PROVED", "  evidence_status: STOP_SCOPED", 1)),
        ("yaml-status-rewrite-scoped", yaml_raw.replace("  evidence_status: STOP_SCOPED", "  evidence_status: PROVED", 1)),
        ("yaml-status-delete", yaml_raw.replace("  evidence_status: PROVED\n", "", 1)),
        ("yaml-route-b", yaml_raw.replace("route_b_invocation_allowed: false", "route_b_invocation_allowed: true", 1)),
        ("yaml-a4", yaml_raw.replace("  verdict: A4_FORMAL_HINT", "  verdict: A4_ROUTE_B_READY", 1)),
        ("yaml-flag", yaml_raw.replace("  claims_target_zero_match: false", "  claims_target_zero_match: true", 1)),
        ("yaml-root-array", "- invalid\n"),
        ("yaml-equivalent-whitespace", yaml_raw + "\n"),
        ("yaml-merge", "base: &b {x: 1}\nmerged:\n  <<: *b\n" + yaml_raw),
        ("yaml-nonstring-key", "1: invalid\n" + yaml_raw),
        ("yaml-implicit-timestamp", yaml_raw.replace("evaluation_date: '2026-09-03'", "evaluation_date: 2026-09-03", 1)),
        ("yaml-unknown-field", yaml_raw + "unknown_field: forbidden\n"),
        ("yaml-type-mutation", yaml_raw.replace("fixed_epoch: 1788393600", 'fixed_epoch: "1788393600"', 1)),
    ]
    attacks.extend((name, json_raw, changed_yaml) for name, changed_yaml in yaml_attacks)

    # Every scalar/list leaf of the evaluator is changed once.  Both nested
    # evaluation hashes and the outer evidence payload hash are repaired, so
    # rejection cannot be attributed to a stale carrier digest.
    evaluation_value = yaml.safe_load(yaml_raw)
    for path, value in leaf_paths(evaluation_value):
        changed = copy.deepcopy(evaluation_value)
        set_path(changed, path, changed_leaf(value))
        rendered_yaml = yaml.safe_dump(changed, sort_keys=False, allow_unicode=True)
        repaired_json = repaired_yaml_evidence(data, rendered_yaml, changed)
        label = ".".join(str(part) for part in path)
        attacks.append((f"yaml-repaired-leaf-{label}", repaired_json, rendered_yaml))

    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c333-mutation-") as directory:
        directory = Path(directory)
        for index, (name, raw_json, raw_yaml) in enumerate(attacks):
            evidence = directory / f"attack-{index}.json"
            evaluation = directory / f"attack-{index}.yaml"
            evidence.write_text(raw_json)
            evaluation.write_text(raw_yaml)
            process = subprocess.run(
                [sys.executable, "-B", str(CHECKER), "--evidence", str(evidence), "--evaluation", str(evaluation)],
                env=environment, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
            )
            if process.returncode == 0:
                raise AssertionError(f"hostile attack survived: {name}-{index}")
            rejected += 1
    print(f"C333 hostile mutation suite: PASS {rejected}/{len(attacks)}")


if __name__ == "__main__":
    main()
