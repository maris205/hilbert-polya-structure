#!/usr/bin/env python3
"""Positive and hostile tests for the two actual Route-A validators."""

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


RECORD = Path("evaluations/route_a/P45-ALLH-RETRACTIONS/2026-08-19.yaml")
CONTRACT = Path("code/route_actual_contract/ROUTE_ACTUAL_CONTRACT.json")
VALIDATORS = (
    Path("code/route_actual_main/validate_route_actual_main.py"),
    Path("code/route_actual_independent/validate_route_actual_independent.py"),
)
RENDERER = Path("code/route_actual_contract/render_route_actual.py")
P45_PREFIX = "symbolic_dynamics/papers/45-isospectral-arithmetic-fiber-retractions"
SCIENCE_SOURCE_COMMIT = "68369da38e651604cbee65df498846b863572448"
TRUSTED_GIT = Path("/usr/bin/git")
TRUSTED_GIT_SHA256 = "fd7c9389e200d626b46551835e5233bbde49a6a2326f9ebb85c70ed235861001"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical(path: Path, value) -> None:
    os.chmod(path, 0o644)
    path.write_text(json.dumps(value, sort_keys=True, indent=2) + "\n", encoding="utf-8")


def consumer_environment(overrides: dict[str, str] | None = None) -> dict[str, str]:
    environment = {
        "LANG": "C",
        "LC_ALL": "C",
        "PATH": "/usr/bin:/bin",
        "PYTHONDONTWRITEBYTECODE": "1",
        "TZ": "UTC",
    }
    if overrides:
        environment.update(overrides)
    return environment


def git_environment(author: bool = False) -> dict[str, str]:
    environment = {
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
    if author:
        environment.update({
            "GIT_AUTHOR_NAME": "Paper 45 Orphan Control",
            "GIT_AUTHOR_EMAIL": "p45-orphan-control@invalid",
            "GIT_AUTHOR_DATE": "2026-08-19T00:20:00Z",
            "GIT_COMMITTER_NAME": "Paper 45 Orphan Control",
            "GIT_COMMITTER_EMAIL": "p45-orphan-control@invalid",
            "GIT_COMMITTER_DATE": "2026-08-19T00:20:00Z",
        })
    return environment


def validate_trusted_git() -> None:
    metadata = os.lstat(TRUSTED_GIT)
    if TRUSTED_GIT.is_symlink() or not stat.S_ISREG(metadata.st_mode) \
            or stat.S_IMODE(metadata.st_mode) != 0o755 \
            or digest(TRUSTED_GIT) != TRUSTED_GIT_SHA256:
        raise SystemExit("TRUSTED_GIT_BOUNDARY")


def validate_repository(repository: Path) -> None:
    metadata = os.lstat(repository)
    dot_git = repository / ".git"
    dot_metadata = os.lstat(dot_git)
    if repository.is_symlink() or not stat.S_ISDIR(metadata.st_mode) \
            or repository.resolve(strict=True) != repository \
            or dot_git.is_symlink() or not stat.S_ISDIR(dot_metadata.st_mode):
        raise SystemExit("UNSAFE_GIT_REPOSITORY")


def git(repository: Path | None, arguments: list[str], author: bool = False) -> subprocess.CompletedProcess[bytes]:
    command = [str(TRUSTED_GIT), "--no-replace-objects", "--literal-pathspecs"]
    if repository is not None:
        command.extend(["-C", str(repository)])
    command.extend(arguments)
    return subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=git_environment(author=author),
        check=False,
    )


def invoke(root: Path, validator: Path, canonical_skill: Path, repository: Path,
           renderer_commit: str, environment: dict[str, str] | None = None) -> tuple[int, dict, str]:
    run = subprocess.run(
        [
            sys.executable, "-I", "-B", str(root / validator),
            "--root", str(root),
            "--canonical-skill", str(canonical_skill),
            "--git-repo", str(repository),
            "--expected-renderer-commit", renderer_commit,
        ],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=consumer_environment() if environment is None else environment,
        check=False,
    )
    try:
        receipt = json.loads(run.stdout)
    except Exception:
        receipt = {"status": "UNPARSEABLE"}
    return run.returncode, receipt, run.stderr


