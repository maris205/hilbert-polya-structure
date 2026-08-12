from __future__ import annotations

import copy
import hashlib
import importlib.util
import os
import stat
import subprocess
import sys
import tempfile
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
SCHEDULER_SOURCE = ROOT / "scripts/run_r401_val_l3_a1_v2_all_slabs.py"
STATIC_CHECKER_SOURCE = ROOT / "scripts/check_r401_val_l3_a1_v2_static_independent.py"
RELEASE_SOURCE = ROOT / "scripts/build_r401_val_l3_a1_v2_release_provenance.py"


def _load(name: str, path: Path):
    specification = importlib.util.spec_from_file_location(name, path)
    assert specification is not None and specification.loader is not None
    module = importlib.util.module_from_spec(specification)
    sys.modules[name] = module
    specification.loader.exec_module(module)
    return module


S = _load("r401_v2_scheduler_adversarial", SCHEDULER_SOURCE)
C = _load("r401_v2_static_checker_adversarial", STATIC_CHECKER_SOURCE)
R = _load("r401_v2_release_adversarial", RELEASE_SOURCE)
REAL_FLOCK = S.fcntl.flock


def _git(repository: Path, *argv: str) -> str:
    completed = subprocess.run(
        ("/usr/bin/git", "-C", os.fspath(repository), *argv),
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return completed.stdout.strip()


def _prepare_role11_publication(
    tmp_path: Path, monkeypatch,
) -> tuple[Path, Path, bytes, str]:
    """Build a non-scientific Git/tmp namespace around the real publisher."""

    repository = tmp_path / "authority"
    repository.mkdir()
    _git(repository, "init", "-b", "main")
    _git(repository, "config", "user.email", "test@example.invalid")
    _git(repository, "config", "user.name", "V2 Test")
    _git(repository, "remote", "add", "origin", S.V2_ROLE11_ORIGIN_URL)
    (repository / "baseline.txt").write_text("baseline\n", encoding="utf-8")
    _git(repository, "add", "baseline.txt")
    _git(repository, "commit", "-m", "baseline")
    capture_commit = _git(repository, "rev-parse", "HEAD")
    capture_tree = _git(repository, "rev-parse", "HEAD^{tree}")
    (repository / "research/route_a_wave_trace").mkdir(parents=True)
    (repository / "results").mkdir()

    candidate_parent = Path(tempfile.mkdtemp(
        prefix="a416-v2-role11-publish-", dir="/tmp"
    ))
    os.chmod(candidate_parent, 0o700)
    candidate = candidate_parent / "prefreeze-tests.json"
    candidate_raw = b'{"synthetic_role11":"non-scientific"}\n'
    S._v2_write_private_candidate(
        candidate,
        candidate_raw,
        maximum_bytes=S.V2_ROLE11_MAX_CANDIDATE_BYTES,
        context="synthetic role-11 publication candidate",
    )

    machine = {"python_arb": {"executable_path": sys.executable}}
    capture_inputs = ((), [], (), {}, machine)
    repository_payload = {
        "repository_snapshot": {
            "capture_commit_oid": capture_commit,
            "capture_tree_oid": capture_tree,
            "origin_main_oid": capture_commit,
        }
    }
    monkeypatch.setattr(S, "ROOT", repository)
    monkeypatch.setattr(S, "V2_ROLE11_FINAL_COMMAND_LOCKED", True)
    monkeypatch.setattr(
        S,
        "V2_ROLE11_EXPECTED_TEST_PASSED",
        {name: 1 for name in S.V2_ROLE11_TEST_TOTALS_KEYS},
    )
    monkeypatch.setattr(
        S, "_v2_role11_live_remote_probe", lambda _root: capture_commit
    )
    monkeypatch.setattr(
        S, "_v2_role11_capture_inputs", lambda _root: capture_inputs
    )
    monkeypatch.setattr(
        S,
        "validate_v2_prefreeze_test_record_bytes",
        lambda *_args, **_kwargs: repository_payload,
    )
    monkeypatch.setattr(
        S, "_v2_git_validate_current_repository", lambda *_args, **_kwargs: None
    )
    return repository, candidate, candidate_raw, capture_commit


def _prepare_role11_capture_terminal_attack(
    tmp_path: Path, monkeypatch, *, attack: str,
) -> tuple[Path, Path, Path]:
    """Reduce role-11 capture to its real candidate/repository transaction."""

    repository = tmp_path / f"capture-{attack}"
    repository.mkdir()
    _git(repository, "init", "-b", "main")
    _git(repository, "config", "user.email", "test@example.invalid")
    _git(repository, "config", "user.name", "V2 Test")
    (repository / "baseline.txt").write_text("baseline\n", encoding="utf-8")
    _git(repository, "add", "baseline.txt")
    _git(repository, "commit", "-m", "baseline")
    capture_commit = _git(repository, "rev-parse", "HEAD")
    capture_tree = _git(repository, "rev-parse", "HEAD^{tree}")
    (repository / "research/route_a_wave_trace").mkdir(parents=True)
    (repository / "results").mkdir()
    foreign = repository / "late-capture-foreign.txt"

    candidate_parent = Path(tempfile.mkdtemp(
        prefix="a416-v2-role11-capture-", dir="/tmp"
    ))
    os.chmod(candidate_parent, 0o700)
    candidate = candidate_parent / "prefreeze-tests.json"

    role_names = (
        "machine_freeze", "s0_compatibility", "scheduler",
        "release_builder", "s0_adapter", "test_adversarial",
    )
    entries = [
        {
            "role": role,
            "path": f"synthetic/{role}.bin",
            "sha256": hashlib.sha256(role.encode("ascii")).hexdigest(),
            "size_bytes": len(role),
            "mode": "0644",
            "nlink": 1,
        }
        for role in role_names
    ]
    machine = {"python_arb": {"executable_path": sys.executable}}
    input_calls = 0

    def capture_inputs(_root: Path):
        nonlocal input_calls
        input_calls += 1
        if attack == "untracked" and input_calls == 2:
            foreign.write_text("late capture foreign\n", encoding="utf-8")
        return (), entries, (), {}, machine

    remote_calls = 0

    def live_remote(_root: Path) -> str:
        nonlocal remote_calls
        remote_calls += 1
        if attack == "remote" and remote_calls == 4:
            return "f" * 40
        return capture_commit

    monkeypatch.setattr(S, "V2_ROLE11_FINAL_COMMAND_LOCKED", True)
    monkeypatch.setattr(
        S,
        "V2_ROLE11_EXPECTED_TEST_PASSED",
        {name: 1 for name in S.V2_ROLE11_TEST_TOTALS_KEYS},
    )
    monkeypatch.setattr(S, "_v2_role11_capture_inputs", capture_inputs)
    monkeypatch.setattr(S, "_v2_role11_live_remote_probe", live_remote)
    monkeypatch.setattr(S, "_v2_git_ref", lambda *_args, **_kwargs: capture_commit)
    monkeypatch.setattr(
        S, "_v2_git_commit_tree", lambda *_args, **_kwargs: capture_tree
    )
    monkeypatch.setattr(
        S, "_v2_git_validate_current_repository", lambda *_args, **_kwargs: None
    )
    monkeypatch.setattr(
        S, "_v2_git_origin_url", lambda *_args, **_kwargs: S.V2_ROLE11_ORIGIN_URL
    )
    monkeypatch.setattr(
        S,
        "v2_role11_fixed_command_argv",
        lambda *_args, **_kwargs: tuple((f"synthetic-{index}",) for index in range(7)),
    )
    monkeypatch.setattr(
        S,
        "_v2_role11_command_capture",
        lambda index, *_args, **_kwargs: {
            "name": f"synthetic-{index}",
            "semantic_receipt": {"synthetic": index},
        },
    )
    monkeypatch.setattr(
        S,
        "_v2_git_find_continuous_introduction",
        lambda *_args, **_kwargs: capture_commit,
    )
    monkeypatch.setattr(
        S,
        "build_v2_prefreeze_test_record",
        lambda **_kwargs: {
            "schema_version": 1,
            "artifact_role": "SYNTHETIC_NON_SCIENTIFIC_ROLE11",
        },
    )
    return repository, candidate, foreign


def _role5_payload() -> dict:
    return {
        "schema_version": 1,
        "protocol_id": S.PROTOCOL_ID,
        "artifact_role": "V2_DESIGN_REVIEW_AND_ATTEMPT1_WITHDRAWAL",
        "status": "ACCEPT_V2_CONTROL_DESIGN_WITHDRAW_ATTEMPT1",
        "authority": "INDEPENDENT_CONTROL_DESIGN_REVIEW_ONLY",
        "scientific_licensing_enabled": False,
        "production_authorized": False,
        "legacy_attempt": {
            "attempt_id": "A416_L3_A1_CONTROL_ATTEMPT_1",
            "status": "WITHDRAWN_NON_LICENSING",
            "terminal_commit": "e9a794d7f4734a1b23ba265c58bbbbc2aca6d5e0",
            "published_artifacts": [dict(item) for item in S.V2_ROLE5_LEGACY_ARTIFACTS],
            "defects": [dict(item) for item in S.V2_ROLE5_DEFECTS],
            "supersession_rule": S.V2_ROLE5_SUPERSESSION_RULE,
        },
        "reviewed_v2_inputs": [
            {
                "role": role,
                "path": dict(S.FORMAL_INPUT_ROLES)[role],
                "sha256": f"{index:064x}",
            }
            for index, role in enumerate(S.V2_ROLE5_REVIEWED_ROLES, start=1)
        ],
        "review": {
            "reviewer_independent_of_attempt1_author": True,
            "verdict": "ACCEPT_CONTROL_PLANE_V2_DESIGN",
            "p0_count": 0,
            "p1_count": 0,
            "p2_count": 0,
            "reviewed_commit": "a" * 40,
            "map_matches_contract": True,
            "legacy_bytes_unchanged": True,
            "scientific_protocol_unchanged": True,
        },
        "claim_boundary": S.V2_ROLE5_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }


def _prepare_role5_publication(
    tmp_path: Path, monkeypatch, *, label: str = "base",
) -> tuple[Path, Path, Path, bytes, bytes, str]:
    """Create a tiny clean/live Git authority and two external reviewed inputs."""

    repository = tmp_path / f"role5-authority-{label}"
    repository.mkdir()
    _git(repository, "init", "-b", "main")
    _git(repository, "config", "user.email", "test@example.invalid")
    _git(repository, "config", "user.name", "V2 Test")
    _git(repository, "remote", "add", "origin", S.V2_ROLE11_ORIGIN_URL)
    role_paths = dict(S.FORMAL_INPUT_ROLES)
    live_raw: dict[str, bytes] = {}
    for index, role in enumerate(S.V2_ROLE5_REVIEWED_ROLES, start=1):
        path = repository / role_paths[role]
        path.parent.mkdir(parents=True, exist_ok=True)
        raw = f"reviewed-{index:02d}-{role}\n".encode("utf-8")
        path.write_bytes(raw)
        path.chmod(0o644)
        live_raw[role] = raw
    _git(repository, "add", ".")
    _git(repository, "commit", "-m", "reviewed role-5 source image")
    reviewed_commit = _git(repository, "rev-parse", "HEAD")
    _git(
        repository,
        "update-ref",
        "refs/remotes/origin/main",
        reviewed_commit,
    )

    payload = _role5_payload()
    payload["review"]["reviewed_commit"] = reviewed_commit
    payload["reviewed_v2_inputs"] = [
        {
            "role": role,
            "path": role_paths[role],
            "sha256": hashlib.sha256(live_raw[role]).hexdigest(),
        }
        for role in S.V2_ROLE5_REVIEWED_ROLES
    ]
    candidate_raw = S.canonical_json_bytes(payload)
    candidate_parent = Path(
        "/tmp/a416-v2-role5-review." + os.urandom(16).hex()
    )
    candidate_parent.mkdir(mode=0o700)
    candidate = candidate_parent / S.V2_ROLE5_CANDIDATE_BASENAME
    S._v2_write_private_candidate(
        candidate,
        candidate_raw,
        maximum_bytes=S.V2_ROLE5_CANDIDATE_MAX_BYTES,
        context="synthetic external role-5 candidate",
    )

    candidate_sha256 = hashlib.sha256(candidate_raw).hexdigest()
    input_map_sha256 = hashlib.sha256(
        S.canonical_json_bytes(payload["reviewed_v2_inputs"])
    ).hexdigest()
    verify_payload = {
        "verification_status": S.V2_ROLE5_VERIFY_STATUS,
        "authority": S.V2_ROLE5_VERIFY_AUTHORITY,
        "candidate_sha256": candidate_sha256,
        "input_map_sha256": input_map_sha256,
        "size_bytes": len(candidate_raw),
        "promotion_authorized": False,
        "artifacts_written": False,
    }
    verify_raw = S.canonical_json_bytes(verify_payload)
    verify_parent = Path(
        "/tmp/a416-v2-role5-verify." + os.urandom(16).hex()
    )
    verify_parent.mkdir(mode=0o700)
    verify_receipt = verify_parent / S.V2_ROLE5_VERIFY_RECEIPT_BASENAME
    S._v2_write_private_candidate(
        verify_receipt,
        verify_raw,
        maximum_bytes=S.V2_ROLE5_VERIFY_RECEIPT_MAX_BYTES,
        context="synthetic role-24 role-5 receipt",
    )

    def validate_without_legacy_history(
        value: dict, root: Path, records: dict[str, S.FormalRoleRecord],
    ) -> None:
        assert root == repository
        S.validate_v2_role5_payload(value, records)

    monkeypatch.setattr(S, "ROOT", repository)
    monkeypatch.setattr(
        S, "_v2_role11_live_remote_probe", lambda root: reviewed_commit
    )
    monkeypatch.setattr(
        S,
        "validate_v2_role5_repository_bindings",
        validate_without_legacy_history,
    )
    return (
        repository,
        candidate,
        verify_receipt,
        candidate_raw,
        verify_raw,
        reviewed_commit,
    )


def _cleanup_role5_external(*paths: Path) -> None:
    for path in paths:
        try:
            if path.is_symlink() or path.is_file() or stat.S_ISFIFO(path.lstat().st_mode):
                path.unlink()
        except FileNotFoundError:
            pass
    for parent in {path.parent for path in paths}:
        try:
            parent.rmdir()
        except FileNotFoundError:
            pass


def _exercise_role5_prehook_attacks(tmp_path: Path, monkeypatch) -> None:
    """Replay all five mutable inputs across the mandatory pre-rename hook."""

    for attack in ("source", "git", "candidate", "receipt", "stage"):
        with monkeypatch.context() as local:
            (
                repository,
                candidate,
                verify_receipt,
                candidate_raw,
                _verify_raw,
                reviewed_commit,
            ) = _prepare_role5_publication(
                tmp_path, local, label=f"prehook-{attack}"
            )
            destination = repository / dict(S.FORMAL_INPUT_ROLES)[
                "implementation_design_review"
            ]
            expected = hashlib.sha256(candidate_raw).hexdigest()

            def inject(phase: str) -> None:
                if phase != "BEFORE_RENAME":
                    return
                if attack == "source":
                    source = repository / dict(S.FORMAL_INPUT_ROLES)[
                        S.V2_ROLE5_REVIEWED_ROLES[0]
                    ]
                    source.write_bytes(b"drifted reviewed source\n")
                elif attack == "git":
                    (repository / ".git/refs/heads/main").write_text(
                        "f" * 40 + "\n", encoding="ascii"
                    )
                elif attack in {"candidate", "receipt"}:
                    target = candidate if attack == "candidate" else verify_receipt
                    descriptor = os.open(
                        target,
                        os.O_RDWR | getattr(os, "O_NOFOLLOW", 0),
                    )
                    try:
                        assert os.pwrite(descriptor, b"X", 0) == 1
                        os.fsync(descriptor)
                    finally:
                        os.close(descriptor)
                else:
                    stages = tuple(destination.parent.glob(
                        ".R401_VAL_L3_A1_V2_DESIGN_REVIEW_AND_WITHDRAWAL.json.publish-*"
                    ))
                    assert len(stages) == 1
                    descriptor = os.open(
                        stages[0],
                        os.O_RDWR | getattr(os, "O_NOFOLLOW", 0),
                    )
                    try:
                        assert os.pwrite(descriptor, b"X", 0) == 1
                        os.fsync(descriptor)
                    finally:
                        os.close(descriptor)

            local.setattr(S, "_v2_role5_publication_fault_hook", inject)
            try:
                with pytest.raises((S.SchedulerContractError, OSError)):
                    S.publish_v2_role5(
                        os.fspath(candidate),
                        os.fspath(verify_receipt),
                        expected,
                        reviewed_commit,
                        S.V2_ROLE5_PUBLICATION_AUTHORITY,
                        os.fspath(repository),
                    )
                assert not destination.exists()
                assert not tuple(destination.parent.glob(
                    ".R401_VAL_L3_A1_V2_DESIGN_REVIEW_AND_WITHDRAWAL.json.publish-*"
                ))
            finally:
                if destination.exists() or destination.is_symlink():
                    destination.unlink()
                _cleanup_role5_external(candidate, verify_receipt)


def _exercise_role5_postrename_no_rollback(tmp_path: Path, monkeypatch) -> None:
    postrename_phases = (
        "AFTER_RENAME",
        "AFTER_DESTINATION_FSYNC",
        "AFTER_PUBLICATION_PARENT_FSYNC",
        "AFTER_ULTIMATE_REPLAY",
    )
    for phase in postrename_phases:
        with monkeypatch.context() as local:
            (
                repository,
                candidate,
                verify_receipt,
                candidate_raw,
                verify_raw,
                reviewed_commit,
            ) = _prepare_role5_publication(
                tmp_path, local, label=f"postrename-{phase.lower()}"
            )
            destination = repository / dict(S.FORMAL_INPUT_ROLES)[
                "implementation_design_review"
            ]

            def fail(boundary: str) -> None:
                if boundary == phase:
                    raise RuntimeError(f"synthetic role-5 crash at {phase}")

            local.setattr(S, "_v2_role5_publication_fault_hook", fail)
            try:
                with pytest.raises(RuntimeError, match=phase):
                    S.publish_v2_role5(
                        os.fspath(candidate),
                        os.fspath(verify_receipt),
                        hashlib.sha256(candidate_raw).hexdigest(),
                        reviewed_commit,
                        S.V2_ROLE5_PUBLICATION_AUTHORITY,
                        os.fspath(repository),
                    )
                assert destination.read_bytes() == candidate_raw
                assert stat.S_IMODE(destination.stat().st_mode) == 0o644
                assert candidate.read_bytes() == candidate_raw
                assert verify_receipt.read_bytes() == verify_raw
                assert not tuple(destination.parent.glob(
                    ".R401_VAL_L3_A1_V2_DESIGN_REVIEW_AND_WITHDRAWAL.json.publish-*"
                ))
            finally:
                if destination.exists() or destination.is_symlink():
                    destination.unlink()
                _cleanup_role5_external(candidate, verify_receipt)

    with monkeypatch.context() as local:
        (
            repository,
            candidate,
            verify_receipt,
            candidate_raw,
            _verify_raw,
            reviewed_commit,
        ) = _prepare_role5_publication(
            tmp_path, local, label="postultimate-inode-replacement"
        )
        destination = repository / dict(S.FORMAL_INPUT_ROLES)[
            "implementation_design_review"
        ]

        def replace(boundary: str) -> None:
            if boundary == "AFTER_ULTIMATE_REPLAY":
                destination.unlink()
                destination.write_bytes(candidate_raw)
                destination.chmod(0o644)

        local.setattr(S, "_v2_role5_publication_fault_hook", replace)
        try:
            with pytest.raises(S.PathContractError, match="posthook canonical"):
                S.publish_v2_role5(
                    os.fspath(candidate),
                    os.fspath(verify_receipt),
                    hashlib.sha256(candidate_raw).hexdigest(),
                    reviewed_commit,
                    S.V2_ROLE5_PUBLICATION_AUTHORITY,
                    os.fspath(repository),
                )
            assert destination.read_bytes() == candidate_raw
        finally:
            if destination.exists() or destination.is_symlink():
                destination.unlink()
            _cleanup_role5_external(candidate, verify_receipt)


def _exercise_role5_cleanup_guard(tmp_path: Path, monkeypatch) -> None:
    with monkeypatch.context() as local:
        (
            repository,
            candidate,
            verify_receipt,
            candidate_raw,
            verify_raw,
            reviewed_commit,
        ) = _prepare_role5_publication(tmp_path, local, label="cleanup-guard")
        destination = repository / dict(S.FORMAL_INPUT_ROLES)[
            "implementation_design_review"
        ]
        foreign_raw = b"foreign substituted role-5 stage\n"
        substituted_stage: Path | None = None

        def substitute(boundary: str) -> None:
            nonlocal substituted_stage
            if boundary != "BEFORE_RENAME":
                return
            stages = tuple(destination.parent.glob(
                ".R401_VAL_L3_A1_V2_DESIGN_REVIEW_AND_WITHDRAWAL.json.publish-*"
            ))
            assert len(stages) == 1
            substituted_stage = stages[0]
            substituted_stage.unlink()
            substituted_stage.write_bytes(foreign_raw)
            substituted_stage.chmod(0o644)

        local.setattr(S, "_v2_role5_publication_fault_hook", substitute)
        try:
            with pytest.raises(
                S.PathContractError, match="refused to unlink a replaced staging inode"
            ) as caught:
                S.publish_v2_role5(
                    os.fspath(candidate),
                    os.fspath(verify_receipt),
                    hashlib.sha256(candidate_raw).hexdigest(),
                    reviewed_commit,
                    S.V2_ROLE5_PUBLICATION_AUTHORITY,
                    os.fspath(repository),
                )
            assert caught.value.__cause__ is not None
            assert substituted_stage is not None
            assert substituted_stage.read_bytes() == foreign_raw
            assert not destination.exists()
            assert candidate.read_bytes() == candidate_raw
            assert verify_receipt.read_bytes() == verify_raw
        finally:
            if substituted_stage is not None and substituted_stage.exists():
                substituted_stage.unlink()
            if destination.exists() or destination.is_symlink():
                destination.unlink()
            _cleanup_role5_external(candidate, verify_receipt)


def _exercise_role5_concurrent_exact_one(tmp_path: Path, monkeypatch) -> None:
    with monkeypatch.context() as local:
        (
            repository,
            candidate,
            verify_receipt,
            candidate_raw,
            _verify_raw,
            reviewed_commit,
        ) = _prepare_role5_publication(tmp_path, local, label="concurrent")
        destination = repository / dict(S.FORMAL_INPUT_ROLES)[
            "implementation_design_review"
        ]
        expected = hashlib.sha256(candidate_raw).hexdigest()
        ready_r, ready_w = os.pipe()
        go_r, go_w = os.pipe()
        attempt_r, attempt_w = os.pipe()
        release_r, release_w = os.pipe()
        result_r, result_w = os.pipe()

        def read_exact(descriptor: int, size: int) -> bytes:
            chunks: list[bytes] = []
            while sum(map(len, chunks)) < size:
                chunk = os.read(descriptor, size - sum(map(len, chunks)))
                assert chunk
                chunks.append(chunk)
            return b"".join(chunks)

        def synchronized_flock(descriptor: int, operation: int) -> None:
            if operation != S.fcntl.LOCK_EX | S.fcntl.LOCK_NB:
                REAL_FLOCK(descriptor, operation)
                return
            os.write(ready_w, b"R")
            assert os.read(go_r, 1) == b"G"
            try:
                REAL_FLOCK(descriptor, operation)
            except BlockingIOError:
                os.write(attempt_w, b"F")
                raise
            os.write(attempt_w, b"W")
            assert os.read(release_r, 1) == b"C"

        local.setattr(S.fcntl, "flock", synchronized_flock)
        children: list[int] = []
        try:
            for _index in range(2):
                child = os.fork()
                if child == 0:
                    try:
                        receipt = S.publish_v2_role5(
                            os.fspath(candidate),
                            os.fspath(verify_receipt),
                            expected,
                            reviewed_commit,
                            S.V2_ROLE5_PUBLICATION_AUTHORITY,
                            os.fspath(repository),
                        )
                        outcome = "OK|" + receipt["design_review_sha256"]
                    except BaseException as error:
                        outcome = f"ERR|{type(error).__name__}|{error}"
                    os.write(result_w, (outcome + "\n").encode("utf-8"))
                    os._exit(0)
                children.append(child)
            os.close(ready_w)
            os.close(go_r)
            os.close(attempt_w)
            os.close(release_r)
            os.close(result_w)
            assert read_exact(ready_r, 2) == b"RR"
            os.write(go_w, b"GG")
            attempts = read_exact(attempt_r, 2)
            assert sorted(attempts) == [ord("F"), ord("W")]
            os.write(release_w, b"C")
            os.close(go_w)
            os.close(release_w)
            chunks: list[bytes] = []
            while True:
                chunk = os.read(result_r, 4096)
                if not chunk:
                    break
                chunks.append(chunk)
            outcomes = b"".join(chunks).decode("utf-8").splitlines()
            assert sum(row == f"OK|{expected}" for row in outcomes) == 1
            assert sum(row.startswith("ERR|PathContractError|") for row in outcomes) == 1
            for child in children:
                waited, status = os.waitpid(child, 0)
                assert waited == child and os.waitstatus_to_exitcode(status) == 0
            children.clear()
            assert destination.read_bytes() == candidate_raw
            assert candidate.read_bytes() == candidate_raw
            assert verify_receipt.exists()
        finally:
            for child in children:
                try:
                    os.kill(child, 9)
                except ProcessLookupError:
                    pass
                os.waitpid(child, 0)
            for descriptor in (
                ready_r, ready_w, go_r, go_w, attempt_r, attempt_w,
                release_r, release_w, result_r, result_w,
            ):
                try:
                    os.close(descriptor)
                except OSError:
                    pass
            if destination.exists() or destination.is_symlink():
                destination.unlink()
            _cleanup_role5_external(candidate, verify_receipt)


def _main_records(machine: dict) -> tuple[S.FormalRoleRecord, ...]:
    records = []
    for index, (role, path) in enumerate(S.FORMAL_INPUT_ROLES, start=1):
        if role == "machine_freeze":
            raw = S.canonical_json_bytes(machine)
        elif role == "prefreeze_review":
            raw = b"Verdict: ACCEPT_FOR_FREEZE\n"
        else:
            raw = f"role-{index}\n".encode("ascii")
        records.append(S.FormalRoleRecord(
            role=role,
            path=path,
            sha256=hashlib.sha256(raw).hexdigest(),
            raw=raw,
            stat_identity=(1, index, len(raw), index, index),
        ))
    return tuple(records)


def test_scheduler_checker_release_share_exact_map_and_main_schema() -> None:
    assert S.FORMAL_INPUT_ROLES == C.INPUT_ROLES == R.INPUT_ROLES
    assert len(S.FORMAL_INPUT_ROLES) == 53
    assert S.FORMAL_MAIN_FREEZE_REQUIRED_KEYS == C.MAIN_FREEZE_KEYS == R.MAIN_FREEZE_KEYS
    assert len(S.FORMAL_MAIN_FREEZE_REQUIRED_KEYS) == 26
    assert S.PROTOCOL_ID == C.PROTOCOL_ID == R.PROTOCOL_ID == "R401-VAL-L3-A1"


def test_v2_scheduler_is_self_contained_from_attempt1_scheduler() -> None:
    source = SCHEDULER_SOURCE.read_text(encoding="utf-8")
    assert "from run_r401_val_l3_a1_all_slabs import" not in source
    assert "import run_r401_val_l3_a1_all_slabs" not in source
    v2_roles = dict(S.FORMAL_INPUT_ROLES)
    for role in (
        "prefreeze_design", "formal_protocol", "scheduler_contract",
        "checker_contract", "release_contract", "scheduler",
        "static_checker_source", "branch_checker_source",
        "composite_checker_source", "s0_adapter", "release_builder",
        "test_static_scheduler", "test_static_checker", "test_branch_scheduler",
        "test_branch_checker", "test_s0_compatibility", "test_composite",
        "test_adversarial", "test_release",
    ):
        assert "v2" in Path(v2_roles[role]).name.lower()


def test_role5_closed15_and_exact_literals_reject_coherent_type_forgery(
    tmp_path: Path, monkeypatch,
) -> None:
    payload = _role5_payload()
    assert set(S.validate_v2_role5_payload(payload)) == S.V2_ROLE5_KEYS
    forged = copy.deepcopy(payload)
    forged["legacy_attempt"]["published_artifacts"][0]["role"] = "10"
    with pytest.raises(S.ProductionAuthorityError, match="publication map"):
        S.validate_v2_role5_payload(forged)
    forged = copy.deepcopy(payload)
    forged["review"]["map_matches_contract"] = 1
    with pytest.raises(S.ProductionAuthorityError, match="review gate"):
        S.validate_v2_role5_payload(forged)
    forged = copy.deepcopy(payload)
    forged["claim_boundary"] += " forged"
    with pytest.raises(S.ProductionAuthorityError, match="scalar"):
        S.validate_v2_role5_payload(forged)

    (
        repository,
        candidate,
        verify_receipt,
        candidate_raw,
        verify_raw,
        reviewed_commit,
    ) = _prepare_role5_publication(tmp_path, monkeypatch)
    expected = hashlib.sha256(candidate_raw).hexdigest()
    destination = repository / dict(S.FORMAL_INPUT_ROLES)[
        "implementation_design_review"
    ]

    def publish(
        *,
        candidate_path: Path = candidate,
        receipt_path: Path = verify_receipt,
        expected_hash: str = expected,
        commit: str = reviewed_commit,
        authority: str = S.V2_ROLE5_PUBLICATION_AUTHORITY,
    ) -> dict:
        return S.publish_v2_role5(
            os.fspath(candidate_path),
            os.fspath(receipt_path),
            expected_hash,
            commit,
            authority,
            os.fspath(repository),
        )

    try:
        for overrides in (
            {"expected_hash": "f" * 64},
            {"commit": "f" * 40},
            {"authority": "ROLE24_RECEIPT_IS_NOT_PUBLICATION_AUTHORITY"},
            {"candidate_path": verify_receipt, "receipt_path": candidate},
        ):
            with pytest.raises((S.SchedulerContractError, OSError)):
                publish(**overrides)
            assert not destination.exists()

        original_verify_payload = S.strict_json_loads(verify_raw.decode("utf-8"))
        for field, forged_value in (
            ("input_map_sha256", "f" * 64),
            ("candidate_sha256", "e" * 64),
            ("size_bytes", len(candidate_raw) + 1),
            ("promotion_authorized", 0),
        ):
            verify_receipt.unlink()
            forged_verify = copy.deepcopy(original_verify_payload)
            forged_verify[field] = forged_value
            S._v2_write_private_candidate(
                verify_receipt,
                S.canonical_json_bytes(forged_verify),
                maximum_bytes=S.V2_ROLE5_VERIFY_RECEIPT_MAX_BYTES,
                context="forged synthetic role-24 receipt",
            )
            with pytest.raises((S.SchedulerContractError, OSError)):
                publish()
            assert not destination.exists()
        verify_receipt.unlink()
        S._v2_write_private_candidate(
            verify_receipt,
            verify_raw,
            maximum_bytes=S.V2_ROLE5_VERIFY_RECEIPT_MAX_BYTES,
            context="restored synthetic role-24 receipt",
        )

        for path, wrong_mode in ((candidate, 0o644), (verify_receipt, 0o644)):
            path.chmod(wrong_mode)
            with pytest.raises((S.SchedulerContractError, OSError)):
                publish()
            path.chmod(0o600)
        for path in (candidate, verify_receipt):
            sibling = path.parent / "unexpected-sibling"
            sibling.write_bytes(b"foreign\n")
            with pytest.raises((S.SchedulerContractError, OSError)):
                publish()
            sibling.unlink()
        for path in (candidate, verify_receipt):
            alias = Path("/tmp/role5-hardlink-" + os.urandom(8).hex())
            os.link(path, alias)
            try:
                with pytest.raises((S.SchedulerContractError, OSError)):
                    publish()
            finally:
                alias.unlink()
        for path, raw, cap in (
            (candidate, candidate_raw, S.V2_ROLE5_CANDIDATE_MAX_BYTES),
            (verify_receipt, verify_raw, S.V2_ROLE5_VERIFY_RECEIPT_MAX_BYTES),
        ):
            path.unlink()
            path.write_bytes(b"X" * (cap + 1))
            path.chmod(0o600)
            with pytest.raises((S.SchedulerContractError, OSError)):
                publish()
            path.unlink()
            S._v2_write_private_candidate(
                path,
                raw,
                maximum_bytes=cap,
                context="restored capped role-5 external input",
            )
        for path, raw, cap in (
            (candidate, candidate_raw, S.V2_ROLE5_CANDIDATE_MAX_BYTES),
            (verify_receipt, verify_raw, S.V2_ROLE5_VERIFY_RECEIPT_MAX_BYTES),
        ):
            path.unlink()
            os.mkfifo(path, 0o600)
            with pytest.raises((S.SchedulerContractError, OSError)):
                publish()
            path.unlink()
            S._v2_write_private_candidate(
                path,
                raw,
                maximum_bytes=cap,
                context="restored FIFO-tested role-5 external input",
            )

        receipt = publish()
        assert list(receipt) == [
            "schema_version", "protocol_id", "artifact_role",
            "artifact_status", "authority", "candidate_path",
            "canonical_path", "design_review_sha256", "reviewed_commit",
            "size_bytes", "mode", "nlink", "serializer",
            "publication_method", "verify_receipt_sha256",
            "input_map_sha256",
            "independent_verification_receipt_validated",
            "scientific_licensing_enabled", "production_authorized",
            "scientific_dispatch_performed", "component_status",
            "milestone_status", "theorem_status", "final_status",
        ]
        assert receipt["design_review_sha256"] == expected
        assert receipt["reviewed_commit"] == reviewed_commit
        assert receipt["verify_receipt_sha256"] == hashlib.sha256(
            verify_raw
        ).hexdigest()
        assert receipt["input_map_sha256"] == hashlib.sha256(
            S.canonical_json_bytes(
                S.strict_json_loads(candidate_raw.decode("utf-8"))[
                    "reviewed_v2_inputs"
                ]
            )
        ).hexdigest()
        assert receipt["independent_verification_receipt_validated"] is True
        assert receipt["scientific_licensing_enabled"] is False
        assert receipt["production_authorized"] is False
        assert receipt["scientific_dispatch_performed"] is False
        assert tuple(receipt[key] for key in (
            "component_status", "milestone_status", "theorem_status",
            "final_status",
        )) == (None, None, None, None)
        assert destination.read_bytes() == candidate_raw
        destination_info = destination.stat()
        assert stat.S_IMODE(destination_info.st_mode) == 0o644
        assert destination_info.st_nlink == 1
        assert candidate.read_bytes() == candidate_raw
        assert verify_receipt.read_bytes() == verify_raw
        assert stat.S_IMODE(candidate.stat().st_mode) == 0o600
        assert stat.S_IMODE(verify_receipt.stat().st_mode) == 0o600
        assert not tuple(destination.parent.glob(
            ".R401_VAL_L3_A1_V2_DESIGN_REVIEW_AND_WITHDRAWAL.json.publish-*"
        ))
        with pytest.raises(
            (S.ProductionAuthorityError, S.PathContractError),
        ):
            publish()
        assert destination.read_bytes() == candidate_raw

        destination.unlink()
        for kind in ("regular", "symlink", "fifo", "directory", "hardlink"):
            anchor: Path | None = None
            if kind == "regular":
                destination.write_bytes(b"foreign regular\n")
                destination.chmod(0o644)
            elif kind == "symlink":
                destination.symlink_to("/tmp/role5-foreign-target")
            elif kind == "fifo":
                os.mkfifo(destination, 0o600)
            elif kind == "directory":
                destination.mkdir()
            else:
                anchor = destination.parent / "role5-hardlink-anchor"
                anchor.write_bytes(b"foreign hardlink\n")
                os.link(anchor, destination)
            before = destination.lstat()
            with pytest.raises((S.SchedulerContractError, OSError)):
                publish()
            after = destination.lstat()
            assert (after.st_dev, after.st_ino, stat.S_IFMT(after.st_mode)) == (
                before.st_dev, before.st_ino, stat.S_IFMT(before.st_mode)
            )
            if kind == "directory":
                destination.rmdir()
            else:
                destination.unlink()
            if anchor is not None:
                anchor.unlink()
    finally:
        if destination.is_dir() and not destination.is_symlink():
            destination.rmdir()
        elif destination.exists() or destination.is_symlink():
            destination.unlink()
        _cleanup_role5_external(candidate, verify_receipt)


def test_main_builder_exact26_and_order_rejection(monkeypatch) -> None:
    machine = {"synthetic_machine": True}
    records = _main_records(machine)
    monkeypatch.setattr(S, "_validate_formal_machine_envelope", lambda value: value)
    payload = S.build_v2_main_freeze_payload(records, machine)
    assert set(payload) == S.FORMAL_MAIN_FREEZE_REQUIRED_KEYS
    assert len(payload["input_roles"]) == 53
    assert [row["role"] for row in payload["input_roles"]] == [
        role for role, _path in S.FORMAL_INPUT_ROLES
    ]
    reordered = list(records)
    reordered[4], reordered[5] = reordered[5], reordered[4]
    with pytest.raises(S.ProductionAuthorityError, match="ordered 53"):
        S.build_v2_main_freeze_payload(reordered, machine)
    with pytest.raises(S.ProductionAuthorityError, match="ordered 53"):
        S.build_v2_main_freeze_payload(records[:-1], machine)


def test_directory_chain_detects_lexical_ancestor_replacement() -> None:
    base = Path("/tmp/a416-v2-chain-" + os.urandom(8).hex())
    original = base / "parent"
    moved = Path(os.fspath(base) + ".moved")
    original.mkdir(parents=True, mode=0o700)
    chain = S._machine_publication_directory_chain(original)
    descriptor = S._open_directory_fd(original)
    try:
        base.rename(moved)
        original.mkdir(parents=True, mode=0o700)
        with pytest.raises(S.PathContractError, match="namespace changed"):
            S._replay_machine_publication_directory(
                original, descriptor, chain, "ancestor attack"
            )
    finally:
        os.close(descriptor)
        original.rmdir()
        base.rmdir()
        (moved / "parent").rmdir()
        moved.rmdir()


def test_private_candidate_rejects_same_bytes_under_replaced_parent(
    tmp_path: Path, monkeypatch,
) -> None:
    parent = Path("/tmp/a416-v2-candidate-chain-" + os.urandom(8).hex())
    moved = Path(os.fspath(parent) + ".moved")
    parent.mkdir(mode=0o700)
    candidate = parent / "candidate.json"
    image = S._v2_write_private_candidate(
        candidate,
        b'{"candidate":"v2"}\n',
        maximum_bytes=1024,
        context="chain candidate",
    )
    parent.rename(moved)
    parent.mkdir(mode=0o700)
    replacement = parent / candidate.name
    replacement.write_bytes(image.raw)
    replacement.chmod(0o600)
    try:
        with pytest.raises(S.PathContractError, match="namespace changed"):
            S._v2_replay_private_candidate(
                replacement, image, context="candidate parent replacement"
            )
    finally:
        replacement.unlink()
        parent.rmdir()
        (moved / candidate.name).unlink()
        moved.rmdir()
    _exercise_role5_cleanup_guard(tmp_path, monkeypatch)


def test_role11_publisher_two_process_barrier_has_exactly_one_winner(
    tmp_path: Path, monkeypatch,
) -> None:
    repository, candidate, candidate_raw, _capture_commit = (
        _prepare_role11_publication(tmp_path, monkeypatch)
    )
    expected = hashlib.sha256(candidate_raw).hexdigest()
    canonical = repository / dict(S.FORMAL_INPUT_ROLES)["prefreeze_tests"]
    ready_read, ready_write = os.pipe()
    go_read, go_write = os.pipe()
    attempt_read, attempt_write = os.pipe()
    winner_read, winner_write = os.pipe()
    result_read, result_write = os.pipe()
    real_flock = S.fcntl.flock
    waited_for_publication_lock = False

    def read_exact(descriptor: int, size: int) -> bytes:
        chunks: list[bytes] = []
        remaining = size
        while remaining:
            chunk = os.read(descriptor, remaining)
            if not chunk:
                raise AssertionError("publication barrier pipe closed early")
            chunks.append(chunk)
            remaining -= len(chunk)
        return b"".join(chunks)

    def synchronized_flock(descriptor: int, operation: int) -> None:
        nonlocal waited_for_publication_lock
        publication_lock = S.fcntl.LOCK_EX | S.fcntl.LOCK_NB
        if operation != publication_lock or waited_for_publication_lock:
            real_flock(descriptor, operation)
            return
        waited_for_publication_lock = True
        os.write(ready_write, b"R")
        assert os.read(go_read, 1) == b"G"
        try:
            real_flock(descriptor, operation)
        except BlockingIOError:
            os.write(attempt_write, b"F")
            raise
        os.write(attempt_write, b"W")
        assert os.read(winner_read, 1) == b"C"

    monkeypatch.setattr(S.fcntl, "flock", synchronized_flock)
    children: list[int] = []
    try:
        for _index in range(2):
            child = os.fork()
            if child == 0:
                os.close(ready_read)
                os.close(go_write)
                os.close(attempt_read)
                os.close(winner_write)
                os.close(result_read)
                try:
                    receipt = S.publish_v2_prefreeze_test_record(
                        candidate_value=os.fspath(candidate),
                        expected_sha256=expected,
                        authority_root_value=os.fspath(repository),
                    )
                    outcome = (
                        "OK|" + receipt["prefreeze_tests_sha256"] + "|"
                        + receipt["authority"] + "\n"
                    )
                except BaseException as error:
                    outcome = (
                        f"ERR|{type(error).__name__}|{error}\n"
                    )
                try:
                    os.write(result_write, outcome.encode("utf-8"))
                finally:
                    os._exit(0)
            children.append(child)

        os.close(ready_write)
        os.close(go_read)
        os.close(attempt_write)
        os.close(winner_read)
        os.close(result_write)
        assert read_exact(ready_read, 2) == b"RR"
        os.write(go_write, b"GG")
        attempts = read_exact(attempt_read, 2)
        assert sorted(attempts) == [ord("F"), ord("W")]
        os.write(winner_write, b"C")
        os.close(go_write)
        os.close(winner_write)

        chunks: list[bytes] = []
        while True:
            chunk = os.read(result_read, 4096)
            if not chunk:
                break
            chunks.append(chunk)
        outcomes = b"".join(chunks).decode("utf-8").splitlines()
        assert len(outcomes) == 2
        assert sum(row.startswith("OK|") for row in outcomes) == 1
        assert sum(row.startswith("ERR|PathContractError|") for row in outcomes) == 1
        failure = next(row for row in outcomes if row.startswith("ERR|"))
        assert "already locked" in failure
        success = next(row for row in outcomes if row.startswith("OK|"))
        assert success == (
            f"OK|{expected}|{S.PREFREEZE_TEST_PUBLICATION_AUTHORITY}"
        )
        for child in children:
            waited, status = os.waitpid(child, 0)
            assert waited == child and os.waitstatus_to_exitcode(status) == 0
        children.clear()

        info = canonical.stat()
        assert canonical.read_bytes() == candidate_raw
        assert stat.S_IMODE(info.st_mode) == 0o644
        assert info.st_nlink == 1
        assert candidate.read_bytes() == candidate_raw
        candidate_info = candidate.stat()
        assert stat.S_IMODE(candidate_info.st_mode) == 0o600
        assert candidate_info.st_nlink == 1
        assert not tuple(canonical.parent.glob(
            ".R401_VAL_L3_A1_V2_PREFREEZE_TESTS.json.publish-*"
        ))
    finally:
        for child in children:
            try:
                os.kill(child, 9)
            except ProcessLookupError:
                pass
            os.waitpid(child, 0)
        for descriptor in (
            ready_read, go_read, attempt_read, winner_read, result_read,
            ready_write, go_write, attempt_write, winner_write, result_write,
        ):
            try:
                os.close(descriptor)
            except OSError:
                pass
        if canonical.exists():
            canonical.unlink()
        if candidate.exists():
            candidate.unlink()
        if candidate.parent.exists():
            candidate.parent.rmdir()
    _exercise_role5_concurrent_exact_one(tmp_path, monkeypatch)


def test_role11_publication_accepts_candidate_above_machine_one_mib_cap(
    tmp_path: Path, monkeypatch,
) -> None:
    repository, candidate, _candidate_raw, _capture_commit = (
        _prepare_role11_publication(tmp_path, monkeypatch)
    )
    large_raw = b'{"padding":"' + b"a" * (1024 * 1024 + 17) + b'"}\n'
    assert 1024 * 1024 < len(large_raw) < S.V2_ROLE11_MAX_CANDIDATE_BYTES
    candidate.write_bytes(large_raw)
    candidate.chmod(0o600)
    expected = hashlib.sha256(large_raw).hexdigest()
    canonical = repository / dict(S.FORMAL_INPUT_ROLES)["prefreeze_tests"]
    try:
        receipt = S.publish_v2_prefreeze_test_record(
            candidate_value=os.fspath(candidate),
            expected_sha256=expected,
            authority_root_value=os.fspath(repository),
        )
        assert receipt["size_bytes"] == len(large_raw)
        assert canonical.read_bytes() == large_raw
        assert stat.S_IMODE(canonical.stat().st_mode) == 0o644
    finally:
        if canonical.exists():
            canonical.unlink()
        if candidate.exists():
            candidate.unlink()
        if candidate.parent.exists():
            candidate.parent.rmdir()


def test_private_candidate_first_inode_fstat_fault_recovers_and_cleans(
    monkeypatch,
) -> None:
    parent = Path(tempfile.mkdtemp(
        prefix="a416-v2-first-fstat-candidate-", dir="/tmp"
    ))
    os.chmod(parent, 0o700)
    candidate = parent / "candidate.json"
    real_fstat = S.os.fstat
    injected = False

    def first_regular_writer_fstat(descriptor: int):
        nonlocal injected
        info = real_fstat(descriptor)
        access = S.fcntl.fcntl(descriptor, S.fcntl.F_GETFL) & os.O_ACCMODE
        if stat.S_ISREG(info.st_mode) and access == os.O_WRONLY and not injected:
            injected = True
            raise OSError("synthetic first candidate fstat fault")
        return info

    monkeypatch.setattr(S.os, "fstat", first_regular_writer_fstat)
    try:
        with pytest.raises(OSError, match="synthetic first candidate fstat fault"):
            S._v2_write_private_candidate(
                candidate,
                b'{"candidate":"first-fstat"}\n',
                maximum_bytes=1024,
                context="first-fstat candidate",
            )
        assert injected is True
        assert tuple(parent.iterdir()) == ()
    finally:
        if candidate.exists():
            candidate.unlink()
        if parent.exists():
            parent.rmdir()


def test_role11_stage_first_inode_fstat_fault_recovers_and_cleans(
    tmp_path: Path, monkeypatch,
) -> None:
    repository, candidate, candidate_raw, _capture_commit = (
        _prepare_role11_publication(tmp_path, monkeypatch)
    )
    expected = hashlib.sha256(candidate_raw).hexdigest()
    canonical = repository / dict(S.FORMAL_INPUT_ROLES)["prefreeze_tests"]
    real_fstat = S.os.fstat
    injected = False

    def first_regular_rdwr_fstat(descriptor: int):
        nonlocal injected
        info = real_fstat(descriptor)
        access = S.fcntl.fcntl(descriptor, S.fcntl.F_GETFL) & os.O_ACCMODE
        if stat.S_ISREG(info.st_mode) and access == os.O_RDWR and not injected:
            injected = True
            raise OSError("synthetic first stage fstat fault")
        return info

    monkeypatch.setattr(S.os, "fstat", first_regular_rdwr_fstat)
    try:
        with pytest.raises(OSError, match="synthetic first stage fstat fault"):
            S.publish_v2_prefreeze_test_record(
                candidate_value=os.fspath(candidate),
                expected_sha256=expected,
                authority_root_value=os.fspath(repository),
            )
        assert injected is True
        assert not canonical.exists()
        assert not tuple(canonical.parent.glob(
            ".R401_VAL_L3_A1_V2_PREFREEZE_TESTS.json.publish-*"
        ))
    finally:
        if canonical.exists():
            canonical.unlink()
        if candidate.exists():
            candidate.unlink()
        if candidate.parent.exists():
            candidate.parent.rmdir()


def test_role11_publisher_posthook_inode_replacement_fails_without_rollback(
    tmp_path: Path, monkeypatch,
) -> None:
    repository, candidate, candidate_raw, _capture_commit = (
        _prepare_role11_publication(tmp_path, monkeypatch)
    )
    expected = hashlib.sha256(candidate_raw).hexdigest()
    canonical = repository / dict(S.FORMAL_INPUT_ROLES)["prefreeze_tests"]

    def replace_after_ultimate(boundary: str) -> None:
        if boundary != "AFTER_ULTIMATE_REPLAY":
            return
        canonical.unlink()
        canonical.write_bytes(candidate_raw)
        canonical.chmod(0o644)

    monkeypatch.setattr(
        S, "_v2_role11_publication_fault_hook", replace_after_ultimate
    )
    try:
        with pytest.raises(S.PathContractError, match="posthook canonical replay"):
            S.publish_v2_prefreeze_test_record(
                candidate_value=os.fspath(candidate),
                expected_sha256=expected,
                authority_root_value=os.fspath(repository),
            )
        assert canonical.read_bytes() == candidate_raw
        assert stat.S_IMODE(canonical.stat().st_mode) == 0o644
        assert not tuple(canonical.parent.glob(
            ".R401_VAL_L3_A1_V2_PREFREEZE_TESTS.json.publish-*"
        ))
    finally:
        if canonical.exists():
            canonical.unlink()
        if candidate.exists():
            candidate.unlink()
        if candidate.parent.exists():
            candidate.parent.rmdir()
    _exercise_role5_postrename_no_rollback(tmp_path, monkeypatch)


@pytest.mark.parametrize(
    ("attack", "error_pattern"),
    (
        ("stage_same_inode", "posthook prerename staged bytes/inode"),
        ("candidate_same_inode", "inode replay"),
        ("remote_drift", "posthook prerename remote replay"),
        ("ignored_downstream", "namespace appeared"),
    ),
)
def test_role11_before_rename_hook_replays_complete_envelope(
    tmp_path: Path,
    monkeypatch,
    attack: str,
    error_pattern: str,
) -> None:
    repository, candidate, candidate_raw, capture_commit = (
        _prepare_role11_publication(tmp_path, monkeypatch)
    )
    expected = hashlib.sha256(candidate_raw).hexdigest()
    canonical = repository / dict(S.FORMAL_INPUT_ROLES)["prefreeze_tests"]
    ignored_fixed = repository / dict(S.FORMAL_INPUT_ROLES)["prefreeze_review"]
    remote_drift = False
    base_remote = S._v2_role11_live_remote_probe

    if attack == "ignored_downstream":
        relative = ignored_fixed.relative_to(repository).as_posix()
        (repository / ".gitignore").write_text(relative + "\n", encoding="utf-8")
        _git(repository, "add", ".gitignore")
        _git(repository, "commit", "-m", "ignore fixed namespace for attack")

    def remote(root: Path) -> str:
        if remote_drift:
            return "f" * 40
        assert base_remote(root) == capture_commit
        return capture_commit

    def attack_before_rename(boundary: str) -> None:
        nonlocal remote_drift
        if boundary != "BEFORE_RENAME":
            return
        if attack == "stage_same_inode":
            stages = tuple(canonical.parent.glob(
                ".R401_VAL_L3_A1_V2_PREFREEZE_TESTS.json.publish-*"
            ))
            assert len(stages) == 1
            descriptor = os.open(stages[0], os.O_RDWR | getattr(os, "O_NOFOLLOW", 0))
            try:
                assert os.pwrite(descriptor, b"X", 0) == 1
                os.fsync(descriptor)
            finally:
                os.close(descriptor)
        elif attack == "candidate_same_inode":
            descriptor = os.open(candidate, os.O_RDWR | getattr(os, "O_NOFOLLOW", 0))
            try:
                assert os.pwrite(descriptor, b"X", 0) == 1
                os.fsync(descriptor)
            finally:
                os.close(descriptor)
        elif attack == "remote_drift":
            remote_drift = True
        else:
            ignored_fixed.write_text("ignored fixed attack\n", encoding="utf-8")

    monkeypatch.setattr(S, "_v2_role11_live_remote_probe", remote)
    monkeypatch.setattr(
        S, "_v2_role11_publication_fault_hook", attack_before_rename
    )
    try:
        with pytest.raises((S.PathContractError, S.ProductionAuthorityError), match=error_pattern):
            S.publish_v2_prefreeze_test_record(
                candidate_value=os.fspath(candidate),
                expected_sha256=expected,
                authority_root_value=os.fspath(repository),
            )
        assert not canonical.exists()
        assert not tuple(canonical.parent.glob(
            ".R401_VAL_L3_A1_V2_PREFREEZE_TESTS.json.publish-*"
        ))
    finally:
        if ignored_fixed.exists():
            ignored_fixed.unlink()
        if canonical.exists():
            canonical.unlink()
        if candidate.exists():
            candidate.unlink()
        if candidate.parent.exists():
            candidate.parent.rmdir()


def test_role11_publisher_rejects_untracked_inserted_by_last_input_replay(
    tmp_path: Path, monkeypatch,
) -> None:
    repository, candidate, candidate_raw, _capture_commit = (
        _prepare_role11_publication(tmp_path, monkeypatch)
    )
    expected = hashlib.sha256(candidate_raw).hexdigest()
    canonical = repository / dict(S.FORMAL_INPUT_ROLES)["prefreeze_tests"]
    foreign = repository / "late-foreign.txt"
    base_capture = S._v2_role11_capture_inputs
    capture_calls = 0

    def inject_on_final_capture(root: Path):
        nonlocal capture_calls
        result = base_capture(root)
        capture_calls += 1
        if capture_calls == 4:
            foreign.write_text("late foreign\n", encoding="utf-8")
        return result

    monkeypatch.setattr(S, "_v2_role11_capture_inputs", inject_on_final_capture)
    try:
        with pytest.raises(
            S.ProductionAuthorityError, match="one owned leaf"
        ):
            S.publish_v2_prefreeze_test_record(
                candidate_value=os.fspath(candidate),
                expected_sha256=expected,
                authority_root_value=os.fspath(repository),
            )
        assert capture_calls == 4
        assert canonical.read_bytes() == candidate_raw
        assert foreign.read_text(encoding="utf-8") == "late foreign\n"
        assert not tuple(canonical.parent.glob(
            ".R401_VAL_L3_A1_V2_PREFREEZE_TESTS.json.publish-*"
        ))
    finally:
        if foreign.exists():
            foreign.unlink()
        if canonical.exists():
            canonical.unlink()
        if candidate.exists():
            candidate.unlink()
        if candidate.parent.exists():
            candidate.parent.rmdir()
    _exercise_role5_prehook_attacks(tmp_path, monkeypatch)


def test_role11_publisher_cleanup_attempts_all_fds_and_chains_primary_error(
    tmp_path: Path, monkeypatch,
) -> None:
    repository, candidate, candidate_raw, _capture_commit = (
        _prepare_role11_publication(tmp_path, monkeypatch)
    )
    expected = hashlib.sha256(candidate_raw).hexdigest()
    canonical = repository / dict(S.FORMAL_INPUT_ROLES)["prefreeze_tests"]
    stage_identity: tuple[int, int] | None = None
    close_failed = False
    unlock_attempted = False
    directory_closes_after_failure: list[tuple[int, int]] = []
    real_close = S.os.close
    real_flock = S.fcntl.flock

    def fail_before_rename(boundary: str) -> None:
        nonlocal stage_identity
        if boundary == "AFTER_STAGE_DURABLE":
            stages = tuple(canonical.parent.glob(
                ".R401_VAL_L3_A1_V2_PREFREEZE_TESTS.json.publish-*"
            ))
            assert len(stages) == 1
            info = stages[0].stat()
            stage_identity = (info.st_dev, info.st_ino)
        elif boundary == "BEFORE_RENAME":
            raise RuntimeError("synthetic primary publication failure")

    def close_with_one_stage_failure(descriptor: int) -> None:
        nonlocal close_failed
        info = os.fstat(descriptor)
        access_mode = S.fcntl.fcntl(descriptor, S.fcntl.F_GETFL) & os.O_ACCMODE
        if (
            stage_identity is not None
            and (info.st_dev, info.st_ino) == stage_identity
            and access_mode == os.O_RDWR
            and not close_failed
        ):
            real_close(descriptor)
            close_failed = True
            raise OSError("synthetic stage descriptor close failure")
        if close_failed and stat.S_ISDIR(info.st_mode):
            directory_closes_after_failure.append((info.st_dev, info.st_ino))
        real_close(descriptor)

    def unlock_with_failure(descriptor: int, operation: int) -> None:
        nonlocal unlock_attempted
        if operation == S.fcntl.LOCK_UN:
            unlock_attempted = True
            real_flock(descriptor, operation)
            raise OSError("synthetic unlock failure")
        real_flock(descriptor, operation)

    monkeypatch.setattr(S, "_v2_role11_publication_fault_hook", fail_before_rename)
    monkeypatch.setattr(S.os, "close", close_with_one_stage_failure)
    monkeypatch.setattr(S.fcntl, "flock", unlock_with_failure)
    try:
        with pytest.raises(
            OSError, match="synthetic stage descriptor close failure"
        ) as caught:
            S.publish_v2_prefreeze_test_record(
                candidate_value=os.fspath(candidate),
                expected_sha256=expected,
                authority_root_value=os.fspath(repository),
            )
        assert isinstance(caught.value.__cause__, RuntimeError)
        assert "synthetic primary publication failure" in str(caught.value.__cause__)
        assert close_failed is True
        assert unlock_attempted is True
        assert len(directory_closes_after_failure) >= 2
        assert not canonical.exists()
        assert not tuple(canonical.parent.glob(
            ".R401_VAL_L3_A1_V2_PREFREEZE_TESTS.json.publish-*"
        ))
    finally:
        if canonical.exists():
            canonical.unlink()
        if candidate.exists():
            candidate.unlink()
        if candidate.parent.exists():
            candidate.parent.rmdir()


@pytest.mark.parametrize(
    ("attack", "error_pattern"),
    (
        ("untracked", "worktree is not exactly clean"),
        ("remote", "final capture repository probe mismatch"),
    ),
)
def test_role11_capture_final_probe_rejects_late_repository_drift(
    tmp_path: Path, monkeypatch, attack: str, error_pattern: str,
) -> None:
    repository, candidate, foreign = _prepare_role11_capture_terminal_attack(
        tmp_path, monkeypatch, attack=attack
    )
    try:
        with pytest.raises(S.ProductionAuthorityError, match=error_pattern):
            S.capture_v2_prefreeze_test_candidate(
                os.fspath(candidate), repository
            )
        assert not candidate.exists()
        if attack == "untracked":
            assert foreign.read_text(encoding="utf-8") == "late capture foreign\n"
        else:
            assert not foreign.exists()
    finally:
        if foreign.exists():
            foreign.unlink()
        if candidate.exists():
            candidate.unlink()
        if candidate.parent.exists():
            candidate.parent.rmdir()


def test_pure_git_commit_header_grammar_is_closed(monkeypatch) -> None:
    tree = b"a" * 40
    parent = b"b" * 40
    author = b"author V2 Test <test@example.invalid> 1 +0000"
    committer = b"committer V2 Test <test@example.invalid> 1 +0000"
    valid = b"\n".join((b"tree " + tree, b"parent " + parent, author, committer))
    valid += b"\n\nmessage\n"
    payload = valid
    monkeypatch.setattr(S, "_v2_git_read_object", lambda *_args: ("commit", payload))
    assert S._v2_git_commit_metadata(Path("/tmp"), "c" * 40) == (
        tree.decode("ascii"),
        (parent.decode("ascii"),),
    )

    malformed = (
        valid.replace(b"tree " + tree + b"\n", b"tree " + tree + b"\ntree " + tree + b"\n", 1),
        valid.replace(author + b"\n", author + b"\nauthor Other <o@x> 1 +0000\n", 1),
        valid.replace(committer + b"\n\n", committer + b"\nencoding UTF-8\n\n", 1),
        valid.replace(author, b" author continuation"),
        valid.replace(b"+0000", b"+1460", 1),
        valid.replace(b"parent " + parent + b"\n", b"parent " + parent + b"\nparent " + parent + b"\n", 1),
        valid.replace(committer + b"\n\n", b"\n", 1),
        valid.replace(b"tree " + tree, b"tree " + tree.upper(), 1),
        valid.replace(b"\nparent", b"\r\nparent", 1),
    )
    for forged in malformed:
        payload = forged
        with pytest.raises(S.ProductionAuthorityError):
            S._v2_git_commit_metadata(Path("/tmp"), "c" * 40)


def test_pure_git_history_rejects_merge_introduction_but_allows_other_merges(
    monkeypatch,
) -> None:
    raw = b"x"
    binding = {
        "path": "control.json",
        "sha256": hashlib.sha256(raw).hexdigest(),
        "size_bytes": 1,
        "mode": "0644",
    }
    monkeypatch.setattr(
        S,
        "_v2_git_optional_commit_blob",
        lambda *_args, **_kwargs: (0o100644, raw, "d" * 40),
    )
    monkeypatch.setattr(
        S,
        "_v2_git_commit_metadata",
        lambda *_args, **_kwargs: ("e" * 40, ("1" * 40, "2" * 40)),
    )
    with pytest.raises(S.ProductionAuthorityError, match="ordinary single-parent"):
        S._v2_git_validate_continuous_introduction(
            Path("/tmp"),
            capture_commit="4" * 40,
            introduction_commit="4" * 40,
            binding=binding,
            context="synthetic merge history",
        )

    capture = "3" * 40
    introduction = "4" * 40
    older_merge = "5" * 40
    root = "6" * 40
    metadata = {
        capture: ("a" * 40, (introduction, "2" * 40)),
        introduction: ("b" * 40, (older_merge,)),
        older_merge: ("c" * 40, (root, "7" * 40)),
        root: ("d" * 40, ()),
    }
    monkeypatch.setattr(
        S,
        "_v2_git_commit_metadata",
        lambda _root, oid: metadata[oid],
    )
    monkeypatch.setattr(
        S,
        "_v2_git_optional_commit_blob",
        lambda _root, oid, _path: (
            (0o100644, raw, "d" * 40)
            if oid in {capture, introduction}
            else None
        ),
    )
    S._v2_git_validate_continuous_introduction(
        Path("/tmp"),
        capture_commit=capture,
        introduction_commit=introduction,
        binding=binding,
        context="synthetic nonintroduction merge history",
    )


def test_repository_probe_uses_isolated_git_config_and_rejects_rewrites(
    tmp_path: Path, monkeypatch,
) -> None:
    repository = tmp_path / "config-authority"
    repository.mkdir()
    _git(repository, "init", "-b", "main")
    _git(repository, "config", "user.email", "test@example.invalid")
    _git(repository, "config", "user.name", "V2 Test")
    _git(repository, "remote", "add", "origin", S.V2_ROLE11_ORIGIN_URL)
    ignored_fixed_relative = dict(S.FORMAL_INPUT_ROLES)["prefreeze_review"]
    (repository / ".gitignore").write_text(
        "ordinary-cache/\n" + ignored_fixed_relative + "\n",
        encoding="utf-8",
    )
    (repository / "baseline.txt").write_text("baseline\n", encoding="utf-8")
    _git(repository, "add", ".gitignore", "baseline.txt")
    _git(repository, "commit", "-m", "baseline")
    capture_commit = _git(repository, "rev-parse", "HEAD")
    monkeypatch.setattr(
        S, "_v2_role11_live_remote_probe", lambda _root: capture_commit
    )

    assert S.V2_ROLE11_ENVIRONMENT["GIT_CONFIG_NOSYSTEM"] == "1"
    assert S.V2_ROLE11_ENVIRONMENT["GIT_CONFIG_GLOBAL"] == "/dev/null"
    assert len(S.V2_ROLE11_ENVIRONMENT) == 14
    assert S._v2_git_origin_url(repository) == S.V2_ROLE11_ORIGIN_URL

    ordinary = repository / "ordinary-cache/ignored.bin"
    ordinary.parent.mkdir()
    ordinary.write_bytes(b"ignored ordinary cache\n")
    assert S._v2_role11_status_probe(repository) == b""
    assert S._v2_role11_repository_probes(repository) == capture_commit

    fixed = repository / ignored_fixed_relative
    fixed.parent.mkdir(parents=True)
    fixed.write_bytes(b"ignored but fixed namespace\n")
    assert S._v2_role11_status_probe(repository) == b""
    with pytest.raises(S.ProductionAuthorityError, match="already exists"):
        S._v2_absence_snapshot((fixed,), "ignored fixed namespace")

    config = repository / ".git/config"
    baseline_config = config.read_text(encoding="utf-8")
    attacks = (
        '\n[include]\n\tpath = /tmp/evil-config\n',
        '\n[includeIf "gitdir:/tmp/"]\n\tpath = /tmp/evil-config\n',
        '\n[url "ssh://evil.invalid/"]\n\tinsteadOf = git@github.com:\n',
        '\n[url "ssh://evil.invalid/"]\n\tpushInsteadOf = git@github.com:\n',
        '\n[remote "origin"]\n\turl = ' + S.V2_ROLE11_ORIGIN_URL + '\n',
    )
    for addition in attacks:
        config.write_text(baseline_config + addition, encoding="utf-8")
        with pytest.raises(S.ProductionAuthorityError):
            S._v2_git_origin_url(repository)


def test_every_production_entry_remains_a_hard_stop(monkeypatch, capsys) -> None:
    candidate = "/tmp/a416-v2-role5-review." + "1" * 32 + "/" + (
        S.V2_ROLE5_CANDIDATE_BASENAME
    )
    verify_receipt = "/tmp/a416-v2-role5-verify." + "2" * 32 + "/" + (
        S.V2_ROLE5_VERIFY_RECEIPT_BASENAME
    )
    expected = "3" * 64
    commit = "4" * 40
    raw_root = "/tmp/raw-role5-authority"
    publication_receipt = {
        "schema_version": 1,
        "protocol_id": S.PROTOCOL_ID,
        "artifact_role": "DESIGN_REVIEW_AND_WITHDRAWAL_PUBLICATION_RECEIPT",
        "artifact_status": "PUBLISHED_WRITE_ONCE_NON_LICENSING",
        "authority": S.V2_ROLE5_PUBLICATION_AUTHORITY,
        "candidate_path": candidate,
        "canonical_path": raw_root + "/research/role5.json",
        "design_review_sha256": expected,
        "reviewed_commit": commit,
        "size_bytes": 1,
        "mode": "0644",
        "nlink": 1,
        "serializer": "CJ_COMPACT_V1",
        "publication_method": S.V2_ROLE5_PUBLICATION_METHOD,
        "verify_receipt_sha256": "5" * 64,
        "input_map_sha256": "6" * 64,
        "independent_verification_receipt_validated": True,
        "scientific_licensing_enabled": False,
        "production_authorized": False,
        "scientific_dispatch_performed": False,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    calls: list[tuple[str, ...]] = []

    def fake_publish(*argv: str) -> dict:
        calls.append(argv)
        return publication_receipt

    monkeypatch.setattr(S, "publish_v2_role5", fake_publish)
    required = [
        "--candidate", candidate,
        "--role24-receipt", verify_receipt,
        "--expected-sha256", expected,
        "--expected-reviewed-commit", commit,
        "--publication-authority", S.V2_ROLE5_PUBLICATION_AUTHORITY,
        "--authority-root", raw_root,
    ]
    assert S.main(["--publish-role5", *required]) == 0
    captured = capsys.readouterr()
    assert captured.err == ""
    assert captured.out.encode("utf-8") == S.canonical_json_bytes(
        publication_receipt
    )
    assert calls == [(
        candidate,
        verify_receipt,
        expected,
        commit,
        S.V2_ROLE5_PUBLICATION_AUTHORITY,
        raw_root,
    )]
    for extra in (
        ("--output", "/tmp/other"),
        ("--mock-only",),
        ("--publish-machine-freeze",),
    ):
        assert S.main(["--publish-role5", *required, *extra]) == 1
        assert "exact-exclusive" in capsys.readouterr().err
        assert len(calls) == 1
    for missing_index in range(0, len(required), 2):
        incomplete = required[:missing_index] + required[missing_index + 2:]
        assert S.main(["--publish-role5", *incomplete]) == 1
        assert "requires exactly" in capsys.readouterr().err
        assert len(calls) == 1
    assert S.main(["--role24-receipt", verify_receipt]) == 1
    assert "require --publish-role5" in capsys.readouterr().err

    def forbidden(*_args, **_kwargs):
        raise AssertionError("scientific evaluator was dispatched")

    monkeypatch.setattr(S.subprocess, "Popen", forbidden)
    assert S.main([
        "--production", "--execute-scientific-dispatch", "--resume"
    ]) == 1
    assert "unconditionally disabled" in capsys.readouterr().err
