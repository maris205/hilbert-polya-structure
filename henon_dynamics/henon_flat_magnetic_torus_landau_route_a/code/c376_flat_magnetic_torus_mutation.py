#!/usr/bin/env python3
"""Repaired-hash hostile mutation suite for HCS-C376."""
from __future__ import annotations

if not __debug__:
    raise RuntimeError("c376 mutation suite refuses optimized Python")

import argparse
import copy
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "code/c376_flat_magnetic_torus_checker.py"
EVIDENCE = ROOT / "results/c376_flat_magnetic_torus_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C376/2026-09-04.yaml"
TEX = ROOT / "paper/main.tex"
SECTIONS = (
    "classical_rows", "flux_rows", "landau_rows", "translation_rows", "heat_rows",
    "determinant_rows", "revival_rows", "boundary_rows",
)


def canonical(value) -> bytes:
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


def run(evidence_blob=None, yaml_blob=None):
    with tempfile.TemporaryDirectory(prefix="c376-mutation-") as directory:
        evidence_path = Path(directory) / "evidence.json"
        yaml_path = Path(directory) / "evaluation.yaml"
        evidence_path.write_bytes(EVIDENCE.read_bytes() if evidence_blob is None else evidence_blob)
        yaml_path.write_bytes(EVALUATION.read_bytes() if yaml_blob is None else yaml_blob)
        return subprocess.run(
            [sys.executable, "-B", str(CHECKER), "--input", str(evidence_path), "--evaluation", str(yaml_path)],
            capture_output=True, text=True,
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

    add("schema", lambda x: x.__setitem__("schema", "wrong"))
    add("candidate", lambda x: x.__setitem__("candidate_id", "HCS-C000"))
    add("obstruction", lambda x: x.__setitem__("obstruction_id", "HEN-O000"))
    add("date", lambda x: x.__setitem__("evaluation_date", "2026-09-03"))
    add("source", lambda x: x.__setitem__("source_commit", "0" * 8))
    add("epoch", lambda x: x.__setitem__("fixed_epoch", 0))
    add("scope", lambda x: x.__setitem__("scope_literal", "BROKEN"))
    add("authority", lambda x: x["evaluator"].__setitem__("authority", "wrong"))
    add("authority-version", lambda x: x["evaluator"].__setitem__("version", "9"))
    add("authority-sha", lambda x: x["evaluator"].__setitem__("sha256", "0" * 64))
    add("yaml-path", lambda x: x["route_a_yaml"].__setitem__("relative_path", "wrong"))
    add("yaml-raw", lambda x: x["route_a_yaml"].__setitem__("raw_sha256", "0" * 64))
    add("yaml-semantic", lambda x: x["route_a_yaml"].__setitem__("semantic_sha256", "0" * 64))
    add("torus", lambda x: x["conventions"].__setitem__("torus", "cylinder"))
    add("symplectic-sign", lambda x: x["conventions"].__setitem__("classical_symplectic", "wrong sign"))
    add("hamiltonian", lambda x: x["conventions"].__setitem__("classical_hamiltonian", "wrong"))
    add("rotation", lambda x: x["conventions"].__setitem__("rotation", "wrong"))
    add("curvature", lambda x: x["conventions"].__setitem__("quantum_curvature", "wrong"))
    add("commutator", lambda x: x["conventions"].__setitem__("kinetic_commutator", "-iB"))
    add("bochner", lambda x: x["conventions"].__setitem__("quantum_hamiltonian", "Dolbeault only"))
    add("det-convention", lambda x: x["conventions"].__setitem__("zeta_determinant", "ordinary product"))
    for key in ("classical", "integrality", "spectrum", "translations", "heat", "zeta", "determinant", "revival", "boundaries"):
        add("contract-" + key, lambda x, key=key: x["theorem_contract"].__setitem__(key, "wrong"))
    add("grid-classical", lambda x: x["finite_grid"].__setitem__("classical_quarter_return_cell_count", 255))
    add("grid-landau", lambda x: x["finite_grid"].__setitem__("landau_label_cell_count", 16511))
    add("grid-translation", lambda x: x["finite_grid"].__setitem__("translation_basis_cell_count", 2079))
    add("collision", lambda x: x["collision_boundary"].pop("C331"))
    add("nonclaim", lambda x: x["nonclaims"].__setitem__(4, "Hilbert-Polya claimed"))
    add("reference-doi", lambda x: x["references"][0].__setitem__("doi", "wrong"))
    add("reference-arxiv", lambda x: x["references"][1].__setitem__("arxiv", "wrong"))
    add("reference-onofri-doi", lambda x: x["references"][1].__setitem__("doi", "wrong"))
    add("scope-flag", lambda x: x["scope_flags"].__setitem__("claims_root_number", True))
    add("scope-bool-int", lambda x: x["scope_flags"].__setitem__("claims_target_euler_factors", 0))
    add("tuple", lambda x: x["route_a"]["tuple"].__setitem__(0, "A0_PASS"))
    add("overall", lambda x: x["route_a"].__setitem__("overall", "ROUTE_A_ACCEPTED"))
    add("route-b", lambda x: x["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("route-b-int", lambda x: x["route_a"].__setitem__("route_b_invocation_allowed", 0))
    add("status", lambda x: x["route_a"].__setitem__("theorem_status", "OPEN"))
    add("evidence-role", lambda x: x.__setitem__("finite_evidence_role", "proof by sampling"))
    add("extra-top", lambda x: x.__setitem__("unexpected", 1))
    add("missing-top", lambda x: x.pop("conventions"))
    add("classical-B", lambda x: x["classical_rows"][0].__setitem__("abs_B", {"numerator": 2, "denominator": 1}))
    add("classical-energy", lambda x: x["classical_rows"][0].__setitem__("energy", {"numerator": 0, "denominator": 1}))
    add("classical-center", lambda x: x["classical_rows"][0]["center"].__setitem__(0, {"numerator": 9, "denominator": 1}))
    add("classical-quarter", lambda x: x["classical_rows"][0]["quarter_states"][1].__setitem__("quarter", 9))
    add("flux-chern", lambda x: x["flux_rows"][0].__setitem__("chern_integral", 0))
    add("flux-multiplicity", lambda x: x["flux_rows"][-1].__setitem__("landau_multiplicity", 63))
    add("landau-level", lambda x: x["landau_rows"][129].__setitem__("level", 7))
    add("landau-energy", lambda x: x["landau_rows"][1000].__setitem__("energy_over_abs_B", {"numerator": 0, "denominator": 1}))
    add("translation-U", lambda x: x["translation_rows"][100].__setitem__("U_image_index", 99))
    add("translation-phase", lambda x: x["translation_rows"][1000].__setitem__("UV_over_VU_phase_exponent_mod_order", 0))
    add("translation-negative-sign", lambda x: x["translation_rows"][1000].__setitem__("flux_sign", 1))
    add("translation-negative-clock", lambda x: x["translation_rows"][1000].__setitem__("V_phase_exponent_mod_order", 0))
    add("translation-positive-sign", lambda x: x["translation_rows"][3080].__setitem__("flux_sign", -1))
    add("translation-positive-phase", lambda x: x["translation_rows"][3080].__setitem__("UV_over_VU_phase_exponent_mod_order", 0))
    add("translation-vectors", lambda x: x["translation_rows"][2000]["ordered_positive_division_vectors"].__setitem__(1, "(0,-Ly/M)"))
    add("heat-q", lambda x: x["heat_rows"][0].__setitem__("q", {"numerator": 2, "denominator": 1}))
    add("heat-trace", lambda x: x["heat_rows"][-1].__setitem__("trace_divided_by_sqrt_q", {"numerator": 0, "denominator": 1}))
    add("det-zeta0", lambda x: x["determinant_rows"][0].__setitem__("zeta_at_zero", 1))
    add("det-exponent", lambda x: x["determinant_rows"][-1].__setitem__("determinant_exponent", {"numerator": 1, "denominator": 1}))
    add("revival-scalar", lambda x: x["revival_rows"][0].__setitem__("phase_at_classical_period", "+1"))
    add("revival-identity", lambda x: x["revival_rows"][-1].__setitem__("phase_at_double_period", "-1"))
    add("boundary", lambda x: x["boundary_rows"][-1].__setitem__("case", "not_B_zero"))
    add("boundary-closure", lambda x: x["boundary_rows"][-1].__setitem__("closure_criterion", "raw slope rational"))
    add("boundary-nonaxial", lambda x: x["boundary_rows"][-1].__setitem__("nonaxial_criterion", "p_y/p_x is rational"))
    add("boundary-x-axis", lambda x: x["boundary_rows"][-1].__setitem__("x_axis_nonzero", "dense"))
    add("boundary-y-axis", lambda x: x["boundary_rows"][-1].__setitem__("y_axis_nonzero", "dense"))
    add("boundary-zero", lambda x: x["boundary_rows"][-1].__setitem__("zero_velocity", "positive least period"))

    killed = 0
    for label, blob in cases:
        assert run(evidence_blob=blob) != 0, label
        killed += 1

    stale = copy.deepcopy(base)
    stale["landau_rows"][0]["level"] = 99
    assert run(evidence_blob=json.dumps(stale, sort_keys=True, indent=2).encode() + b"\n") != 0
    killed += 1
    raw = EVIDENCE.read_bytes()
    duplicate = raw.replace(b'{\n  "boundary_rows"', b'{\n  "schema": "evil",\n  "boundary_rows"', 1)
    nonfinite = raw.replace(b'"fixed_epoch": 1788480000', b'"fixed_epoch": NaN', 1)
    for label, blob in (("duplicate-json", duplicate), ("nonfinite-json", nonfinite)):
        assert run(evidence_blob=blob) != 0, label
        killed += 1

    yaml_text = EVALUATION.read_text()
    yaml_attacks = (
        yaml_text + "candidate_id: HCS-C376\n",
        "base: &b {x: 1}\nmerged: {<<: *b}\n" + yaml_text,
        "1: bad\n" + yaml_text,
        yaml_text + "unknown_field: true\n",
        yaml_text.replace("evaluation_date: '2026-09-04'", "evaluation_date: 2026-09-04"),
        yaml_text.replace("route_b_invocation_allowed: false", "route_b_invocation_allowed: true"),
        yaml_text.replace("skill: route-a-evaluator", "skill: wrong-evaluator"),
        yaml_text.replace("skill_version: 0.2.0", "skill_version: 9.9.9"),
        yaml_text.replace("code_commit: " + "f58422d8f03235329863f946654981ecb5d4dc97", "code_commit: " + "0" * 40),
        yaml_text.replace("    - prime and composite values of abs(N) obey the same formulas, with no prime-specific term\n", ""),
        yaml_text.replace("  metrics:\n    target_tables_used: 0", "  metrics:\n    target_tables_used: 1", 1),
        yaml_text.replace("claim_boundary: exact source-local", "claim_boundary: overclaimed global"),
        yaml_text.replace("round2_clues:\n", "round2_clues: []\n# ", 1),
        yaml_text.replace("  - A0_FAIL", "  - A0_WEAK_ARITHMETIC_RELATION"),
        yaml_text.replace("  - A2_FAIL", "  - A2_PASS"),
        yaml_text.replace("evidence_status: STOP_SCOPED", "evidence_status: PROVED"),
    )
    for index, attack in enumerate(yaml_attacks):
        assert run(yaml_blob=attack.encode()) != 0, f"yaml-{index}"
        killed += 1
    spacing_pattern = re.compile(r"(?<!\\)\b(?:quad|qquad)\b")
    clean_tex = TEX.read_text()
    assert spacing_pattern.search(clean_tex) is None
    assert spacing_pattern.search("x,quad y") is not None
    assert spacing_pattern.search("x,qquad y") is not None
    killed += 2
    expected = len(cases) + 3 + len(yaml_attacks) + 2
    print(f"C376 mutation PASS: killed={killed}/{expected} repaired_hash_attacks={len(cases)}")


if __name__ == "__main__":
    main()
