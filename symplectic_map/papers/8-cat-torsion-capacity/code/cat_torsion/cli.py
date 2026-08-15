"""Fixed command lifecycle with a hard independent-review boundary."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .lifecycle import claim_registered_run, validate_registered_claim, write_terminal_ledger
from .manifest import (
    collect_safe_preflight,
    validate_registered_result,
    write_post_run_manifest,
    write_safe_preflight,
)
from .protocol import _raw_absolute, safe_directory_entries, write_json


def build_parser() -> argparse.ArgumentParser:
    project_root = _raw_absolute(Path(__file__)).parents[2]
    parser = argparse.ArgumentParser(description="Exact source-locked cat torsion audit")
    subparsers = parser.add_subparsers(dest="command", required=True)
    safe = subparsers.add_parser("safe-preflight", help="run P0--P3 only; never access candidate")
    safe.add_argument("--output-root", type=Path, default=project_root / "results")
    subparsers.add_parser("registered", help="run the fixed n=1..12 audit after DEPLOYMENT_PASS")
    subparsers.add_parser("post-manifest", help="validate the completed official package")
    return parser


def run_registered(project_root: Path) -> tuple[Path, Path]:
    project_root = _raw_absolute(project_root)
    results = project_root / "results"
    existing_names = {record["name"] for record in safe_directory_entries(results)}
    one_shot_names = {
        "registered_run.claim.json",
        "registered_run.json",
        "EXPERIMENT_RESULTS.json",
        "result_manifest.json",
    }
    if existing_names.intersection(one_shot_names):
        raise RuntimeError("registered lifecycle is already claimed or has an orphan artifact")
    preflight = collect_safe_preflight(project_root)
    if preflight.get("pass") is not True:
        raise RuntimeError("safe preflight failed; registered candidate remains locked")
    if preflight.get("status") != "AUTHORIZED_FOR_REGISTERED_EXECUTION":
        raise RuntimeError("independent DEPLOYMENT_PASS is missing or stale")
    write_json(results / "PRE_EXECUTION_AUDIT.json", preflight)
    code_digest = preflight["reviewed_code_sha256"]
    claim_registered_run(project_root, code_digest)
    claim = validate_registered_claim(project_root, code_digest, require_clean_started=True)
    if claim["pass"] is not True:
        raise RuntimeError("durable STARTED claim failed immediate validation")
    terminal_written = False
    periods_started: list[int] = []
    periods_completed: list[int] = []
    try:
        from .candidate import RegisteredCandidateFailure, run_registered_candidate

        try:
            result = run_registered_candidate(project_root)
        except RegisteredCandidateFailure as error:
            periods_started = error.periods_started
            periods_completed = error.periods_completed
            raise
        result["pre_execution_gates"] = preflight["gates"]
        result["independent_review_gate"] = preflight["independent_review"]
        result["registered_claim_sha256"] = claim["claim_sha256"]
        semantic = validate_registered_result(result, project_root)
        if semantic["pass"] is not True:
            raise RuntimeError("registered result failed pre-commit semantic validation")
        result_path = results / "EXPERIMENT_RESULTS.json"
        write_json(result_path, result, exclusive=True)
        terminal = write_terminal_ledger(
            project_root,
            reviewed_code_sha256=code_digest,
            state="COMPLETED_CERTIFIED",
            periods_started=list(range(1, 13)),
            periods_completed=list(range(1, 13)),
            artifact_path="results/EXPERIMENT_RESULTS.json",
            classification="INTRINSIC_TORSION_CAPACITY_CERTIFIED_A0_FAIL_PROVES_TOO_MUCH",
            failure_code=None,
        )
        terminal_written = True
        return result_path, terminal
    except BaseException as error:
        if not terminal_written:
            failure_code = (
                "INTERRUPTED"
                if isinstance(error, KeyboardInterrupt)
                else "THEOREM_CONTRADICTION"
                if type(error).__name__ == "RegisteredCandidateFailure"
                else "GATE_OR_TREE_CHANGED"
                if not periods_started
                else "IMPLEMENTATION_EXCEPTION"
            )
            classification = (
                "REJECTED_THEOREM_CONTRACT"
                if failure_code == "THEOREM_CONTRADICTION"
                else "NARROW_OR_REPAIR"
            )
            write_terminal_ledger(
                project_root,
                reviewed_code_sha256=code_digest,
                state="FAILED_CLOSED",
                periods_started=periods_started,
                periods_completed=periods_completed,
                artifact_path=None,
                classification=classification,
                failure_code=failure_code,
            )
        raise


def main(argv: list[str] | None = None) -> int:
    project_root = _raw_absolute(Path(__file__)).parents[2]
    args = build_parser().parse_args(argv)
    if args.command == "safe-preflight":
        output = write_safe_preflight(project_root, args.output_root)
        payload = {
            "stage": "P0_P3_SAFE_ONLY",
            "output": str(output),
            "registered_exact_audit": False,
        }
    elif args.command == "registered":
        result, terminal = run_registered(project_root)
        payload = {"result": str(result), "terminal": str(terminal)}
    else:
        output = write_post_run_manifest(project_root)
        payload = {"manifest": str(output)}
    json.dump(payload, sys.stdout, indent=2, sort_keys=True)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
