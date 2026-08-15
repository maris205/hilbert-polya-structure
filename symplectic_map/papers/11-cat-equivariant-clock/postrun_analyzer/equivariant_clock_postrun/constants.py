"""Frozen bindings for the separate post-run analyzer tree."""

from __future__ import annotations

from typing import Final


CANDIDATE_ID: Final = "cat_equivariant_retention_tradeoff_v1"
SOURCE_LOCK_SHA256: Final = (
    "331a1f9004f83c7979daf8eacddd6844072c6b5b7068293c1276985cf6aaa87b"
)
EXECUTION_TREE_SHA256: Final = (
    "5ee1918a57fee56a2ca5a117c5749f614efbfd6baed96ae45480d6091a4741eb"
)
TERMINAL_CLASSIFICATION: Final = (
    "EQUIVARIANT_RETENTION_COMPRESSION_TRADEOFF_CERTIFIED / "
    "A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC / ROUTE_B_NOT_OPENED"
)
LOCKED_MODULI: Final = (2, 3, 5, 7, 11, 4, 6, 9, 10)
EXPECTED_LEDGER: Final = {
    2: (3, 3, 1),
    3: (8, 4, 2),
    5: (20, 10, 2),
    7: (48, 8, 6),
    11: (100, 5, 20),
    4: (12, 3, 4),
    6: (24, 12, 2),
    9: (72, 12, 6),
    10: (60, 30, 2),
}
CONTROL_KEYS: Final = frozenset(f"K{index:03d}" for index in range(1, 13))

# These bytes are immutable.  The analyzer may only observe them.
IMMUTABLE_ARTIFACTS: Final = {
    "results/CODE_REVIEW.md": (
        "3cfe1a34677ef5af06d1a8448de74f5d5dc202dc0136ccf51bfd88f3915110c5",
        10377,
    ),
    "results/PRE_EXECUTION_TESTS.xml": (
        "4cf187fbd29f8a2b89dae2035a0971086b70108e395629ef198fcfc4869307ff",
        2214,
    ),
    "results/PRE_EXECUTION_AUDIT.json": (
        "429c43d1002b5e51ad60ee7614f3156081f32651972500624d05185694996479",
        18510,
    ),
    "results/registered_run.claim.json": (
        "c58c9bc93d0e6af2440c163323d7dcc3c098a0c470f0f11bfb31fa98fb82c79f",
        970,
    ),
    "results/EXPERIMENT_RESULTS.json": (
        "bef8aa5d632ed11b1ca58a123bbfe967a5426e2049d862118a373e4c1dc005fe",
        4129468,
    ),
    "results/registered_run.json": (
        "e6ec2c40094a933a3b6f18a46afb36df538e84fb8afee9b63ba6ab166acbe983",
        919,
    ),
    "results/POSTRUN_TESTS.xml": (
        "a4bd081c0ac9bd8ab9efca301d01c858e5e90a43e9c2796acc0431d79df0287f",
        2214,
    ),
    "results/INDEPENDENT_RESULT_INTEGRITY.md": (
        "c91737c8bf860bd559eebebe08420fc5d095800c47d132381f584e918e714a20",
        15759,
    ),
    "experiments/OFFICIAL_EXPERIMENT_RESULTS.md": (
        "06f547fdfbbfb3bd51a57041758a49f18acceca9dda8e19967c2364500d64918",
        5482,
    ),
    "experiments/OFFICIAL_VALIDATION_REPORT.md": (
        "754a36c0e2e6b5c5002ecb8b3473d0af0e077b4f5b88da2bc6851bdafad23221",
        4166,
    ),
}

EXECUTION_TREE_FILES: Final = (
    "code/README.md",
    "code/equivariant_clock/__init__.py",
    "code/equivariant_clock/candidate.py",
    "code/equivariant_clock/cli.py",
    "code/equivariant_clock/constants.py",
    "code/equivariant_clock/cyclic_cset.py",
    "code/equivariant_clock/finite_module.py",
    "code/equivariant_clock/gates.py",
    "code/equivariant_clock/invariants.py",
    "code/equivariant_clock/lifecycle.py",
    "code/equivariant_clock/manifest.py",
    "code/equivariant_clock/protocol.py",
    "code/equivariant_clock/review.py",
    "code/scripts/build_result_manifest.py",
    "code/scripts/run_registered_audit.py",
    "code/scripts/run_safe_preflight.py",
    "code/scripts/show_code_hash.py",
    "code/tests/test_candidate_contract.py",
    "code/tests/test_cyclic_cset.py",
    "code/tests/test_gates.py",
    "code/tests/test_import_boundary.py",
    "code/tests/test_invariants.py",
    "code/tests/test_lifecycle.py",
    "code/tests/test_manifest.py",
    "code/tests/test_protocol_security.py",
    "code/tests/test_review.py",
    "experiments/EXPERIMENT_PLAN.md",
    "experiments/EXPERIMENT_TRACKER.md",
    "experiments/source_lock.json",
    "notes/CITATION_VERIFICATION.md",
    "notes/CLAIMS_EVIDENCE_MATRIX.md",
    "notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md",
    "notes/INDEPENDENT_SOURCE_LOCK_REVIEW_R2.md",
    "notes/NOVELTY_ASSESSMENT.md",
    "notes/PROOF_PACKAGE.md",
    "notes/RESEARCH_QUESTION.md",
)
EXECUTION_CODE_FILES: Final = frozenset(
    path.removeprefix("code/") for path in EXECUTION_TREE_FILES if path.startswith("code/")
)
EXECUTION_CODE_DIRECTORIES: Final = frozenset({"equivariant_clock", "scripts", "tests"})

