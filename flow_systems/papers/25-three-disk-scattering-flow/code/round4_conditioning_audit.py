#!/usr/bin/env python3
"""Deterministic Round-4 conditioning audit for the certified P25 ledger.

This program performs no orbit solve and reads no prime or zero data.  It
audits the already frozen Round-3 direct-return-map ledger, separates direct
Newton rows from the geometric stationarity fallback, and verifies from the
Round-3 source that the fallback/refinement path does not consume the
paraxial trace or half-density comparison fields.
"""

from __future__ import annotations

import argparse
import ast
import csv
import hashlib
import io
import json
from collections import Counter, defaultdict
from decimal import Decimal, getcontext
from pathlib import Path
from statistics import median
from typing import Iterable, Sequence


getcontext().prec = 80

DATE = "2026-08-27"
CANDIDATE_ID = "P25-THREE-DISK-ROUND4-CONDITIONING-AUDIT"
EXPECTED_ROWS = 2241
EXPECTED_INPUT_SHA256 = (
    "1b932a5ca3cf7123e9428b3eb2f26078d8e289eabb11dd828379ecf39eeb414e"
)
EXPECTED_ROUND3_SOURCE_SHA256 = (
    "6589730dbe14a0a56190d05acdef4dd430604c0813be092a8d1616465d6d9298"
)
DIRECT_METHOD = "DIRECT_RETURN_MAP_MDNEWTON"
FALLBACK_METHOD = "SPECULAR_STATIONARITY_FALLBACK"
POST_LIMIT = Decimal("1e-60")
SPAN_LIMIT = Decimal("1e-18")
DET_LIMIT = Decimal("1e-18")
TRACE_LIMIT = Decimal("2e-12")
HALF_DENSITY_LIMIT = Decimal("2e-12")

LENGTH_FIELDS = (
    "topological_word_length",
    "row_count",
    "odd_length_rows",
    "round2_open_rows",
    "round3_certified_rows",
    "direct_newton_rows",
    "stationarity_fallback_rows",
    "fallback_fraction",
    "fallback_rate_decimal",
    "abs_paraxial_trace_min",
    "abs_paraxial_trace_median",
    "abs_paraxial_trace_max",
    "pre_refinement_return_residual_max",
    "post_refinement_return_residual_max",
    "multiscale_trace_relative_span_max",
    "fine_determinant_residual_max",
    "parity_trace_relative_residual_max",
    "half_density_relative_residual_max",
)

FALLBACK_FIELDS = (
    "row_id",
    "d_over_a",
    "topological_word_length",
    "cyclic_word",
    "source_round2_fd_status",
    "abs_source_paraxial_trace",
    "source_trace_condition_tier",
    "pre_refinement_return_residual",
    "fallback_stationarity_residual",
    "post_refinement_return_residual",
    "multiscale_trace_relative_span",
    "fine_determinant_residual",
    "parity_corrected_trace_relative_residual",
    "half_density_relative_residual",
    "round3_validation_status",
    "round3_failure_tier",
    "fallback_selector_uses_paraxial_target",
    "fallback_selector_uses_prime_or_zero_data",
    "evidence_status",
)

REFINEMENT_FUNCTIONS = (
    "ray_step_mp",
    "direct_return_map",
    "direct_return_residual",
    "initial_state_from_row",
    "initial_collision_angles_from_row",
    "specular_stationarity_gradient",
    "state_from_collision_angles",
    "refine_state_via_specular_stationarity",
    "refine_periodic_state",
    "central_difference_jacobian",
)

FORBIDDEN_REFINEMENT_NAMES = {
    "monodromy_trace",
    "half_density_value",
    "source_paraxial_trace",
    "source_half_density",
    "prime",
    "riemann_zero",
    "zero_table",
}


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def decimal_text(value: Decimal) -> str:
    return format(value, "e")


def read_rows(project_root: Path) -> tuple[list[dict[str, str]], str]:
    path = project_root / "results/three_disk_return_map_validation_round3.csv"
    payload = path.read_bytes()
    digest = sha256_bytes(payload)
    if digest != EXPECTED_INPUT_SHA256:
        raise RuntimeError(f"Round-3 ledger drift: {digest}")
    rows = list(csv.DictReader(io.StringIO(payload.decode("utf-8"))))
    if len(rows) != EXPECTED_ROWS:
        raise RuntimeError(f"expected {EXPECTED_ROWS} rows, found {len(rows)}")
    return rows, digest


