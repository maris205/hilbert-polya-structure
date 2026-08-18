#!/usr/bin/env python3
"""Validate P46 State-A outputs and emit the writer-side science summary.

The script never writes its input tree.  It accepts a canonical `outputs/`
directory, verifies its self-described result ledger and all JSON
serialization, rechecks the exact cross-lane science surface, and writes only
the two caller-selected writer artifacts.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


EXPECTED_LEDGER_SHA256 = (
    "fa22dde6ec3a9cbd473528ebb619863ac7beb0d1c9cc807394541501153add37"
)
EXPECTED_ROWS = [
    "outputs/audits/external_auditor_mutations.json",
    "outputs/audits/independence_audit.json",
    "outputs/audits/proof_audit.json",
    "outputs/audits/route_independent.json",
    "outputs/audits/route_primary.json",
    "outputs/audits/source_audit.json",
    "outputs/audits/type_audit.json",
    "outputs/data/source_packet.json",
    "outputs/evaluations/route_a/SD-C48/2026-08-18.yaml",
    "outputs/reports/EXPERIMENT_REPORT.md",
    "outputs/results/evaluator_c.json",
    "outputs/results/evaluator_m.json",
    "outputs/results/exact_comparison.json",
    "outputs/tests/mutation_results.json",
]


def sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


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


def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in pairs:
        if key in out:
            raise ValueError(f"duplicate JSON key: {key}")
        out[key] = value
    return out


def load_json(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    value = json.loads(raw.decode("ascii"), object_pairs_hook=unique)
    if raw != canonical(value):
        raise ValueError(f"noncanonical JSON: {path}")
    if not isinstance(value, dict):
        raise ValueError(f"non-object envelope: {path}")
    return value


def strict_equal(left: Any, right: Any) -> bool:
    if type(left) is not type(right):
        return False
    if isinstance(left, dict):
        return list(left) == list(right) and all(
            strict_equal(left[key], right[key]) for key in left
        )
    if isinstance(left, list):
        return len(left) == len(right) and all(
            strict_equal(a, b) for a, b in zip(left, right)
        )
    return left == right


def require_pass(value: dict[str, Any], schema: str) -> dict[str, Any]:
    if list(value) != ["payload", "schema", "status"]:
        raise ValueError(f"unexpected envelope keys for {schema}")
    if value["schema"] != schema or value["status"] != "PASS":
        raise ValueError(f"failed or wrong schema: {schema}")
    if not isinstance(value["payload"], dict):
        raise ValueError(f"non-object payload: {schema}")
    return value["payload"]


def path_below(output_root: Path, ledger_path: str) -> Path:
    prefix = "outputs/"
    if not ledger_path.startswith(prefix):
        raise ValueError("ledger path outside outputs")
    relative = ledger_path[len(prefix) :]
    if not relative or relative.startswith("/") or ".." in relative.split("/"):
        raise ValueError("unsafe ledger path")
    base = output_root.resolve(strict=True)
    cursor = output_root
    for part in relative.split("/"):
        cursor /= part
        if cursor.is_symlink():
            raise ValueError(f"symlink in ledger path: {ledger_path}")
    final = cursor.resolve(strict=True)
    if base not in final.parents or not final.is_file():
        raise ValueError(f"ledger containment failure: {ledger_path}")
    return final


def validate_ledger(output_root: Path) -> tuple[dict[str, str], str]:
    ledger_path = output_root / "RESULT_LEDGER.json"
    raw = ledger_path.read_bytes()
    if sha256(raw) != EXPECTED_LEDGER_SHA256:
        raise ValueError("unexpected State-A result-ledger digest")
    ledger = load_json(ledger_path)
    payload = require_pass(ledger, "paper46-result-ledger-v1")
    if payload.get("state") != "A" or payload.get("entry_count") != 14:
        raise ValueError("not exact State A")
    rows = payload.get("rows")
    if not isinstance(rows, list) or len(rows) != 14:
        raise ValueError("ledger row count")
    paths = [row.get("path") for row in rows if isinstance(row, dict)]
    if paths != EXPECTED_ROWS:
        raise ValueError("ledger path order/domain mismatch")
    hashes: dict[str, str] = {}
    for row in rows:
        if list(row) != ["path", "sha256"]:
            raise ValueError("ledger row key set")
        path = path_below(output_root, row["path"])
        actual = sha256(path.read_bytes())
        if actual != row["sha256"]:
            raise ValueError(f"ledger digest mismatch: {row['path']}")
        hashes[row["path"]] = actual
    return hashes, sha256(raw)


def validate_all_json(output_root: Path) -> None:
    for path in sorted(output_root.rglob("*.json")):
        if path.is_symlink() or not path.is_file():
            raise ValueError(f"unsafe JSON path: {path}")
        load_json(path)


def science_projection(payload: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in payload.items() if key != "implementation_lane"}


def build_summary(output_root: Path, hashes: dict[str, str], ledger_sha: str) -> dict[str, Any]:
    matrix = require_pass(
        load_json(output_root / "results/evaluator_m.json"), "paper46-evaluator-m-v1"
    )
    cyclic = require_pass(
        load_json(output_root / "results/evaluator_c.json"), "paper46-evaluator-c-v1"
    )
    if matrix.get("implementation_lane") != (
        "M_LITERAL_BIT_PREDICATE_MATRIX_AND_DIRECT_BOUNDED_WALKS"
    ):
        raise ValueError("matrix lane identity")
    if cyclic.get("implementation_lane") != (
        "C_ANTI_DIAGONAL_VALUATION_AND_ALGEBRAIC_CYCLIC_SOLVER"
    ):
        raise ValueError("cyclic lane identity")
    if not strict_equal(science_projection(matrix), science_projection(cyclic)):
        raise ValueError("strict science projection mismatch")

    comparison = require_pass(
        load_json(output_root / "results/exact_comparison.json"),
        "paper46-exact-comparison-v1",
    )
    expected_counts = {
        "cycle_ordered_label_tuples": 335922,
        "finite_trace_cases": 36,
        "structural_cutoffs": 4,
    }
    if comparison.get("case_counts") != expected_counts:
        raise ValueError("comparison case counts")
    if any(
        type(comparison.get(key)) is not int or comparison[key] != 0
        for key in (
            "cycle_solution_mismatch_count",
            "finite_trace_mismatch_count",
            "support_mismatch_count",
        )
    ):
        raise ValueError("nonzero or ill-typed science mismatch")
    if comparison.get("strict_recursive_type_and_value_equal") is not True:
        raise ValueError("comparison strict equality false")
    if comparison.get("finite_trace_truncation") != (
        "SCALE_DEPENDENT_ODD_BLOCK_CUTOFF_NO_GEOMETRIC_COLLAPSE"
    ):
        raise ValueError("finite trace truncation policy")
    if comparison.get("evidence_boundary") != {
        "finite_evidence_type": "FINITE_EXACT_DIAGNOSTIC",
        "infinite_theorem_status": "NOT_INFERRED_FROM_FINITE_EVIDENCE",
    }:
        raise ValueError("finite/infinite evidence firewall")

    proof = require_pass(
        load_json(output_root / "audits/proof_audit.json"), "paper46-proof-audit-v1"
    )
    source = require_pass(
        load_json(output_root / "audits/source_audit.json"), "paper46-source-audit-v1"
    )
    types = require_pass(
        load_json(output_root / "audits/type_audit.json"), "paper46-type-audit-v1"
    )
    independence = require_pass(
        load_json(output_root / "audits/independence_audit.json"),
        "paper46-independence-audit-v1",
    )
    integrity = require_pass(
        load_json(output_root / "audits/integrity_audit.json"),
        "paper46-read-only-integrity-audit-v1",
    )
    mutations = require_pass(
        load_json(output_root / "tests/mutation_results.json"),
        "paper46-mutation-results-v1",
    )
    external = require_pass(
        load_json(output_root / "audits/external_auditor_mutations.json"),
        "paper46-external-auditor-mutations-v1",
    )
    route1 = require_pass(
        load_json(output_root / "audits/route_primary.json"),
        "paper46-route-primary-audit-v1",
    )
    route2 = require_pass(
        load_json(output_root / "audits/route_independent.json"),
        "paper46-route-independent-audit-v1",
    )

    if proof.get("theorem_failure_count") != 0 or proof.get("finite_grid_used_as_proof") is not False:
        raise ValueError("proof audit failure")
    if source.get("priority_claimed") is not False or source.get("fournier_wagner_novelty_credit") != 0:
        raise ValueError("source ownership failure")
    if types.get("recursive_scalar_type_failures") != 0:
        raise ValueError("type audit failure")
    if integrity.get("checks_passed") != 16 or integrity.get("checks_total") != 16:
        raise ValueError("integrity audit failure")
    if mutations.get("instance_count") != 62 or mutations.get("family_count") != 25 \
            or mutations.get("consumer_invocation_count") != 162 \
            or mutations.get("survivor_count") != 0:
        raise ValueError("mutation closeout failure")
    if external.get("physical_mutated_clone_count") != 13 \
            or external.get("physical_consumer_invocation_count") != 22 \
            or external.get("accepted_mutation_count") != 0:
        raise ValueError("external mutation closeout failure")
    if route1.get("normalized_route_sha256") != route2.get("normalized_route_sha256"):
        raise ValueError("Route auditor disagreement")

    finite = matrix["finite_endpoint_diagnostics"]
    trace = matrix["finite_trace_certificate"]
    summary = {
        "payload": {
            "candidate_id": "SD-C48",
            "canonical_input": {
                "result_ledger_sha256": ledger_sha,
                "science_projection_sha256": comparison["science_projection_sha256"],
                "selected_file_sha256": hashes,
                "state": "A",
            },
            "comparison": comparison,
            "cycle": {
                "direct_vertex_bound": matrix["cycle_certificate"]["direct_vertex_bound"],
                "length_records": matrix["cycle_certificate"]["length_records"],
                "ordered_tuple_policy": matrix["cycle_certificate"]["ordered_tuple_policy"],
                "witnesses": matrix["cycle_certificate"]["witnesses"],
            },
            "endpoint_diagnostics": {
                "evidence_type": finite["evidence_type"],
                "hs_sigma_one_level_record_count": len(finite["hs_sigma_one_level_records"]),
                "hs_sigma_one_level_records_sha256": sha256(
                    canonical(finite["hs_sigma_one_level_records"])
                ),
                "row_one_sigma_zero_partial_sum_a_le_16": finite[
                    "row_one_sigma_zero_partial_sum_a_le_16"
                ],
                "theorem_endpoint_verdicts": finite["theorem_endpoint_verdicts"],
            },
            "independence": independence,
            "integrity": integrity,
            "mutation_closeout": {
                "consumer_invocation_count": mutations["consumer_invocation_count"],
                "family_count": mutations["family_count"],
                "instance_count": mutations["instance_count"],
                "survivor_count": mutations["survivor_count"],
                "external_accepted_mutation_count": external["accepted_mutation_count"],
                "external_physical_consumer_invocation_count": external[
                    "physical_consumer_invocation_count"
                ],
                "external_physical_mutated_clone_count": external[
                    "physical_mutated_clone_count"
                ],
            },
            "proof": proof,
            "route": {
                "independent_checks": [route2["checks_passed"], route2["checks_total"]],
                "normalized_route_sha256": route1["normalized_route_sha256"],
                "primary_checks": [route1["checks_passed"], route1["checks_total"]],
                "route_b_invocation_allowed": route1["route_b_invocation_allowed"],
                "route_tuple": route1["route_tuple"],
            },
            "source": source,
            "structural_records": matrix["structural_certificate"]["records"],
            "trace_replay": {
                "formula": trace["formula"],
                "record_count": len(trace["records"]),
                "records_sha256": sha256(canonical(trace["records"])),
                "truncation_policy": trace["truncation_policy"],
            },
            "types": types,
        },
        "schema": "paper46-writer-canonical-summary-v1",
        "status": "PASS",
    }
    return summary


def render_ledger(summary: dict[str, Any]) -> str:
    p = summary["payload"]
    c = p["comparison"]
    m = p["mutation_closeout"]
    proof = p["proof"]
    source = p["source"]
    route = p["route"]
    rows = [
        "# P46 canonical State-A results ledger",
        "",
        "This writer-side ledger was mechanically regenerated from the protected",
        "canonical State-A snapshot. It reports implementation replay separately",
        "from analytic proof and does not claim external priority.",
        "",
        "## Bound input",
        "",
        f"- Result-ledger SHA-256: `{p['canonical_input']['result_ledger_sha256']}`",
        f"- Science projection SHA-256: `{p['canonical_input']['science_projection_sha256']}`",
        "- Provenance state: `A` (all commit fields remain pending; no paper manifest)",
        "",
        "## Exact finite replay",
        "",
        "| Surface | Canonical cases | Mismatches |",
        "|---|---:|---:|",
        f"| complete support cutoffs | {c['case_counts']['structural_cutoffs']} | {c['support_mismatch_count']} |",
        f"| ordered dyadic label tuples | {c['case_counts']['cycle_ordered_label_tuples']} | {c['cycle_solution_mismatch_count']} |",
        f"| exact rational finite traces | {c['case_counts']['finite_trace_cases']} | {c['finite_trace_mismatch_count']} |",
        "",
        f"Strict recursive type-and-value equality: `{str(c['strict_recursive_type_and_value_equal']).lower()}`.",
        f"Finite evidence type: `{c['evidence_boundary']['finite_evidence_type']}`; infinite",
        f"status: `{c['evidence_boundary']['infinite_theorem_status']}`.",
        "Finite traces retain a scale-dependent odd cutoff and are never collapsed",
        "to the infinite geometric factor.",
        "",
        "## Analytic proof replay",
        "",
        f"The proof auditor replayed {proof['proof_anchor_count']} frozen anchors,",
        f"reported {proof['theorem_failure_count']} theorem failures, and recorded",
        f"finite-grid-as-proof as `{str(proof['finite_grid_used_as_proof']).lower()}`.",
        "Its certificate covers the strict `0`, `1/2`, and `1` walls, the exact",
        "valuation direct sum, the odd/even cycle classification, and the separately",
        "typed infinite trace identity.",
        "",
        "## Independence and adversarial closeout",
        "",
        f"The evaluator source digests are distinct (`{p['independence']['evaluator_m_sha256']}`",
        f"and `{p['independence']['evaluator_c_sha256']}`), with no project-local",
        "imports, shared expanded fixtures, or serialized intermediates.",
        f"All {m['instance_count']} mutations in {m['family_count']} families were",
        f"rejected across {m['consumer_invocation_count']} designated invocations;",
        f"survivors: `{m['survivor_count']}`. The frozen external audit rejected all",
        f"{m['external_physical_mutated_clone_count']} physical clones across",
        f"{m['external_physical_consumer_invocation_count']} invocations.",
        "",
        "## Source and Route boundary",
        "",
        f"Fournier--Wagner novelty credit is `{source['fournier_wagner_novelty_credit']}`;",
        f"priority claimed is `{str(source['priority_claimed']).lower()}`; bounded-search",
        f"disposition is `{source['search_disposition']}`.",
        f"The two Route validators passed {route['primary_checks'][0]}/{route['primary_checks'][1]} and",
        f"{route['independent_checks'][0]}/{route['independent_checks'][1]} checks and agree on",
        "`[A0_WEAK_ARITHMETIC_RELATION, A1_PASS_ANALYTIC,",
        "A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL]`.",
        "Route B remains locked.",
        "",
        "## Use in the manuscript",
        "",
        "These results support statements about exact implementation agreement and",
        "reproducibility. Infinite operator thresholds, determinant legality, and the",
        "cycle theorem are established by the manuscript's proofs; this ledger is not",
        "used to infer an endpoint, novelty, rational-prime emergence, or a target divisor.",
        "",
    ]
    return "\n".join(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-root", required=True)
    parser.add_argument("--summary", required=True)
    parser.add_argument("--ledger", required=True)
    args = parser.parse_args()
    output_root = Path(args.output_root)
    if not output_root.is_absolute() or output_root.is_symlink() or not output_root.is_dir():
        raise ValueError("unsafe output root")
    validate_all_json(output_root)
    hashes, ledger_sha = validate_ledger(output_root)
    summary = build_summary(output_root, hashes, ledger_sha)
    Path(args.summary).write_bytes(canonical(summary))
    Path(args.ledger).write_text(render_ledger(summary), encoding="utf-8", newline="\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
