#!/usr/bin/env python3
"""Render a fresh canonical Route-A v0.2 evaluation for frozen SD-C46.

This is not a downgrade of the historical v0.3 card.  It reconstructs the
v0.2 object from the frozen preauthority source/proof descriptions and checks
that every later execution artifact needed to turn the expectation into an
actual evaluation is present, exact, and successful.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import stat
import subprocess
import sys
from pathlib import Path, PurePosixPath
from typing import Any

import yaml


SOURCE_COMMIT = "b0e41ac3d6bd30618421d1b76122c3e9e04d070b"
GIT = "/usr/bin/git"
SKILL_SHA256 = "29bd6275aa0c80ecce9cca898f06687208475c0a9a40cf3b9592fde45951458a"
EXPECTATION_SHA256 = "0326a3c5d7bb10a953c9987d71d2c627798f138b5e671e74a114e5819c328892"
HISTORICAL_ROUTE_SHA256 = "e871be0a1fe6ca47566b82435eddf9e3b856c29a1940bd467cad19cf0b28e32f"
EXPECTED_TUPLE = [
    "A0_FAIL", "A1_FAIL", "A2_FAIL",
    "A3_PARTIAL_ANALYTIC_STRUCTURE", "A4_FAIL",
]
ARTIFACT_SHA256 = {
    "preauthority/SOURCE_LOCK.md": "a49bbc392e21a25e7f36ab8c0c5426bbec510aa30bc6d2d6943b0e81c5347984",
    "preauthority/SELECTION_AND_PROVENANCE.md": "c11bb2d159191c1b7fc8f0a59f0f6b17569d6e49770442ee56b724f3ef4c334a",
    "preauthority/EXACT_WITNESS_LEDGER.md": "b171d3742dd56eab910fa399fbfc6e1ed0d0f19a4321c5ab6c044e58fb9445e8",
    "preauthority/OBJECT_MARKER_OPERATOR_CONTRACT.md": "059ecbc4edcd097cb9eb83a0452591735fc25ca6d6d8da5a3ce10f4cff15330f",
    "preauthority/PROOF_PACKAGE.md": "9367109c025c885c11f2e49b9bdef0353b867efd618eb4698f171be8161757e0",
    "preauthority/THEOREM_FALSIFIERS.md": "dbac28929c905d3bc2b9f2b7311bc1addf79925633dfa4b1e00f3a7deb1fc734",
    "preauthority/DERIVATION_PACKAGE.md": "06271bf0d6ff04eda8ad06cb2b9f394616cfb72154ebdcc646cef1b002c7eb51",
    "preauthority/LITERATURE_NOVELTY_AUDIT.md": "1de200d9757fab8107bc5d11791c7a903034e97307d27f060a1b6b07b04130f0",
    "outputs/audits/source_audit.json": "9fffd522fe108d3c6cf9580a835757192020abbe967ef61354d1a1a8314ea0a3",
    "outputs/audits/proof_audit.json": "afd17de5efd811a90645efaf5aadf96cec0881a6b73d25966c1b081204708cde",
    "outputs/audits/type_audit.json": "966dee537ef56ae904ea09f9c8383d2f4092bc043224fff2b0fba436cf200e08",
    "outputs/audits/independence_audit.json": "d9eb6ab3e767654e84d723bbe09ad21ddceccd8079ff2c042ab8584e53822a51",
    "outputs/results/exact_comparison.json": "c988d083cbdd05a84f698497bfb6b8c13f9540fe3801497da9c7ce05d09f8e10",
    "outputs/tests/mutation_results.json": "21f9238294305d6adcff2c0afa66576c878f8a3d5b964b540a2372872261f9d6",
}
CODE_PATHS = [
    "symbolic_dynamics/papers/44-q-adic-finite-size-boundary-spectra/code/route/render_route_v0_2.py",
    "symbolic_dynamics/papers/44-q-adic-finite-size-boundary-spectra/code/route/validate_route_v0_2.py",
    "symbolic_dynamics/papers/44-q-adic-finite-size-boundary-spectra/code/route/audit_route_v0_2_independent.py",
    "symbolic_dynamics/papers/44-q-adic-finite-size-boundary-spectra/code/tests/run_route_v0_2_mutations.py",
]
DERIVED_PATHS = [
    "symbolic_dynamics/papers/44-q-adic-finite-size-boundary-spectra/evaluations/route_a/SD-C46/2026-08-19.yaml",
    "symbolic_dynamics/papers/44-q-adic-finite-size-boundary-spectra/evidence/route_v0_2/PRIMARY_AUDIT.json",
    "symbolic_dynamics/papers/44-q-adic-finite-size-boundary-spectra/evidence/route_v0_2/INDEPENDENT_AUDIT.json",
    "symbolic_dynamics/papers/44-q-adic-finite-size-boundary-spectra/evidence/route_v0_2/MUTATION_RESULTS.json",
]


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       separators=(",", ": "), allow_nan=False) + "\n").encode("ascii")


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def secure_regular(root: Path, relative: str) -> Path:
    pure = PurePosixPath(relative)
    if pure.is_absolute() or "\\" in relative \
            or any(part in {"", ".", ".."} for part in pure.parts):
        raise ValueError("unsafe relative path")
    path = root.joinpath(*pure.parts)
    cursor = path
    while cursor != root:
        if cursor.is_symlink():
            raise ValueError("symlink forbidden")
        cursor = cursor.parent
    resolved = path.resolve(strict=True)
    metadata = os.lstat(resolved)
    expected_mode = 0o444 if pure.parts[0] == "preauthority" else 0o644
    if root.resolve(strict=True) not in resolved.parents \
            or not stat.S_ISREG(metadata.st_mode) \
            or stat.S_IMODE(metadata.st_mode) != expected_mode:
        raise ValueError("artifact physical contract")
    return resolved


def unique_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def load_json(root: Path, relative: str) -> tuple[dict[str, Any], bytes]:
    path = secure_regular(root, relative)
    raw = path.read_bytes()
    value = json.loads(raw.decode("ascii"), object_pairs_hook=unique_pairs)
    if type(value) is not dict or raw != canonical(value):
        raise ValueError("noncanonical JSON evidence")
    return value, raw


def validate_inputs(root: Path, skill: Path, source_commit: str) -> tuple[dict[str, Any], dict[str, Any]]:
    if not root.is_absolute() or root.is_symlink() or not root.is_dir() \
            or root.resolve(strict=True) != root \
            or stat.S_IMODE(os.lstat(root).st_mode) != 0o755:
        raise ValueError("unsafe paper root")
    if source_commit != SOURCE_COMMIT:
        raise ValueError("frozen source commit mismatch")
    if not skill.is_absolute() or skill.is_symlink() or not skill.is_file() \
            or sha(skill.read_bytes()) != SKILL_SHA256:
        raise ValueError("canonical v0.2 skill mismatch")
    skill_text = skill.read_text(encoding="utf-8")
    if "**Version:** `0.2.0`" not in skill_text or "# 8. Output schema" not in skill_text \
            or "route_b_invocation_allowed: false" not in skill_text:
        raise ValueError("skill semantic anchors missing")

    expectation_path = secure_regular(root, "preauthority/ROUTE_EXPECTATION.yaml")
    expectation_raw = expectation_path.read_bytes()
    if sha(expectation_raw) != EXPECTATION_SHA256:
        raise ValueError("frozen expectation mismatch")
    expectation = yaml.safe_load(expectation_raw.decode("utf-8"))
    if type(expectation) is not dict \
            or expectation.get("skill_version") != "0.2.0" \
            or expectation.get("candidate_id") != "SD-C46" \
            or expectation.get("route_tuple") != EXPECTED_TUPLE \
            or expectation.get("overall_verdict") != "ROUTE_A_REJECTED" \
            or expectation.get("route_b_invocation_allowed") is not False:
        raise ValueError("expectation semantic anchors")

    historical, historical_raw = load_json(
        root, "outputs/evaluations/route_a/SD-C46/2026-08-18.yaml")
    if sha(historical_raw) != HISTORICAL_ROUTE_SHA256 \
            or historical.get("skill_version") != "0.3.0" \
            or historical.get("route_tuple") != EXPECTED_TUPLE \
            or historical.get("overall_verdict") != "ROUTE_A_REJECTED" \
            or historical.get("route_b", {}).get("invocation_allowed") is not False \
            or historical.get("source_commit") != SOURCE_COMMIT:
        raise ValueError("historical actual result mismatch")

    for relative, digest in ARTIFACT_SHA256.items():
        if sha(secure_regular(root, relative).read_bytes()) != digest:
            raise ValueError("frozen evidence mismatch: " + relative)
    expected_status = {
        "outputs/audits/source_audit.json": ("paper44-source-audit-v1", "PASS"),
        "outputs/audits/proof_audit.json": ("paper44-proof-audit-v1", "PASS"),
        "outputs/audits/type_audit.json": ("paper44-type-audit-v1", "PASS"),
        "outputs/audits/independence_audit.json": ("paper44-independence-audit-v1", "PASS"),
        "outputs/results/exact_comparison.json": ("paper44-exact-comparison-v1", "PASS"),
        "outputs/tests/mutation_results.json": ("paper44-mutation-results-v1", "PASS"),
    }
    values: dict[str, dict[str, Any]] = {}
    for relative, (schema, status) in expected_status.items():
        value, _ = load_json(root, relative)
        if value.get("schema") != schema or value.get("status") != status:
            raise ValueError("evidence status mismatch: " + relative)
        values[relative] = value
    mutation = values["outputs/tests/mutation_results.json"]
    payload = mutation.get("payload", {})
    if payload.get("family_count") != 19 or payload.get("instance_count") != 20 \
            or payload.get("consumer_invocation_count") != 52 \
            or payload.get("survivor_count") != 0:
        raise ValueError("mutation closure mismatch")
    comparison = values["outputs/results/exact_comparison.json"]
    if comparison.get("payload", {}).get("strict_recursive_type_and_value_equal") is not True:
        raise ValueError("dual evaluator comparison mismatch")
    return expectation, historical


def prefixed(items: list[str], extras: list[str]) -> list[str]:
    result = ["preauthority/" + item for item in items]
    result.extend(extras)
    if len(result) != len(set(result)):
        raise ValueError("duplicate artifact path")
    return result


def validate_code_commit(root: Path, repo: Path, code_commit: str) -> None:
    if type(code_commit) is not str or re.fullmatch(r"[0-9a-f]{40}", code_commit) is None \
            or code_commit == "0" * 40:
        raise ValueError("invalid code commit")
    if not repo.is_absolute() or repo.is_symlink() or not repo.is_dir() \
            or repo.resolve(strict=True) != repo or not (repo / ".git").exists():
        raise ValueError("unsafe code repository")
    ancestry = subprocess.run(
        [GIT, "--no-replace-objects", "-C", str(repo), "merge-base", "--is-ancestor",
         SOURCE_COMMIT, code_commit],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
        env={"PATH": os.environ.get("PATH", "/usr/bin:/bin"),
             "LC_ALL": "C", "LANG": "C"},
    )
    if ancestry.returncode != 0 or ancestry.stdout or ancestry.stderr:
        raise ValueError("code commit is not descended from frozen science H1")
    for repository_path in CODE_PATHS:
        relative = repository_path.split("papers/44-q-adic-finite-size-boundary-spectra/", 1)[1]
        current = secure_regular(root, relative).read_bytes()
        process = subprocess.run(
            [GIT, "--no-replace-objects", "-C", str(repo),
             "show", code_commit + ":" + repository_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
            env={"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "LC_ALL": "C", "LANG": "C"},
        )
        if process.returncode != 0 or process.stderr or process.stdout != current:
            raise ValueError("code commit does not bind current evaluator code: " + relative)
    for repository_path in DERIVED_PATHS:
        process = subprocess.run(
            [GIT, "--no-replace-objects", "-C", str(repo),
             "cat-file", "-e", code_commit + ":" + repository_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
            env={"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "LC_ALL": "C", "LANG": "C"},
        )
        if process.returncode == 0:
            raise ValueError("H1 prime must not contain derived H2 prime object")


def render(expectation: dict[str, Any], historical: dict[str, Any],
           source_commit: str) -> dict[str, Any]:
    source = expectation["source_lock"]
    a0 = expectation["a0"]
    a1 = expectation["a1"]
    a2 = expectation["a2"]
    a3 = expectation["a3"]
    a4 = expectation["a4"]
    stale = "evaluator_independence_remains_unexecuted"
    blockers = [item for item in expectation["blocking_conditions"] if item != stale]
    if len(blockers) != 5 or stale not in expectation["blocking_conditions"]:
        raise ValueError("nonmechanical blocker transition")
    return {
        "skill": "route-a-evaluator",
        "skill_version": "0.2.0",
        "candidate_id": "SD-C46",
        "source_commit": source_commit,
        "evaluation_date": "2026-08-19",
        "artifact_path_base": "papers/44-q-adic-finite-size-boundary-spectra",
        "source_lock": {
            "object": source["object"],
            "arithmetic_origin": source["arithmetic_origin"],
            "clock": source["clock"],
            "normalization": source["normalization"],
            "determinant_convention": source["determinant_convention"],
            "cutoff": source["cutoff"],
            "precision": source["precision"],
            "allowed_data": source["allowed_data"],
            "forbidden_data": source["forbidden_data"],
        },
        "a0": {
            "verdict": a0["verdict"],
            "evidence_status": a0["evidence_status"],
            "strongest_evidence": a0["strongest_evidence"],
            "strongest_failure": a0["strongest_failure"],
            "arithmetic_controls": a0["arithmetic_controls"],
            "artifacts": prefixed(a0["artifacts"], [
                "outputs/audits/source_audit.json",
                "outputs/tests/mutation_results.json",
            ]),
        },
        "a1": {
            "verdict": a1["verdict"],
            "evidence_status": a1["evidence_status"],
            "strongest_evidence": a1["strongest_evidence"],
            "strongest_failure": a1["strongest_failure"],
            "metrics": a1["metrics"],
            "artifacts": prefixed(a1["artifacts"], [
                "outputs/audits/proof_audit.json",
                "outputs/audits/independence_audit.json",
            ]),
        },
        "a2": {
            "verdict": a2["verdict"],
            "evidence_status": a2["evidence_status"],
            "strongest_evidence": a2["strongest_evidence"],
            "strongest_failure": a2["strongest_failure"],
            "metrics": a2["metrics"],
            "artifacts": prefixed(a2["artifacts"], [
                "outputs/audits/type_audit.json",
                "outputs/results/exact_comparison.json",
            ]),
        },
        "a3": {
            "verdict": a3["verdict"],
            "evidence_status": a3["evidence_status"],
            "strongest_evidence": a3["strongest_evidence"],
            "strongest_failure": a3["strongest_failure"],
            "analytic_structure": a3["analytic_structure"],
            "weil_compression": a3["weil_compression"],
            "artifacts": prefixed(a3["artifacts"], [
                "outputs/audits/proof_audit.json",
                "outputs/results/exact_comparison.json",
            ]),
        },
        "a4": {
            "verdict": a4["verdict"],
            "evidence_status": a4["evidence_status"],
            "strongest_evidence": a4["strongest_evidence"],
            "strongest_failure": a4["strongest_failure"],
            "metrics": a4["metrics"],
            "artifacts": prefixed(a4["artifacts"], [
                "outputs/audits/type_audit.json",
                "outputs/audits/independence_audit.json",
            ]),
        },
        "adversarial_controls": {
            "controls_used": expectation["adversarial_controls"]["controls_used"],
            "proves_too_much_risk": expectation["adversarial_controls"]["proves_too_much_risk"],
            "verdict": expectation["adversarial_controls"]["verdict"],
        },
        "overall_verdict": historical["overall_verdict"],
        "claim_boundary": historical["claim_boundary"],
        "blocking_conditions": blockers,
        "next_smallest_test": "NONE_CURRENT_OBJECT_ROUTE_A_REJECTED_ROUTE_B_LOCKED",
        "round2_clues": historical["round2_clues"],
        "route_b_invocation_allowed": historical["route_b"]["invocation_allowed"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--paper-root", required=True)
    parser.add_argument("--skill", required=True)
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--code-commit", required=True)
    parser.add_argument("--repo-root", required=True)
    args = parser.parse_args()
    root = Path(args.paper_root)
    expectation, historical = validate_inputs(root, Path(args.skill), args.source_commit)
    validate_code_commit(root, Path(args.repo_root), args.code_commit)
    sys.stdout.buffer.write(canonical(render(
        expectation, historical, args.source_commit)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
