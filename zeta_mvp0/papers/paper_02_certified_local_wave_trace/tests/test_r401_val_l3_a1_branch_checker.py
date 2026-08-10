from __future__ import annotations

import ast
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
from contextlib import contextmanager
from dataclasses import replace
from fractions import Fraction
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
CHECKER_SOURCE = ROOT / "scripts/check_r401_val_l3_a1_branch_independent.py"
SCHEDULER_SOURCE = ROOT / "scripts/run_r401_val_l3_a1_all_slabs.py"
MOCK_EVALUATOR = ROOT / "scripts/mock_r401_val_l3_a1_branch_evaluator.py"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def checker():
    return load_module(
        CHECKER_SOURCE,
        "r401_val_l3_a1_branch_checker_focused_tests",
    )


@pytest.fixture(scope="module")
def scheduler():
    return load_module(
        SCHEDULER_SOURCE,
        "r401_val_l3_a1_scheduler_branch_checker_fixture",
    )


@pytest.fixture(scope="module")
def full_mock_archive(tmp_path_factory, scheduler) -> Path:
    output = tmp_path_factory.mktemp("a416-branch-checker") / "archive"
    static = scheduler.run_mock_static(output, 102, resume=False)
    assert static["aggregate_finalized"] is True
    branch = scheduler.run_mock_branch(
        output,
        MOCK_EVALUATOR,
        102,
        resume=False,
    )
    assert branch["aggregate_finalized"] is True
    return output


def compact_bytes(payload) -> bytes:
    return (
        json.dumps(
            payload,
            sort_keys=True,
            ensure_ascii=False,
            separators=(",", ":"),
            allow_nan=False,
        ).encode("utf-8")
        + b"\n"
    )


def runtime_bytes(payload) -> bytes:
    return (
        json.dumps(
            payload,
            indent=2,
            sort_keys=True,
            ensure_ascii=False,
            allow_nan=False,
        ).encode("utf-8")
        + b"\n"
    )


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


@contextmanager
def restore_files(paths: list[Path]):
    originals = {path: path.read_bytes() for path in paths}
    try:
        yield
    finally:
        for path, raw in originals.items():
            if path.is_symlink() or path.exists():
                path.unlink()
            path.write_bytes(raw)


def cell_paths(archive: Path, bits: int = 128, slab: str = "S000") -> list[Path]:
    cell = archive / f"branch/cells/{bits}/{slab}"
    return [
        cell / "stdout.txt",
        cell / "stderr.txt",
        cell / "record.json",
        archive / f"branch/cell_manifests/{bits}/{slab}.json",
        archive / "branch/aggregate_summary.json",
        archive / "branch/aggregate_manifest.json",
    ]


def rebind_cell_archive(
    archive: Path,
    *,
    bits: int = 128,
    slab: str = "S000",
    update_raw_bindings: bool,
) -> None:
    stdout, stderr, record_path, cell_manifest_path, summary_path, aggregate_path = cell_paths(
        archive, bits, slab
    )
    record = json.loads(record_path.read_text(encoding="utf-8"))
    if update_raw_bindings:
        for stem, path in (("stdout", stdout), ("stderr", stderr)):
            raw = path.read_bytes()
            record["raw"][f"{stem}_bytes"] = len(raw)
            record["raw"][f"{stem}_sha256"] = digest(raw)
    record_path.write_bytes(runtime_bytes(record))

    manifest = json.loads(cell_manifest_path.read_text(encoding="utf-8"))
    for path in (stdout, stderr, record_path):
        relative = path.relative_to(archive).as_posix()
        manifest["files"][relative] = digest(path.read_bytes())
    cell_manifest_path.write_bytes(runtime_bytes(manifest))

    aggregate = json.loads(aggregate_path.read_text(encoding="utf-8"))
    entries = aggregate["cell_manifests"]
    target = next(
        entry
        for entry in entries
        if entry["cell"] == {"precision_bits": bits, "slab_id": slab}
    )
    target["sha256"] = digest(cell_manifest_path.read_bytes())
    target["size_bytes"] = cell_manifest_path.stat().st_size
    ordered_root = digest(compact_bytes(entries))

    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    summary["ordered_cell_manifest_root"] = ordered_root
    summary_path.write_bytes(compact_bytes(summary))
    aggregate["ordered_cell_manifest_root"] = ordered_root
    aggregate["summary"] = {
        "path": "branch/aggregate_summary.json",
        "sha256": digest(summary_path.read_bytes()),
        "size_bytes": summary_path.stat().st_size,
    }
    aggregate_path.write_bytes(compact_bytes(aggregate))


