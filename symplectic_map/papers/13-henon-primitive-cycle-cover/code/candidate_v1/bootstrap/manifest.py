"""Immutable source/code/preflight/JUnit manifest construction."""

from pathlib import Path
import xml.etree.ElementTree as ET

from .canonical import (
    canonical_bytes,
    read_regular_bytes,
    sha256_bytes,
    strict_canonical_load,
)
from .constants import (
    CANDIDATE_ID,
    CODE_RELATIVE,
    JUNIT_RELATIVE,
    PREFLIGHT_RELATIVE,
    SOURCE_LOCK_SHA256,
    SOURCE_REVIEW_SHA256,
)
from .preflight import collect_preflight


EXPECTED_TEST_IDS = tuple(sorted("code." + identifier for identifier in {
    "tests.test_adjudicator_mutations::test_adjudicator_route_attack_counter_and_contract_mutations_fail_without_science",
    "tests.test_canonical_security::test_source_bindings_and_absent_runtime_are_exact",
    "tests.test_canonical_security::test_static_audit_and_exact_private_fixture_schemas_close",
    "tests.test_canonical_security::test_strict_canonical_json_rejects_ambiguous_values",
    "tests.test_lifecycle::test_claim_commit_fsync_failure_is_terminal_after_boundary_crossing",
    "tests.test_lifecycle::test_diagnostic_and_symlink_guards_are_bounded",
    "tests.test_lifecycle::test_post_claim_drift_raw_pointer_and_evil_diagnostic_getter_terminalize",
    "tests.test_lifecycle::test_post_claim_exception_writes_terminal_and_forbids_retry",
    "tests.test_lifecycle::test_science_boundary_before_after_and_single_operation_call",
    "tests.test_manifest_junit::test_junit_parser_accepts_exact_expected_inventory_and_code_tree",
    "tests.test_manifest_junit::test_junit_parser_rejects_empty_declared_suite_and_child_failures",
    "tests.test_manifest_junit::test_manifest_preflight_parser_rejects_noncanonical_shape_and_staleness",
    "tests.test_mutation_security::test_engine_ast_alias_dunder_pattern_top_level_and_scan_mutations_fail",
    "tests.test_mutation_security::test_runner_minimal_builtins_fork_hook_and_rejection_category_mutations_fail",
    "tests.test_mutation_security::test_schema_open_empty_items_type_ref_and_unknown_keyword_mutations_fail",
    "tests.test_q_helpers::test_q_exact_algebra_controls_are_nonhollow_and_mutation_sensitive",
    "tests.test_q_helpers::test_q_helper_endpoint_shapes_without_top_level_science",
    "tests.test_q_helpers::test_q_scalar_tuple_wire_mutation_is_rejected",
    "tests.test_r_helpers::test_r_exact_elimination_controls_are_nonhollow_and_mutation_sensitive",
    "tests.test_r_helpers::test_r_helper_endpoint_shapes_without_top_level_science",
    "tests.test_r_helpers::test_r_scalar_tuple_wire_mutation_is_rejected",
    "tests.test_registered_orchestrator::test_registered_transaction_and_orchestration_are_science_free_and_one_shot",
    "tests.test_runtime_isolation::test_descendant_timeout_overflow_and_closed_pipe_are_group_reaped",
    "tests.test_runtime_isolation::test_fd3_closed_matrix_success_nonzero_timeout_overflow_and_injected_exception",
    "tests.test_runtime_isolation::test_fd3_open_matrix_success_nonzero_timeout_overflow_and_injected_exception",
    "tests.test_runtime_isolation::test_protocol_and_start_failures_preserve_bounded_diagnostics",
    "tests.test_runtime_isolation::test_real_safe_probe_q_never_loads_science",
    "tests.test_runtime_isolation::test_real_safe_probe_r_never_loads_science",
}))


def _code_files(project_root: Path):
    root = project_root / CODE_RELATIVE
    records = {}
    for path in sorted(root.rglob("*"), key=lambda item: item.as_posix()):
        if path.is_symlink():
            raise RuntimeError("manifest rejects symlink")
        if not path.is_file():
            continue
        if "__pycache__" in path.parts or path.suffix == ".pyc" or ".pytest_cache" in path.parts:
            raise RuntimeError("manifest rejects cache")
        payload = read_regular_bytes(path)
        relative = path.relative_to(root).as_posix()
        records[relative] = {
            "sha256": sha256_bytes(payload),
            "size_bytes": len(payload),
        }
    return records


def code_tree_sha256(project_root: Path):
    records = _code_files(project_root)
    if not records:
        raise RuntimeError("empty code tree")
    closure_lines = [
        path + "\u0000" + record["sha256"] + "\n"
        for path, record in sorted(records.items())
    ]
    return sha256_bytes("".join(closure_lines).encode("utf-8"))


