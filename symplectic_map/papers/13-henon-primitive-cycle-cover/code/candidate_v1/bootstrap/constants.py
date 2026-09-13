"""Frozen identifiers and paths for the Paper 13 pre-execution package."""

from pathlib import Path


CANDIDATE_ID = "henon_primitive_cycle_cover_v1"
CANDIDATE_VERSION = 1
REGISTERED_RUN_ID = "R100"
REGISTERED_TRACK_TIMEOUT_SECONDS = 30
SOURCE_LOCK_SHA256 = "11d51aae93f4230a06046de7c3c8331a7e00169b69295d335435f470f9ff9469"
SOURCE_REVIEW_SHA256 = "83b380d5fa1d5e2161281052ea69b447f6c26831f0cf0d818eced8affecd6c8e"

SOURCE_LOCK_RELATIVE = Path("experiments/source_lock.json")
SOURCE_REVIEW_RELATIVE = Path("notes/INDEPENDENT_SOURCE_LOCK_REVIEW_R2.md")
CODE_RELATIVE = Path("code")
DEFINITIONS_RELATIVE = Path("code/candidate_v1/shared/definitions.json")
ACCEPTANCE_LEDGER_RELATIVE = Path("code/candidate_v1/adjudicator/acceptance_ledger.json")
Q_RUNNER_RELATIVE = Path("code/candidate_v1/track_q/runner.py")
Q_ENGINE_RELATIVE = Path("code/candidate_v1/track_q/engine.py")
Q_FIXTURE_RELATIVE = Path("code/candidate_v1/track_q/private_fixture.json")
R_RUNNER_RELATIVE = Path("code/candidate_v1/track_r/runner.py")
R_ENGINE_RELATIVE = Path("code/candidate_v1/track_r/engine.py")
R_FIXTURE_RELATIVE = Path("code/candidate_v1/track_r/private_fixture.json")

PREEXECUTION_RELATIVE = Path("preexecution")
JUNIT_RELATIVE = Path("preexecution/junit.xml")
PREFLIGHT_RELATIVE = Path("preexecution/preflight.json")
CODE_MANIFEST_RELATIVE = Path("preexecution/code_manifest.json")
DEPLOYMENT_REVIEW_RELATIVE = Path("preexecution/INDEPENDENT_DEPLOYMENT_REVIEW.json")

RUNTIME_RELATIVE = Path("runtime/candidate_v1")
OFFICIAL_RELATIVE = RUNTIME_RELATIVE / "official"
CLAIM_RELATIVE = OFFICIAL_RELATIVE / "durable_claim.json"
EXECUTION_STAGE_RELATIVE = OFFICIAL_RELATIVE / "execution_started.json"
TERMINAL_RELATIVE = OFFICIAL_RELATIVE / "terminal.json"
RAW_RESULT_RELATIVE = OFFICIAL_RELATIVE / "raw_result.json"
RESULT_MANIFEST_RELATIVE = OFFICIAL_RELATIVE / "result_manifest.json"
Q_STAGE_RELATIVE = RUNTIME_RELATIVE / "staging/track_q/envelope.json"
R_STAGE_RELATIVE = RUNTIME_RELATIVE / "staging/track_r/envelope.json"

FORBIDDEN_SCIENCE_COMPONENTS = frozenset(
    {
        "experiments",
        "notes",
        "refine-logs",
        "adjudicator",
        "preexecution",
        "runtime",
    }
)


def project_root_from_bootstrap() -> Path:
    return Path(__file__).resolve().parents[3]
