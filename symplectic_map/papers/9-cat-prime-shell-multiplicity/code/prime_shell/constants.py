"""Immutable Paper 9 inputs, bindings, schemas, and closed-world inventory."""

from __future__ import annotations

from typing import Final


CANDIDATE_ID: Final = "cat_prime_shell_multiplicity_obstruction_v1"
SOURCE_LOCK_SHA256: Final = (
    "662809d40f7e409e439983774a36349b90f265616a488061fda3c5b9064c2d49"
)
SOURCE_REVIEW_SHA256: Final = (
    "9509278ce55d908dba7d7cb4a809a335cc51d9364e8bfdfd1dc66be594775b8f"
)

CAT_MATRIX: Final = ((2, 1), (1, 1))
IDENTITY: Final = ((1, 0), (0, 1))
LOCKED_PRIMES: Final = (2, 3, 5, 7, 11)
REPEATS: Final = (1, 2, 3)

LOCAL_BINDINGS: Final = {
    "research_question_sha256": (
        "notes/RESEARCH_QUESTION.md",
        "79339c412dc9df2d7babb3ff5b0bf19b5255a2ddc989ac72440200bfeb8563fc",
    ),
    "novelty_assessment_sha256": (
        "notes/NOVELTY_ASSESSMENT.md",
        "71de2f31ce196e06a4600f0fbc931e7ff707e8634f88fbb6e8d5698b3a4a75a0",
    ),
    "claims_evidence_matrix_sha256": (
        "notes/CLAIMS_EVIDENCE_MATRIX.md",
        "cbf2f23b6ea3c24b97f731adb3be22c2a685e698f5eb7ea888f1c40b1c6ce8fa",
    ),
    "proof_package_sha256": (
        "notes/PROOF_PACKAGE.md",
        "47216ad4021d3476bfd0850ebec24c9ceafb5af8c0573214182fd2d0da7b2daa",
    ),
    "experiment_plan_sha256": (
        "experiments/EXPERIMENT_PLAN.md",
        "6a58e26935a3e406adfa723a2ab304880709667940b76b85707f82f844f94cc5",
    ),
    "experiment_tracker_sha256": (
        "experiments/EXPERIMENT_TRACKER.md",
        "00fc66f266b7a1ddcccc0b355ff7dbb6ea787f1d60319862dbd7d5da6262d0b9",
    ),
}

UPSTREAM_BINDINGS: Final = {
    "source_lock_sha256": (
        "../8-cat-torsion-capacity/experiments/source_lock.json",
        "87d80da28cacb349c0e277b8f73812287eeb6f8a2e244945a05f90a2f6269dce",
    ),
    "proof_package_sha256": (
        "../8-cat-torsion-capacity/notes/PROOF_PACKAGE.md",
        "ee02fe72071c0bbea26f5f34c28130374fe1a919195cfbe154f6f5a39ab420af",
    ),
    "raw_result_sha256": (
        "../8-cat-torsion-capacity/results/EXPERIMENT_RESULTS.json",
        "0d8054ad36ad8cdef1496948cf5dd98d6a1a55c186d68124f45a5e6e35bddaa0",
    ),
    "result_manifest_sha256": (
        "../8-cat-torsion-capacity/results/result_manifest.json",
        "045f3c3d935cd5670e900a210be9d26a2e272bd715c8e0b997da6510efd7d49f",
    ),
    "official_result_report_sha256": (
        "../8-cat-torsion-capacity/experiments/OFFICIAL_EXPERIMENT_RESULTS.md",
        "4cf1645505a835a9d0aa62d84e7b6b47fc708b1347a954eeac26eb9710b9187d",
    ),
    "official_validation_report_sha256": (
        "../8-cat-torsion-capacity/experiments/OFFICIAL_VALIDATION_REPORT.md",
        "ac9ac741cffd89dc8ab32db654ae59dc901b823a4b496be0607c7ce05fd403c3",
    ),
}