def replace_transcript_field(raw: bytes, key: str, value: str) -> bytes:
    prefix = f"{key}="
    lines = raw.decode("utf-8").splitlines()
    hits = [index for index, line in enumerate(lines) if line.startswith(prefix)]
    assert len(hits) == 1
    lines[hits[0]] = prefix + value
    return ("\n".join(lines) + "\n").encode("utf-8")


def test_checker_has_no_producer_or_checker_import(checker) -> None:
    tree = ast.parse(CHECKER_SOURCE.read_text(encoding="utf-8"))
    imported: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.add(node.module)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            assert node.func.id not in {"eval", "exec", "__import__"}
    assert not any(name.startswith("r401_val_l3_a1") for name in imported)
    assert "importlib" not in imported
    assert "subprocess" not in imported
    assert checker.SCHEDULER.name not in imported


def test_exact_102_mock_replay_is_nonlicensing(checker, full_mock_archive) -> None:
    result = checker.run_checker(full_mock_archive)
    assert set(result) == checker.CHECKER_KEYS
    assert result["checker_status"] == "PASS_MOCK_INDEPENDENT_REPLAY"
    assert result["authority"] == "INDEPENDENT_CHECKER"
    assert result["passed"] is True
    assert result["scientific_licensing_enabled"] is False
    assert result["component_status"] is None
    assert result["milestone_status"] is None
    assert result["theorem_status"] is None
    assert result["final_status"] is None
    assert result["replay_counts"] == {
        "accepted_l1_chain_objects": 6,
        "aggregate_objects": 2,
        "cell_directories": 102,
        "cell_manifests": 102,
        "cell_records": 102,
        "hash_bound_payloads": 408,
        "phase_records": 6528,
        "raw_stderr_objects": 102,
        "raw_transcripts": 102,
        "tube_implication_checks": 6528,
    }
    assert result["cross_precision"] == {
        "all_agree": True,
        "input_domains_agree": 51,
        "mock_only": True,
        "scientific_domain_replay_performed": False,
        "slab_pairs": 51,
        "status_pairs_agree": 51,
    }
    assert result["diagnostics"]["production_dispatch_observed"] is False
    assert result["diagnostics"]["scientific_flow_replay_performed"] is False
    assert result["diagnostics"]["synthetic_tube_implication_replay_performed"] is True


def test_cli_checker_and_postcheck_are_write_once(
    checker, full_mock_archive
) -> None:
    checker_path = full_mock_archive / "independent_branch_checker.json"
    postcheck_path = full_mock_archive / "BRANCH_POSTCHECK_STATUS.json"
    for path in (checker_path, postcheck_path):
        if path.exists() or path.is_symlink():
            path.unlink()
    try:
        command = [
            sys.executable,
            str(CHECKER_SOURCE),
            "--input-dir",
            str(full_mock_archive),
        ]
        first = subprocess.run(command, text=True, capture_output=True, check=False)
        assert first.returncode == 0, first.stderr
        assert "PASS_MOCK_INDEPENDENT_REPLAY" in first.stdout
        checker_raw = checker_path.read_bytes()
        second = subprocess.run(command, text=True, capture_output=True, check=False)
        assert second.returncode == 1
        assert checker_path.read_bytes() == checker_raw

        post = subprocess.run(
            [*command, "--postcheck"],
            text=True,
            capture_output=True,
            check=False,
        )
        assert post.returncode == 0, post.stderr
        payload = json.loads(postcheck_path.read_text(encoding="utf-8"))
        assert set(payload) == checker.POSTCHECK_KEYS
        assert payload["postcheck_status"] == "PASS_MOCK_WRITE_ONCE_POSTCHECK"
        assert payload["component_status"] is None
        assert payload["milestone_status"] is None
        assert payload["theorem_status"] is None
        assert payload["final_status"] is None
        assert payload["bound_artifacts"] == {
            "aggregate_manifest": {
                "path": "branch/aggregate_manifest.json",
                "sha256": digest(
                    (full_mock_archive / "branch/aggregate_manifest.json").read_bytes()
                ),
            },
            "aggregate_summary": {
                "path": "branch/aggregate_summary.json",
                "sha256": digest(
                    (full_mock_archive / "branch/aggregate_summary.json").read_bytes()
                ),
            },
            "checker_source": {
                "path": CHECKER_SOURCE.relative_to(ROOT).as_posix(),
                "sha256": digest(CHECKER_SOURCE.read_bytes()),
            },
        }
        post_raw = postcheck_path.read_bytes()
        repeated = subprocess.run(
            [*command, "--postcheck"],
            text=True,
            capture_output=True,
            check=False,
        )
        assert repeated.returncode == 1
        assert postcheck_path.read_bytes() == post_raw
    finally:
        for path in (postcheck_path, checker_path):
            if path.exists() or path.is_symlink():
                path.unlink()


