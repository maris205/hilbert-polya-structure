#!/usr/bin/env python3
"""Repaired-hash hostile mutation suite for HCS-C370."""
from __future__ import annotations

if not __debug__:
    raise RuntimeError("c370 mutation suite refuses optimized Python")

import argparse
import copy
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "code/c370_brieskorn_reeb_checker.py"
EVIDENCE = ROOT / "results/c370_brieskorn_reeb_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C370/2026-09-04.yaml"
SECTIONS = ("pair_rows", "orbit_type_rows", "rotation_rows", "invariant_rows")


def canonical(value) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def repair(value):
    for section in SECTIONS:
        value["section_sha256"][section] = hashlib.sha256(canonical(value[section])).hexdigest()
    value.pop("payload_sha256", None)
    value["payload_sha256"] = hashlib.sha256(canonical(value)).hexdigest()
    return value


def encode(value) -> bytes:
    return json.dumps(repair(value), sort_keys=True, indent=2, ensure_ascii=False).encode() + b"\n"


def run(evidence_blob=None, yaml_blob=None):
    with tempfile.TemporaryDirectory(prefix="c370-mutation-") as directory:
        evidence_path = Path(directory) / "evidence.json"
        yaml_path = Path(directory) / "evaluation.yaml"
        evidence_path.write_bytes(EVIDENCE.read_bytes() if evidence_blob is None else evidence_blob)
        yaml_path.write_bytes(EVALUATION.read_bytes() if yaml_blob is None else yaml_blob)
        return subprocess.run(
            [sys.executable, str(CHECKER), "--input", str(evidence_path), "--evaluation", str(yaml_path)],
            capture_output=True,
            text=True,
        ).returncode


