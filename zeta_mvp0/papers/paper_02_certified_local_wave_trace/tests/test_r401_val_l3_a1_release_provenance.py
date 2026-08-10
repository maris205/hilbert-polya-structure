from __future__ import annotations

import copy
from datetime import datetime, timezone
from decimal import Decimal
import hashlib
import importlib.util
import json
import os
import shutil
import stat
import struct
import zlib
from pathlib import Path
from typing import Any

import pytest


ROOT = Path(__file__).resolve().parents[1]
BUILDER_SOURCE = ROOT / "scripts/build_r401_val_l3_a1_release_provenance.py"
COMPOSITE_SOURCE = ROOT / "scripts/check_r401_val_l3_a1_composite_independent.py"
COMPOSITE_TEST_SOURCE = ROOT / "tests/test_r401_val_l3_a1_composite_contract.py"


def load(path: Path, name: str):
    specification = importlib.util.spec_from_file_location(name, path)
    assert specification is not None and specification.loader is not None
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


R = load(BUILDER_SOURCE, "l3_a1_release")
C = load(COMPOSITE_SOURCE, "l3_a1_composite_for_release")
CT = load(COMPOSITE_TEST_SOURCE, "l3_a1_composite_fixture")


def write_json(path: Path, payload: Any) -> bytes:
    raw = R.canonical_json_bytes(payload)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(raw)
    return raw


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def build_result(project: Path) -> Path:
    result = project / R.RESULT_RELATIVE
    result.mkdir(parents=True)
    _, run_raw = CT.mock_run_config(result)
    run_hash = sha(run_raw)
    CT.make_component(result, "static", run_hash)
    CT.make_component(result, "branch", run_hash)
    static_chain, _, _ = C.validate_component_chain(result, "static", run_hash)
    branch_chain, _, _ = C.validate_component_chain(result, "branch", run_hash)
    summary, manifest = C.expected_composite_controls(
        result, run_hash, static_chain, branch_chain
    )
    CT.write_json(result / "composite_summary.json", summary)
    CT.write_json(result / "composite_manifest.json", manifest)
    checker = C.run_checker(result)
    CT.write_json(result / "independent_checker.json", checker)
    postcheck = C.run_postcheck(result)
    CT.write_json(result / "POSTCHECK_STATUS.json", postcheck)
    report = (
        "Status: PASS_MOCK_PROVENANCE_REPLAY\n"
        "milestone_status = null\n"
        "theorem_status = null\n"
        "final_status = null\n"
        f"Claim boundary: {R.MOCK_CLAIM_BOUNDARY}\n"
    )
    (result / "R401_VAL_L3_A1_REPORT.md").write_text(report, encoding="utf-8")
    return result


def populate_inputs(project: Path) -> None:
    for role, relative in R.INPUT_ROLES:
        path = project / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        source = ROOT / relative
        if source.is_file():
            path.write_bytes(source.read_bytes())
        elif relative.endswith(".json"):
            write_json(path, {"role": role, "mock_only": True})
        elif role == "branch_evaluator_binary":
            path.write_bytes(b"MOCK BINARY - NEVER EXECUTED\n")
        else:
            path.write_text(f"mock input role: {role}\n", encoding="utf-8")


