#!/usr/bin/env python3
"""Repaired-hash semantic and parser attacks against the C304 checker."""
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
EVIDENCE = ROOT / "results/c304_ch_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C304/2026-09-03.yaml"
CHECKER = ROOT / "code/c304_ch_checker.py"


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def set_path(data, path, value) -> None:
    cursor = data
    for item in path[:-1]:
        cursor = cursor[item]
    cursor[path[-1]] = value


def main() -> None:
    pristine = json.loads(EVIDENCE.read_text())
    yaml_raw = EVALUATION.read_text()
    attacks: list[tuple[str, str, str]] = []
    mutations = [
        (("schema",), "false-schema"), (("candidate_id",), "HCS-C000"),
        (("obstruction_id",), "HEN-O000"), (("evaluation_date",), "2026-09-04"),
        (("fixed_epoch",), 1788393601), (("source_commit",), "0" * 40),
        (("scope_literal",), "EXPANDED_SCOPE"), (("evaluator", "sha256"), "0" * 64),
        (("model", "generator"), False), (("theorem_contract", "spectrum"), False),
        (("proof_contract", "full_dimension"), "finite samples suffice"),
        (("proof_contract", "fastest_exhaustion"), "search shells n<=64"),
        (("proof_contract", "finite_role"), "finite rows prove all dimensions"),
        (("route_a", "tuple", 0), "A0_PASS"), (("route_a", "overall"), "ROUTE_A_ACCEPTED"),
        (("route_a", "route_b_invocation_allowed"), True),
        (("scope_flags", "claims_target_euler_factors"), True),
        (("scope_flags", "claims_root_number"), True),
        (("scope_flags", "claims_hilbert_polya_operator"), True),
        (("nonclaims", 0), "We construct arithmetic local data."),
        (("collision_boundary", "C195"), "identical"),
        (("references", 0, "identifier"), "invented"),
        (("references", 0, "role"), False),
        (("boundaries", 2, "statement"), False),
        (("enumeration", "case_count"), 17), (("enumeration", "audited_cell_count"), 1652),
        (("enumeration", "case_ids", 0), "D1-CRITICAL"),
        (("cases", 0, "dimension"), True), (("cases", 0, "kappa"), "2/2"),
        (("cases", 0, "ratio_alpha_over_kappa"), "-2/2"),
        (("cases", 0, "analytic_exhaustion_cutoff"), 64),
        (("cases", 0, "chamber"), "spinodal_unstable"),
        (("cases", 0, "fastest_shells"), [2]), (("cases", 1, "neutral_shells"), []),
        (("cases", 2, "morse_index"), 999), (("cases", 3, "kernel_dimension"), True),
        (("cases", 4, "spectral_bound"), "0/1"),
        (("cases", 5, "shell_rows", 0, "multiplicity"), True),
        (("cases", 6, "shell_rows", 1, "eigenvalue"), "0/1"),
        (("cases", 7, "shell_rows", 2, "energy_coefficient"), "1/1"),
        (("cases", 8, "shell_rows", 3, "classification"), "absent"),
        (("cases", 9, "shell_rows", 4, "trace_term_t_one_third"), 0),
        (("support_probes", 0, "leading_shells"), [1]),
        (("support_probes", 1, "leading_rate"), "0/1"),
        (("support_probes", 2, "normalized_limit"), False),
        (("support_probes", 3, "support", 0, "coefficient"), "3/1"),
        (("kappa_zero_boundary", 0, "classification"), "identity_semigroup"),
        (("kappa_zero_boundary", 1, "spectrum_bounded_above"), 1),
        (("kappa_zero_boundary", 2, "first_four_mode_rates", 3), "999"),
    ]
    for path, value in mutations:
        changed = copy.deepcopy(pristine)
        set_path(changed, path, value)
        changed["payload_sha256"] = payload_hash(changed)
        attacks.append(("semantic-" + "-".join(map(str, path)), json.dumps(changed, sort_keys=True, indent=2) + "\n", yaml_raw))

    # Exact-key and ordered-identity attacks, also repaired with a valid self-hash.
    for name, mutator in (
        ("extra-top-key", lambda d: d.__setitem__("unexpected", False)),
        ("extra-case-key", lambda d: d["cases"][0].__setitem__("unexpected", 0)),
        ("extra-row-key", lambda d: d["cases"][0]["shell_rows"][0].__setitem__("unexpected", 0)),
        ("duplicate-case-id", lambda d: d["cases"][1].__setitem__("case_id", d["cases"][0]["case_id"])),
        ("reordered-cases", lambda d: d["cases"].reverse()),
        ("missing-boundary", lambda d: d["boundaries"].pop()),
    ):
        changed = copy.deepcopy(pristine)
        mutator(changed)
        changed["payload_sha256"] = payload_hash(changed)
        attacks.append((name, json.dumps(changed, sort_keys=True, indent=2) + "\n", yaml_raw))

    raw = EVIDENCE.read_text()
    attacks.extend([
        ("stale-payload-hash", raw.replace('"candidate_id": "HCS-C304"', '"candidate_id": "HCS-C000"', 1), yaml_raw),
        ("duplicate-json-key", raw.replace("{\n", '{\n  "schema": "duplicate",\n', 1), yaml_raw),
        ("nonfinite-json", raw.replace('"fixed_epoch": 1788393600', '"fixed_epoch": NaN', 1), yaml_raw),
        ("json-top-array", "[]\n", yaml_raw),
    ])
    yaml_attacks = [
        ("duplicate-yaml-key", yaml_raw + "candidate_id: HCS-C304\n"),
        ("yaml-anchor", yaml_raw.replace("candidate_id: HCS-C304", "candidate_id: &bad HCS-C304", 1)),
        ("yaml-alias", yaml_raw + "alias_probe: *bad\n"),
        ("yaml-merge", yaml_raw + "merge_probe:\n  <<: {x: y}\n"),
        ("yaml-top-array", "- HCS-C304\n"),
        ("yaml-epoch-string", yaml_raw.replace("fixed_epoch: 1788393600", 'fixed_epoch: "1788393600"', 1)),
        ("yaml-title-false", yaml_raw.replace('title: "Full-dimensional linear periodic Cahn--Hilliard spinodal semigroup atlas"', "title: false", 1)),
        ("yaml-dynamics-false", yaml_raw.replace('dynamics: "partial_t u=-kappa Delta^2 u-alpha Delta u"', "dynamics: false", 1)),
        ("yaml-a0-failure-false", yaml_raw.replace('  strongest_failure: "no rational-prime local datum or target Euler factor is constructed"', "  strongest_failure: false", 1)),
        ("yaml-a4-artifact-missing", yaml_raw.replace("    - SOURCE_AUDIT.md\n    - paper/main.pdf", "    - SOURCE_AUDIT.md", 1)),
        ("yaml-scope-int", yaml_raw.replace("  claims_target_euler_factors: false", "  claims_target_euler_factors: 0", 1)),
        ("yaml-tuple-pass", yaml_raw.replace("  - A0_FAIL", "  - A0_PASS", 1)),
        ("yaml-scope-escalation", yaml_raw.replace("NO_BAD_EULER_OR_ROOT_NUMBER", "EXPANDED_SCOPE", 1)),
    ]
    attacks.extend((name, raw, altered) for name, altered in yaml_attacks)

    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c304-mutations-") as temporary:
        base = Path(temporary)
        for index, (name, evidence_text, yaml_text) in enumerate(attacks):
            evidence_path = base / f"evidence-{index}.json"
            evaluation_path = base / f"evaluation-{index}.yaml"
            evidence_path.write_text(evidence_text)
            evaluation_path.write_text(yaml_text)
            completed = subprocess.run(
                [sys.executable, "-B", str(CHECKER), "--evidence", str(evidence_path), "--evaluation", str(evaluation_path)],
                env=env,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
            )
            if completed.returncode == 0:
                raise AssertionError(f"mutation survived: {name}")
            rejected += 1
    if rejected != len(attacks):
        raise AssertionError("mutation accounting mismatch")
    print(f"C304 hostile mutation suite: PASS {rejected}/{len(attacks)}")


if __name__ == "__main__":
    main()