def main():
    argparse.ArgumentParser().parse_args()
    base = json.loads(EVIDENCE.read_text())
    assert run() == 0
    cases = []

    def add(label, mutation):
        value = copy.deepcopy(base)
        mutation(value)
        cases.append((label, encode(value)))

    add("candidate", lambda x: x.__setitem__("candidate_id", "HCS-C000"))
    add("obstruction", lambda x: x.__setitem__("obstruction_id", "HEN-O000"))
    add("date", lambda x: x.__setitem__("evaluation_date", "2026-09-03"))
    add("source", lambda x: x.__setitem__("source_commit", "0" * 40))
    add("epoch", lambda x: x.__setitem__("fixed_epoch", 0))
    add("scope", lambda x: x.__setitem__("scope_literal", "BROKEN"))
    add("authority", lambda x: x["evaluator"].__setitem__("authority", "wrong"))
    add("authority-version", lambda x: x["evaluator"].__setitem__("version", "9"))
    add("authority-sha", lambda x: x["evaluator"].__setitem__("sha256", "0" * 64))
    add("yaml-path", lambda x: x["route_a_yaml"].__setitem__("relative_path", "wrong"))
    add("yaml-raw", lambda x: x["route_a_yaml"].__setitem__("raw_sha256", "0" * 64))
    add("yaml-semantic", lambda x: x["route_a_yaml"].__setitem__("semantic_sha256", "0" * 64))
    add("domain-p", lambda x: x["parameter_domain"].__setitem__("p_min", 5))
    add("domain-q", lambda x: x["parameter_domain"].__setitem__("q_max", 99))
    add("domain-bool-int", lambda x: x["parameter_domain"].__setitem__("p_q_odd", 1))
    add("contact-normalization", lambda x: x["conventions"].__setitem__("contact_form", "wrong"))
    add("reeb-speed", lambda x: x["conventions"].__setitem__("reeb_flow", "half speed"))
    add("empty-dimension", lambda x: x["conventions"].__setitem__("fixed_empty_dimension", 0))
    add("determinant-convention", lambda x: x["conventions"].__setitem__("return_determinant", "wrong"))
    add("period-contract", lambda x: x["theorem_contract"].__setitem__("periods", "wrong"))
    add("fixed-contract", lambda x: x["theorem_contract"].__setitem__("fixed_atlas", "all times fixed"))
    add("rotation-contract", lambda x: x["theorem_contract"].__setitem__("rotations", "wrong"))
    add("index-contract", lambda x: x["theorem_contract"].__setitem__("indices", "wrong sign"))
    add("quotient-contract", lambda x: x["theorem_contract"].__setitem__("quotient", "torus"))
    add("sign-contract", lambda x: x["theorem_contract"].__setitem__("sign", "zero exists"))
    add("collision", lambda x: x["collision_boundary"].__setitem__("C242", "same mechanism"))
    add("nonclaim", lambda x: x["nonclaims"].__setitem__(0, "rational-prime taxonomy"))
    add("reference", lambda x: x["references"][0].__setitem__("doi", "wrong"))
    add("scope-flag", lambda x: x["scope_flags"].__setitem__("claims_target_euler_factors", True))
    add("scope-bool-int", lambda x: x["scope_flags"].__setitem__("claims_root_number", 0))
    add("tuple", lambda x: x["route_a"]["tuple"].__setitem__(0, "A0_PASS"))
    add("overall", lambda x: x["route_a"].__setitem__("overall", "ROUTE_A_ACCEPTED"))
    add("route-b", lambda x: x["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("route-b-bool-int", lambda x: x["route_a"].__setitem__("route_b_invocation_allowed", 0))
    add("theorem-status", lambda x: x["route_a"].__setitem__("theorem_status", "OPEN"))
    add("evidence-role", lambda x: x.__setitem__("finite_evidence_role", "proof by enumeration"))
    add("extra-top", lambda x: x.__setitem__("unexpected", 1))
    add("missing-top", lambda x: x.pop("conventions"))

    # These repaired-hash mathematical attacks require full independent recomputation.
    add("grid-fixed-count", lambda x: x["finite_grid"].__setitem__("fixed_time_cell_count", 5_469_177))
    add("grid-fixed-digest", lambda x: x["finite_grid"].__setitem__("fixed_time_sha256", "0" * 64))
    add("pair-period", lambda x: x["pair_rows"][0].__setitem__("principal_period", 29))
    add("pair-class-count", lambda x: x["pair_rows"][0]["fixed_class_counts"].__setitem__("empty", 0))
    add("orbit-isotropy", lambda x: x["orbit_type_rows"][0].__setitem__("isotropy_order", 1))
    add("rotation-denominator", lambda x: x["rotation_rows"][0]["rotation_number"].__setitem__("denominator", 4))
    add("rotation-degeneracy", lambda x: x["rotation_rows"][0].__setitem__("first_degenerate_cover", 4))
    add("invariant-index", lambda x: x["invariant_rows"][0].__setitem__("principal_robbin_salamon_index", -2))

    killed = 0
    for label, blob in cases:
        assert run(evidence_blob=blob) != 0, label
        killed += 1

    stale = copy.deepcopy(base)
    stale["pair_rows"][0]["principal_period"] = 29
    stale_blob = json.dumps(stale, sort_keys=True, indent=2).encode() + b"\n"
    assert run(evidence_blob=stale_blob) != 0
    killed += 1

    raw = EVIDENCE.read_bytes()
    duplicate_blob = raw.replace(
        b'{\n  "candidate_id"', b'{\n  "schema": "evil",\n  "candidate_id"', 1
    )
    nonfinite_blob = raw.replace(b'"fixed_epoch": 1788480000', b'"fixed_epoch": NaN', 1)
    for label, blob in (("duplicate-json", duplicate_blob), ("nonfinite-json", nonfinite_blob)):
        assert run(evidence_blob=blob) != 0, label
        killed += 1

    yaml_text = EVALUATION.read_text()
    yaml_attacks = [
        ("yaml-duplicate", yaml_text + "candidate_id: HCS-C370\n"),
        ("yaml-merge", "base: &b {x: 1}\nmerged: {<<: *b}\n" + yaml_text),
        ("yaml-nonstring", "1: bad\n" + yaml_text),
        ("yaml-alias", "anchor: &a bad\nalias: *a\n" + yaml_text),
        ("yaml-timestamp", yaml_text.replace("evaluation_date: '2026-09-04'", "evaluation_date: 2026-09-04")),
        ("yaml-unknown", yaml_text + "unknown_field: true\n"),
        ("yaml-epoch-type", yaml_text.replace("fixed_epoch: 1788480000", "fixed_epoch: '1788480000'")),
        ("yaml-authority", yaml_text.replace("evaluator_authority: flow_systems/skills/route-a-evaluator.md", "evaluator_authority: wrong")),
        ("yaml-status", yaml_text.replace("evidence_status: STOP_SCOPED", "evidence_status: PROVED", 1)),
        ("yaml-artifact", yaml_text.replace("paper/main.pdf", "paper/wrong.pdf")),
        ("yaml-tuple", yaml_text.replace("  - A4_FORMAL_HINT", "  - A4_FAIL")),
        ("yaml-route-b", yaml_text.replace("route_b_invocation_allowed: false", "route_b_invocation_allowed: true")),
    ]
    for label, text in yaml_attacks:
        assert run(yaml_blob=text.encode()) != 0, label
        killed += 1

    expected = len(cases) + 3 + len(yaml_attacks)
    print(
        f"C370 mutation PASS: killed={killed}/{expected} "
        f"repaired_hash_attacks={len(cases)} stale_hash_control=1"
    )


if __name__ == "__main__":
    main()