def create_orphan_static_repo(root: Path, parent: Path, relatives: list[str],
                              source_repository: Path) -> tuple[Path, str]:
    repository = parent / "orphan-repository"
    initialized = git(None, ["init", "-q", "--object-format=sha1", str(repository)])
    if initialized.returncode != 0 or initialized.stderr:
        raise SystemExit("ORPHAN_INIT_FAILURE")
    validate_repository(repository.resolve(strict=True))
    source_objects = (source_repository / ".git" / "objects").resolve(strict=True)
    if source_objects.is_symlink() or not source_objects.is_dir():
        raise SystemExit("SOURCE_OBJECT_DIRECTORY")
    alternates = repository / ".git" / "objects" / "info" / "alternates"
    alternates.parent.mkdir(mode=0o755, parents=True, exist_ok=True)
    alternates.write_text(source_objects.as_posix() + "\n", encoding="ascii")
    os.chmod(alternates, 0o444)
    for relative in relatives:
        source = root.joinpath(*relative.split("/"))
        destination = repository.joinpath(*P45_PREFIX.split("/"), *relative.split("/"))
        destination.parent.mkdir(mode=0o755, parents=True, exist_ok=True)
        shutil.copy2(source, destination)
    added = git(repository, ["add", "--", P45_PREFIX])
    committed = git(
        repository,
        ["-c", "core.hooksPath=/dev/null", "-c", "commit.gpgsign=false", "commit", "-q",
         "-m", "Paper 45 orphan identical-static-blobs control"],
        author=True,
    )
    oid_run = git(repository, ["rev-parse", "--verify", "HEAD^{commit}"])
    if any(run.returncode != 0 or run.stderr for run in (added, committed, oid_run)):
        raise SystemExit("ORPHAN_COMMIT_FAILURE")
    commit = oid_run.stdout.decode("ascii").strip()
    if re.fullmatch(r"[0-9a-f]{40}", commit) is None:
        raise SystemExit("ORPHAN_COMMIT_OID")
    parents = git(repository, ["rev-list", "--parents", "-n", "1", commit])
    if parents.returncode != 0 or parents.stderr \
            or parents.stdout.decode("ascii").strip().split() != [commit]:
        raise SystemExit("ORPHAN_IS_NOT_ROOT")
    return repository, commit


def activate_replace_fixture(repository: Path, orphan_commit: str) -> str:
    tree = git(repository, ["rev-parse", "--verify", orphan_commit + "^{tree}"])
    if tree.returncode != 0 or tree.stderr or re.fullmatch(rb"[0-9a-f]{40}\n", tree.stdout) is None:
        raise SystemExit("ORPHAN_TREE_LOOKUP")
    surrogate = git(
        repository,
        ["commit-tree", tree.stdout.decode("ascii").strip(), "-p", SCIENCE_SOURCE_COMMIT],
        author=True,
    )
    if surrogate.returncode != 0 or surrogate.stderr \
            or re.fullmatch(rb"[0-9a-f]{40}\n", surrogate.stdout) is None:
        raise SystemExit("REPLACE_SURROGATE_COMMIT")
    surrogate_commit = surrogate.stdout.decode("ascii").strip()
    ancestry = git(repository, ["merge-base", "--is-ancestor", SCIENCE_SOURCE_COMMIT, surrogate_commit])
    surrogate_tree = git(repository, ["rev-parse", "--verify", surrogate_commit + "^{tree}"])
    if ancestry.returncode != 0 or ancestry.stdout or ancestry.stderr \
            or surrogate_tree.returncode != 0 or surrogate_tree.stderr \
            or surrogate_tree.stdout != tree.stdout:
        raise SystemExit("REPLACE_SURROGATE_TOPOLOGY")
    installed = git(repository, ["replace", orphan_commit, surrogate_commit])
    ref = git(repository, ["rev-parse", "--verify", "refs/replace/" + orphan_commit])
    if installed.returncode != 0 or installed.stderr \
            or ref.returncode != 0 or ref.stderr \
            or ref.stdout.decode("ascii").strip() != surrogate_commit:
        raise SystemExit("REPLACE_REF_INSTALL")
    return surrogate_commit


def invoke_renderer(root: Path, repository: Path, commit: str, environment: dict) -> tuple[int, str, str]:
    run = subprocess.run(
        [
            sys.executable, "-I", "-B", str(root / RENDERER),
            "--root", str(root), "--git-repo", str(repository),
            "--route-renderer-commit", commit,
        ],
        text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        env=environment, check=False,
    )
    return run.returncode, run.stdout, run.stderr


