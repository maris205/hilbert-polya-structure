#!/usr/bin/env python3
"""Cold disposable State-A upgrade, State-B transition, rollback, and attack suite."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


AUDITOR = "evidence/publication_gate/publication_auditor.py"
TRANSACTION = "evidence/publication_gate/publication_transaction.py"
BRIDGE = "evidence/publication_gate/stateb_bridge.py"
BUILDER = "evidence/publication_gate/build_overlay_seal.py"
SEAL = "evidence/publication_gate/PUBLICATION_OVERLAY_SEAL.json"
ROUTE = "outputs/evaluations/route_a/SD-C46/2026-08-18.yaml"
PAPER_MANIFEST = "outputs/PAPER_MANIFEST.sha256"
HEX64 = re.compile(r"[0-9a-f]{64}\Z")
HEX40 = re.compile(r"[0-9a-f]{40}\Z")
CHECKLIST_OVERRIDE = False

EXPECTED_CASES = [
    ("source_exact", 0, "PASS", "SOURCE_OVERLAY_EXACT"),
    ("predecessor_exact", 0, "PASS", "PREDECESSOR_STATE_A_EXACT"),
    ("overlay_forced_late", 86, "FORCED_FAILURE", "FORCED_LATE_FAILURE"),
    ("overlay_rollback", 87, "ROLLED_BACK", "INJECTED_INSTALL_FAILURE_ROLLED_BACK"),
    ("overlay_first", 0, "PASS", "UPGRADED_TO_SUPERSEDING_OVERLAY"),
    ("overlay_second", 0, "PASS", "ALREADY_INSTALLED_EXACT"),
    ("stateb_forced_late", 86, "FORCED_FAILURE", "FORCED_LATE_FAILURE"),
    ("stateb_rollback", 87, "ROLLED_BACK", "INJECTED_POST_EXCHANGE_FAILURE_ROLLED_BACK"),
    ("stateb_first", 0, "PASS", "TRANSITIONED_TO_STATE_B_EXACT"),
    ("stateb_second", 0, "PASS", "ALREADY_STATE_B_EXACT"),
    ("stateb_publication_exact", 0, "PASS", "PUBLISHED_STATE_B_EXACT"),
    ("attack_missing_h1", 2, "REJECT", "EXPECTED_STAGE1_COMMIT_MISSING"),
    ("attack_wrong_h1", 2, "REJECT", "ROUTE_STAGE1_COMMIT_MISMATCH"),
    ("attack_uppercase_h1", 2, "REJECT", "EXPECTED_STAGE1_COMMIT_INVALID"),
    ("attack_route_commit_full_reclose", 2, "REJECT", "ROUTE_STAGE1_COMMIT_MISMATCH"),
    ("attack_paper_manifest_reclose", 2, "REJECT", "FINAL_RUNTIME_REJECT"),
    ("attack_writer_manifest_seal_reclose", 2, "REJECT", "PUBLICATION_SEAL_SHA256_MISMATCH"),
    ("attack_auditor_manifest_seal_reclose", 2, "REJECT", "PUBLICATION_SEAL_SHA256_MISMATCH"),
    ("attack_state_a_b_mixed", 2, "REJECT", "STATE_A_PROVENANCE_DRIFT"),
    ("governance_missing_seal", 2, "REJECT", "EXPECTED_PUBLICATION_SEAL_SHA256_MISSING"),
    ("governance_wrong_seal", 2, "REJECT", "PUBLICATION_SEAL_SHA256_MISMATCH"),
    ("governance_uppercase_seal", 2, "REJECT", "EXPECTED_PUBLICATION_SEAL_SHA256_INVALID"),
]


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       separators=(",", ": "), allow_nan=False) + "\n").encode("ascii")


def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def sha_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def invoke(command: list[str], cwd: Path) -> tuple[int, dict[str, Any] | None, bytes, bytes]:
    environment = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "PYTHONPATH": "",
                   "PYTHONDONTWRITEBYTECODE": "1", "TZ": "UTC", "LC_ALL": "C", "LANG": "C"}
    process = subprocess.run(command, cwd=cwd, env=environment, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, check=False)
    value: dict[str, Any] | None = None
    try:
        parsed = json.loads(process.stdout.decode("ascii"), object_pairs_hook=unique)
        if type(parsed) is dict and process.stdout == canonical(parsed):
            value = parsed
    except Exception:
        pass
    return process.returncode, value, process.stdout, process.stderr


def require(label: str, result: tuple[int, dict[str, Any] | None, bytes, bytes],
            expected_rc: int, expected_status: str, expected_code: str) -> dict[str, Any]:
    rc, value, _stdout, stderr = result
    observed = value.get("payload", {}).get("code") if value else "INVALID_ENVELOPE"
    status = value.get("status") if value else None
    if rc != expected_rc or stderr or value is None \
            or status != expected_status or observed != expected_code:
        raise RuntimeError(
            f"{label}: expected {expected_rc}/{expected_status}/{expected_code}, "
            f"observed {rc}/{status}/{observed}, stderr={stderr[-200:]!r}")
    return value


def copied(source: Path, destination: Path) -> Path:
    shutil.copytree(source, destination, copy_function=shutil.copy2)
    destination.chmod(0o755)
    return destination


def audit_command(auditor: Path, root: Path, source: Path, anchor: str | None,
                  commit: str | None, source_only: bool = False) -> list[str]:
    command = [sys.executable, "-I", "-B", str(auditor), "--root", str(root),
               "--overlay-source", str(source), "--relocated-disposable"]
    if anchor is not None:
        command += ["--expected-publication-seal-sha256", anchor]
    if commit is not None:
        command += ["--expected-stage1-commit", commit]
    if source_only:
        command.append("--source-only")
    if CHECKLIST_OVERRIDE:
        command.append("--allow-unexecuted-checklist")
    return command


def transaction_command(script: Path, source: Path, target: Path, anchor: str,
                        commit: str, extra: list[str] | None = None) -> list[str]:
    command = [sys.executable, "-I", "-B", str(script), "--source", str(source),
               "--target", str(target), "--expected-publication-seal-sha256", anchor,
               "--expected-stage1-commit", commit, "--relocated-disposable"]
    if CHECKLIST_OVERRIDE:
        command.append("--allow-unexecuted-checklist")
    return command + (extra or [])


def bridge_command(script: Path, source: Path, target: Path, anchor: str,
                   commit: str | None, extra: list[str] | None = None) -> list[str]:
    command = [sys.executable, "-I", "-B", str(script), "--source", str(source),
               "--target", str(target), "--expected-publication-seal-sha256", anchor,
               "--relocated-disposable"]
    if commit is not None:
        command += ["--expected-stage1-commit", commit]
    if CHECKLIST_OVERRIDE:
        command.append("--allow-unexecuted-checklist")
    return command + (extra or [])


def logical_tree(root: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in [root] + sorted(root.rglob("*"), key=lambda item: item.relative_to(root).as_posix()):
        metadata = os.lstat(path)
        relative = "." if path == root else path.relative_to(root).as_posix()
        if stat.S_ISDIR(metadata.st_mode):
            kind, digest = "directory", None
        elif stat.S_ISREG(metadata.st_mode):
            kind, digest = "regular", sha_file(path)
        elif stat.S_ISLNK(metadata.st_mode):
            kind, digest = "symlink", os.readlink(path)
        else:
            kind, digest = "nonregular", None
        rows.append({"kind": kind, "mode": stat.S_IMODE(metadata.st_mode),
                     "path": relative, "sha256": digest})
    return rows


def paper_manifest(root: Path, output: Path) -> bytes:
    rows: list[tuple[str, str, str, str]] = []
    for path in root.rglob("*"):
        relative = path.relative_to(root).as_posix()
        if relative == "outputs" or relative.startswith("outputs/") \
                or relative == "PREOUTPUT_STATIC_SEAL.json":
            continue
        metadata = os.lstat(path)
        mode = f"{stat.S_IMODE(metadata.st_mode):04o}"
        if stat.S_ISDIR(metadata.st_mode):
            rows.append((relative, "directory", mode, "-"))
        elif stat.S_ISREG(metadata.st_mode):
            rows.append((relative, "regular", mode, sha_file(path)))
        else:
            raise ValueError("nonregular manifest node")
    for path in output.rglob("*"):
        relative_output = path.relative_to(output).as_posix()
        if relative_output == "PAPER_MANIFEST.sha256":
            continue
        relative = "outputs/" + relative_output
        metadata = os.lstat(path)
        mode = f"{stat.S_IMODE(metadata.st_mode):04o}"
        if stat.S_ISDIR(metadata.st_mode):
            rows.append((relative, "directory", mode, "-"))
        elif stat.S_ISREG(metadata.st_mode):
            rows.append((relative, "regular", mode, sha_file(path)))
        else:
            raise ValueError("nonregular output manifest node")
    rows.sort()
    header = "paper44-state-b-manifest-v2 exclude=PREOUTPUT_STATIC_SEAL.json,PAPER_MANIFEST.sha256\n"
    return (header + "".join(f"{kind} {mode} {digest} {path}\n"
                              for path, kind, mode, digest in rows)).encode("ascii")


def evidence_object(observed: bool) -> dict[str, Any]:
    cases = [
        {"expected_code": code, "expected_exit": rc, "id": label,
         "expected_status": status}
        for label, rc, status, code in EXPECTED_CASES
    ]
    if observed:
        for case in cases:
            case["observed_outcome"] = "EXACT"
    return {
        "candidate_id": "SD-C46",
        "case_count": len(EXPECTED_CASES),
        "cases": cases,
        "execution_observations_recorded": observed,
        "external_values_recorded": False,
        "legacy_frozen_auditor_disposition":
            "EXPECTED_REJECT_STATIC_TREE_MISMATCH_SUPERSESSION",
        "replay_contract": {
            "publication_seal_sha256": "supply_out_of_band",
            "stage1_commit": "supply_out_of_band_lowercase40",
        },
        "schema": "paper44-stateb-publication-smoke-evidence-v2",
        "status": "HOLD_FOR_INDEPENDENT_STATEB_PUBLICATION_AUDIT",
    }


def main() -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--source")
    parser.add_argument("--authority-fixture")
    parser.add_argument("--expected-publication-seal-sha256")
    parser.add_argument("--expected-stage1-commit")
    parser.add_argument("--evidence-out")
    parser.add_argument("--write-evidence-template", action="store_true")
    parser.add_argument("--allow-unexecuted-checklist", action="store_true")
    arguments = parser.parse_args()

    if arguments.write_evidence_template:
        if arguments.evidence_out is None:
            raise SystemExit("--evidence-out required")
        output = Path(arguments.evidence_out)
        output.write_bytes(canonical(evidence_object(False)))
        output.chmod(0o644)
        return 0

    if None in {arguments.source, arguments.authority_fixture,
                arguments.expected_publication_seal_sha256, arguments.expected_stage1_commit}:
        raise SystemExit("source, fixture, seal, and Stage1 commit are required")
    anchor = arguments.expected_publication_seal_sha256
    commit = arguments.expected_stage1_commit
    if HEX64.fullmatch(anchor) is None or HEX40.fullmatch(commit) is None \
            or commit == "0" * 40:
        raise SystemExit("invalid external anchor")
    source = Path(arguments.source).resolve(strict=True)
    fixture = Path(arguments.authority_fixture).resolve(strict=True)
    if not str(source).startswith("/tmp/"):
        raise SystemExit("source must be disposable")
    global CHECKLIST_OVERRIDE
    CHECKLIST_OVERRIDE = arguments.allow_unexecuted_checklist
    temporary = Path(tempfile.mkdtemp(prefix="paper44-stateb-publication-smoke-"))
    try:
        authenticated_runtime = Path(__file__).resolve(strict=True).parent
        controller = temporary / "authenticated_controller"
        controller.mkdir(mode=0o755)
        controller_paths: dict[str, Path] = {}
        for relative in (AUDITOR, TRANSACTION, BRIDGE):
            destination = controller / Path(relative).name
            shutil.copy2(authenticated_runtime / Path(relative).name, destination)
            destination.chmod(0o444)
            controller_paths[relative] = destination
        controller.chmod(0o555)
        auditor = controller_paths[AUDITOR]
        transaction = controller_paths[TRANSACTION]
        bridge = controller_paths[BRIDGE]
        require("source_exact", invoke(audit_command(
            auditor, source, source, anchor, commit, True), source.parent),
            0, "PASS", "SOURCE_OVERLAY_EXACT")
        working = copied(fixture, temporary / "working")
        require("predecessor_exact", invoke(audit_command(
            auditor, working, source, anchor, commit), working.parent),
            0, "PASS", "PREDECESSOR_STATE_A_EXACT")

        before = logical_tree(working)
        late = require("overlay_forced_late", invoke(transaction_command(
            transaction, source, working, anchor, commit, ["--force-late-failure"]),
            working.parent), 86, "FORCED_FAILURE", "FORCED_LATE_FAILURE")
        if late["payload"].get("target_unchanged") is not True or logical_tree(working) != before:
            raise RuntimeError("overlay late failure changed target")
        rollback = require("overlay_rollback", invoke(transaction_command(
            transaction, source, working, anchor, commit,
            ["--inject-install-failure-after", "1"]), working.parent),
            87, "ROLLED_BACK", "INJECTED_INSTALL_FAILURE_ROLLED_BACK")
        if rollback["payload"].get("target_unchanged") is not True or logical_tree(working) != before:
            raise RuntimeError("overlay rollback changed target")
        first_overlay = require("overlay_first", invoke(transaction_command(
            transaction, source, working, anchor, commit), working.parent),
            0, "PASS", "UPGRADED_TO_SUPERSEDING_OVERLAY")
        if first_overlay["payload"].get("physical_target_replacements", 0) <= 0:
            raise RuntimeError("overlay first upgrade made no replacement")
        second_overlay = require("overlay_second", invoke(transaction_command(
            transaction, source, working, anchor, commit), working.parent),
            0, "PASS", "ALREADY_INSTALLED_EXACT")
        if second_overlay["payload"].get("physical_target_replacements") != 0:
            raise RuntimeError("overlay idempotence failed")

        state_a_template = copied(working, temporary / "state_a_template")
        before_outputs = logical_tree(working / "outputs")
        stateb_late = require("stateb_forced_late", invoke(bridge_command(
            bridge, source, working, anchor, commit, ["--force-late-failure"]),
            working.parent), 86, "FORCED_FAILURE", "FORCED_LATE_FAILURE")
        if stateb_late["payload"].get("target_outputs_unchanged") is not True \
                or logical_tree(working / "outputs") != before_outputs:
            raise RuntimeError("State B late failure changed outputs")
        stateb_rollback = require("stateb_rollback", invoke(bridge_command(
            bridge, source, working, anchor, commit,
            ["--inject-post-exchange-failure"]), working.parent),
            87, "ROLLED_BACK", "INJECTED_POST_EXCHANGE_FAILURE_ROLLED_BACK")
        if stateb_rollback["payload"].get("target_outputs_unchanged") is not True \
                or logical_tree(working / "outputs") != before_outputs:
            raise RuntimeError("State B rollback changed outputs")
        stateb_first = require("stateb_first", invoke(bridge_command(
            bridge, source, working, anchor, commit), working.parent),
            0, "PASS", "TRANSITIONED_TO_STATE_B_EXACT")
        if stateb_first["payload"].get("atomic_output_exchanges") != 1:
            raise RuntimeError("State B first transition was not one exchange")
        stateb_second = require("stateb_second", invoke(bridge_command(
            bridge, source, working, anchor, commit), working.parent),
            0, "PASS", "ALREADY_STATE_B_EXACT")
        if stateb_second["payload"].get("atomic_output_exchanges") != 0:
            raise RuntimeError("State B second transition was not idempotent")
        exact_b = require("stateb_publication_exact", invoke(audit_command(
            auditor, working, source, anchor, commit), working.parent),
            0, "PASS", "PUBLISHED_STATE_B_EXACT")
        if exact_b["payload"].get("stage1_commit_bound_three_times") is not True \
                or exact_b["payload"].get("legacy_frozen_auditor_disposition") \
                != "EXPECTED_REJECT_STATIC_TREE_MISMATCH_SUPERSESSION":
            raise RuntimeError("State B publication semantics")

        require("attack_missing_h1", invoke(audit_command(
            auditor, working, source, anchor, None), working.parent),
            2, "REJECT", "EXPECTED_STAGE1_COMMIT_MISSING")
        wrong_commit = "1" * 40 if commit != "1" * 40 else "2" * 40
        require("attack_wrong_h1", invoke(audit_command(
            auditor, working, source, anchor, wrong_commit), working.parent),
            2, "REJECT", "ROUTE_STAGE1_COMMIT_MISMATCH")
        require("attack_uppercase_h1", invoke(audit_command(
            auditor, working, source, anchor, "A" * 40), working.parent),
            2, "REJECT", "EXPECTED_STAGE1_COMMIT_INVALID")

        route_reclose = copied(state_a_template, temporary / "route_reclose")
        require("route_reclose_build", invoke(bridge_command(
            bridge, source, route_reclose, anchor, wrong_commit), route_reclose.parent),
            0, "PASS", "TRANSITIONED_TO_STATE_B_EXACT")
        require("attack_route_commit_full_reclose", invoke(audit_command(
            auditor, route_reclose, source, anchor, commit), route_reclose.parent),
            2, "REJECT", "ROUTE_STAGE1_COMMIT_MISMATCH")

        manifest_reclose = copied(working, temporary / "manifest_reclose")
        report = manifest_reclose / "outputs/reports/EXPERIMENT_REPORT.md"
        report.write_bytes(report.read_bytes() + b"\ncoordinated false publication line\n")
        report.chmod(0o644)
        (manifest_reclose / PAPER_MANIFEST).write_bytes(
            paper_manifest(manifest_reclose, manifest_reclose / "outputs"))
        (manifest_reclose / PAPER_MANIFEST).chmod(0o644)
        require("attack_paper_manifest_reclose", invoke(audit_command(
            auditor, manifest_reclose, source, anchor, commit), manifest_reclose.parent),
            2, "REJECT", "FINAL_RUNTIME_REJECT")

        writer_reclose = copied(source, temporary / "writer_reclose")
        protocol = writer_reclose / "evidence/publication_gate/PUBLICATION_PROTOCOL.md"
        protocol.write_bytes(protocol.read_bytes() + b"\nmalicious writer rewrite\n")
        protocol.chmod(0o644)
        built = invoke([sys.executable, "-I", "-B", str(writer_reclose / BUILDER),
                        "--root", str(writer_reclose)], writer_reclose.parent)
        if built[0] != 0 or built[3] or built[1] is None or built[1].get("status") != "SEALED":
            raise RuntimeError("writer reclose builder")
        require("attack_writer_manifest_seal_reclose", invoke(audit_command(
            auditor, writer_reclose, writer_reclose, anchor, commit, True), writer_reclose.parent),
            2, "REJECT", "PUBLICATION_SEAL_SHA256_MISMATCH")

        auditor_reclose = copied(source, temporary / "auditor_reclose")
        rewritten = auditor_reclose / AUDITOR
        rewritten.write_bytes(rewritten.read_bytes() + b"\n# malicious auditor rewrite\n")
        rewritten.chmod(0o644)
        built = invoke([sys.executable, "-I", "-B", str(auditor_reclose / BUILDER),
                        "--root", str(auditor_reclose)], auditor_reclose.parent)
        if built[0] != 0 or built[3] or built[1] is None or built[1].get("status") != "SEALED":
            raise RuntimeError("auditor reclose builder")
        require("attack_auditor_manifest_seal_reclose", invoke(audit_command(
            auditor, auditor_reclose, auditor_reclose, anchor, commit, True), auditor_reclose.parent),
            2, "REJECT", "PUBLICATION_SEAL_SHA256_MISMATCH")

        mixed = copied(working, temporary / "mixed")
        route_path = mixed / ROUTE
        route = json.loads(route_path.read_text(encoding="ascii"), object_pairs_hook=unique)
        route["authority_integration"]["state"] = "A"
        route_path.write_bytes(canonical(route))
        route_path.chmod(0o644)
        require("attack_state_a_b_mixed", invoke(audit_command(
            auditor, mixed, source, anchor, commit), mixed.parent),
            2, "REJECT", "STATE_A_PROVENANCE_DRIFT")

        require("governance_missing_seal", invoke(audit_command(
            auditor, source, source, None, commit, True), source.parent),
            2, "REJECT", "EXPECTED_PUBLICATION_SEAL_SHA256_MISSING")
        require("governance_wrong_seal", invoke(audit_command(
            auditor, source, source, "0" * 64, commit, True), source.parent),
            2, "REJECT", "PUBLICATION_SEAL_SHA256_MISMATCH")
        require("governance_uppercase_seal", invoke(audit_command(
            auditor, source, source, "A" * 64, commit, True), source.parent),
            2, "REJECT", "EXPECTED_PUBLICATION_SEAL_SHA256_INVALID")

        evidence_raw = canonical(evidence_object(True))
        if arguments.evidence_out:
            evidence_path = Path(arguments.evidence_out)
            evidence_path.write_bytes(evidence_raw)
            evidence_path.chmod(0o644)
        sys.stdout.buffer.write(canonical({
            "payload": {
                "case_count": len(EXPECTED_CASES),
                "evidence_sha256": hashlib.sha256(evidence_raw).hexdigest(),
                "external_values_recorded": False,
                "state": "PUBLISHED_STATE_B_EXACT",
            },
            "schema": "paper44-stateb-publication-smoke-result-v2",
            "status": "PASS",
        }))
        return 0
    finally:
        shutil.rmtree(temporary, ignore_errors=True)


if __name__ == "__main__":
    raise SystemExit(main())
