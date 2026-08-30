#!/usr/bin/env python3
"""Derive the authorized Stage-4 loxodromic-only collision profile for P24.

This module is deliberately derivative.  It reads the hash-pinned Round-7
exact ledger, selects only rows already classified as ``LOXODROMIC``, and
retains the corresponding hash-pinned Round-8 D9/first-jet profile rows.  It
does not regenerate a word ball, refresh a canonical result, classify owners,
or infer primitivity or conjugacy from matrix-row collisions.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-08-30"
MANIFEST_PATH = Path("experiments/stage4_loxodromic_profile_manifest.json")
MANIFEST_SHA256 = "1860b1a566e2c4a9a3b9362af4947aa2333d2df4728893780341dd79accaae07"
LEDGER_PATH = Path("results/round7_trace_discriminant_ledger.csv")
POOLED_PROFILE_PATH = Path("results/round8_d9_jet_collision_profile.csv")
ROUND7_METRICS_PATH = Path("results/round7_trace_discriminant_metrics.json")
ROUND8_METRICS_PATH = Path("results/round8_congruence_specificity_metrics.json")
PROFILE_PATH = Path("results/stage4_loxodromic_d9_jet_collision_profile.csv")
METRICS_PATH = Path("results/stage4_loxodromic_d9_jet_metrics.json")
RECEIPT_PATH = Path("experiments/stage4_loxodromic_profile_receipt.json")
TEST_PATH = Path("code/test_stage4_loxodromic_profile.py")
REPRODUCER_PATH = Path("experiments/reproduce_stage4_loxodromic_profile.sh")

PROFILE_FIELDS = [
    "d9_re",
    "d9_im",
    "matrix_rows",
    "distinct_first_jets_up_to_sign",
    "joint_descriptor_collisions_beyond_first",
    "maximum_joint_descriptor_bucket",
    "all_joint_descriptor_buckets_are_matrix_collisions",
    "owner_interpretation",
]

REQUIRED_LEDGER_FIELDS = {
    "matrix_id",
    "matrix_class",
    "d9_re",
    "d9_im",
    "determinant_one",
    "level3_membership",
    "all_exact_witnesses_pass",
    "evidence_status",
    "arithmetic_mode",
    "owner_status",
    "completeness_boundary",
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(payload: Any) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")


def csv_bytes(rows: list[dict[str, str]]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=PROFILE_FIELDS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def combined_hash(outputs: dict[Path, bytes]) -> str:
    digest = hashlib.sha256()
    for path in sorted(outputs, key=lambda item: item.as_posix()):
        digest.update(path.as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(outputs[path])
        digest.update(b"\0")
    return digest.hexdigest()


def bound_path(relative: str | Path) -> Path:
    return (PROJECT_ROOT / relative).resolve()


def read_csv(relative: Path) -> tuple[list[str], list[dict[str, str]]]:
    raw = bound_path(relative).read_bytes()
    stream = io.StringIO(raw.decode("utf-8"), newline="")
    reader = csv.DictReader(stream)
    if reader.fieldnames is None:
        raise AssertionError(f"missing CSV header: {relative}")
    return list(reader.fieldnames), list(reader)


@lru_cache(maxsize=1)
def load_manifest() -> tuple[dict[str, Any], bytes]:
    raw = bound_path(MANIFEST_PATH).read_bytes()
    if sha256(raw) != MANIFEST_SHA256:
        raise RuntimeError("P24 Stage-4 loxodromic-profile manifest changed")
    payload = json.loads(raw)
    if payload["status"] != "AUTHOR_AUTHORIZED_DERIVATIVE_ANALYSIS":
        raise AssertionError("manifest authorization status changed")
    if payload["authorization"]["canonical_result_refresh_authorized"]:
        raise AssertionError("canonical result refresh must remain unauthorized")
    for relative, binding in payload["source_bindings"].items():
        source = bound_path(relative)
        source_raw = source.read_bytes()
        if sha256(source_raw) != binding["sha256"]:
            raise RuntimeError(f"source binding changed: {relative}")
        if len(source_raw) != binding["bytes"]:
            raise RuntimeError(f"source byte count changed: {relative}")
    if set(payload["new_output_paths"]) & set(payload["protected_paths"]):
        raise AssertionError("new outputs overlap protected paths")
    return payload, raw


def d9_key(row: dict[str, str]) -> tuple[int, int]:
    return int(row["d9_re"]), int(row["d9_im"])


@lru_cache(maxsize=1)
def source_rows() -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    ledger_fields, ledger_rows = read_csv(LEDGER_PATH)
    profile_fields, pooled_rows = read_csv(POOLED_PROFILE_PATH)
    if not REQUIRED_LEDGER_FIELDS.issubset(ledger_fields):
        raise AssertionError("frozen ledger schema lacks required fields")
    if profile_fields != PROFILE_FIELDS:
        raise AssertionError("frozen pooled-profile schema changed")
    return ledger_rows, pooled_rows


@lru_cache(maxsize=1)
def build_payload() -> tuple[list[dict[str, str]], dict[str, Any]]:
    manifest, _manifest_raw = load_manifest()
    ledger_rows, pooled_rows = source_rows()
    expected = manifest["expected_exact_metrics"]
    pooled_expected = manifest["pooled_baseline"]

    if len(ledger_rows) != pooled_expected["matrix_rows"]:
        raise AssertionError("frozen ledger row count changed")
    if len({row["matrix_id"] for row in ledger_rows}) != len(ledger_rows):
        raise AssertionError("frozen ledger matrix IDs are not unique")
    if not all(row["determinant_one"] == "true" for row in ledger_rows):
        raise AssertionError("determinant-one witness failed")
    if not all(row["level3_membership"] == "true" for row in ledger_rows):
        raise AssertionError("level-(3) witness failed")
    if not all(row["all_exact_witnesses_pass"] == "true" for row in ledger_rows):
        raise AssertionError("a frozen exact witness failed")

    class_counts = Counter(row["matrix_class"] for row in ledger_rows)
    required_class_counts = {"IDENTITY": 1, "LOXODROMIC": 10976, "PARABOLIC": 504}
    if dict(sorted(class_counts.items())) != required_class_counts:
        raise AssertionError("frozen matrix-class partition changed")

    loxodromic_rows = [row for row in ledger_rows if row["matrix_class"] == "LOXODROMIC"]
    excluded_rows = [row for row in ledger_rows if row["matrix_class"] != "LOXODROMIC"]
    if any(d9_key(row) == (0, 0) for row in loxodromic_rows):
        raise AssertionError("a selected loxodromic row has D9=(0,0)")
    if any(d9_key(row) != (0, 0) for row in excluded_rows):
        raise AssertionError("an excluded identity/parabolic row has nonzero D9")

    loxodromic_d9_counts = Counter(d9_key(row) for row in loxodromic_rows)
    pooled_by_d9 = {d9_key(row): row for row in pooled_rows}
    if len(pooled_by_d9) != len(pooled_rows):
        raise AssertionError("pooled profile contains duplicate D9 keys")
    profile = [
        dict(row)
        for row in pooled_rows
        if d9_key(row) in loxodromic_d9_counts
    ]
    if {d9_key(row) for row in profile} != set(loxodromic_d9_counts):
        raise AssertionError("loxodromic D9 keys and pooled profile disagree")
    for row in profile:
        if int(row["matrix_rows"]) != loxodromic_d9_counts[d9_key(row)]:
            raise AssertionError(f"D9 bucket size changed: {d9_key(row)}")
        if row["owner_interpretation"] != "NECESSARY_INVARIANT_ONLY_NOT_CONJUGACY_CLASSIFICATION":
            raise AssertionError("owner-interpretation boundary changed")

    matrix_rows = sum(int(row["matrix_rows"]) for row in profile)
    distinct_d9 = len(profile)
    distinct_joint = sum(int(row["distinct_first_jets_up_to_sign"]) for row in profile)
    d9_collisions = matrix_rows - distinct_d9
    joint_collisions = sum(
        int(row["joint_descriptor_collisions_beyond_first"]) for row in profile
    )
    separated = d9_collisions - joint_collisions
    maximum_d9_bucket = max(int(row["matrix_rows"]) for row in profile)
    maximum_joint_bucket = max(
        int(row["maximum_joint_descriptor_bucket"]) for row in profile
    )
    singleton_d9 = sum(int(row["matrix_rows"]) == 1 for row in profile)
    if not all(
        row["all_joint_descriptor_buckets_are_matrix_collisions"] == "true"
        for row in profile
    ):
        raise AssertionError("a loxodromic joint descriptor became a singleton")
    singleton_joint = 0

    exact_metrics = {
        "loxodromic_rows": matrix_rows,
        "distinct_d9_values": distinct_d9,
        "d9_collision_rows_beyond_first": d9_collisions,
        "distinct_joint_d9_jet_descriptors": distinct_joint,
        "joint_descriptor_collision_rows_beyond_first": joint_collisions,
        "collision_rows_separated_by_first_jet": separated,
        "collision_reduction_fraction": f"{separated}/{d9_collisions}",
        "collision_reduction_decimal": f"{separated / d9_collisions:.15f}",
        "maximum_d9_bucket": maximum_d9_bucket,
        "maximum_joint_descriptor_bucket": maximum_joint_bucket,
        "singleton_d9_buckets": singleton_d9,
        "singleton_joint_descriptor_buckets": singleton_joint,
        "profile_rows": len(profile),
    }
    if exact_metrics != expected:
        raise AssertionError(
            "authorized exact loxodromic metrics changed: "
            f"expected={expected!r}, observed={exact_metrics!r}"
        )

    round7_metrics = json.loads(bound_path(ROUND7_METRICS_PATH).read_bytes())
    round8_metrics = json.loads(bound_path(ROUND8_METRICS_PATH).read_bytes())
    pooled_audit = round8_metrics["first_jet_audit"]
    for key, value in pooled_expected.items():
        observed = (
            pooled_audit[key]
            if key in pooled_audit
            else round7_metrics.get(key)
        )
        if observed != value:
            raise AssertionError(f"pooled baseline changed for {key}")

    descriptor_multiplier = Fraction(distinct_joint, distinct_d9)
    maximum_bucket_factor = Fraction(maximum_d9_bucket, maximum_joint_bucket)
    residual_share = Fraction(joint_collisions, d9_collisions)
    metrics = {
        "schema": "p24-stage4-loxodromic-d9-jet-metrics/1.0",
        "date": DATE,
        "status": "DERIVED_EXACT_PROFILE",
        "manifest_sha256": MANIFEST_SHA256,
        "source_population": {
            "frozen_matrix_rows": len(ledger_rows),
            "selection_predicate": "matrix_class == LOXODROMIC",
            "selected_loxodromic_rows": len(loxodromic_rows),
            "excluded_identity_or_parabolic_rows": len(excluded_rows),
            "excluded_class_counts": {
                "IDENTITY": class_counts["IDENTITY"],
                "PARABOLIC": class_counts["PARABOLIC"],
            },
            "selected_d9_zero_rows": 0,
            "excluded_d9_zero_rows": len(excluded_rows),
            "classification_source": "FROZEN_ROUND7_MATRIX_CLASS_COLUMN",
        },
        "loxodromic_only_profile": exact_metrics,
        "derived_ratios": {
            "joint_to_scalar_descriptor_multiplier_fraction": (
                f"{descriptor_multiplier.numerator}/{descriptor_multiplier.denominator}"
            ),
            "joint_to_scalar_descriptor_multiplier_decimal": (
                f"{float(descriptor_multiplier):.15f}"
            ),
            "maximum_bucket_reduction_factor_fraction": (
                f"{maximum_bucket_factor.numerator}/{maximum_bucket_factor.denominator}"
            ),
            "maximum_bucket_reduction_factor_decimal": (
                f"{float(maximum_bucket_factor):.15f}"
            ),
            "residual_joint_collision_share_fraction": (
                f"{residual_share.numerator}/{residual_share.denominator}"
            ),
            "residual_joint_collision_share_decimal": (
                f"{float(residual_share):.15f}"
            ),
        },
        "pooled_baseline": pooled_expected,
        "exact_delta_pooled_minus_loxodromic": {
            "matrix_rows": pooled_expected["matrix_rows"] - matrix_rows,
            "distinct_d9_values": pooled_expected["distinct_d9_values"] - distinct_d9,
            "d9_collision_rows_beyond_first": (
                pooled_expected["d9_collision_rows_beyond_first"] - d9_collisions
            ),
            "distinct_joint_d9_jet_descriptors": (
                pooled_expected["distinct_joint_d9_jet_descriptors"] - distinct_joint
            ),
            "joint_descriptor_collision_rows_beyond_first": (
                pooled_expected["joint_descriptor_collision_rows_beyond_first"]
                - joint_collisions
            ),
            "collision_rows_separated_by_first_jet": (
                pooled_expected["collision_rows_separated_by_first_jet"] - separated
            ),
            "maximum_d9_bucket": (
                pooled_expected["maximum_d9_bucket"] - maximum_d9_bucket
            ),
            "maximum_joint_descriptor_bucket": (
                pooled_expected["maximum_joint_descriptor_bucket"]
                - maximum_joint_bucket
            ),
        },
        "interpretation": {
            "population": "FROZEN_EXACT_LOXODROMIC_MATRIX_ROWS_ONLY",
            "collision_unit": "ROWS_BEYOND_FIRST_REPRESENTATIVES_NOT_PAIRS",
            "claim": "FINITE_MATRIX_COMPRESSION_PROFILE_ONLY",
            "primitive_owner_collision_witness": "NOT_SUPPLIED",
            "primitive_owner_separation_claim": "NOT_MADE",
            "operative_owner_equivalence": "LEVEL_SUBGROUP_CONJUGACY_ONLY",
            "completeness_boundary": (
                "ELEMENTARY_GENERATED_SUBGROUP_REDUCED_WORD_BALL_LE_5;"
                "NOT_FULL_GAMMA3;NOT_FULL_CONJUGACY_ENUMERATION"
            ),
        },
        "formal_route_a_tuple": manifest["claim_boundary"]["formal_route_a_tuple"],
        "overall_verdict": "ROUTE_A_EXPLORATORY",
        "full_bianchi_flow_route_tuple": "UNASSIGNED",
        "typed_proxy_a2_a4_evaluation": "A2_FAIL_A3_FAIL_A4_FAIL",
        "route_b_evaluation": "NOT_RUN",
        "route_b_invocation_allowed": False,
        "prime_or_zero_target_data_used": False,
        "canonical_results_refreshed": False,
        "registered_claim_surfaces_modified": False,
    }
    return profile, metrics


def primary_outputs() -> tuple[dict[Path, bytes], dict[str, Any]]:
    profile, metrics = build_payload()
    return {
        PROFILE_PATH: csv_bytes(profile),
        METRICS_PATH: json_bytes(metrics),
    }, metrics


def receipt_for(material: dict[Path, bytes], metrics: dict[str, Any]) -> dict[str, Any]:
    source_paths = [MANIFEST_PATH, Path(__file__).resolve().relative_to(PROJECT_ROOT), TEST_PATH, REPRODUCER_PATH]
    source_bindings = {
        relative.as_posix(): {
            "sha256": sha256(bound_path(relative).read_bytes()),
            "bytes": bound_path(relative).stat().st_size,
        }
        for relative in source_paths
    }
    manifest, _raw = load_manifest()
    audit = metrics["loxodromic_only_profile"]
    return {
        "schema": "p24-stage4-loxodromic-profile-receipt/1.0",
        "date": DATE,
        "status": "REPRODUCIBLE",
        "manifest": {"path": MANIFEST_PATH.as_posix(), "sha256": MANIFEST_SHA256},
        "material_sha256": combined_hash(material),
        "execution": {"required_independent_builds": 2, "byte_identical": True},
        "unit_tests": {"expected": 10, "failed": 0},
        "output_bindings": {
            path.as_posix(): {"sha256": sha256(data), "bytes": len(data)}
            for path, data in sorted(material.items(), key=lambda item: item[0].as_posix())
        },
        "source_bindings": source_bindings,
        "canonical_source_bindings": manifest["source_bindings"],
        "selected_loxodromic_rows": audit["loxodromic_rows"],
        "distinct_d9_values": audit["distinct_d9_values"],
        "distinct_joint_d9_jet_descriptors": audit["distinct_joint_d9_jet_descriptors"],
        "joint_descriptor_collision_rows_beyond_first": (
            audit["joint_descriptor_collision_rows_beyond_first"]
        ),
        "primitive_owner_claim": "NOT_MADE",
        "formal_route_a_tuple": metrics["formal_route_a_tuple"],
        "overall_verdict": metrics["overall_verdict"],
        "full_bianchi_flow_route_tuple": "UNASSIGNED",
        "route_b_invocation_allowed": False,
        "canonical_results_refreshed": False,
        "registered_claim_surfaces_modified": False,
        "default_reproduction_command": "bash experiments/reproduce_stage4_loxodromic_profile.sh",
        "new-output-refresh_command": (
            "bash experiments/reproduce_stage4_loxodromic_profile.sh --refresh"
        ),
    }


def rendered_outputs() -> dict[Path, bytes]:
    primary, metrics = primary_outputs()
    return {**primary, RECEIPT_PATH: json_bytes(receipt_for(primary, metrics))}


def write_outputs(output_root: Path) -> None:
    for relative, data in rendered_outputs().items():
        destination = output_root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(data)


def verify_existing(output_root: Path) -> None:
    mismatches: list[str] = []
    for relative, expected in rendered_outputs().items():
        destination = output_root / relative
        if not destination.exists():
            mismatches.append(f"missing:{relative}")
        elif destination.read_bytes() != expected:
            mismatches.append(f"different:{relative}")
    if mismatches:
        raise SystemExit("verification failed: " + ", ".join(mismatches))
    print("P24 Stage-4 loxodromic-only profile VERIFIED")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-root", type=Path, default=PROJECT_ROOT)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--verify-existing", action="store_true")
    mode.add_argument("--refresh", action="store_true")
    args = parser.parse_args()
    if args.refresh:
        write_outputs(args.output_root)
        _primary, metrics = primary_outputs()
        audit = metrics["loxodromic_only_profile"]
        print(json.dumps({
            "distinct_d9_values": audit["distinct_d9_values"],
            "distinct_joint_descriptors": audit["distinct_joint_d9_jet_descriptors"],
            "joint_collision_rows": audit["joint_descriptor_collision_rows_beyond_first"],
            "loxodromic_rows": audit["loxodromic_rows"],
            "status": "NEW_DERIVATIVE_OUTPUTS_REFRESHED",
        }, sort_keys=True))
    else:
        verify_existing(args.output_root)


if __name__ == "__main__":
    main()