def test_formal_run_config_is_fail_closed(checker, full_mock_archive) -> None:
    path = full_mock_archive / "run_config.json"
    with restore_files([path]):
        payload = json.loads(path.read_text(encoding="utf-8"))
        payload["artifact_status"] = "FORMAL_PRODUCTION"
        payload["mock_only"] = False
        payload["production_authorized"] = True
        path.write_bytes(compact_bytes(payload))
        with pytest.raises(checker.FormalBranchAuthorityError, match="fail-closed"):
            checker.run_checker(full_mock_archive)


@pytest.mark.parametrize(
    "raw",
    [
        b'{"x":1,"x":2}\n',
        b'{"x":NaN}\n',
        b'{"x":Infinity}\n',
        b'{"x":1e400}\n',
    ],
)
def test_strict_json_rejects_duplicate_and_nonfinite(checker, raw: bytes) -> None:
    with pytest.raises(checker.BranchCheckError):
        checker.strict_json_from_bytes(raw, "adversarial JSON")


def test_independent_runtime_serializer_requires_exact_plain_json(checker) -> None:
    class DictAlias(dict):
        pass

    class ListAlias(list):
        pass

    class StringAlias(str):
        pass

    cycle = []
    cycle.append(cycle)
    attacks = [
        ("tuple",),
        {1: "non-string-key"},
        {StringAlias("alias-key"): "value"},
        DictAlias({"key": "value"}),
        ListAlias([1]),
        {"nested": [StringAlias("value")]},
        {"nested": [float("nan")]},
        {"nested": [float("inf")]},
        {"nested": [float("-inf")]},
        cycle,
    ]
    for serializer in (checker.runtime_json_bytes, checker.canonical_json_bytes):
        for payload in attacks:
            with pytest.raises(checker.BranchCheckError):
                serializer(payload)

    assert checker.runtime_json_bytes(
        {"finite": 1.25, "items": [True, None, 3]}
    ) == (
        b'{\n  "finite": 1.25,\n  "items": [\n'
        b"    true,\n    null,\n    3\n  ]\n}\n"
    )
    shared = [1]
    assert checker.runtime_json_bytes({"left": shared, "right": shared}) == (
        b'{\n  "left": [\n    1\n  ],\n'
        b'  "right": [\n    1\n  ]\n}\n'
    )


@pytest.mark.parametrize("bad_count", [True, 102.0])
def test_exact_count_rejects_boolean_and_integral_float_alias(
    checker, full_mock_archive, bad_count
) -> None:
    summary = full_mock_archive / "branch/aggregate_summary.json"
    with restore_files([summary]):
        payload = json.loads(summary.read_text(encoding="utf-8"))
        payload["cell_count"] = bad_count
        summary.write_bytes(compact_bytes(payload))
        with pytest.raises(checker.BranchCheckError):
            checker.run_checker(full_mock_archive)


def test_missing_extra_and_hidden_authoritative_paths_are_rejected(
    checker, full_mock_archive, tmp_path: Path
) -> None:
    manifest = full_mock_archive / "branch/cell_manifests/128/S050.json"
    parked = tmp_path / "S050.json"
    manifest.rename(parked)
    try:
        with pytest.raises(checker.BranchCheckError, match="names differ"):
            checker.run_checker(full_mock_archive)
    finally:
        parked.rename(manifest)

    extra = full_mock_archive / "branch/cells/128/S000/.hidden"
    extra.write_bytes(b"hidden\n")
    try:
        with pytest.raises(checker.BranchCheckError, match="names differ"):
            checker.run_checker(full_mock_archive)
    finally:
        extra.unlink()


