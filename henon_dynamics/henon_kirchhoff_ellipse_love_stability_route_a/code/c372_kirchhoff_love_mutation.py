#!/usr/bin/env python3
"""Hostile JSON/YAML mutation suite for HCS-C372."""
from __future__ import annotations

if not __debug__:
    raise RuntimeError("C372 mutation suite refuses optimized Python")

import copy
import hashlib
import json
import tempfile
from pathlib import Path

from c372_kirchhoff_love_checker import EV, YML, check


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def repair(value):
    value = copy.deepcopy(value)
    value.pop("payload_sha256", None)
    value["payload_sha256"] = hashlib.sha256(canonical(value)).hexdigest()
    return value


def mutate_path(base, path, replacement):
    value = copy.deepcopy(base)
    cursor = value
    for key in path[:-1]:
        cursor = cursor[key]
    cursor[path[-1]] = replacement
    return repair(value)


def reject_json(value, label, raw=False):
    with tempfile.TemporaryDirectory(prefix="c372-mutation-") as directory:
        path = Path(directory) / "mutant.json"
        path.write_text(value if raw else json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
        try:
            check(path, YML)
        except Exception:
            return
    raise AssertionError(f"surviving JSON mutation: {label}")


def reject_yaml(raw, label):
    with tempfile.TemporaryDirectory(prefix="c372-yaml-") as directory:
        path = Path(directory) / "mutant.yaml"
        path.write_text(raw)
        try:
            check(EV, path)
        except Exception:
            return
    raise AssertionError(f"surviving YAML mutation: {label}")


def main():
    base = json.loads(EV.read_text())
    attacks = [
        (("candidate_id",), "HCS-C000", "candidate"),
        (("obstruction_id",), "HEN-O000", "obstruction"),
        (("source_commit",), "0" * 40, "source"),
        (("fixed_epoch",), 0, "epoch"),
        (("scope_literal",), "OPEN", "scope"),
        (("evaluator", "sha256"), "0" * 64, "evaluator"),
        (("route_a_yaml", "semantic_sha256"), "0" * 64, "YAML receipt"),
        (("model", "equation"), "Navier-Stokes", "equation"),
        (("model", "ellipse"), "circle", "ellipse"),
        (("model", "mode_convention"), "exp(+lambda*t)", "mode convention"),
        (("theorem_contract", "rigid_rotation"), "Omega=0", "rotation theorem"),
        (("theorem_contract", "love_dispersion"), "lambda=0", "Love formula"),
        (("theorem_contract", "symmetry_modes"), "m1=m2=0", "symmetry modes"),
        (("theorem_contract", "critical_equation"), "no root", "critical equation"),
        (("theorem_contract", "threshold_order"), "decreasing", "threshold order"),
        (("theorem_contract", "threshold_asymptotic"), "gamma_m/m tends to zero", "threshold asymptotic"),
        (("theorem_contract", "sharp_wall"), "gamma=4", "first wall"),
        (("theorem_contract", "scope"), "nonlinear stability proved", "scope theorem"),
        (("proof_receipts", "dimensionless_variables"), "kappa=delta", "dimensionless proof"),
        (("proof_receipts", "factorization"), "one factor", "factorization proof"),
        (("proof_receipts", "positive_second_factor"), "G is negative", "G proof"),
        (("proof_receipts", "ordered_roots"), "zero", "order proof"),
        (("proof_receipts", "scaled_root"), "c_m is unbounded", "scaled-root proof"),
        (("proof_receipts", "m3_factor"), "wrong", "m3 proof"),
        (("finite_grid", "distinct_aspect_ratios"), 560, "aspect count"),
        (("finite_grid", "modal_cells"), 35903, "modal count"),
        (("finite_grid", "modal_cells_sha256"), "0" * 64, "modal digest"),
        (("aspect_rows", 0, "delta"), "1", "circle delta"),
        (("aspect_rows", 1, "rotation_rate_over_vorticity"), "0", "rotation ratio"),
        (("aspect_rows", 2, "classification_counts", "critical"), 2, "class counts"),
        (("aspect_rows", 3, "mode_rows_sha256"), "0" * 64, "row digest"),
        (("aspect_rows", 4, "anchor_modes", 0, "love_square_coefficient"), "0", "m1 anchor"),
        (("aspect_rows", 5, "anchor_modes", 1, "m2_family_identity_residual"), "1", "m2 residual"),
        (("critical_thresholds", 0, "delta_lower"), "1/3", "first threshold"),
        (("critical_thresholds", 1, "upper_sign"), 1, "bracket sign"),
        (("critical_thresholds", 2, "aspect_upper"), "7", "threshold transform"),
        (("rigid_solution_rows", 0, "rotation_rate"), "0", "rigid rate"),
        (("rigid_solution_rows", 1, "quadratic_vorticity_moment_over_pi"), "0", "moment"),
        (("rigid_solution_rows", 5, "patch_minimal_period_over_pi"), "3", "patch period"),
        (("rigid_solution_rows", 5, "oriented_axis_period_over_pi"), "3/2", "oriented-axis period"),
        (("rigid_solution_rows", 0, "rotation_orientation"), "clockwise", "circle orientation"),
        (("boundary_atlas", 1, "mode_statement"), "rotating circle", "circle boundary"),
        (("collision_boundary", "C284"), "same system", "collision"),
        (("references", 0, "role"), "secondary source", "Love owner role"),
        (("references", 1, "role"), "inertial-frame convention", "co-rotating source role"),
        (("nonclaims", 0), "nonlinear stability theorem", "nonclaim"),
        (("route_a", "tuple"), ["A0_PASS"] * 5, "route tuple"),
        (("route_a", "overall"), "ROUTE_A_CANDIDATE", "route verdict"),
        (("route_a", "route_b_invocation_allowed"), True, "Route B"),
        (("scope_flags", "claims_hilbert_polya_operator"), True, "forbidden flag"),
    ]
    count = 0
    for path, replacement, label in attacks:
        reject_json(mutate_path(base, path, replacement), label)
        count += 1
    deleted = copy.deepcopy(base)
    del deleted["theorem_contract"]
    reject_json(repair(deleted), "deleted key")
    count += 1
    extra = copy.deepcopy(base)
    extra["surprise"] = True
    reject_json(repair(extra), "extra key")
    count += 1
    truncated = copy.deepcopy(base)
    truncated["aspect_rows"] = truncated["aspect_rows"][:-1]
    reject_json(repair(truncated), "truncated aspects")
    count += 1
    reordered = copy.deepcopy(base)
    reordered["critical_thresholds"][0], reordered["critical_thresholds"][1] = reordered["critical_thresholds"][1], reordered["critical_thresholds"][0]
    reject_json(repair(reordered), "reordered thresholds")
    count += 1
    stale = copy.deepcopy(base)
    stale["candidate_id"] = "HCS-C000"
    reject_json(stale, "stale payload hash")
    count += 1
    reject_json('{"candidate_id":"a","candidate_id":"b"}', "duplicate JSON", raw=True)
    count += 1
    reject_json('{"payload_sha256":NaN}', "nonfinite JSON", raw=True)
    count += 1
    reject_json('[]', "invalid JSON root", raw=True)
    count += 1
    yraw = YML.read_text()
    reject_yaml(yraw + "candidate_id: duplicate\n", "duplicate YAML")
    count += 1
    reject_yaml("base: &base {x: 1}\ncopy: *base\n", "aliased YAML")
    count += 1
    reject_yaml(yraw.replace("A1_WEAK", "A1_PASS_ANALYTIC", 1), "YAML route")
    count += 1
    reject_yaml(yraw.replace("claims_target_zero_match: false", "claims_target_zero_match: true"), "YAML scope")
    count += 1
    reject_yaml(yraw.replace("DOI:10.1112/plms/s1-25.1.18", "DOI:10.1112/removed"), "YAML Love owner")
    count += 1
    reject_yaml("- invalid\n- root\n", "YAML root")
    count += 1
    print(f"C372 hostile mutation suite: PASS ({count} attacks)")


if __name__ == "__main__":
    main()
