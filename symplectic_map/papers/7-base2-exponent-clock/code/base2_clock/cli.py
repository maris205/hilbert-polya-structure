"""Command-line lifecycle with a hard P3 boundary before candidate execution."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .candidate import run_registered_candidate
from .lifecycle import (
    claim_registered_run,
    validate_registered_claim,
    write_terminal_ledger,
)
from .manifest import collect_safe_preflight, write_post_run_manifest, write_safe_preflight
from .protocol import _raw_absolute, safe_directory_entries, write_json


def build_parser() -> argparse.ArgumentParser:
    project_root = _raw_absolute(Path(__file__)).parents[2]
    parser = argparse.ArgumentParser(description="Exact source-locked base-2 clock audit")
    subparsers = parser.add_subparsers(dest="command", required=True)
    safe = subparsers.add_parser("safe-preflight", help="run P0--P2 only; never access P4")
    safe.add_argument("--output-root", type=Path, default=project_root / "results")
    subparsers.add_parser("registered", help="run fixed P4 periods 2--7 after DEPLOYMENT_PASS")
    subparsers.add_parser("post-manifest", help="validate and hash the completed official package")
    return parser


def run_registered(project_root: Path) -> tuple[Path, Path]:
    """Create exactly one official result and registry after all live gates pass."""

    project_root = _raw_absolute(project_root)
    results = project_root / "results"
    result_path = results / "EXPERIMENT_RESULTS.json"
    existing_names = {item["name"] for item in safe_directory_entries(results)}
    one_shot_names = {
        "registered_run.claim.json",
        "registered_run.json",
        "EXPERIMENT_RESULTS.json",
        "TARGET_HIT_HALT.json",
        "result_manifest.json",
    }
    if existing_names.intersection(one_shot_names):
        raise RuntimeError("registered lifecycle already claimed or has an orphan artifact")
    preflight = collect_safe_preflight(project_root)
    if preflight.get("pass") is not True:
        raise RuntimeError("P0--P2 safe preflight failed; registered candidate remains locked")
    if preflight.get("status") != "AUTHORIZED_FOR_REGISTERED_EXECUTION":
        raise RuntimeError("independent DEPLOYMENT_PASS is missing or stale")
    write_json(results / "PRE_EXECUTION_AUDIT.json", preflight)
    code_digest = preflight["reviewed_code_sha256"]
    claim_registered_run(project_root, code_digest)
    claim = validate_registered_claim(project_root, code_digest, require_clean_started=True)
    if claim["pass"] is not True:
        raise RuntimeError("durable registered claim failed immediate validation")
    terminal_written = False
    try:
        result = run_registered_candidate(project_root)
        result["pre_execution_gates"] = preflight["gates"]
        result["independent_review_gate"] = preflight["independent_review"]
        result["registered_claim_sha256"] = claim["claim_sha256"]
        periods = result["periods_executed"]
        if result.get("pass") is not True:
            halt_path = results / "TARGET_HIT_HALT.json"
            write_json(halt_path, result, exclusive=True)
            terminal_path = write_terminal_ledger(
                project_root,
                reviewed_code_sha256=code_digest,
                state="HALTED_TARGET_HIT",
                periods_started=periods,
                periods_completed=periods,
                stopped_period=periods[-1],
                artifact_path="results/TARGET_HIT_HALT.json",
                failure_code="TARGET_HIT",
            )
            terminal_written = True
            raise RuntimeError("registered scan halted; inspect the immutable target-hit ledger")
        write_json(result_path, result, exclusive=True)
        terminal_path = write_terminal_ledger(
            project_root,
            reviewed_code_sha256=code_digest,
            state="COMPLETED_NO_HIT",
            periods_started=periods,
            periods_completed=periods,
            stopped_period=None,
            artifact_path="results/EXPERIMENT_RESULTS.json",
            failure_code=None,
        )
        terminal_written = True
        return result_path, terminal_path
    except BaseException as error:
        if not terminal_written:
            failure_code = "INTERRUPTED" if isinstance(error, KeyboardInterrupt) else "IMPLEMENTATION_EXCEPTION"
            write_terminal_ledger(
                project_root,
                reviewed_code_sha256=code_digest,
                state="FAILED_CLOSED",
                periods_started=[],
                periods_completed=[],
                stopped_period=None,
                artifact_path=None,
                failure_code=failure_code,
            )
        raise


def main(argv: list[str] | None = None) -> int:
    project_root = _raw_absolute(Path(__file__)).parents[2]
    args = build_parser().parse_args(argv)
    if args.command == "safe-preflight":
        output = write_safe_preflight(project_root, args.output_root)
        payload = {"stage": "P0_P2_ONLY", "output": str(output), "registered_candidate_run": False}
    elif args.command == "registered":
        result, registry = run_registered(project_root)
        payload = {"result": str(result), "registry": str(registry)}
    else:
        output = write_post_run_manifest(project_root)
        payload = {"manifest": str(output)}
    json.dump(payload, sys.stdout, indent=2, sort_keys=True)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
