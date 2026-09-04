#!/usr/bin/env python3
"""Repaired-hash hostile mutation suite for HCS-C377."""
from __future__ import annotations

if not __debug__:
    raise RuntimeError("c377 mutation suite refuses optimized Python")

import argparse
import copy
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "code/c377_periodic_clm_checker.py"
EVIDENCE = ROOT / "results/c377_periodic_clm_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C377/2026-09-04.yaml"
PAPER = ROOT / "paper/main.tex"
SECTIONS = (
    "multiplier_rows", "tricomi_rows", "zero_mean_rows", "nonzero_mean_rows",
    "one_mode_rows", "arithmetic_control_rows", "nonzero_profile_rows", "zero_profile_rows",
    "boundary_rows",
)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def repair(value):
    for section in SECTIONS:
        if section in value and section in value.get("section_sha256", {}):
            value["section_sha256"][section] = hashlib.sha256(canonical(value[section])).hexdigest()
    value.pop("payload_sha256", None)
    value["payload_sha256"] = hashlib.sha256(canonical(value)).hexdigest()
    return value


def encode(value):
    return json.dumps(repair(value), sort_keys=True, indent=2, ensure_ascii=False).encode() + b"\n"


def run(evidence_blob=None, yaml_blob=None, paper_blob=None):
    with tempfile.TemporaryDirectory(prefix="c377-mutation-") as directory:
        ep = Path(directory) / "evidence.json"
        yp = Path(directory) / "evaluation.yaml"
        pp = Path(directory) / "main.tex"
        ep.write_bytes(EVIDENCE.read_bytes() if evidence_blob is None else evidence_blob)
        yp.write_bytes(EVALUATION.read_bytes() if yaml_blob is None else yaml_blob)
        pp.write_bytes(PAPER.read_bytes() if paper_blob is None else paper_blob)
        return subprocess.run([
            sys.executable, "-B", str(CHECKER), "--input", str(ep),
            "--evaluation", str(yp), "--paper", str(pp),
        ], capture_output=True, text=True).returncode


