#!/usr/bin/env python3
"""Hostile repaired-hash mutations for HCS-C275."""
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
EVIDENCE = ROOT / "results/c275_poncelet_evidence.json"
CHECKER = ROOT / "code/c275_poncelet_checker.py"


def payload_hash(data: dict) -> str:
    clone = dict(data)
    clone.pop("payload_sha256", None)
    raw = json.dumps(clone, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    mutations = [
        ("source", lambda d: d.__setitem__("source_commit", "0" * 40)),
        ("epoch", lambda d: d.__setitem__("fixed_epoch", d["fixed_epoch"] + 1)),
        ("scope", lambda d: d.__setitem__("scope_literal", "MUTATED_SCOPE")),
        ("evaluator", lambda d: d["evaluator"].__setitem__("sha256", "0" * 64)),
        ("route_tuple", lambda d: d["route_a"]["tuple"].__setitem__(1, "A1_FAIL")),
        ("route_a4_tuple", lambda d: d["route_a"]["tuple"].__setitem__(4, "A4_NATURAL_QUANTIZATION")),
        ("overall", lambda d: d["route_a"].__setitem__("overall", "ROUTE_A_EXPLORATORY")),
        ("route_b", lambda d: d["route_a"].__setitem__("route_b_invocation_allowed", True)),
        ("scope_flag", lambda d: d["scope_flags"].__setitem__("hilbert_polya_operator", True)),
        ("domain", lambda d: d["owner"].__setitem__("parameter_domain", "0<e<f<1")),
        ("formula", lambda d: d["regression"]["formula_cells"][0].__setitem__("rho", "0.49")),
        ("tangency", lambda d: d["regression"]["covering_cells"][0].__setitem__(
            "caustic_tangency_relative_residual", "0.01")),
        ("monotone_direction", lambda d: d["regression"]["monotonicity_in_f"][0].__setitem__(
            "direction", "increasing")),
        ("endpoint", lambda d: d["regression"]["endpoint_paths"][0].__setitem__(
            "limit", "1/2")),
        ("minimal_period", lambda d: d["regression"]["porism_cases"][0].__setitem__(
            "minimal_period", 4)),
        ("return_derivative", lambda d: d["regression"]["porism_cases"][0].__setitem__(
            "tangent_q_return_derivative", "2")),
        ("ambient", lambda d: d["regression"]["porism_cases"][0].__setitem__(
            "ambient_unipotent_conclusion", True)),
        ("isolated_product", lambda d: d["regression"]["porism_cases"][0].__setitem__(
            "isolated_orbit_product_applicable", True)),
        ("theorem", lambda d: d["theorem_contract"].__setitem__(
            "strict_monotonicity", "partial_e rho<0")),
        ("a4_classification", lambda d: d["a4_liftability"].__setitem__(
            "classification", "A4_NATURAL_QUANTIZATION")),
        ("a4_domain", lambda d: d["a4_liftability"]["ambient_quantum_owner"].__setitem__(
            "operator_domain", "H_0^1(Omega_f)")),
        ("a4_antiunitary", lambda d: d["a4_liftability"]["ambient_quantum_owner"].__setitem__(
            "antiunitary_time_reversal", "UNTESTED")),
        ("a4_same_clock", lambda d: d["a4_liftability"].__setitem__(
            "same_clock_quantum_return_constructed", True)),
        ("a4_phase_weights", lambda d: d["a4_liftability"].__setitem__(
            "fixed_caustic_orbit_phases_weights_preserved", True)),
    ]
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c275-mutations-") as directory:
        for index, (name, mutate) in enumerate(mutations):
            candidate = copy.deepcopy(original)
            mutate(candidate)
            candidate["payload_sha256"] = payload_hash(candidate)
            path = Path(directory) / f"{index:02d}_{name}.json"
            path.write_text(json.dumps(candidate, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
            environment = dict(os.environ)
            environment["PYTHONDONTWRITEBYTECODE"] = "1"
            environment["C275_EVIDENCE_PATH"] = str(path)
            result = subprocess.run(
                [sys.executable, "-B", str(CHECKER)], env=environment,
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False,
            )
            if result.returncode != 0:
                rejected += 1
    assert rejected == len(mutations), (rejected, len(mutations))
    print(f"C275 hostile mutation: PASS {rejected}/{len(mutations)}")


if __name__ == "__main__":
    main()