def condition_tier(value: Decimal) -> str:
    magnitude = abs(value)
    if magnitude <= Decimal("1e3"):
        return "ABS_TRACE_LE_1E3"
    if magnitude <= Decimal("1e6"):
        return "ABS_TRACE_1E3_TO_1E6"
    if magnitude <= Decimal("1e9"):
        return "ABS_TRACE_1E6_TO_1E9"
    if magnitude <= Decimal("1e12"):
        return "ABS_TRACE_1E9_TO_1E12"
    return "ABS_TRACE_GT_1E12"


def refinement_source_audit(project_root: Path) -> dict[str, object]:
    path = project_root / "code/round3_return_map_validation.py"
    payload = path.read_bytes()
    source_digest = sha256_bytes(payload)
    if source_digest != EXPECTED_ROUND3_SOURCE_SHA256:
        raise RuntimeError(f"Round-3 validation source drift: {source_digest}")
    text = payload.decode("utf-8")
    tree = ast.parse(text)
    functions = {
        node.name: node
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    missing = sorted(set(REFINEMENT_FUNCTIONS) - functions.keys())
    findings: dict[str, list[str]] = {}
    for name in REFINEMENT_FUNCTIONS:
        node = functions.get(name)
        if node is None:
            continue
        segment = ast.get_source_segment(text, node) or ""
        hits = sorted(token for token in FORBIDDEN_REFINEMENT_NAMES if token in segment)
        if hits:
            findings[name] = hits

    validate_node = functions.get("validate_row")
    validate_segment = ast.get_source_segment(text, validate_node) if validate_node else ""
    fallback_call = validate_segment.find("refine_state_via_specular_stationarity(")
    target_read = validate_segment.find('source_trace = mp.mpf(row["monodromy_trace"])')
    selection_precedes_comparison_assignment = (
        fallback_call >= 0 and target_read >= 0 and fallback_call < target_read
    )
    return {
        "round3_source_sha256": source_digest,
        "functions_checked": list(REFINEMENT_FUNCTIONS),
        "missing_functions": missing,
        "forbidden_target_name_findings": findings,
        "fallback_call_precedes_paraxial_comparison_assignment": (
            selection_precedes_comparison_assignment
        ),
        "fallback_selector_uses_paraxial_target": bool(
            missing or findings or not selection_precedes_comparison_assignment
        ),
        "audit_kind": "STATIC_SOURCE_DEPENDENCY_AND_STATEMENT_ORDER_CHECK",
        "audit_boundary": (
            "IMPLEMENTATION_PATH_CHECK_ONLY;NOT_A_PROOF_OF_STATISTICAL_UNBIASEDNESS"
        ),
    }


def maximum(rows: Sequence[dict[str, str]], field: str) -> Decimal:
    return max(Decimal(row[field]) for row in rows)


def build_length_rows(rows: Sequence[dict[str, str]]) -> list[dict[str, str]]:
    grouped: dict[int, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[int(row["topological_word_length"])].append(row)

    output: list[dict[str, str]] = []
    for length in sorted(grouped):
        group = grouped[length]
        traces = sorted(abs(Decimal(row["source_paraxial_trace"])) for row in group)
        fallback_count = sum(row["refinement_method"] == FALLBACK_METHOD for row in group)
        output.append(
            {
                "topological_word_length": str(length),
                "row_count": str(len(group)),
                "odd_length_rows": str(sum(length % 2 for _ in group)),
                "round2_open_rows": str(
                    sum(row["source_round2_fd_status"] == "OPEN" for row in group)
                ),
                "round3_certified_rows": str(
                    sum(row["validation_status"] == "NUMERICALLY_CERTIFIED" for row in group)
                ),
                "direct_newton_rows": str(
                    sum(row["refinement_method"] == DIRECT_METHOD for row in group)
                ),
                "stationarity_fallback_rows": str(fallback_count),
                "fallback_fraction": f"{fallback_count}/{len(group)}",
                "fallback_rate_decimal": f"{Decimal(fallback_count) / Decimal(len(group)):.15f}",
                "abs_paraxial_trace_min": decimal_text(min(traces)),
                "abs_paraxial_trace_median": decimal_text(median(traces)),
                "abs_paraxial_trace_max": decimal_text(max(traces)),
                "pre_refinement_return_residual_max": decimal_text(
                    maximum(group, "pre_refinement_return_residual")
                ),
                "post_refinement_return_residual_max": decimal_text(
                    maximum(group, "post_refinement_return_residual")
                ),
                "multiscale_trace_relative_span_max": decimal_text(
                    maximum(group, "multiscale_trace_relative_span")
                ),
                "fine_determinant_residual_max": decimal_text(
                    maximum(group, "determinant_residual_h1e_36")
                ),
                "parity_trace_relative_residual_max": decimal_text(
                    maximum(group, "parity_corrected_trace_relative_residual")
                ),
                "half_density_relative_residual_max": decimal_text(
                    maximum(group, "half_density_relative_residual")
                ),
            }
        )
    return output


def build_fallback_rows(rows: Sequence[dict[str, str]]) -> list[dict[str, str]]:
    output: list[dict[str, str]] = []
    for row in rows:
        if row["refinement_method"] != FALLBACK_METHOD:
            continue
        trace = abs(Decimal(row["source_paraxial_trace"]))
        output.append(
            {
                "row_id": row["row_id"],
                "d_over_a": row["d_over_a"],
                "topological_word_length": row["topological_word_length"],
                "cyclic_word": row["cyclic_word"],
                "source_round2_fd_status": row["source_round2_fd_status"],
                "abs_source_paraxial_trace": decimal_text(trace),
                "source_trace_condition_tier": condition_tier(trace),
                "pre_refinement_return_residual": row[
                    "pre_refinement_return_residual"
                ],
                "fallback_stationarity_residual": row[
                    "fallback_stationarity_residual"
                ],
                "post_refinement_return_residual": row[
                    "post_refinement_return_residual"
                ],
                "multiscale_trace_relative_span": row[
                    "multiscale_trace_relative_span"
                ],
                "fine_determinant_residual": row["determinant_residual_h1e_36"],
                "parity_corrected_trace_relative_residual": row[
                    "parity_corrected_trace_relative_residual"
                ],
                "half_density_relative_residual": row[
                    "half_density_relative_residual"
                ],
                "round3_validation_status": row["validation_status"],
                "round3_failure_tier": row["failure_tier"],
                "fallback_selector_uses_paraxial_target": "false",
                "fallback_selector_uses_prime_or_zero_data": "false",
                "evidence_status": "NUMERICALLY_CERTIFIED",
            }
        )
    return output


def acceptance_checks(rows: Sequence[dict[str, str]]) -> dict[str, bool]:
    return {
        "all_rows_round3_certified": all(
            row["validation_status"] == "NUMERICALLY_CERTIFIED" for row in rows
        ),
        "all_failure_tiers_none": all(row["failure_tier"] == "NONE" for row in rows),
        "post_refinement_residuals_below_limit": all(
            Decimal(row["post_refinement_return_residual"]) <= POST_LIMIT for row in rows
        ),
        "multiscale_spans_below_limit": all(
            Decimal(row["multiscale_trace_relative_span"]) <= SPAN_LIMIT for row in rows
        ),
        "fine_determinant_residuals_below_limit": all(
            Decimal(row["determinant_residual_h1e_36"]) <= DET_LIMIT for row in rows
        ),
        "parity_trace_residuals_below_limit": all(
            Decimal(row["parity_corrected_trace_relative_residual"]) <= TRACE_LIMIT
            for row in rows
        ),
        "half_density_residuals_below_limit": all(
            Decimal(row["half_density_relative_residual"]) <= HALF_DENSITY_LIMIT
            for row in rows
        ),
    }


def build_metrics(
    rows: Sequence[dict[str, str]], source_audit: dict[str, object], input_sha: str
) -> dict[str, object]:
    fallback = [row for row in rows if row["refinement_method"] == FALLBACK_METHOD]
    direct = [row for row in rows if row["refinement_method"] == DIRECT_METHOD]
    by_length = Counter(int(row["topological_word_length"]) for row in fallback)
    by_distance = Counter(row["d_over_a"] for row in fallback)
    by_tier = Counter(
        condition_tier(Decimal(row["source_paraxial_trace"])) for row in fallback
    )
    checks = acceptance_checks(rows)
    claims = {
        "fallback_rows_all_round2_open": all(
            row["source_round2_fd_status"] == "OPEN" for row in fallback
        ),
        "fallback_rows_only_lengths_11_or_12": all(
            int(row["topological_word_length"]) in {11, 12} for row in fallback
        ),
        "fallback_rows_all_abs_trace_gt_1e9": all(
            abs(Decimal(row["source_paraxial_trace"])) > Decimal("1e9")
            for row in fallback
        ),
        "fallback_rows_share_round3_acceptance_contract": all(checks.values()),
        "fallback_selection_path_target_free": not source_audit[
            "fallback_selector_uses_paraxial_target"
        ],
    }
    if not all(checks.values()) or not all(claims.values()):
        raise RuntimeError("Round-4 conditioning contract failed")
    return {
        "schema": "p25_round4_conditioning_audit/1.0",
        "candidate_id": CANDIDATE_ID,
        "date": DATE,
        "status": "PASS",
        "input_round3_ledger_sha256": input_sha,
        "input_rows": len(rows),
        "direct_newton_rows": len(direct),
        "stationarity_fallback_rows": len(fallback),
        "fallback_by_topological_length": {
            str(key): by_length[key] for key in sorted(by_length)
        },
        "fallback_by_distance_ratio": {
            key: by_distance[key] for key in sorted(by_distance, key=Decimal)
        },
        "fallback_by_source_trace_condition_tier": {
            key: by_tier[key] for key in sorted(by_tier)
        },
        "fallback_pre_refinement_residual_range": [
            decimal_text(min(Decimal(row["pre_refinement_return_residual"]) for row in fallback)),
            decimal_text(max(Decimal(row["pre_refinement_return_residual"]) for row in fallback)),
        ],
        "fallback_post_refinement_residual_max": decimal_text(
            maximum(fallback, "post_refinement_return_residual")
        ),
        "fallback_stationarity_residual_max": decimal_text(
            maximum(fallback, "fallback_stationarity_residual")
        ),
        "fallback_half_density_relative_residual_max": decimal_text(
            maximum(fallback, "half_density_relative_residual")
        ),
        "acceptance_checks": checks,
        "descriptive_claim_checks": claims,
        "source_dependency_audit": source_audit,
        "evidence_status": "NUMERICALLY_CERTIFIED",
        "inference_boundary": (
            "POST_HOC_DESCRIPTIVE_CONDITIONING_AUDIT;NO_CAUSAL_OR_SAMPLING_"
            "UNBIASEDNESS_CLAIM"
        ),
        "half_density_evidence_status": "NUMERICAL_OBSERVATION",
        "half_density_control_verdict": "STOP_SCOPED / PROVES_TOO_MUCH",
        "formal_route_a_tuple": "UNASSIGNED",
        "a2_evaluation": "NOT_RUN",
        "route_b_evaluation": "NOT_RUN",
        "route_b_invocation_allowed": False,
        "prime_or_zero_tables_used": False,
    }


def csv_payload(fields: Sequence[str], rows: Iterable[dict[str, str]]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def json_payload(value: object) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode("utf-8")


def build_outputs(project_root: Path) -> dict[str, bytes]:
    rows, input_sha = read_rows(project_root)
    source_audit = refinement_source_audit(project_root)
    length_rows = build_length_rows(rows)
    fallback_rows = build_fallback_rows(rows)
    metrics = build_metrics(rows, source_audit, input_sha)
    return {
        "round4_conditioning_by_length.csv": csv_payload(LENGTH_FIELDS, length_rows),
        "round4_fallback_audit.csv": csv_payload(FALLBACK_FIELDS, fallback_rows),
        "round4_conditioning_metrics.json": json_payload(metrics),
    }


def write_outputs(output_dir: Path, outputs: dict[str, bytes]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for name, payload in outputs.items():
        (output_dir / name).write_bytes(payload)


def combined_hash(outputs: dict[str, bytes]) -> str:
    digest = hashlib.sha256()
    for name in sorted(outputs):
        digest.update(name.encode("utf-8"))
        digest.update(b"\0")
        digest.update(outputs[name])
        digest.update(b"\0")
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    project_root = Path(__file__).resolve().parents[1]
    outputs = build_outputs(project_root)
    write_outputs(args.output_dir, outputs)
    print(
        json.dumps(
            {
                "status": "PASS",
                "output_count": len(outputs),
                "combined_sha256": combined_hash(outputs),
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
