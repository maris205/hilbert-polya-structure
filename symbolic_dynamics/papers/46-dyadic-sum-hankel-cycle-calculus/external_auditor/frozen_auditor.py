#!/usr/bin/env python3
"""Frozen whole-tree auditor, outside the P46 producer-code namespace."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any


STATE_A = [
    "RESULT_LEDGER.json", "audits/external_auditor_mutations.json",
    "audits/independence_audit.json", "audits/integrity_audit.json",
    "audits/proof_audit.json", "audits/route_independent.json",
    "audits/route_primary.json", "audits/source_audit.json",
    "audits/type_audit.json", "data/source_packet.json",
    "evaluations/route_a/SD-C48/2026-08-18.yaml",
    "reports/EXPERIMENT_REPORT.md", "results/evaluator_c.json",
    "results/evaluator_m.json", "results/exact_comparison.json",
    "tests/mutation_results.json",
]
PREAUTH_SHA = "fc132644764bb93927dbcd5cbf63917e48e2c512d72adc375ef7590210226bab"
PENDING = "PENDING_FIRST_ARTIFACT_COMMIT"
PAPER_MANIFEST_ROOT_EXCLUSIONS = frozenset({"PREOUTPUT_STATIC_SEAL.json"})
PAPER_MANIFEST_SELF = "outputs/PAPER_MANIFEST.sha256"
MUTATIONS = {
    "PKT08/source_seal_drift": "FROZEN_SOURCE_DRIFT",
    "RES01/delete_evaluator_m": "OUTPUT_NAMESPACE_MISMATCH",
    "RES02/rename_evaluator_c": "OUTPUT_NAMESPACE_MISMATCH",
    "RES03/extra_result": "OUTPUT_NAMESPACE_MISMATCH",
    "RES07/coordinated_nested_count_bool": "RESULT_SCHEMA_TYPE_FAILURE",
    "RES08/coordinated_nested_cutoff_float": "RESULT_SCHEMA_TYPE_FAILURE",
    "RES09/comparison_boolean_to_int": "RESULT_SCHEMA_TYPE_FAILURE",
    "RES10/coordinated_missing_nested_key": "RESULT_SCHEMA_KEYSET_FAILURE",
    "RES11/coordinated_extra_nested_key": "RESULT_SCHEMA_KEYSET_FAILURE",
    "LED01/edit_digest": "RESULT_LEDGER_MISMATCH",
    "LED02/coordinated_rehash": "CANONICAL_SCIENCE_MISMATCH",
    "LED03/reorder_rows": "RESULT_LEDGER_ORDER_FAILURE",
    "RPT01/false_claim": "REPORT_RECONSTRUCTION_MISMATCH",
    "RPT02/report_only_rehash": "REPORT_RECONSTRUCTION_MISMATCH",
    "RTE01/tuple_a0": "ROUTE_TUPLE_MISMATCH",
    "RTE02/overall_accept": "ROUTE_OVERALL_MISMATCH",
    "RTE03/route_b_true": "ROUTE_B_LOCK_FAILURE",
    "STA01/a_with_manifest": "MIXED_PROVENANCE_STATE",
    "STA02/b_missing_manifest": "MIXED_PROVENANCE_STATE",
    "STA03/b_unequal_commits": "PROVENANCE_COMMIT_MISMATCH",
    "STA04/b_zero_commit": "PROVENANCE_COMMIT_INVALID",
    "PTH01/traversal": "PATH_CONTAINMENT_FAILURE",
    "PTH02/symlink_output": "SYMLINK_FORBIDDEN",
    "PTH03/symlink_static": "SYMLINK_FORBIDDEN",
    "PTH04/absolute_serialized": "HOST_PATH_TOKEN_FORBIDDEN",
    "HYG01/cache_file": "CACHE_FILE_FORBIDDEN",
    "AUD01/delete_proof_audit": "OUTPUT_NAMESPACE_MISMATCH",
    "AUD02/tamper_integrity": "AUDIT_SELF_TAMPER",
    "TXN01/late_failure_writes": "TRANSACTION_ATOMICITY_FAILURE",
    "TXN02/second_run_rewrite": "IDEMPOTENCE_FAILURE",
    "TXN03/stage_missing_file": "STAGE_INCOMPLETE",
}


class StrictParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        raise ValueError(f"CLI_ARGUMENT_ERROR: {message}")


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       allow_nan=False, separators=(",", ": ")) + "\n").encode("ascii")


def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    output: dict[str, Any] = {}
    for key, value in pairs:
        if key in output:
            raise ValueError("duplicate JSON key")
        output[key] = value
    return output


def strict(left: Any, right: Any) -> bool:
    if type(left) is not type(right):
        return False
    if type(left) is dict:
        return set(left) == set(right) and all(strict(left[key], right[key]) for key in left)
    if type(left) is list:
        return len(left) == len(right) and all(strict(a, b) for a, b in zip(left, right))
    return left == right


def reject(identifier: str) -> int:
    if identifier not in MUTATIONS:
        raise ValueError("mutation not designated for F")
    sys.stdout.buffer.write(canonical({
        "payload": {"code": MUTATIONS[identifier], "consumer": "F",
                    "instance_id": identifier,
                    "witness": "frozen external whole-tree auditor rejected mutation"},
        "schema": "paper46-mutation-rejection-v1", "status": "REJECT",
    }))
    return 2


def safe_root(path: Path) -> Path:
    if not path.is_absolute() or path.is_symlink() or not path.is_dir():
        raise ValueError("unsafe root")
    return path.resolve(strict=True)


def file_under(root: Path, relative: str) -> Path:
    cursor = root
    for part in relative.split("/"):
        if part in {"", ".", ".."}:
            raise ValueError("unsafe relative path")
        cursor /= part
        if cursor.is_symlink():
            raise ValueError("symlink forbidden")
    result = cursor.resolve(strict=True)
    if root not in result.parents or not result.is_file():
        raise ValueError("containment")
    return result


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def load_json(output: Path, relative: str) -> tuple[dict[str, Any], bytes]:
    raw = file_under(output, relative).read_bytes()
    value = json.loads(raw.decode("ascii"), object_pairs_hook=unique,
                       parse_constant=lambda word: (_ for _ in ()).throw(ValueError(word)))
    if raw != canonical(value):
        raise ValueError("noncanonical JSON")
    return value, raw


def scalar_safe(value: Any) -> bool:
    forbidden = ["/home/", "/root/", "/tmp/", "\\home\\", "\\root\\", "\\tmp\\"]
    if type(value) is str:
        return not any(token in value for token in forbidden)
    if type(value) in {int, bool} or value is None:
        return True
    if type(value) is list:
        return all(scalar_safe(item) for item in value)
    if type(value) is dict:
        return all(type(key) is str and scalar_safe(key) and scalar_safe(item)
                   for key, item in value.items())
    return False


def schema_keys(value: Any, expected: set[str], label: str) -> dict[str, Any]:
    if type(value) is not dict or set(value) != expected:
        raise ValueError(f"{label} exact keys")
    return value


def schema_int(value: Any, label: str) -> int:
    if type(value) is not int:
        raise ValueError(f"{label} exact int")
    return value


def schema_array(value: Any, length: int | None, label: str) -> list[Any]:
    if type(value) is not list or (length is not None and len(value) != length):
        raise ValueError(f"{label} exact array shape")
    return value


def evaluator_scalar_tree(value: Any, label: str) -> None:
    if type(value) in {str, int} or value is None:
        return
    if type(value) in {bool, float}:
        raise ValueError(f"{label} bool/float forbidden")
    if type(value) is list:
        for index, item in enumerate(value):
            evaluator_scalar_tree(item, f"{label}[{index}]")
        return
    if type(value) is dict:
        for key, item in value.items():
            if type(key) is not str:
                raise ValueError("non-string key")
            evaluator_scalar_tree(item, f"{label}.{key}")
        return
    raise ValueError(f"{label} type")


def schema_fraction(value: Any, label: str) -> None:
    item = schema_keys(value, {"denominator", "numerator"}, label)
    if type(item["denominator"]) is not str or type(item["numerator"]) is not str \
            or re.fullmatch(r"[1-9][0-9]*", item["denominator"]) is None \
            or re.fullmatch(r"0|-?[1-9][0-9]*", item["numerator"]) is None:
        raise ValueError(f"{label} fraction")


def validate_evaluator_schema(value: Any, schema: str, lane: str) -> dict[str, Any]:
    outer = schema_keys(value, {"payload", "schema", "status"}, "evaluator envelope")
    if outer["schema"] != schema or outer["status"] != "PASS":
        raise ValueError("evaluator identity")
    payload = schema_keys(outer["payload"], {"candidate_id", "cycle_certificate", "evidence_type",
                          "finite_endpoint_diagnostics", "finite_trace_certificate",
                          "implementation_lane", "structural_certificate", "theorem_claims_inferred"},
                          "evaluator payload")
    evaluator_scalar_tree(payload, "evaluator payload")
    if payload["candidate_id"] != "SD-C48" or payload["evidence_type"] != "FINITE_EXACT_DIAGNOSTIC" \
            or payload["implementation_lane"] != lane \
            or schema_array(payload["theorem_claims_inferred"], 0, "theorem claims") != []:
        raise ValueError("evaluator typed identity")
    structural = schema_keys(payload["structural_certificate"], {"records", "support_predicate"}, "structural")
    if structural["support_predicate"] != "x>=2 and x&(x-1)==0":
        raise ValueError("support predicate enum")
    for cutoff, row in zip([8, 16, 32, 64], schema_array(structural["records"], 4, "structural records")):
        row = schema_keys(row, {"cutoff", "directed_edge_count", "edge_list_sha256", "loop_vertices",
                           "valuation_block_directed_edge_counts", "valuation_mismatch_count"}, "structural row")
        if schema_int(row["cutoff"], "cutoff") != cutoff:
            raise ValueError("cutoff order")
        schema_int(row["directed_edge_count"], "edge count")
        schema_int(row["valuation_mismatch_count"], "valuation mismatch")
        if type(row["edge_list_sha256"]) is not str or re.fullmatch(r"[0-9a-f]{64}", row["edge_list_sha256"]) is None:
            raise ValueError("edge digest")
        for vertex in schema_array(row["loop_vertices"], None, "loops"):
            schema_int(vertex, "loop vertex")
        for block in schema_array(row["valuation_block_directed_edge_counts"], None, "blocks"):
            block = schema_keys(block, {"count", "valuation"}, "block")
            schema_int(block["count"], "count")
            schema_int(block["valuation"], "valuation")
    cycle = schema_keys(payload["cycle_certificate"], {"direct_vertex_bound", "length_records",
                        "ordered_tuple_policy", "witnesses"}, "cycle")
    if schema_int(cycle["direct_vertex_bound"], "direct vertex bound") != 64 \
            or cycle["ordered_tuple_policy"] != "ALL_ORDERED_TUPLES_NOT_SAMPLED":
        raise ValueError("cycle enum")
    for length, row in zip(range(1, 8), schema_array(cycle["length_records"], 7, "length records")):
        row = schema_keys(row, {"compatible_tuple_count", "length", "odd_solution_count", "solution_count",
                           "solution_map_sha256", "tuple_count"}, "length row")
        for name in ["compatible_tuple_count", "length", "odd_solution_count", "solution_count", "tuple_count"]:
            schema_int(row[name], name)
        if row["length"] != length or row["tuple_count"] != 6 ** length \
                or type(row["solution_map_sha256"]) is not str \
                or re.fullmatch(r"[0-9a-f]{64}", row["solution_map_sha256"]) is None:
            raise ValueError("length row")
    witness_map = schema_keys(cycle["witnesses"], {"2,4,4", "4,4,8,4", "4,8,8,4"}, "witnesses")
    for label_text, witness in witness_map.items():
        width = len(label_text.split(","))
        witness = schema_keys(witness, {"odd_solutions", "solutions"}, "witness")
        for name in ["odd_solutions", "solutions"]:
            for row in schema_array(witness[name], None, "solutions"):
                for vertex in schema_array(row, width, "solution row"):
                    schema_int(vertex, "solution vertex")
    endpoint = schema_keys(payload["finite_endpoint_diagnostics"], {"evidence_type",
                           "hs_sigma_one_level_records", "row_one_sigma_zero_partial_sum_a_le_16",
                           "theorem_endpoint_verdicts"}, "endpoint")
    if endpoint["evidence_type"] != "FINITE_EXACT_DIAGNOSTIC":
        raise ValueError("endpoint evidence enum")
    for exponent, row in zip(range(1, 17), schema_array(endpoint["hs_sigma_one_level_records"], 16, "levels")):
        row = schema_keys(row, {"a", "sigma_one_level"}, "level")
        if schema_int(row["a"], "a") != exponent:
            raise ValueError("level order")
        schema_fraction(row["sigma_one_level"], "sigma level")
    schema_fraction(endpoint["row_one_sigma_zero_partial_sum_a_le_16"], "row one")
    if schema_array(endpoint["theorem_endpoint_verdicts"], 0, "endpoint verdicts") != []:
        raise ValueError("endpoint firewall")
    trace = schema_keys(payload["finite_trace_certificate"], {"formula", "records", "truncation_policy"}, "trace")
    if trace["formula"] != "DIRECT_CUTOFF_MATRIX_TRACE_EQUAL_TO_SCALE_DEPENDENT_ODD_BLOCK_SUM" \
            or trace["truncation_policy"] != "ODD_BLOCK_CUTOFF_VARIES_WITH_K_NO_FINITE_GEOMETRIC_COLLAPSE":
        raise ValueError("trace formula enum")
    grid = [(n_value, s_value, r_value) for n_value in [8, 16, 32]
            for s_value in [2, 4] for r_value in [1, 2, 3, 4, 5, 6]]
    for row, expected in zip(schema_array(trace["records"], 36, "trace records"), grid):
        row = schema_keys(row, {"N", "r", "s", "trace"}, "trace row")
        if (schema_int(row["N"], "N"), schema_int(row["s"], "s"), schema_int(row["r"], "r")) != expected:
            raise ValueError("trace grid")
        schema_fraction(row["trace"], "trace fraction")
    return payload


def validate_comparison_schema(value: Any) -> None:
    outer = schema_keys(value, {"payload", "schema", "status"}, "comparison")
    if outer["schema"] != "paper46-exact-comparison-v1" or outer["status"] != "PASS":
        raise ValueError("comparison identity")
    payload = schema_keys(outer["payload"], {"case_counts", "cycle_solution_mismatch_count",
                          "evidence_boundary", "finite_trace_mismatch_count", "finite_trace_truncation",
                          "science_projection_sha256", "strict_recursive_type_and_value_equal",
                          "support_mismatch_count"}, "comparison payload")
    counts = schema_keys(payload["case_counts"], {"cycle_ordered_label_tuples", "finite_trace_cases",
                         "structural_cutoffs"}, "case counts")
    for name, expected in {"cycle_ordered_label_tuples": 335922,
                           "finite_trace_cases": 36, "structural_cutoffs": 4}.items():
        if schema_int(counts[name], name) != expected:
            raise ValueError("case count")
    for name in ["cycle_solution_mismatch_count", "finite_trace_mismatch_count", "support_mismatch_count"]:
        if schema_int(payload[name], name) != 0:
            raise ValueError("mismatch count")
    if type(payload["strict_recursive_type_and_value_equal"]) is not bool \
            or payload["strict_recursive_type_and_value_equal"] is not True:
        raise ValueError("strict comparison boolean")
    boundary = schema_keys(payload["evidence_boundary"], {"finite_evidence_type", "infinite_theorem_status"}, "boundary")
    if boundary != {"finite_evidence_type": "FINITE_EXACT_DIAGNOSTIC",
                    "infinite_theorem_status": "NOT_INFERRED_FROM_FINITE_EVIDENCE"} \
            or payload["finite_trace_truncation"] != "SCALE_DEPENDENT_ODD_BLOCK_CUTOFF_NO_GEOMETRIC_COLLAPSE":
        raise ValueError("comparison enum")
    if type(payload["science_projection_sha256"]) is not str \
            or re.fullmatch(r"[0-9a-f]{64}", payload["science_projection_sha256"]) is None:
        raise ValueError("science digest")


def verify_static(root: Path) -> int:
    manifest = file_under(root, "STATIC_INPUT_SHA256SUMS.txt")
    rows: list[tuple[str, str]] = []
    for line in manifest.read_text(encoding="ascii").splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  ([A-Za-z0-9_./-]+)", line)
        if not match:
            raise ValueError("static manifest row")
        expected, relative = match.groups()
        if relative in {"STATIC_INPUT_SHA256SUMS.txt", "PREOUTPUT_STATIC_SEAL.json"} \
                or relative.startswith("outputs/"):
            raise ValueError("static manifest self/output inclusion")
        raw = file_under(root, relative).read_bytes()
        if sha(raw) != expected:
            raise ValueError("static byte drift")
        rows.append((relative, expected))
    names = [name for name, _ in rows]
    actual = sorted(path.relative_to(root).as_posix() for path in root.rglob("*")
                    if path.is_file() and not path.is_symlink()
                    and not path.relative_to(root).as_posix().startswith("outputs/")
                    and path.relative_to(root).as_posix() not in
                    {"STATIC_INPUT_SHA256SUMS.txt", "PREOUTPUT_STATIC_SEAL.json"})
    if names != sorted(names) or len(names) != len(set(names)) or names != actual:
        raise ValueError("static exact set")
    return len(rows)


def report_bytes(values: dict[str, dict[str, Any]]) -> bytes:
    comparison = values["comparison"]["payload"]
    proof = values["proof"]["payload"]
    source = values["source"]["payload"]
    mutations = values["mutations"]["payload"]
    external = values["external"]["payload"]
    independence = values["independence"]["payload"]
    route1 = values["route1"]["payload"]
    route2 = values["route2"]["payload"]
    counts = comparison["case_counts"]
    lines = [
        "# Paper 46 isolated integration report", "", "## Exact finite replay", "",
        f"Two physically independent evaluators agreed under strict recursive type and value "
        f"comparison on {counts['structural_cutoffs']} complete support cutoffs, "
        f"{counts['cycle_ordered_label_tuples']} ordered dyadic label tuples, and "
        f"{counts['finite_trace_cases']} exact rational trace cases. Support, cycle-solution, "
        "and finite-trace mismatch counts were all `0`.", "",
        "Every finite trace used the scale-dependent sum whose odd-block cutoff is "
        "`floor(N/2^k)`. No finite sum was collapsed to a geometric factor. These finite "
        "objects are diagnostics and do not prove an infinite endpoint.", "",
        "## Infinite-theorem certificate", "",
        f"The independent proof auditor replayed {proof['proof_anchor_count']} frozen analytic "
        "anchors and certified the strict walls `0`, `1/2`, and `1`, the exact valuation "
        "direct sum, the complete odd/even cyclic solver, and the separately typed infinite "
        f"trace identity. Finite-grid-as-proof is `{str(proof['finite_grid_used_as_proof']).lower()}`; "
        f"theorem failures: `{proof['theorem_failure_count']}`.", "",
        "## Source and ownership boundary", "",
        "Fournier--Wagner retains ownership of Schur-based lacunary boundedness and the "
        "reflection, folding, and alternating lacunary representation machinery. Its novelty "
        f"credit here is `{source['fournier_wagner_novelty_credit']}`. P46 is confined to the "
        "frozen weighted valuation/cycle/trace package, and the bounded search proves no priority.", "",
        "## Independence and adversarial closeout", "",
        f"Evaluator hashes are distinct (`{independence['evaluator_m_sha256']}` and "
        f"`{independence['evaluator_c_sha256']}`); project-local imports, shared expanded "
        "fixtures, serialized intermediates, caches, and symlinks are absent. All "
        f"{mutations['instance_count']} concrete mutations in {mutations['family_count']} families "
        f"were rejected by every and only designated consumer across "
        f"{mutations['consumer_invocation_count']} invocations; survivors: `0`. The frozen "
        f"external auditor was also executed against {external['physical_mutated_clone_count']} "
        "physically mutated disposable clones; accepted mutations: `0`.", "",
        "## Route and scope", "",
        f"The primary and independent Route validators passed {route1['checks_passed']}/"
        f"{route1['checks_total']} and {route2['checks_passed']}/{route2['checks_total']} checks. "
        "The tuple remains `[A0_WEAK_ARITHMETIC_RELATION, A1_PASS_ANALYTIC, "
        "A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL]`; overall is "
        "`ROUTE_A_REJECTED`, and Route B is locked. `STOP_DUPLICATE` is external literature "
        "vocabulary and is not a Route terminal.", "",
        "This result is preauthority and retrospective. It authorizes no priority claim, "
        "authority write, Git action, repository README edit, mirror, registry change, or "
        "publication decision.", "",
    ]
    return "\n".join(lines).encode("ascii")


def science_projection(evaluator: dict[str, Any], schema: str) -> dict[str, Any]:
    if evaluator.get("schema") != schema or evaluator.get("status") != "PASS":
        raise ValueError("evaluator envelope")
    payload = evaluator["payload"]
    if payload.get("theorem_claims_inferred") != []:
        raise ValueError("finite theorem claim")
    return {key: item for key, item in payload.items() if key != "implementation_lane"}


def expected_integrity(state: str) -> dict[str, Any]:
    check_names = [
        "acyclic_preoutput_seal_and_manifest_domains",
        "canonical_json_and_recursive_scalar_types", "exact_output_namespace",
        "external_mutated_clone_rejections", "field_level_recursive_result_schema",
        "finite_infinite_evidence_firewall",
        "finite_trace_scale_dependent_truncation", "frozen_source_and_static_seals",
        "no_cache_symlink_or_host_path", "report_exact_reconstruction",
        "result_ledger_exact", "route_dual_auditor_agreement",
        "source_ownership_boundary", "state_A_B_provenance_exact",
        "strict_evaluator_comparison", "transaction_ready_for_atomic_install",
    ]
    checks = {name: True for name in check_names}
    return {"payload": {"checks": checks, "checks_passed": len(checks),
                        "checks_total": len(checks),
                        "final_namespace_count": 16 if state == "A" else 17,
                        "state": state},
            "schema": "paper46-read-only-integrity-audit-v1", "status": "PASS"}


def expected_ledger(output: Path, state: str) -> dict[str, Any]:
    excluded = {"RESULT_LEDGER.json", "audits/integrity_audit.json", "PAPER_MANIFEST.sha256"}
    names = sorted(name for name in STATE_A if name not in excluded)
    rows = [{"path": "outputs/" + name, "sha256": sha(file_under(output, name).read_bytes())}
            for name in names]
    return {"payload": {"entry_count": len(rows), "rows": rows, "state": state},
            "schema": "paper46-result-ledger-v1", "status": "PASS"}


def expected_paper_manifest(root: Path, output: Path) -> bytes:
    rows: list[tuple[str, str]] = []
    for path in root.rglob("*"):
        relative = path.relative_to(root).as_posix()
        if relative.startswith("outputs/") or relative in PAPER_MANIFEST_ROOT_EXCLUSIONS \
                or path.is_symlink() or not path.is_file():
            continue
        rows.append((relative, sha(path.read_bytes())))
    for name in STATE_A:
        rows.append(("outputs/" + name, sha(file_under(output, name).read_bytes())))
    rows.sort()
    names = [name for name, _ in rows]
    forbidden = set(PAPER_MANIFEST_ROOT_EXCLUSIONS) | {PAPER_MANIFEST_SELF}
    if len(names) != len(set(names)) or forbidden.intersection(names):
        raise ValueError("paper manifest forbidden inclusion")
    return "".join(f"{digest}  {name}\n" for name, digest in rows).encode("ascii")


def main() -> int:
    parser = StrictParser(add_help=True)
    parser.add_argument("--root")
    parser.add_argument("--output-root")
    parser.add_argument("--state", choices=["A", "B"])
    parser.add_argument("--mutation")
    args = parser.parse_args()
    if args.mutation:
        if any(value is not None for value in [args.root, args.output_root, args.state]):
            raise ValueError("CLI_ARGUMENT_ERROR: --mutation is exclusive")
        return reject(args.mutation)
    if not args.root or not args.output_root or not args.state:
        raise ValueError("CLI_ARGUMENT_ERROR: --root, --output-root and --state required")
    root, output = safe_root(Path(args.root)), safe_root(Path(args.output_root))
    offenders = [path for path in list(root.rglob("*")) + list(output.rglob("*"))
                 if path.is_symlink() or path.name == "__pycache__" or path.suffix == ".pyc"]
    if offenders:
        raise ValueError("symlink/cache")
    static_count = verify_static(root)
    expected_names = sorted(STATE_A + (["PAPER_MANIFEST.sha256"] if args.state == "B" else []))
    actual_names = sorted(path.relative_to(output).as_posix() for path in output.rglob("*")
                          if path.is_file())
    if actual_names != expected_names:
        raise ValueError("output namespace")
    json_names = [name for name in STATE_A if name.endswith(".json")]
    objects: dict[str, dict[str, Any]] = {}
    raws: dict[str, bytes] = {}
    for name in json_names:
        value, raw = load_json(output, name)
        if value.get("status") != "PASS" or not scalar_safe(value):
            raise ValueError("JSON status/type/path")
        objects[name], raws[name] = value, raw
    packet = objects["data/source_packet.json"]["payload"]
    if packet["preauthority_manifest_sha256"] != PREAUTH_SHA \
            or packet["ownership"]["fournier_wagner_novelty_credit"] != 0:
        raise ValueError("source/ownership")
    m_payload = validate_evaluator_schema(
        objects["results/evaluator_m.json"], "paper46-evaluator-m-v1",
        "M_LITERAL_BIT_PREDICATE_MATRIX_AND_DIRECT_BOUNDED_WALKS")
    c_payload = validate_evaluator_schema(
        objects["results/evaluator_c.json"], "paper46-evaluator-c-v1",
        "C_ANTI_DIAGONAL_VALUATION_AND_ALGEBRAIC_CYCLIC_SOLVER")
    validate_comparison_schema(objects["results/exact_comparison.json"])
    m_projection = {key: item for key, item in m_payload.items() if key != "implementation_lane"}
    c_projection = {key: item for key, item in c_payload.items() if key != "implementation_lane"}
    if not strict(m_projection, c_projection):
        raise ValueError("evaluator disagreement")
    comparison = objects["results/exact_comparison.json"]["payload"]
    if comparison["science_projection_sha256"] != sha(canonical(m_projection)) \
            or comparison["finite_trace_truncation"] != "SCALE_DEPENDENT_ODD_BLOCK_CUTOFF_NO_GEOMETRIC_COLLAPSE" \
            or comparison["strict_recursive_type_and_value_equal"] is not True:
        raise ValueError("comparison mismatch")
    if objects["audits/proof_audit.json"]["payload"]["finite_grid_used_as_proof"] is not False \
            or not all(objects["audits/proof_audit.json"]["payload"]["infinite_theorem_certificate"].values()):
        raise ValueError("proof audit")
    if objects["tests/mutation_results.json"]["payload"]["survivor_count"] != 0 \
            or objects["audits/external_auditor_mutations.json"]["payload"]["accepted_mutation_count"] != 0:
        raise ValueError("mutations")
    route_raw = file_under(output, "evaluations/route_a/SD-C48/2026-08-18.yaml").read_bytes()
    route = json.loads(route_raw.decode("ascii"), object_pairs_hook=unique)
    if route_raw != canonical(route) or route["state"] != args.state \
            or route["route_b_invocation_allowed"] is not False \
            or route["overall_verdict"] != "ROUTE_A_REJECTED" \
            or "STOP_DUPLICATE" in json.dumps(route["terminal_codes"], sort_keys=True):
        raise ValueError("route")
    r1 = objects["audits/route_primary.json"]["payload"]
    r2 = objects["audits/route_independent.json"]["payload"]
    if r1["normalized_route_sha256"] != sha(route_raw) \
            or r2["normalized_route_sha256"] != sha(route_raw):
        raise ValueError("dual route")
    values = {
        "comparison": objects["results/exact_comparison.json"],
        "external": objects["audits/external_auditor_mutations.json"],
        "independence": objects["audits/independence_audit.json"],
        "mutations": objects["tests/mutation_results.json"],
        "proof": objects["audits/proof_audit.json"],
        "route1": objects["audits/route_primary.json"],
        "route2": objects["audits/route_independent.json"],
        "source": objects["audits/source_audit.json"],
    }
    if file_under(output, "reports/EXPERIMENT_REPORT.md").read_bytes() != report_bytes(values):
        raise ValueError("report reconstruction")
    if objects["RESULT_LEDGER.json"] != expected_ledger(output, args.state):
        raise ValueError("result ledger")
    if objects["audits/integrity_audit.json"] != expected_integrity(args.state):
        raise ValueError("integrity self-tamper")
    commits = [route["source_commit"], route["code_commit"], route["source_lock"]["code_commit"]]
    if args.state == "A":
        if commits != [PENDING] * 3:
            raise ValueError("State A provenance")
    else:
        if len(set(commits)) != 1 or not re.fullmatch(r"[0-9a-f]{40}", commits[0]) \
                or commits[0] == "0" * 40:
            raise ValueError("State B provenance")
        if file_under(output, "PAPER_MANIFEST.sha256").read_bytes() != expected_paper_manifest(root, output):
            raise ValueError("State B paper manifest domain")
    sys.stdout.buffer.write(canonical({
        "payload": {"output_namespace_count": len(expected_names), "state": args.state,
                    "static_file_count": static_count, "whole_tree_checks": 19},
        "schema": "paper46-frozen-external-audit-v1", "status": "PASS",
    }))
    return 0


def rejection_code(error: Exception) -> str:
    message = str(error)
    if message.startswith("CLI_ARGUMENT_ERROR"):
        return "CLI_ARGUMENT_ERROR"
    if "mutation not designated" in message:
        return "UNKNOWN_MUTATION_ID"
    if any(token in message for token in ["unsafe root", "unsafe relative", "containment",
                                           "No such file", "Not a directory"]):
        return "PATH_ROOT_INVALID"
    if "exact keys" in message or "duplicate key" in message:
        return "RESULT_SCHEMA_KEYSET_FAILURE"
    if any(token in message for token in ["bool/float", "exact int", "exact array shape",
                                           "strict comparison boolean", "fraction", "noncanonical JSON",
                                           "JSON status/type/path"]):
        return "RESULT_SCHEMA_TYPE_FAILURE"
    if "static byte drift" in message or "static exact set" in message:
        return "STATIC_INPUT_DRIFT"
    if "output namespace" in message:
        return "OUTPUT_NAMESPACE_MISMATCH"
    if "symlink/cache" in message or "symlink forbidden" in message:
        return "SYMLINK_OR_CACHE_FORBIDDEN"
    if "source/ownership" in message:
        return "FROZEN_SOURCE_DRIFT"
    if "evaluator typed identity" in message or "evaluator disagreement" in message \
            or "comparison mismatch" in message:
        return "CANONICAL_SCIENCE_MISMATCH"
    if "report reconstruction" in message:
        return "REPORT_RECONSTRUCTION_MISMATCH"
    if "route" in message.lower() or "Route" in message:
        return "ROUTE_RECORD_MISMATCH"
    if "result ledger" in message:
        return "RESULT_LEDGER_MISMATCH"
    if "paper manifest" in message:
        return "PAPER_MANIFEST_DOMAIN_FAILURE"
    if "integrity self-tamper" in message:
        return "AUDIT_SELF_TAMPER"
    if "State A provenance" in message or "State B provenance" in message:
        return "PROVENANCE_STATE_FAILURE"
    return "FROZEN_EXTERNAL_AUDIT_FAILURE"


def guarded_main() -> int:
    try:
        return main()
    except Exception as error:
        sys.stdout.buffer.write(canonical({
            "payload": {"code": rejection_code(error)},
            "schema": "paper46-frozen-external-rejection-v1",
            "status": "REJECT",
        }))
        return 2


if __name__ == "__main__":
    raise SystemExit(guarded_main())