def test_raw_hash_mutation_is_rejected(checker, full_mock_archive) -> None:
    stdout = full_mock_archive / "branch/cells/128/S000/stdout.txt"
    with restore_files([stdout]):
        stdout.write_bytes(stdout.read_bytes() + b"unbound=true\n")
        with pytest.raises(checker.BranchCheckError, match="stdout_(?:bytes|sha256)|stdout hash"):
            checker.run_checker(full_mock_archive)


def test_symlink_leaf_and_hardlink_alias_are_rejected(
    checker, full_mock_archive, tmp_path: Path
) -> None:
    stdout = full_mock_archive / "branch/cells/128/S000/stdout.txt"
    original = stdout.read_bytes()
    target = tmp_path / "target.txt"
    target.write_bytes(original)
    stdout.unlink()
    stdout.symlink_to(target)
    try:
        with pytest.raises(checker.BranchCheckError, match="symlink"):
            checker.run_checker(full_mock_archive)
    finally:
        stdout.unlink()
        stdout.write_bytes(original)

    stdout.unlink()
    os.link(target, stdout)
    try:
        with pytest.raises(checker.BranchCheckError, match="hard-link"):
            checker.run_checker(full_mock_archive)
    finally:
        stdout.unlink()
        stdout.write_bytes(original)


def test_symlink_parent_and_noncanonical_cli_alias_are_rejected(
    checker, tmp_path: Path
) -> None:
    real = tmp_path / "real"
    real.mkdir()
    (real / "payload").write_bytes(b"x")
    alias = tmp_path / "alias"
    alias.symlink_to(real, target_is_directory=True)
    with pytest.raises(checker.BranchCheckError, match="symlink"):
        checker.capture_file(alias / "payload", "aliased parent")
    with pytest.raises(SystemExit):
        checker.main(["--input-dir", "//tmp/noncanonical-a416"])


def test_captured_snapshot_detects_post_read_mutation(checker, tmp_path: Path) -> None:
    path = tmp_path / "snapshot.bin"
    path.write_bytes(b"before")
    image = checker.capture_file(path, "snapshot")
    path.write_bytes(b"after!")
    with pytest.raises(checker.BranchCheckError, match="changed after capture"):
        image.verify_unchanged("snapshot replay")


@pytest.mark.parametrize(
    ("field", "value", "error_fragment"),
    [
        ("segment_000_phase", "[0,0.02]", "phase 0"),
        (
            "segment_000_state",
            "{[1,1],[0,0],[0,0],[0,0],[0,0.0021],[0.663,0.664]}",
            "tube gate",
        ),
        ("segment_000_rslow_sq", "[1,1]", "printed radius"),
        ("segment_000_margin_sq", "[1,1]", "printed margin"),
        ("segment_000_relation", "OUTSIDE", "relation"),
        ("omega_slow", "[0,0]", "omega"),
        ("input_arg_02", "9", "input echo"),
        ("maximum_rslow_sq_upper", "[1,1]", "aggregate maximum"),
        ("status", "BRANCH_TUBE_UNRESOLVED", "terminal status"),
    ],
)
def test_semantic_transcript_mutations_survive_rehash_but_fail_replay(
    checker,
    full_mock_archive,
    field: str,
    value: str,
    error_fragment: str,
) -> None:
    paths = cell_paths(full_mock_archive)
    with restore_files(paths):
        paths[0].write_bytes(replace_transcript_field(paths[0].read_bytes(), field, value))
        rebind_cell_archive(full_mock_archive, update_raw_bindings=True)
        with pytest.raises(checker.BranchCheckError, match=error_fragment):
            checker.run_checker(full_mock_archive)


