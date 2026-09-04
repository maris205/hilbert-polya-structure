#!/usr/bin/env python3
"""Repaired-hash hostile mutation suite for HCS-C373."""
from __future__ import annotations

if not __debug__:
    raise RuntimeError("c373 mutation suite refuses optimized Python")

import argparse
import copy
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "code/c373_higgs_oscillator_checker.py"
EVIDENCE = ROOT / "results/c373_higgs_oscillator_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C373/2026-09-04.yaml"
RELEASE = ROOT / "code/c373_release_manifest.py"
SECTIONS = (
    "classical_rows", "quantum_state_rows", "quantum_level_rows",
    "rational_revival_rows", "irrational_revival_rows", "boundary_rows",
)


def canonical(value) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def repair(value):
    for section in SECTIONS:
        value["section_sha256"][section] = hashlib.sha256(canonical(value[section])).hexdigest()
    value.pop("payload_sha256", None)
    value["payload_sha256"] = hashlib.sha256(canonical(value)).hexdigest()
    return value


def encode(value):
    return json.dumps(repair(value), sort_keys=True, indent=2, ensure_ascii=False).encode() + b"\n"


def run(evidence_blob=None, yaml_blob=None):
    with tempfile.TemporaryDirectory(prefix="c373-mutation-") as directory:
        evidence_path = Path(directory) / "evidence.json"
        yaml_path = Path(directory) / "evaluation.yaml"
        evidence_path.write_bytes(EVIDENCE.read_bytes() if evidence_blob is None else evidence_blob)
        yaml_path.write_bytes(EVALUATION.read_bytes() if yaml_blob is None else yaml_blob)
        return subprocess.run(
            [sys.executable, "-B", str(CHECKER), "--input", str(evidence_path), "--evaluation", str(yaml_path)],
            capture_output=True, text=True,
        ).returncode