def h1_blob_map(root: Path, repository: Path, commit: str, relatives: list[str]) -> dict:
    probe = git(repository, ["cat-file", "-t", commit])
    if probe.returncode != 0 or probe.stderr or probe.stdout != b"commit\n":
        raise SystemExit("H1_COMMIT_TYPE")
    repository_paths = [P45_PREFIX + "/" + relative for relative in relatives]
    listing = git(repository, ["ls-tree", "-z", "--full-tree", commit, "--", *repository_paths])
    if listing.returncode != 0 or listing.stderr or not listing.stdout.endswith(b"\0"):
        raise SystemExit("H1_TREE_LOOKUP")
    entries = {}
    for row in listing.stdout.rstrip(b"\0").split(b"\0"):
        match = re.fullmatch(rb"100644 blob ([0-9a-f]{40})\t([^\0]+)", row)
        if match is None:
            raise SystemExit("H1_TREE_NOT_EXACT_100644_BLOB")
        path = match.group(2).decode("ascii")
        if path in entries:
            raise SystemExit("H1_TREE_DUPLICATE")
        entries[path] = match.group(1).decode("ascii")
    if set(entries) != set(repository_paths) or len(entries) != len(relatives):
        raise SystemExit("H1_TREE_PATH_CLOSURE")
    result = {}
    for relative in relatives:
        repo_path = P45_PREFIX + "/" + relative
        oid = entries[repo_path]
        blob_run = git(repository, ["cat-file", "blob", oid])
        local = root.joinpath(*relative.split("/"))
        if blob_run.returncode != 0 or blob_run.stderr or blob_run.stdout != local.read_bytes():
            raise SystemExit("H1_BLOB_MISMATCH:" + relative)
        result[relative] = {
            "git_blob": oid,
            "sha256": digest(local),
        }
    return result


def edit_record(root: Path, operation) -> None:
    path = root / RECORD
    value = json.loads(path.read_bytes())
    operation(value)
    canonical(path, value)


def duplicate_skill(root: Path) -> None:
    path = root / RECORD
    os.chmod(path, 0o644)
    raw = path.read_text(encoding="utf-8")
    path.write_text(raw.replace('  "skill": "route-a-evaluator",', '  "skill": "route-a-evaluator",\n  "skill": "route-a-evaluator",', 1), encoding="utf-8")


def drift_source(root: Path) -> None:
    path = root / "inputs/preauthority/SOURCE_LOCK.md"
    os.chmod(path, 0o644)
    path.write_bytes(path.read_bytes() + b"\n")


def drift_result(root: Path) -> None:
    path = root / "results/evaluation_report.json"
    value = json.loads(path.read_bytes())
    value["c2"] = "HOLD_REPAIR"
    canonical(path, value)


def drift_result_manifest(root: Path) -> None:
    path = root / "results/SHA256SUMS.txt"
    os.chmod(path, 0o644)
    raw = path.read_text(encoding="ascii")
    path.write_text("0" + raw[1:], encoding="ascii")


ATTACKS = (
    ("duplicate_skill_key", duplicate_skill),
    ("skill_version_0_3", lambda root: edit_record(root, lambda value: value.__setitem__("skill_version", "0.3.0"))),
    ("guessed_sd_c47_identity", lambda root: edit_record(root, lambda value: value.__setitem__("candidate_id", "SD-C47"))),
    ("wrong_science_source_commit", lambda root: edit_record(root, lambda value: value.__setitem__("source_commit", "0" * 40))),
    ("noncanonical_code_commit_in_record", lambda root: edit_record(root, lambda value: value.__setitem__("code_commit", "1" * 40))),
    ("a0_promoted", lambda root: edit_record(root, lambda value: value["a0"].__setitem__("verdict", "A0_ANALYTIC_ARITHMETIC_ORIGIN"))),
    ("route_b_unlocked", lambda root: edit_record(root, lambda value: value.__setitem__("route_b_invocation_allowed", True))),
    ("external_go_retyped_as_route", lambda root: edit_record(root, lambda value: value.__setitem__("overall_verdict", "GO_EVALUATED"))),
    ("record_artifact_digest_changed", lambda root: edit_record(root, lambda value: value["a2"]["artifacts"][0].__setitem__("sha256", "0" * 64))),
    ("source_lock_byte_drift", drift_source),
    ("evaluation_report_drift", drift_result),
    ("result_manifest_drift", drift_result_manifest),
)


