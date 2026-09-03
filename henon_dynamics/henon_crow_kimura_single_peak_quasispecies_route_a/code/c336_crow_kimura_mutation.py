#!/usr/bin/env python3
"""Repaired-hash hostile mutation suite for HCS-C336."""
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
CHECKER = ROOT / "code/c336_crow_kimura_checker.py"
EVIDENCE = ROOT / "results/c336_crow_kimura_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C336/2026-09-03.yaml"


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def repaired(data) -> str:
    value = copy.deepcopy(data)
    value.pop("payload_sha256", None)
    value["payload_sha256"] = digest(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    )
    return json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False) + "\n"


def changed(data, path, value):
    answer = copy.deepcopy(data)
    cursor = answer
    for key in path[:-1]:
        cursor = cursor[key]
    cursor[path[-1]] = value
    return answer


def yaml_repaired_evidence(data, raw_yaml: str, semantic) -> str:
    answer = copy.deepcopy(data)
    answer["evaluation"]["raw_sha256"] = digest(raw_yaml.encode())
    answer["evaluation"]["semantic_sha256"] = digest(
        json.dumps(semantic, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    )
    return repaired(answer)


def run_checker(evidence: Path, evaluation: Path):
    return subprocess.run(
        [sys.executable, "-B", str(CHECKER), "--evidence", str(evidence), "--evaluation", str(evaluation)],
        env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC"),
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
    )


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C336 mutation suite refuses optimized Python")
    data = json.loads(EVIDENCE.read_text())
    json_raw = EVIDENCE.read_text()
    yaml_raw = EVALUATION.read_text()
    attacks: list[tuple[str, str, str]] = []

    semantic_changes = [
        (("schema",), "hcs-c336-false"),
        (("candidate_id",), "HCS-C335"),
        (("obstruction_id",), "HEN-O319"),
        (("source_commit",), "0" * 40),
        (("fixed_epoch",), 0),
        (("scope_literal",), "UNSCOPED"),
        (("evaluator_authority_sha256",), "0" * 64),
        (("model", "normalization"), "omit mean fitness"),
        (("theorem", "retained"), "wrong multiplicity"),
        (("theorem", "interlacing"), "roots may collide"),
        (("spectral_rows", 0, "dimension"), 3),
        (("spectral_rows", 0, "U"), "2"),
        (("spectral_rows", 0, "poles", 1), "-1"),
        (("spectral_rows", 0, "weights", 0), "3/4"),
        (("spectral_rows", 4, "retained", 1, "multiplicity"), 99),
        (("spectral_rows", 8, "secular_coefficients_ascending", 0), "0"),
        (("spectral_rows", 10, "full_characteristic_coefficients_ascending", 0), "1"),
        (("spectral_rows", 12, "trace"), "0"),
        (("spectral_rows", 15, "root_count"), 1),
        (("spectral_rows", 18, "interlacing_intervals", 0, "left"), "-1"),
        (("spectral_rows", 21, "no_root_below"), "0"),
        (("walsh_rows", 0, "walsh_masks", 0), 0),
        (("walsh_rows", 3, "eigenvalue"), "0"),
        (("walsh_rows", 7, "residual_l1"), "1"),
        (("flow_rows", 0, "mean_fitness"), "0"),
        (("flow_rows", 2, "initial", 0), "0"),
        (("flow_rows", 4, "derivative_mass"), "1"),
        (("boundary_rows", 0, "stationary_law"), "master"),
        (("boundary_rows", 8, "conclusion"), "converges_to_master"),
        (("boundary_rows", 10, "retained_multiplicity_total"), 1),
        (("counts", "spectral_rows"), 29),
        (("references", 0, "identifier"), "fabricated"),
        (("collisions", "C171"), "same owner"),
        (("nonclaims", 0), "A finite-L threshold is proved."),
        (("route_tuple", 4), "A4_ROUTE_B_READY"),
        (("overall_verdict",), "ROUTE_A_PASS"),
        (("scope_flags", "claims_target_euler_factors"), True),
        (("scope_flags", "claims_target_zero_match"), True),
        (("scope_flags", "invokes_route_b"), True),
        (("evaluation", "raw_sha256"), "0" * 64),
        (("evaluation", "semantic_sha256"), "0" * 64),
    ]
    for index, (path, value) in enumerate(semantic_changes):
        attacks.append((f"semantic-{index}", repaired(changed(data, path, value)), yaml_raw))

    extra = copy.deepcopy(data)
    extra["unexpected"] = True
    missing = copy.deepcopy(data)
    missing.pop("model")
    attacks.extend([
        ("extra-top-key", repaired(extra), yaml_raw),
        ("missing-top-key", repaired(missing), yaml_raw),
        ("duplicate-json", json_raw.replace("{\n", '{\n  "schema": "duplicate",\n', 1), yaml_raw),
        ("nan-json", json_raw.replace('"fixed_epoch": 1788393600', '"fixed_epoch": NaN', 1), yaml_raw),
        ("json-root-array", "[]\n", yaml_raw),
        ("stale-hash-control", json_raw.replace('"root_count": 2', '"root_count": 99', 1), yaml_raw),
    ])

    yaml_attacks = [
        ("yaml-duplicate", yaml_raw + "candidate_id: HCS-C336\n"),
        ("yaml-anchor", yaml_raw.replace("candidate_id: HCS-C336", "candidate_id: &owner HCS-C336", 1)),
        ("yaml-alias", yaml_raw + "alias: *owner\n"),
        ("yaml-merge", "base: &b {x: 1}\nmerged:\n  <<: *b\n" + yaml_raw),
        ("yaml-nonstring-key", "1: invalid\n" + yaml_raw),
        ("yaml-root-array", "- invalid\n"),
        ("yaml-source", yaml_raw.replace(SOURCE_TOKEN := "db2c816b7b6bd450f51f79b91842cb882b0bd773", "0" * 40, 1)),
        ("yaml-epoch-type", yaml_raw.replace("fixed_epoch: 1788393600", 'fixed_epoch: "1788393600"', 1)),
        ("yaml-date-type", yaml_raw.replace("evaluation_date: '2026-09-03'", "evaluation_date: 2026-09-03", 1)),
        ("yaml-scope", yaml_raw.replace("scope_literal: NO_BAD_EULER_OR_ROOT_NUMBER", "scope_literal: UNSCOPED", 1)),
        ("yaml-route-b", yaml_raw.replace("route_b_invocation_allowed: false", "route_b_invocation_allowed: true", 1)),
        ("yaml-a4", yaml_raw.replace("  verdict: A4_FORMAL_HINT", "  verdict: A4_ROUTE_B_READY", 1)),
        ("yaml-status", yaml_raw.replace("  evidence_status: STOP_SCOPED", "  evidence_status: PROVED", 1)),
        ("yaml-flag", yaml_raw.replace("  claims_root_number: false", "  claims_root_number: true", 1)),
        ("yaml-tuple", yaml_raw.replace("  - A1_FAIL", "  - A1_PASS_ANALYTIC", 1)),
        ("yaml-unknown", yaml_raw + "unknown_field: forbidden\n"),
        ("yaml-whitespace", yaml_raw + "\n"),
    ]
    attacks.extend((name, json_raw, raw) for name, raw in yaml_attacks)

    semantic_yaml = yaml.safe_load(yaml_raw)
    yaml_leaf_changes = [
        (("candidate_id",), "HCS-C999"),
        (("obstruction_id",), "HEN-O999"),
        (("a0", "verdict"), "A0_WEAK_ARITHMETIC_RELATION"),
        (("a1", "evidence_status"), "STOP_SCOPED"),
        (("scope_flags", "claims_automorphy"), True),
        (("overall_verdict",), "ROUTE_A_EXPLORATORY"),
    ]
    for index, (path, value) in enumerate(yaml_leaf_changes):
        altered = copy.deepcopy(semantic_yaml)
        cursor = altered
        for key in path[:-1]:
            cursor = cursor[key]
        cursor[path[-1]] = value
        rendered = yaml.safe_dump(altered, sort_keys=False, allow_unicode=True)
        evidence = yaml_repaired_evidence(data, rendered, altered)
        attacks.append((f"yaml-repaired-leaf-{index}", evidence, rendered))

    with tempfile.TemporaryDirectory(prefix="c336-mutation-") as directory:
        work = Path(directory)
        valid_evidence = work / "valid.json"
        valid_yaml = work / "valid.yaml"
        valid_evidence.write_text(json_raw)
        valid_yaml.write_text(yaml_raw)
        valid = run_checker(valid_evidence, valid_yaml)
        if valid.returncode != 0:
            raise AssertionError("baseline rejected: " + valid.stdout)
        accepted = []
        for index, (name, raw_json, raw_yaml) in enumerate(attacks):
            evidence = work / f"attack-{index}.json"
            evaluation = work / f"attack-{index}.yaml"
            evidence.write_text(raw_json)
            evaluation.write_text(raw_yaml)
            process = run_checker(evidence, evaluation)
            if process.returncode == 0:
                accepted.append(name)
    if accepted:
        raise AssertionError(f"hostile mutations accepted: {accepted}")
    print(f"C336 hostile mutation suite: PASS {len(attacks)}/{len(attacks)}")


if __name__ == "__main__":
    main()
