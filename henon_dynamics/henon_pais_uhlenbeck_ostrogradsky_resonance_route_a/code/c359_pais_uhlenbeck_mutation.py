#!/usr/bin/env python3
"""Repaired-hash hostile mutation suite for HCS-C359."""
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
CHECKER = ROOT / "code/c359_pais_uhlenbeck_checker.py"
EVIDENCE = ROOT / "results/c359_pais_uhlenbeck_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C359/2026-09-04.yaml"


def repair(data):
    value = copy.deepcopy(data); value.pop("payload_sha256", None)
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    value["payload_sha256"] = hashlib.sha256(raw).hexdigest()
    return json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False).encode() + b"\n"


def rejected(evidence, evaluation):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    with tempfile.TemporaryDirectory(prefix="c359-mutation-") as directory:
        epath, ypath = Path(directory)/"e.json", Path(directory)/"y.yaml"
        epath.write_bytes(evidence); ypath.write_bytes(evaluation)
        proc = subprocess.run([sys.executable, "-B", str(CHECKER), "--evidence", str(epath), "--evaluation", str(ypath)], env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return proc.returncode != 0


def main():
    if sys.flags.optimize:
        raise RuntimeError("C359 mutation suite refuses optimized Python")
    base_raw, eval_raw = EVIDENCE.read_bytes(), EVALUATION.read_bytes()
    base = json.loads(base_raw)
    attacks = []
    def add(name, fn):
        value = copy.deepcopy(base); fn(value); attacks.append((name, repair(value), eval_raw))
    add("candidate", lambda x: x.__setitem__("candidate_id", "HCS-C000"))
    add("obstruction", lambda x: x.__setitem__("obstruction_id", "HEN-O000"))
    add("date", lambda x: x.__setitem__("evaluation_date", "2026-09-03"))
    add("source", lambda x: x.__setitem__("source_commit", "0"*40))
    add("epoch", lambda x: x.__setitem__("fixed_epoch", 0))
    add("scope", lambda x: x.__setitem__("scope_literal", "OTHER"))
    add("evaluator_authority", lambda x: x["evaluator"].__setitem__("authority", "elsewhere"))
    add("evaluator_version", lambda x: x["evaluator"].__setitem__("version", "0.1.0"))
    add("evaluator_sha", lambda x: x["evaluator"].__setitem__("sha256", "0"*64))
    add("evaluation_path", lambda x: x["evaluation_lock"].__setitem__("relative_path", "wrong"))
    add("evaluation_raw", lambda x: x["evaluation_lock"].__setitem__("raw_sha256", "0"*64))
    add("evaluation_semantic", lambda x: x["evaluation_lock"].__setitem__("semantic_sha256", "0"*64))
    add("model_sign", lambda x: x["model"].__setitem__("distinct_positive_normal_form", "both positive"))
    add("model_equation", lambda x: x["model"].__setitem__("equation", "second order"))
    add("model_quantum_domain", lambda x: x["model"].__setitem__("quantum_domain", "lambda*c in l2 only"))
    add("theorem_rational", lambda x: x["theorem_contract"].__setitem__("classical_resonance", "all ratios periodic"))
    add("theorem_quantum", lambda x: x["theorem_contract"].__setitem__("quantum", "semibounded compact resolvent"))
    add("equal_boundary", lambda x: x["boundary_atlas"].__setitem__("equal_positive", "diagonalizable"))
    add("zero_boundary", lambda x: x["boundary_atlas"].__setitem__("double_zero", "linear only"))
    add("reference", lambda x: x["references"][0].__setitem__("identifier", "fabricated"))
    add("collision", lambda x: x["collision_boundary"].__setitem__("C357", "same model"))
    add("nonclaim", lambda x: x["nonclaims"].__setitem__(3, "Hilbert--Polya"))
    add("route_tuple", lambda x: x["route_a"]["tuple"].__setitem__(0, "A0_PASS"))
    add("route_overall", lambda x: x["route_a"].__setitem__("overall", "PASS"))
    add("route_b", lambda x: x["route_a"].__setitem__("route_b", True))
    add("scope_flag", lambda x: x["scope_flags"].__setitem__("claims_hilbert_polya_operator", True))
    add("frequency_grid", lambda x: x["rational_frequency_grid"][0].__setitem__(1, 2))
    add("support_grid", lambda x: x["support_grid"][0].__setitem__(0, "1"))
    add("canonical_coordinate", lambda x: x["canonical_rows"][0].__setitem__("frequency_index", 7))
    add("canonical_extra", lambda x: x["canonical_rows"][0].__setitem__("extra", 1))
    add("canonical_noncanonical", lambda x: x["canonical_rows"][0].__setitem__("omega1", "2/2"))
    add("canonical_nan", lambda x: x["canonical_rows"][0].__setitem__("delta", "nan"))
    add("canonical_delta", lambda x: x["canonical_rows"][0].__setitem__("delta", "4"))
    add("canonical_sign", lambda x: x["canonical_rows"][0].__setitem__("mode1_energy_sign", 1))
    add("poisson", lambda x: x["canonical_rows"][0]["poisson_matrix"][0].__setitem__(1, "-1"))
    add("duplicate_canonical", lambda x: x["canonical_rows"].__setitem__(1, copy.deepcopy(x["canonical_rows"][0])))
    add("orbit_coordinate", lambda x: x["orbit_rows"][0].__setitem__("support_index", 8))
    add("orbit_periodic", lambda x: x["orbit_rows"][1].__setitem__("periodic", False))
    add("orbit_kind", lambda x: x["orbit_rows"][3].__setitem__("orbit_type", "single_mode"))
    add("orbit_phase", lambda x: x["orbit_rows"][3].__setitem__("phase2_turns", 99))
    add("duplicate_orbit", lambda x: x["orbit_rows"].__setitem__(1, copy.deepcopy(x["orbit_rows"][0])))
    add("omit_orbit", lambda x: x["orbit_rows"].pop())
    add("irrational_ratio", lambda x: x["irrational_rows"][0].__setitem__("ratio", "1/2"))
    add("irrational_closure", lambda x: x["irrational_rows"][0].__setitem__("double_mode_closure", True))
    add("irrational_spectrum", lambda x: x["irrational_rows"][0].__setitem__("quantum_eigenvalues", "discrete"))
    add("quantum_coordinate", lambda x: x["quantum_rows"][0].__setitem__("n2", 15))
    add("quantum_lattice", lambda x: x["quantum_rows"][0].__setitem__("lattice_coordinate", 9))
    add("quantum_energy", lambda x: x["quantum_rows"][0].__setitem__("energy", "9"))
    add("duplicate_quantum", lambda x: x["quantum_rows"].__setitem__(1, copy.deepcopy(x["quantum_rows"][0])))
    add("omit_quantum", lambda x: x["quantum_rows"].pop())
    add("boundary_basis", lambda x: x["boundary_rows"][0]["solution_basis"].__setitem__(2, "cos"))
    add("boundary_bounded_subspace", lambda x: x["boundary_rows"][2].__setitem__("bounded_entire_subspace", "all polynomials"))
    add("boundary_quantum", lambda x: x["boundary_rows"][0].__setitem__("quantum_claimed", True))
    add("enumeration", lambda x: x["enumeration"].__setitem__("quantum_rows", 1))
    add("leaf_count", lambda x: x["enumeration"].__setitem__("leaf_count_without_payload_hash", 1))
    add("top_extra", lambda x: x.__setitem__("unexpected", 1))
    attacks.append(("stale_hash", base_raw.replace(b'"mode1_energy_sign": -1', b'"mode1_energy_sign": 1', 1), eval_raw))
    attacks.append(("duplicate_json", base_raw.replace(b'{\n', b'{\n  "schema": "duplicate",\n', 1), eval_raw))
    attacks.append(("nonfinite_json", base_raw.replace(b'"fixed_epoch": 1788480000', b'"fixed_epoch": NaN', 1), eval_raw))
    for name, raw in [
        ("yaml_authority", eval_raw.replace(b"evaluator_authority: flow_systems/skills/route-a-evaluator.md", b"evaluator_authority: elsewhere")),
        ("yaml_status", eval_raw.replace(b"evidence_status: PROVED", b"evidence_status: STOP_SCOPED", 1)),
        ("yaml_path", eval_raw.replace(b"results/c359_pais_uhlenbeck_evidence.json", b"results/wrong.json")),
        ("yaml_alias", eval_raw+b"alias_attack: &x 1\nalias_use: *x\n"),
        ("yaml_duplicate", eval_raw+b"candidate_id: HCS-C359\n"),
        ("yaml_nonstring", eval_raw+b"7: bad\n"),
    ]:
        attacks.append((name, base_raw, raw))
    passed = 0
    for name, evidence, evaluation in attacks:
        if not rejected(evidence, evaluation):
            raise AssertionError(f"mutation survived: {name}")
        passed += 1
    print(f"C359 hostile mutation suite: PASS ({passed}/{len(attacks)} rejected)")


if __name__ == "__main__":
    main()
