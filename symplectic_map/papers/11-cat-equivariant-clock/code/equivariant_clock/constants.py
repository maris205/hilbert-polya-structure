"""Immutable source bindings, scientific literals, schemas, and inventory."""

from __future__ import annotations

from typing import Final


CANDIDATE_ID: Final = "cat_equivariant_retention_tradeoff_v1"
SOURCE_LOCK_SHA256: Final = (
    "331a1f9004f83c7979daf8eacddd6844072c6b5b7068293c1276985cf6aaa87b"
)
SOURCE_REVIEW_R1_SHA256: Final = (
    "233da2cb9707f340e7dec588437f694133af63f30bc17c0547dd2a9032a1c17a"
)
SOURCE_REVIEW_R2_SHA256: Final = (
    "2f75d6934e3d61bdc941ee6689102a1cb08a959270a7cd87965579f1ec5cc622"
)
TERMINAL_CLASSIFICATION: Final = (
    "EQUIVARIANT_RETENTION_COMPRESSION_TRADEOFF_CERTIFIED / "
    "A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC / ROUTE_B_NOT_OPENED"
)

CAT_MATRIX: Final = ((2, 1), (1, 1))
IDENTITY: Final = ((1, 0), (0, 1))
BASE_VECTOR: Final = (1, 0)
LOCKED_MODULI: Final = (2, 3, 5, 7, 11, 4, 6, 9, 10)
LOCKED_PRIMES: Final = (2, 3, 5, 7, 11)
LOCKED_COMPOSITES: Final = (4, 6, 9, 10)
STRUCTURAL_CONTROL: Final = (6, ((2, 1), (3, 1)), 1)

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
LEDGER_FIELDS: Final = ("n", "r", "m")
PERIOD_COLLISIONS: Final = (((2, 4), 3), ((6, 9), 12))

LOCAL_BINDINGS: Final = {
    "research_question_sha256": (
        "notes/RESEARCH_QUESTION.md",
        "f695dd359e4f965fcf13e7c4550daf9ae90ce6565fbdb61a8c3a39fb2cee174a",
    ),
    "novelty_assessment_sha256": (
        "notes/NOVELTY_ASSESSMENT.md",
        "1dbd6e4dc07fbc1e126334f6484a71b77852f0583749ba64259bd0e603669c95",
    ),
    "proof_package_sha256": (
        "notes/PROOF_PACKAGE.md",
        "3d723fdb02c89f9b2f281da807bcd745c5991393d25e223f95d6673961c20948",
    ),
    "claims_evidence_matrix_sha256": (
        "notes/CLAIMS_EVIDENCE_MATRIX.md",
        "0ea191ebb1f6f0f915db096a68606099d4a315d80d333adadd3e396b11885490",
    ),
    "experiment_plan_sha256": (
        "experiments/EXPERIMENT_PLAN.md",
        "2e69d035a315061cf0cbc9608fae66cbc2545480b84dabaa6e20b3a40f3409e5",
    ),
    "experiment_tracker_sha256": (
        "experiments/EXPERIMENT_TRACKER.md",
        "a02e413ba9e493b38588f7809172e03a8b6c07c9d6b102f407b12b829194dc81",
    ),
}
CITATION_BINDING: Final = (
    "notes/CITATION_VERIFICATION.md",
    "1bfc33598d9ff5e5a8636a9ba5f8365ef9c3176614ba90a2b64ae1eb6dc4154b",
)
SOURCE_REVIEW_BINDINGS: Final = (
    (
        "notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md",
        SOURCE_REVIEW_R1_SHA256,
        "REPAIR_REQUIRED",
    ),
    (
        "notes/INDEPENDENT_SOURCE_LOCK_REVIEW_R2.md",
        SOURCE_REVIEW_R2_SHA256,
        "SOURCE_LOCK_PASS",
    ),
)