def main():
    argparse.ArgumentParser().parse_args()
    base = json.loads(EVIDENCE.read_text())
    assert run() == 0
    cases = []

    def add(label, mutation):
        value = copy.deepcopy(base)
        mutation(value)
        cases.append((label, encode(value)))

    add("schema", lambda x: x.__setitem__("schema", "wrong"))
    add("candidate", lambda x: x.__setitem__("candidate_id", "HCS-C000"))
    add("obstruction", lambda x: x.__setitem__("obstruction_id", "HEN-O000"))
    add("date", lambda x: x.__setitem__("evaluation_date", "2026-09-03"))
    add("source", lambda x: x.__setitem__("source_commit", "00000000"))
    add("epoch", lambda x: x.__setitem__("fixed_epoch", 0))
    add("scope", lambda x: x.__setitem__("scope_literal", "BROKEN"))
    add("authority", lambda x: x["evaluator"].__setitem__("authority", "wrong"))
    add("authority-version", lambda x: x["evaluator"].__setitem__("version", "9"))
    add("authority-sha", lambda x: x["evaluator"].__setitem__("sha256", "0" * 64))
    add("yaml-path", lambda x: x["route_a_yaml"].__setitem__("relative_path", "wrong"))
    add("yaml-raw", lambda x: x["route_a_yaml"].__setitem__("raw_sha256", "0" * 64))
    add("yaml-semantic", lambda x: x["route_a_yaml"].__setitem__("semantic_sha256", "0" * 64))
    for key in ("equation", "hilbert", "decomposition", "tricomi", "riccati", "arccot_branch"):
        add("convention-" + key, lambda x, key=key: x["conventions"].__setitem__(key, "wrong"))
    for key in ("mean", "zero_mean", "nonzero_mean", "nonzero_omega", "nonzero_criterion", "zero_criterion", "one_mode", "profile", "boundaries"):
        add("contract-" + key, lambda x, key=key: x["theorem_contract"].__setitem__(key, "wrong"))
    add("grid-multiplier", lambda x: x["finite_grid"].__setitem__("hilbert_multiplier_count", 255))
    add("grid-tricomi", lambda x: x["finite_grid"].__setitem__("tricomi_polynomial_count", 1023))
    add("grid-profile", lambda x: x["finite_grid"].__setitem__("zero_mean_profile_count", 255))
    add("grid-control", lambda x: x["finite_grid"].__setitem__("arithmetic_control_count", 3))
    add("collision", lambda x: x["collision_boundary"].pop("C324"))
    add("nonclaim-rate", lambda x: x["nonclaims"].__setitem__(0, "unconditional universal rate"))
    add("reference", lambda x: x["references"][0].__setitem__("doi", "wrong"))
    add("reference-arxiv", lambda x: x["references"][1].__setitem__("arxiv", "wrong"))
    add("scope-flag", lambda x: x["scope_flags"].__setitem__("claims_root_number", True))
    add("scope-int", lambda x: x["scope_flags"].__setitem__("claims_target_euler_factors", 0))
    add("tuple", lambda x: x["route_a"]["tuple"].__setitem__(0, "A0_PASS"))
    add("overall", lambda x: x["route_a"].__setitem__("overall", "ROUTE_A_ACCEPTED"))
    add("route-b", lambda x: x["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("route-b-int", lambda x: x["route_a"].__setitem__("route_b_invocation_allowed", 0))
    add("status", lambda x: x["route_a"].__setitem__("theorem_status", "UNCONDITIONAL_PROFILE"))
    add("role", lambda x: x.__setitem__("finite_evidence_role", "proof by sampling"))
    add("extra", lambda x: x.__setitem__("unexpected", 1))
    add("missing", lambda x: x.pop("conventions"))
    add("multiplier-sign", lambda x: x["multiplier_rows"][255]["multiplier"]["im"].__setitem__("numerator", 1))
    add("multiplier-square", lambda x: x["multiplier_rows"][0].__setitem__("square_on_nonzero_mode", 1))
    add("tricomi-residual", lambda x: x["tricomi_rows"][0].__setitem__("residual_nonzero_count", 1))
    add("tricomi-hash", lambda x: x["tricomi_rows"][-1].__setitem__("identity_coefficient_sha256", "0" * 64))
    add("zero-denominator", lambda x: x["zero_mean_rows"][0]["denominator_abs_squared"].__setitem__("numerator", 0))
    add("zero-omega", lambda x: x["zero_mean_rows"][-1]["omega_formula"].__setitem__("numerator", 0))
    add("nonzero-mu", lambda x: x["nonzero_mean_rows"][0]["mu"].__setitem__("numerator", 0))
    add("nonzero-delta", lambda x: x["nonzero_mean_rows"][100]["delta"]["re"].__setitem__("numerator", 99))
    add("nonzero-singular", lambda x: x["nonzero_mean_rows"][1000].__setitem__("singular", not x["nonzero_mean_rows"][1000]["singular"]))
    add("one-mode-regime", lambda x: x["one_mode_rows"][0].__setitem__("regime", "wrong"))
    add("one-mode-zero", lambda x: x["one_mode_rows"][-1].__setitem__("zero_exists", not x["one_mode_rows"][-1]["zero_exists"]))
    add("one-mode-branch", lambda x: next(r for r in x["one_mode_rows"] if r["first_forward_time"] and r["first_forward_time"].get("arccot_branch"))["first_forward_time"].__setitem__("arccot_branch", "(-pi,0)"))
    add("control-status", lambda x: x["arithmetic_control_rows"][0].__setitem__("status", "OBSERVED"))
    add("control-primes", lambda x: x["arithmetic_control_rows"][0]["prime_modes"].append(4))
    add("control-common-hash", lambda x: x["arithmetic_control_rows"][0].__setitem__("common_stripped_clock_sha256", "0" * 64))
    add("control-permutation", lambda x: x["arithmetic_control_rows"][1]["mapping"][0].__setitem__(1, 16))
    add("control-preservation", lambda x: x["arithmetic_control_rows"][1].__setitem__("all_stripped_clock_hashes_preserved", False))
    add("control-regime-count", lambda x: x["arithmetic_control_rows"][2]["regime_counts"].__setitem__("tangent_zero", 0))
    add("control-threshold", lambda x: x["arithmetic_control_rows"][2].__setitem__("only_threshold", "mode_is_prime"))
    add("control-parent-hash", lambda x: x["arithmetic_control_rows"][3].__setitem__("section_sha256", "0" * 64))
    add("control-parent-label", lambda x: x["arithmetic_control_rows"][3].__setitem__("arithmetic_labels_used", True))
    add("profile-mu", lambda x: x["nonzero_profile_rows"][0]["mu"].__setitem__("numerator", 0))
    add("profile-transverse", lambda x: x["nonzero_profile_rows"][-1].__setitem__("transverse", False))
    add("profile-value", lambda x: x["zero_profile_rows"][0]["profile"].__setitem__("numerator", 0))
    add("profile-time", lambda x: x["zero_profile_rows"][-1]["blowup_time"].__setitem__("numerator", 0))
    add("boundary", lambda x: x["boundary_rows"][2].__setitem__("case", "simple"))

    killed = 0
    for label, blob in cases:
        assert run(evidence_blob=blob) != 0, label
        killed += 1
    stale = copy.deepcopy(base)
    stale["tricomi_rows"][0]["residual_nonzero_count"] = 1
    assert run(evidence_blob=json.dumps(stale, sort_keys=True, indent=2).encode() + b"\n") != 0
    killed += 1
    raw = EVIDENCE.read_bytes()
    duplicate = raw.replace(
        b'{\n  "arithmetic_control_rows"',
        b'{\n  "schema": "evil",\n  "arithmetic_control_rows"', 1,
    )
    nonfinite = raw.replace(b'"fixed_epoch": 1788480000', b'"fixed_epoch": NaN', 1)
    for label, blob in (("duplicate", duplicate), ("nonfinite", nonfinite)):
        assert run(evidence_blob=blob) != 0, label
        killed += 1
    y = EVALUATION.read_text()
    yaml_attacks = (
        ("duplicate-key", y + "candidate_id: HCS-C377\n"),
        ("anchor-merge", "base: &b {x: 1}\nmerged: {<<: *b}\n" + y),
        ("non-string-key", "1: bad\n" + y),
        ("unknown-field", y + "unknown_field: true\n"),
        ("date-type", y.replace("evaluation_date: '2026-09-04'", "evaluation_date: 2026-09-04")),
        ("skill-version", y.replace("skill_version: 0.2.0", "skill_version: 9.9.9")),
        ("code-commit", y.replace("code_commit: f58422d8f03235329863f946654981ecb5d4dc97", "code_commit: 0000000000000000000000000000000000000000")),
        ("source-lock", y.replace("  clock: physical PDE time in omega_t=omega*Homega", "  clock: fitted logarithmic clock", 1)),
        ("a0-control-status", y.replace("      status: EXECUTED_EXACT", "      status: NUMERICAL_OBSERVATION", 1)),
        ("a0-control-artifact", y.replace("      artifact: results/c377_periodic_clm_evidence.json#arithmetic_control_rows", "      artifact: missing.json", 1)),
        ("a1-metric", y.replace("    isolated_primitive_orbit_count: 0", "    isolated_primitive_orbit_count: 1")),
        ("a2-metric", y.replace("    zero_error_train: not applicable because no determinant is defined", "    zero_error_train: 0")),
        ("a3-structure", y.replace("    functional_equation: absent", "    functional_equation: claimed")),
        ("a4-metric", y.replace("    same_clock_quantum_lift: absent", "    same_clock_quantum_lift: present")),
        ("adversarial", y.replace("  verdict: PASS_DOES_NOT_CERTIFY_TARGET", "  verdict: CERTIFIES_TARGET")),
        ("claim-boundary", y.replace("  - no claim after the first pole, for three-dimensional Euler, for target arithmetic, or for global literature novelty", "  - claims three-dimensional Euler regularity")),
        ("blocking", y.replace("  - no intrinsic rational-prime carrier or prime-power repetition law", "  - none")),
        ("next-test", y.replace("next_smallest_test: no within-model target fit is authorized; any renewed Route-A attempt must first exhibit an independently sourced arithmetic carrier before computing target data", "next_smallest_test: fit target zeros")),
        ("round2-clue", y.replace("  - tangent zeros require a separate degenerate scaling analysis and must not inherit the simple-pole rate", "  - claim the simple-pole rate at tangent zeros")),
        ("route-b", y.replace("route_b_invocation_allowed: false", "route_b_invocation_allowed: true")),
        ("tuple", y.replace("  - A4_FAIL", "  - A4_PASS")),
        ("evidence-status", y.replace("evidence_status: STOP_SCOPED", "evidence_status: PROVED", 1)),
    )
    for label, blob in yaml_attacks:
        assert blob != y, label
        assert run(yaml_blob=blob.encode()) != 0, "yaml-" + label
        killed += 1
    paper = PAPER.read_text()
    paper_attacks = (
        ("r0-title-leak", paper.replace(
            "Exact Arbitrary-Mean Riccati Flow}",
            "Exact Arbitrary-Mean Flow, First-Pole Clock, and Transverse Profiles}", 1,
        )),
        ("r1-title-leak", paper.replace(
            "Exact Arbitrary-Mean Flow and Complete First-Pole Clock}",
            "Exact Arbitrary-Mean Flow, First-Pole Clock, and Transverse Profiles}", 1,
        )),
        ("round-title-gate", paper.replace("\\ifcase\\CRevisionRound", "\\ifnum\\CRevisionRound>9", 1)),
    )
    for label, blob in paper_attacks:
        assert blob != paper, label
        assert run(paper_blob=blob.encode()) != 0, "paper-" + label
        killed += 1
    expected = len(cases) + 3 + len(yaml_attacks) + len(paper_attacks)
    print(f"C377 mutation PASS: killed={killed}/{expected} repaired_hash_attacks={len(cases)}")


if __name__ == "__main__":
    main()
