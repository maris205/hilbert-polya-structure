from copy import deepcopy
import xml.etree.ElementTree as ET

import pytest

from candidate_v1.bootstrap.canonical import canonical_bytes
from candidate_v1.bootstrap.constants import CANDIDATE_ID, SOURCE_LOCK_SHA256, SOURCE_REVIEW_SHA256
from candidate_v1.bootstrap.manifest import EXPECTED_TEST_IDS, _junit_record, _preflight_record


CODE_TREE = "a" * 64


def _exact_junit():
    root = ET.Element("testsuites", {"errors": "0", "failures": "0", "skipped": "0", "tests": str(len(EXPECTED_TEST_IDS))})
    suite = ET.SubElement(root, "testsuite", {"errors": "0", "failures": "0", "skipped": "0", "tests": str(len(EXPECTED_TEST_IDS))})
    properties = ET.SubElement(suite, "properties")
    ET.SubElement(properties, "property", {"name": "p13_code_tree_sha256", "value": CODE_TREE})
    for identifier in EXPECTED_TEST_IDS:
        classname, name = identifier.split("::", 1)
        ET.SubElement(suite, "testcase", {"classname": classname, "name": name})
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def _preflight():
    return {
        "candidate_id": CANDIDATE_ID,
        "development_execution_boundary": {
            "development_helper_module_imported_by_unit_tests": True,
            "fixed_helper_unit_tests_are_nonofficial": True,
            "official_result_file_count": 0,
            "registered_audit_count": 0,
            "scientific_child_engine_load_count": 0,
            "top_level_run_science_call_count": 0,
        },
        "external_data_access_count": 0,
        "gpu_hour_count": 0,
        "network_access_count": 0,
        "random_seed_count": 0,
        "registered_audit_count": 0,
        "safe_runtime_probes": {"Q": {}, "R": {}},
        "schema": "P13_SAFE_PREFLIGHT_V1",
        "source_bindings": {
            "source_lock_sha256": SOURCE_LOCK_SHA256,
            "source_review_sha256": SOURCE_REVIEW_SHA256,
        },
        "static_audit": {"exact_engine_count": 2},
        "status": "SAFE_PREFLIGHT_FROZEN_FOR_INDEPENDENT_REVIEW",
    }


def test_junit_parser_accepts_exact_expected_inventory_and_code_tree():
    record = _junit_record(_exact_junit(), CODE_TREE)
    assert record["test_ids"] == list(EXPECTED_TEST_IDS)
    assert record["test_count"] == len(EXPECTED_TEST_IDS)
    assert record["failure_count"] == record["error_count"] == record["skipped_count"] == 0


def test_junit_parser_rejects_empty_declared_suite_and_child_failures():
    empty = b'<testsuite tests="0" failures="0" errors="0" skipped="0" />'
    with pytest.raises(ValueError, match="no testcases"):
        _junit_record(empty, CODE_TREE)

    valid_root = ET.fromstring(_exact_junit())
    ET.SubElement(valid_root, "testsuite", {"tests": "0", "failures": "0", "errors": "0", "skipped": "0"})
    with pytest.raises(ValueError, match="no testcases"):
        _junit_record(ET.tostring(valid_root), CODE_TREE)

    duplicate_properties = ET.fromstring(_exact_junit())
    first_suite = duplicate_properties.find("testsuite")
    first_suite.insert(1, ET.Element("properties"))
    with pytest.raises(ValueError, match="properties"):
        _junit_record(ET.tostring(duplicate_properties), CODE_TREE)

    suite_failure = ET.fromstring(_exact_junit())
    suite_failure.find("testsuite").append(ET.Element("failure"))
    with pytest.raises(ValueError, match="suite-level"):
        _junit_record(ET.tostring(suite_failure), CODE_TREE)

    nested_failure = ET.fromstring(_exact_junit())
    testcase = nested_failure.find("testsuite/testcase")
    output = ET.SubElement(testcase, "system-out")
    ET.SubElement(output, "failure")
    with pytest.raises(ValueError, match="nested"):
        _junit_record(ET.tostring(nested_failure), CODE_TREE)


def test_manifest_preflight_parser_rejects_noncanonical_shape_and_staleness():
    value = _preflight()
    payload = canonical_bytes(value)
    assert _preflight_record(payload, value)["status"] == value["status"]
    stale = deepcopy(value)
    stale["static_audit"]["exact_engine_count"] = 3
    with pytest.raises(RuntimeError, match="fresh live recomputation"):
        _preflight_record(payload, stale)
    with pytest.raises(ValueError):
        _preflight_record(payload.replace(b'"candidate_id"', b' "candidate_id"', 1), value)
    malformed = deepcopy(value)
    malformed["extra"] = 0
    with pytest.raises(ValueError, match="top-level"):
        _preflight_record(canonical_bytes(malformed), malformed)
