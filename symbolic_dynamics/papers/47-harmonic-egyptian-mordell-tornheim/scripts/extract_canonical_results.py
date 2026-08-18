#!/usr/bin/env python3
"""Extract a small, hash-verified P47 writer summary from canonical State A."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import stat
from pathlib import Path
from typing import Any


EXPECTED_CHECKS = [
    "based_closed_walks",
    "coprime_coordinate_bijection",
    "endpoint_and_complex_phase_controls",
    "exact_trace_powers_1_through_5",
    "finite_evidence_class",
    "first_trace_even_harmonic",
    "full_divisor_rows",
    "literal_matrices",
    "negative_principal_minor",
    "ordered_support_quotients_loops",
    "rectangular_primitive_mt_gcd_extraction",
    "second_trace_termwise_finite_cutoff",
]
EXPECTED_AUDITS = [
    "audits/external_auditor_mutations.json",
    "audits/frozen_static_audit.json",
    "audits/independence_audit.json",
    "audits/integrity_audit.json",
    "audits/literature_audit.json",
    "audits/proof_result_audit.json",
    "audits/route_independent.json",
    "audits/route_primary.json",
    "audits/runtime_controls.json",
    "audits/source_audit.json",
    "audits/type_audit.json",
]


def canonical(value: Any) -> bytes:
    return (
        json.dumps(
            value,
            sort_keys=True,
            indent=2,
            ensure_ascii=True,
            allow_nan=False,
            separators=(",", ": "),
        )
        + "\n"
    ).encode("ascii")


def pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in items:
        if key in value:
            raise ValueError("duplicate JSON key")
        value[key] = item
    return value


def load(path: Path, require_pass: bool = True) -> tuple[dict[str, Any], bytes]:
    raw = path.read_bytes()
    value = json.loads(raw.decode("ascii"), object_pairs_hook=pairs)
    if type(value) is not dict or raw != canonical(value):
        raise SystemExit(f"NONCANONICAL_JSON:{path.name}")
    if require_pass and value.get("status") != "PASS":
        raise SystemExit(f"NONPASS_JSON:{path.name}")
    return value, raw


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def tree_rows(root: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in root.rglob("*"):
        relative = path.relative_to(root).as_posix()
        info = os.lstat(path)
        mode = f"{stat.S_IMODE(info.st_mode):04o}"
        if stat.S_ISDIR(info.st_mode):
            rows.append({"kind": "directory", "mode": mode, "path": relative})
        elif stat.S_ISREG(info.st_mode):
            rows.append({
                "kind": "regular",
                "mode": mode,
                "path": relative,
                "sha256": sha(path.read_bytes()),
            })
        else:
            raise SystemExit("NONREGULAR_OUTPUT_NODE")
    return sorted(rows, key=lambda row: row["path"])


def rational_text(value: dict[str, Any]) -> str:
    if set(value) != {"denominator", "numerator"}:
        raise SystemExit("RATIONAL_SHAPE")
    numerator = value["numerator"]
    denominator = value["denominator"]
    if type(numerator) is not int or type(denominator) is not int or denominator <= 0:
        raise SystemExit("RATIONAL_TYPE")
    return f"{numerator}/{denominator}"


def write_exclusive(path: Path, raw: bytes, writer_root: Path) -> None:
    if not path.is_absolute() or writer_root not in path.parents:
        raise SystemExit("OUTPUT_OUTSIDE_WRITER_ROOT")
    if path.parent.resolve(strict=True) != path.parent or os.path.lexists(path):
        raise SystemExit("OUTPUT_NOT_NEW")
    descriptor = os.open(
        path,
        os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0),
        0o644,
    )
    try:
        os.fchmod(descriptor, 0o644)
        offset = 0
        while offset < len(raw):
            offset += os.write(descriptor, raw[offset:])
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def build(authority: Path) -> bytes:
    output = authority / "outputs"
    seal, seal_raw = load(authority / "PREOUTPUT_STATIC_SEAL.json", require_pass=False)
    if seal.get("status") != "HOLD_FOR_INDEPENDENT_AUDIT":
        raise SystemExit("STATIC_SEAL_STATUS")
    observed_tree = sha(canonical(tree_rows(output)))
    if observed_tree != seal["smoke"]["state_A_final_tree_sha256"]:
        raise SystemExit("STATEA_TREE_HASH")

    ledger, ledger_raw = load(output / "RESULT_LEDGER.json")
    if ledger["payload"].get("state") != "A":
        raise SystemExit("LEDGER_STATE")
    if sha(ledger_raw) != seal["smoke"]["result_ledger_sha256"]:
        raise SystemExit("LEDGER_SEAL_HASH")
    for row in ledger["payload"]["rows"]:
        if row["kind"] == "regular":
            path = output / row["path"]
            if not path.is_file() or sha(path.read_bytes()) != row["sha256"]:
                raise SystemExit(f"LEDGER_ROW_HASH:{row['path']}")

    direct, direct_raw = load(output / "results" / "evaluator_d.json")
    parameter, parameter_raw = load(output / "results" / "evaluator_p.json")
    comparison, comparison_raw = load(output / "results" / "exact_comparison.json")
    if comparison["payload"]["direct_sha256"] != sha(direct_raw):
        raise SystemExit("DIRECT_HASH")
    if comparison["payload"]["parameter_sha256"] != sha(parameter_raw):
        raise SystemExit("PARAMETER_HASH")
    checks = comparison["payload"]["checks"]
    if list(checks) != EXPECTED_CHECKS or any(value != "PASS" for value in checks.values()):
        raise SystemExit("COMPARISON_CHECKS")

    direct_cutoffs = direct["payload"]["cutoffs"]
    parameter_cutoffs = parameter["payload"]["cutoffs"]
    if direct_cutoffs != parameter_cutoffs:
        raise SystemExit("CUTOFF_DISAGREEMENT")
    cutoff_summary = []
    for row in direct_cutoffs:
        cutoff_summary.append({
            "N": row["N"],
            "loop_count": len(row["loops"]),
            "ordered_edge_count": len(row["ordered_edges"]),
        })
    if cutoff_summary != [
        {"N": 16, "loop_count": 8, "ordered_edge_count": 16},
        {"N": 32, "loop_count": 16, "ordered_edge_count": 40},
        {"N": 64, "loop_count": 32, "ordered_edge_count": 96},
        {"N": 128, "loop_count": 64, "ordered_edge_count": 228},
    ]:
        raise SystemExit("CUTOFF_VALUES")

    direct_traces = {
        (row["N"], row["s"]): row for row in direct["payload"]["trace_summary"]
    }
    parameter_traces = {
        (row["N"], row["s"]): row for row in parameter["payload"]["trace_summary"]
    }
    selected_traces = []
    for s in (2, 4):
        drow = direct_traces[(128, s)]
        prow = parameter_traces[(128, s)]
        first = drow["trace_1_direct_diagonal"]
        second = drow["trace_2_direct_ordered_edges"]
        if first != prow["trace_1_even_harmonic"]:
            raise SystemExit("FIRST_TRACE_DISAGREEMENT")
        if second != prow["trace_2_parameter_ordered_edges"] \
                or second != prow["trace_2_termwise_scale_cutoff"]:
            raise SystemExit("SECOND_TRACE_DISAGREEMENT")
        selected_traces.append({
            "N": 128,
            "s": s,
            "trace_1": rational_text(first),
            "trace_2": rational_text(second),
        })

    audit_hashes: dict[str, str] = {}
    audit_schemas: dict[str, str] = {}
    audit_objects: dict[str, dict[str, Any]] = {}
    for relative in EXPECTED_AUDITS:
        value, raw = load(output / relative)
        audit_hashes[relative] = sha(raw)
        audit_schemas[relative] = value["schema"]
        audit_objects[relative] = value

    mutation, mutation_raw = load(output / "tests" / "mutation_results.json")
    expanded, expanded_raw = load(output / "tests" / "expanded_mutation_results.json")
    external = audit_objects["audits/external_auditor_mutations.json"]
    if (
        mutation["payload"]["survivors"] != 0
        or expanded["payload"]["survivors"] != 0
        or external["payload"]["survivors"] != 0
    ):
        raise SystemExit("MUTATION_SURVIVOR")

    route, route_raw = load(
        output / "evaluations" / "route_a" / "SD-C49" / "2026-08-18.json",
        require_pass=False,
    )
    if route.get("overall_verdict") != "ROUTE_A_REJECTED":
        raise SystemExit("ROUTE_VERDICT")
    if route.get("route_b_invocation_allowed") is not False:
        raise SystemExit("ROUTE_B")
    expected_tuple = [
        "A0_ANALYTIC_ARITHMETIC_ORIGIN",
        "A1_PASS_ANALYTIC",
        "A2_ANALYTIC_DETERMINANT",
        "A3_PARTIAL_ANALYTIC_STRUCTURE",
        "A4_FAIL",
    ]
    if route.get("route_tuple") != expected_tuple:
        raise SystemExit("ROUTE_TUPLE")

    report_raw = (output / "reports" / "EXPERIMENT_REPORT.md").read_bytes()
    if sha(report_raw) != seal["smoke"]["report_sha256"]:
        raise SystemExit("REPORT_HASH")

    endpoint = parameter["payload"]["endpoint_controls"]
    phase = parameter["payload"]["phase_certificate"]
    if phase != {
        "bounded_compact": "Re_s_gt_0",
        "det2": "Re_s_gt_one_half",
        "hilbert_schmidt": "Re_s_gt_one_half",
        "ordinary_determinant": "Re_s_gt_1",
        "proof_owner": "preauthority/PROOF_PACKAGE.md",
        "trace_class": "Re_s_gt_1",
    }:
        raise SystemExit("PHASE_CERTIFICATE")

    summary = {
        "candidate_id": "SD-C49",
        "payload": {
            "audits": {
                "hashes": audit_hashes,
                "schemas": audit_schemas,
                "status": "ALL_PASS",
            },
            "canonical_hashes": {
                "comparison_sha256": sha(comparison_raw),
                "direct_sha256": sha(direct_raw),
                "expanded_mutations_sha256": sha(expanded_raw),
                "parameter_sha256": sha(parameter_raw),
                "report_sha256": sha(report_raw),
                "result_ledger_sha256": sha(ledger_raw),
                "route_sha256": sha(route_raw),
                "state_a_output_tree_sha256": observed_tree,
                "static_seal_sha256": sha(seal_raw),
                "theorem_mutations_sha256": sha(mutation_raw),
            },
            "comparison_checks": checks,
            "cutoffs": cutoff_summary,
            "evidence_class": direct["payload"]["evidence_class"],
            "finite_trace_controls": selected_traces,
            "mixed_triangle": [15, 30, 60],
            "mutation_controls": {
                "expanded_consumer_invocations": expanded["payload"]["consumer_invocation_count"],
                "expanded_instances": expanded["payload"]["instance_count"],
                "external_instances": external["payload"]["instance_count"],
                "survivors": 0,
                "theorem_consumer_invocations": mutation["payload"]["consumer_invocation_count"],
                "theorem_instances": mutation["payload"]["instance_count"],
            },
            "negative_principal_minor_controls": direct["payload"]["negative_minor"],
            "operator_phase_certificate": phase,
            "proof_boundary": {
                "analytic_certificates": audit_objects["audits/proof_result_audit.json"]["payload"]["analytic_certificates"],
                "finite_results_role": audit_objects["audits/proof_result_audit.json"]["payload"]["finite_results_role"],
                "strict_endpoint_witnesses": endpoint["strict_endpoint_witnesses"],
            },
            "route": {
                "overall_verdict": route["overall_verdict"],
                "route_b_invocation_allowed": route["route_b_invocation_allowed"],
                "route_tuple": route["route_tuple"],
                "terminal_codes": route["terminal_codes"],
            },
            "source_and_ownership": {
                "literature_disposition": audit_objects["audits/literature_audit.json"]["payload"]["disposition"],
                "novelty_boundary": audit_objects["audits/literature_audit.json"]["payload"]["novelty_boundary"],
                "paper46_generated_inputs": audit_objects["audits/source_audit.json"]["payload"]["paper46_generated_inputs"],
                "priority_proved": False,
                "source_relation": audit_objects["audits/source_audit.json"]["payload"]["source_relation"],
            },
            "state": "A",
        },
        "schema": "paper47.writer-canonical-summary.v1",
        "status": "PASS",
    }
    return canonical(summary)


def main() -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--authority", required=True)
    parser.add_argument("--writer-root", required=True)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--write", action="store_true")
    action.add_argument("--check", action="store_true")
    args = parser.parse_args()
    authority = Path(args.authority)
    writer_root = Path(args.writer_root)
    if (
        not authority.is_absolute()
        or authority.is_symlink()
        or authority.resolve(strict=True) != authority
        or not writer_root.is_absolute()
        or writer_root.is_symlink()
        or writer_root.resolve(strict=True) != writer_root
    ):
        raise SystemExit("UNSAFE_ROOT")
    raw = build(authority)
    target = writer_root / "figures" / "data" / "canonical_summary.json"
    if args.write:
        write_exclusive(target, raw, writer_root)
        print(f"WROTE sha256={sha(raw)}")
        return 0
    if not target.is_file() or target.read_bytes() != raw:
        raise SystemExit("SUMMARY_MISMATCH")
    print(f"PASS sha256={sha(raw)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
