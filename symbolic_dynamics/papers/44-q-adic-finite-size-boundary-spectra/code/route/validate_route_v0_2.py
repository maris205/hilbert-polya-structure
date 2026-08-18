#!/usr/bin/env python3
"""Primary whole-object validator for the fresh SD-C46 Route-A v0.2 card."""

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


COMMIT = "b0e41ac3d6bd30618421d1b76122c3e9e04d070b"
GIT = "/usr/bin/git"
SKILL_HASH = "29bd6275aa0c80ecce9cca898f06687208475c0a9a40cf3b9592fde45951458a"
EXPECTATION_HASH = "0326a3c5d7bb10a953c9987d71d2c627798f138b5e671e74a114e5819c328892"
OLD_ROUTE_HASH = "e871be0a1fe6ca47566b82435eddf9e3b856c29a1940bd467cad19cf0b28e32f"
TUPLE = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_PARTIAL_ANALYTIC_STRUCTURE", "A4_FAIL"]
BASE = "papers/44-q-adic-finite-size-boundary-spectra"
HASHES = {
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
    "code/route/render_route_v0_2.py",
    "code/route/validate_route_v0_2.py",
    "code/route/audit_route_v0_2_independent.py",
    "code/tests/run_route_v0_2_mutations.py",
]


def encode(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=True, allow_nan=False, sort_keys=True,
                       indent=2, separators=(",", ": ")) + "\n").encode("ascii")


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    answer: dict[str, Any] = {}
    for key, value in pairs:
        if key in answer:
            raise ValueError("duplicate JSON member")
        answer[key] = value
    return answer


def exact_equal(left: Any, right: Any) -> bool:
    if type(left) is not type(right):
        return False
    if type(left) is dict:
        return set(left) == set(right) and all(exact_equal(left[k], right[k]) for k in left)
    if type(left) is list:
        return len(left) == len(right) and all(exact_equal(a, b) for a, b in zip(left, right))
    return left == right


def load_card(path: Path) -> tuple[dict[str, Any], bytes]:
    if not path.is_absolute() or path.is_symlink():
        raise ValueError("unsafe route argument")
    resolved = path.resolve(strict=True)
    mode = os.lstat(resolved).st_mode
    if not stat.S_ISREG(mode) or stat.S_IMODE(mode) != 0o644:
        raise ValueError("route kind/mode")
    raw = resolved.read_bytes()
    value = json.loads(raw.decode("ascii"), object_pairs_hook=reject_duplicates)
    if type(value) is not dict or raw != encode(value):
        raise ValueError("route is not canonical JSON/YAML")
    return value, raw


def file_below(root: Path, relative: str) -> Path:
    pure = PurePosixPath(relative)
    if pure.is_absolute() or "\\" in relative \
            or any(p in {"", ".", ".."} for p in pure.parts):
        raise ValueError("unsafe evidence path")
    path = root.joinpath(*pure.parts)
    cursor = path
    while cursor != root:
        if cursor.is_symlink():
            raise ValueError("evidence symlink")
        cursor = cursor.parent
    resolved = path.resolve(strict=True)
    mode = os.lstat(resolved).st_mode
    expected_mode = 0o444 if pure.parts[0] == "preauthority" else 0o644
    if root.resolve(strict=True) not in resolved.parents or not stat.S_ISREG(mode) \
            or stat.S_IMODE(mode) != expected_mode:
        raise ValueError("evidence physical contract")
    return resolved


def load_evidence_json(root: Path, relative: str) -> tuple[dict[str, Any], bytes]:
    raw = file_below(root, relative).read_bytes()
    value = json.loads(raw.decode("ascii"), object_pairs_hook=reject_duplicates)
    if type(value) is not dict or raw != encode(value):
        raise ValueError("noncanonical evidence")
    return value, raw


def with_prefix(values: list[str], more: list[str]) -> list[str]:
    result = ["preauthority/" + x for x in values] + more
    if len(result) != len(set(result)):
        raise ValueError("duplicate expected artifact")
    return result


