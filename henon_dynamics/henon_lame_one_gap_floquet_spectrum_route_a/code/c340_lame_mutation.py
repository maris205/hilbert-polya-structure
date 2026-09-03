#!/usr/bin/env python3
"""Repaired-hash hostile mutations for HCS-C340."""
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
EVIDENCE = ROOT / "results/c340_lame_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C340/2026-09-03.yaml"
CHECKER = ROOT / "code/c340_lame_checker.py"


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def repair(data):
    changed = copy.deepcopy(data)
    body = dict(changed)
    body.pop("payload_sha256", None)
    changed["payload_sha256"] = digest(body)
    return json.dumps(changed, sort_keys=True, indent=2, ensure_ascii=False) + "\n"


def set_path(data, path, value):
    cursor = data
    for key in path[:-1]:
        cursor = cursor[key]
    cursor[path[-1]] = value


def yaml_repair(data, raw):
    semantic = yaml.safe_load(raw)
    changed = copy.deepcopy(data)
    changed["route_a_yaml"]["raw_sha256"] = hashlib.sha256(raw.encode()).hexdigest()
    changed["route_a_yaml"]["semantic_sha256"] = digest(semantic)
    return repair(changed)


def main():
    if sys.flags.optimize:
        raise RuntimeError("C340 mutation lane refuses optimized Python")
    data = json.loads(EVIDENCE.read_text())
    json_raw = EVIDENCE.read_text()
    yaml_raw = EVALUATION.read_text()
    attacks = []
    repaired = [
        (("candidate_id",), "HCS-C000"),
        (("obstruction_id",), "HEN-O000"),
        (("evaluation_date",), "2099-01-01"),
        (("source_commit",), "0" * 40),
        (("scope_literal",), "EXPANDED"),
        (("evaluator", "authority"), "forged"),
        (("evaluator", "version"), "9.9.9"),
        (("evaluator", "sha256"), "0" * 64),
        (("route_a_yaml", "relative_path"), "evaluation.yaml"),
        (("route_a_yaml", "raw_sha256"), "0" * 64),
        (("route_a_yaml", "semantic_sha256"), "0" * 64),
        (("model", "operator"), "wrong sign Laplacian"),
        (("model", "fiber_domain"), "unspecified domain"),
        (("theorem_contract", "spectrum"), "one interval"),
        (("theorem_contract", "spectral_type"), "pure point"),
        (("theorem_contract", "gap_count"), "finite evidence proves all gaps"),
        (("theorem_contract", "spectral_curve"), "wrong factor"),
        (("theorem_contract", "fiber_skew_adjointness"), "formal integration by parts without endpoint conditions"),
        (("boundary_atlas", "free_face"), "gap remains open"),
        (("collision_boundary", "C262"), "same owner"),
        (("route_a", "tuple", 4), "A4_ROUTE_B_READY"),
        (("route_a", "overall"), "ROUTE_A_ACCEPTED"),
        (("route_a", "route_b_invocation_allowed"), True),
        (("scope_flags", "claims_hilbert_polya_operator"), True),
        (("rational_modulus_rows", 0, "upper_band_start"), "8/2"),
        (("rational_modulus_rows", 50, "gap_width"), "0"),
        (("rational_modulus_rows", 198, "band_edge_modes", 1, "fiber"), "periodic"),
        (("rational_modulus_rows", 100, "spectral_curve_coefficients_descending", 1), "-8/2"),
        (("enumeration", "audited_leaf_count"), 0),
        (("nonclaims", 4), "finite grid proves all gaps"),
        (("references", 0, "identifier"), "DOI:0.0/fabricated"),
        (("references", 3, "identifier"), "DOI:0.0/fabricated-floquet-source"),
    ]
    for path, value in repaired:
        changed = copy.deepcopy(data)
        set_path(changed, path, value)
        attacks.append(("repaired-" + ".".join(map(str, path)), repair(changed), yaml_raw))
    extra = copy.deepcopy(data)
    extra["rational_modulus_rows"][0]["unowned"] = 1
    attacks.append(("repaired-nested-extra", repair(extra), yaml_raw))
    omitted = copy.deepcopy(data)
    omitted["rational_modulus_rows"].pop()
    attacks.append(("repaired-omitted-row", repair(omitted), yaml_raw))
    duplicate = copy.deepcopy(data)
    duplicate["rational_modulus_rows"].insert(0, copy.deepcopy(duplicate["rational_modulus_rows"][0]))
    attacks.append(("repaired-duplicate-row", repair(duplicate), yaml_raw))
    missing = copy.deepcopy(data)
    del missing["boundary_atlas"]
    attacks.append(("repaired-missing-top", repair(missing), yaml_raw))
    stale = copy.deepcopy(data)
    stale["candidate_id"] = "HCS-C000"
    attacks.append(("stale-hash-control", json.dumps(stale, sort_keys=True, indent=2) + "\n", yaml_raw))
    attacks.extend([
        ("duplicate-json", json_raw.replace('{\n', '{\n  "schema": "duplicate",\n', 1), yaml_raw),
        ("nonfinite-json", json_raw.replace('"fixed_epoch": 1788393600', '"fixed_epoch": Infinity', 1), yaml_raw),
        ("json-root-array", "[]\n", yaml_raw),
    ])
    yaml_changes = [
        ("yaml-authority", yaml_raw.replace("evaluator_authority: flow_systems/skills/route-a-evaluator.md", "evaluator_authority: forged", 1)),
        ("yaml-evaluator-hash", yaml_raw.replace("6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c", "0" * 64, 1)),
        ("yaml-evidence-status", yaml_raw.replace("  evidence_status: PROVED", "  evidence_status: STOP_SCOPED", 1)),
        ("yaml-verdict", yaml_raw.replace("  verdict: A4_NATURAL_QUANTIZATION", "  verdict: A4_ROUTE_B_READY", 1)),
        ("yaml-route-b", yaml_raw.replace("route_b_invocation_allowed: false", "route_b_invocation_allowed: true", 1)),
        ("yaml-source", yaml_raw.replace("source_commit: e2d94f886963cbe3d42b83f6ef542413a163d3a4", "source_commit: " + "0" * 40, 1)),
        ("yaml-source-owner", yaml_raw.replace("  - 10.1090/bull/1528", "  - 10.1090/bull/9999", 1)),
        ("yaml-unknown", yaml_raw + "unknown_field: forbidden\n"),
        ("yaml-whitespace", yaml_raw + "\n"),
    ]
    for name, changed_yaml in yaml_changes:
        attacks.append(("repaired-" + name, yaml_repair(data, changed_yaml), changed_yaml))
    attacks.extend([
        ("yaml-duplicate", json_raw, yaml_raw + "candidate_id: HCS-C340\n"),
        ("yaml-anchor", json_raw, yaml_raw.replace("candidate_id: HCS-C340", "candidate_id: &owner HCS-C340", 1)),
        ("yaml-alias", json_raw, "owner: &o HCS-C340\ncandidate_id: *o\n" + yaml_raw),
        ("yaml-merge", json_raw, "base: &b {x: 1}\nmerged:\n  <<: *b\n" + yaml_raw),
        ("yaml-nonstring-key", json_raw, "1: invalid\n" + yaml_raw),
        ("yaml-root-array", json_raw, "- invalid\n"),
    ])
    rejected = 0
    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    with tempfile.TemporaryDirectory(prefix="c340-hostile-") as directory:
        work = Path(directory)
        for index, (name, evidence_raw, evaluation_raw) in enumerate(attacks):
            evidence = work / f"attack-{index}.json"
            evaluation = work / f"attack-{index}.yaml"
            evidence.write_text(evidence_raw)
            evaluation.write_text(evaluation_raw)
            process = subprocess.run([sys.executable, "-B", str(CHECKER), "--evidence", str(evidence), "--evaluation", str(evaluation)],
                                     env=environment, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            if process.returncode == 0:
                raise AssertionError(f"hostile attack survived: {name}")
            rejected += 1
    print(f"C340 hostile mutation suite: PASS {rejected}/{len(attacks)}")


if __name__ == "__main__":
    main()
