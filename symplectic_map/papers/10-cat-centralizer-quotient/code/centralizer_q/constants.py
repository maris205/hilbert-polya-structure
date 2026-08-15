"""Immutable source bindings, finite controls, schemas, and file inventory."""

from __future__ import annotations

from typing import Final


CANDIDATE_ID: Final = "cat_centralizer_cyclic_torsor_v1"
SOURCE_LOCK_SHA256: Final = (
    "aa99218099f2e2c3e14367bfe75f9da881d8b204689c07c6fa963f9582b696e2"
)
SOURCE_REVIEW_SHA256: Final = (
    "a551784d205d9ef52ce6a493ab66cb7295a4a9dadbeb8bb2353fc58e3011dff5"
)
TERMINAL_CLASSIFICATION: Final = (
    "CENTRALIZER_CYCLIC_TORSOR_CERTIFIED / "
    "A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC / ROUTE_B_NOT_OPENED"
)
CAT_MATRIX: Final = ((2, 1), (1, 1))
IDENTITY: Final = ((1, 0), (0, 1))
REVERSOR: Final = ((0, -1), (1, 0))
BASE_VECTOR: Final = (1, 0)
LOCKED_MODULI: Final = (2, 3, 5, 7, 11, 4, 6, 9, 10)
LOCKED_PRIMES: Final = (2, 3, 5, 7, 11)
LOCKED_COMPOSITES: Final = (4, 6, 9, 10)

LOCAL_BINDINGS: Final = {
    "research_question_sha256": (
        "notes/RESEARCH_QUESTION.md",
        "e1b8c735cd06a33e776220b04c5e8927d9d756aafbaa38783a010b7326d86461",
    ),
    "novelty_assessment_sha256": (
        "notes/NOVELTY_ASSESSMENT.md",
        "6ee0fe2aff13c2d4329496e32f2d6aa190a92a3c3b4904168a21828b646de0a5",
    ),
    "claims_evidence_matrix_sha256": (
        "notes/CLAIMS_EVIDENCE_MATRIX.md",
        "03424a71fc8716618545a6c7c8b0fd05f5ad744cff034255ab0337012da0303d",
    ),
    "proof_package_sha256": (
        "notes/PROOF_PACKAGE.md",
        "2eafe71f32c452ff8a20a6818ccb43082e02b866db7353e26c36ff432f1b2a4c",
    ),
    "experiment_plan_sha256": (
        "experiments/EXPERIMENT_PLAN.md",
        "1735bfe8c161d125836529edd17548275368559dee82f00f2a3a616df6f45672",
    ),
    "experiment_tracker_sha256": (
        "experiments/EXPERIMENT_TRACKER.md",
        "6fabe06923b242aab4de7735ee0d87bc20edecaeafc9763161d3ac01d184fc6e",
    ),
}

UPSTREAM_BINDINGS: Final = {
    "source_lock_sha256": (
        "../9-cat-prime-shell-multiplicity/experiments/source_lock.json",
        "662809d40f7e409e439983774a36349b90f265616a488061fda3c5b9064c2d49",
    ),
    "proof_package_sha256": (
        "../9-cat-prime-shell-multiplicity/notes/PROOF_PACKAGE.md",
        "47216ad4021d3476bfd0850ebec24c9ceafb5af8c0573214182fd2d0da7b2daa",
    ),
    "raw_result_sha256": (
        "../9-cat-prime-shell-multiplicity/results/EXPERIMENT_RESULTS.json",
        "448de06e92bd7ab4e5374e5d1f57413df45859cd3476ff14b2691b63ac364fab",
    ),
    "result_manifest_sha256": (
        "../9-cat-prime-shell-multiplicity/results/result_manifest.json",
        "8ca12744638a47b6e4fa3239a60a19d79229d2b9596ae4fe4b2f66a399618f92",
    ),
    "independent_result_integrity_sha256": (
        "../9-cat-prime-shell-multiplicity/results/INDEPENDENT_RESULT_INTEGRITY.md",
        "aa0c7db555f11920c7305be508f6cfff62375970e112e9f720111831da20b3bd",
    ),
    "official_result_report_sha256": (
        "../9-cat-prime-shell-multiplicity/experiments/OFFICIAL_EXPERIMENT_RESULTS.md",
        "66bfefe9dcf5731cb89a0597deed5df322f9bc24f9fc3a592d4790a46d2a4dc0",
    ),
    "official_validation_report_sha256": (
        "../9-cat-prime-shell-multiplicity/experiments/OFFICIAL_VALIDATION_REPORT.md",
        "32a1758362f94372a83588de63e2b5df33a8f7e45e0646de53154a2ca1afaab4",
    ),
    "final_pdf_sha256": (
        "../9-cat-prime-shell-multiplicity/paper/paper_final.pdf",
        "96a560712ae7fb34e1d0ecfcd59e9b2c210ad61fe8ee0537c3a5ff5c860b4cd6",
    ),
    "round2_review_sha256": (
        "../9-cat-prime-shell-multiplicity/paper/reviews/round2_review.md",
        "32cc795c358d979988673658398dd4dbf2768cd9f1b38464b9b438703c2ebd23",
    ),
    "final_integrity_sha256": (
        "../9-cat-prime-shell-multiplicity/paper/FINAL_INTEGRITY.md",
        "7abbf1d25a3d57ccf3f195aa633237d2e641073ba647dcaacd6a177d7c66a712",
    ),
}