def expected_object(pre: dict[str, Any], old: dict[str, Any]) -> dict[str, Any]:
    src = pre["source_lock"]
    keys_by_layer = {
        "a0": ["verdict", "evidence_status", "strongest_evidence", "strongest_failure", "arithmetic_controls"],
        "a1": ["verdict", "evidence_status", "strongest_evidence", "strongest_failure", "metrics"],
        "a2": ["verdict", "evidence_status", "strongest_evidence", "strongest_failure", "metrics"],
        "a3": ["verdict", "evidence_status", "strongest_evidence", "strongest_failure", "analytic_structure", "weil_compression"],
        "a4": ["verdict", "evidence_status", "strongest_evidence", "strongest_failure", "metrics"],
    }
    extras = {
        "a0": ["outputs/audits/source_audit.json", "outputs/tests/mutation_results.json"],
        "a1": ["outputs/audits/proof_audit.json", "outputs/audits/independence_audit.json"],
        "a2": ["outputs/audits/type_audit.json", "outputs/results/exact_comparison.json"],
        "a3": ["outputs/audits/proof_audit.json", "outputs/results/exact_comparison.json"],
        "a4": ["outputs/audits/type_audit.json", "outputs/audits/independence_audit.json"],
    }
    layers: dict[str, dict[str, Any]] = {}
    for label in ("a0", "a1", "a2", "a3", "a4"):
        source = pre[label]
        block = {key: source[key] for key in keys_by_layer[label]}
        block["artifacts"] = with_prefix(source["artifacts"], extras[label])
        layers[label] = block
    blockers = list(pre["blocking_conditions"])
    blockers.remove("evaluator_independence_remains_unexecuted")
    result = {
        **layers,
        "adversarial_controls": {
            key: pre["adversarial_controls"][key]
            for key in ("controls_used", "proves_too_much_risk", "verdict")
        },
        "artifact_path_base": BASE,
        "blocking_conditions": blockers,
        "candidate_id": "SD-C46",
        "claim_boundary": old["claim_boundary"],
        "evaluation_date": "2026-08-19",
        "next_smallest_test": "NONE_CURRENT_OBJECT_ROUTE_A_REJECTED_ROUTE_B_LOCKED",
        "overall_verdict": old["overall_verdict"],
        "round2_clues": old["round2_clues"],
        "route_b_invocation_allowed": old["route_b"]["invocation_allowed"],
        "skill": "route-a-evaluator",
        "skill_version": "0.2.0",
        "source_commit": COMMIT,
        "source_lock": {
            key: src[key] for key in (
                "allowed_data", "arithmetic_origin", "clock", "cutoff",
                "determinant_convention", "forbidden_data", "normalization",
                "object", "precision",
            )
        },
    }
    return result


def git_blob(repo: Path, commit: str, repository_path: str) -> bytes:
    spec = commit + ":" + repository_path
    run = subprocess.run([GIT, "--no-replace-objects", "-C", str(repo), "show", spec],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, check=False,
                         env={"PATH": os.environ.get("PATH", "/usr/bin:/bin"),
                              "LC_ALL": "C", "LANG": "C"})
    if run.returncode != 0 or run.stderr:
        raise ValueError("git provenance lookup failed")
    return run.stdout


def require_ancestor(repo: Path, ancestor: str, descendant: str) -> None:
    run = subprocess.run(
        [GIT, "--no-replace-objects", "-C", str(repo),
         "merge-base", "--is-ancestor", ancestor, descendant],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
        env={"PATH": os.environ.get("PATH", "/usr/bin:/bin"),
             "LC_ALL": "C", "LANG": "C"},
    )
    if run.returncode != 0 or run.stdout or run.stderr:
        raise ValueError("code commit is not descended from frozen science H1")


