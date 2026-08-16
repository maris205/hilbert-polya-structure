#!/usr/bin/env python3
"""Read-only, environment-stable integrity audit for Paper 39 / SD-C41."""

from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path
import re
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SCIENCE_SHA256 = "77a45be483807b81ba61fe0f16b16be20fcd7e6e4ff1f3f74f34d052c6881d93"
EXPECTED_RESEARCH = {
    "DAG_BRIDGE.json": "4fa3bb28e6a2371dfb134f4a45ff03c1953ea68764f1decb70c64a9d5423d240",
    "DA_REPORT.md": "ef9aacc4584125853c572802a81e7243a60472ad5c5df17af57dd92d2e1599a3",
    "DERIVATION_PACKAGE.md": "ba3d6686928ebc67a24080a48d759cf6395547216b37aa7eeaffddc1bdfc58ed",
    "LITERATURE_AUDIT.md": "aaca0a1834cc9793873698a07cbf4ddedb73a409eb9bd4dbc72ec4dd857fc781",
    "MATH_PACKAGE.md": "9af9b4cc68edf87871b9f3d94b04a1df9a92befa59bb2561394f1b6c990c37e9",
    "PROOF_PACKAGE.md": "cc58540cb7a2396b7578f3aa7a76de3fcd7554a9faa5f26a4f98d6334b6da621",
    "QUANTIFIER_AUDIT.md": "29653cc74b95b3e4e32382f138c1ac00598a5c92bfbbd3c31d8cf8a9ad244073",
    "ROUTE_A_EVALUATION.yaml": "7bdb90811575a96518c2f67510ef9deb4335e2051c965643f7e3572e806ff6cd",
    "SOURCE_LOCK.md": "70456aff0b3afff0fe78336da3af7f2fc47724eb59674bf50bb7de4f1857770b",
}
EXPECTED_PLANS = {
    "experiments/EXPERIMENT_PLAN.md": "901661536afe4a6741d459c8ed83329b2a29dae76f08e2b551910354e6d0fdba",
    "experiments/PREREGISTRATION.md": "524048cc678709f663602536b29d197a739e2edfe6c9e52baf947f0ff2a3005d",
}
EXPECTED_CODE = sorted(
    [
        "code/audit_integrity.py",
        "code/contracts/CANDIDATE_CONTRACT.json",
        "code/contracts/DAG_BRIDGE.json",
        "code/contracts/EMPTY_REGISTRY_FIXTURE.json",
        "code/contracts/INPUT_LOCK.json",
        "code/evaluator/evaluate_packet.py",
        "code/evaluator/evaluate_route_a.py",
        "code/evaluator/independent_evaluator.py",
        "code/evaluator/packet_adapter.py",
        "code/run_exact_integration.py",
        "code/run_tests.py",
        "code/source/emit_packet.py",
        "code/source/source_core.py",
    ]
)
EXPECTED_DOCS = sorted(
    [
        "docs/DEPENDENCY_LOCK.json",
        "docs/INTEGRITY_PROTOCOL.md",
        "docs/PROTOTYPE_LOCK.json",
        "docs/RESEARCH_LOCK.json",
    ]
)
EXPECTED_EXPERIMENTS = sorted(EXPECTED_PLANS)
EXPECTED_EVALUATIONS = sorted(
    [
        "evaluations/route_a/SD-C41/2026-08-16.yaml",
        "evaluations/route_a/SD-C41/independent_evaluation.json",
    ]
)


