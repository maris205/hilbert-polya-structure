#!/usr/bin/env python3
"""Hostile repaired-hash and parser mutations for HCS-C300."""
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
EVIDENCE = ROOT / "results/c300_euler_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C300/2026-09-02.yaml"
CHECKER = ROOT / "code/c300_euler_checker.py"


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
    yaml_raw = EVALUATION.read_text()
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    attacks: list[tuple[str, str, str]] = []
    mutations = [
        (("candidate_id",), "HCS-C000"), (("obstruction_id",), "HEN-O000"),
        (("fixed_epoch",), 1788307201), (("source_commit",), "0" * 40),
        (("scope_literal",), "EXPANDED_SCOPE"), (("evaluator", "sha256"), "0" * 64),
        (("route_a", "overall"), "ROUTE_A_ACCEPTED"), (("route_a", "tuple", 1), "A1_PASS"),
        (("route_a", "route_b_invocation_allowed"), True),
        (("scope_flags", "claims_target_euler_factors"), True),
        (("scope_flags", "claims_root_number"), True),
        (("scope_flags", "claims_hilbert_polya_operator"), True),
        (("proof_contract", "entropy_formula"), "entropy sign unknown"),
        (("proof_contract", "finite_role"), "finite rows prove all data"),
        (("collision_boundary", "C195"), "same system"),
        (("references", 0, "identifier"), "invented"),
        (("enumeration", "case_count"), 19), (("enumeration", "wave_count"), 39),
        (("enumeration", "root_receipt_cells"), 119), (("enumeration", "wave_receipt_cells"), 272),
        (("enumeration", "scaling_receipt_cells"), 19), (("enumeration", "pressureless_receipt_cells"), 15),
        (("enumeration", "boundary_receipt_cells"), 7), (("enumeration", "audited_cell_count"), 436),
        (("enumeration", "wave_kind_counts", "shock"), 16),
        (("enumeration", "pattern_counts", "R-R"), 3),
        (("enumeration", "scaling_pairs", 0, "same_pattern"), False),
        (("enumeration", "pressureless_probes", 0, "separating_rho_star"), "0.5"),
        (("enumeration", "boundary_rows", 0, "boundary_id"), "B0-corrupt"),
        # Nine repaired-hash survivors from the second independent red team.
        (("model", "equations"), False),
        (("theorem_contract", "root"), False),
        (("nonclaims", 0), "Target arithmetic local data are asserted."),
        (("enumeration", "boundary_rows", 0, "statement"), False),
        (("references", 0, "role"), False),
        (("unexpected_top_key",), "surplus"),
        (("enumeration", "cases", 0, "exact_parameters", "a"), "2/2"),
        (("enumeration", "cases", 0, "root_receipts", "root_absolute_error"), 0),
        (("enumeration", "cases", 1, "case_id"), "P01-RR"),
        # Row-ledger, scalar-type, boolean-type, and decimal-canonicality probes.
        (("enumeration", "cases", 0, "unexpected_key"), "surplus"),
        (("enumeration", "cases", 0, "derived_data", "unexpected_key"), "surplus"),
        (("enumeration", "cases", 0, "root_receipts", "unexpected_key"), "surplus"),
        (("enumeration", "cases", 0, "wave_1", "unexpected_key"), "surplus"),
        (("enumeration", "cases", 0, "wave_1", "midpoint", "unexpected_key"), "surplus"),
        (("enumeration", "cases", 1, "wave_2", "strict_entropy"), 1),
        (("enumeration", "cases", 0, "wave_1", "family"), "1"),
        (("enumeration", "scaling_pairs", 0, "unexpected_key"), "surplus"),
        (("enumeration", "pressureless_probes", 0, "unexpected_key"), "surplus"),
        (("enumeration", "boundary_rows", 0, "unexpected_key"), "surplus"),
        (("enumeration", "cases", 0, "intermediate_speed_gap"), "0" + pristine["enumeration"]["cases"][0]["intermediate_speed_gap"]),
    ]
    for index in range(20):
        mutations.append((("enumeration", "cases", index, "intermediate_speed_gap"), "0.0"))
    for index in range(12):
        for family_key in ("wave_1", "wave_2"):
            wave = pristine["enumeration"]["cases"][index][family_key]
            if wave["kind"] == "rarefaction":
                path = ("enumeration", "cases", index, family_key, "left_edge")
            elif wave["kind"] == "shock":
                path = ("enumeration", "cases", index, family_key, "speed_from_outer")
            else:
                path = ("enumeration", "cases", index, family_key, "characteristic_speed")
            mutations.append((path, "999"))
    for path, value in mutations:
        changed = copy.deepcopy(pristine)
        set_path(changed, path, value)
        changed["payload_sha256"] = payload_hash(changed)
        attacks.append(("semantic-" + "-".join(map(str, path)), json.dumps(changed, sort_keys=True, indent=2) + "\n", yaml_raw))

    raw = EVIDENCE.read_text()
    attacks.extend([
        ("stale-payload-hash", raw.replace('"candidate_id": "HCS-C300"', '"candidate_id": "HCS-C000"'), yaml_raw),
        ("duplicate-json-key", raw.replace('{\n', '{\n  "schema": "duplicate",\n', 1), yaml_raw),
        ("nonfinite-json", raw.replace('"fixed_epoch": 1788307200', '"fixed_epoch": NaN'), yaml_raw),
        ("json-top-level-array", "[]\n", yaml_raw),
    ])
    yaml_attacks = [
        ("duplicate-yaml-key", yaml_raw + "candidate_id: HCS-C300\n"),
        ("yaml-anchor", yaml_raw.replace("candidate_id: HCS-C300", "candidate_id: &bad HCS-C300")),
        ("yaml-alias", yaml_raw + "alias_probe: *bad\n"),
        ("yaml-merge", yaml_raw + "merge_probe:\n  <<: {x: y}\n"),
        ("yaml-top-level-array", "- HCS-C300\n"),
        ("yaml-epoch-string", yaml_raw.replace("fixed_epoch: 1788307200", 'fixed_epoch: "1788307200"')),
        ("yaml-tuple-pass", yaml_raw.replace("  - A1_FAIL", "  - A1_PASS", 1)),
        ("yaml-scope-escalation", yaml_raw.replace("NO_BAD_EULER_OR_ROOT_NUMBER", "EXPANDED_SCOPE", 1)),
        # Five semantic survivors from the second independent red team.
        ("yaml-title-false", yaml_raw.replace('title: "Complete positive-density Riemann atlas for one-dimensional isothermal Euler flow"', "title: false")),
        ("yaml-dynamics-false", yaml_raw.replace('dynamics: "rho_t+(rho u)_x=0 and (rho u)_t+(rho u^2+a^2 rho)_x=0"', "dynamics: false")),
        ("yaml-a0-failure-false", yaml_raw.replace('  strongest_failure: "no rational-prime local datum or target Euler factor is constructed"', "  strongest_failure: false", 1)),
        ("yaml-a4-missing-artifact", yaml_raw.replace("    - paper/main.pdf\ntuple:", "tuple:", 1)),
        ("yaml-scope-flag-int", yaml_raw.replace("  claims_target_euler_factors: false", "  claims_target_euler_factors: 0", 1)),
    ]
    attacks.extend((name, raw, changed_yaml) for name, changed_yaml in yaml_attacks)

    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c300-mutations-") as temporary:
        base = Path(temporary)
        for index, (name, evidence_text, yaml_text) in enumerate(attacks):
            evidence_path, yaml_path = base / f"evidence-{index}.json", base / f"evaluation-{index}.yaml"
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
    print(f"C300 hostile mutation suite: PASS {rejected}/{len(attacks)}")


if __name__ == "__main__":
    main()
