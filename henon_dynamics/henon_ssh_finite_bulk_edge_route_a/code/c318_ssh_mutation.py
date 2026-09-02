#!/usr/bin/env python3
"""Hostile repaired-hash and parser mutation suite for HCS-C318."""
from __future__ import annotations

import copy
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c318_ssh_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C318/2026-09-03.yaml"
CHECKER = ROOT / "code/c318_ssh_checker.py"


def payload_hash(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def set_path(data, path, value):
    cursor = data
    for key in path[:-1]:
        cursor = cursor[key]
    cursor[path[-1]] = value


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C318 mutation lane refuses optimized Python")
    data = json.loads(EVIDENCE.read_text())
    json_raw = EVIDENCE.read_text()
    yaml_raw = EVALUATION.read_text()
    attacks = []
    semantic = [
        (("candidate_id",), "HCS-C000"),
        (("obstruction_id",), "HEN-O000"),
        (("source_commit",), "0" * 40),
        (("scope_literal",), "EXPANDED"),
        (("evaluator", "version"), "9.9.9"),
        (("model", "open_block"), "wrong block"),
        (("theorem_contract", "characteristic"), "monic prefactor omitted"),
        (("collision_boundary", "C308"), "collision erased"),
        (("nonclaims", 1), "claim promoted"),
        (("references", 0, "role"), "wrong provenance"),
        (("route_a", "tuple", 4), "A4_PASS"),
        (("route_a", "route_b_invocation_allowed"), True),
        (("scope_flags", "claims_hilbert_polya_operator"), True),
        (("obc_polynomial_rows", 0, "label"), "topological"),
        (("obc_polynomial_rows", 1, "q_coefficients_y_ascending", 0), "0"),
        (("obc_polynomial_rows", 2, "root_zone"), "one_hyperbolic_pair"),
        (("exact_edge_witnesses", 0, "w"), "2"),
        (("exact_edge_witnesses", 1, "edge_energy"), "1"),
        (("exact_edge_witnesses", 2, "a_vector", 0), "0"),
        (("exact_edge_witnesses", 3, "strict_decay_bound"), "2/3"),
        (("finite_threshold_rows", 0, "x"), "0"),
        (("finite_threshold_rows", 1, "b_linear_taper", 0), "0"),
        (("periodic_rows", 0, "label"), "topological"),
        (("periodic_rows", 1, "winding_value"), 0),
        (("periodic_rows", 2, "finite_zero_multiplicity"), 0),
        (("periodic_rows", 3, "momentum_cells", 0, "mode"), 9),
        (("periodic_rows", 4, "momentum_cells", 0, "q_real"), "9.0"),
        (("boundary_rows", 0, "face"), "v_zero"),
        (("boundary_rows", 1, "kernel_dimension"), 0),
        (("one_cell_convention", "periodic_wrap_eigenvalues", 1), "5"),
        (("propagator_rows", 0, "label"), "critical"),
        (("propagator_rows", 1, "selected_entries", 0, "imag"), "1.0"),
        (("propagator_rows", 2, "unitarity_residual"), "1.0"),
        (("quench_rows", 0, "cos_k_star"), "-1/3"),
        (("quench_rows", 1, "finite_grid_hits_M_2_to_12"), [{"M": 4, "modes": [1]}]),
        (("quench_rows", 5, "endpoints_gapped"), True),
        (("enumeration", "periodic_momentum_cells"), 594),
        (("enumeration", "audited_leaf_count"), 0),
    ]
    for path, value in semantic:
        mutated = copy.deepcopy(data)
        set_path(mutated, path, value)
        mutated["payload_sha256"] = payload_hash(mutated)
        attacks.append(("semantic", json.dumps(mutated, sort_keys=True, indent=2) + "\n", yaml_raw))

    extra = copy.deepcopy(data)
    extra["obc_polynomial_rows"][0]["unlocked_metadata"] = "survive?"
    extra["payload_sha256"] = payload_hash(extra)
    attacks.append(("extra-row-key", json.dumps(extra, sort_keys=True, indent=2) + "\n", yaml_raw))

    # This repaired-hash attack preserves the first row's ratio, root zone,
    # characteristic polynomial, and determinant after the global scale
    # (v,w)=(3,2)->(6,4).  Only the independently fixed producer grid can
    # reject it.
    scaled = copy.deepcopy(data)
    scaled_row = scaled["obc_polynomial_rows"][0]
    m = scaled_row["M"]
    factor = Fraction(2)
    scaled_row["v"] = q(factor * Fraction(scaled_row["v"]))
    scaled_row["w"] = q(factor * Fraction(scaled_row["w"]))
    scaled_row["q_coefficients_y_ascending"] = [
        q(Fraction(value) * factor ** (2 * m - 2 * degree))
        for degree, value in enumerate(scaled_row["q_coefficients_y_ascending"])
    ]
    scaled_row["det_T"] = q(Fraction(scaled_row["det_T"]) * factor**m)
    scaled["payload_sha256"] = payload_hash(scaled)
    attacks.append(("repaired-hash-obc-global-scale", json.dumps(scaled, sort_keys=True, indent=2) + "\n", yaml_raw))

    # At v=w on an odd ring the continuum gap vanishes but the sampled
    # ring gap is strictly positive.  A repaired checksum must not conceal
    # a regression to the old ambiguous zero-gap receipt.
    odd_gap = copy.deepcopy(data)
    odd_row = next(row for row in odd_gap["periodic_rows"] if row["M"] == 3 and row["label"] == "critical")
    odd_row["finite_sampled_gap_to_zero"] = "0.0"
    odd_row["finite_sampled_central_band_gap"] = "0.0"
    odd_gap["payload_sha256"] = payload_hash(odd_gap)
    attacks.append(("repaired-hash-odd-critical-sampled-gap", json.dumps(odd_gap, sort_keys=True, indent=2) + "\n", yaml_raw))
    attacks.extend(
        [
            ("duplicate-json", json_raw.replace("{\n", '{\n  "schema": "duplicate",\n', 1), yaml_raw),
            ("nan-json", json_raw.replace('"fixed_epoch": 1788393600', '"fixed_epoch": NaN', 1), yaml_raw),
            ("json-root-array", "[]\n", yaml_raw),
        ]
    )
    yaml_attacks = [
        ("yaml-duplicate", yaml_raw + "candidate_id: HCS-C318\n"),
        ("yaml-anchor", yaml_raw.replace("candidate_id: HCS-C318", "candidate_id: &owner HCS-C318", 1)),
        ("yaml-source", yaml_raw.replace("source_commit: 1938bae19e5a92f9ce2411aafdc68323bd641bd0", "source_commit: 0000000000000000000000000000000000000000", 1)),
        ("yaml-route", yaml_raw.replace("route_b_invocation_allowed: false", "route_b_invocation_allowed: true", 1)),
        ("yaml-scope", yaml_raw.replace("  claims_hilbert_polya_operator: false", "  claims_hilbert_polya_operator: true", 1)),
        ("yaml-theorem", yaml_raw.replace("theorem_status: PROVABLE_AS_STATED", "theorem_status: UNCHECKED", 1)),
        ("yaml-source-owner", yaml_raw.replace("  - 10.1103/PhysRevLett.42.1698", "  - 10.0000/fake", 1)),
        ("yaml-root-array", "- invalid\n"),
        ("yaml-equivalent-whitespace", yaml_raw + "\n"),
    ]
    attacks.extend((name, json_raw, mutated_yaml) for name, mutated_yaml in yaml_attacks)

    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c318-mutation-") as directory:
        directory = Path(directory)
        for index, (name, raw_json, raw_yaml) in enumerate(attacks):
            evidence = directory / f"attack-{index}.json"
            evaluation = directory / f"attack-{index}.yaml"
            evidence.write_text(raw_json)
            evaluation.write_text(raw_yaml)
            process = subprocess.run(
                [sys.executable, "-B", str(CHECKER), "--evidence", str(evidence), "--evaluation", str(evaluation)],
                env=env,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
            )
            if process.returncode == 0:
                raise AssertionError(f"hostile attack survived: {name}-{index}")
            rejected += 1
    print(f"C318 hostile mutation suite: PASS {rejected}/{len(attacks)}")


if __name__ == "__main__":
    main()