def canonical_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def digest_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def parse_json(relative: str) -> Any:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def python_imports(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    output: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            output.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            output.add(node.module.split(".")[0])
    return output


def text_hygiene(path: Path) -> bool:
    raw = path.read_bytes()
    try:
        raw.decode("utf-8")
    except UnicodeDecodeError:
        return False
    if raw.startswith(b"\xef\xbb\xbf") or b"\r" in raw:
        return False
    if not raw.endswith(b"\n") or raw.endswith(b"\n\n"):
        return False
    if any(line.rstrip(b" \t") != line for line in raw.splitlines()):
        return False
    return not any(byte < 32 and byte not in (9, 10) for byte in raw)


def main() -> int:
    checks: list[tuple[str, bool]] = []

    def check(name: str, passed: Any) -> None:
        checks.append((name, bool(passed)))

    check("stage1_manifest_absent", not (ROOT / "PAPER_MANIFEST.sha256").exists())
    check("authority_root_has_code", (ROOT / "code/run_exact_integration.py").is_file())

    research = parse_json("docs/RESEARCH_LOCK.json")
    check("research_lock_schema", research.get("schema") == "paper39-authority-research-lock-v1")
    check("research_lock_exact_files", research.get("immutable_authority_files") == EXPECTED_RESEARCH)
    check("research_lock_exact_plans", research.get("immutable_experiment_plans") == EXPECTED_PLANS)
    check("research_lock_count", research.get("locked_file_count") == 11)
    check(
        "research_lock_mutable_writer_exclusions",
        {"README.md", "PREREGISTRATION.md", "ROUND2_CLUES.md", "main.tex", "main.pdf"}
        <= set(research.get("mutable_writer_files_deliberately_excluded", [])),
    )
    for relative, expected in {**EXPECTED_RESEARCH, **EXPECTED_PLANS}.items():
        check("locked_hash:" + relative, (ROOT / relative).is_file() and digest(ROOT / relative) == expected)

    prototype = parse_json("docs/PROTOTYPE_LOCK.json")
    check("prototype_lock_schema", prototype.get("schema") == "paper39-authority-prototype-lock-v1")
    check("prototype_runtime_independence", prototype.get("external_prototype_is_runtime_dependency") is False)
    check(
        "prototype_math_v4",
        prototype.get("final_math_bundle", {}).get("bridge_schema")
        == "paper39-structural-spine-expanded-proof-dag-bridge-v4"
        and prototype.get("final_math_bundle", {}).get("bridge_sha256")
        == "4fa3bb28e6a2371dfb134f4a45ff03c1953ea68764f1decb70c64a9d5423d240"
        and prototype.get("final_math_bundle", {}).get("manifest_sha256")
        == "2ad22641c3ea0adbe0f9ae53671dd7ce8406d1558c399f5a5cc94bf17bdd761b"
        and prototype.get("final_math_bundle", {}).get("aggregate_sha256")
        == "cc7f068b81b2a04a8c319a90bd0d033dea440e19b3ff61703f81a5aab5d548bb",
    )
    check(
        "prototype_review_locks",
        prototype.get("final_reviews", {}).get("corrected_literature_audit_sha256")
        == "aaca0a1834cc9793873698a07cbf4ddedb73a409eb9bd4dbc72ec4dd857fc781"
        and prototype.get("final_reviews", {}).get("decision_audit_report_sha256")
        == "ef9aacc4584125853c572802a81e7243a60472ad5c5df17af57dd92d2e1599a3",
    )
    check(
        "prototype_science_target",
        prototype.get("frozen_expected_outcome", {}).get("science_projection_sha256") == EXPECTED_SCIENCE_SHA256,
    )
    for relative, expected in prototype.get("authority_imports", {}).items():
        check("prototype_import_hash:" + relative, (ROOT / relative).is_file() and digest(ROOT / relative) == expected)

    actual_code = sorted(path.relative_to(ROOT).as_posix() for path in (ROOT / "code").rglob("*") if path.is_file())
    actual_docs = sorted(path.relative_to(ROOT).as_posix() for path in (ROOT / "docs").rglob("*") if path.is_file())
    actual_experiments = sorted(path.relative_to(ROOT).as_posix() for path in (ROOT / "experiments").rglob("*") if path.is_file())
    actual_evaluations = sorted(path.relative_to(ROOT).as_posix() for path in (ROOT / "evaluations").rglob("*") if path.is_file())
    check("exact_code_set", actual_code == EXPECTED_CODE)
    check("exact_docs_set", actual_docs == EXPECTED_DOCS)
    check("exact_experiment_set", actual_experiments == EXPECTED_EXPERIMENTS)
    check("exact_evaluation_set", actual_evaluations == EXPECTED_EVALUATIONS)
    check("report_present", (ROOT / "EXPERIMENT_REPORT.md").is_file())

    contract = parse_json("results/integrity_contract.json")
    result_set = parse_json("results/exact_result_set.json")
    text_set = parse_json("results/exact_text_set.json")
    actual_results = sorted(path.relative_to(ROOT).as_posix() for path in (ROOT / "results").rglob("*") if path.is_file())
    check("integrity_contract_schema", contract.get("schema") == "paper39-integrity-contract-v1")
    check("exact_result_contract_match", contract.get("exact_result_paths") == result_set.get("paths"))
    check("exact_result_count", result_set.get("count") == len(result_set.get("paths", [])))
    check("exact_result_sorted_unique", result_set.get("paths") == sorted(set(result_set.get("paths", []))))
    check("exact_result_actual_set", result_set.get("paths") == actual_results)
    check("exact_text_contract_match", contract.get("exact_text_paths") == text_set.get("paths"))
    check("exact_text_count", text_set.get("count") == len(text_set.get("paths", [])))
    check("exact_text_sorted_unique", text_set.get("paths") == sorted(set(text_set.get("paths", []))))
    check("exact_text_all_present", all((ROOT / relative).is_file() for relative in text_set.get("paths", [])))
    check(
        "exact_text_expected_scopes",
        set(EXPECTED_CODE + EXPECTED_DOCS + EXPECTED_EXPERIMENTS + EXPECTED_EVALUATIONS + actual_results + list(EXPECTED_RESEARCH) + ["EXPERIMENT_REPORT.md"])
        == set(text_set.get("paths", [])),
    )

    for relative in text_set.get("paths", []):
        check("text_hygiene:" + relative, text_hygiene(ROOT / relative))

    all_entries = list(ROOT.rglob("*"))
    check("no_symlinks", not any(path.is_symlink() for path in all_entries))
    forbidden_names = {"__pycache__", ".pytest_cache", ".mypy_cache", ".DS_Store"}
    check("no_cache_names", not any(path.name in forbidden_names for path in all_entries))
    check("no_bytecode", not any(path.is_file() and path.suffix in {".pyc", ".pyo"} for path in all_entries))
    check(
        "no_hidden_temporary_residue",
        not any(path.name.startswith(".") and path.name not in {".", ".."} for path in all_entries),
    )
    aux_suffixes = {".aux", ".bbl", ".blg", ".fdb_latexmk", ".fls", ".log", ".out", ".toc"}
    check("no_auxiliary_build_residue", not any(path.is_file() and path.suffix in aux_suffixes for path in all_entries))

    ledger_lines = (ROOT / "results/SHA256SUMS.txt").read_text(encoding="utf-8").splitlines()
    ledger_rows: list[tuple[str, str]] = []
    ledger_format = True
    for line in ledger_lines:
        match = re.fullmatch(r"([0-9a-f]{64})  ([^\n]+)", line)
        if match is None:
            ledger_format = False
            continue
        ledger_rows.append((match.group(2), match.group(1)))
    ledger_paths = [relative for relative, _ in ledger_rows]
    check("ledger_format", ledger_format)
    check("ledger_sorted_unique", ledger_paths == sorted(set(ledger_paths)))
    check("ledger_contract_exact", ledger_paths == contract.get("ledger_paths"))
    check("ledger_exclusions_exact", contract.get("ledger_exclusions") == ["PAPER_MANIFEST.sha256", "evaluations/route_a/SD-C41/2026-08-16.yaml", "results/SHA256SUMS.txt"])
    check("ledger_self_excluded", "results/SHA256SUMS.txt" not in ledger_paths)
    check("ledger_route_excluded", "evaluations/route_a/SD-C41/2026-08-16.yaml" not in ledger_paths)
    check("ledger_manifest_excluded", "PAPER_MANIFEST.sha256" not in ledger_paths)
    check("ledger_mutable_writer_excluded", not ({"README.md", "PREREGISTRATION.md", "ROUND2_CLUES.md"} & set(ledger_paths)))
    check("ledger_hashes", all((ROOT / relative).is_file() and digest(ROOT / relative) == expected for relative, expected in ledger_rows))

    dependency = parse_json("docs/DEPENDENCY_LOCK.json")
    code_paths = sorted((ROOT / "code").rglob("*.py"))
    import_union = set().union(*(python_imports(path) for path in code_paths)) if code_paths else set()
    actual_stdlib = sorted(import_union - {"__future__", "source_core"})
    check("dependency_schema", dependency.get("schema") == "paper39-dependency-lock-v1")
    check("dependency_no_external", dependency.get("external_dependencies") == [])
    check("dependency_network_forbidden", dependency.get("network_allowed") is False)
    check("dependency_exact_ast_imports", dependency.get("declared_standard_library") == actual_stdlib)
    source_imports = set().union(*(python_imports(path) for path in (ROOT / "code/source").glob("*.py")))
    evaluator_imports = set().union(*(python_imports(path) for path in (ROOT / "code/evaluator").glob("*.py")))
    check("source_import_firewall", not (source_imports & {"evaluate_packet", "evaluate_route_a", "independent_evaluator", "packet_adapter"}))
    check("evaluator_import_firewall", not (evaluator_imports & {"emit_packet", "source_core"}))

    input_lock = parse_json("code/contracts/INPUT_LOCK.json")
    authority_base = Path(input_lock["authority_papers_base"])
    current_input_checks: list[bool] = []
    for spec in input_lock.get("papers", []):
        for relative, expected in spec.get("files", {}).items():
            current_input_checks.append(digest(authority_base / spec["slug"] / relative) == expected)
    registry = input_lock.get("registry", {})
    current_input_checks.append(digest(authority_base / registry["candidate_registry_relative"]) == registry["candidate_registry_sha256"])
    current_input_checks.append(digest(authority_base / registry["preregistration_relative"]) == registry["preregistration_sha256"])
    route_authority = input_lock.get("route_a_evaluator", {})
    current_input_checks.append(digest(Path(route_authority["absolute_path"])) == route_authority["sha256"])
    check("predecessor_and_registry_lock_count_31", len(current_input_checks) == 31)
    check("predecessor_registry_route_locks_current", all(current_input_checks))
    route_authority_text = Path(route_authority["absolute_path"]).read_text(encoding="utf-8")
    check(
        "good_conjunct_authority_anchors",
        len(route_authority.get("good_conjunct_criterion_map", [])) == 6
        and all(
            anchor in route_authority_text
            for row in route_authority.get("good_conjunct_criterion_map", [])
            for anchor in row.get("required_anchor_substrings", [])
        ),
    )

    candidate = parse_json("code/contracts/CANDIDATE_CONTRACT.json")
    bridge = parse_json("code/contracts/DAG_BRIDGE.json")
    fixture = parse_json("code/contracts/EMPTY_REGISTRY_FIXTURE.json")
    check("candidate_contract_hash", digest(ROOT / "code/contracts/CANDIDATE_CONTRACT.json") == "810797ea277a4754d88591ad6f6990ecc3affb73aa8f83fc1cb091c3fb6796e4")
    check("bridge_hash", digest(ROOT / "code/contracts/DAG_BRIDGE.json") == "4fa3bb28e6a2371dfb134f4a45ff03c1953ea68764f1decb70c64a9d5423d240")
    check("bridge_authority_byte_identity", (ROOT / "DAG_BRIDGE.json").read_bytes() == (ROOT / "code/contracts/DAG_BRIDGE.json").read_bytes())
    check("empty_fixture_hash", digest(ROOT / "code/contracts/EMPTY_REGISTRY_FIXTURE.json") == "c404212170a88c03cd45798b5da654e51001974cf80ec3d757a9b95fb60c62d7")
    check("input_lock_hash", digest(ROOT / "code/contracts/INPUT_LOCK.json") == "dcd2e64959986c543554d6fd2827196623b986977ac22f354c799be422e3d7ee")
    check("bridge_schema_v4", bridge.get("schema") == "paper39-structural-spine-expanded-proof-dag-bridge-v4")
    bridge_counts = bridge.get("counts", {})
    check(
        "bridge_counts_14_16_17_6_5_22_28",
        bridge_counts.get("top_level_repair_classes") == 14
        and bridge_counts.get("frozen_request_tokens") == 16
        and bridge_counts.get("internal_transition_tags") == 17
        and bridge_counts.get("structural_spine_nodes") == 6
        and bridge_counts.get("structural_spine_edges") == 5
        and bridge_counts.get("expanded_proof_dag_nodes") == 22
        and bridge_counts.get("expanded_proof_dag_edges") == 28,
    )
    e36 = next(edge for edge in candidate.get("edges", []) if edge.get("edge_id") == "E36_37")
    check(
        "e36_37_four_identity_resets",
        set(e36.get("field_transfer", {})) == {"object", "marker", "operator_owner", "determinant_owner"}
        and all(
            e36["field_transfer"][field].get("mode") == "RESET"
            and e36["field_transfer"][field].get("reset_authority_id") == "P37_SOURCE_LOCK_SD_C39"
            and "equivalence_id" not in e36["field_transfer"][field]
            for field in ("object", "marker", "operator_owner", "determinant_owner")
        ),
    )
    firewall = bridge.get("non_domain_firewall_edges", [])
    check(
        "e22_firewall_exact_zero_credit",
        len(firewall) == 1
        and firewall[0].get("edge_id") == "E22"
        and firewall[0].get("request_token_ids") == []
        and firewall[0].get("repair_class_coverage_ids") == [],
    )
    check("empty_registry_fixture_true_branch", fixture.get("rows") == [] and fixture.get("expected_terminal") == "STOP_NO_SOURCE_LOCKED_NON_AFFINE_SUCCESSOR")

    source = parse_json("results/source_packet.json")
    evaluation = parse_json("results/main_evaluation.json")
    independent = parse_json("results/independent_evaluation.json")
    science = parse_json("results/scientific_results.json")
    tests = parse_json("results/adversarial_tests.json")
    analysis = parse_json("results/analysis_summary.json")
    check("source_hash_exact", digest(ROOT / "results/source_packet.json") == "7bbb1a701a9461812cb0d40ae6aab335f6507b58fd9591dba2881276abf8e62b")
    check("main_hash_exact", digest(ROOT / "results/main_evaluation.json") == "041461feaf8d34c9974606b9856be5ba5fc6c26f62c88ba38b041998bfd82394")
    check("independent_hash_exact", digest(ROOT / "results/independent_evaluation.json") == "21bb9b3f623215875bdf93670165da41ff5c42f7e5ccb25cc19a432f7c048398")
    check("tests_hash_exact", digest(ROOT / "results/adversarial_tests.json") == "f5fee0209155d06c8e16aedbf44ed2003f29115ad76b7f06bafe8be8a6d26f56")
    check("analysis_hash_exact", digest(ROOT / "results/analysis_summary.json") == "acf6dfefcead90b84eb0f28f43c60bf94ad0512389a7ce50d458d6b08e87560a")
    check("science_hash_exact", digest(ROOT / "results/scientific_results.json") == EXPECTED_SCIENCE_SHA256)
    check("source_schema", source.get("schema") == "paper39-source-packet-v1")
    check("main_535", evaluation.get("all_pass") is True and evaluation.get("counts", {}).get("checks_passed") == 535 and evaluation.get("counts", {}).get("checks_total") == 535)
    check("independent_278", independent.get("all_pass") is True and independent.get("counts", {}).get("checks_passed") == 278 and independent.get("counts", {}).get("checks_total") == 278)
    check("evaluator_science_equal", evaluation.get("science_projection") == independent.get("science_projection") == science)
    check("evaluator_science_hash_fields", evaluation.get("science_projection_sha256") == independent.get("science_projection_sha256") == EXPECTED_SCIENCE_SHA256)
    check("mutations_29_both", tests.get("all_pass") is True and tests.get("counts") == {"independent_rejections": 29, "main_rejections": 29, "mutations": 29})
    check("every_mutation_rejected_both", len(tests.get("mutations", [])) == 29 and all(row.get("main_rejected") and row.get("independent_rejected") for row in tests.get("mutations", [])))
    check("analysis_retrospective", analysis.get("exhaustiveness_scope") == "RETROSPECTIVE_CHECKER_FROZEN_P39_ENCODING_ONLY" and analysis.get("preregistration_semantics", {}).get("predecessor_outcomes_known_when_encoded") is True)
    check("analysis_no_universal_claim", analysis.get("universal_affine_no_go_claimed") is False)
    check("analysis_class_census_6_6_2", analysis.get("repair_disposition_counts") == {"MIXED_CANONICAL_OBSTRUCTION_ALTERNATIVES_EXIT": 2, "OBSTRUCTED": 6, "OUT_OF_CONTRACT_CATEGORY_CHANGE": 6})
    check("analysis_counts", analysis.get("raw_counts", {}).get("request_tokens") == 16 and analysis.get("raw_counts", {}).get("internal_transition_tags") == 17 and analysis.get("raw_counts", {}).get("new_mechanisms") == 0)
    check("analysis_registry_return", analysis.get("realized_terminal") == "RETURN_CONTROL_TO_PREEXISTING_GLOBAL_CANDIDATE_REGISTRY")
    check("analysis_registry_six", [row.get("candidate_id") for row in analysis.get("registry_classification", [])] == [f"SD-C0{i}" for i in range(1, 7)])
    check("science_endpoint_totality", science.get("endpoint_obstruction_totality") is True)
    check("science_token_census_8_8", list(science.get("request_token_dispositions", {}).values()).count("OBSTRUCTED") == 8 and list(science.get("request_token_dispositions", {}).values()).count("EXIT") == 8)
    check("science_no_new_mechanism", science.get("new_mechanism_count") == 0)
    check("science_registry_terminals_distinct", science.get("realized_terminal") == "RETURN_CONTROL_TO_PREEXISTING_GLOBAL_CANDIDATE_REGISTRY" and science.get("empty_registry_fixture_terminal") == "STOP_NO_SOURCE_LOCKED_NON_AFFINE_SUCCESSOR")

    for branch in ("A", "B", "C"):
        for name in ("source_packet.json", "main_evaluation.json", "independent_evaluation.json", "scientific_results.json", "route_evaluation.json"):
            check(
                f"run_identity:{branch}:{name}",
                (ROOT / "results/runs" / branch / name).read_bytes() == (ROOT / "results" / name).read_bytes(),
            )

    metadata = parse_json("results/metadata_stability.json")
    manifest = parse_json("results/manifest_metadata_stability.json")
    reproducibility = parse_json("results/reproducibility_certificate.json")
    external = parse_json("results/external_provenance_stability.json")
    cold = parse_json("results/cold_copy_certificate.json")
    idempotence = parse_json("results/idempotence_certificate.json")
    reproduction = parse_json("results/prototype_reproduction.json")
    boundary = parse_json("results/source_evaluator_boundary.json")
    check("metadata_stability", metadata.get("all_pass") is True and metadata.get("states") == ["absent", "null", "empty", "populated"])
    check("manifest_metadata_stability", manifest.get("all_pass") is True and manifest.get("stage1_manifest_actual_state") == "ABSENT")
    check("reproducibility_ABC", reproducibility.get("all_pass") is True and reproducibility.get("fresh_processes") == ["A", "B", "C"] and all(reproducibility.get("byte_identity", {}).values()))
    check("external_provenance_stability", external.get("all_pass") is True and external.get("external_prototype_consulted_by_either_run") is False)
    check("cold_copy_pass", cold.get("all_pass") is True and cold.get("empty_results_at_start") is True and cold.get("external_provenance_hidden") is True)
    check("idempotence_pass", idempotence.get("all_pass") is True and idempotence.get("changed_paths_between_identical_materializations") == 0)
    check("prototype_reproduction_pass", reproduction.get("all_pass") is True and reproduction.get("science_projection_sha256") == EXPECTED_SCIENCE_SHA256)
    check("source_evaluator_boundary_pass", boundary.get("all_pass") is True)

    route = parse_json("results/route_evaluation.json")
    independent_route = parse_json("evaluations/route_a/SD-C41/independent_evaluation.json")
    route_text = (ROOT / "evaluations/route_a/SD-C41/2026-08-16.yaml").read_text(encoding="utf-8")
    pending = "PENDING_FIRST_ARTIFACT_COMMIT"
    check("route_json_independent_copy", route == independent_route)
    check("route_v02", route.get("skill_version") == "0.2.0")
    check("route_all_fail", route.get("route_tuple") == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"])
    check("route_rejected", route.get("overall_verdict") == "ROUTE_A_REJECTED")
    check("route_B_false", route.get("B") is False and route.get("route_b_invocation_allowed") is False)
    check("route_metrics_all_NA", route.get("target_and_root_metrics") and set(route["target_and_root_metrics"].values()) == {"NA"})
    check("route_pending_json_triple", set(route.get("paired_provenance", {}).values()) == {pending} and len(route.get("paired_provenance", {})) == 3)
    check("route_science_hash", route.get("science_projection_sha256") == EXPECTED_SCIENCE_SHA256)
    check("route_seed_hash", route.get("seed_route_sha256") == EXPECTED_RESEARCH["ROUTE_A_EVALUATION.yaml"])
    check("route_yaml_top_source_pending", re.search(rf"^source_commit: {pending}$", route_text, re.MULTILINE) is not None)
    check("route_yaml_top_code_pending", re.search(rf"^code_commit: {pending}$", route_text, re.MULTILINE) is not None)
    check("route_yaml_source_lock_code_pending", re.search(rf"^  code_commit: {pending}$", route_text, re.MULTILINE) is not None)
    pending_field_lines = [
        line
        for line in route_text.splitlines()
        if re.fullmatch(rf"(?:  )?(?:source_commit|code_commit): {pending}", line)
    ]
    check("route_yaml_exact_pending_field_triple", len(pending_field_lines) == 3)
    check("route_yaml_stage1_manifest_absent", "stage1_root_manifest: ABSENT" in route_text)
    check("route_yaml_stage2_scope", "stage2_semantic_scope: ROUTE_CARD_PLUS_SELF_EXCLUDING_ROOT_MANIFEST_ONLY" in route_text)
    check("route_yaml_no_stale_tmp_wording", "in this /tmp package" not in route_text)
    check("route_yaml_metrics_NA", all(f"  {key}: \"NA\"" in route_text for key in route.get("target_and_root_metrics", {})))

    report = (ROOT / "EXPERIMENT_REPORT.md").read_text(encoding="utf-8")
    check("report_science_hash", EXPECTED_SCIENCE_SHA256 in report)
    check("report_counts", "535/535" in report and "278/278" in report and "29" in report)
    check("report_retrospective_scope", "retrospective" in report and "not a universal affine no-go" in report)
    check("report_registry_handoff", "RETURN_CONTROL_TO_PREEXISTING_GLOBAL_CANDIDATE_REGISTRY" in report)
    check("report_route_all_fail", "(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)" in report)
    check("report_pending", pending in report)

    passed = sum(value for _, value in checks)
    result = {
        "all_pass": passed == len(checks),
        "checks": [{"name": name, "passed": value} for name, value in checks],
        "counts": {"checks_passed": passed, "checks_total": len(checks)},
        "schema": "paper39-authority-integrity-audit-v1",
    }
    sys.stdout.buffer.write(canonical_bytes(result))
    return 0 if result["all_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