def publish_mock_freeze(project: Path) -> dict[str, Any]:
    input_roles = [R.role_binding(project, role, relative) for role, relative in R.INPUT_ROLES]
    machine_hash = next(item["sha256"] for item in input_roles if item["role"] == "machine_freeze")
    payload = {
        "schema_version": 1,
        "protocol_id": R.PROTOCOL_ID,
        "artifact_role": "MOCK_MAIN_FREEZE",
        "artifact_status": "MOCK_ONLY_NON_LICENSING",
        "authority": "ENGINEERING_TEST_ONLY",
        "mock_only": True,
        "scientific_licensing_enabled": False,
        "matrix": R.matrix_payload(),
        "matrix_id": R.matrix_id(),
        "machine_freeze_sha256": machine_hash,
        "input_roles": input_roles,
        "claim_boundary": R.MOCK_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    write_json(project / R.MAIN_FREEZE_RELATIVE, payload)
    return payload


def release_fixture(tmp_path: Path) -> Path:
    project = tmp_path / "project"
    project.mkdir()
    populate_inputs(project)
    build_result(project)
    publish_mock_freeze(project)
    return project


def rewrite(path: Path, mutator) -> None:
    payload = json.loads(path.read_text(encoding="utf-8"))
    mutator(payload)
    write_json(path, payload)


def test_build_and_verify_exact_68_role_mock_release(tmp_path: Path) -> None:
    project = release_fixture(tmp_path)
    released = R.build_release(project)
    assert released["release_status"] == R.MOCK_RELEASE_STATUS
    assert released["scientific_licensing_enabled"] is False
    assert released["milestone_status"] is None
    assert released["theorem_status"] is None
    assert released["final_status"] is None
    assert len(released["roles"]) == 68
    assert [item["role"] for item in released["roles"]] == [
        *[role for role, _ in R.INPUT_ROLES],
        "main_freeze",
        *[role for role, _ in R.DOWNSTREAM_ROLES],
    ]
    before = (project / R.RESULT_RELATIVE / R.RELEASE_NAME).read_bytes()
    verified = R.verify_release(project)
    assert verified == released
    assert (project / R.RESULT_RELATIVE / R.RELEASE_NAME).read_bytes() == before


def test_identical_build_is_idempotent(tmp_path: Path) -> None:
    project = release_fixture(tmp_path)
    first = R.build_release(project)
    path = project / R.RESULT_RELATIVE / R.RELEASE_NAME
    before = (path.read_bytes(), path.stat().st_mtime_ns)
    second = R.build_release(project)
    assert second == first
    assert (path.read_bytes(), path.stat().st_mtime_ns) == before


def test_missing_main_freeze_input_is_rejected(tmp_path: Path) -> None:
    project = release_fixture(tmp_path)
    (project / R.INPUT_ROLES[0][1]).unlink()
    with pytest.raises((R.ReleaseError, FileNotFoundError)):
        R.build_expected_release(project)


def test_changed_input_after_freeze_is_rejected(tmp_path: Path) -> None:
    project = release_fixture(tmp_path)
    path = project / R.INPUT_ROLES[5][1]
    path.write_text("changed after mock freeze\n", encoding="utf-8")
    with pytest.raises(R.ReleaseError, match="53-role"):
        R.build_expected_release(project)


def test_downstream_manifest_mutation_is_rejected(tmp_path: Path) -> None:
    project = release_fixture(tmp_path)
    path = project / R.RESULT_RELATIVE / "branch/cell_manifests/128/S000.json"
    rewrite(path, lambda payload: payload.__setitem__("evaluator_status", "FORGED"))
    with pytest.raises(R.ReleaseError, match="canonical|hash mismatch|key set"):
        R.build_expected_release(project)


def test_nominal_formal_freeze_is_fail_closed(tmp_path: Path) -> None:
    project = release_fixture(tmp_path)
    path = project / R.MAIN_FREEZE_RELATIVE
    rewrite(path, lambda payload: payload.__setitem__("mock_only", False))
    with pytest.raises(R.ReleaseError, match="not implemented"):
        R.build_expected_release(project)


def test_report_authority_mutation_is_rejected(tmp_path: Path) -> None:
    project = release_fixture(tmp_path)
    path = project / R.RESULT_RELATIVE / "R401_VAL_L3_A1_REPORT.md"
    path.write_text(path.read_text(encoding="utf-8") + "theorem_status = PASS\n", encoding="utf-8")
    with pytest.raises(R.ReleaseError, match="authority block"):
        R.build_expected_release(project)


def test_duplicate_key_in_json_role_is_rejected(tmp_path: Path) -> None:
    project = release_fixture(tmp_path)
    path = project / "research/route_a_wave_trace/R401_VAL_L3_A1_S0_COMPATIBILITY_REPLAY.json"
    path.write_text('{"x":1,"x":2}\n', encoding="utf-8")
    with pytest.raises(R.StrictJSONError, match="duplicate"):
        R.build_expected_release(project)


def test_symlinked_input_role_is_rejected(tmp_path: Path) -> None:
    project = release_fixture(tmp_path)
    path = project / R.INPUT_ROLES[0][1]
    saved = project / "saved.md"
    path.rename(saved)
    path.symlink_to(saved)
    with pytest.raises((R.PathContractError, OSError)):
        R.build_expected_release(project)


def test_different_existing_release_is_never_overwritten(tmp_path: Path) -> None:
    project = release_fixture(tmp_path)
    path = project / R.RESULT_RELATIVE / R.RELEASE_NAME
    path.write_bytes(b'{"foreign":true}\n')
    before = path.read_bytes()
    with pytest.raises(R.ReleaseError, match="different release"):
        R.build_release(project)
    assert path.read_bytes() == before


def test_verify_only_rejects_noncanonical_release_bytes(tmp_path: Path) -> None:
    project = release_fixture(tmp_path)
    released = R.build_release(project)
    path = project / R.RESULT_RELATIVE / R.RELEASE_NAME
    path.write_text(json.dumps(released, indent=2) + "\n", encoding="utf-8")
    with pytest.raises(R.StrictJSONError, match="not canonical"):
        R.verify_release(project)


def test_composite_checker_claim_mutation_is_rejected(tmp_path: Path) -> None:
    project = release_fixture(tmp_path)
    result = project / R.RESULT_RELATIVE
    checker_path = result / "independent_checker.json"
    rewrite(
        checker_path,
        lambda payload: payload.__setitem__("claim_boundary", "FORGED THEOREM AUTHORITY"),
    )
    checker_hash = sha(checker_path.read_bytes())
    rewrite(
        result / "POSTCHECK_STATUS.json",
        lambda payload: payload.__setitem__("checker_sha256", checker_hash),
    )
    with pytest.raises(R.ReleaseError, match="composite checker authority"):
        R.build_expected_release(project)


def test_nested_composite_postcheck_authority_is_rejected(tmp_path: Path) -> None:
    project = release_fixture(tmp_path)
    path = project / R.RESULT_RELATIVE / "POSTCHECK_STATUS.json"
    rewrite(
        path,
        lambda payload: payload["bound_artifacts"].__setitem__(
            "theorem_status", "RH_PROVED"
        ),
    )
    with pytest.raises(R.ReleaseError, match="nested authority|artifact bindings"):
        R.build_expected_release(project)


def test_frozen_release_builder_must_match_executing_source(tmp_path: Path) -> None:
    project = release_fixture(tmp_path)
    (project / "scripts/build_r401_val_l3_a1_release_provenance.py").write_text(
        "# coherent but foreign release builder\n", encoding="utf-8"
    )
    publish_mock_freeze(project)
    with pytest.raises(R.ReleaseError, match="executing source"):
        R.build_expected_release(project)


def test_frozen_protocol_must_match_checker_source_binding(tmp_path: Path) -> None:
    project = release_fixture(tmp_path)
    (project / "research/route_a_wave_trace/R401_VAL_L3_A1_PROTOCOL.md").write_text(
        "FORGED ALTERNATE PROTOCOL\n", encoding="utf-8"
    )
    publish_mock_freeze(project)
    with pytest.raises(R.ReleaseError, match="executing source"):
        R.build_expected_release(project)


def test_hidden_component_authority_file_is_rejected(tmp_path: Path) -> None:
    project = release_fixture(tmp_path)
    path = project / R.RESULT_RELATIVE / "static/.hidden-authority.json"
    write_json(path, {"theorem_status": "FORGED"})
    with pytest.raises(R.PathContractError, match="namespace mismatch"):
        R.build_expected_release(project)


def test_late_authoritative_extra_prevents_success(tmp_path: Path, monkeypatch) -> None:
    project = release_fixture(tmp_path)
    original = R.write_once

    def publish_then_add_extra(path: Path, raw: bytes) -> None:
        original(path, raw)
        (path.parent / ".late-authority-extra").write_text(
            "late extra\n", encoding="utf-8"
        )

    monkeypatch.setattr(R, "write_once", publish_then_add_extra)
    with pytest.raises(R.PathContractError, match="namespace mismatch"):
        R.build_release(project)


def test_release_source_has_no_component_imports() -> None:
    text = BUILDER_SOURCE.read_text(encoding="utf-8")
    assert "import run_r401" not in text
    assert "import check_r401" not in text
    assert "subprocess" not in text


def _fixture_file(path: Path, raw: bytes, mode: int = 0o644) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(raw)
    path.chmod(mode)
    return path


def _copy_fixture_file(source: Path, target: Path, mode: int) -> Path:
    return _fixture_file(target, source.read_bytes(), mode)


def _live_binding(path: Path, build_id: str | None) -> dict[str, Any]:
    raw = path.read_bytes()
    return {
        "path": str(path),
        "mode": stat.S_IMODE(path.stat().st_mode),
        "size_bytes": len(raw),
        "sha256": sha(raw),
        "build_id": build_id,
    }


def _runtime_binding(path: Path, soname: str, marker: str) -> dict[str, Any]:
    binding = _live_binding(path, (marker * 40)[:40])
    return {"soname": soname, **binding}


def _fixture_elf(
    build_id: str,
    *,
    soname: str | None = None,
    needed: tuple[str, ...] = (),
) -> bytes:
    """Construct the smallest section-table ELF needed by the live parser."""

    assert len(build_id) == 40 and all(character in "0123456789abcdef" for character in build_id)
    dynamic_strings = bytearray(b"\x00")

    def add_string(value: str) -> int:
        offset = len(dynamic_strings)
        dynamic_strings.extend(value.encode("ascii") + b"\x00")
        return offset

    dynamic_entries = [(1, add_string(value)) for value in needed]
    if soname is not None:
        dynamic_entries.append((14, add_string(soname)))
    dynamic_entries.append((0, 0))
    dynamic = b"".join(struct.pack("<qQ", *entry) for entry in dynamic_entries)
    note = struct.pack("<III", 4, 20, 3) + b"GNU\x00" + bytes.fromhex(build_id)
    shstr = b"\x00.dynstr\x00.dynamic\x00.note.gnu.build-id\x00.shstrtab\x00"
    names = {
        ".dynstr": shstr.index(b".dynstr"),
        ".dynamic": shstr.index(b".dynamic"),
        ".note.gnu.build-id": shstr.index(b".note.gnu.build-id"),
        ".shstrtab": shstr.index(b".shstrtab"),
    }
    image = bytearray(b"\x00" * 64)

    def append_section(raw: bytes, alignment: int) -> tuple[int, int]:
        while len(image) % alignment:
            image.append(0)
        offset = len(image)
        image.extend(raw)
        return offset, len(raw)

    dynstr_offset, dynstr_size = append_section(bytes(dynamic_strings), 1)
    dynamic_offset, dynamic_size = append_section(dynamic, 8)
    note_offset, note_size = append_section(note, 4)
    shstr_offset, shstr_size = append_section(shstr, 1)
    while len(image) % 8:
        image.append(0)
    section_offset = len(image)
    section_format = "<IIQQQQIIQQ"
    sections = [struct.pack(section_format, *([0] * 10))]
    sections.append(struct.pack(
        section_format, names[".dynstr"], 3, 0, 0, dynstr_offset,
        dynstr_size, 0, 0, 1, 0,
    ))
    sections.append(struct.pack(
        section_format, names[".dynamic"], 6, 0, 0, dynamic_offset,
        dynamic_size, 1, 0, 8, 16,
    ))
    sections.append(struct.pack(
        section_format, names[".note.gnu.build-id"], 7, 0, 0, note_offset,
        note_size, 0, 0, 4, 0,
    ))
    sections.append(struct.pack(
        section_format, names[".shstrtab"], 3, 0, 0, shstr_offset,
        shstr_size, 0, 0, 1, 0,
    ))
    image.extend(b"".join(sections))
    ident = b"\x7fELF" + bytes((2, 1, 1, 0)) + b"\x00" * 8
    header = struct.pack(
        "<16sHHIQQQIHHHHHH",
        ident, 3, 62, 1, 0, 0, section_offset, 0, 64, 0, 0, 64,
        len(sections), 4,
    )
    image[:64] = header
    return bytes(image)


def _fixture_conda_manifest(prefix: Path, files: list[str]) -> tuple[int, str]:
    rows: list[dict[str, Any]] = []
    for relative in files:
        path = prefix / relative
        info = os.lstat(path)
        if stat.S_ISLNK(info.st_mode):
            raw = os.fsencode(os.readlink(path))
            kind = "SYMLINK"
        else:
            raw = path.read_bytes()
            kind = "REGULAR"
        rows.append({
            "kind": kind,
            "mode": f"{stat.S_IMODE(info.st_mode):04o}",
            "path": relative,
            "sha256": sha(raw),
            "size_bytes": len(raw),
        })
    rows.sort(key=lambda row: row["path"].encode("utf-8"))
    return len(rows), sha(R.canonical_json_bytes(rows))


def _fixture_git_index(
    checkout: Path,
    tracked: dict[str, tuple[int, bytes]],
    *,
    update_head: bool = True,
) -> tuple[str, str]:
    git_dir = checkout / ".git"
    git_dir.mkdir(parents=True, exist_ok=True)
    entries = bytearray()
    rows: list[dict[str, Any]] = []
    tree_entries: list[tuple[bytes, bytes]] = []
    for relative in sorted(tracked, key=lambda item: item.encode("utf-8")):
        mode, raw = tracked[relative]
        object_id = hashlib.sha1(
            b"blob " + str(len(raw)).encode("ascii") + b"\x00" + raw,
            usedforsecurity=False,
        ).digest()
        path_raw = relative.encode("utf-8")
        entry = bytearray(struct.pack(
            ">LLLLLLLLLL20sH",
            0, 0, 0, 0, 0, 0, mode, 0, 0, len(raw), object_id,
            min(len(path_raw), 0xFFF),
        ))
        entry.extend(path_raw + b"\x00")
        while len(entry) % 8:
            entry.append(0)
        entries.extend(entry)
        rows.append({
            "git_blob_sha1": object_id.hex(),
            "mode": f"{mode:06o}",
            "path": relative,
            "sha256": sha(raw),
            "size_bytes": len(raw),
        })
        tree_entries.append((
            path_raw,
            f"{mode:06o}".encode("ascii")
            + b" " + path_raw + b"\x00" + object_id,
        ))
    body = b"DIRC" + struct.pack(">II", 2, len(tracked)) + bytes(entries)
    checksum = hashlib.sha1(body, usedforsecurity=False).digest()
    (git_dir / "index").write_bytes(body + checksum)
    tree_payload = b"".join(payload for _, payload in sorted(tree_entries))
    tree_framed = (
        b"tree " + str(len(tree_payload)).encode("ascii") + b"\x00" + tree_payload
    )
    tree_oid = hashlib.sha1(tree_framed, usedforsecurity=False).hexdigest()
    commit_payload = (
        f"tree {tree_oid}\n"
        "author Fixture <fixture@example.test> 0 +0000\n"
        "committer Fixture <fixture@example.test> 0 +0000\n"
        "\nfixture\n"
    ).encode("ascii")
    commit_framed = (
        b"commit " + str(len(commit_payload)).encode("ascii")
        + b"\x00" + commit_payload
    )
    commit = hashlib.sha1(commit_framed, usedforsecurity=False).hexdigest()
    loose = git_dir / "objects" / commit[:2] / commit[2:]
    loose.parent.mkdir(parents=True)
    loose.write_bytes(zlib.compress(commit_framed))
    if update_head:
        (git_dir / "HEAD").write_bytes((commit + "\n").encode("ascii"))
    return commit, sha(R.canonical_json_bytes(rows))


def _fixture_static_argv(
    row: dict[str, Any], bindings: dict[str, Any], plan_record: dict[str, Any]
) -> list[str]:
    return [
        bindings["interpreter"]["invocation_path"],
        bindings["evaluator"]["path"],
        "--slab-id", row["slab_id"],
        "--precision-bits", str(row["precision_bits"]),
        "--epsilon-lower", plan_record["epsilon_lower"],
        "--epsilon-upper", plan_record["epsilon_upper"],
        "--matrix-id", bindings["calibration_binding"]["matrix_id"],
        "--freeze-sha256", bindings["calibration_binding"]["nonfreeze_sha256"],
        "--run-config-sha256",
        bindings["calibration_binding"]["nonrunconfig_sha256"],
        "--plan-record-sha256", sha(R.canonical_json_bytes(plan_record)),
        "--max-depth", "24",
        "--max-nodes-per-tree", "250000",
        "--max-nodes-per-cell", "1000000",
        "--output", row["output"],
    ]


def _fixture_branch_argv(
    binary: str, bits: int, record: dict[str, Any]
) -> list[str]:
    center = record["center"]
    radii = record["root_radii"]

    def endpoint(name: str, sign: int) -> str:
        return format(Decimal(center[name]) + sign * Decimal(radii[name]), "f")

    return [
        binary,
        str(bits),
        record["epsilon_lower"],
        record["epsilon_upper"],
        endpoint("q_slow", -1),
        endpoint("q_slow", 1),
        endpoint("q_fast", -1),
        endpoint("q_fast", 1),
        endpoint("p_slow", -1),
        endpoint("p_slow", 1),
        endpoint("period", -1),
        endpoint("period", 1),
    ]


def formal_machine_fixture(tmp_path: Path) -> dict[str, Any]:
    project = tmp_path / "formal-project"
    results = project / "results"
    results.mkdir(parents=True)
    scheduler = _copy_fixture_file(
        ROOT / R.FORMAL_MACHINE_CAPTURE_TOOL,
        project / R.FORMAL_MACHINE_CAPTURE_TOOL,
        0o644,
    )
    evaluator = _copy_fixture_file(
        ROOT / R.FORMAL_MACHINE_STATIC_EVALUATOR,
        project / R.FORMAL_MACHINE_STATIC_EVALUATOR,
        0o644,
    )
    source = _copy_fixture_file(
        ROOT / R.FORMAL_MACHINE_BRANCH_SOURCE,
        project / R.FORMAL_MACHINE_BRANCH_SOURCE,
        0o644,
    )
    binary = _copy_fixture_file(
        ROOT / R.FORMAL_MACHINE_BRANCH_BINARY,
        project / R.FORMAL_MACHINE_BRANCH_BINARY,
        0o755,
    )
    plan_path = _copy_fixture_file(
        ROOT / "research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json",
        project / "research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json",
        0o644,
    )
    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    plan_records = {record["slab_id"]: record for record in plan["slabs"]}

    external = tmp_path / "external"
    python_executable = _fixture_file(
        external / "python/bin/python3", b"fixture CPython 3.12.3\n", 0o755
    )
    conda_extra = _fixture_file(
        external / "python/lib/python3.12/fixture.py", b"# conda fixture\n", 0o644
    )
    conda_link = external / "python/bin/python-link"
    conda_link.symlink_to("python3")
    conda_files = [
        "bin/python3", "lib/python3.12/fixture.py", "bin/python-link",
    ]
    write_json(
        external / "python/conda-meta/python-3.12.3-fixture.json",
        {
            "name": "python",
            "version": "3.12.3",
            "files": conda_files,
            "paths_data": {"paths": [{"_path": path} for path in conda_files]},
        },
    )
    conda_count, conda_root = _fixture_conda_manifest(
        external / "python", conda_files
    )
    compiler_executable = _fixture_file(
        external / "compiler/bin/g++", b"fixture g++ 11.4.0\n", 0o755
    )
    live_site_packages = Path("/root/miniconda3/lib/python3.12/site-packages")
    arb_extension = live_site_packages / "flint/types/arb.abi3.so"
    fmpq_extension = live_site_packages / "flint/types/fmpq.abi3.so"
    flint_module = live_site_packages / "flint/__init__.py"
    flint_record = live_site_packages / "python_flint-0.9.0.dist-info/RECORD"
    assert all(
        path.is_file()
        for path in (arb_extension, fmpq_extension, flint_module, flint_record)
    )

    python_runtime: list[dict[str, Any]] = []
    for index, soname in enumerate(R.FORMAL_MACHINE_PYTHON_BUNDLED_SONAMES):
        path = _fixture_file(
            external / "python/runtime" / soname,
            _fixture_elf((f"{index + 1:x}" * 40)[:40], soname=soname),
            0o755,
        )
        python_runtime.append(_runtime_binding(path, soname, f"{index + 1:x}"))
    capd_runtime: list[dict[str, Any]] = []
    for index, soname in enumerate(R.FORMAL_MACHINE_CAPD_SYSTEM_SONAMES):
        path = _fixture_file(
            external / "system/runtime" / soname,
            _fixture_elf((f"{index + 8:x}" * 40)[:40], soname=soname),
            0o755,
        )
        capd_runtime.append(_runtime_binding(path, soname, f"{index + 8:x}"))
    runtime_libraries = {
        "python_bundled": python_runtime,
        "capd_system": capd_runtime,
    }

    checkout = external / "capd"
    checkout.mkdir(parents=True)
    capd_readme = _fixture_file(checkout / "README.md", b"fixture CAPD source\n")
    capd_link = checkout / "README-link"
    capd_link.symlink_to("README.md")
    capd_commit, capd_tree_root = _fixture_git_index(
        checkout,
        {
            "README-link": (0o120000, b"README.md"),
            "README.md": (0o100644, capd_readme.read_bytes()),
        },
    )
    cache = _fixture_file(
        checkout / "build-mp/CMakeCache.txt", b"fixture CMake cache\n"
    )
    config = _fixture_file(
        checkout / "build-mp/bin/capd-config", b"fixture capd-config\n", 0o755
    )
    libcapd = _fixture_file(
        checkout / "build-mp/libcapd.a", b"fixture libcapd archive\n"
    )
    libfilib = _fixture_file(
        checkout / "build-mp/capdExt/filibsrc/libfilib.a",
        b"fixture libfilib archive\n",
    )
    capd_tokens = [
        "-std=c++17", "-O2", "-frounding-math", "-D__USE_FILIB__",
        "-D__HAVE_MPFR__", "-O2", "-frounding-math", "-DFILIB_EXTENDED",
        "-DFILIB_HAVE_SSE",
        f"-I{checkout}/capdDynSys/include",
        f"-I{checkout}/capdAlg/include",
        f"-I{checkout}/capdAux/include",
        f"-I{checkout}/capdExt/include",
        f"-I{checkout}/capdExt/filibsrc",
        f"-L{checkout}/build-mp",
        f"-L{checkout}/build-mp/capdExt/filibsrc",
        "-lcapd", "-lfilib", "-lmpfr", "-lgmp",
    ]
    raw_flags = " ".join(capd_tokens) + "\n"

    python_version = R.FORMAL_MACHINE_PYTHON_VERSION
    temporary_root = tmp_path / "resource-evidence"
    static_bindings = {
        "calibration_binding": {
            "matrix_id": R.matrix_id(),
            "nonfreeze_sha256": sha(b"nonfreeze calibration fixture"),
            "nonrunconfig_sha256": sha(b"nonrunconfig calibration fixture"),
        },
        "evaluator": {
            "path": str(evaluator),
            "sha256": sha(evaluator.read_bytes()),
            "size_bytes": evaluator.stat().st_size,
            "mode": "0644",
        },
        "interpreter": {
            "invocation_path": str(python_executable),
            "resolved_path": str(python_executable),
            "sha256": sha(python_executable.read_bytes()),
            "size_bytes": python_executable.stat().st_size,
            "version": python_version,
        },
        "python_flint": {
            "version": "0.9.0",
            "flint_version": "3.6.0",
            "module_path": str(flint_module),
            "record_path": str(flint_record),
            "record_sha256": sha(flint_record.read_bytes()),
            "installed_record_file_count": 139,
            "installed_manifest_sha256": (
                R.FORMAL_MACHINE_PYTHON_FLINT_INSTALLED_MANIFEST_ROOT_SHA256
            ),
            "arb_extension_path": str(arb_extension),
            "arb_extension_sha256": sha(arb_extension.read_bytes()),
        },
        "plan": {
            "path": str(plan_path),
            "sha256": sha(plan_path.read_bytes()),
            "public_slab_ids": list(R.FORMAL_MACHINE_PUBLIC_SLABS),
        },
    }

    def static_row(
        bits: int, slab: str, replica: int, label: str, peak_kib: int
    ) -> dict[str, Any]:
        base = temporary_root / label
        row = {
            "label": label,
            "precision_bits": bits,
            "slab_id": slab,
            "replica": replica,
            "argv": [],
            "returncode": 0,
            "elapsed_seconds": 0.1,
            "peak_rss_kib": peak_kib,
            "user_cpu_seconds": 0.05,
            "system_cpu_seconds": 0.01,
            "output": str(base / "proof.json"),
            "output_bytes": 6,
            "output_sha256": sha(b"proof\n"),
            "stdout": str(base / "stdout.txt"),
            "stdout_bytes": len(b"evaluator_status=STATIC_CELL_CERTIFIED\n"),
            "stdout_sha256": sha(b"evaluator_status=STATIC_CELL_CERTIFIED\n"),
            "stdout_exact_status_line": "evaluator_status=STATIC_CELL_CERTIFIED",
            "stderr": str(base / "stderr.txt"),
            "stderr_bytes": 0,
            "stderr_sha256": sha(b""),
            "stderr_empty": True,
            "evaluator_status": "STATIC_CELL_CERTIFIED",
            "scientific_status": None,
            "component_status": None,
            "milestone_status": None,
            "theorem_status": None,
            "final_status": None,
        }
        row["argv"] = _fixture_static_argv(
            row, static_bindings, plan_records[slab]
        )
        return row

    public = [
        (bits, slab)
        for bits in R.PRECISIONS
        for slab in R.FORMAL_MACHINE_PUBLIC_SLABS
    ]
    sequential = [
        static_row(bits, slab, 0, f"{bits}_{slab}", 1_000 + index)
        for index, (bits, slab) in enumerate(public)
    ]
    stress = [*public, (256, "S025"), (256, "S050")]
    seen: dict[tuple[int, str], int] = {}
    concurrent = []
    for index, (bits, slab) in enumerate(stress):
        replica = seen.get((bits, slab), 0)
        seen[(bits, slab)] = replica + 1
        concurrent.append(
            static_row(
                bits,
                slab,
                replica,
                f"{index:02d}_{bits}_{slab}_r{replica}",
                1_100 + index,
            )
        )
    static_peak = max(
        row["peak_rss_kib"] * 1024 for row in [*sequential, *concurrent]
    )
    static_baseline_samples = [1_000_000 + index for index in range(21)]
    static_baseline = max(static_baseline_samples)
    static_concurrent_samples = [1_100_000 + index for index in range(21)]
    static_lhs = (
        static_baseline
        + R.FORMAL_MACHINE_REQUIREMENTS["static_workers"] * static_peak
        + R.FORMAL_MACHINE_REQUIREMENTS["reserve_bytes"]
    )
    static_payload = {
        "schema_version": 1,
        "protocol_id": R.PROTOCOL_ID,
        "artifact_role": "TEMP_PUBLIC_STATIC_RSS_CALIBRATION",
        "scope": "PUBLIC_S0_RESOURCE_CALIBRATION_ONLY",
        "production_authorized": False,
        "scientific_licensing_enabled": False,
        "claim_boundary": (
            "resource telemetry on already-public S000/S025/S050 at 128/256 only; "
            "no held-out/all-slab evaluation, no freeze, no scientific promotion"
        ),
        "project_root": str(project),
        "temporary_root": str(temporary_root),
        "execution_environment": {
            "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8", "TZ": "UTC",
            "PYTHONHASHSEED": "0", "PYTHONNOUSERSITE": "1",
            "PYTHONDONTWRITEBYTECODE": "1", "OMP_NUM_THREADS": "1",
            "OPENBLAS_NUM_THREADS": "1", "MKL_NUM_THREADS": "1",
            "NUMEXPR_NUM_THREADS": "1",
        },
        "bindings": static_bindings,
        "measurement": {
            "method": "os.wait4(pid,0/WNOHANG).rusage.ru_maxrss on Linux",
            "ru_maxrss_unit": "KiB",
            "bytes_per_kib": 1024,
            "cgroup_usage_path": "/sys/fs/cgroup/memory/memory.usage_in_bytes",
            "cgroup_limit_path": "/sys/fs/cgroup/memory/memory.limit_in_bytes",
            "cgroup_limit_bytes": R.FORMAL_MACHINE_REQUIREMENTS["memory_limit_bytes"],
            "baseline_samples_bytes": static_baseline_samples,
            "baseline_conservative_bytes": static_baseline,
            "concurrent_samples_bytes": static_concurrent_samples,
            "concurrent_peak_bytes": max(static_concurrent_samples),
            "sample_interval_seconds": 0.05,
        },
        "sequential_runs": sequential,
        "concurrent_schedule": [
            {"precision_bits": bits, "slab_id": slab} for bits, slab in stress
        ],
        "concurrent_runs": concurrent,
        "admission": {
            "workers": 8,
            "representative_peak_rss_bytes": static_peak,
            "idle_baseline_bytes": static_baseline,
            "reserve_bytes": R.FORMAL_MACHINE_REQUIREMENTS["reserve_bytes"],
            "admission_limit_bytes": R.FORMAL_MACHINE_REQUIREMENTS[
                "memory_admission_limit_bytes"
            ],
            "lhs_bytes": static_lhs,
            "headroom_bytes": R.FORMAL_MACHINE_REQUIREMENTS[
                "memory_admission_limit_bytes"
            ] - static_lhs,
            "formula": "idle_baseline_bytes + workers * representative_peak_rss_bytes + reserve_bytes <= admission_limit_bytes",
            "passes": True,
        },
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    static_raw = R.canonical_json_bytes(static_payload)

    discarded_binary = str(temporary_root / "branch-calibration-binary")
    branch_results = []
    for index, (bits, slab) in enumerate(public):
        argv = _fixture_branch_argv(discarded_binary, bits, plan_records[slab])
        branch_results.append({
            "precision_bits": bits,
            "slab_id": slab,
            "argv": argv,
            "argv_count": 12,
            "returncode": 0,
            "elapsed_seconds": 0.2,
            "peak_rss_kib": 2_000 + index,
            "user_cpu_seconds": 0.1,
            "system_cpu_seconds": 0.02,
            "stdout_bytes": 10,
            "stdout_sha256": sha(f"stdout-{index}".encode("ascii")),
            "stderr_bytes": 0,
            "stderr_sha256": sha(b""),
            "abi_verified": True,
            "terminal_abi_value": "BRANCH_CELL_CERTIFIED",
        })
    branch_peak = max(row["peak_rss_kib"] * 1024 for row in branch_results)
    branch_baseline_samples = [1_200_000 + index for index in range(21)]
    branch_baseline = max(branch_baseline_samples)
    branch_post_samples = [1_100_000 + index for index in range(21)]
    branch_lhs = (
        branch_baseline
        + R.FORMAL_MACHINE_REQUIREMENTS["branch_workers"] * branch_peak
        + R.FORMAL_MACHINE_REQUIREMENTS["reserve_bytes"]
    )
    branch_payload = {
        "scope": "REPRESENTATIVE_S0_CALIBRATION_ONLY",
        "binary": discarded_binary,
        "binary_sha256": sha(binary.read_bytes()),
        "cgroup_limit_bytes": R.FORMAL_MACHINE_REQUIREMENTS["memory_limit_bytes"],
        "baseline_samples_bytes": branch_baseline_samples,
        "baseline_conservative_bytes": branch_baseline,
        "post_samples_bytes": branch_post_samples,
        "results": branch_results,
        "task_count": 6,
        "per_process_peak_rss_max_kib": branch_peak // 1024,
        "sampled_concurrent_peak_bytes": branch_baseline + 5_000_000,
        "sampled_concurrent_increment_bytes": 5_000_000,
        "admission": {
            "baseline_bytes": branch_baseline,
            "peak_rss_bytes": branch_peak,
            "workers": 6,
            "reserve_bytes": R.FORMAL_MACHINE_REQUIREMENTS["reserve_bytes"],
            "limit_bytes": R.FORMAL_MACHINE_REQUIREMENTS[
                "memory_admission_limit_bytes"
            ],
            "lhs_bytes": branch_lhs,
            "headroom_bytes": R.FORMAL_MACHINE_REQUIREMENTS[
                "memory_admission_limit_bytes"
            ] - branch_lhs,
            "formula": "baseline + 6*peak_rss + 8GiB <= 48GiB",
            "passes": True,
        },
        "scientific_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    branch_raw = R.branch_transaction_json_bytes(branch_payload)

    build_template = [
        str(compiler_executable),
        "-Wall", "-Wextra", "-Wpedantic", "-Werror",
        str(source),
        *capd_tokens,
        "-o", R.FORMAL_MACHINE_STAGING_OUTPUT_TOKEN,
    ]
    staging_directory = Path("/tmp") / (
        "r401-val-l3-a1-fresh-fixture-"
        + sha(str(tmp_path).encode("utf-8"))[:16]
    )
    staging_output = staging_directory / binary.name
    fresh_argv = [*build_template[:-1], str(staging_output)]
    binary_info = binary.stat()
    binary_sha = sha(binary.read_bytes())
    binary_build_id, binary_dt_needed, binary_soname = R._machine_elf_metadata(
        binary.read_bytes(), "fixture branch binary"
    )
    runtime_root = sha(R.canonical_json_bytes(runtime_libraries))
    free_bytes = 300 * 1024**3
    baseline = max(static_baseline, branch_baseline)
    static_required = (
        baseline
        + R.FORMAL_MACHINE_REQUIREMENTS["static_workers"] * static_peak
        + R.FORMAL_MACHINE_REQUIREMENTS["reserve_bytes"]
    )
    branch_required = (
        baseline
        + R.FORMAL_MACHINE_REQUIREMENTS["branch_workers"] * branch_peak
        + R.FORMAL_MACHINE_REQUIREMENTS["reserve_bytes"]
    )
    device_id = project.stat().st_dev
    machine = {
        "schema_version": 1,
        "protocol_id": R.PROTOCOL_ID,
        "artifact_role": "MACHINE_FREEZE",
        "status": "FROZEN_FOR_PRODUCTION",
        "authority": "MACHINE_ADMISSION_ONLY",
        "scientific_licensing_enabled": True,
        "production_authorized": False,
        "capture": {
            "captured_at_utc": datetime.now(timezone.utc).strftime(
                "%Y-%m-%dT%H:%M:%SZ"
            ),
            "capture_tool_path": R.FORMAL_MACHINE_CAPTURE_TOOL,
            "capture_tool_sha256": sha(scheduler.read_bytes()),
            "boot_id_sha256": sha(Path("/proc/sys/kernel/random/boot_id").read_bytes()),
        },
        "machine_requirements": copy.deepcopy(R.FORMAL_MACHINE_REQUIREMENTS),
        "machine_observations": {
            "logical_cpu_count": R.FORMAL_MACHINE_REQUIREMENTS["logical_cpu_count"],
            "memory_limit_bytes": R.FORMAL_MACHINE_REQUIREMENTS["memory_limit_bytes"],
            "result_parent_free_bytes": free_bytes,
            "idle_baseline_rss_bytes": baseline,
            "representative_static_peak_rss_bytes": static_peak,
            "representative_branch_peak_rss_bytes": branch_peak,
        },
        "python_arb": {
            "executable_path": str(python_executable),
            "executable_sha256": sha(python_executable.read_bytes()),
            "python_version": python_version,
            "implementation": "CPython",
            "python_flint_version": "0.9.0",
            "flint_version": "3.6.0",
            "arb_version": "FLINT-3.6.0",
            "conda_manifest_algorithm": R.FORMAL_MACHINE_CONDA_MANIFEST_ALGORITHM,
            "conda_manifest_file_count": conda_count,
            "conda_installed_manifest_root_sha256": conda_root,
            "python_flint_record_sha256": (
                R.FORMAL_MACHINE_PYTHON_FLINT_RECORD_SHA256
            ),
            "python_flint_installed_manifest_root_sha256": (
                R.FORMAL_MACHINE_PYTHON_FLINT_INSTALLED_MANIFEST_ROOT_SHA256
            ),
            "arb_extension": _live_binding(
                arb_extension,
                R._machine_elf_metadata(
                    arb_extension.read_bytes(), "fixture Arb extension"
                )[0],
            ),
            "fmpq_extension": _live_binding(
                fmpq_extension,
                R._machine_elf_metadata(
                    fmpq_extension.read_bytes(), "fixture fmpq extension"
                )[0],
            ),
            "bundled_libraries": copy.deepcopy(python_runtime),
        },
        "capd": {
            "checkout_path": str(checkout),
            "commit": capd_commit,
            "tree_algorithm": R.FORMAL_MACHINE_CAPD_TREE_ALGORITHM,
            "tree_sha256": capd_tree_root,
            "clean": True,
            "cmake_cache_path": str(cache),
            "cmake_cache_sha256": sha(cache.read_bytes()),
            "config_path": str(config),
            "config_sha256": sha(config.read_bytes()),
            "raw_flags": raw_flags,
            "raw_flags_sha256": sha(raw_flags.encode("utf-8")),
            "libcapd": _live_binding(libcapd, None),
            "libfilib": _live_binding(libfilib, None),
        },
        "compiler": {
            "executable_path": str(compiler_executable),
            "executable_sha256": sha(compiler_executable.read_bytes()),
            "version": R.FORMAL_MACHINE_COMPILER_VERSION,
            "build_recipe": {
                "cwd": str(project),
                "environment": copy.deepcopy(R.FORMAL_MACHINE_BUILD_ENVIRONMENT),
                "umask": "0022",
                "staging_output_token": R.FORMAL_MACHINE_STAGING_OUTPUT_TOKEN,
                "argv_template": build_template,
                "argv_template_sha256": sha(
                    R.canonical_json_bytes(build_template)
                ),
            },
            "fresh_rebuild_receipt": {
                "cwd": str(project),
                "environment": copy.deepcopy(R.FORMAL_MACHINE_BUILD_ENVIRONMENT),
                "umask": "0022",
                "staging_directory": str(staging_directory),
                "staging_output_path": str(staging_output),
                "argv": fresh_argv,
                "argv_sha256": sha(R.canonical_json_bytes(fresh_argv)),
                "stdout_sha256": sha(b""),
                "stderr_sha256": sha(b""),
                "stdout": "",
                "stderr": "",
                "return_code": 0,
                "shell_used": False,
                "output_sha256": binary_sha,
                "output_size_bytes": binary_info.st_size,
                "output_mode": stat.S_IMODE(binary_info.st_mode),
                "output_build_id": binary_build_id,
                "output_dt_needed": binary_dt_needed,
                "output_dt_needed_sha256": sha(
                    R.canonical_json_bytes(binary_dt_needed)
                ),
                "output_soname": binary_soname,
            },
            "transfer_evidence": {
                "staging_output_sha256": binary_sha,
                "staging_output_size_bytes": binary_info.st_size,
                "staging_output_mode": stat.S_IMODE(binary_info.st_mode),
                "branch_calibration_binary_sha256": binary_sha,
                "persistent_before_sha256": binary_sha,
                "persistent_before_size_bytes": binary_info.st_size,
                "persistent_before_mode": stat.S_IMODE(binary_info.st_mode),
                "persistent_before_device_id": binary_info.st_dev,
                "persistent_before_inode": binary_info.st_ino,
                "persistent_after_sha256": binary_sha,
                "persistent_after_size_bytes": binary_info.st_size,
                "persistent_after_mode": stat.S_IMODE(binary_info.st_mode),
                "persistent_after_device_id": binary_info.st_dev,
                "persistent_after_inode": binary_info.st_ino,
                "byte_for_byte_equal": True,
                "persistent_identity_unchanged": True,
                "persistent_overwrite_performed": False,
            },
        },
        "branch_binary": {
            "path": R.FORMAL_MACHINE_BRANCH_BINARY,
            "sha256": binary_sha,
            "size_bytes": binary_info.st_size,
            "executable_mode": 0o755,
            "build_id": binary_build_id,
            "source_path": R.FORMAL_MACHINE_BRANCH_SOURCE,
            "source_sha256": sha(source.read_bytes()),
            "elf_sha256": binary_sha,
            "dt_needed": list(R.FORMAL_MACHINE_DT_NEEDED),
            "dt_needed_sha256": sha(
                R.canonical_json_bytes(list(R.FORMAL_MACHINE_DT_NEEDED))
            ),
            "runtime_libraries_sha256": runtime_root,
        },
        "runtime_libraries": runtime_libraries,
        "resource_evidence": {
            "static_payload_raw_utf8": static_raw.decode("utf-8"),
            "static_payload_sha256": sha(static_raw),
            "branch_payload_raw_utf8": branch_raw.decode("utf-8"),
            "branch_payload_sha256": sha(branch_raw),
            "persistent_binary_sha256": sha(binary.read_bytes()),
        },
        "resource_admission": {
            "static_required_bytes": static_required,
            "branch_required_bytes": branch_required,
            "admitted_required_bytes": max(static_required, branch_required),
            "admission_limit_bytes": R.FORMAL_MACHINE_REQUIREMENTS[
                "memory_admission_limit_bytes"
            ],
            "static_inequality_passed": True,
            "branch_inequality_passed": True,
            "storage_launch_passed": free_bytes
            >= R.FORMAL_MACHINE_REQUIREMENTS["launch_free_bytes"],
        },
        "filesystem": {
            "project_root": str(project),
            "result_parent": str(results),
            "operational_parent": str(results),
            "project_device_id": device_id,
            "result_device_id": device_id,
            "operational_device_id": device_id,
            "same_filesystem": True,
        },
        "claim_boundary": R.FORMAL_MACHINE_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    machine_path = project / "research/route_a_wave_trace/R401_VAL_L3_A1_MACHINE_FREEZE.json"
    write_json(machine_path, machine)
    role_hashes = {
        "scheduler": sha(scheduler.read_bytes()),
        "static_evaluator": sha(evaluator.read_bytes()),
        "branch_evaluator_source": sha(source.read_bytes()),
        "branch_evaluator_binary": sha(binary.read_bytes()),
        "l1_final_plan": sha(plan_path.read_bytes()),
    }
    return {
        "project": project,
        "machine": machine,
        "machine_path": machine_path,
        "roles": role_hashes,
        "external": external,
        "binary": binary,
        "source": source,
        "python_executable": python_executable,
    }


def _publish_formal_machine(fixture: dict[str, Any]) -> None:
    write_json(fixture["machine_path"], fixture["machine"])


def _replace_static_resource(
    fixture: dict[str, Any], payload: dict[str, Any], *, pretty: bool = False
) -> None:
    raw = (
        R.branch_transaction_json_bytes(payload)
        if pretty
        else R.canonical_json_bytes(payload)
    )
    evidence = fixture["machine"]["resource_evidence"]
    evidence["static_payload_raw_utf8"] = raw.decode("utf-8")
    evidence["static_payload_sha256"] = sha(raw)
    _publish_formal_machine(fixture)


def _replace_branch_resource(
    fixture: dict[str, Any], payload: dict[str, Any], *, compact: bool = False
) -> None:
    raw = R.canonical_json_bytes(payload) if compact else R.branch_transaction_json_bytes(payload)
    evidence = fixture["machine"]["resource_evidence"]
    evidence["branch_payload_raw_utf8"] = raw.decode("utf-8")
    evidence["branch_payload_sha256"] = sha(raw)
    _publish_formal_machine(fixture)


_DEFAULT_ROLES = object()


def _validate_machine_fixture(
    fixture: dict[str, Any], role_hashes: Any = _DEFAULT_ROLES
) -> Any:
    """Replay the 300-GiB machine gate although pytest's /tmp is an overlay."""

    original_statvfs = R.os.statvfs

    def fixture_statvfs(path: Any):
        observed = original_statvfs(path)
        values = list(observed)
        values[4] = max(values[4], (300 * 1024**3) // observed.f_frsize)
        return os.statvfs_result(values)

    R.os.statvfs = fixture_statvfs
    try:
        roles = fixture["roles"] if role_hashes is _DEFAULT_ROLES else role_hashes
        return R.validate_formal_machine_freeze(
            fixture["project"],
            machine_path=fixture["machine_path"],
            expected_role_hashes=roles,
        )
    finally:
        R.os.statvfs = original_statvfs


def _patch_machine_verify_environment(
    fixture: dict[str, Any], monkeypatch: pytest.MonkeyPatch
) -> None:
    """Point the one-argument verifier at a complete temporary paper root."""

    original_statvfs = R.os.statvfs

    def fixture_statvfs(path: Any):
        observed = original_statvfs(path)
        values = list(observed)
        values[4] = max(values[4], (300 * 1024**3) // observed.f_frsize)
        return os.statvfs_result(values)

    monkeypatch.setattr(R, "ROOT", fixture["project"])
    monkeypatch.setattr(R.os, "statvfs", fixture_statvfs)


def _read_only_tree_snapshot(root: Path) -> list[tuple[Any, ...]]:
    rows: list[tuple[Any, ...]] = []
    for path in sorted(root.rglob("*"), key=lambda item: item.as_posix()):
        info = path.lstat()
        relative = path.relative_to(root).as_posix()
        if path.is_symlink():
            content: Any = ("symlink", os.readlink(path))
        elif path.is_file():
            content = ("file", sha(path.read_bytes()))
        else:
            content = ("directory", None)
        rows.append(
            (
                relative,
                stat.S_IFMT(info.st_mode),
                stat.S_IMODE(info.st_mode),
                info.st_dev,
                info.st_ino,
                info.st_nlink,
                info.st_size,
                info.st_mtime_ns,
                info.st_ctime_ns,
                content,
            )
        )
    return rows


def test_verify_machine_path_accepts_temp_candidate_without_authority(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    fixture = formal_machine_fixture(tmp_path)
    candidate = tmp_path / "prospective-machine-freeze.json"
    fixture["machine_path"].rename(candidate)
    fixture["machine_path"] = candidate
    _patch_machine_verify_environment(fixture, monkeypatch)

    before = (
        candidate.read_bytes(),
        candidate.stat().st_ino,
        candidate.stat().st_mtime_ns,
    )
    result = R.verify_formal_machine_freeze_path(str(candidate))

    assert result == {
        "verification_status": R.FORMAL_MACHINE_VERIFY_STATUS,
        "authority": R.FORMAL_MACHINE_VERIFY_AUTHORITY,
        "claim_boundary": R.FORMAL_MACHINE_VERIFY_CLAIM_BOUNDARY,
        "candidate_sha256": sha(before[0]),
        "size_bytes": len(before[0]),
        "promotion_authorized": False,
        "release_artifacts_written": False,
    }
    assert "machine_freeze_sha256" not in fixture["machine"]
    assert "machine_freeze_sha256" not in result
    assert (
        candidate.read_bytes(),
        candidate.stat().st_ino,
        candidate.stat().st_mtime_ns,
    ) == before
    assert list((fixture["project"] / "results").iterdir()) == []


def test_verify_machine_cli_emits_one_non_authoritative_line(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    fixture = formal_machine_fixture(tmp_path)
    _patch_machine_verify_environment(fixture, monkeypatch)
    raw = fixture["machine_path"].read_bytes()

    assert R.main(["--verify-machine-freeze", str(fixture["machine_path"])]) == 0
    captured = capsys.readouterr()
    assert captured.err == ""
    assert captured.out == (
        "machine_freeze_verification=PASS_MACHINE_FREEZE_VERIFY_ONLY "
        "authority=NON_AUTHORITATIVE_VERIFY_ONLY "
        f"candidate_sha256={sha(raw)} size_bytes={len(raw)} "
        "promotion_authorized=false\n"
    )
    assert list((fixture["project"] / "results").iterdir()) == []


def test_verify_machine_cli_does_not_change_mock_verify_only_behavior(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    project = release_fixture(tmp_path)
    released = R.build_release(project)
    release = project / R.RESULT_RELATIVE / R.RELEASE_NAME
    before = (release.read_bytes(), release.stat().st_ino, release.stat().st_mtime_ns)

    assert R.main(["--project-root", str(project), "--verify-only"]) == 0
    captured = capsys.readouterr()
    assert captured.err == ""
    assert captured.out == (
        f"release_status={released['release_status']} roles=68 "
        "scientific_licensing_enabled=false\n"
    )
    assert (
        release.read_bytes(),
        release.stat().st_ino,
        release.stat().st_mtime_ns,
    ) == before


@pytest.mark.parametrize(
    "value",
    [
        "candidate.json",
        "",
        "//tmp/candidate.json",
        "/tmp//candidate.json",
        "/tmp/./candidate.json",
        "/tmp/../candidate.json",
        "/tmp/candidate.json/",
        "/tmp/candidate\\name.json",
    ],
)
def test_verify_machine_path_rejects_relative_or_noncanonical_text(value: str) -> None:
    with pytest.raises(R.PathContractError, match="path|absolute|unsafe|noncanonical"):
        R.verify_formal_machine_freeze_path(value)


@pytest.mark.parametrize("value", [None, 7, b"/tmp/candidate.json", [], {}])
def test_verify_machine_path_rejects_non_path_types(value: Any) -> None:
    with pytest.raises(R.PathContractError, match="string or pathlib.Path"):
        R.verify_formal_machine_freeze_path(value)


def test_verify_machine_path_never_accepts_a_caller_supplied_digest() -> None:
    with pytest.raises(TypeError, match="unexpected keyword"):
        R.verify_formal_machine_freeze_path(
            "/tmp/prospective-machine-freeze.json",
            expected_sha256="0" * 64,
        )


@pytest.mark.parametrize("variant", ["duplicate", "noncanonical"])
def test_verify_machine_path_rejects_duplicate_or_noncanonical_json(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    variant: str,
) -> None:
    fixture = formal_machine_fixture(tmp_path)
    if variant == "duplicate":
        fixture["machine_path"].write_bytes(
            b'{"schema_version":1,"schema_version":1}\n'
        )
        expected = "duplicate"
    else:
        fixture["machine_path"].write_text(
            json.dumps(fixture["machine"], indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        expected = "not canonical"
    _patch_machine_verify_environment(fixture, monkeypatch)
    with pytest.raises(R.StrictJSONError, match=expected):
        R.verify_formal_machine_freeze_path(fixture["machine_path"])


@pytest.mark.parametrize("alias_kind", ["symlink", "hardlink"])
def test_verify_machine_path_rejects_symlink_and_hardlink_aliases(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    alias_kind: str,
) -> None:
    fixture = formal_machine_fixture(tmp_path)
    path = fixture["machine_path"]
    saved = path.with_name("saved-machine-freeze.json")
    path.rename(saved)
    if alias_kind == "symlink":
        path.symlink_to(saved)
    else:
        os.link(saved, path)
    _patch_machine_verify_environment(fixture, monkeypatch)
    with pytest.raises((R.PathContractError, OSError), match="regular|link|alias|loop"):
        R.verify_formal_machine_freeze_path(path)


def test_verify_machine_path_rejects_terminal_inode_toctou(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    fixture = formal_machine_fixture(tmp_path)
    path = fixture["machine_path"]
    _patch_machine_verify_environment(fixture, monkeypatch)
    original = R._validate_formal_machine_freeze

    def validate_then_replace(*args: Any, **kwargs: Any):
        result = original(*args, **kwargs)
        saved = path.with_name("validated-but-replaced-machine-freeze.json")
        path.rename(saved)
        write_json(path, fixture["machine"])
        return result

    monkeypatch.setattr(R, "_validate_formal_machine_freeze", validate_then_replace)
    with pytest.raises(R.PathContractError, match="namespace changed|input changed"):
        R.verify_formal_machine_freeze_path(path)


def test_verify_machine_path_rejects_parent_namespace_toctou(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    fixture = formal_machine_fixture(tmp_path)
    parent = tmp_path / "prospective-parent"
    parent.mkdir()
    path = parent / "machine-freeze.json"
    fixture["machine_path"].rename(path)
    fixture["machine_path"] = path
    _patch_machine_verify_environment(fixture, monkeypatch)
    original = R._validate_formal_machine_freeze

    def validate_then_replace_parent(*args: Any, **kwargs: Any):
        result = original(*args, **kwargs)
        saved_parent = tmp_path / "replaced-prospective-parent"
        parent.rename(saved_parent)
        parent.mkdir()
        (saved_parent / path.name).rename(path)
        return result

    monkeypatch.setattr(
        R, "_validate_formal_machine_freeze", validate_then_replace_parent
    )
    with pytest.raises(R.PathContractError, match="namespace changed"):
        R.verify_formal_machine_freeze_path(path)


def test_verify_machine_path_has_no_write_side_effects(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    fixture = formal_machine_fixture(tmp_path)
    _patch_machine_verify_environment(fixture, monkeypatch)
    project_before = _read_only_tree_snapshot(fixture["project"])
    external_before = _read_only_tree_snapshot(fixture["external"])
    freeze_before = fixture["machine_path"].read_bytes()
    original_open = R.os.open
    write_flags = (
        os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND
    )

    def reject_write_open(path: Any, flags: int, *args: Any, **kwargs: Any):
        if flags & write_flags:
            raise AssertionError(f"verify-only attempted writable os.open: {path}")
        return original_open(path, flags, *args, **kwargs)

    def reject_release_write(*args: Any, **kwargs: Any) -> None:
        raise AssertionError("verify-only called release publication")

    monkeypatch.setattr(R.os, "open", reject_write_open)
    monkeypatch.setattr(R, "write_once", reject_release_write)
    result = R.verify_formal_machine_freeze_path(fixture["machine_path"])

    assert result["release_artifacts_written"] is False
    assert fixture["machine_path"].read_bytes() == freeze_before
    assert _read_only_tree_snapshot(fixture["project"]) == project_before
    assert _read_only_tree_snapshot(fixture["external"]) == external_before
    assert list((fixture["project"] / "results").iterdir()) == []


@pytest.mark.parametrize(
    "attack",
    (
        "recipe-direct-to-canonical",
        "receipt-direct-to-canonical",
        "staging-persistent-mismatch",
        "shell-enabled-receipt",
        "shell-integer-alias",
        "missing-recipe-environment",
        "missing-receipt-environment",
        "missing-receipt",
    ),
)
def test_verify_machine_path_rejects_false_fresh_build_receipts(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    attack: str,
) -> None:
    fixture = formal_machine_fixture(tmp_path)
    compiler = fixture["machine"]["compiler"]
    persistent = fixture["binary"]
    if attack == "recipe-direct-to-canonical":
        recipe = compiler["build_recipe"]
        recipe["staging_output_token"] = str(persistent)
        recipe["argv_template"][-1] = str(persistent)
        recipe["argv_template_sha256"] = sha(
            R.canonical_json_bytes(recipe["argv_template"])
        )
    elif attack == "receipt-direct-to-canonical":
        receipt = compiler["fresh_rebuild_receipt"]
        receipt["staging_directory"] = str(persistent.parent)
        receipt["staging_output_path"] = str(persistent)
        receipt["argv"][-1] = str(persistent)
        receipt["argv_sha256"] = sha(R.canonical_json_bytes(receipt["argv"]))
    elif attack == "staging-persistent-mismatch":
        forged = "f" * 64
        compiler["fresh_rebuild_receipt"]["output_sha256"] = forged
        compiler["transfer_evidence"]["staging_output_sha256"] = forged
    elif attack == "shell-enabled-receipt":
        compiler["fresh_rebuild_receipt"]["shell_used"] = True
    elif attack == "shell-integer-alias":
        compiler["fresh_rebuild_receipt"]["shell_used"] = 0
    elif attack == "missing-recipe-environment":
        del compiler["build_recipe"]["environment"]["PYTHONHASHSEED"]
    elif attack == "missing-receipt-environment":
        del compiler["fresh_rebuild_receipt"]["environment"]["PATH"]
    else:
        del compiler["fresh_rebuild_receipt"]
    _publish_formal_machine(fixture)
    _patch_machine_verify_environment(fixture, monkeypatch)

    with pytest.raises((R.ReleaseError, R.StrictJSONError, R.PathContractError)):
        R.verify_formal_machine_freeze_path(fixture["machine_path"])


def test_independent_formal_machine_validator_accepts_exact_temp_fixture(
    tmp_path: Path,
) -> None:
    fixture = formal_machine_fixture(tmp_path)
    before = fixture["machine_path"].read_bytes()
    validated = _validate_machine_fixture(fixture)
    assert validated["authority"] == "MACHINE_ADMISSION_ONLY"
    assert validated["production_authorized"] is False
    assert all(
        validated[key] is None
        for key in ("component_status", "milestone_status", "theorem_status", "final_status")
    )
    assert fixture["machine_path"].read_bytes() == before
    assert list((fixture["project"] / "results").iterdir()) == []


def test_formal_machine_requires_all_frozen_cross_bindings(tmp_path: Path) -> None:
    fixture = formal_machine_fixture(tmp_path)
    with pytest.raises(R.ReleaseError, match="requires frozen role hashes"):
        _validate_machine_fixture(fixture, None)
    fixture["roles"]["l1_final_plan"] = "0" * 64
    with pytest.raises(R.ReleaseError, match="l1_final_plan.*cross-binding"):
        _validate_machine_fixture(fixture)


@pytest.mark.parametrize(
    "domain",
    ("arithmetic", "mode-alias", "status", "extra-key", "build-bool"),
)
def test_formal_machine_rejects_nested_schema_authority_and_type_attacks(
    tmp_path: Path, domain: str
) -> None:
    fixture = formal_machine_fixture(tmp_path)
    machine = fixture["machine"]
    if domain == "arithmetic":
        machine["resource_admission"]["static_required_bytes"] += 1
    elif domain == "mode-alias":
        machine["python_arb"]["arb_extension"]["mode"] = "0755"
    elif domain == "status":
        machine["theorem_status"] = "RH_PROVED"
    elif domain == "extra-key":
        machine["resource_evidence"]["evidence_path"] = "/tmp/forged.json"
    else:
        machine["compiler"]["fresh_rebuild_receipt"]["return_code"] = False
    _publish_formal_machine(fixture)
    with pytest.raises((R.ReleaseError, R.StrictJSONError)):
        _validate_machine_fixture(fixture)


@pytest.mark.parametrize(
    "domain",
    (
        "binary-size",
        "static-evaluator-size",
        "static-interpreter-size",
        "static-flint-count",
        "static-measurement",
        "static-admission",
        "branch-top",
        "branch-admission",
    ),
)
def test_formal_machine_rejects_coherent_integral_float_aliases(
    tmp_path: Path, domain: str
) -> None:
    fixture = formal_machine_fixture(tmp_path)
    if domain == "binary-size":
        binding = fixture["machine"]["branch_binary"]
        binding["size_bytes"] = float(binding["size_bytes"])
        _publish_formal_machine(fixture)
    elif domain.startswith("static-"):
        payload = json.loads(
            fixture["machine"]["resource_evidence"]["static_payload_raw_utf8"]
        )
        if domain == "static-evaluator-size":
            target = payload["bindings"]["evaluator"]
            key = "size_bytes"
        elif domain == "static-interpreter-size":
            target = payload["bindings"]["interpreter"]
            key = "size_bytes"
        elif domain == "static-flint-count":
            target = payload["bindings"]["python_flint"]
            key = "installed_record_file_count"
        elif domain == "static-measurement":
            target = payload["measurement"]
            key = "cgroup_limit_bytes"
        else:
            target = payload["admission"]
            key = "lhs_bytes"
        target[key] = float(target[key])
        _replace_static_resource(fixture, payload)
    else:
        payload = json.loads(
            fixture["machine"]["resource_evidence"]["branch_payload_raw_utf8"]
        )
        target = payload if domain == "branch-top" else payload["admission"]
        key = "task_count" if domain == "branch-top" else "lhs_bytes"
        target[key] = float(target[key])
        _replace_branch_resource(fixture, payload)
    with pytest.raises(R.ReleaseError, match="exact integer"):
        _validate_machine_fixture(fixture)


def test_formal_machine_rejects_static_noncanonical_and_heldout_receipts(
    tmp_path: Path,
) -> None:
    fixture = formal_machine_fixture(tmp_path)
    static = json.loads(
        fixture["machine"]["resource_evidence"]["static_payload_raw_utf8"]
    )
    _replace_static_resource(fixture, static, pretty=True)
    with pytest.raises(R.StrictJSONError, match="not canonical"):
        _validate_machine_fixture(fixture)

    fixture = formal_machine_fixture(tmp_path / "heldout")
    static = json.loads(
        fixture["machine"]["resource_evidence"]["static_payload_raw_utf8"]
    )
    static["sequential_runs"][0]["slab_id"] = "S051"
    _replace_static_resource(fixture, static)
    with pytest.raises(R.ReleaseError, match="identity/order|public"):
        _validate_machine_fixture(fixture)


def test_formal_machine_rejects_branch_nonpretty_and_abi_receipts(
    tmp_path: Path,
) -> None:
    fixture = formal_machine_fixture(tmp_path)
    branch = json.loads(
        fixture["machine"]["resource_evidence"]["branch_payload_raw_utf8"]
    )
    _replace_branch_resource(fixture, branch, compact=True)
    with pytest.raises(R.StrictJSONError, match="pretty"):
        _validate_machine_fixture(fixture)

    fixture = formal_machine_fixture(tmp_path / "abi")
    branch = json.loads(
        fixture["machine"]["resource_evidence"]["branch_payload_raw_utf8"]
    )
    branch["results"][0]["terminal_abi_value"] = "FORGED"
    _replace_branch_resource(fixture, branch)
    with pytest.raises(R.ReleaseError, match="ABI"):
        _validate_machine_fixture(fixture)


@pytest.mark.parametrize("target", ("binary", "source", "runtime"))
def test_formal_machine_rejects_live_bound_byte_mutation(
    tmp_path: Path, target: str
) -> None:
    fixture = formal_machine_fixture(tmp_path)
    if target == "binary":
        path = fixture["binary"]
    elif target == "source":
        path = fixture["source"]
    else:
        path = Path(
            fixture["machine"]["runtime_libraries"]["capd_system"][0]["path"]
        )
    path.write_bytes(path.read_bytes() + b"late mutation\n")
    if target == "binary":
        path.chmod(0o755)
    with pytest.raises(R.ReleaseError, match="live bytes|metadata|size"):
        _validate_machine_fixture(fixture)


def test_formal_machine_rejects_project_symlink_and_hardlink_aliases(
    tmp_path: Path,
) -> None:
    fixture = formal_machine_fixture(tmp_path)
    saved_source = fixture["source"].with_name("saved-source.cpp")
    fixture["source"].rename(saved_source)
    fixture["source"].symlink_to(saved_source)
    with pytest.raises((R.PathContractError, OSError)):
        _validate_machine_fixture(fixture)

    fixture = formal_machine_fixture(tmp_path / "hardlink")
    os.link(fixture["binary"], fixture["binary"].with_name("binary-alias"))
    with pytest.raises(R.PathContractError, match="hard-link"):
        _validate_machine_fixture(fixture)


def test_formal_machine_replays_external_symlink_at_transaction_end(
    tmp_path: Path, monkeypatch
) -> None:
    fixture = formal_machine_fixture(tmp_path)
    old_compiler = fixture["python_executable"]
    first = old_compiler.with_name("python-target-a")
    second = old_compiler.with_name("python-target-b")
    raw = old_compiler.read_bytes()
    old_compiler.rename(first)
    _fixture_file(second, raw, 0o755)
    old_compiler.symlink_to(first)
    machine = fixture["machine"]
    machine["python_arb"]["executable_path"] = str(old_compiler)
    conda_count, conda_root = R._machine_recompute_conda_manifest(str(old_compiler))
    machine["python_arb"]["conda_manifest_file_count"] = conda_count
    machine["python_arb"]["conda_installed_manifest_root_sha256"] = conda_root
    static = json.loads(machine["resource_evidence"]["static_payload_raw_utf8"])
    static["bindings"]["interpreter"]["invocation_path"] = str(old_compiler)
    static["bindings"]["interpreter"]["resolved_path"] = str(first)
    for row in [*static["sequential_runs"], *static["concurrent_runs"]]:
        row["argv"][0] = str(old_compiler)
    _replace_static_resource(fixture, static)

    original = R._machine_validate_filesystem

    def validate_then_swap(project: Path, payload: dict[str, Any]) -> None:
        original(project, payload)
        old_compiler.unlink()
        old_compiler.symlink_to(second)

    monkeypatch.setattr(R, "_machine_validate_filesystem", validate_then_swap)
    with pytest.raises(R.PathContractError, match="external machine path changed"):
        _validate_machine_fixture(fixture)


@pytest.mark.parametrize(
    "payload",
    (
        ("tuple",),
        {1: "non-string-key"},
    ),
)
def test_canonical_serializers_reject_non_plain_python_aliases(payload: Any) -> None:
    with pytest.raises(R.StrictJSONError, match="non-plain|non-string"):
        R.canonical_json_bytes(payload)
    with pytest.raises(R.StrictJSONError, match="non-plain|non-string"):
        R.branch_transaction_json_bytes(payload)


def test_canonical_serializers_reject_subclasses_nonfinite_and_cycles() -> None:
    class DictAlias(dict):
        pass

    class ListAlias(list):
        pass

    cycle: list[Any] = []
    cycle.append(cycle)
    attacks: list[Any] = [
        DictAlias({"key": "value"}),
        ListAlias([1]),
        {"nested": [float("nan")]},
        {"nested": [float("inf")]},
        cycle,
    ]
    for payload in attacks:
        with pytest.raises(R.StrictJSONError):
            R.canonical_json_bytes(payload)
        with pytest.raises(R.StrictJSONError):
            R.branch_transaction_json_bytes(payload)


@pytest.mark.parametrize("attack", ("alias", "count", "file"))
def test_formal_machine_live_conda_manifest_and_distinct_roots(
    tmp_path: Path, attack: str
) -> None:
    fixture = formal_machine_fixture(tmp_path)
    python = fixture["machine"]["python_arb"]
    if attack == "alias":
        forged = "f" * 64
        python["conda_installed_manifest_root_sha256"] = forged
        python["python_flint_record_sha256"] = forged
        python["python_flint_installed_manifest_root_sha256"] = forged
        expected = "pairwise distinct"
    elif attack == "count":
        python["conda_manifest_file_count"] += 1
        expected = "conda manifest live replay"
    else:
        path = Path(python["executable_path"]).parents[1] / "lib/python3.12/fixture.py"
        path.write_bytes(b"# forged conda bytes\n")
        expected = "conda manifest live replay"
    _publish_formal_machine(fixture)
    with pytest.raises(R.ReleaseError, match=expected):
        _validate_machine_fixture(fixture)


@pytest.mark.parametrize(
    "attack", ("branch-build-id", "branch-needed", "runtime-build-id", "runtime-soname")
)
def test_formal_machine_rejects_forged_live_elf_metadata(
    tmp_path: Path, attack: str
) -> None:
    fixture = formal_machine_fixture(tmp_path)
    machine = fixture["machine"]
    if attack == "branch-build-id":
        machine["branch_binary"]["build_id"] = "f" * 40
    elif attack == "branch-needed":
        machine["branch_binary"]["dt_needed"] = [*R.FORMAL_MACHINE_DT_NEEDED, "libforged.so"]
        machine["branch_binary"]["dt_needed_sha256"] = sha(
            R.canonical_json_bytes(machine["branch_binary"]["dt_needed"])
        )
    elif attack == "runtime-build-id":
        machine["runtime_libraries"]["capd_system"][0]["build_id"] = "f" * 40
        machine["branch_binary"]["runtime_libraries_sha256"] = sha(
            R.canonical_json_bytes(machine["runtime_libraries"])
        )
    else:
        row = machine["runtime_libraries"]["capd_system"][0]
        path = Path(row["path"])
        raw = _fixture_elf(row["build_id"], soname="libforged.so")
        path.write_bytes(raw)
        path.chmod(row["mode"])
        row["size_bytes"] = len(raw)
        row["sha256"] = sha(raw)
        machine["branch_binary"]["runtime_libraries_sha256"] = sha(
            R.canonical_json_bytes(machine["runtime_libraries"])
        )
    _publish_formal_machine(fixture)
    with pytest.raises(R.ReleaseError, match="ELF|DT_NEEDED|build-id|SONAME"):
        _validate_machine_fixture(fixture)


@pytest.mark.parametrize("attack", ("head", "tracked", "untracked", "staged"))
def test_formal_machine_replays_live_capd_commit_tree_and_clean_namespace(
    tmp_path: Path, attack: str
) -> None:
    fixture = formal_machine_fixture(tmp_path)
    checkout = Path(fixture["machine"]["capd"]["checkout_path"])
    if attack == "head":
        (checkout / ".git/HEAD").write_text("d" * 40 + "\n", encoding="ascii")
        expected = "HEAD commit|commit/tree"
    elif attack == "tracked":
        (checkout / "README.md").write_text("forged tracked source\n", encoding="utf-8")
        expected = "Git index object ID"
    elif attack == "untracked":
        (checkout / "untracked.txt").write_text("untracked\n", encoding="utf-8")
        expected = "namespace drift"
    else:
        readme = checkout / "README.md"
        readme.write_text("coherent staged source\n", encoding="utf-8")
        _, staged_root = _fixture_git_index(
            checkout,
            {
                "README-link": (0o120000, b"README.md"),
                "README.md": (0o100644, readme.read_bytes()),
            },
            update_head=False,
        )
        fixture["machine"]["capd"]["tree_sha256"] = staged_root
        _publish_formal_machine(fixture)
        expected = "index tree differs"
    with pytest.raises((R.ReleaseError, R.PathContractError), match=expected):
        _validate_machine_fixture(fixture)


def test_formal_machine_rejects_unrelated_python_flint_module_path(
    tmp_path: Path,
) -> None:
    fixture = formal_machine_fixture(tmp_path)
    unrelated = _fixture_file(tmp_path / "unrelated.py", b"# unrelated\n")
    static = json.loads(
        fixture["machine"]["resource_evidence"]["static_payload_raw_utf8"]
    )
    static["bindings"]["python_flint"]["module_path"] = str(unrelated)
    _replace_static_resource(fixture, static)
    with pytest.raises(R.PathContractError, match="installation paths are incoherent"):
        _validate_machine_fixture(fixture)


def test_formal_machine_rejects_coherent_forged_python_version(
    tmp_path: Path,
) -> None:
    fixture = formal_machine_fixture(tmp_path)
    forged_version = "3.12.3 | forged distribution [GCC 11.2.0]"
    fixture["machine"]["python_arb"]["python_version"] = forged_version
    static = json.loads(
        fixture["machine"]["resource_evidence"]["static_payload_raw_utf8"]
    )
    static["bindings"]["interpreter"]["version"] = forged_version
    _replace_static_resource(fixture, static)
    with pytest.raises(R.ReleaseError, match="Python-Arb identity"):
        _validate_machine_fixture(fixture)


def test_formal_machine_rejects_forged_compiler_version(tmp_path: Path) -> None:
    fixture = formal_machine_fixture(tmp_path)
    fixture["machine"]["compiler"]["version"] = "attacker 11.4.0"
    _publish_formal_machine(fixture)
    with pytest.raises(R.ReleaseError, match="compiler version mismatch"):
        _validate_machine_fixture(fixture)


def test_formal_machine_rejects_capture_from_another_boot(tmp_path: Path) -> None:
    fixture = formal_machine_fixture(tmp_path)
    fixture["machine"]["capture"]["captured_at_utc"] = "2000-01-01T00:00:00Z"
    _publish_formal_machine(fixture)
    with pytest.raises(R.ReleaseError, match="live boot window"):
        _validate_machine_fixture(fixture)


def test_formal_machine_replays_manifest_inode_at_transaction_end(
    tmp_path: Path, monkeypatch
) -> None:
    fixture = formal_machine_fixture(tmp_path)
    python = fixture["machine"]["python_arb"]
    target = Path(python["executable_path"]).parents[1] / "lib/python3.12/fixture.py"
    original = R._machine_validate_filesystem

    def validate_then_swap(project: Path, payload: dict[str, Any]) -> None:
        original(project, payload)
        replacement = target.with_name("fixture-replacement.py")
        replacement.write_bytes(target.read_bytes())
        replacement.chmod(stat.S_IMODE(target.stat().st_mode))
        os.replace(replacement, target)

    monkeypatch.setattr(R, "_machine_validate_filesystem", validate_then_swap)
    with pytest.raises(R.PathContractError, match="machine manifest file changed"):
        _validate_machine_fixture(fixture)


def test_formal_machine_replays_conda_metadata_namespace_at_transaction_end(
    tmp_path: Path, monkeypatch
) -> None:
    fixture = formal_machine_fixture(tmp_path)
    prefix = Path(fixture["machine"]["python_arb"]["executable_path"]).parents[1]
    original = R._machine_validate_filesystem

    def validate_then_add_metadata(project: Path, payload: dict[str, Any]) -> None:
        original(project, payload)
        write_json(
            prefix / "conda-meta/unrelated-late.json",
            {"name": "python", "version": "3.12.3", "files": [], "paths_data": {"paths": []}},
        )

    monkeypatch.setattr(R, "_machine_validate_filesystem", validate_then_add_metadata)
    with pytest.raises(R.PathContractError, match="metadata namespace changed"):
        _validate_machine_fixture(fixture)


def test_conda_manifest_requires_exact_python3_and_utf8_symlink(
    tmp_path: Path,
) -> None:
    fixture = formal_machine_fixture(tmp_path)
    executable = Path(fixture["machine"]["python_arb"]["executable_path"])
    alias = _fixture_file(executable.with_name("python-alias"), executable.read_bytes(), 0o755)
    with pytest.raises(R.PathContractError, match="conda bin layout"):
        R._machine_recompute_conda_manifest(str(alias))

    invalid_link = tmp_path / "invalid-target-link"
    os.symlink(b"\xff", os.fsencode(invalid_link))
    with pytest.raises(R.PathContractError, match="strict UTF-8"):
        R._machine_manifest_symlink_snapshot(invalid_link, "invalid fixture link")


def test_release_branch_budget_uses_exact_integer_milliseconds() -> None:
    assert R.BRANCH_CELL_BUDGETS == {
        "pipe_close_grace_ms": 1000,
        "record_bytes": 4 * 1024 * 1024,
        "stderr_bytes": 1 * 1024 * 1024,
        "stdout_bytes": 16 * 1024 * 1024,
        "term_grace_ms": 2000,
        "timeout_ms": 600000,
        "total_cell_bytes": 32 * 1024 * 1024,
    }
    assert all(type(value) is int for value in R.BRANCH_CELL_BUDGETS.values())
