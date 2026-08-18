#!/usr/bin/env python3
"""Render the P45 actual Route record after the static renderer H1 exists."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import stat
import subprocess
import tempfile
from pathlib import Path


CONTRACT_REL = Path("code/route_actual_contract/ROUTE_ACTUAL_CONTRACT.json")
SCIENCE_SOURCE_COMMIT = "68369da38e651604cbee65df498846b863572448"
P45_PREFIX = "symbolic_dynamics/papers/45-isospectral-arithmetic-fiber-retractions"
ROUTE_TOP_KEYS = {
    "a0", "a1", "a2", "a3", "a4", "adversarial_controls",
    "artifact_path_base", "blocking_conditions", "candidate_id", "claim_boundary",
    "evaluation_date", "next_smallest_test", "overall_verdict", "round2_clues",
    "route_b_invocation_allowed", "skill", "skill_version", "source_commit", "source_lock",
}
SOURCE_LOCK_KEYS = {
    "allowed_data", "arithmetic_origin", "clock", "cutoff", "determinant_convention",
    "forbidden_data", "normalization", "object", "precision",
}
TRUSTED_GIT = Path("/usr/bin/git")
TRUSTED_GIT_SHA256 = "fd7c9389e200d626b46551835e5233bbde49a6a2326f9ebb85c70ed235861001"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def regular_under(root: Path, relative: str) -> Path:
    if relative.startswith("/") or ".." in Path(relative).parts:
        raise ValueError("unsafe relative path")
    path = root.joinpath(*relative.split("/"))
    if not path.is_file() or path.is_symlink():
        raise ValueError("nonregular contract path")
    return path


def git_environment() -> dict[str, str]:
    return {
        "GIT_CONFIG_GLOBAL": "/dev/null",
        "GIT_CONFIG_NOSYSTEM": "1",
        "GIT_CONFIG_SYSTEM": "/dev/null",
        "GIT_NO_REPLACE_OBJECTS": "1",
        "GIT_OPTIONAL_LOCKS": "0",
        "GIT_TERMINAL_PROMPT": "0",
        "HOME": "/nonexistent-paper45-route-git-home",
        "LANG": "C",
        "LC_ALL": "C",
        "PATH": "/usr/bin:/bin",
        "TZ": "UTC",
    }


def validate_git_boundary(repository: Path) -> None:
    git_metadata = os.lstat(TRUSTED_GIT)
    if TRUSTED_GIT.is_symlink() or not stat.S_ISREG(git_metadata.st_mode) \
            or stat.S_IMODE(git_metadata.st_mode) != 0o755 \
            or digest(TRUSTED_GIT) != TRUSTED_GIT_SHA256:
        raise ValueError("trusted Git boundary")
    repository_metadata = os.lstat(repository)
    dot_git = repository / ".git"
    dot_git_metadata = os.lstat(dot_git)
    if repository.is_symlink() or not stat.S_ISDIR(repository_metadata.st_mode) \
            or repository.resolve(strict=True) != repository \
            or dot_git.is_symlink() or not stat.S_ISDIR(dot_git_metadata.st_mode):
        raise ValueError("unsafe Git repository")


def git(repository: Path, arguments: list[str]) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        [str(TRUSTED_GIT), "--no-replace-objects", "--literal-pathspecs",
         "-C", str(repository), *arguments],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        env=git_environment(),
    )


def verify_h1_blobs(root: Path, repository: Path, commit: str, relatives: list[str]) -> dict:
    probe = git(repository, ["cat-file", "-t", commit])
    if probe.returncode != 0 or probe.stdout != b"commit\n" or probe.stderr:
        raise ValueError("expected H1 is not a readable commit")
    repository_paths = [P45_PREFIX + "/" + relative for relative in relatives]
    listing = git(repository, ["ls-tree", "-z", "--full-tree", commit, "--", *repository_paths])
    if listing.returncode != 0 or listing.stderr or not listing.stdout.endswith(b"\0"):
        raise ValueError("H1 tree lookup")
    entries = {}
    for row in listing.stdout.rstrip(b"\0").split(b"\0"):
        match = re.fullmatch(rb"100644 blob ([0-9a-f]{40})\t([^\0]+)", row)
        if match is None:
            raise ValueError("H1 tree entry is not exact 100644 blob")
        path = match.group(2).decode("ascii")
        if path in entries:
            raise ValueError("duplicate H1 tree entry")
        entries[path] = match.group(1).decode("ascii")
    if set(entries) != set(repository_paths) or len(entries) != len(relatives):
        raise ValueError("H1 tree path closure")
    result = {}
    for relative in relatives:
        local = regular_under(root, relative)
        repo_path = P45_PREFIX + "/" + relative
        oid = entries[repo_path]
        blob_run = git(repository, ["cat-file", "blob", oid])
        if blob_run.returncode != 0 or blob_run.stderr or blob_run.stdout != local.read_bytes():
            raise ValueError("H1 blob mismatch: " + relative)
        result[relative] = {"git_blob": oid, "sha256": digest(local)}
    return result


def require_science_ancestor(repository: Path, commit: str) -> None:
    ancestry = git(repository, ["merge-base", "--is-ancestor", SCIENCE_SOURCE_COMMIT, commit])
    if ancestry.returncode != 0 or ancestry.stdout or ancestry.stderr:
        raise ValueError("SCIENCE_SOURCE_NOT_ANCESTOR_OF_RENDERER_H1")


def main() -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--git-repo", type=Path, required=True)
    parser.add_argument("--route-renderer-commit", required=True)
    args = parser.parse_args()

    root = args.root.resolve(strict=True)
    repository = args.git_repo.resolve(strict=True)
    if not root.as_posix().startswith("/tmp/"):
        raise SystemExit("DISPOSABLE_TMP_ROOT_REQUIRED")
    renderer_commit = args.route_renderer_commit
    if not re.fullmatch(r"[0-9a-f]{40}", renderer_commit):
        raise SystemExit("INVALID_RENDERER_COMMIT")
    validate_git_boundary(repository)

    contract_path = root / CONTRACT_REL
    contract_raw = contract_path.read_bytes()
    contract = json.loads(contract_raw)
    if contract_raw != (json.dumps(contract, sort_keys=True, indent=2) + "\n").encode("utf-8"):
        raise SystemExit("NONCANONICAL_CONTRACT")
    if contract.get("schema") != "paper45.route-a-v0.2-render-contract.v1":
        raise SystemExit("CONTRACT_SCHEMA")
    if contract.get("science_source_commit") != SCIENCE_SOURCE_COMMIT:
        raise SystemExit("SCIENCE_SOURCE_CONTRACT")
    if contract.get("candidate_id") != "P45-ALLH-RETRACTIONS":
        raise SystemExit("CANDIDATE_CONTRACT")
    if contract.get("canonical_skill") != {
        "path": "skills/route-a-evaluator.md",
        "sha256": "29bd6275aa0c80ecce9cca898f06687208475c0a9a40cf3b9592fde45951458a",
        "version": "0.2.0",
    }:
        raise SystemExit("CANONICAL_SKILL_CONTRACT")
    if contract.get("trusted_git") != {
        "path": TRUSTED_GIT.as_posix(),
        "required_global_options": ["--no-replace-objects", "--literal-pathspecs"],
        "sha256": TRUSTED_GIT_SHA256,
    }:
        raise SystemExit("TRUSTED_GIT_CONTRACT")
    if renderer_commit == SCIENCE_SOURCE_COMMIT:
        raise SystemExit("RENDERER_COMMIT_MUST_POSTDATE_SCIENCE_SOURCE")
    for relative, expected in contract["evidence_sha256"].items():
        if digest(regular_under(root, relative)) != expected:
            raise SystemExit("EVIDENCE_DRIFT:" + relative)

    template_path = regular_under(root, contract["template_path"])
    if digest(template_path) != contract["template_sha256"]:
        raise SystemExit("TEMPLATE_DRIFT")
    template_raw = template_path.read_bytes()
    template = json.loads(template_raw)
    if template_raw != (json.dumps(template, sort_keys=True, indent=2) + "\n").encode("utf-8"):
        raise SystemExit("NONCANONICAL_TEMPLATE")
    if template.get("source_commit") != SCIENCE_SOURCE_COMMIT:
        raise SystemExit("SCIENCE_SOURCE_BINDING")
    if set(template) != ROUTE_TOP_KEYS or set(template.get("source_lock", {})) != SOURCE_LOCK_KEYS:
        raise SystemExit("CANONICAL_ROUTE_SCHEMA_SHAPE")

    require_science_ancestor(repository, renderer_commit)
    h1_blobs = verify_h1_blobs(
        root, repository, renderer_commit, contract["h1_static_code_paths"]
    )
    h1_blob_map_sha256 = hashlib.sha256(
        json.dumps(h1_blobs, sort_keys=True, separators=(",", ":")).encode("ascii")
    ).hexdigest()
    rendered = template
    raw = template_raw
    output = root.joinpath(*contract["record_path"].split("/"))
    if output.exists() or output.is_symlink():
        raise SystemExit("REFUSE_RECORD_OVERWRITE")
    output.parent.mkdir(mode=0o755, parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(prefix=".route-actual-", dir=output.parent)
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(raw)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temporary, 0o444)
        os.replace(temporary, output)
    finally:
        if temporary.exists():
            temporary.unlink()
    print(json.dumps({
        "candidate_id": rendered["candidate_id"],
        "code_commit": renderer_commit,
        "h1_blob_map_sha256": h1_blob_map_sha256,
        "h1_static_blob_count": len(h1_blobs),
        "record_path": contract["record_path"],
        "record_sha256": hashlib.sha256(raw).hexdigest(),
        "schema": "paper45.route-a-v0.2-render-receipt.v1",
        "science_ancestor_check": "PASS",
        "science_source_commit": contract["science_source_commit"],
        "status": "PASS",
        "trusted_git_path": TRUSTED_GIT.as_posix(),
        "trusted_git_sha256": TRUSTED_GIT_SHA256,
    }, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
