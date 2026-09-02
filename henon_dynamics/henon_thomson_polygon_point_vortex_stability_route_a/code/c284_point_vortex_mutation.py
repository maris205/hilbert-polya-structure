#!/usr/bin/env python3
"""Repaired-hash semantic and stale-hash mutation audit for HCS-C284."""
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
SOURCE = ROOT / "results/c284_point_vortex_evidence.json"


def payload_hash(data: dict) -> str:
    clean = dict(data)
    clean.pop("payload_sha256", None)
    raw = json.dumps(
        clean, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode()
    return hashlib.sha256(raw).hexdigest()


def set_path(data, path, value) -> None:
    target = data
    for key in path[:-1]:
        target = target[key]
    target[path[-1]] = value


def delete_path(data, path) -> None:
    target = data
    for key in path[:-1]:
        target = target[key]
    del target[path[-1]]


def run_checker(candidate: Path) -> bool:
    env = dict(os.environ)
    env["C284_EVIDENCE"] = str(candidate)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    run = subprocess.run(
        [sys.executable, "-B", str(ROOT / "code/c284_point_vortex_checker.py")],
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    return run.returncode != 0


def main() -> None:
    base = json.loads(SOURCE.read_text())
    mutations = [
        ("source", ("source_commit",), "0" * 40),
        ("date", ("evaluation_date",), "2026-09-01"),
        ("epoch", ("fixed_epoch",), 1),
        ("scope", ("scope_literal",), "BROKEN_SCOPE"),
        ("evaluator", ("evaluator", "sha256"), "0" * 64),
        ("schema", ("schema",), "wrong-schema"),
        ("candidate", ("candidate_id",), "HCS-C000"),
        ("headline", ("headline",), "false repaired headline"),
        ("audit_json", ("audit_contract", "json_policy"), "accept duplicates"),
        ("audit_slice", ("audit_contract", "slice_policy"), "assume the slice"),
        ("model_hamiltonian", ("model_contract", "hamiltonian"), "H=0"),
        ("model_omega", ("model_contract", "angular_velocity"), "Omega=Gamma*N/(4*pi*R^2)"),
        ("block_root_sum", ("block_contract", "root_sum"), "S_m=0"),
        ("block_square", ("block_contract", "square"), "L_m^2=0"),
        ("reduction_center", ("reduction_contract", "center"), "remove all first harmonics"),
        ("reduction_complement", ("reduction_contract", "first_harmonic_remainder"), "hyperbolic"),
        ("proof_status", ("proof_contract", "status"), "HEURISTIC"),
        ("proof_dependency", ("proof_contract", "dependencies", 0), "copied final block"),
        ("proof_scope", ("proof_contract", "scope"), "nonlinear stability too"),
        ("proof_heptagon", ("proof_contract", "heptagon_boundary"), "N=7 is nonlinearly stable"),
        ("source_owner", ("source_owner_contract", "classical_owner"), "anonymous"),
        ("source_doi", ("source_owner_contract", "linear_stability_owner_doi"), "10.invalid"),
        ("source_use", ("source_owner_contract", "use_boundary"), "proof outsourced"),
        ("obligation", ("analytic_proof_obligations", 0), "skip Omega"),
        ("nonclaim", ("nonclaims", 1), "finite table proves all N"),
        ("route_tuple", ("route_a", "tuple", 1), "A1_PASS_ANALYTIC"),
        ("route_overall", ("route_a", "overall"), "ROUTE_A_ACCEPTED"),
        ("route_b", ("route_a", "route_b_invocation_allowed"), True),
        ("scope_flag", ("scope_flags", "euler_factors"), True),
        ("count_block", ("regression", "counts", "block_rows"), 2076),
        ("block_q", ("regression", "block_rows", 100, "q_m"), -1),
        ("block_radial", ("regression", "block_rows", 250, "radial_hessian_over_c"), 999),
        ("block_det", ("regression", "block_rows", 500, "det_hessian_over_c2"), 1),
        ("block_regime", ("regression", "block_rows", 750, "regime"), "elliptic"),
        ("block_role", ("regression", "block_rows", 1, "reduced_role"), "THIS_IS_FALSE"),
        ("block_spectral", ("regression", "block_rows", 2, "spectral_pair"), "zero"),
        ("block_mode", ("regression", "block_rows", 0, "mode"), 3),
        ("polygon_class", ("regression", "polygon_rows", 4, "classification"), "nonlinearly_stable"),
        ("polygon_degenerate", ("regression", "polygon_rows", 4, "degenerate_modes"), []),
        ("polygon_hyperbolic", ("regression", "polygon_rows", 5, "hyperbolic_modes"), [4]),
        ("scale_value", ("regression", "scale_rows", 0, "four_pi_c"), "999/1"),
        ("scale_bool_type", ("regression", "scale_rows", 0, "stability_class_invariant_under_scale"), 1),
        ("slice_dimension", ("regression", "slice_rows", 0, "reduced_dimension"), 999),
        ("slice_semantic", ("regression", "slice_rows", 0, "first_harmonic_restriction"), "remove all"),
        ("boundary_semantic", ("regression", "boundary_rows", 6, "status"), "nonlinear stability proved"),
        ("bool_mode", ("regression", "block_rows", 0, "mode"), False),
        ("bool_q", ("regression", "block_rows", 0, "q_m"), False),
        ("bool_polygon_count", ("regression", "polygon_rows", 0, "hyperbolic_mode_count"), False),
        ("string_n", ("regression", "block_rows", 0, "n"), "3"),
        ("unknown_top", ("unexpected_top",), True),
        ("unknown_nested", ("regression", "unexpected_nested"), True),
        ("unknown_row", ("regression", "block_rows", 0, "unexpected"), True),
    ]
    drops = [
        ("drop_headline", ("headline",)),
        ("drop_audit", ("audit_contract", "row_policy")),
        ("drop_model", ("model_contract", "clock")),
        ("drop_block", ("block_contract", "linear_block")),
        ("drop_reduction", ("reduction_contract", "classification")),
        ("drop_proof_dependency", ("proof_contract", "dependencies", 0)),
        ("drop_source", ("source_owner_contract", "use_boundary")),
        ("drop_obligation", ("analytic_proof_obligations", 0)),
        ("drop_nonclaim", ("nonclaims", 1)),
        ("drop_block_field", ("regression", "block_rows", 0, "reduced_role")),
        ("drop_polygon_field", ("regression", "polygon_rows", 0, "classification")),
        ("drop_scale_field", ("regression", "scale_rows", 0, "radius")),
        ("drop_slice_field", ("regression", "slice_rows", 0, "reduced_dimension")),
        ("drop_boundary_field", ("regression", "boundary_rows", 0, "condition")),
        ("drop_row_family", ("regression", "slice_rows")),
    ]

    repaired_trials: list[tuple[str, dict]] = []
    for name, path, value in mutations:
        trial = copy.deepcopy(base)
        set_path(trial, path, value)
        trial["payload_sha256"] = payload_hash(trial)
        repaired_trials.append((name, trial))
    for name, path in drops:
        trial = copy.deepcopy(base)
        delete_path(trial, path)
        trial["payload_sha256"] = payload_hash(trial)
        repaired_trials.append((name, trial))
    for family in ("block_rows", "polygon_rows", "scale_rows", "slice_rows", "boundary_rows"):
        trial = copy.deepcopy(base)
        trial["regression"][family][-1] = copy.deepcopy(trial["regression"][family][0])
        trial["payload_sha256"] = payload_hash(trial)
        repaired_trials.append((f"duplicate_replace_{family}", trial))
    trial = copy.deepcopy(base)
    trial["regression"]["block_rows"][0], trial["regression"]["block_rows"][1] = (
        trial["regression"]["block_rows"][1], trial["regression"]["block_rows"][0]
    )
    trial["payload_sha256"] = payload_hash(trial)
    repaired_trials.append(("block_order_swap", trial))

    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c284-mutation-") as temp:
        directory = Path(temp)
        accepted: list[str] = []
        for index, (name, trial) in enumerate(repaired_trials):
            candidate = directory / f"{index:02d}_{name}.json"
            candidate.write_text(
                json.dumps(trial, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
            )
            was_rejected = run_checker(candidate)
            rejected += was_rejected
            if not was_rejected:
                accepted.append(name)

        stale = copy.deepcopy(base)
        stale["headline"] += " stale-hash tamper"
        stale_path = directory / "stale_hash.json"
        stale_path.write_text(json.dumps(stale, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
        rejected += run_checker(stale_path)

        raw = SOURCE.read_text()
        duplicate_path = directory / "raw_duplicate.json"
        needle = '  "candidate_id": "HCS-C284",\n'
        duplicate_path.write_text(raw.replace(needle, '  "candidate_id": "EVIL-FIRST",\n' + needle, 1))
        rejected += run_checker(duplicate_path)

        nonstandard_path = directory / "raw_nan.json"
        nonstandard_path.write_text(raw.replace(
            '  "fixed_epoch": 1788307200,', '  "fixed_epoch": NaN,', 1
        ))
        rejected += run_checker(nonstandard_path)

    total = len(repaired_trials) + 3
    assert not accepted, f"accepted repaired-hash mutations: {accepted}"
    assert rejected == total
    print(
        f"C284 hostile mutation audit: PASS {rejected}/{total} "
        "(repaired-hash schema/semantic attacks plus stale-hash, raw "
        "duplicate-key, and nonstandard-constant controls)"
    )


if __name__ == "__main__":
    main()
