"""Frozen non-scientific lifecycle constants for Paper 12."""

from pathlib import Path


CANDIDATE_ID = "henon_period3_residue_v1"
SOURCE_LOCK_SHA256 = "2fa930f697f6040cb16916d2b4dba7ec591a712882c108848e9eecf53608e1c2"
SOURCE_REVIEW_SHA256 = "5e66edcd7f33769f748c8b6bd6582aa7e05b3325329839c46bf3627945803d11"
PROOF_SHA256 = "36f2edd5a1a25960a2c656adaeb07fbd4251c61b51c9e0a0382200460b589ba9"
SOURCE_LOCK_PATH = Path("experiments/source_lock.json")
SOURCE_REVIEW_PATH = Path("notes/INDEPENDENT_SOURCE_LOCK_REVIEW_R2.md")
PROOF_PATH = Path("notes/PROOF_PACKAGE.md")
CODE_MANIFEST_PATH = Path("preexecution/code_manifest.json")
CLAIM_SCHEMA_PATH = Path("code/candidate_v1/shared/durable_claim.schema.json")
JUNIT_PATH = Path("preexecution/junit.xml")
PREFLIGHT_PATH = Path("preexecution/preflight.json")
DEPLOYMENT_REVIEW_PATH = Path("preexecution/INDEPENDENT_DEPLOYMENT_REVIEW.json")
RUNTIME_ROOT = Path("runtime/candidate_v1")
CLAIM_PATH = RUNTIME_ROOT / "official/durable_claim.json"
RESULT_PATH = RUNTIME_ROOT / "official/raw_result.json"
TERMINAL_PATH = RUNTIME_ROOT / "official/terminal.json"
RESULT_MANIFEST_PATH = RUNTIME_ROOT / "official/result_manifest.json"
POSTRUN_REVIEW_PATH = RUNTIME_ROOT / "review/INDEPENDENT_RESULT_REVIEW.json"
TRACK_Q_ENVELOPE = RUNTIME_ROOT / "staging/track_q/sealed_envelope.json"
TRACK_R_ENVELOPE = RUNTIME_ROOT / "staging/track_r/sealed_envelope.json"
ADJUDICATED_PATH = RUNTIME_ROOT / "staging/final/adjudicated_science.json"
REGISTERED_INDICES = (8, 9)
TERMINAL_SUCCESS = "REGISTERED_AUDIT_COMPLETED_EXACT_AGREEMENT"
TERMINAL_FAILURE = "REGISTERED_AUDIT_TERMINAL_FAIL"


SOURCE_BINDINGS = {
    "notes/RESEARCH_QUESTION.md": "6feb5c525caecf81fd6e9de98116b9ff0ffc143749e0a586d0dbc131a10e75d8",
    "notes/NOVELTY_ASSESSMENT.md": "c497dc4e2c404fbbfc3c89450991964d1049f06288a051bc647a15005a66146a",
    "notes/PROOF_PACKAGE.md": PROOF_SHA256,
    "notes/CLAIMS_EVIDENCE_MATRIX.md": "5630610bb637e155fa631eb2d9c4b36c6ea334ae976a6ef39a53dd733b8c62de",
    "notes/CITATION_VERIFICATION.md": "eb99e7ab59e5d2947b6d5dab0d23dd471c05d090280f7915f010210b021e39ee",
    "experiments/EXPERIMENT_PLAN.md": "5f93cd0b156f096abab7f366d2bbc209677fb913b0fdfcea14895a1ab3d1eec6",
    "experiments/EXPERIMENT_TRACKER.md": "531d42a7c00847115accb6a54f5c147e3cb0eed2da64c19bc21a0038da001c39",
    "refine-logs/FINAL_PROPOSAL.md": "ff20ef84c3a55900881a5ad4d380ccf840da7b1fd9794c4d26d23e5b78df315f",
    "refine-logs/REFINEMENT_REPORT.md": "0a2d3020c9715bdba6c855dcc1156f49029ff959ed853636572106fea7c014ac",
    "refine-logs/REVIEW_SUMMARY.md": "5a6e67c0bba046ae8540c585cf2ffa116a471ca0b1a66e5ae4b5977b3e26ec6c",
    "refine-logs/INITIAL_PROPOSAL.md": "46984d6028e52842602f5a1d5a4f41b13aa9a840528c21328af3f4eb5ea5c8d6",
    "refine-logs/round-1-review.md": "757279f1b7274f20f619db78f4ae38214927d8ce04161c63d5da89b919ae86ba",
    "refine-logs/round-2-review.md": "7a35bd1feb2283e6934032a489c648e116e712ccbb14d5377c5d9575a7620277",
    "refine-logs/score-history.md": "edd13b5ce88132f6ec08f571885ecb6b6501b2eafacb57c9d4f9df561dd04b28",
}


PRESERVED_R1_PATH = "notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md"
PRESERVED_R1_SHA256 = "e514ec05235be640dc4a8d02df3147d8018df40b445e92a4c6d1d0ffed0aff1f"


NONCLAIMS = (
    "UNIVERSAL_D_M_NONVANISHING_OPEN",
    "NO_ALL_M_PERIOD3_SEPARATION",
    "NO_ALL_QUARTIC_HENON_SEPARATION",
    "NO_GLOBAL_P4_EQUALS_3",
    "NO_FAMILY_OR_LOW_PERIOD_PRIORITY",
    "NO_RESIDUE_METHOD_PRIORITY",
    "NO_HISTORICAL_PRIORITY_FROM_BOUNDED_SEARCH",
)