def _declared_count(attributes, name):
    raw = attributes.get(name)
    if type(raw) is not str or not raw or not raw.isdecimal():
        raise ValueError("JUnit suite missing exact " + name + " count")
    return int(raw)


def _suite_record(suite):
    if suite.tag != "testsuite":
        raise ValueError("JUnit suite element")
    cases = []
    failure_count = 0
    error_count = 0
    skipped_count = 0
    properties = []
    seen_properties = False
    for child in list(suite):
        if child.tag == "properties":
            if seen_properties:
                raise ValueError("duplicate JUnit properties container")
            seen_properties = True
            if not list(child):
                raise ValueError("empty JUnit properties container")
            for prop in list(child):
                if prop.tag != "property" or set(prop.attrib) != {"name", "value"} or list(prop):
                    raise ValueError("malformed JUnit property")
                properties.append((prop.attrib["name"], prop.attrib["value"]))
        elif child.tag == "testcase":
            classname = child.attrib.get("classname")
            name = child.attrib.get("name")
            if type(classname) is not str or type(name) is not str or not classname or not name:
                raise ValueError("JUnit testcase identity")
            identifier = classname + "::" + name
            if identifier in cases:
                raise ValueError("duplicate JUnit testcase")
            cases.append(identifier)
            result_children = list(child)
            unknown = [
                item.tag
                for item in result_children
                if item.tag not in {"failure", "error", "skipped", "system-out", "system-err"}
            ]
            if unknown:
                raise ValueError("unknown JUnit testcase child")
            for item in result_children:
                if list(item):
                    raise ValueError("nested JUnit testcase result content")
                if item.tag in {"system-out", "system-err"} and item.attrib:
                    raise ValueError("JUnit diagnostic node attributes")
            dispositions = [
                item.tag for item in result_children if item.tag in {"failure", "error", "skipped"}
            ]
            if len(dispositions) > 1:
                raise ValueError("multiple JUnit testcase dispositions")
            failure_count += dispositions.count("failure")
            error_count += dispositions.count("error")
            skipped_count += dispositions.count("skipped")
        else:
            # In particular, suite-level failure/error nodes never count as a
            # passing suite and arbitrary nodes cannot be hidden from parsing.
            raise ValueError("unknown or suite-level JUnit child: " + child.tag)
    declared = {
        "errors": _declared_count(suite.attrib, "errors"),
        "failures": _declared_count(suite.attrib, "failures"),
        "skipped": _declared_count(suite.attrib, "skipped"),
        "tests": _declared_count(suite.attrib, "tests"),
    }
    actual = {
        "errors": error_count,
        "failures": failure_count,
        "skipped": skipped_count,
        "tests": len(cases),
    }
    if not cases:
        raise ValueError("JUnit suite contains no testcases")
    if declared != actual:
        raise ValueError("JUnit suite declared/actual count mismatch")
    return cases, actual, properties


def _junit_record(payload: bytes, expected_code_tree_sha256=None):
    if b"<!DOCTYPE" in payload.upper() or b"<!ENTITY" in payload.upper():
        raise ValueError("JUnit DTD/entity forbidden")
    try:
        root = ET.fromstring(payload)
    except ET.ParseError as exc:
        raise ValueError("JUnit XML parse") from exc
    if root.tag == "testsuite":
        suites = [root]
    elif root.tag == "testsuites":
        if any(child.tag != "testsuite" for child in list(root)):
            raise ValueError("unknown JUnit root child")
        suites = list(root)
    else:
        raise ValueError("JUnit root element")
    if not suites:
        raise ValueError("empty JUnit suite inventory")
    cases = []
    totals = {"errors": 0, "failures": 0, "skipped": 0, "tests": 0}
    properties = []
    for suite in suites:
        suite_cases, actual, suite_properties = _suite_record(suite)
        cases.extend(suite_cases)
        properties.extend(suite_properties)
        for key in totals:
            totals[key] += actual[key]
    if root.tag == "testsuites" and any(key in root.attrib for key in totals):
        declared_root = {key: _declared_count(root.attrib, key) for key in totals}
        if declared_root != totals:
            raise ValueError("JUnit root declared/actual count mismatch")
    if len(cases) != len(set(cases)):
        raise ValueError("duplicate JUnit testcase across suites")
    cases.sort()
    if not cases or tuple(cases) != EXPECTED_TEST_IDS:
        raise ValueError("JUnit exact testcase inventory drift")
    if totals["failures"] or totals["errors"] or totals["skipped"]:
        raise RuntimeError("JUnit is not a complete successful suite")
    code_properties = [value for name, value in properties if name == "p13_code_tree_sha256"]
    if len(properties) != 1 or len(code_properties) != 1:
        raise ValueError("JUnit exact code-tree property inventory")
    code_tree = code_properties[0]
    if (
        len(code_tree) != 64
        or any(character not in "0123456789abcdef" for character in code_tree)
    ):
        raise ValueError("JUnit code-tree property hash")
    if expected_code_tree_sha256 is not None and code_tree != expected_code_tree_sha256:
        raise RuntimeError("JUnit was not produced from the current code tree")
    return {
        "code_tree_sha256": code_tree,
        "error_count": totals["errors"],
        "failure_count": totals["failures"],
        "skipped_count": totals["skipped"],
        "test_count": totals["tests"],
        "test_ids": cases,
    }


