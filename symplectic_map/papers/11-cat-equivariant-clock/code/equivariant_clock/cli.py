"""Commands with no configurable scientific inputs."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .constants import CLAIM_PATH, PREEXECUTION_AUDIT_PATH, RESULT_PATH, TERMINAL_PATH
from .gates import collect_safe_preflight, write_safe_preflight
from .lifecycle import claim_registered_run, validate_claim, write_terminal
from .protocol import code_tree_sha256, lexical_absolute, regular_file, sha256_file, write_json
from .review import validate_deployment_authority


def project_root() -> Path:
    return lexical_absolute(Path(__file__).parents[2])


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Source-locked exact equivariant-clock audit")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("code-hash", help="print framed reviewed-tree SHA-256")
    subparsers.add_parser("safe-preflight", help="run non-candidate gates")
    subparsers.add_parser("registered", help="run the one-shot audit after review PASS")
    subparsers.add_parser("postrun-audit", help="validate evidence without a registered rerun")
    subparsers.add_parser("result-manifest", help="write strict one-shot result manifest")
    return parser


def load_postclaim_science(root: Path, reviewed_code_sha256: str):
    """Import the candidate and semantic engine only after a live durable claim."""

    claim = validate_claim(root, reviewed_code_sha256)
    if claim["pass"] is not True:
        raise RuntimeError("durable registered claim is not live and exact")
    from .candidate import RegisteredCandidateFailure, run_registered_candidate
    from .manifest import validate_registered_result

    return claim, RegisteredCandidateFailure, run_registered_candidate, validate_registered_result


def run_registered(root: Path) -> tuple[Path, Path]:
    if any(regular_file(root / relative) for relative in (CLAIM_PATH, RESULT_PATH, TERMINAL_PATH)):
        raise RuntimeError("registered lifecycle already claimed; rerun forbidden")
    preflight = collect_safe_preflight(root)
    if preflight.get("pass") is not True or preflight.get("status") != "AUTHORIZED_FOR_REGISTERED_EXECUTION":
        raise RuntimeError("fresh hash-bound DEPLOYMENT_PASS is missing or stale")
    write_json(root / PREEXECUTION_AUDIT_PATH, preflight)
    code_sha = code_tree_sha256(root)
    review = validate_deployment_authority(root)
    review_sha = review.get("review_file_sha256")
    if type(review_sha) is not str:
        raise RuntimeError("deployment review hash unavailable")
    claim_registered_run(
        root,
        reviewed_code_sha256=code_sha,
        review_file_sha256=review_sha,
        preflight_sha256=sha256_file(root / PREEXECUTION_AUDIT_PATH),
    )
    started: list[int] = []
    completed: list[int] = []
    terminal_written = False
    try:
        claim, RegisteredCandidateFailure, run_registered_candidate, validate_registered_result = (
            load_postclaim_science(root, code_sha)
        )

        try:
            audit = run_registered_candidate()
            started = list(audit["arithmetic_modulus_order"])
            completed = list(audit["arithmetic_modulus_order"])
        except RegisteredCandidateFailure as error:
            started = error.moduli_started
            completed = error.moduli_completed
            raise
        if code_tree_sha256(root) != code_sha:
            raise RuntimeError("reviewed tree changed during candidate execution")
        result = {
            "schema": "EQUIVARIANT_CLOCK_OFFICIAL_RESULT_V1",
            "candidate_id": audit["candidate_id"],
            "source_lock_sha256": audit["source_lock_sha256"],
            "reviewed_code_sha256": code_sha,
            "registered_claim_sha256": claim["claim_sha256"],
            "pre_execution_gates": preflight["gates"],
            "independent_review_gate": preflight["independent_review"],
            "audit": audit,
            "registered_audit_count": 1,
            "candidate_numerical_run_count": 0,
            "pass": True,
        }
        semantic = validate_registered_result(result, root)
        if semantic["pass"] is not True:
            raise RuntimeError("registered result failed exact semantic validation")
        result_path = root / RESULT_PATH
        write_json(result_path, result, exclusive=True)
        terminal_path = write_terminal(
            root,
            reviewed_code_sha256=code_sha,
            state="COMPLETED_CERTIFIED",
            moduli_started=started,
            moduli_completed=completed,
            failure_code=None,
        )
        terminal_written = True
        return result_path, terminal_path
    except BaseException as error:
        if not terminal_written:
            failure_code = (
                "THEOREM_OR_CONTROL_CONTRADICTION"
                if type(error).__name__ == "RegisteredCandidateFailure"
                else ("INTERRUPTED" if isinstance(error, KeyboardInterrupt) else "IMPLEMENTATION_OR_GATE_EXCEPTION")
            )
            write_terminal(
                root,
                reviewed_code_sha256=code_sha,
                state="FAILED_CLOSED",
                moduli_started=started,
                moduli_completed=completed,
                failure_code=failure_code,
            )
        raise


def main(argv: list[str] | None = None) -> int:
    root = project_root()
    args = build_parser().parse_args(argv)
    if args.command == "code-hash":
        payload = {"reviewed_code_sha256": code_tree_sha256(root)}
    elif args.command == "safe-preflight":
        output = write_safe_preflight(root)
        payload = {"output": str(output), "audit": collect_safe_preflight(root)}
    elif args.command == "registered":
        result, terminal = run_registered(root)
        payload = {"result": str(result), "terminal": str(terminal)}
    elif args.command == "postrun-audit":
        from .manifest import collect_postrun_audit

        payload = collect_postrun_audit(root)
    else:
        from .manifest import write_result_manifest

        output = write_result_manifest(root)
        payload = {"manifest": str(output)}
    json.dump(payload, sys.stdout, indent=2, sort_keys=True)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