EXPECTED_LEDGER: Final = {
    2: {
        "case": "binary_inert",
        "point_period_profile": {3: 3},
        "cycle_profile": {3: 1},
        "m_p": 1,
        "eigenline_cycles": None,
        "off_eigenline_cycles": None,
    },
    3: {
        "case": "inert",
        "point_period_profile": {4: 8},
        "cycle_profile": {4: 2},
        "m_p": 2,
        "eigenline_cycles": None,
        "off_eigenline_cycles": None,
    },
    5: {
        "case": "ramified",
        "point_period_profile": {2: 4, 10: 20},
        "cycle_profile": {2: 2, 10: 2},
        "m_p": 4,
        "eigenline_cycles": None,
        "off_eigenline_cycles": None,
    },
    7: {
        "case": "inert",
        "point_period_profile": {8: 48},
        "cycle_profile": {8: 6},
        "m_p": 6,
        "eigenline_cycles": None,
        "off_eigenline_cycles": None,
    },
    11: {
        "case": "split",
        "point_period_profile": {5: 120},
        "cycle_profile": {5: 24},
        "m_p": 24,
        "eigenline_cycles": 4,
        "off_eigenline_cycles": 20,
    },
}

EXPECTED_RAW_FACTORS: Final = {
    2: "(1-2^(-3s))^(-1)",
    3: "(1-3^(-4s))^(-2)",
    5: "(1-5^(-2s))^(-2)*(1-5^(-10s))^(-2)",
    7: "(1-7^(-8s))^(-6)",
    11: "(1-11^(-5s))^(-24)",
}

REQUIRED_ANALYTIC_CONTRACTS: Final = (
    "DIVERGES_REAL_1_LT_SIGMA_LE_2",
    "NOT_ABSOLUTE_1_LT_SIGMA_LE_2",
    "ABSOLUTE_SIGMA_GT_3",
)
OUTSIDE_SCOPE_ESCAPES: Final = (
    "CENTRALIZER_QUOTIENT",
    "MATRIX_VALUED_WEIGHTS",
    "NUMERATOR_OR_ALTERNATING_CANCELLATION",
    "TRANSFER_OR_FREDHOLM_DETERMINANT",
    "COHOMOLOGICAL_SUPERDETERMINANT",
    "ENRICHED_ORBIT_SELECTOR",
)
TERMINAL_LABELS: Final = (
    "PRIME_SHELL_MULTIPLICITY_OBSTRUCTION_CERTIFIED",
    "P2_UNIQUE_SINGLE_ORBIT_SHELL",
    "ODD_PRIME_MULTIPLICITY_AT_LEAST_P_MINUS_1",
    "RAW_RETURN_AND_ORBIT_LABEL_PRODUCTS_DISTINCT",
    "PURE_NONZERO_SCALAR_DENOMINATOR_COLLAPSE_REJECTED",
    "A0_FAIL_GLOBAL_NORMALIZATION_ONLY",
    "CENTRALIZER_QUOTIENT_RESERVED_FOR_PAPER10",
    "ROUTE_B_NOT_OPENED",
)

CODE_FILES: Final = frozenset(
    {
        "README.md",
        "prime_shell/__init__.py",
        "prime_shell/candidate.py",
        "prime_shell/cli.py",
        "prime_shell/constants.py",
        "prime_shell/finite_field.py",
        "prime_shell/gates.py",
        "prime_shell/lifecycle.py",
        "prime_shell/manifest.py",
        "prime_shell/mechanisms.py",
        "prime_shell/proof_contract.py",
        "prime_shell/protocol.py",
        "prime_shell/review.py",
        "prime_shell/symbolic.py",
        "scripts/build_result_manifest.py",
        "scripts/run_registered_audit.py",
        "scripts/run_safe_preflight.py",
        "scripts/show_code_hash.py",
        "tests/test_candidate_contract.py",
        "tests/test_finite_field.py",
        "tests/test_gates.py",
        "tests/test_lifecycle.py",
        "tests/test_manifest.py",
        "tests/test_mechanisms.py",
        "tests/test_protocol_security.py",
        "tests/test_review.py",
        "tests/test_symbolic.py",
    }
)
CODE_DIRECTORIES: Final = frozenset({"prime_shell", "scripts", "tests"})

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