def main() -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--paper-root", required=True)
    parser.add_argument("--route", required=True)
    parser.add_argument("--skill", required=True)
    parser.add_argument("--repo-root", required=True)
    parser.add_argument("--code-commit", required=True)
    args = parser.parse_args()
    root = Path(args.paper_root)
    repo = Path(args.repo_root)
    if not root.is_absolute() or root.is_symlink() or root.resolve(strict=True) != root \
            or not root.is_dir() or stat.S_IMODE(os.lstat(root).st_mode) != 0o755:
        raise ValueError("unsafe paper root")
    if not repo.is_absolute() or repo.is_symlink() or repo.resolve(strict=True) != repo \
            or not (repo / ".git").is_dir():
        raise ValueError("unsafe repository root")
    skill = Path(args.skill)
    if not skill.is_absolute() or skill.is_symlink() or digest(skill.read_bytes()) != SKILL_HASH \
            or "**Version:** `0.2.0`" not in skill.read_text(encoding="utf-8"):
        raise ValueError("canonical skill mismatch")

    pre_raw = file_below(root, "preauthority/ROUTE_EXPECTATION.yaml").read_bytes()
    if digest(pre_raw) != EXPECTATION_HASH:
        raise ValueError("expectation digest")
    pre = yaml.safe_load(pre_raw.decode("utf-8"))
    old, old_raw = load_evidence_json(root, "outputs/evaluations/route_a/SD-C46/2026-08-18.yaml")
    if digest(old_raw) != OLD_ROUTE_HASH or old.get("route_tuple") != TUPLE \
            or old.get("skill_version") != "0.3.0" or old.get("source_commit") != COMMIT:
        raise ValueError("historical route chronology")
    if pre.get("route_tuple") != TUPLE or pre.get("skill_version") != "0.2.0":
        raise ValueError("frozen expected tuple")

    if re.fullmatch(r"[0-9a-f]{40}", args.code_commit) is None or args.code_commit == "0" * 40:
        raise ValueError("invalid code commit")
    require_ancestor(repo, COMMIT, args.code_commit)
    route, route_raw = load_card(Path(args.route))
    wanted = expected_object(pre, old)
    if not exact_equal(route, wanted):
        raise ValueError("complete v0.2 object mismatch")

    used = set()
    for layer in ("a0", "a1", "a2", "a3", "a4"):
        used.update(route[layer]["artifacts"])
    if used != set(HASHES):
        raise ValueError("artifact set is not exact")
    for relative, promised in HASHES.items():
        current = file_below(root, relative).read_bytes()
        repository_path = "symbolic_dynamics/papers/44-q-adic-finite-size-boundary-spectra/" + relative
        if digest(current) != promised or current != git_blob(repo, COMMIT, repository_path):
            raise ValueError("artifact hash/Git provenance mismatch: " + relative)
    for relative in CODE_PATHS:
        repository_path = "symbolic_dynamics/papers/44-q-adic-finite-size-boundary-spectra/" + relative
        if file_below(root, relative).read_bytes() != git_blob(repo, args.code_commit, repository_path):
            raise ValueError("code commit mismatch: " + relative)

    checks = {
        "canonical_skill_v0_2_exact": True,
        "canonical_whole_object_reconstructed": True,
        "frozen_expectation_inputs_exact": True,
        "historical_v0_3_chronology_preserved": True,
        "science_h1_is_ancestor_of_code_h1_prime": True,
        "h1_prime_code_commit_binds_all_evaluation_code": True,
        "required_artifact_set_hash_kind_mode_exact": True,
        "stale_preauthority_blocker_removed_only": True,
        "route_b_lock_derived_from_actual_record": True,
    }
    sys.stdout.buffer.write(encode({
        "payload": {
            "checks": checks,
            "checks_passed": len(checks),
            "checks_total": len(checks),
            "code_commit": args.code_commit,
            "route_sha256": digest(route_raw),
            "source_commit": COMMIT,
        },
        "schema": "paper44-route-v0.2-primary-audit-v1",
        "status": "PASS",
    }))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except SystemExit:
        raise
    except Exception:
        sys.stdout.buffer.write(encode({
            "payload": {"code": "ROUTE_V0_2_CONTRACT_REJECT"},
            "schema": "paper44-route-v0.2-primary-audit-v1",
            "status": "REJECT",
        }))
        raise SystemExit(2)
