from __future__ import annotations

import hashlib
import importlib.util
import os
import subprocess
import sys
import tempfile
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "scripts/run_r401_val_l3_a1_v2_all_slabs.py"


def load_scheduler():
    name = "r401_val_l3_a1_v2_scheduler_branch_tests"
    specification = importlib.util.spec_from_file_location(name, SOURCE)
    assert specification is not None and specification.loader is not None
    module = importlib.util.module_from_spec(specification)
    sys.modules[name] = module
    specification.loader.exec_module(module)
    return module


S = load_scheduler()


def _git(repo: Path, *argv: str) -> str:
    return subprocess.run(
        ("/usr/bin/git", "-C", os.fspath(repo), *argv),
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    ).stdout.strip()


def _new_git_repo(tmp_path: Path) -> Path:
    repo = tmp_path / "repo"
    repo.mkdir()
    _git(repo, "init", "-b", "main")
    _git(repo, "config", "user.email", "test@example.invalid")
    _git(repo, "config", "user.name", "V2 Test")
    (repo / "tracked.txt").write_text("tracked\n", encoding="utf-8")
    _git(repo, "add", "tracked.txt")
    _git(repo, "commit", "-m", "root")
    return repo


def _prepare_rebuild_authority(
    tmp_path: Path,
    monkeypatch,
    *,
    compiler_script: str,
) -> tuple[Path, Path, bytes]:
    project = tmp_path / "authority"
    source_relative = dict(S.FORMAL_INPUT_ROLES)["branch_evaluator_source"]
    binary_relative = dict(S.FORMAL_INPUT_ROLES)["branch_evaluator_binary"]
    source_path = project / source_relative
    binary_path = project / binary_relative
    source_path.parent.mkdir(parents=True, exist_ok=True)
    binary_path.parent.mkdir(parents=True, exist_ok=True)
    source_raw = b"int main(){return 0;}\n"
    binary_raw = b"synthetic-reproducible-binary\n"
    source_path.write_bytes(source_raw)
    source_path.chmod(0o644)
    binary_path.write_bytes(binary_raw)
    binary_path.chmod(0o755)
    machine = {
        "branch_binary": {
            "source_sha256": hashlib.sha256(source_raw).hexdigest(),
            "sha256": hashlib.sha256(binary_raw).hexdigest(),
            "size_bytes": len(binary_raw),
        },
        "compiler": {
            "build_recipe": {
                "argv_template": [
                    sys.executable,
                    "-c",
                    compiler_script,
                    "@STAGING_BINARY@",
                ],
                "environment": dict(os.environ),
            }
        },
    }
    machine_raw = S.canonical_json_bytes(machine)
    monkeypatch.setattr(
        S,
        "strict_json_image",
        lambda *_args, **_kwargs: (machine, machine_raw, None),
    )
    monkeypatch.setattr(S, "_validate_formal_machine_envelope", lambda value: value)
    parent = Path(
        "/tmp/a416-l3a1-v2-role11-rebuild." + os.urandom(8).hex()
    )
    os.mkdir(parent, 0o700)
    return project, parent / "capd_r401_phase_branch_tube_mp_a1", binary_raw


def test_role11_publication_status_allows_only_exact_owned_leaf(
    tmp_path: Path,
) -> None:
    repo = _new_git_repo(tmp_path)
    stage = repo / ".R401_VAL_L3_A1_V2_PREFREEZE_TESTS.json.publish-0123456789abcdef"
    stage.write_bytes(b"candidate\n")
    stage.chmod(0o644)
    info = stage.stat()
    S._v2_role11_expect_publication_status(
        repo, stage, (info.st_dev, info.st_ino), "stage"
    )
    extra = repo / "foreign.txt"
    extra.write_text("foreign\n", encoding="utf-8")
    with pytest.raises(S.ProductionAuthorityError, match="one owned leaf"):
        S._v2_role11_expect_publication_status(
            repo, stage, (info.st_dev, info.st_ino), "stage with foreign"
        )
    extra.unlink()
    canonical = repo / "R401_VAL_L3_A1_V2_PREFREEZE_TESTS.json"
    stage.rename(canonical)
    renamed = canonical.stat()
    assert (renamed.st_dev, renamed.st_ino) == (info.st_dev, info.st_ino)
    S._v2_role11_expect_publication_status(
        repo, canonical, (info.st_dev, info.st_ino), "canonical"
    )


def test_role11_cli_preserves_raw_candidate_spelling(monkeypatch, capsys) -> None:
    observed: dict[str, str] = {}

    def fake_capture(output: str, authority_root: str):
        observed["output"] = output
        observed["authority_root"] = authority_root
        return {"artifact_role": S.V2_ROLE11_ARTIFACT_ROLE}, "a" * 64

    monkeypatch.setattr(S, "capture_v2_prefreeze_test_candidate", fake_capture)
    raw_output = "/tmp/a416-v2-raw-parent//candidate.json"
    assert S.main([
        "--capture-prefreeze-tests",
        "--output", raw_output,
        "--authority-root", os.fspath(ROOT),
    ]) == 0
    assert observed == {
        "output": raw_output,
        "authority_root": os.fspath(ROOT),
    }
    assert "TEMP_PREFREEZE_TESTS_CANDIDATE" in capsys.readouterr().out