EXPECTED_LEDGER: Final = {
    2: ("binary_inert", 3, 3, 0, 3, 3, 3, 1, 1, 1, 1, 1, 1),
    3: ("inert", 8, 8, 0, 8, 4, 4, 2, 1, 2, 1, 2, 1),
    5: ("ramified", 24, 20, 4, 20, 10, 10, 2, 1, 2, 2, 4, 2),
    7: ("inert", 48, 48, 0, 48, 8, 8, 6, 1, 6, 1, 6, 1),
    11: ("split", 120, 100, 20, 100, 10, 5, 20, 1, 10, 3, 12, 2),
    4: ("binary_inert_lift", 12, 12, 0, 12, 6, 3, 4, 1, 2, 1, 2, None),
    6: ("binary_inert_CRT", 24, 24, 0, 24, 12, 12, 2, 1, 2, 1, 2, None),
    9: ("inert_lift", 72, 72, 0, 72, 12, 12, 6, 1, 6, 1, 6, None),
    10: ("binary_ramified_CRT", 72, 60, 12, 60, 30, 30, 2, 1, 2, 2, 4, None),
}
LEDGER_FIELDS: Final = (
    "case",
    "exact_shell_size",
    "cyclic_locus_size",
    "discard_size",
    "full_centralizer_size",
    "symplectic_centralizer_size",
    "A_order",
    "cyclic_A_orbit_count",
    "full_CV_quotient_count",
    "symplectic_CV_quotient_count",
    "full_centralizer_shell_orbits",
    "symplectic_centralizer_shell_orbits",
    "prime_reversing_group_shell_orbits",
)

DESIGN_REVIEWED_PATHS: Final = (
    "experiments/source_lock.json",
    "experiments/EXPERIMENT_PLAN.md",
    "experiments/EXPERIMENT_TRACKER.md",
    "notes/RESEARCH_QUESTION.md",
    "notes/NOVELTY_ASSESSMENT.md",
    "notes/CLAIMS_EVIDENCE_MATRIX.md",
    "notes/PROOF_PACKAGE.md",
    "notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md",
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
        "centralizer_q/__init__.py",
        "centralizer_q/candidate.py",
        "centralizer_q/cli.py",
        "centralizer_q/constants.py",
        "centralizer_q/finite_module.py",
        "centralizer_q/gates.py",
        "centralizer_q/lifecycle.py",
        "centralizer_q/manifest.py",
        "centralizer_q/protocol.py",
        "centralizer_q/review.py",
        "scripts/build_result_manifest.py",
        "scripts/run_registered_audit.py",
        "scripts/run_safe_preflight.py",
        "scripts/show_code_hash.py",
        "tests/test_candidate_contract.py",
        "tests/test_gates.py",
        "tests/test_lifecycle.py",
        "tests/test_manifest.py",
        "tests/test_math.py",
        "tests/test_protocol_security.py",
        "tests/test_review.py",
    }
)
CODE_DIRECTORIES: Final = frozenset({"centralizer_q", "scripts", "tests"})