def test_record_task_path_and_binding_mutations_are_rejected(
    checker, full_mock_archive
) -> None:
    paths = cell_paths(full_mock_archive)
    with restore_files(paths):
        record = json.loads(paths[2].read_text(encoding="utf-8"))
        record["cell"]["accepted_l1_primary_record_sha256"] = "0" * 64
        paths[2].write_bytes(runtime_bytes(record))
        rebind_cell_archive(full_mock_archive, update_raw_bindings=False)
        with pytest.raises(checker.BranchCheckError, match="task"):
            checker.run_checker(full_mock_archive)

    with restore_files(paths):
        manifest = json.loads(paths[3].read_text(encoding="utf-8"))
        old = f"branch/cells/128/S000/stdout.txt"
        manifest["files"]["branch/cells/128/S000/../stdout.txt"] = manifest["files"].pop(old)
        paths[3].write_bytes(runtime_bytes(manifest))
        rebind_cell_archive(full_mock_archive, update_raw_bindings=False)
        with pytest.raises(checker.BranchCheckError, match="manifest.files"):
            checker.run_checker(full_mock_archive)


def test_rehashed_legacy_second_budget_abi_is_rejected(
    checker, full_mock_archive
) -> None:
    paths = cell_paths(full_mock_archive)
    with restore_files(paths):
        legacy_budget = {
            "pipe_close_grace_seconds": 1.0,
            "record_bytes": 4 * 1024 * 1024,
            "stderr_bytes": 1 * 1024 * 1024,
            "stdout_bytes": 16 * 1024 * 1024,
            "term_grace_seconds": 2.0,
            "timeout_seconds": 600.0,
            "total_cell_bytes": 32 * 1024 * 1024,
        }
        record = json.loads(paths[2].read_text(encoding="utf-8"))
        record["budgets"] = legacy_budget
        paths[2].write_bytes(runtime_bytes(record))
        manifest = json.loads(paths[3].read_text(encoding="utf-8"))
        manifest["budgets"] = legacy_budget
        paths[3].write_bytes(runtime_bytes(manifest))
        rebind_cell_archive(full_mock_archive, update_raw_bindings=False)
        with pytest.raises(checker.BranchCheckError, match="budgets"):
            checker.run_checker(full_mock_archive)


def test_aggregate_order_root_and_summary_binding_are_replayed(
    checker, full_mock_archive
) -> None:
    summary = full_mock_archive / "branch/aggregate_summary.json"
    manifest = full_mock_archive / "branch/aggregate_manifest.json"
    with restore_files([summary, manifest]):
        aggregate = json.loads(manifest.read_text(encoding="utf-8"))
        aggregate["cell_manifests"][0], aggregate["cell_manifests"][1] = (
            aggregate["cell_manifests"][1],
            aggregate["cell_manifests"][0],
        )
        root = digest(compact_bytes(aggregate["cell_manifests"]))
        aggregate["ordered_cell_manifest_root"] = root
        summary_payload = json.loads(summary.read_text(encoding="utf-8"))
        summary_payload["ordered_cell_manifest_root"] = root
        summary.write_bytes(compact_bytes(summary_payload))
        aggregate["summary"]["sha256"] = digest(summary.read_bytes())
        aggregate["summary"]["size_bytes"] = summary.stat().st_size
        manifest.write_bytes(compact_bytes(aggregate))
        with pytest.raises(checker.BranchCheckError, match="aggregate (?:summary|manifest)"):
            checker.run_checker(full_mock_archive)


def _synthetic_cross_precision_cells(checker):
    cells = {}
    for bits in checker.PRECISIONS:
        for slab in checker.SLABS:
            transcript = checker.TranscriptReplay(
                maximum_rslow_sq_upper=Fraction(0),
                minimum_margin_sq_lower=Fraction(1, 625),
                phase_checks=64,
                input_domain=((slab, slab), (("0", "1"),) * 4),
                evaluator_status=checker.CELL_PASS_STATUS,
            )
            cells[(bits, slab)] = checker.CellReplay(
                aggregate_entry={},
                transcript=transcript,
                evaluator_binding={},
                snapshots=(),
            )
    return cells