def write_receipt(root: Path, contract: dict, receipt: dict) -> None:
    relative = contract["validation_receipt_path"]
    if relative.startswith("/") or ".." in Path(relative).parts:
        raise SystemExit("UNSAFE_RECEIPT_PATH")
    output = root.joinpath(*relative.split("/"))
    if output.exists() or output.is_symlink():
        raise SystemExit("REFUSE_RECEIPT_OVERWRITE")
    output.parent.mkdir(mode=0o755, parents=True, exist_ok=True)
    raw = (json.dumps(receipt, sort_keys=True, indent=2) + "\n").encode("utf-8")
    descriptor, temporary_name = tempfile.mkstemp(prefix=".route-validation-", dir=output.parent)
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


def main() -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--canonical-skill", type=Path, required=True)
    parser.add_argument("--git-repo", type=Path, required=True)
    parser.add_argument("--expected-renderer-commit", required=True)
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve(strict=True)
    canonical_skill = args.canonical_skill.resolve(strict=True)
    repository = args.git_repo.resolve(strict=True)
    renderer_commit = args.expected_renderer_commit
    if re.fullmatch(r"[0-9a-f]{40}", renderer_commit) is None:
        raise SystemExit("INVALID_RENDERER_COMMIT")
    validate_trusted_git()
    validate_repository(repository)

    contract = json.loads((root / CONTRACT).read_bytes())
    if digest(canonical_skill) != contract["canonical_skill"]["sha256"]:
        raise SystemExit("CANONICAL_SKILL_DRIFT")
    static_blobs = h1_blob_map(root, repository, renderer_commit, contract["h1_static_code_paths"])
    static_blob_map_sha256 = hashlib.sha256(
        json.dumps(static_blobs, sort_keys=True, separators=(",", ":")).encode("ascii")
    ).hexdigest()

    normal = []
    for validator in VALIDATORS:
        rc, receipt, stderr = invoke(root, validator, canonical_skill, repository, renderer_commit)
        if rc != 0 or receipt.get("status") != "PASS" or stderr \
                or receipt.get("h1_blob_map_sha256") != static_blob_map_sha256 \
                or receipt.get("h1_static_blob_count") != len(static_blobs):
            raise SystemExit("NORMAL_VALIDATOR_FAILURE:" + validator.as_posix())
        normal.append({"receipt": receipt, "validator": validator.as_posix()})

    outcomes = []
    for attack_id, attack in ATTACKS:
        temporary = Path(tempfile.mkdtemp(prefix="p45-route-attack-", dir="/tmp"))
        clone = temporary / "candidate"
        try:
            shutil.copytree(root, clone, symlinks=True)
            attack(clone)
            for validator in VALIDATORS:
                rc, receipt, stderr = invoke(clone, validator, canonical_skill, repository, renderer_commit)
                outcomes.append({
                    "attack_id": attack_id,
                    "rc": rc,
                    "status": receipt.get("status"),
                    "stderr_bytes": len(stderr.encode("utf-8")),
                    "validator": validator.as_posix(),
                })
                if rc != 2 or receipt.get("status") != "REJECT" or stderr:
                    raise SystemExit("ATTACK_SURVIVED:" + attack_id + ":" + validator.as_posix())
        finally:
            shutil.rmtree(temporary, ignore_errors=True)

    topology_temporary = Path(tempfile.mkdtemp(prefix="p45-route-orphan-", dir="/tmp"))
    topology_outcomes = []
    topology_attack_ids = [
        "ORPHAN_IDENTICAL_STATIC_BLOBS",
        "HOSTILE_PATH_FAKE_GIT_ORPHAN",
        "REPLACE_REF_ORPHAN",
    ]
    replace_surrogate_commit = None
    try:
        orphan_repository, orphan_commit = create_orphan_static_repo(
            root, topology_temporary, contract["h1_static_code_paths"], repository
        )
        orphan_blob_map = h1_blob_map(
            root, orphan_repository, orphan_commit, contract["h1_static_code_paths"]
        )
        if orphan_blob_map != static_blobs:
            raise SystemExit("ORPHAN_STATIC_BLOB_MAP_DRIFT")

        def exercise_topology(attack_id: str, environment: dict[str, str]) -> None:
            renderer_rc, renderer_stdout, renderer_stderr = invoke_renderer(
                root, orphan_repository, orphan_commit, environment
            )
            renderer_rejected = renderer_rc != 0 \
                and "SCIENCE_SOURCE_NOT_ANCESTOR_OF_RENDERER_H1" in renderer_stderr
            topology_outcomes.append({
                "attack_id": attack_id,
                "consumer": "renderer",
                "rc": renderer_rc,
                "rejected": renderer_rejected,
                "stderr_bytes": len(renderer_stderr.encode("utf-8")),
                "stdout_bytes": len(renderer_stdout.encode("utf-8")),
            })
            if not renderer_rejected:
                raise SystemExit("TOPOLOGY_RENDERER_SURVIVED:" + attack_id)
            for validator in VALIDATORS:
                rc, topology_receipt, stderr = invoke(
                    root, validator, canonical_skill, orphan_repository, orphan_commit,
                    environment=environment,
                )
                rejected = rc == 2 and topology_receipt.get("status") == "REJECT" and not stderr
                topology_outcomes.append({
                    "attack_id": attack_id,
                    "consumer": validator.as_posix(),
                    "rc": rc,
                    "rejected": rejected,
                    "stderr_bytes": len(stderr.encode("utf-8")),
                })
                if not rejected:
                    raise SystemExit("TOPOLOGY_VALIDATOR_SURVIVED:" + attack_id + ":" + validator.as_posix())

        exercise_topology(topology_attack_ids[0], consumer_environment())

        fake_directory = topology_temporary / "hostile-path"
        fake_directory.mkdir(mode=0o755)
        fake_marker = topology_temporary / "FAKE_GIT_WAS_INVOKED"
        fake_git = fake_directory / "git"
        fake_git.write_text(
            "#!/bin/sh\nprintf invoked > " + fake_marker.as_posix() + "\nexit 0\n",
            encoding="ascii",
        )
        os.chmod(fake_git, 0o755)
        hostile_path_environment = consumer_environment({
            "GIT_CONFIG_COUNT": "1",
            "GIT_CONFIG_KEY_0": "alias.merge-base",
            "GIT_CONFIG_VALUE_0": "!true",
            "GIT_OBJECT_DIRECTORY": "/tmp/nonexistent-p45-hostile-object-directory",
            "GIT_REPLACE_REF_BASE": "refs/replace/",
            "PATH": fake_directory.as_posix() + ":/usr/bin:/bin",
        })
        exercise_topology(topology_attack_ids[1], hostile_path_environment)
        if fake_marker.exists() or fake_marker.is_symlink():
            raise SystemExit("HOSTILE_PATH_FAKE_GIT_INVOKED")

        replace_surrogate_commit = activate_replace_fixture(orphan_repository, orphan_commit)
        if h1_blob_map(root, orphan_repository, orphan_commit,
                       contract["h1_static_code_paths"]) != orphan_blob_map:
            raise SystemExit("NO_REPLACE_TREE_REPLAY_DRIFT")
        replace_environment = consumer_environment({
            "GIT_NO_REPLACE_OBJECTS": "0",
            "GIT_REPLACE_REF_BASE": "refs/replace/",
        })
        exercise_topology(topology_attack_ids[2], replace_environment)
    finally:
        shutil.rmtree(topology_temporary, ignore_errors=True)

    receipt = {
        "attack_count": len(ATTACKS),
        "attack_validator_calls": len(outcomes),
        "canonical_skill_sha256": digest(canonical_skill),
        "code_commit": renderer_commit,
        "contract_sha256": digest(root / CONTRACT),
        "h1_blob_map_sha256": static_blob_map_sha256,
        "h1_static_blob_count": len(static_blobs),
        "h1_static_blobs": static_blobs,
        "normal": normal,
        "record_sha256": digest(root / RECORD),
        "record_source_commit": "68369da38e651604cbee65df498846b863572448",
        "record_source_lock_key_count": 9,
        "record_top_level_key_count": 19,
        "route_renderer_commit": renderer_commit,
        "schema": "paper45.route-a-v0.2-hostile-tests.v2",
        "science_source_commit": "68369da38e651604cbee65df498846b863572448",
        "status": "PASS",
        "survivors": 0,
        "topology_attack_count": len(topology_attack_ids),
        "topology_attack_ids": topology_attack_ids,
        "topology_calls": len(topology_outcomes),
        "topology_fake_git_invoked": False,
        "topology_orphan_commit": orphan_commit,
        "topology_outcomes": topology_outcomes,
        "topology_replace_surrogate_commit": replace_surrogate_commit,
        "topology_survivors": sum(not row["rejected"] for row in topology_outcomes),
        "trusted_git_path": TRUSTED_GIT.as_posix(),
        "trusted_git_sha256": TRUSTED_GIT_SHA256,
        "validator_sha256": {path.as_posix(): digest(root / path) for path in VALIDATORS},
    }
    if args.write_receipt:
        write_receipt(root, contract, receipt)
    print(json.dumps(receipt, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