def load_tex_spacing_gate():
    namespace = {
        "__name__": "c373_release_gate_for_mutation",
        "__file__": str(RELEASE),
    }
    exec(compile(RELEASE.read_bytes(), str(RELEASE), "exec"), namespace)
    return namespace["assert_tex_spacing_hygiene"]


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
    add("classical-domain", lambda x: x["conventions"].__setitem__("classical_domain", "omega>=0"))
    add("hamiltonian", lambda x: x["conventions"].__setitem__("hamiltonian", "wrong sign"))
    add("action-normalization", lambda x: x["conventions"].__setitem__("radial_action", "missing 2*pi"))
    add("J", lambda x: x["conventions"].__setitem__("J", "wrong"))
    add("quantum-domain", lambda x: x["conventions"].__setitem__("quantum_domain", "full sphere"))
    add("nu", lambda x: x["conventions"].__setitem__("nu", "omega*R^2/hbar"))
    add("tau", lambda x: x["conventions"].__setitem__("revival_tau", "wrong"))
    add("identity-phase", lambda x: x["conventions"].__setitem__("identity_revival", "up to phase"))
    add("turning-contract", lambda x: x["theorem_contract"].__setitem__("turning_polynomial", "wrong"))
    add("action-contract", lambda x: x["theorem_contract"].__setitem__("action", "wrong"))
    add("frequency-contract", lambda x: x["theorem_contract"].__setitem__("frequencies", "one-to-one"))
    add("face-contract", lambda x: x["theorem_contract"].__setitem__("faces", "omega zero periodic"))
    add("quantum-contract", lambda x: x["theorem_contract"].__setitem__("quantum", "full sphere"))
    add("limit-contract", lambda x: x["theorem_contract"].__setitem__("limits", "full sphere limit"))
    add("revival-contract", lambda x: x["theorem_contract"].__setitem__("revival", "up to global phase"))
    add("collision", lambda x: x["collision_boundary"].__setitem__("C349", "same"))
    add("nonclaim-classical", lambda x: x["nonclaims"].__setitem__(0, "omega zero periodic"))
    add("nonclaim-sphere", lambda x: x["nonclaims"].__setitem__(1, "full sphere multiplicity"))
    add("reference", lambda x: x["references"][0].__setitem__("doi", "wrong"))
    add("scope-flag", lambda x: x["scope_flags"].__setitem__("claims_target_euler_factors", True))
    add("scope-bool-int", lambda x: x["scope_flags"].__setitem__("claims_root_number", 0))
    add("tuple", lambda x: x["route_a"]["tuple"].__setitem__(0, "A0_PASS"))
    add("overall", lambda x: x["route_a"].__setitem__("overall", "ROUTE_A_ACCEPTED"))
    add("route-b", lambda x: x["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("route-b-bool-int", lambda x: x["route_a"].__setitem__("route_b_invocation_allowed", 0))
    add("theorem-status", lambda x: x["route_a"].__setitem__("theorem_status", "OPEN"))
    add("evidence-role", lambda x: x.__setitem__("finite_evidence_role", "proof by sampling"))
    add("extra-top", lambda x: x.__setitem__("unexpected", 1))
    add("missing-top", lambda x: x.pop("conventions"))
    add("grid-classical", lambda x: x["finite_grid"].__setitem__("classical_cell_count", 2047))
    add("grid-states", lambda x: x["finite_grid"].__setitem__("quantum_state_label_count", 8384))
    add("grid-revivals", lambda x: x["finite_grid"].__setitem__("total_revival_case_count", 511))
    add("classical-energy", lambda x: x["classical_rows"][0].__setitem__("energy", {"numerator": 0, "denominator": 1}))
    add("classical-action", lambda x: x["classical_rows"][0].__setitem__("action_recovered", {"numerator": 0, "denominator": 1}))
    add("classical-discriminant", lambda x: x["classical_rows"][0]["turning_polynomial"].__setitem__("discriminant", {"numerator": 0, "denominator": 1}))
    add("classical-frequency", lambda x: x["classical_rows"][0].__setitem__("omega_r", x["classical_rows"][0]["omega_phi"]))
    add("quantum-label", lambda x: x["quantum_state_rows"][10].__setitem__("n_r", 99))
    add("quantum-energy", lambda x: x["quantum_state_rows"][10]["energy_scaled_2R2_over_hbar2"].__setitem__("nu_coefficient", 0))
    add("level-multiplicity", lambda x: x["quantum_level_rows"][128].__setitem__("multiplicity", 128))
    add("dirichlet-l", lambda x: x["quantum_level_rows"][0].__setitem__("omega_zero_dirichlet_l", 0))
    add("rational-M", lambda x: x["rational_revival_rows"][0].__setitem__("minimum_M", 2))
    add("global-phase", lambda x: x["rational_revival_rows"][0].__setitem__("global_k1_exponent", 1))
    add("irrational-square", lambda x: x["irrational_revival_rows"][0].__setitem__("radicand", 4))
    add("irrational-revival", lambda x: x["irrational_revival_rows"][0].__setitem__("identity_revival_exists", True))
    add("boundary-zero", lambda x: x["boundary_rows"][4].__setitem__("phase_period", "periodic"))
    add("boundary-quantum", lambda x: x["boundary_rows"][5].__setitem__("phase_period", "full sphere"))

    killed = 0
    for label, blob in cases:
        assert run(evidence_blob=blob) != 0, label
        killed += 1

    stale = copy.deepcopy(base)
    stale["classical_rows"][0]["energy"] = {"numerator": 0, "denominator": 1}
    assert run(evidence_blob=json.dumps(stale, sort_keys=True, indent=2).encode() + b"\n") != 0
    killed += 1

    raw = EVIDENCE.read_bytes()
    duplicate = raw.replace(b'{\n  "boundary_rows"', b'{\n  "schema": "evil",\n  "boundary_rows"', 1)
    nonfinite = raw.replace(b'"fixed_epoch": 1788480000', b'"fixed_epoch": NaN', 1)
    for label, blob in (("duplicate-json", duplicate), ("nonfinite-json", nonfinite)):
        assert run(evidence_blob=blob) != 0, label
        killed += 1

    yaml_text = EVALUATION.read_text()
    yaml_attacks = [
        ("yaml-duplicate", yaml_text + "candidate_id: HCS-C373\n"),
        ("yaml-merge", "base: &b {x: 1}\nmerged: {<<: *b}\n" + yaml_text),
        ("yaml-nonstring", "1: bad\n" + yaml_text),
        ("yaml-alias", "anchor: &a bad\nalias: *a\n" + yaml_text),
        ("yaml-date", yaml_text.replace("evaluation_date: '2026-09-04'", "evaluation_date: 2026-09-04")),
        ("yaml-unknown", yaml_text + "unknown_field: true\n"),
        ("yaml-type", yaml_text.replace("fixed_epoch: 1788480000", "fixed_epoch: '1788480000'")),
        ("yaml-classical-domain", yaml_text.replace("classically R and omega are strictly positive", "classically omega is nonnegative")),
        ("yaml-status", yaml_text.replace("evidence_status: STOP_SCOPED", "evidence_status: PROVED", 1)),
        ("yaml-artifact", yaml_text.replace("paper/main.pdf", "paper/wrong.pdf")),
        ("yaml-tuple", yaml_text.replace("  - A4_NATURAL_QUANTIZATION", "  - A4_FAIL")),
        ("yaml-route-b", yaml_text.replace("route_b_invocation_allowed: false", "route_b_invocation_allowed: true")),
    ]
    for label, text in yaml_attacks:
        assert run(yaml_blob=text.encode()) != 0, label
        killed += 1

    spacing_gate = load_tex_spacing_gate()
    clean_tex = (ROOT / "paper/main.tex").read_text()
    spacing_gate(clean_tex, "clean-main.tex")
    tex_spacing_attacks = (
        ("tex-unescaped-quad", clean_tex.replace(r"\qquad", "quad", 1)),
        ("tex-unescaped-qquad", clean_tex.replace(r"\qquad", "qquad", 1)),
    )
    for label, text in tex_spacing_attacks:
        try:
            spacing_gate(text, label)
        except AssertionError:
            killed += 1
        else:
            raise AssertionError(label)
    legal_spacing_controls = (
        r"$a\quad b$", r"$a\qquad b$", r"quadratic form", r"quadric surface",
    )
    for index, text in enumerate(legal_spacing_controls):
        spacing_gate(text, f"legal-spacing-control-{index}")

    expected = len(cases) + 3 + len(yaml_attacks) + len(tex_spacing_attacks)
    print(
        f"C373 mutation PASS: killed={killed}/{expected} "
        f"repaired_hash_attacks={len(cases)} stale_hash_control=1 "
        f"tex_spacing_attacks={len(tex_spacing_attacks)} "
        f"legal_spacing_controls={len(legal_spacing_controls)}"
    )


if __name__ == "__main__":
    main()