def test_cross_precision_input_and_final_verdict_disagreement_fail_closed(
    checker,
) -> None:
    cells = _synthetic_cross_precision_cells(checker)
    assert checker.validate_cross_precision(cells) == (51, 51)
    key = (256, "S000")
    original = cells[key]
    cells[key] = replace(
        original,
        transcript=replace(
            original.transcript,
            input_domain=(("different", "domain"), (("0", "1"),) * 4),
        ),
    )
    with pytest.raises(checker.BranchCheckError, match="input disagreement"):
        checker.validate_cross_precision(cells)
    cells = _synthetic_cross_precision_cells(checker)
    original = cells[key]
    cells[key] = replace(
        original,
        transcript=replace(
            original.transcript,
            evaluator_status="BRANCH_TUBE_UNRESOLVED",
        ),
    )
    with pytest.raises(checker.BranchCheckError, match="verdict disagreement"):
        checker.validate_cross_precision(cells)


def test_exact_l1_primary_tasks_and_cross_precision_domains(checker) -> None:
    bundle = checker.load_l1_bundle()
    tasks = checker.expected_tasks(bundle, str(MOCK_EVALUATOR.resolve()))
    assert len(tasks) == 102
    assert [task.slab_id for task in tasks[:51]] == list(checker.SLABS)
    assert [task.slab_id for task in tasks[51:]] == list(checker.SLABS)
    for index, slab in enumerate(checker.SLABS):
        left, right = tasks[index], tasks[index + 51]
        assert left.precision_bits == 128
        assert right.precision_bits == 256
        assert left.epsilon == right.epsilon
        assert left.root_box == right.root_box
        assert left.accepted_l1_primary_record_id == f"128/{slab}/primary"
        assert right.accepted_l1_primary_record_id == f"256/{slab}/primary"
        assert len(left.argv()) == len(right.argv()) == 12


def test_write_once_rejects_existing_symlink_hardlink_and_wrong_path(
    checker, tmp_path: Path
) -> None:
    output = tmp_path / "checker.json"
    checker.write_once(output, b"{}\n")
    with pytest.raises(FileExistsError):
        checker.write_once(output, b"{}\n")

    symlink = tmp_path / "symlink.json"
    symlink.symlink_to(output)
    with pytest.raises(checker.BranchCheckError, match="symlink"):
        checker.write_once(symlink, b"{}\n")

    hardlink = tmp_path / "hardlink.json"
    os.link(output, hardlink)
    with pytest.raises(FileExistsError):
        checker.write_once(hardlink, b"{}\n")

    nonexistent = tmp_path / "archive"
    nonexistent.mkdir()
    assert checker.main(
        [
            "--input-dir",
            str(nonexistent),
            "--output",
            str(nonexistent / "wrong.json"),
        ]
    ) == 1


def test_missing_aggregate_and_live_operational_owner_are_rejected(
    checker, full_mock_archive
) -> None:
    aggregate = full_mock_archive / "branch/aggregate_manifest.json"
    parked = aggregate.with_suffix(".parked")
    aggregate.rename(parked)
    try:
        with pytest.raises(checker.BranchCheckError, match="names differ"):
            checker.run_checker(full_mock_archive)
    finally:
        parked.rename(aggregate)

    operational = full_mock_archive.with_name(full_mock_archive.name + ".operational")
    stage = operational / "staging/branch/128/.S000.tmp-deadbeefdeadbeef-0"
    stage.mkdir()
    try:
        with pytest.raises(checker.BranchCheckError, match="names differ"):
            checker.run_checker(full_mock_archive)
    finally:
        stage.rmdir()


def test_duplicate_key_in_canonical_aggregate_is_rejected(
    checker, full_mock_archive
) -> None:
    summary = full_mock_archive / "branch/aggregate_summary.json"
    with restore_files([summary]):
        raw = summary.read_bytes()
        assert raw.startswith(b"{")
        summary.write_bytes(b'{"schema_version":1,' + raw[1:])
        with pytest.raises(checker.BranchCheckError, match="duplicate JSON key"):
            checker.run_checker(full_mock_archive)


def test_postcheck_rejects_changed_published_checker(
    checker, full_mock_archive
) -> None:
    checker_path = full_mock_archive / "independent_branch_checker.json"
    if checker_path.exists():
        checker_path.unlink()
    result = checker.run_checker(full_mock_archive)
    result["passed"] = False
    checker_path.write_bytes(compact_bytes(result))
    try:
        with pytest.raises(checker.BranchCheckError, match="published mock branch checker"):
            checker.run_postcheck(full_mock_archive)
    finally:
        checker_path.unlink()
