#!/usr/bin/env python3
"""Independent schema/semantics/provenance auditor for SD-C46 Route-A v0.2.

Unlike the primary validator, this program does not read the preauthority
expectation and does not reconstruct the card through the renderer's mapping.
It validates the published card node-by-node, locks independent component
digests, and audits the two Git provenance domains directly.
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


SCIENCE_COMMIT = "b0e41ac3d6bd30618421d1b76122c3e9e04d070b"
GIT = "/usr/bin/git"
PAPER_PREFIX = "symbolic_dynamics/papers/44-q-adic-finite-size-boundary-spectra/"
SKILL_SHA = "29bd6275aa0c80ecce9cca898f06687208475c0a9a40cf3b9592fde45951458a"
TOP_KEYS = {
    "a0", "a1", "a2", "a3", "a4", "adversarial_controls",
    "artifact_path_base", "blocking_conditions", "candidate_id", "claim_boundary",
    "evaluation_date", "next_smallest_test", "overall_verdict",
    "round2_clues", "route_b_invocation_allowed", "skill", "skill_version",
    "source_commit", "source_lock",
}
NESTED_KEYS = {
    "source_lock": {
        "object", "arithmetic_origin", "clock", "normalization",
        "determinant_convention", "cutoff", "precision", "allowed_data", "forbidden_data",
    },
    "a0": {
        "verdict", "evidence_status", "strongest_evidence", "strongest_failure",
        "arithmetic_controls", "artifacts",
    },
    "a1": {
        "verdict", "evidence_status", "strongest_evidence", "strongest_failure",
        "metrics", "artifacts",
    },
    "a2": {
        "verdict", "evidence_status", "strongest_evidence", "strongest_failure",
        "metrics", "artifacts",
    },
    "a3": {
        "verdict", "evidence_status", "strongest_evidence", "strongest_failure",
        "analytic_structure", "weil_compression", "artifacts",
    },
    "a4": {
        "verdict", "evidence_status", "strongest_evidence", "strongest_failure",
        "metrics", "artifacts",
    },
    "adversarial_controls": {"controls_used", "proves_too_much_risk", "verdict"},
}
COMPONENT_SHA = {
    "source_lock": "dde6551347a78788b30599c11cbe42aff08c634a28fbf398dcea3cc67f9c2b22",
    "a0": "eb211a43221970da14fea27092eecc8b64538493deb6bab8ab6d93986a02eb7c",
    "a1": "ca6a044e664809cc62abf04af94a08ee78097e87f332e7ffdf78c93f1f029177",
    "a2": "6e16c5e2508bb1716db751e32c08eab01f7879fe9aa027abcd5d14b86a655f3e",
    "a3": "b44b996894d53844eba84674ccacd02acc380de35b2068216696b07f0262179d",
    "a4": "5ec6c948668de8da21e2ddc9ff7103d7e5a39b646985a5fb4da0b83ab3d5eec4",
    "adversarial_controls": "9046cd0d22296db5fd2fb78561e4ef76e83930306bc21a518e6231b1cd58b373",
    "blocking_conditions": "26e3f0b6bda58cad03bd7df52bbafcd4b93126ad9c3254aa7abf4eec44b65197",
    "claim_boundary": "8068f387bdd762543aa5e298ad46b5562b7f35e7fe8e6f2f8ea48b520a47c546",
}
EVIDENCE_SHA = {
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
DERIVED_PATHS = [
    "evaluations/route_a/SD-C46/2026-08-19.yaml",
    "evidence/route_v0_2/PRIMARY_AUDIT.json",
    "evidence/route_v0_2/INDEPENDENT_AUDIT.json",
    "evidence/route_v0_2/MUTATION_RESULTS.json",
]


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, ensure_ascii=True, allow_nan=False,
                       indent=2, separators=(",", ": ")) + "\n").encode("ascii")


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def walk_unique(node: yaml.Node) -> None:
    if isinstance(node, yaml.MappingNode):
        names: set[str] = set()
        for key, value in node.value:
            if not isinstance(key, yaml.ScalarNode) or key.value in names:
                raise ValueError("duplicate or nonscalar YAML key")
            names.add(key.value)
            walk_unique(value)
    elif isinstance(node, yaml.SequenceNode):
        for value in node.value:
            walk_unique(value)


def load_route(path: Path) -> tuple[dict[str, Any], bytes]:
    if not path.is_absolute() or path.is_symlink():
        raise ValueError("unsafe route")
    resolved = path.resolve(strict=True)
    metadata = os.lstat(resolved)
    if not stat.S_ISREG(metadata.st_mode) or stat.S_IMODE(metadata.st_mode) != 0o644:
        raise ValueError("route physical contract")
    raw = resolved.read_bytes()
    text = raw.decode("ascii")
    syntax = yaml.compose(text, Loader=yaml.BaseLoader)
    if syntax is None:
        raise ValueError("empty route")
    walk_unique(syntax)
    value = json.loads(text)
    if type(value) is not dict or raw != canonical(value):
        raise ValueError("noncanonical JSON subset of YAML")
    return value, raw


def below(root: Path, relative: str) -> Path:
    pure = PurePosixPath(relative)
    if pure.is_absolute() or "\\" in relative or any(x in {"", ".", ".."} for x in pure.parts):
        raise ValueError("unsafe relative")
    candidate = root.joinpath(*pure.parts)
    cursor = candidate
    while cursor != root:
        if cursor.is_symlink():
            raise ValueError("symlink evidence")
        cursor = cursor.parent
    resolved = candidate.resolve(strict=True)
    metadata = os.lstat(resolved)
    expected_mode = 0o444 if pure.parts[0] == "preauthority" else 0o644
    if root.resolve(strict=True) not in resolved.parents or not stat.S_ISREG(metadata.st_mode) \
            or stat.S_IMODE(metadata.st_mode) != expected_mode:
        raise ValueError("bad evidence kind/mode")
    return resolved


def git(repo: Path, arguments: list[str], expected: int = 0) -> bytes:
    process = subprocess.run([GIT, "--no-replace-objects", "-C", str(repo), *arguments],
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, check=False,
                             env={"PATH": os.environ.get("PATH", "/usr/bin:/bin"),
                                  "LC_ALL": "C", "LANG": "C"})
    if process.returncode != expected or (expected == 0 and process.stderr):
        raise ValueError("Git provenance operation failed")
    return process.stdout


def validate_semantics(card: dict[str, Any]) -> None:
    if set(card) != TOP_KEYS:
        raise ValueError("top-level v0.2 schema")
    for key, required in NESTED_KEYS.items():
        if type(card.get(key)) is not dict or set(card[key]) != required:
            raise ValueError("nested v0.2 schema: " + key)
    stable = {
        "artifact_path_base": "papers/44-q-adic-finite-size-boundary-spectra",
        "candidate_id": "SD-C46",
        "evaluation_date": "2026-08-19",
        "next_smallest_test": "NONE_CURRENT_OBJECT_ROUTE_A_REJECTED_ROUTE_B_LOCKED",
        "overall_verdict": "ROUTE_A_REJECTED",
        "round2_clues": [],
        "route_b_invocation_allowed": False,
        "skill": "route-a-evaluator",
        "skill_version": "0.2.0",
        "source_commit": SCIENCE_COMMIT,
    }
    for key, expected in stable.items():
        if type(card.get(key)) is not type(expected) or card[key] != expected:
            raise ValueError("stable terminal/provenance field: " + key)
    tuple_observed = [card[f"a{i}"]["verdict"] for i in range(5)]
    if tuple_observed != ["A0_FAIL", "A1_FAIL", "A2_FAIL",
                          "A3_PARTIAL_ANALYTIC_STRUCTURE", "A4_FAIL"]:
        raise ValueError("Route tuple")
    if [card[f"a{i}"]["evidence_status"] for i in range(5)] \
            != ["MODELING_CHOICE", "NOT_TESTABLE", "NOT_TESTABLE", "PROVED", "NOT_TESTABLE"]:
        raise ValueError("evidence hierarchy")
    if card["a1"]["metrics"].get("periodic_orbit_ledger") is not False \
            or card["a2"]["metrics"].get("determinant_defined") is not False \
            or card["a3"]["analytic_structure"].get("unit_circle_natural_boundary") != "golden_control_only" \
            or card["a4"]["metrics"].get("route_b_readiness") is not False:
        raise ValueError("same-object failure semantics")
    for key, promised in COMPONENT_SHA.items():
        if sha(canonical(card[key])) != promised:
            raise ValueError("independent component lock: " + key)
    artifacts: list[str] = []
    for index in range(5):
        value = card[f"a{index}"]["artifacts"]
        if type(value) is not list or any(type(x) is not str for x in value):
            raise ValueError("artifact list type")
        artifacts.extend(value)
    if set(artifacts) != set(EVIDENCE_SHA) or len(artifacts) != 24:
        raise ValueError("artifact coverage/multiplicity")
    serialized = canonical(card)
    for forbidden in (b"evaluator_independence_remains_unexecuted", b"STOP_DUPLICATE",
                      b"ROUTE_A_REJECTED_NOT_EVALUATED", b"0.3.0"):
        if forbidden in serialized:
            raise ValueError("stale or foreign terminal token")


def main() -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--paper-root", required=True)
    parser.add_argument("--route", required=True)
    parser.add_argument("--skill", required=True)
    parser.add_argument("--repo-root", required=True)
    parser.add_argument("--code-commit", required=True)
    args = parser.parse_args()
    root, repo = Path(args.paper_root), Path(args.repo_root)
    if not root.is_absolute() or root.is_symlink() or root.resolve(strict=True) != root \
            or not root.is_dir() or stat.S_IMODE(os.lstat(root).st_mode) != 0o755:
        raise ValueError("unsafe paper root")
    if not repo.is_absolute() or repo.is_symlink() or repo.resolve(strict=True) != repo \
            or not (repo / ".git").exists():
        raise ValueError("unsafe Git root")
    if re.fullmatch(r"[0-9a-f]{40}", args.code_commit) is None \
            or args.code_commit == "0" * 40:
        raise ValueError("invalid code commit")
    skill = Path(args.skill)
    skill_text = skill.read_text(encoding="utf-8")
    if skill.is_symlink() or sha(skill.read_bytes()) != SKILL_SHA \
            or "**Version:** `0.2.0`" not in skill_text or "# 8. Output schema" not in skill_text:
        raise ValueError("skill lock")

    card, route_raw = load_route(Path(args.route))
    validate_semantics(card)
    for relative, promised in EVIDENCE_SHA.items():
        if sha(below(root, relative).read_bytes()) != promised:
            raise ValueError("physical evidence digest: " + relative)
    git(repo, ["merge-base", "--is-ancestor", SCIENCE_COMMIT, args.code_commit])
    git(repo, ["diff", "--quiet", SCIENCE_COMMIT, args.code_commit, "--",
               *[PAPER_PREFIX + p for p in sorted(EVIDENCE_SHA)]])
    for relative in CODE_PATHS:
        committed = git(repo, ["show", args.code_commit + ":" + PAPER_PREFIX + relative])
        if committed != below(root, relative).read_bytes():
            raise ValueError("code blob provenance: " + relative)
    for relative in DERIVED_PATHS:
        process = subprocess.run(
            [GIT, "--no-replace-objects", "-C", str(repo), "cat-file", "-e",
             args.code_commit + ":" + PAPER_PREFIX + relative],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
            env={"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "LC_ALL": "C", "LANG": "C"},
        )
        if process.returncode == 0:
            raise ValueError("derived card/receipt already present in H1 prime")

    checks = {
        "yaml_ast_duplicate_rejection": True,
        "canonical_json_yaml_byte_form": True,
        "section8_exact_recursive_schema": True,
        "independent_component_digest_locks": True,
        "tuple_overall_route_b_consistency": True,
        "science_h1_to_code_h1_prime_no_artifact_drift": True,
        "code_h1_prime_binds_four_executables": True,
        "derived_h2_prime_objects_absent_from_h1_prime": True,
    }
    sys.stdout.buffer.write(canonical({
        "payload": {
            "checks": checks,
            "checks_passed": len(checks),
            "checks_total": len(checks),
            "code_commit": args.code_commit,
            "route_sha256": sha(route_raw),
            "source_commit": SCIENCE_COMMIT,
        },
        "schema": "paper44-route-v0.2-independent-audit-v1",
        "status": "PASS",
    }))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except SystemExit:
        raise
    except Exception:
        sys.stdout.buffer.write(canonical({
            "payload": {"code": "ROUTE_V0_2_INDEPENDENT_REJECT"},
            "schema": "paper44-route-v0.2-independent-audit-v1",
            "status": "REJECT",
        }))
        raise SystemExit(2)
