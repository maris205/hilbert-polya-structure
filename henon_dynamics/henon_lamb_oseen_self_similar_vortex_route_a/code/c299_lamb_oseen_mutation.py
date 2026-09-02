#!/usr/bin/env python3
"""Hostile semantic and parser mutations for the HCS-C299 checker."""
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
EVIDENCE = ROOT / "results/c299_lamb_oseen_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C299/2026-09-02.yaml"
CHECKER = ROOT / "code/c299_lamb_oseen_checker.py"


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def set_path(data, path, value):
    cursor = data
    for item in path[:-1]:
        cursor = cursor[item]
    cursor[path[-1]] = value


def main() -> None:
    pristine = json.loads(EVIDENCE.read_text())
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    attacks: list[tuple[str, str, str]] = []

    evidence_mutations = [
        (("candidate_id",), "HCS-C000"), (("obstruction_id",), "HEN-O000"),
        (("fixed_epoch",), 1788307201), (("source_commit",), "0" * 40),
        (("scope_literal",), "EXPANDED_SCOPE"), (("evaluator", "sha256"), "0" * 64),
        (("route_a", "overall"), "ROUTE_A_ACCEPTED"), (("route_a", "tuple", 0), "A0_PASS"),
        (("route_a", "route_b_invocation_allowed"), True),
        (("scope_flags", "claims_target_euler_factors"), True),
        (("scope_flags", "claims_root_number"), True),
        (("scope_flags", "claims_hilbert_polya_operator"), True),
        (("theorem_contract", "classification"), "all vortices are Gaussian"),
        (("theorem_contract", "lagrangian"), "angle modulo 2pi only"),
        (("proof_contract", "uniqueness_ode"), "constant not controlled"),
        (("proof_contract", "finite_role"), "finite rows prove the theorem"),
        (("nonclaims", 0), "arithmetic promotion"),
        (("references", 0, "identifier"), "invented"),
        (("references", 0, "role"), "priority claim"),
        (("references", 1, "verification"), "unchecked"),
        (("collision_boundary", "C206"), "same system"),
        (("enumeration", "boundary_rows", 0, "statement"), "corrupt boundary"),
        (("enumeration", "field_cases", 0, "Gamma"), "0/1"),
        (("enumeration", "field_cases", 0, "unexpected_key"), "surplus"),
        (("enumeration", "field_cases", 0, "point_rows", 0, "unexpected_key"), "surplus"),
        (("enumeration", "field_case_count"), 9),
        (("enumeration", "point_receipt_cells"), 71),
        (("enumeration", "moment_receipt_cells"), 71),
        (("enumeration", "lp_receipt_cells"), 47),
        (("enumeration", "lagrangian_receipt_cells"), 11),
        (("enumeration", "boundary_receipt_cells"), 8),
        (("enumeration", "audited_cell_count"), 212),
    ]
    for case_index in range(8):
        evidence_mutations.extend([
            (("enumeration", "field_cases", case_index, "core_radius_squared"), "999"),
            (("enumeration", "field_cases", case_index, "point_rows", case_index % 9, "exp_minus_x"), "0.123"),
            (("enumeration", "field_cases", case_index, "moment_rows", case_index, "radial_moment_over_gamma"), "999"),
            (("enumeration", "field_cases", case_index, "lp_rows", case_index % 6, "scaled_lp_power_coefficient"), "999"),
        ])
    for row_index in range(8):
        evidence_mutations.append((("enumeration", "lagrangian_cases", row_index, "angle_increment"), "0.123"))
    for path, value in evidence_mutations:
        changed = copy.deepcopy(pristine)
        set_path(changed, path, value)
        changed["payload_sha256"] = payload_hash(changed)
        attacks.append(("semantic-" + "-".join(map(str, path)), json.dumps(changed, sort_keys=True, indent=2) + "\n", EVALUATION.read_text()))

    raw = EVIDENCE.read_text()
    attacks.extend([
        ("stale-payload-hash", raw.replace('"candidate_id": "HCS-C299"', '"candidate_id": "HCS-C000"'), EVALUATION.read_text()),
        ("duplicate-json-key", raw.replace('{\n', '{\n  "schema": "duplicate",\n', 1), EVALUATION.read_text()),
        ("nonfinite-json", raw.replace('"fixed_epoch": 1788307200', '"fixed_epoch": NaN'), EVALUATION.read_text()),
        ("json-top-level-array", "[]\n", EVALUATION.read_text()),
    ])
    yaml_raw = EVALUATION.read_text()
    yaml_attacks = [
        ("duplicate-yaml-key", yaml_raw + "candidate_id: HCS-C299\n"),
        ("yaml-anchor", yaml_raw.replace("candidate_id: HCS-C299", "candidate_id: &bad HCS-C299")),
        ("yaml-alias", yaml_raw + "alias_probe: *bad\n"),
        ("yaml-merge", yaml_raw + "merge_probe:\n  <<: {x: y}\n"),
        ("yaml-top-level-array", "- HCS-C299\n"),
        ("yaml-epoch-string", yaml_raw.replace("fixed_epoch: 1788307200", 'fixed_epoch: "1788307200"')),
        ("yaml-tuple-pass", yaml_raw.replace("  - A0_FAIL", "  - A0_PASS", 1)),
        ("yaml-scope-escalation", yaml_raw.replace("NO_BAD_EULER_OR_ROOT_NUMBER", "EXPANDED_SCOPE", 1)),
    ]
    attacks.extend((name, raw, altered) for name, altered in yaml_attacks)

    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c299-mutations-") as temporary:
        base = Path(temporary)
        for index, (name, evidence_text, yaml_text) in enumerate(attacks):
            evidence_path = base / f"evidence-{index}.json"
            yaml_path = base / f"evaluation-{index}.yaml"
            evidence_path.write_text(evidence_text)
            yaml_path.write_text(yaml_text)
            result = subprocess.run(
                [sys.executable, "-B", str(CHECKER), "--evidence", str(evidence_path), "--evaluation", str(yaml_path)],
                env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            )
            if result.returncode == 0:
                raise AssertionError(f"mutation survived: {name}")
            rejected += 1
    assert rejected == len(attacks)
    print(f"C299 hostile mutation suite: PASS {rejected}/{len(attacks)}")


if __name__ == "__main__":
    main()