def test_role11_cli_modes_are_exact_xor(monkeypatch, capsys) -> None:
    monkeypatch.setattr(
        S,
        "capture_v2_prefreeze_test_candidate",
        lambda *_args, **_kwargs: (_ for _ in ()).throw(
            AssertionError("conflicting CLI dispatched capture")
        ),
    )
    assert S.main([
        "--capture-prefreeze-tests",
        "--publish-prefreeze-tests",
        "--output", "/tmp/a416-v2-parent/candidate.json",
        "--candidate", "/tmp/a416-v2-parent/candidate.json",
        "--expected-sha256", "a" * 64,
        "--authority-root", os.fspath(ROOT),
    ]) == 1
    assert "exact-exclusive" in capsys.readouterr().err


def test_second_rebuild_success_removes_owned_leaf_and_parent(
    tmp_path: Path, monkeypatch
) -> None:
    binary_literal = repr(b"synthetic-reproducible-binary\n")
    project, output, binary_raw = _prepare_rebuild_authority(
        tmp_path,
        monkeypatch,
        compiler_script=(
            "import os,sys; raw=" + binary_literal + "; "
            "open(sys.argv[1],'wb').write(raw); os.chmod(sys.argv[1],0o755)"
        ),
    )
    receipt = S.run_v2_role11_second_fresh_rebuild(
        os.fspath(output), project
    )
    assert receipt["staging_output_sha256"] == hashlib.sha256(binary_raw).hexdigest()
    assert receipt["staging_output_removed"] is True
    assert not output.exists()
    assert not output.parent.exists()


def test_second_rebuild_nonzero_cleans_owned_residue(
    tmp_path: Path, monkeypatch
) -> None:
    project, output, _binary_raw = _prepare_rebuild_authority(
        tmp_path,
        monkeypatch,
        compiler_script=(
            "import os,sys; open(sys.argv[1],'wb').write(b'partial'); "
            "os.chmod(sys.argv[1],0o755); raise SystemExit(7)"
        ),
    )
    with pytest.raises(S.ProductionAuthorityError, match="compiler failed"):
        S.run_v2_role11_second_fresh_rebuild(os.fspath(output), project)
    assert not output.exists()
    assert not output.parent.exists()


def test_second_rebuild_timeout_path_cleans_owned_residue(
    tmp_path: Path, monkeypatch
) -> None:
    project, output, _binary_raw = _prepare_rebuild_authority(
        tmp_path,
        monkeypatch,
        compiler_script="raise AssertionError('replaced capture helper should run')",
    )

    def fake_timeout(argv, **_kwargs):
        path = Path(argv[-1])
        path.write_bytes(b"partial-timeout")
        path.chmod(0o755)
        raise S.ProductionAuthorityError("synthetic compiler timeout")

    monkeypatch.setattr(S, "_capture_command", fake_timeout)
    with pytest.raises(S.ProductionAuthorityError, match="synthetic compiler timeout"):
        S.run_v2_role11_second_fresh_rebuild(os.fspath(output), project)
    assert not output.exists()
    assert not output.parent.exists()


def test_second_rebuild_semantic_mismatch_cleans_owned_residue(
    tmp_path: Path, monkeypatch
) -> None:
    project, output, _binary_raw = _prepare_rebuild_authority(
        tmp_path,
        monkeypatch,
        compiler_script=(
            "import os,sys; open(sys.argv[1],'wb').write(b'wrong-binary'); "
            "os.chmod(sys.argv[1],0o755)"
        ),
    )
    with pytest.raises(S.ProductionAuthorityError, match="differed byte-for-byte"):
        S.run_v2_role11_second_fresh_rebuild(os.fspath(output), project)
    assert not output.exists()
    assert not output.parent.exists()


def test_second_rebuild_preserves_foreign_inode_substitution(
    tmp_path: Path, monkeypatch
) -> None:
    binary_literal = repr(b"synthetic-reproducible-binary\n")
    project, output, _binary_raw = _prepare_rebuild_authority(
        tmp_path,
        monkeypatch,
        compiler_script=(
            "import os,sys; raw=" + binary_literal + "; "
            "open(sys.argv[1],'wb').write(raw); os.chmod(sys.argv[1],0o755)"
        ),
    )
    original_reader = S._read_machine_publication_file_at
    substituted = False

    def substitute(parent_fd, name, context, **kwargs):
        nonlocal substituted
        if context == "second rebuild staging output" and not substituted:
            substituted = True
            S.os.unlink(name, dir_fd=parent_fd)
            descriptor = S.os.open(
                name,
                S.os.O_WRONLY | S.os.O_CREAT | S.os.O_EXCL,
                0o755,
                dir_fd=parent_fd,
            )
            try:
                S.os.write(descriptor, b"foreign")
            finally:
                S.os.close(descriptor)
        return original_reader(parent_fd, name, context, **kwargs)

    monkeypatch.setattr(S, "_read_machine_publication_file_at", substitute)
    with pytest.raises(S.PathContractError, match="substituted output"):
        S.run_v2_role11_second_fresh_rebuild(os.fspath(output), project)
    assert output.read_bytes() == b"foreign"
    output.unlink()
    output.parent.rmdir()


def test_capture_command_timeout_is_bounded_and_restores_subreaper() -> None:
    before = S._capture_child_subreaper_state()
    with pytest.raises(S.ProductionAuthorityError, match="timed out"):
        S._capture_command(
            (sys.executable, "-c", "import time; time.sleep(30)"),
            cwd=ROOT,
            environment=dict(os.environ),
            timeout_seconds=1,
        )
    assert S._capture_child_subreaper_state() is before