UPSTREAM_PAPER9_BINDINGS: Final = {
    "source_lock_sha256": (
        "../9-cat-prime-shell-multiplicity/experiments/source_lock.json",
        "662809d40f7e409e439983774a36349b90f265616a488061fda3c5b9064c2d49",
    ),
    "final_integrity_sha256": (
        "../9-cat-prime-shell-multiplicity/paper/FINAL_INTEGRITY.md",
        "7abbf1d25a3d57ccf3f195aa633237d2e641073ba647dcaacd6a177d7c66a712",
    ),
    "final_pdf_sha256": (
        "../9-cat-prime-shell-multiplicity/paper/paper_final.pdf",
        "96a560712ae7fb34e1d0ecfcd59e9b2c210ad61fe8ee0537c3a5ff5c860b4cd6",
    ),
}
UPSTREAM_PAPER10_BINDINGS: Final = {
    "source_lock_sha256": (
        "../10-cat-centralizer-quotient/experiments/source_lock.json",
        "aa99218099f2e2c3e14367bfe75f9da881d8b204689c07c6fa963f9582b696e2",
    ),
    "independent_source_review_sha256": (
        "../10-cat-centralizer-quotient/notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md",
        "a551784d205d9ef52ce6a493ab66cb7295a4a9dadbeb8bb2353fc58e3011dff5",
    ),
    "raw_result_sha256": (
        "../10-cat-centralizer-quotient/results/EXPERIMENT_RESULTS.json",
        "8dceb1b8a63db462c1fd55a242ea35de974f73b6c80da68517b91c9eebb214ff",
    ),
    "result_manifest_sha256": (
        "../10-cat-centralizer-quotient/results/result_manifest.json",
        "db1dda86ff8bf13fd307cbb1eb6ea6a8c3c0de531ea5b1cc28a58c7bb085b658",
    ),
    "independent_result_integrity_sha256": (
        "../10-cat-centralizer-quotient/results/INDEPENDENT_RESULT_INTEGRITY.md",
        "29264a8fd97d3acf4435ed807294bffcda0844a48728d8572083d92a3bcf5b58",
    ),
    "official_result_report_sha256": (
        "../10-cat-centralizer-quotient/experiments/OFFICIAL_EXPERIMENT_RESULTS.md",
        "1ece7db3fbee75bcecaecb0ad05f89fe88699c4231bea80581f382f33ed3aa6e",
    ),
    "official_validation_report_sha256": (
        "../10-cat-centralizer-quotient/experiments/OFFICIAL_VALIDATION_REPORT.md",
        "f94dbfb28a71aea4dac5e89a8bc2a622bba092b66098c2fc2217ceba19a8ad5a",
    ),
    "final_pdf_sha256": (
        "../10-cat-centralizer-quotient/paper/paper_final.pdf",
        "f685996c741c3e92d4eb18086f2a4e4d898ede10e8124a23991ada3579f8d378",
    ),
    "round2_review_sha256": (
        "../10-cat-centralizer-quotient/paper/reviews/round2_review.md",
        "ca8ee460f0956eb2f653e837402888b9d88d4888ae04ea1ad76231b6764a79ae",
    ),
    "final_integrity_sha256": (
        "../10-cat-centralizer-quotient/paper/FINAL_INTEGRITY.md",
        "e0a4803ff8e2063ebf5766803212579b44cd80c15572b166c1389f0242f8e6ce",
    ),
    "pipeline_state_sha256": (
        "../10-cat-centralizer-quotient/paper/PIPELINE_STATE.json",
        "dc7550b39e42cdeeeacd4ae64f9fb4142b0f2e2e4b315d0e73f1932077e0b09c",
    ),
}

DESIGN_REVIEWED_PATHS: Final = (
    "experiments/source_lock.json",
    "experiments/EXPERIMENT_PLAN.md",
    "experiments/EXPERIMENT_TRACKER.md",
    "notes/RESEARCH_QUESTION.md",
    "notes/NOVELTY_ASSESSMENT.md",
    "notes/PROOF_PACKAGE.md",
    "notes/CLAIMS_EVIDENCE_MATRIX.md",
    "notes/CITATION_VERIFICATION.md",
    "notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md",
    "notes/INDEPENDENT_SOURCE_LOCK_REVIEW_R2.md",
)

PREEXECUTION_TEST_PATH: Final = "results/PRE_EXECUTION_TESTS.xml"
PREEXECUTION_AUDIT_PATH: Final = "results/PRE_EXECUTION_AUDIT.json"
CODE_REVIEW_PATH: Final = "results/CODE_REVIEW.md"
CLAIM_PATH: Final = "results/registered_run.claim.json"
RESULT_PATH: Final = "results/EXPERIMENT_RESULTS.json"
TERMINAL_PATH: Final = "results/registered_run.json"
POSTRUN_TEST_PATH: Final = "results/POSTRUN_TESTS.xml"
RESULT_REVIEW_PATH: Final = "results/INDEPENDENT_RESULT_INTEGRITY.md"
RESULT_MANIFEST_PATH: Final = "results/result_manifest.json"
OFFICIAL_REPORT_PATHS: Final = (
    "experiments/OFFICIAL_EXPERIMENT_RESULTS.md",
    "experiments/OFFICIAL_VALIDATION_REPORT.md",
)

CODE_FILES: Final = frozenset(
    {
        "README.md",
        "equivariant_clock/__init__.py",
        "equivariant_clock/candidate.py",
        "equivariant_clock/cli.py",
        "equivariant_clock/constants.py",
        "equivariant_clock/cyclic_cset.py",
        "equivariant_clock/finite_module.py",
        "equivariant_clock/gates.py",
        "equivariant_clock/invariants.py",
        "equivariant_clock/lifecycle.py",
        "equivariant_clock/manifest.py",
        "equivariant_clock/protocol.py",
        "equivariant_clock/review.py",
        "scripts/build_result_manifest.py",
        "scripts/run_registered_audit.py",
        "scripts/run_safe_preflight.py",
        "scripts/show_code_hash.py",
        "tests/test_candidate_contract.py",
        "tests/test_cyclic_cset.py",
        "tests/test_gates.py",
        "tests/test_invariants.py",
        "tests/test_import_boundary.py",
        "tests/test_lifecycle.py",
        "tests/test_manifest.py",
        "tests/test_protocol_security.py",
        "tests/test_review.py",
    }
)
CODE_DIRECTORIES: Final = frozenset({"equivariant_clock", "scripts", "tests"})
