from __future__ import annotations

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
SOURCE = ROOT / "scripts/run_r401_val_l3_a1_v2_all_slabs.py"


def load_scheduler():
    name = "r401_val_l3_a1_v2_scheduler_static_tests"
    specification = importlib.util.spec_from_file_location(name, SOURCE)
    assert specification is not None and specification.loader is not None
    module = importlib.util.module_from_spec(specification)
    sys.modules[name] = module
    specification.loader.exec_module(module)
    return module


S = load_scheduler()


@pytest.fixture()
def private_parent():
    parent = Path(tempfile.mkdtemp(prefix="a416-v2-role19-test-", dir="/tmp"))
    os.chmod(parent, 0o700)
    try:
        yield parent
    finally:
        for entry in tuple(parent.iterdir()):
            if entry.is_dir() and not entry.is_symlink():
                entry.rmdir()
            else:
                entry.unlink()
        parent.rmdir()


def _git(repo: Path, *argv: str) -> str:
    completed = subprocess.run(
        ("/usr/bin/git", "-C", os.fspath(repo), *argv),
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return completed.stdout.strip()


def _commit_all(repo: Path, message: str) -> str:
    _git(repo, "add", "--all")
    _git(repo, "commit", "-m", message)
    return _git(repo, "rev-parse", "HEAD")


def _binding(path: Path, relative: str) -> dict[str, object]:
    raw = path.read_bytes()
    info = path.stat()
    return {
        "path": relative,
        "sha256": hashlib.sha256(raw).hexdigest(),
        "size_bytes": len(raw),
        "mode": f"{stat.S_IMODE(info.st_mode):04o}",
    }


def _synthetic_formal_snapshot(
    authority_root: Path, *, component: str = "STATIC"
):
    raw = b"synthetic evaluator bytes\n"
    role = (
        "static_evaluator"
        if component == "STATIC"
        else "branch_evaluator_source"
    )
    record = S.FormalRoleRecord(
        role=role,
        path=f"synthetic/{role}.bin",
        sha256=hashlib.sha256(raw).hexdigest(),
        raw=raw,
        stat_identity=(1, 2, len(raw), 3, 4),
    )
    records = [record]
    if component == "BRANCH":
        binary_raw = b"synthetic binary bytes\n"
        records.append(
            S.FormalRoleRecord(
                role="branch_evaluator_binary",
                path="synthetic/branch_evaluator_binary",
                sha256=hashlib.sha256(binary_raw).hexdigest(),
                raw=binary_raw,
                stat_identity=(1, 5, len(binary_raw), 6, 7),
            )
        )
    return S.FormalAuthoritySnapshot(
        authority_root=authority_root,
        main_freeze_path=authority_root / "synthetic-main.json",
        main_freeze_sha256="a" * 64,
        machine_freeze_path=authority_root / "synthetic-machine.json",
        machine_freeze_sha256="b" * 64,
        prefreeze_review_path=authority_root / "synthetic-review.md",
        prefreeze_review_sha256="c" * 64,
        input_roles=tuple(records),
        main_freeze_raw=b"{}\n",
        main_freeze_stat_identity=(1, 8, 3, 9, 10),
        machine_freeze_raw=b"{}\n",
    )


def _synthetic_component_entries(component: str) -> list[dict[str, object]]:
    prefix = component.lower()
    certified = f"{component}_CELL_CERTIFIED"
    return [
        {
            "cell": cell.payload(),
            "path": (
                f"{prefix}/cell_manifests/"
                f"{cell.precision_bits}/{cell.slab_id}.json"
            ),
            "sha256": hashlib.sha256(cell.label.encode("ascii")).hexdigest(),
            "size_bytes": 1,
            "evaluator_status": certified,
            "scheduler_classification": "COMMITTED_EVALUATOR_RESULT",
        }
        for cell in S.exact_matrix()
    ]


def test_exact_v2_role_map_is_ordered_closed_53() -> None:
    assert len(S.FORMAL_INPUT_ROLES) == 53
    assert len(dict(S.FORMAL_INPUT_ROLES)) == 53
    assert len({path for _role, path in S.FORMAL_INPUT_ROLES}) == 53
    roles = dict(S.FORMAL_INPUT_ROLES)
    assert tuple(role for role, _path in S.FORMAL_INPUT_ROLES[:3]) == (
        "a416_derivation",
        "s0_protocol",
        "s0_report",
    )
    assert roles["implementation_design_review"].endswith(
        "R401_VAL_L3_A1_V2_DESIGN_REVIEW_AND_WITHDRAWAL.json"
    )
    assert roles["machine_freeze"].endswith(
        "R401_VAL_L3_A1_V2_MACHINE_FREEZE.json"
    )
    assert roles["prefreeze_tests"].endswith(
        "R401_VAL_L3_A1_V2_PREFREEZE_TESTS.json"
    )
    assert roles["prefreeze_review"].endswith(
        "R401_VAL_L3_A1_V2_PREFREEZE_REVIEW.md"
    )
    assert roles["s0_compatibility"].endswith(
        "R401_VAL_L3_A1_V2_S0_COMPATIBILITY_REPLAY.json"
    )
    assert tuple(role for role, _path in S.FORMAL_INPUT_ROLES[18:24]) == (
        "scheduler",
        "static_checker_source",
        "branch_checker_source",
        "composite_checker_source",
        "s0_adapter",
        "release_builder",
    )


def test_role11_mechanical_lock_fails_before_any_capture(monkeypatch) -> None:
    monkeypatch.setattr(S, "V2_ROLE11_FINAL_COMMAND_LOCKED", False)
    monkeypatch.setattr(S, "V2_ROLE11_EXPECTED_TEST_PASSED", None)
    monkeypatch.setattr(
        S,
        "_v2_private_candidate_path",
        lambda *_args, **_kwargs: (_ for _ in ()).throw(
            AssertionError("capture performed I/O before mechanical lock")
        ),
    )
    with pytest.raises(S.ProductionAuthorityError, match="mechanical lock"):
        S.capture_v2_prefreeze_test_candidate(
            "/tmp/a416-v2-never/candidate.json", ROOT
        )


def test_private_candidate_is_0600_nlink1_and_full_replay(private_parent: Path) -> None:
    path = private_parent / "candidate.json"
    image = S._v2_write_private_candidate(
        path, b'{"ok":true}\n', maximum_bytes=1024, context="test candidate"
    )
    info = path.stat()
    assert stat.S_IMODE(info.st_mode) == 0o600
    assert info.st_nlink == 1
    assert image.parent_nlink == 2
    S._v2_replay_private_candidate(path, image, context="test replay")


def test_private_candidate_rejects_same_inode_timestamp_drift(
    private_parent: Path,
) -> None:
    path = private_parent / "candidate.json"
    image = S._v2_write_private_candidate(
        path, b'{"ok":true}\n', maximum_bytes=1024, context="test candidate"
    )
    info = path.stat()
    os.utime(path, ns=(info.st_atime_ns, info.st_mtime_ns + 1_000_000))
    with pytest.raises(S.PathContractError, match="inode replay"):
        S._v2_replay_private_candidate(path, image, context="drift replay")
    S._v2_remove_owned_candidate(path, image)
    assert tuple(private_parent.iterdir()) == ()


def test_private_candidate_writer_cleans_its_inode_on_write_error(
    private_parent: Path, monkeypatch
) -> None:
    path = private_parent / "candidate.json"
    original_write = S.os.write
    calls = 0

    def fail_first_write(descriptor: int, raw: bytes) -> int:
        nonlocal calls
        calls += 1
        if calls == 1:
            raise OSError("synthetic write failure")
        return original_write(descriptor, raw)

    monkeypatch.setattr(S.os, "write", fail_first_write)
    with pytest.raises(OSError, match="synthetic write failure"):
        S._v2_write_private_candidate(
            path, b"candidate\n", maximum_bytes=1024, context="failing writer"
        )
    assert tuple(private_parent.iterdir()) == ()


def test_private_candidate_no_replace_and_parent_nlink_gate(
    private_parent: Path,
) -> None:
    path = private_parent / "candidate.json"
    path.write_bytes(b"existing")
    path.chmod(0o600)
    with pytest.raises(S.PathContractError, match="already exists"):
        S._v2_write_private_candidate(
            path, b"replacement", maximum_bytes=1024, context="no replace"
        )
    path.unlink()
    (private_parent / "nested").mkdir()
    with pytest.raises(S.PathContractError, match="nlink-2"):
        S._v2_private_candidate_path(os.fspath(path), "parent gate")


def test_pure_git_continuous_introduction_and_no_subprocess_fallback(
    tmp_path: Path, monkeypatch
) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    _git(repo, "init", "-b", "main")
    _git(repo, "config", "user.email", "test@example.invalid")
    _git(repo, "config", "user.name", "V2 Test")
    (repo / "root.txt").write_text("root\n", encoding="utf-8")
    _commit_all(repo, "root")
    artifact = repo / "control.json"
    artifact.write_bytes(b'{"generation":"v2"}\n')
    introduction = _commit_all(repo, "introduce")
    (repo / "later.txt").write_text("later\n", encoding="utf-8")
    capture = _commit_all(repo, "later")
    binding = _binding(artifact, "control.json")

    def forbidden(*_args, **_kwargs):
        raise AssertionError("pure Git verifier invoked a child process")

    monkeypatch.setattr(S.subprocess, "run", forbidden)
    monkeypatch.setattr(S.subprocess, "Popen", forbidden)
    S._v2_git_validate_continuous_introduction(
        repo,
        capture_commit=capture,
        introduction_commit=introduction,
        binding=binding,
        context="synthetic introduction",
    )
    assert S._v2_git_find_continuous_introduction(
        repo,
        capture_commit=capture,
        binding=binding,
        context="synthetic discovery",
    ) == introduction
    with pytest.raises(S.ProductionAuthorityError):
        S._v2_git_validate_continuous_introduction(
            repo,
            capture_commit=capture,
            introduction_commit=capture,
            binding=binding,
            context="later-containing commit",
        )


def test_pure_git_rejects_delete_then_readd_history(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    _git(repo, "init", "-b", "main")
    _git(repo, "config", "user.email", "test@example.invalid")
    _git(repo, "config", "user.name", "V2 Test")
    (repo / "root.txt").write_text("root\n", encoding="utf-8")
    _commit_all(repo, "root")
    artifact = repo / "control.json"
    artifact.write_bytes(b'{"generation":"v2"}\n')
    _commit_all(repo, "first introduction")
    artifact.unlink()
    _commit_all(repo, "delete")
    artifact.write_bytes(b'{"generation":"v2"}\n')
    readd = _commit_all(repo, "readd")
    binding = _binding(artifact, "control.json")
    with pytest.raises(S.ProductionAuthorityError, match="before its claimed"):
        S._v2_git_validate_continuous_introduction(
            repo,
            capture_commit=readd,
            introduction_commit=readd,
            binding=binding,
            context="delete/readd",
        )
    with pytest.raises(S.ProductionAuthorityError, match="before its claimed"):
        S._v2_git_find_continuous_introduction(
            repo,
            capture_commit=readd,
            binding=binding,
            context="delete/readd discovery",
        )


def test_pure_git_first_parent_continuity_allows_nonintroduction_merges(
    tmp_path: Path,
) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    _git(repo, "init", "-b", "main")
    _git(repo, "config", "user.email", "test@example.invalid")
    _git(repo, "config", "user.name", "V2 Test")
    (repo / "root.txt").write_text("root\n", encoding="utf-8")
    _commit_all(repo, "root")
    _git(repo, "checkout", "-b", "pre-side")
    (repo / "pre-side.txt").write_text("side\n", encoding="utf-8")
    _commit_all(repo, "pre side")
    _git(repo, "checkout", "main")
    (repo / "pre-main.txt").write_text("main\n", encoding="utf-8")
    _commit_all(repo, "pre main")
    _git(repo, "merge", "--no-ff", "pre-side", "-m", "pre merge")
    artifact = repo / "control.json"
    artifact.write_bytes(b'{"generation":"v2"}\n')
    introduction = _commit_all(repo, "ordinary introduction")
    _git(repo, "checkout", "-b", "post-side")
    (repo / "post-side.txt").write_text("side\n", encoding="utf-8")
    _commit_all(repo, "post side")
    _git(repo, "checkout", "main")
    (repo / "post-main.txt").write_text("main\n", encoding="utf-8")
    _commit_all(repo, "post main")
    _git(repo, "merge", "--no-ff", "post-side", "-m", "post merge")
    capture = _git(repo, "rev-parse", "HEAD")
    binding = _binding(artifact, "control.json")
    S._v2_git_validate_continuous_introduction(
        repo,
        capture_commit=capture,
        introduction_commit=introduction,
        binding=binding,
        context="first-parent merges",
    )
    assert S._v2_git_find_continuous_introduction(
        repo,
        capture_commit=capture,
        binding=binding,
        context="first-parent merge discovery",
    ) == introduction


def test_git_snapshot_fifo_swap_is_nonblocking(
    private_parent: Path, monkeypatch
) -> None:
    path = private_parent / "object"
    path.write_bytes(b"safe")
    original_stat = S.os.stat
    swapped = False

    def racing_stat(value, *args, **kwargs):
        nonlocal swapped
        result = original_stat(value, *args, **kwargs)
        if value == path.name and kwargs.get("dir_fd") is not None and not swapped:
            swapped = True
            S.os.unlink(path.name, dir_fd=kwargs["dir_fd"])
            S.os.mkfifo(path.name, 0o600, dir_fd=kwargs["dir_fd"])
        return result

    monkeypatch.setattr(S.os, "stat", racing_stat)
    with pytest.raises(S.ProductionAuthorityError, match="path/inode race"):
        S._v2_git_snapshot(path, 1024)


def test_git_snapshot_growth_is_bounded(private_parent: Path, monkeypatch) -> None:
    path = private_parent / "object"
    path.write_bytes(b"small")
    original_pread = S.os.pread
    grown = False

    def racing_pread(descriptor: int, count: int, offset: int) -> bytes:
        nonlocal grown
        if not grown:
            grown = True
            with path.open("ab") as stream:
                stream.write(b"x" * 64)
        return original_pread(descriptor, count, offset)

    monkeypatch.setattr(S.os, "pread", racing_pread)
    with pytest.raises(S.ProductionAuthorityError, match="grew beyond read cap"):
        S._v2_git_snapshot(path, 16)


@pytest.mark.parametrize(
    "transcript",
    (
        "FAILED forged\n3 passed in 1.00s\n",
        "ERROR collecting\n3 passed in 1.00s\n",
        "3 passed, 1 warning in 1.00s\n",
        "3 passed in 1.00s\n3 passed in 1.00s\n",
        "3 passed in 59.99s (0:02:00)\n",
        "100000 passed in 1.00s\n",
        "3 passed in 600.01s (0:10:00)\n",
    ),
)
def test_pytest_receipt_rejects_hidden_or_inconsistent_tokens(
    transcript: str,
) -> None:
    with pytest.raises(S.ProductionAuthorityError):
        S._v2_role11_pytest_counts(transcript, "attack transcript")


def test_capture_command_stream_cap_and_subreaper_restore() -> None:
    before = S._capture_child_subreaper_state()
    with pytest.raises(S.ProductionAuthorityError, match="stdout cap exceeded"):
        S._capture_command(
            (
                sys.executable,
                "-c",
                "import os; os.write(1, b'x' * (1024 * 1024 + 1))",
            ),
            cwd=ROOT,
            environment=dict(os.environ),
            timeout_seconds=10,
        )
    assert S._capture_child_subreaper_state() is before


def test_capture_command_kills_descendant_pipe_holder() -> None:
    before = S._capture_child_subreaper_state()
    with pytest.raises(
        S.ProductionAuthorityError, match="descendants retained output pipes"
    ):
        S._capture_command(
            (
                sys.executable,
                "-c",
                "import os,time; p=os.fork(); "
                "os._exit(0) if p else time.sleep(30)",
            ),
            cwd=ROOT,
            environment=dict(os.environ),
            timeout_seconds=10,
        )
    assert S._capture_child_subreaper_state() is before


def test_formal_scientific_dispatch_is_unconditionally_stopped() -> None:
    class ValidPlan:
        def validate(self) -> None:
            return None

    def forbidden_runner(*_args, **_kwargs):
        raise AssertionError("scientific transaction runner was invoked")

    with pytest.raises(S.ProductionAuthorityError, match="unconditionally disabled"):
        S.dispatch_formal_branch_transaction(
            ValidPlan(), transaction_runner=forbidden_runner
        )


def test_formal_role55_staged_directory_publication_is_write_once(
    tmp_path: Path, private_parent: Path, monkeypatch
) -> None:
    authority = tmp_path / "authority"
    (authority / "results").mkdir(parents=True)
    snapshot = _synthetic_formal_snapshot(authority)
    binding = {
        "schema_version": 1,
        "artifact_role": "SYNTHETIC_ROLE55_NON_SCIENTIFIC",
        "scientific_licensing_enabled": False,
    }
    monkeypatch.setattr(S, "revalidate_formal_snapshot", lambda *_a, **_k: None)
    monkeypatch.setattr(
        S, "build_formal_canonical_run_binding", lambda _snapshot: binding
    )
    monkeypatch.setattr(
        S, "validate_formal_canonical_run_binding", lambda value, *_a: value
    )
    candidate = private_parent / "run_config.json"
    captured, digest = S.build_formal_run_config_candidate(
        snapshot, os.fspath(candidate)
    )
    assert captured == binding
    candidate_before = candidate.read_bytes()
    receipt = S.publish_formal_run_config(
        snapshot,
        os.fspath(candidate),
        digest,
        publication_authority=S.FORMAL_RUN_CONFIG_PUBLICATION_AUTHORITY,
    )
    result = authority / "results/r401_val_l3_a1_v2_all_slabs"
    assert tuple(path.name for path in result.iterdir()) == ("run_config.json",)
    assert (result / "run_config.json").read_bytes() == candidate_before
    assert stat.S_IMODE((result / "run_config.json").stat().st_mode) == 0o644
    assert candidate.read_bytes() == candidate_before
    assert receipt["scientific_dispatch_performed"] is False
    with pytest.raises((S.RunBindingMismatch, S.CorruptGeneration)):
        S.publish_formal_run_config(
            snapshot,
            os.fspath(candidate),
            digest,
            publication_authority=S.FORMAL_RUN_CONFIG_PUBLICATION_AUTHORITY,
        )


@pytest.mark.parametrize("phase", ("BEFORE_RENAME", "AFTER_RENAME"))
def test_formal_role55_hook_directory_swap_is_rejected_without_rollback(
    tmp_path: Path, private_parent: Path, monkeypatch, phase: str
) -> None:
    authority = tmp_path / "authority"
    results_parent = authority / "results"
    results_parent.mkdir(parents=True)
    snapshot = _synthetic_formal_snapshot(authority)
    binding = {
        "schema_version": 1,
        "artifact_role": "SYNTHETIC_ROLE55_NON_SCIENTIFIC",
        "scientific_licensing_enabled": False,
    }
    monkeypatch.setattr(S, "revalidate_formal_snapshot", lambda *_a, **_k: None)
    monkeypatch.setattr(
        S, "build_formal_canonical_run_binding", lambda _snapshot: binding
    )
    monkeypatch.setattr(
        S, "validate_formal_canonical_run_binding", lambda value, *_a: value
    )
    candidate = private_parent / "run_config.json"
    _, digest = S.build_formal_run_config_candidate(
        snapshot, os.fspath(candidate)
    )
    raw = candidate.read_bytes()

    def hook(observed: str) -> None:
        if observed != phase:
            return
        result = results_parent / "r401_val_l3_a1_v2_all_slabs"
        if phase == "BEFORE_RENAME":
            stage = next(
                path
                for path in results_parent.iterdir()
                if path.name.startswith(
                    ".r401_val_l3_a1_v2_all_slabs.role55-publish-"
                )
            )
            displaced = results_parent / ".attacker-displaced-stage"
            stage.rename(displaced)
            stage.mkdir(mode=0o755)
            replacement = stage / "run_config.json"
        else:
            displaced = results_parent / ".attacker-displaced-result"
            result.rename(displaced)
            result.mkdir(mode=0o755)
            replacement = result / "run_config.json"
        replacement.write_bytes(raw)
        replacement.chmod(0o644)

    monkeypatch.setattr(S, "_formal_run_publication_fault_hook", hook)
    with pytest.raises(
        S.PathContractError, match="identity mismatch|incomplete cleanup"
    ):
        S.publish_formal_run_config(
            snapshot,
            os.fspath(candidate),
            digest,
            publication_authority=S.FORMAL_RUN_CONFIG_PUBLICATION_AUTHORITY,
        )
    result = results_parent / "r401_val_l3_a1_v2_all_slabs"
    if phase == "BEFORE_RENAME":
        assert not result.exists()
    else:
        assert result.exists()
        assert (result / "run_config.json").read_bytes() == raw
        assert (results_parent / ".attacker-displaced-result").exists()


@pytest.mark.parametrize("phase", ("BEFORE_RENAME", "AFTER_RENAME"))
def test_formal_role55_rejects_foreign_reserved_stage_across_hooks(
    tmp_path: Path, private_parent: Path, monkeypatch, phase: str
) -> None:
    authority = tmp_path / "authority"
    results_parent = authority / "results"
    results_parent.mkdir(parents=True)
    snapshot = _synthetic_formal_snapshot(authority)
    binding = {
        "schema_version": 1,
        "artifact_role": "SYNTHETIC_ROLE55_NON_SCIENTIFIC",
        "scientific_licensing_enabled": False,
    }
    monkeypatch.setattr(S, "revalidate_formal_snapshot", lambda *_a, **_k: None)
    monkeypatch.setattr(
        S, "build_formal_canonical_run_binding", lambda _snapshot: binding
    )
    monkeypatch.setattr(
        S, "validate_formal_canonical_run_binding", lambda value, *_a: value
    )
    candidate = private_parent / "run_config.json"
    _, digest = S.build_formal_run_config_candidate(
        snapshot, os.fspath(candidate)
    )
    foreign = (
        results_parent
        / ".r401_val_l3_a1_v2_all_slabs.role55-publish-foreign"
    )

    def hook(observed: str) -> None:
        if observed == phase:
            foreign.mkdir()

    monkeypatch.setattr(S, "_formal_run_publication_fault_hook", hook)
    with pytest.raises(S.CorruptGeneration, match="reserved staging namespace"):
        S.publish_formal_run_config(
            snapshot,
            os.fspath(candidate),
            digest,
            publication_authority=S.FORMAL_RUN_CONFIG_PUBLICATION_AUTHORITY,
        )
    result = results_parent / "r401_val_l3_a1_v2_all_slabs"
    assert foreign.is_dir()
    own_stages = [
        path
        for path in results_parent.iterdir()
        if path.name.startswith(
            ".r401_val_l3_a1_v2_all_slabs.role55-publish-"
        )
        and path != foreign
    ]
    assert own_stages == []
    if phase == "BEFORE_RENAME":
        assert not result.exists()
    else:
        assert (result / "run_config.json").is_file()
    foreign.rmdir()


def test_formal_role55_forces_0755_directory_under_restrictive_umask(
    tmp_path: Path, private_parent: Path, monkeypatch
) -> None:
    authority = tmp_path / "authority"
    (authority / "results").mkdir(parents=True)
    snapshot = _synthetic_formal_snapshot(authority)
    binding = {
        "schema_version": 1,
        "artifact_role": "SYNTHETIC_ROLE55_NON_SCIENTIFIC",
        "scientific_licensing_enabled": False,
    }
    monkeypatch.setattr(S, "revalidate_formal_snapshot", lambda *_a, **_k: None)
    monkeypatch.setattr(
        S, "build_formal_canonical_run_binding", lambda _snapshot: binding
    )
    monkeypatch.setattr(
        S, "validate_formal_canonical_run_binding", lambda value, *_a: value
    )
    candidate = private_parent / "run_config.json"
    _, digest = S.build_formal_run_config_candidate(
        snapshot, os.fspath(candidate)
    )
    previous_umask = os.umask(0o077)
    try:
        S.publish_formal_run_config(
            snapshot,
            os.fspath(candidate),
            digest,
            publication_authority=S.FORMAL_RUN_CONFIG_PUBLICATION_AUTHORITY,
        )
    finally:
        os.umask(previous_umask)
    result = authority / "results/r401_val_l3_a1_v2_all_slabs"
    assert stat.S_IMODE(result.stat().st_mode) == 0o755
    assert stat.S_IMODE((result / "run_config.json").stat().st_mode) == 0o644


def test_formal_role55_first_stage_fstat_fault_recovers_identity_and_cleans(
    tmp_path: Path, private_parent: Path, monkeypatch
) -> None:
    authority = tmp_path / "authority"
    results_parent = authority / "results"
    results_parent.mkdir(parents=True)
    snapshot = _synthetic_formal_snapshot(authority)
    binding = {
        "schema_version": 1,
        "artifact_role": "SYNTHETIC_ROLE55_NON_SCIENTIFIC",
        "scientific_licensing_enabled": False,
    }
    monkeypatch.setattr(S, "revalidate_formal_snapshot", lambda *_a, **_k: None)
    monkeypatch.setattr(
        S, "build_formal_canonical_run_binding", lambda _snapshot: binding
    )
    monkeypatch.setattr(
        S, "validate_formal_canonical_run_binding", lambda value, *_a: value
    )
    candidate = private_parent / "run_config.json"
    _, digest = S.build_formal_run_config_candidate(
        snapshot, os.fspath(candidate)
    )
    original_fstat = S.os.fstat
    injected = False

    def attacked_fstat(descriptor: int):
        nonlocal injected
        if not injected:
            try:
                target = os.readlink(f"/proc/self/fd/{descriptor}")
            except OSError:
                target = ""
            if ".r401_val_l3_a1_v2_all_slabs.role55-publish-" in target:
                injected = True
                raise OSError("synthetic first role55 stage fstat failure")
        return original_fstat(descriptor)

    monkeypatch.setattr(S.os, "fstat", attacked_fstat)
    with pytest.raises(OSError, match="first role55 stage fstat failure"):
        S.publish_formal_run_config(
            snapshot,
            os.fspath(candidate),
            digest,
            publication_authority=S.FORMAL_RUN_CONFIG_PUBLICATION_AUTHORITY,
        )
    assert injected is True
    assert not (results_parent / "r401_val_l3_a1_v2_all_slabs").exists()
    assert not [
        path
        for path in results_parent.iterdir()
        if path.name.startswith(
            ".r401_val_l3_a1_v2_all_slabs.role55-publish-"
        )
    ]


def test_formal_component_pair_crash_is_never_repaired(
    tmp_path: Path, private_parent: Path, monkeypatch
) -> None:
    authority = tmp_path / "authority"
    component_root = (
        authority / "results/r401_val_l3_a1_v2_all_slabs/static"
    )
    component_root.mkdir(parents=True)
    (component_root / "cells").mkdir()
    (component_root / "cell_manifests").mkdir()
    snapshot = _synthetic_formal_snapshot(authority)
    entries = _synthetic_component_entries("STATIC")
    run_hash = "d" * 64
    monkeypatch.setattr(S, "revalidate_formal_snapshot", lambda *_a, **_k: None)
    monkeypatch.setattr(
        S,
        "capture_formal_component_aggregate_inputs",
        lambda _component, _snapshot, **_kwargs: (
            run_hash, tuple(entries), "fixed-component-generation"
        ),
    )
    summary, manifest, package = (
        S.build_formal_component_aggregate_candidate_package(
            "STATIC",
            snapshot,
            run_hash,
            entries,
            os.fspath(private_parent),
        )
    )
    summary_raw = S.canonical_json_bytes(summary)
    manifest_raw = S.canonical_json_bytes(manifest)
    with pytest.raises(S.SyntheticCrash, match="after summary rename"):
        S.publish_formal_component_aggregates(
            "STATIC",
            snapshot,
            run_hash,
            entries,
            os.fspath(private_parent),
            hashlib.sha256(summary_raw).hexdigest(),
            hashlib.sha256(manifest_raw).hexdigest(),
            publication_authority=(
                S.FORMAL_COMPONENT_AGGREGATES_PUBLICATION_AUTHORITY
            ),
            _fail_at="AFTER_SUMMARY_RENAME",
        )
    summary_path = component_root / "aggregate_summary.json"
    manifest_path = component_root / "aggregate_manifest.json"
    assert summary_path.read_bytes() == summary_raw
    assert not manifest_path.exists()
    assert not [path for path in component_root.iterdir() if path.name.startswith(".")]
    S._replay_formal_private_pair_package(
        package,
        ("aggregate_summary.json", "aggregate_manifest.json"),
        context="post-crash candidate package",
    )
    with pytest.raises(S.CorruptGeneration, match="unexpected existing"):
        S.publish_formal_component_aggregates(
            "STATIC",
            snapshot,
            run_hash,
            entries,
            os.fspath(private_parent),
            hashlib.sha256(summary_raw).hexdigest(),
            hashlib.sha256(manifest_raw).hexdigest(),
            publication_authority=(
                S.FORMAL_COMPONENT_AGGREGATES_PUBLICATION_AUTHORITY
            ),
        )
    assert summary_path.read_bytes() == summary_raw
    assert not manifest_path.exists()


@pytest.mark.parametrize("fault", ("write", "first_fstat", "close"))
def test_formal_pair_stage_faults_close_and_inode_guard_cleanup(
    tmp_path: Path, monkeypatch, fault: str
) -> None:
    parent_fd = os.open(
        tmp_path,
        os.O_RDONLY | getattr(os, "O_DIRECTORY", 0),
    )
    original_write = S.os.write
    original_fstat = S.os.fstat
    original_close = S.os.close
    injected = False

    def is_stage(descriptor: int) -> bool:
        try:
            return stat.S_ISREG(original_fstat(descriptor).st_mode)
        except OSError:
            return False

    def attacked_write(descriptor: int, raw: bytes) -> int:
        nonlocal injected
        if fault == "write" and not injected and is_stage(descriptor):
            injected = True
            raise OSError("synthetic stage write failure")
        return original_write(descriptor, raw)

    def attacked_fstat(descriptor: int):
        nonlocal injected
        if fault == "first_fstat" and not injected and is_stage(descriptor):
            injected = True
            raise OSError("synthetic first fstat failure")
        return original_fstat(descriptor)

    def attacked_close(descriptor: int) -> None:
        nonlocal injected
        if fault == "close" and not injected and is_stage(descriptor):
            injected = True
            original_close(descriptor)
            raise OSError("synthetic close failure")
        original_close(descriptor)

    monkeypatch.setattr(S.os, "write", attacked_write)
    monkeypatch.setattr(S.os, "fstat", attacked_fstat)
    monkeypatch.setattr(S.os, "close", attacked_close)
    try:
        with pytest.raises((OSError, S.PathContractError)):
            S._write_formal_pair_stage(
                parent_fd,
                "aggregate_summary.json",
                b'{"candidate":true}\n',
                context=f"synthetic {fault} stage",
            )
        assert injected is True
        assert tuple(tmp_path.iterdir()) == ()
        assert original_fstat(parent_fd).st_nlink >= 2
    finally:
        original_close(parent_fd)


def test_formal_pair_stage_primary_and_close_failures_are_combined(
    tmp_path: Path, monkeypatch
) -> None:
    parent_fd = os.open(
        tmp_path,
        os.O_RDONLY | getattr(os, "O_DIRECTORY", 0),
    )
    original_write = S.os.write
    original_fstat = S.os.fstat
    original_close = S.os.close
    write_failed = False
    close_failed = False

    def is_stage(descriptor: int) -> bool:
        try:
            return stat.S_ISREG(original_fstat(descriptor).st_mode)
        except OSError:
            return False

    def attacked_write(descriptor: int, raw: bytes) -> int:
        nonlocal write_failed
        if not write_failed and is_stage(descriptor):
            write_failed = True
            raise OSError("synthetic primary stage write failure")
        return original_write(descriptor, raw)

    def attacked_close(descriptor: int) -> None:
        nonlocal close_failed
        if not close_failed and is_stage(descriptor):
            close_failed = True
            original_close(descriptor)
            raise OSError("synthetic stage close failure")
        original_close(descriptor)

    monkeypatch.setattr(S.os, "write", attacked_write)
    monkeypatch.setattr(S.os, "close", attacked_close)
    try:
        with pytest.raises(
            S.PathContractError, match="incomplete descriptor cleanup"
        ) as caught:
            S._write_formal_pair_stage(
                parent_fd,
                "aggregate_summary.json",
                b'{"candidate":true}\n',
                context="synthetic primary plus close stage",
            )
        assert isinstance(caught.value.__cause__, OSError)
        assert "primary stage write failure" in str(caught.value.__cause__)
        assert write_failed is True
        assert close_failed is True
        assert tuple(tmp_path.iterdir()) == ()
        assert original_fstat(parent_fd).st_nlink >= 2
    finally:
        original_close(parent_fd)


@pytest.mark.parametrize(
    "attack",
    ("summary_stage", "candidate", "input", "published_summary"),
)
def test_formal_pair_before_rename_hooks_replay_complete_envelope(
    tmp_path: Path, private_parent: Path, monkeypatch, attack: str
) -> None:
    authority = tmp_path / "authority"
    component_root = (
        authority / "results/r401_val_l3_a1_v2_all_slabs/static"
    )
    component_root.mkdir(parents=True)
    (component_root / "cells").mkdir()
    (component_root / "cell_manifests").mkdir()
    snapshot = _synthetic_formal_snapshot(authority)
    entries = _synthetic_component_entries("STATIC")
    run_hash = "d" * 64
    monkeypatch.setattr(S, "revalidate_formal_snapshot", lambda *_a, **_k: None)
    monkeypatch.setattr(
        S,
        "capture_formal_component_aggregate_inputs",
        lambda _component, _snapshot, **_kwargs: (
            run_hash, tuple(entries), "fixed-component-generation"
        ),
    )
    summary, manifest, _ = S.build_formal_component_aggregate_candidate_package(
        "STATIC", snapshot, run_hash, entries, os.fspath(private_parent)
    )
    summary_raw = S.canonical_json_bytes(summary)
    manifest_raw = S.canonical_json_bytes(manifest)

    def fault_hook(phase: str) -> None:
        if phase == "BEFORE_SUMMARY_RENAME" and attack in {
            "summary_stage", "candidate", "input"
        }:
            if attack == "summary_stage":
                stage = next(
                    path
                    for path in component_root.iterdir()
                    if path.name.startswith(".aggregate_summary.json.role19-publish-")
                )
                with stage.open("r+b", buffering=0) as stream:
                    stream.seek(0)
                    stream.write(b"X")
                    os.fsync(stream.fileno())
            elif attack == "candidate":
                candidate = private_parent / "aggregate_summary.json"
                with candidate.open("r+b", buffering=0) as stream:
                    stream.seek(0)
                    stream.write(b"X")
                    os.fsync(stream.fileno())
            else:
                entries[0]["sha256"] = "f" * 64
        if phase == "BEFORE_MANIFEST_RENAME" and attack == "published_summary":
            published = component_root / "aggregate_summary.json"
            with published.open("r+b", buffering=0) as stream:
                stream.seek(0)
                stream.write(b"X")
                os.fsync(stream.fileno())

    monkeypatch.setattr(S, "_formal_pair_publication_fault_hook", fault_hook)
    with pytest.raises((S.PathContractError, S.CorruptGeneration)):
        S.publish_formal_component_aggregates(
            "STATIC",
            snapshot,
            run_hash,
            entries,
            os.fspath(private_parent),
            hashlib.sha256(summary_raw).hexdigest(),
            hashlib.sha256(manifest_raw).hexdigest(),
            publication_authority=(
                S.FORMAL_COMPONENT_AGGREGATES_PUBLICATION_AUTHORITY
            ),
        )
    manifest_path = component_root / "aggregate_manifest.json"
    assert not manifest_path.exists()
    if attack == "published_summary":
        assert (component_root / "aggregate_summary.json").exists()
    else:
        assert not (component_root / "aggregate_summary.json").exists()


def test_real_exact102_generation_tracks_same_byte_inode_swaps_and_pair_rejects(
    tmp_path: Path, private_parent: Path, monkeypatch
) -> None:
    authority = tmp_path / "authority"
    result = authority / "results/r401_val_l3_a1_v2_all_slabs"
    component_root = result / "static"

    def directory(path: Path) -> None:
        path.mkdir(parents=True, exist_ok=True)
        path.chmod(0o755)

    def regular(path: Path, raw: bytes) -> None:
        path.write_bytes(raw)
        path.chmod(0o644)

    def replace_same_bytes(path: Path) -> None:
        raw = path.read_bytes()
        replacement = path.with_name(path.name + ".same-byte-replacement")
        regular(replacement, raw)
        before = path.stat().st_ino
        os.replace(replacement, path)
        assert path.stat().st_ino != before

    directory(result)
    directory(component_root / "cells")
    directory(component_root / "cell_manifests")
    regular(result / "run_config.json", b'{"role":55}\n')
    for bits in S.PRECISIONS:
        cells_precision = component_root / "cells" / str(bits)
        manifests_precision = component_root / "cell_manifests" / str(bits)
        directory(cells_precision)
        directory(manifests_precision)
        for slab in S.SLAB_IDS:
            cell_root = cells_precision / slab
            directory(cell_root)
            for name in ("proof.json", "stdout.txt", "stderr.txt", "record.json"):
                regular(cell_root / name, f"{bits}:{slab}:{name}\n".encode())
            regular(
                manifests_precision / f"{slab}.json",
                f"{bits}:{slab}:manifest\n".encode(),
            )

    snapshot = _synthetic_formal_snapshot(authority)
    image0 = S._capture_formal_component_generation_image("STATIC", snapshot)
    manifest_path = component_root / "cell_manifests/128" / f"{S.SLAB_IDS[0]}.json"
    replace_same_bytes(manifest_path)
    image1 = S._capture_formal_component_generation_image("STATIC", snapshot)
    assert image1 != image0
    payload_path = component_root / "cells/128" / S.SLAB_IDS[0] / "proof.json"
    replace_same_bytes(payload_path)
    image2 = S._capture_formal_component_generation_image("STATIC", snapshot)
    assert image2 != image1
    replace_same_bytes(result / "run_config.json")
    image3 = S._capture_formal_component_generation_image("STATIC", snapshot)
    assert image3 != image2

    entries = _synthetic_component_entries("STATIC")
    run_hash = "d" * 64
    monkeypatch.setattr(S, "revalidate_formal_snapshot", lambda *_a, **_k: None)

    def live_capture(
        _component: str,
        _snapshot: S.FormalAuthoritySnapshot,
        *,
        _component_entries: frozenset[str] = frozenset(),
    ):
        return (
            run_hash,
            tuple(entries),
            S._capture_formal_component_generation_image(
                "STATIC",
                snapshot,
                component_entries=_component_entries,
            ),
        )

    monkeypatch.setattr(S, "capture_formal_component_aggregate_inputs", live_capture)
    summary, manifest, _ = S.build_formal_component_aggregate_candidate_package(
        "STATIC", snapshot, run_hash, entries, os.fspath(private_parent)
    )
    attacked = False

    def swap_after_staging(phase: str) -> None:
        nonlocal attacked
        if phase == "BEFORE_SUMMARY_RENAME":
            attacked = True
            replace_same_bytes(payload_path)

    monkeypatch.setattr(S, "_formal_pair_publication_fault_hook", swap_after_staging)
    with pytest.raises(S.CorruptGeneration, match="canonical frontier changed"):
        S.publish_formal_component_aggregates(
            "STATIC",
            snapshot,
            run_hash,
            entries,
            os.fspath(private_parent),
            hashlib.sha256(S.canonical_json_bytes(summary)).hexdigest(),
            hashlib.sha256(S.canonical_json_bytes(manifest)).hexdigest(),
            publication_authority=(
                S.FORMAL_COMPONENT_AGGREGATES_PUBLICATION_AUTHORITY
            ),
        )
    assert attacked is True
    assert not (component_root / "aggregate_summary.json").exists()
    assert not (component_root / "aggregate_manifest.json").exists()
    assert not [path for path in component_root.iterdir() if path.name.startswith(".")]


def test_formal_composite_pair_exact18_17_and_zero_dispatch_publication(
    tmp_path: Path, private_parent: Path, monkeypatch
) -> None:
    authority = tmp_path / "authority"
    result = authority / "results/r401_val_l3_a1_v2_all_slabs"
    result.mkdir(parents=True)
    for directory in ("static", "branch"):
        (result / directory).mkdir()
    for name in (
        "run_config.json",
        "independent_static_checker.json",
        "STATIC_POSTCHECK_STATUS.json",
        "independent_branch_checker.json",
        "BRANCH_POSTCHECK_STATUS.json",
    ):
        (result / name).write_bytes(b"{}\n")
    snapshot = _synthetic_formal_snapshot(authority)
    monkeypatch.setattr(S, "revalidate_formal_snapshot", lambda *_a, **_k: None)
    chains = {
        component: {
            "aggregate_summary_sha256": hashlib.sha256(
                f"{component}-summary".encode("ascii")
            ).hexdigest(),
            "aggregate_manifest_sha256": hashlib.sha256(
                f"{component}-manifest".encode("ascii")
            ).hexdigest(),
            "checker_sha256": hashlib.sha256(
                f"{component}-checker".encode("ascii")
            ).hexdigest(),
            "postcheck_sha256": hashlib.sha256(
                f"{component}-postcheck".encode("ascii")
            ).hexdigest(),
            "ordered_cell_manifest_root": hashlib.sha256(
                f"{component}-root".encode("ascii")
            ).hexdigest(),
        }
        for component in ("static", "branch")
    }
    monkeypatch.setattr(
        S,
        "capture_formal_composite_inputs",
        lambda _snapshot, **_kwargs: (
            "e" * 64, chains, "fixed-composite-generation"
        ),
    )
    summary, manifest, _package = S.build_formal_composite_candidate_package(
        snapshot, "e" * 64, chains, os.fspath(private_parent)
    )
    assert set(summary) == S.FORMAL_COMPOSITE_SUMMARY_KEYS
    assert set(manifest) == S.FORMAL_COMPOSITE_MANIFEST_KEYS
    assert summary["cell_count_per_component"] == 102
    assert summary["scientific_licensing_enabled"] is False
    summary_raw = S.canonical_json_bytes(summary)
    manifest_raw = S.canonical_json_bytes(manifest)
    receipt = S.publish_formal_composite_candidates(
        snapshot,
        "e" * 64,
        chains,
        os.fspath(private_parent),
        hashlib.sha256(summary_raw).hexdigest(),
        hashlib.sha256(manifest_raw).hexdigest(),
        publication_authority=S.FORMAL_COMPOSITE_PUBLICATION_AUTHORITY,
    )
    assert (result / "composite_summary.json").read_bytes() == summary_raw
    assert (result / "composite_manifest.json").read_bytes() == manifest_raw
    assert receipt["scientific_licensing_enabled"] is False
    assert receipt["production_authorized"] is False
    assert receipt["scientific_dispatch_performed"] is False


def test_formal_static_live_capture_derives_pass_from_record_raw(
    tmp_path: Path, monkeypatch
) -> None:
    result = tmp_path / "results"
    cell = S.CellKey(128, S.SLAB_IDS[0])
    cell_root = result / "static/cells/128" / cell.slab_id
    manifest_root = result / "static/cell_manifests/128"
    cell_root.mkdir(parents=True)
    manifest_root.mkdir(parents=True)
    proof = {
        "authority": "PRODUCER_ONLY",
        "scientific_licensing_enabled": False,
        "matrix_id": S.canonical_matrix_id(),
        "freeze_sha256": "a" * 64,
        "run_config_sha256": "d" * 64,
        "claim_boundary": S.FORMAL_STATIC_CELL_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    raw_files = {
        "proof.json": S.canonical_json_bytes(proof),
        "stdout.txt": b"evaluator_status=STATIC_CELL_CERTIFIED\n",
        "stderr.txt": b"",
    }
    bindings = {
        name: {
            "path": name,
            "sha256": hashlib.sha256(raw).hexdigest(),
            "size_bytes": len(raw),
            "serializer": "CJ_COMPACT_V1" if name == "proof.json" else "RAW_BYTES",
            "truncated": False,
        }
        for name, raw in raw_files.items()
    }
    semantic = ["python", "evaluator", *(["x"] * 23), "<STAGING_PROOF_PATH>"]
    record = {
        "schema_version": 1,
        "protocol_id": S.PROTOCOL_ID,
        "artifact_role": "STATIC_CELL_RECORD",
        "authority": "PRODUCER_ONLY",
        "scientific_licensing_enabled": False,
        "matrix_id": S.canonical_matrix_id(),
        "freeze_sha256": "a" * 64,
        "main_freeze_sha256": "a" * 64,
        "run_config_sha256": "d" * 64,
        "cell": cell.payload(),
        "task": {
            "epsilon_lower": "0",
            "epsilon_upper": "1",
            "plan_record_sha256": "e" * 64,
        },
        "semantic_invocation": {
            "argv": semantic,
            "argv_sha256": hashlib.sha256(
                S.canonical_json_bytes(semantic)
            ).hexdigest(),
            "exact_string_count": 26,
            "output_token": "<STAGING_PROOF_PATH>",
        },
        "scheduler_result": {
            "classification": "CELL_TIMEOUT",
            "evaluator_status": None,
            "return_code": None,
            "proof_kind": "SCHEDULER_NO_PROOF_SENTINEL",
            "reason_code": "TIMEOUT",
        },
        "evaluator_result": {
            "status": None,
            "return_code": None,
            "status_line_count": 0,
        },
        "files": bindings,
        "limits": S.formal_limits()["static"],
        "claim_boundary": S.FORMAL_STATIC_CELL_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    record_raw = S.canonical_json_bytes(record)
    raw_files["record.json"] = record_raw
    for name, raw in raw_files.items():
        (cell_root / name).write_bytes(raw)
        (cell_root / name).chmod(0o644)
    record_binding = {
        "path": "record.json",
        "sha256": hashlib.sha256(record_raw).hexdigest(),
        "size_bytes": len(record_raw),
        "serializer": "CJ_COMPACT_V1",
        "truncated": False,
    }
    manifest = {
        "schema_version": 1,
        "protocol_id": S.PROTOCOL_ID,
        "artifact_role": "STATIC_CELL_MANIFEST",
        "authority": "PRODUCER_ONLY",
        "scientific_licensing_enabled": False,
        "matrix_id": S.canonical_matrix_id(),
        "freeze_sha256": "a" * 64,
        "main_freeze_sha256": "a" * 64,
        "run_config_sha256": "d" * 64,
        "cell": cell.payload(),
        "semantic_invocation_sha256": record["semantic_invocation"]["argv_sha256"],
        "scheduler_classification": "COMMITTED_EVALUATOR_RESULT",
        "evaluator_status": "STATIC_CELL_CERTIFIED",
        "record": record_binding,
        "files": {**bindings, "record.json": record_binding},
        "claim_boundary": S.FORMAL_STATIC_CELL_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    (manifest_root / f"{cell.slab_id}.json").write_bytes(
        S.canonical_json_bytes(manifest)
    )
    fake_plan = type("FakePlan", (), {"semantic_argv": tuple(semantic)})()
    monkeypatch.setattr(S, "_formal_static_capture_plan", lambda *_a: fake_plan)
    semantic_values = {
        "--epsilon-lower": "0",
        "--epsilon-upper": "1",
        "--plan-record-sha256": "e" * 64,
    }
    monkeypatch.setattr(
        S, "_semantic_flag", lambda _plan, flag: semantic_values[flag]
    )
    monkeypatch.setattr(
        S, "_validate_formal_static_evaluator_proof", lambda *_a: None
    )
    with pytest.raises(S.CorruptGeneration, match="producer pass ABI"):
        S._capture_formal_static_manifest_entry(
            result,
            cell,
            "a" * 64,
            "d" * 64,
            _synthetic_formal_snapshot(tmp_path),
        )


def test_formal_static_plan_rejects_coherent_frozen_task_mutation(
    tmp_path: Path
) -> None:
    authority = tmp_path / "authority"
    evaluator = authority / "synthetic/static_evaluator.py"
    evaluator.parent.mkdir(parents=True)
    evaluator.write_bytes(b"# synthetic evaluator\n")
    evaluator.chmod(0o644)

    def role(name: str, path: str, raw: bytes) -> object:
        return S.FormalRoleRecord(
            role=name,
            path=path,
            sha256=hashlib.sha256(raw).hexdigest(),
            raw=raw,
            stat_identity=(1, len(name) + 10, len(raw), 20, 30),
        )

    plan_raw = S.PLAN.read_bytes()
    roles = [
        role("static_evaluator", "synthetic/static_evaluator.py", evaluator.read_bytes()),
        role("static_checker_source", "synthetic/static_checker.py", b"checker\n"),
        role("l1_final_plan", S.PLAN.relative_to(S.ROOT).as_posix(), plan_raw),
    ]
    for name in S.FORMAL_STATIC_L1_SOURCE_ROLES:
        roles.append(role(name, dict(S.FORMAL_INPUT_ROLES)[name], name.encode()))
    snapshot = S.FormalAuthoritySnapshot(
        authority_root=authority,
        main_freeze_path=authority / "main.json",
        main_freeze_sha256="a" * 64,
        machine_freeze_path=authority / "machine.json",
        machine_freeze_sha256="b" * 64,
        prefreeze_review_path=authority / "review.md",
        prefreeze_review_sha256="c" * 64,
        input_roles=tuple(roles),
        main_freeze_raw=b"{}\n",
        main_freeze_stat_identity=(1, 2, 3, 4, 5),
        machine_freeze_raw=b"{}\n",
    )
    cell = S.CellKey(128, S.SLAB_IDS[0])
    frozen = S.validate_plan_payload(
        S.strict_json_loads(plan_raw.decode("utf-8"))
    )[cell.slab_id]
    semantic = [
        sys.executable,
        os.fspath(evaluator),
        "--slab-id",
        cell.slab_id,
        "--precision-bits",
        "128",
        "--epsilon-lower",
        "FORGED_BUT_SELF_HASHED",
        "--epsilon-upper",
        frozen["epsilon_upper"],
        "--matrix-id",
        S.canonical_matrix_id(),
        "--freeze-sha256",
        "a" * 64,
        "--run-config-sha256",
        "d" * 64,
        "--plan-record-sha256",
        hashlib.sha256(S.canonical_json_bytes(frozen)).hexdigest(),
        "--max-depth",
        str(S.candidate_limits()["static"]["max_depth_per_tree"]),
        "--max-nodes-per-tree",
        str(S.candidate_limits()["static"]["max_nodes_per_tree"]),
        "--max-nodes-per-cell",
        str(S.candidate_limits()["static"]["max_nodes_per_cell"]),
        "--output",
        "<STAGING_PROOF_PATH>",
    ]
    record = {
        "semantic_invocation": {
            "argv": semantic,
            "argv_sha256": hashlib.sha256(
                S.canonical_json_bytes(semantic)
            ).hexdigest(),
            "exact_string_count": 26,
            "output_token": "<STAGING_PROOF_PATH>",
        }
    }
    with pytest.raises(S.CorruptGeneration, match="frozen task ABI"):
        S._formal_static_capture_plan(
            snapshot, authority / "results", cell, "d" * 64, record
        )


def test_formal_branch_live_capture_rejects_coherent_nonpass_record(
    tmp_path: Path
) -> None:
    result = tmp_path / "results"
    cell = S.CellKey(128, S.SLAB_IDS[0])
    cell_root = result / "branch/cells/128" / cell.slab_id
    manifest_root = result / "branch/cell_manifests/128"
    cell_root.mkdir(parents=True)
    manifest_root.mkdir(parents=True)
    record = {key: None for key in S.FORMAL_BRANCH_RECORD_KEYS}
    record.update(
        {
            "artifact_role": "BRANCH_CELL_RECORD",
            "authority": "PRODUCER_ONLY",
            "claim_boundary": S.FORMAL_BRANCH_CELL_CLAIM_BOUNDARY,
            "component_status": None,
            "final_status": None,
            "freeze_sha256": "a" * 64,
            "matrix_id": S.canonical_matrix_id(),
            "milestone_status": None,
            "protocol_id": S.PROTOCOL_ID,
            "run_config_sha256": "d" * 64,
            "schema_version": 1,
            "scientific_licensing_enabled": False,
            "theorem_status": None,
            "scheduler_result": {
                "classification": "CELL_TIMEOUT",
                "evaluator_status": None,
                "return_code": None,
                "failure_reason": "FROZEN_CELL_TIMEOUT",
            },
        }
    )
    payloads = {
        "stdout.txt": b"",
        "stderr.txt": b"",
        "record.json": S.pretty_json_bytes(record),
    }
    files = {}
    for name, raw in payloads.items():
        path = cell_root / name
        path.write_bytes(raw)
        path.chmod(0o644)
        relative = f"branch/cells/128/{cell.slab_id}/{name}"
        files[relative] = hashlib.sha256(raw).hexdigest()
    budgets = {
        key: S.formal_limits()["branch"][key]
        for key in (
            "timeout_ms", "term_grace_ms", "pipe_close_grace_ms",
            "stdout_bytes", "stderr_bytes", "record_bytes", "total_cell_bytes",
        )
    }
    manifest = {
        "schema_version": 1,
        "protocol_id": S.PROTOCOL_ID,
        "artifact_role": "BRANCH_CELL_MANIFEST",
        "authority": "PRODUCER_ONLY",
        "scientific_licensing_enabled": False,
        "matrix_id": S.canonical_matrix_id(),
        "freeze_sha256": "a" * 64,
        "run_config_sha256": "d" * 64,
        "budgets": budgets,
        "cell_identity": cell.payload(),
        "files": files,
        "task_binding_sha256": "e" * 64,
        "claim_boundary": S.FORMAL_BRANCH_CELL_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    (manifest_root / f"{cell.slab_id}.json").write_bytes(
        S.pretty_json_bytes(manifest)
    )

    class FakeRuntime:
        @staticmethod
        def validate_committed_branch_cell(*_args):
            return record, manifest

    with pytest.raises(S.CorruptGeneration, match="producer pass ABI"):
        S._capture_formal_branch_manifest_entry(
            result,
            cell,
            "a" * 64,
            "d" * 64,
            (FakeRuntime(), object(), object(), object()),
        )


def test_formal_cli_rejects_explicit_zero_legacy_option_before_io(
    tmp_path: Path, monkeypatch, capsys
) -> None:
    monkeypatch.setattr(
        S,
        "load_formal_authority",
        lambda *_a: (_ for _ in ()).throw(
            AssertionError("formal CLI performed I/O before exact option gate")
        ),
    )
    status = S.main(
        [
            "--build-formal-run-config-candidate",
            "--authority-root",
            os.fspath(tmp_path / "authority"),
            "--output",
            os.fspath(tmp_path / "candidate"),
            "--mock-static-cells",
            "0",
        ]
    )
    captured = capsys.readouterr()
    assert status == 1
    assert captured.out == ""
    assert "exact-exclusive" in captured.err


def test_formal_cli_six_primary_modes_are_pairwise_exact_xor(
    tmp_path: Path, monkeypatch, capsys
) -> None:
    monkeypatch.setattr(
        S,
        "load_formal_authority",
        lambda *_a: (_ for _ in ()).throw(
            AssertionError("formal CLI performed I/O before XOR gate")
        ),
    )
    flags = (
        "--build-formal-run-config-candidate",
        "--publish-formal-run-config",
        "--build-formal-component-aggregate-candidates",
        "--publish-formal-component-aggregates",
        "--build-formal-composite-candidates",
        "--publish-formal-composite-candidates",
    )
    for left_index, left in enumerate(flags):
        for right in flags[left_index + 1 :]:
            status = S.main(
                [
                    left,
                    right,
                    "--authority-root",
                    os.fspath(tmp_path / "authority"),
                ]
            )
            captured = capsys.readouterr()
            assert status == 1
            assert captured.out == ""
            assert "exact XOR" in captured.err


@pytest.mark.parametrize("operation", ("snapshot", "writer"))
def test_private_pair_unlock_failure_still_closes_package_fd(
    private_parent: Path, monkeypatch, operation: str
) -> None:
    names = ("aggregate_summary.json", "aggregate_manifest.json")
    payloads = {
        names[0]: b'{"summary":true}\n',
        names[1]: b'{"manifest":true}\n',
    }
    if operation == "snapshot":
        for name, raw in payloads.items():
            path = private_parent / name
            path.write_bytes(raw)
            path.chmod(0o600)
    original_flock = S.fcntl.flock
    original_close = S.os.close
    unlock_fd = None
    closed_unlock_fd = False

    def attacked_flock(descriptor: int, operation_code: int) -> None:
        nonlocal unlock_fd
        if operation_code == S.fcntl.LOCK_UN:
            unlock_fd = descriptor
            raise OSError("synthetic unlock failure")
        original_flock(descriptor, operation_code)

    def observed_close(descriptor: int) -> None:
        nonlocal closed_unlock_fd
        if descriptor == unlock_fd:
            closed_unlock_fd = True
        original_close(descriptor)

    monkeypatch.setattr(S.fcntl, "flock", attacked_flock)
    monkeypatch.setattr(S.os, "close", observed_close)
    with pytest.raises(OSError, match="unlock failure"):
        if operation == "snapshot":
            S._snapshot_formal_private_pair_package(
                os.fspath(private_parent), names, context="unlock snapshot"
            )
        else:
            S._write_formal_private_pair_package(
                os.fspath(private_parent),
                payloads,
                names,
                context="unlock writer",
            )
    assert unlock_fd is not None
    assert closed_unlock_fd is True
    with pytest.raises(OSError):
        original_fstat = os.fstat
        original_fstat(unlock_fd)


def test_private_pair_writer_binds_initial_lexical_directory_inode(
    private_parent: Path, monkeypatch
) -> None:
    names = ("aggregate_summary.json", "aggregate_manifest.json")
    payloads = {names[0]: b'{"s":1}\n', names[1]: b'{"m":1}\n'}
    displaced = private_parent.with_name(private_parent.name + "-displaced")
    original_chain = S._machine_publication_directory_chain
    attacked = False

    def swap_before_chain(path: Path):
        nonlocal attacked
        if path == private_parent and not attacked:
            attacked = True
            private_parent.rename(displaced)
            private_parent.mkdir(mode=0o700)
        return original_chain(path)

    monkeypatch.setattr(S, "_machine_publication_directory_chain", swap_before_chain)
    try:
        with pytest.raises(S.PathContractError, match="initial lexical inode"):
            S._write_formal_private_pair_package(
                os.fspath(private_parent), payloads, names, context="swap writer"
            )
    finally:
        if private_parent.exists():
            private_parent.rmdir()
        if displaced.exists():
            displaced.rename(private_parent)
    assert attacked is True


def test_private_pair_writer_double_fstat_fault_recovers_and_cleans(
    private_parent: Path, monkeypatch
) -> None:
    names = ("aggregate_summary.json", "aggregate_manifest.json")
    payloads = {names[0]: b'{"s":1}\n', names[1]: b'{"m":1}\n'}
    original_fstat = S.os.fstat
    failures = 0

    def attacked_fstat(descriptor: int):
        nonlocal failures
        info = original_fstat(descriptor)
        if stat.S_ISREG(info.st_mode) and failures < 2:
            failures += 1
            raise OSError("synthetic repeated fstat failure")
        return info

    monkeypatch.setattr(S.os, "fstat", attacked_fstat)
    with pytest.raises(OSError, match="repeated fstat failure"):
        S._write_formal_private_pair_package(
            os.fspath(private_parent), payloads, names, context="double fstat"
        )
    assert failures == 2
    assert tuple(private_parent.iterdir()) == ()


def test_role55_primary_and_cleanup_failure_is_explicit_and_all_attempt(
    tmp_path: Path, private_parent: Path, monkeypatch
) -> None:
    authority = tmp_path / "authority"
    results_parent = authority / "results"
    results_parent.mkdir(parents=True)
    snapshot = _synthetic_formal_snapshot(authority)
    binding = {
        "schema_version": 1,
        "artifact_role": "SYNTHETIC_ROLE55_NON_SCIENTIFIC",
        "scientific_licensing_enabled": False,
    }
    monkeypatch.setattr(S, "revalidate_formal_snapshot", lambda *_a, **_k: None)
    monkeypatch.setattr(
        S, "build_formal_canonical_run_binding", lambda _snapshot: binding
    )
    monkeypatch.setattr(
        S, "validate_formal_canonical_run_binding", lambda value, *_a: value
    )
    candidate = private_parent / "run_config.json"
    _, digest = S.build_formal_run_config_candidate(
        snapshot, os.fspath(candidate)
    )
    original_unlink = S.os.unlink

    def failed_cleanup_unlink(path, *args, **kwargs):
        if path == "run_config.json" and kwargs.get("dir_fd") is not None:
            raise OSError("synthetic cleanup unlink failure")
        return original_unlink(path, *args, **kwargs)

    monkeypatch.setattr(S.os, "unlink", failed_cleanup_unlink)
    with pytest.raises(S.PathContractError, match="incomplete cleanup") as caught:
        S.publish_formal_run_config(
            snapshot,
            os.fspath(candidate),
            digest,
            publication_authority=S.FORMAL_RUN_CONFIG_PUBLICATION_AUTHORITY,
            _fail_at="BEFORE_RENAME",
        )
    assert isinstance(caught.value.__cause__, S.SyntheticCrash)
    stages = [
        path for path in results_parent.iterdir()
        if path.name.startswith(".r401_val_l3_a1_v2_all_slabs.role55-publish-")
    ]
    assert len(stages) == 1
    original_unlink(stages[0] / "run_config.json")
    stages[0].rmdir()
    assert not (results_parent / "r401_val_l3_a1_v2_all_slabs").exists()


def test_pair_primary_and_cleanup_failure_is_explicit(
    tmp_path: Path, private_parent: Path, monkeypatch
) -> None:
    authority = tmp_path / "authority"
    component_root = authority / "results/r401_val_l3_a1_v2_all_slabs/static"
    component_root.mkdir(parents=True)
    (component_root / "cells").mkdir()
    (component_root / "cell_manifests").mkdir()
    snapshot = _synthetic_formal_snapshot(authority)
    entries = _synthetic_component_entries("STATIC")
    run_hash = "d" * 64
    monkeypatch.setattr(S, "revalidate_formal_snapshot", lambda *_a, **_k: None)
    monkeypatch.setattr(
        S,
        "capture_formal_component_aggregate_inputs",
        lambda _component, _snapshot, **_kwargs: (
            run_hash, tuple(entries), "fixed-component-generation"
        ),
    )
    summary, manifest, _ = S.build_formal_component_aggregate_candidate_package(
        "STATIC", snapshot, run_hash, entries, os.fspath(private_parent)
    )
    monkeypatch.setattr(
        S,
        "_cleanup_machine_publication_stage",
        lambda *_a, **_k: (_ for _ in ()).throw(
            OSError("synthetic pair cleanup failure")
        ),
    )
    with pytest.raises(S.PathContractError, match="incomplete cleanup") as caught:
        S.publish_formal_component_aggregates(
            "STATIC",
            snapshot,
            run_hash,
            entries,
            os.fspath(private_parent),
            hashlib.sha256(S.canonical_json_bytes(summary)).hexdigest(),
            hashlib.sha256(S.canonical_json_bytes(manifest)).hexdigest(),
            publication_authority=S.FORMAL_COMPONENT_AGGREGATES_PUBLICATION_AUTHORITY,
            _fail_at="BEFORE_SUMMARY_RENAME",
        )
    assert isinstance(caught.value.__cause__, S.SyntheticCrash)
    for path in tuple(component_root.iterdir()):
        if path.name.startswith("."):
            path.unlink()
    assert {path.name for path in component_root.iterdir()} == {
        "cells", "cell_manifests"
    }