ANALYZER_FILES: Final = frozenset(
    {
        "README.md",
        "equivariant_clock_postrun/__init__.py",
        "equivariant_clock_postrun/audit.py",
        "equivariant_clock_postrun/constants.py",
        "equivariant_clock_postrun/manifest.py",
        "equivariant_clock_postrun/protocol.py",
        "equivariant_clock_postrun/review.py",
        "scripts/build_result_manifest_v2.py",
        "scripts/run_safe_analyzer_audit.py",
        "scripts/show_analyzer_hash.py",
        "tests/test_analyzer_contract.py",
        "tests/test_manifest_closure.py",
    }
)
ANALYZER_DIRECTORIES: Final = frozenset(
    {"equivariant_clock_postrun", "scripts", "tests"}
)

ANALYZER_JUNIT_PATH: Final = "results/POSTRUN_ANALYZER_PYTEST.xml"
ANALYZER_REVIEW_PATH: Final = "results/POSTRUN_ANALYZER_REVIEW.md"
RESULT_MANIFEST_PATH: Final = "results/result_manifest.json"

BASE_RESULT_FILES: Final = frozenset(
    {
        "CODE_REVIEW.md",
        "EXPERIMENT_RESULTS.json",
        "INDEPENDENT_RESULT_INTEGRITY.md",
        "POSTRUN_TESTS.xml",
        "PRE_EXECUTION_AUDIT.json",
        "PRE_EXECUTION_TESTS.xml",
        "registered_run.claim.json",
        "registered_run.json",
    }
)
PREWRITE_RESULT_FILES: Final = BASE_RESULT_FILES | {
    "POSTRUN_ANALYZER_PYTEST.xml",
    "POSTRUN_ANALYZER_REVIEW.md",
}
FINAL_RESULT_FILES: Final = PREWRITE_RESULT_FILES | {"result_manifest.json"}
MANIFEST_RECORD_PATHS: Final = tuple(
    sorted(
        {"experiments/source_lock.json"}
        | set(IMMUTABLE_ARTIFACTS)
        | {ANALYZER_JUNIT_PATH, ANALYZER_REVIEW_PATH}
    )
)

ANALYZER_AUTHORITY_PREFIX: Final = "EQUIVARIANT_CLOCK_POSTRUN_ANALYZER_REVIEW_V1 "
ANALYZER_AUTHORITY_KEYS: Final = frozenset(
    {
        "analyzer_junit_sha256",
        "analyzer_tree_sha256",
        "candidate_id",
        "execution_code_sha256",
        "registered_result_sha256",
        "result_review_sha256",
        "reviewer_independent",
        "source_lock_sha256",
        "verdict",
    }
)

REQUIRED_ANALYZER_TESTS: Final = frozenset(
    {
        "test_analyzer_import_is_science_free_and_execution_tree_is_immutable",
        "test_analyzer_review_authority_is_canonical_duplicate_and_stale_closed",
        "test_analyzer_tree_inventory_rejects_extra_and_symlink",
        "test_corrected_k005_requires_singleton_json_lists_and_detects_tampering",
        "test_exact_legacy_k005_failure_is_reproduced_without_artifact_mutation",
        "test_immutable_chain_and_result_authorities_are_exact",
        "test_manifest_prewrite_one_shot_final_closure_and_second_write_reject",
        "test_manifest_rejects_changed_missing_extra_symlink_and_json_tampering",
        "test_prewrite_inventory_rejects_missing_extra_and_symlink",
        "test_strict_json_rejects_duplicate_float_constant_and_trailing_data",
    }
)

FIRST_MANIFEST_ATTEMPT: Final = {
    "attempt_index": 1,
    "builder": "IMMUTABLE_EXECUTION_TREE_V1_BUILDER",
    "failure_code": "CONTROLS_NOT_EXACT_RECOMPUTED_TRUE",
    "manifest_created": False,
    "root_cause": "K005_JSON_LIST_COMPARED_TO_PYTHON_TUPLE",
    "state": "FAILED_PREWRITE_NO_FILE",
}