def _validate_preflight_shape(value):
    required = {
        "candidate_id",
        "development_execution_boundary",
        "external_data_access_count",
        "gpu_hour_count",
        "network_access_count",
        "random_seed_count",
        "registered_audit_count",
        "safe_runtime_probes",
        "schema",
        "source_bindings",
        "static_audit",
        "status",
    }
    if type(value) is not dict or set(value) != required:
        raise ValueError("preflight exact top-level shape")
    if value["candidate_id"] != CANDIDATE_ID or value["schema"] != "P13_SAFE_PREFLIGHT_V1":
        raise ValueError("preflight identity")
    if value["status"] != "SAFE_PREFLIGHT_FROZEN_FOR_INDEPENDENT_REVIEW":
        raise ValueError("preflight status")
    for key in (
        "external_data_access_count",
        "gpu_hour_count",
        "network_access_count",
        "random_seed_count",
        "registered_audit_count",
    ):
        if value[key] != 0:
            raise ValueError("preflight zero counter: " + key)
    boundary = value["development_execution_boundary"]
    boundary_keys = {
        "development_helper_module_imported_by_unit_tests",
        "fixed_helper_unit_tests_are_nonofficial",
        "official_result_file_count",
        "registered_audit_count",
        "scientific_child_engine_load_count",
        "top_level_run_science_call_count",
    }
    if type(boundary) is not dict or set(boundary) != boundary_keys:
        raise ValueError("preflight development boundary shape")
    if boundary != {
        "development_helper_module_imported_by_unit_tests": True,
        "fixed_helper_unit_tests_are_nonofficial": True,
        "official_result_file_count": 0,
        "registered_audit_count": 0,
        "scientific_child_engine_load_count": 0,
        "top_level_run_science_call_count": 0,
    }:
        raise ValueError("preflight development boundary value")
    if type(value["safe_runtime_probes"]) is not dict or set(value["safe_runtime_probes"]) != {"Q", "R"}:
        raise ValueError("preflight probe inventory")
    if type(value["static_audit"]) is not dict or not value["static_audit"]:
        raise ValueError("preflight static audit")
    if value["source_bindings"] != {
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "source_review_sha256": SOURCE_REVIEW_SHA256,
    }:
        raise ValueError("preflight source binding")


def _preflight_record(payload: bytes, fresh_preflight):
    value = strict_canonical_load(payload)
    _validate_preflight_shape(value)
    fresh_bytes = canonical_bytes(fresh_preflight)
    if payload != fresh_bytes:
        raise RuntimeError("stored preflight is not a fresh live recomputation")
    return {
        "sha256": sha256_bytes(payload),
        "status": value["status"],
    }


def build_code_manifest(project_root: Path):
    code_files = _code_files(project_root)
    if not code_files:
        raise RuntimeError("empty code tree")
    closure_lines = [
        path + "\u0000" + record["sha256"] + "\n"
        for path, record in sorted(code_files.items())
    ]
    tree_sha256 = sha256_bytes("".join(closure_lines).encode("utf-8"))
    junit_bytes = read_regular_bytes(project_root / JUNIT_RELATIVE)
    preflight_bytes = read_regular_bytes(project_root / PREFLIGHT_RELATIVE)
    preflight_record = _preflight_record(preflight_bytes, collect_preflight(project_root))
    return {
        "candidate_id": CANDIDATE_ID,
        "code_file_count": len(code_files),
        "code_files": code_files,
        "code_tree_algorithm": "sha256 of UTF-8 sorted path+NUL+file-sha256+LF records",
        "code_tree_sha256": tree_sha256,
        "junit_sha256": sha256_bytes(junit_bytes),
        "junit_record": _junit_record(junit_bytes, tree_sha256),
        "preflight_record": preflight_record,
        "preflight_sha256": preflight_record["sha256"],
        "registered_audit_count_at_freeze": 0,
        "schema": "P13_CODE_MANIFEST_V1",
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "source_review_sha256": SOURCE_REVIEW_SHA256,
        "status": "CODE_FROZEN_FOR_INDEPENDENT_DEPLOYMENT_REVIEW",
    }


def validate_manifest_object(project_root: Path, manifest):
    fresh = build_code_manifest(project_root)
    if canonical_bytes(fresh) != canonical_bytes(manifest):
        raise RuntimeError("code manifest drift")
    return fresh
