#!/usr/bin/env python3
"""Repaired-hash semantic, parser, and YAML attacks for HCS-C317."""
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
EVIDENCE = ROOT / "results/c317_newton_schulz_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C317/2026-09-03.yaml"
CHECKER = ROOT / "code/c317_newton_schulz_checker.py"


def payload(data):
    body = dict(data); body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def set_path(data, path, value):
    cursor = data
    for key in path[:-1]:
        cursor = cursor[key]
    cursor[path[-1]] = value


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C317 mutation suite refuses optimized Python")
    pristine = json.loads(EVIDENCE.read_text()); raw = EVIDENCE.read_text(); yraw = EVALUATION.read_text()
    mutations = [
        (("candidate_id",), "HCS-C000"), (("obstruction_id",), "HEN-O000"),
        (("source_commit",), "0" * 40), (("scope_literal",), "EXPANDED"),
        (("model", "dynamics"), "linear"),
        (("theorem_contract", "pseudoinverse_basin"), "spectral radius only"),
        (("route_a", "tuple", 0), "A0_PASS"), (("route_a", "overall"), "ROUTE_A_ACCEPTED"),
        (("scope_flags", "claims_root_number"), True),
        (("square_cases", 0, "regime"), "convergent"),
        (("square_cases", 3, "initial_residual", 0, 0), "99"),
        (("square_cases", 6, "regime"), "bounded-nonconvergent"),
        (("square_cases", 9, "jordan_binomial_rows", 0, "coefficients", 0), "7"),
        (("square_cases", 10, "spectral_radius"), "1/2"),
        (("compatible_rectangular_cases", 0, "compatibility_left", 0, 0), "1"),
        (("compatible_rectangular_cases", 2, "snapshots", 3, "compressed_residual", 0, 0), "8"),
        (("incompatible_rectangular_cases", 0, "converges_to_moore_penrose"), True),
        (("incompatible_rectangular_cases", 4, "off_support_kind"), "C"),
        (("canonical_alpha_cases", 0, "classification"), "converges-pseudoinverse"),
        (("canonical_alpha_cases", 1, "alpha"), "1/7"),
        (("canonical_alpha_cases", 3, "directions", 1, "predicted_limit"), "1/2"),
        (("canonical_alpha_cases", 5, "directions", 0, "iterate_coefficients", 2), "0"),
        (("enumeration", "canonical_alpha_case_count"), 18),
        (("enumeration", "audited_leaf_count"), 1),
        (("collision_boundary", "C257"), "same theorem"),
        (("references", 0, "identifier"), "unknown"),
    ]
    attacks = []
    for path, value in mutations:
        changed = copy.deepcopy(pristine); set_path(changed, path, value)
        changed["payload_sha256"] = payload(changed)
        attacks.append(("semantic", json.dumps(changed, sort_keys=True, indent=2) + "\n", yraw))
    attacks.extend([
        ("stale-hash", raw.replace('"candidate_id": "HCS-C317"', '"candidate_id": "HCS-C000"', 1), yraw),
        ("duplicate-json", raw.replace("{\n", '{\n  "schema": "duplicate",\n', 1), yraw),
        ("nonfinite-json", raw.replace('"fixed_epoch": 1788393600', '"fixed_epoch": Infinity', 1), yraw),
        ("json-array", "[]\n", yraw),
        ("yaml-duplicate", raw, yraw + "candidate_id: HCS-C317\n"),
        ("yaml-anchor", raw, yraw.replace("candidate_id: HCS-C317", "candidate_id: &bad HCS-C317", 1)),
        ("yaml-alias", raw, yraw + "probe: *bad\n"),
        ("yaml-array", raw, "- bad\n"),
        ("yaml-tuple", raw, yraw.replace("  - A2_FAIL", "  - A2_PASS", 1)),
        ("yaml-routeb", raw, yraw.replace("route_b_invocation_allowed: false", "route_b_invocation_allowed: true", 1)),
        ("yaml-scope", raw, yraw.replace("  claims_automorphy: false", "  claims_automorphy: true", 1)),
        ("yaml-epoch-type", raw, yraw.replace("fixed_epoch: 1788393600", 'fixed_epoch: "1788393600"', 1)),
        ("yaml-family-semantic", raw, yraw.replace(
            'family: "nonlinear discrete matrix iterations"',
            'family: "repaired but unauthorized family"', 1)),
        ("yaml-finite-role-semantic", raw, yraw.replace(
            'finite_evidence_role: "regression evidence only; the arbitrary-dimensional basin and rate statements are analytic"',
            'finite_evidence_role: "finite matrices prove the arbitrary-dimensional theorem"', 1)),
    ])
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC"); rejected = 0
    with tempfile.TemporaryDirectory(prefix="c317-mutation-") as tmp:
        for index, (name, text, ytext) in enumerate(attacks):
            path = Path(tmp) / f"{index}.json"; ypath = Path(tmp) / f"{index}.yaml"
            path.write_text(text); ypath.write_text(ytext)
            run = subprocess.run([sys.executable, "-B", str(CHECKER), "--evidence", str(path),
                                  "--evaluation", str(ypath)], env=env,
                                 stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            if run.returncode == 0:
                raise AssertionError(f"mutation survived {name}-{index}")
            rejected += 1
        optimized = subprocess.run([sys.executable, "-O", str(CHECKER)], env=env,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        if optimized.returncode == 0:
            raise AssertionError("optimized checker survived")
    print(f"C317 hostile mutation suite: PASS {rejected}/{len(attacks)} plus optimized-Python rejection")


if __name__ == "__main__":
    main()
