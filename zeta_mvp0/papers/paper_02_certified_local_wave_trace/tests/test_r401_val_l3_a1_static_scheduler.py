from __future__ import annotations

import importlib.util
import json
import os
import re
import shutil
import struct
import subprocess
import sys
import tempfile
import time
import types
from dataclasses import FrozenInstanceError
from datetime import datetime, timezone
from decimal import Decimal
from fractions import Fraction
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/run_r401_val_l3_a1_all_slabs.py"
BRANCH_RUNTIME = ROOT / "scripts/r401_val_l3_a1_branch_runtime.py"
PREFREEZE_DESIGN = (
    ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_PREFREEZE_DESIGN.md"
)
SCHEDULER_CONTRACT = (
    ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_SCHEDULER_CONTRACT.md"
)
PROTOCOL = ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_PROTOCOL.md"
CHECKER_CONTRACT = (
    ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_CHECKER_CONTRACT.md"
)
RELEASE_CONTRACT = (
    ROOT
    / "research/route_a_wave_trace/R401_VAL_L3_A1_RELEASE_PROVENANCE_CONTRACT.md"
)
STATIC_CHECKER = ROOT / "scripts/check_r401_val_l3_a1_static_independent.py"
RELEASE_BUILDER = ROOT / "scripts/build_r401_val_l3_a1_release_provenance.py"
SPEC = importlib.util.spec_from_file_location("r401_val_l3_a1_scheduler", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

_FORMAL_AUTHORITY_PARENT = ROOT.parents[3] / ".pytest-a416-formal-authorities"
_FORMAL_AUTHORITY_CLEANUPS: list[Path] = []


@pytest.fixture(autouse=True)
def cleanup_formal_authority_roots() -> object:
    """Keep exact authority fixtures on the admitted workspace filesystem."""

    start = len(_FORMAL_AUTHORITY_CLEANUPS)
    yield
    for path in reversed(_FORMAL_AUTHORITY_CLEANUPS[start:]):
        shutil.rmtree(path, ignore_errors=True)
    del _FORMAL_AUTHORITY_CLEANUPS[start:]
    try:
        _FORMAL_AUTHORITY_PARENT.rmdir()
    except OSError:
        pass


def load_static_checker() -> object:
    name = "r401_val_l3_a1_static_checker_scheduler_e2e"
    spec = importlib.util.spec_from_file_location(name, STATIC_CHECKER)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def load_release_builder() -> object:
    name = "r401_val_l3_a1_release_builder_machine_capture_roundtrip"
    spec = importlib.util.spec_from_file_location(name, RELEASE_BUILDER)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def roots(tmp_path: Path) -> tuple[Path, Path]:
    output = tmp_path / "mock-generation"
    return output, MODULE.operational_root_for(output)


def initialize(tmp_path: Path) -> tuple[Path, Path, dict[str, object], str]:
    output, operational = roots(tmp_path)
    binding = MODULE.build_mock_binding(output, operational)
    _, config_hash = MODULE.ensure_run_config(output, binding, resume=False)
    operational.mkdir()
    return output, operational, binding, config_hash


def write_canonical_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(MODULE.canonical_json_bytes(payload))


def _fixture_elf(
    build_id: str,
    *,
    soname: str | None = None,
    needed: tuple[str, ...] = (),
) -> bytes:
    """Construct the minimal ELF section ABI used by the live parser."""

    assert re.fullmatch(r"[0-9a-f]{40}", build_id) is not None
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
        name: shstr.index(name.encode("ascii"))
        for name in (".dynstr", ".dynamic", ".note.gnu.build-id", ".shstrtab")
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
    sections.append(
        struct.pack(
            section_format, names[".dynstr"], 3, 0, 0, dynstr_offset,
            dynstr_size, 0, 0, 1, 0,
        )
    )
    sections.append(
        struct.pack(
            section_format, names[".dynamic"], 6, 0, 0, dynamic_offset,
            dynamic_size, 1, 0, 8, 16,
        )
    )
    sections.append(
        struct.pack(
            section_format, names[".note.gnu.build-id"], 7, 0, 0,
            note_offset, note_size, 0, 0, 4, 0,
        )
    )
    sections.append(
        struct.pack(
            section_format, names[".shstrtab"], 3, 0, 0, shstr_offset,
            shstr_size, 0, 0, 1, 0,
        )
    )
    image.extend(b"".join(sections))
    ident = b"\x7fELF" + bytes((2, 1, 1, 0)) + b"\x00" * 8
    image[:64] = struct.pack(
        "<16sHHIQQQIHHHHHH",
        ident, 3, 62, 1, 0, 0, section_offset, 0, 64, 0, 0, 64,
        len(sections), 4,
    )
    return bytes(image)


def _live_file_binding(path: Path, build_id: str | None) -> dict[str, object]:
    raw = path.read_bytes()
    return {
        "path": str(path),
        "mode": path.stat().st_mode & 0o777,
        "size_bytes": len(raw),
        "sha256": MODULE.sha256_bytes(raw),
        "build_id": build_id,
    }


def _runtime_binding(
    path: Path, soname: str, build_id: str
) -> dict[str, object]:
    return {"soname": soname, **_live_file_binding(path, build_id)}


def _resource_static_payload(
    authority: Path, *, evaluator_sha: str, plan_sha: str, interpreter_sha: str,
    interpreter_path: str, python_version: str, flint_module: Path,
    flint_record: Path, arb_extension: Path, installed_count: int,
    installed_root: str, record_sha: str, baseline: int = 1_000,
    peak_kib: int = 100,
) -> dict[str, object]:
    evaluator_path = str(authority / dict(MODULE.FORMAL_INPUT_ROLES)["static_evaluator"])
    plan_path = authority / dict(MODULE.FORMAL_INPUT_ROLES)["l1_final_plan"]
    plan_records = MODULE.validate_plan_payload(
        MODULE.strict_json_load(plan_path)
    )
    public = [(bits, slab) for bits in (128, 256) for slab in ("S000", "S025", "S050")]

    def run(bits: int, slab: str, replica: int, label: str) -> dict[str, object]:
        output = f"/tmp/r401-static/{label}/proof.json"
        record = plan_records[slab]
        argv = [
            interpreter_path, evaluator_path, "--slab-id", slab,
            "--precision-bits", str(bits), "--epsilon-lower", record["epsilon_lower"],
            "--epsilon-upper", record["epsilon_upper"], "--matrix-id", MODULE.canonical_matrix_id(),
            "--freeze-sha256", "1" * 64, "--run-config-sha256", "2" * 64,
            "--plan-record-sha256", MODULE.sha256_bytes(
                MODULE.canonical_json_bytes(record)
            ), "--max-depth", "24",
            "--max-nodes-per-tree", "250000", "--max-nodes-per-cell",
            "1000000", "--output", output,
        ]
        return {
            "argv": argv, "component_status": None, "elapsed_seconds": 0.1,
            "evaluator_status": "STATIC_CELL_CERTIFIED", "final_status": None,
            "label": label, "milestone_status": None, "output": output,
            "output_bytes": 10, "output_sha256": "4" * 64,
            "peak_rss_kib": peak_kib, "precision_bits": bits,
            "replica": replica, "returncode": 0, "scientific_status": None,
            "slab_id": slab, "stderr": f"/tmp/r401-static/{label}/stderr.txt",
            "stderr_bytes": 0, "stderr_empty": True,
            "stderr_sha256": MODULE.sha256_bytes(b""),
            "stdout": f"/tmp/r401-static/{label}/stdout.txt", "stdout_bytes": 39,
            "stdout_exact_status_line": "evaluator_status=STATIC_CELL_CERTIFIED",
            "stdout_sha256": MODULE.sha256_bytes(b"evaluator_status=STATIC_CELL_CERTIFIED\n"),
            "system_cpu_seconds": 0.0, "theorem_status": None,
            "user_cpu_seconds": 0.1,
        }

    sequential = [run(bits, slab, 0, f"{bits}_{slab}") for bits, slab in public]
    concurrent_ids = [(bits, slab, 0) for bits, slab in public] + [
        (256, "S025", 1), (256, "S050", 1)
    ]
    concurrent = [
        run(bits, slab, replica, f"{index:02d}_{bits}_{slab}_r{replica}")
        for index, (bits, slab, replica) in enumerate(concurrent_ids)
    ]
    peak = peak_kib * 1024
    lhs = baseline + 8 * peak + 8 * 1024**3
    return {
        "admission": {
            "admission_limit_bytes": 48 * 1024**3,
            "formula": "idle_baseline_bytes + workers * representative_peak_rss_bytes + reserve_bytes <= admission_limit_bytes",
            "headroom_bytes": 48 * 1024**3 - lhs,
            "idle_baseline_bytes": baseline, "lhs_bytes": lhs, "passes": True,
            "representative_peak_rss_bytes": peak, "reserve_bytes": 8 * 1024**3,
            "workers": 8,
        },
        "artifact_role": "TEMP_PUBLIC_STATIC_RSS_CALIBRATION",
        "bindings": {
            "calibration_binding": {
                "matrix_id": MODULE.canonical_matrix_id(),
                "nonfreeze_sha256": "1" * 64, "nonrunconfig_sha256": "2" * 64,
            },
            "evaluator": {
                "mode": "0644", "path": evaluator_path, "sha256": evaluator_sha,
                "size_bytes": (authority / dict(MODULE.FORMAL_INPUT_ROLES)["static_evaluator"]).stat().st_size,
            },
            "interpreter": {
                "invocation_path": interpreter_path,
                "resolved_path": interpreter_path,
                "sha256": interpreter_sha,
                "size_bytes": Path(interpreter_path).stat().st_size,
                "version": python_version,
            },
            "plan": {
                "path": str(plan_path),
                "public_slab_ids": ["S000", "S025", "S050"], "sha256": plan_sha,
            },
            "python_flint": {
                "arb_extension_path": str(arb_extension),
                "arb_extension_sha256": MODULE.sha256(arb_extension),
                "flint_version": "3.6.0",
                "installed_manifest_sha256": installed_root,
                "installed_record_file_count": installed_count,
                "module_path": str(flint_module),
                "record_path": str(flint_record),
                "record_sha256": record_sha, "version": "0.9.0",
            },
        },
        "claim_boundary": "resource telemetry on already-public S000/S025/S050 at 128/256 only; no held-out/all-slab evaluation, no freeze, no scientific promotion",
        "component_status": None,
        "concurrent_runs": concurrent,
        "concurrent_schedule": [
            {"precision_bits": bits, "slab_id": slab}
            for bits, slab, _replica in concurrent_ids
        ],
        "execution_environment": {
            "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8", "MKL_NUM_THREADS": "1",
            "NUMEXPR_NUM_THREADS": "1", "OMP_NUM_THREADS": "1",
            "OPENBLAS_NUM_THREADS": "1", "PYTHONDONTWRITEBYTECODE": "1",
            "PYTHONHASHSEED": "0", "PYTHONNOUSERSITE": "1", "TZ": "UTC",
        },
        "final_status": None,
        "measurement": {
            "baseline_conservative_bytes": baseline,
            "baseline_samples_bytes": [baseline - 20 + index for index in range(21)],
            "bytes_per_kib": 1024,
            "cgroup_limit_bytes": 60 * 1024**3,
            "cgroup_limit_path": "/sys/fs/cgroup/memory/memory.limit_in_bytes",
            "cgroup_usage_path": "/sys/fs/cgroup/memory/memory.usage_in_bytes",
            "concurrent_peak_bytes": baseline + 20,
            "concurrent_samples_bytes": [baseline + index for index in range(21)],
            "method": "os.wait4(pid,0/WNOHANG).rusage.ru_maxrss on Linux",
            "ru_maxrss_unit": "KiB", "sample_interval_seconds": 0.05,
        },
        "milestone_status": None, "production_authorized": False,
        "project_root": str(authority), "protocol_id": MODULE.PROTOCOL_ID,
        "schema_version": 1, "scientific_licensing_enabled": False,
        "scope": "PUBLIC_S0_RESOURCE_CALIBRATION_ONLY",
        "sequential_runs": sequential, "temporary_root": "/tmp/r401-static",
        "theorem_status": None,
    }


def _resource_branch_payload(
    *, authority: Path, binary_path: str, binary_sha: str, baseline: int = 1_200,
    peak_kib: int = 200,
) -> dict[str, object]:
    plan_records = MODULE.validate_plan_payload(
        MODULE.strict_json_load(
            authority / dict(MODULE.FORMAL_INPUT_ROLES)["l1_final_plan"]
        )
    )

    def argv(bits: int, slab: str) -> list[str]:
        record = plan_records[slab]
        center = record["center"]
        radii = record["root_radii"]

        def endpoint(name: str, sign: int) -> str:
            return format(
                Decimal(center[name]) + sign * Decimal(radii[name]), "f"
            )

        return [
            binary_path, str(bits), record["epsilon_lower"],
            record["epsilon_upper"], endpoint("q_slow", -1),
            endpoint("q_slow", 1), endpoint("q_fast", -1),
            endpoint("q_fast", 1), endpoint("p_slow", -1),
            endpoint("p_slow", 1), endpoint("period", -1),
            endpoint("period", 1),
        ]

    identities = [(bits, slab) for bits in (128, 256) for slab in ("S000", "S025", "S050")]
    results = []
    for bits, slab in identities:
        results.append({
            "abi_verified": True,
            "argv": argv(bits, slab),
            "argv_count": 12, "elapsed_seconds": 0.1,
            "peak_rss_kib": peak_kib, "precision_bits": bits,
            "returncode": 0, "slab_id": slab, "stderr_bytes": 0,
            "stderr_sha256": MODULE.sha256_bytes(b""), "stdout_bytes": 10,
            "stdout_sha256": "7" * 64, "system_cpu_seconds": 0.0,
            "terminal_abi_value": "BRANCH_CELL_CERTIFIED",
            "user_cpu_seconds": 0.1,
        })
    peak = peak_kib * 1024
    lhs = baseline + 6 * peak + 8 * 1024**3
    return {
        "admission": {
            "baseline_bytes": baseline,
            "formula": "baseline + 6*peak_rss + 8GiB <= 48GiB",
            "headroom_bytes": 48 * 1024**3 - lhs, "lhs_bytes": lhs,
            "limit_bytes": 48 * 1024**3, "passes": True,
            "peak_rss_bytes": peak, "reserve_bytes": 8 * 1024**3, "workers": 6,
        },
        "baseline_conservative_bytes": baseline,
        "baseline_samples_bytes": [baseline - 20 + index for index in range(21)],
        "binary": binary_path, "binary_sha256": binary_sha,
        "cgroup_limit_bytes": 60 * 1024**3, "final_status": None,
        "milestone_status": None, "per_process_peak_rss_max_kib": peak_kib,
        "post_samples_bytes": [baseline + index for index in range(21)],
        "results": results,
        "sampled_concurrent_increment_bytes": 100,
        "sampled_concurrent_peak_bytes": baseline + 100,
        "scientific_status": None, "scope": "REPRESENTATIVE_S0_CALIBRATION_ONLY",
        "task_count": 6, "theorem_status": None,
    }


def _fixture_conda_python_prefix(
    prefix: Path,
) -> tuple[Path, str, int, str]:
    executable = prefix / "bin/python3"
    executable.parent.mkdir(parents=True)
    executable.write_bytes(b"fixture Python 3.12.3\n")
    executable.chmod(0o755)
    library = prefix / "lib/python-core.txt"
    library.parent.mkdir(parents=True)
    library.write_bytes(b"fixture standard library\n")
    link = prefix / "lib/python-link"
    link.symlink_to("python-core.txt")
    files = ["lib/python-link", "bin/python3", "lib/python-core.txt"]
    metadata = {
        "name": "python",
        "version": "3.12.3",
        "files": files,
        "paths_data": {
            "paths_version": 1,
            "paths": [
                {"_path": "bin/python3", "path_type": "hardlink"},
                {"_path": "lib/python-core.txt", "path_type": "hardlink"},
                {"_path": "lib/python-link", "path_type": "softlink"},
            ],
        },
    }
    write_canonical_json(
        prefix / "conda-meta/python-3.12.3-fixture_0.json", metadata
    )
    algorithm, count, root = MODULE.recompute_conda_python_manifest(
        str(executable)
    )
    expected_rows = [
        {
            "kind": "REGULAR",
            "mode": "0755",
            "path": "bin/python3",
            "sha256": MODULE.sha256_bytes(executable.read_bytes()),
            "size_bytes": executable.stat().st_size,
        },
        {
            "kind": "REGULAR",
            "mode": "0644",
            "path": "lib/python-core.txt",
            "sha256": MODULE.sha256_bytes(library.read_bytes()),
            "size_bytes": library.stat().st_size,
        },
        {
            "kind": "SYMLINK",
            "mode": "0777",
            "path": "lib/python-link",
            "sha256": MODULE.sha256_bytes(b"python-core.txt"),
            "size_bytes": len(b"python-core.txt"),
        },
    ]
    assert algorithm == MODULE.CONDA_MANIFEST_ALGORITHM
    assert count == 3
    assert root == MODULE.sha256_bytes(MODULE.canonical_json_bytes(expected_rows))
    return executable, algorithm, count, root


def _fixture_capd_checkout(
    checkout: Path,
) -> tuple[str, str, dict[str, Path], str]:
    """Create a small detached, clean v2-index checkout plus build-mp files."""

    checkout.mkdir(parents=True)
    subprocess.run(["git", "init", "-q", str(checkout)], check=True)
    subprocess.run(
        ["git", "-C", str(checkout), "config", "user.name", "A416 Fixture"],
        check=True,
    )
    subprocess.run(
        ["git", "-C", str(checkout), "config", "user.email", "fixture@example.invalid"],
        check=True,
    )
    (checkout / "README.md").write_bytes(b"A4.16 CAPD fixture\n")
    header = checkout / "capdAlg/include/fixture.hpp"
    header.parent.mkdir(parents=True)
    header.write_bytes(b"#pragma once\n")
    tool = checkout / "capdAux/bin/fixture-tool"
    tool.parent.mkdir(parents=True)
    tool.write_bytes(b"#!/bin/sh\nexit 0\n")
    tool.chmod(0o755)
    link = checkout / "capdAlg/include/fixture-link.hpp"
    link.symlink_to("fixture.hpp")
    subprocess.run(["git", "-C", str(checkout), "add", "--all"], check=True)
    commit_environment = dict(os.environ)
    commit_environment.update(
        {
            "GIT_AUTHOR_DATE": "2026-08-10T00:00:00Z",
            "GIT_COMMITTER_DATE": "2026-08-10T00:00:00Z",
        }
    )
    subprocess.run(
        ["git", "-C", str(checkout), "commit", "-q", "-m", "fixture"],
        check=True,
        env=commit_environment,
    )
    commit = subprocess.check_output(
        ["git", "-C", str(checkout), "rev-parse", "HEAD"], text=True
    ).strip()
    subprocess.run(
        ["git", "-C", str(checkout), "checkout", "-q", "--detach", commit],
        check=True,
    )
    subprocess.run(
        ["git", "-C", str(checkout), "update-index", "--index-version", "2"],
        check=True,
    )

    build = checkout / "build-mp"
    cache = build / "CMakeCache.txt"
    config = build / "bin/capd-config"
    libcapd = build / "libcapd.a"
    libfilib = build / "capdExt/filibsrc/libfilib.a"
    for path in (cache, config, libcapd, libfilib):
        path.parent.mkdir(parents=True, exist_ok=True)
    cache.write_bytes(b"fixture cache\n")
    config.write_bytes(b"#!/bin/sh\n")
    config.chmod(0o755)
    libcapd.write_bytes(b"fixture libcapd archive\n")
    libfilib.write_bytes(b"fixture libfilib archive\n")
    algorithm, live_commit, tree_root = MODULE.recompute_capd_git_index_tree(
        str(checkout)
    )
    assert algorithm == MODULE.CAPD_TREE_ALGORITHM
    assert live_commit == commit
    flags = [
        "-std=c++17", "-O2", "-frounding-math", "-D__USE_FILIB__",
        "-D__HAVE_MPFR__", "-O2", "-frounding-math", "-DFILIB_EXTENDED",
        "-DFILIB_HAVE_SSE", f"-I{checkout}/capdDynSys/include",
        f"-I{checkout}/capdAlg/include", f"-I{checkout}/capdAux/include",
        f"-I{checkout}/capdExt/include", f"-I{checkout}/capdExt/filibsrc",
        f"-L{checkout}/build-mp", f"-L{checkout}/build-mp/capdExt/filibsrc",
        "-lcapd", "-lfilib", "-lmpfr", "-lgmp",
    ]
    return commit, tree_root, {
        "cache": cache,
        "config": config,
        "libcapd": libcapd,
        "libfilib": libfilib,
    }, " ".join(flags) + "\n"


def formal_authority_fixture(tmp_path: Path) -> Path:
    _FORMAL_AUTHORITY_PARENT.mkdir(parents=True, exist_ok=True)
    authority = Path(
        tempfile.mkdtemp(
            prefix=f"{tmp_path.name}-",
            dir=_FORMAL_AUTHORITY_PARENT,
        )
    ).absolute()
    _FORMAL_AUTHORITY_CLEANUPS.append(authority)
    (authority / "results").mkdir()
    for role, relative in MODULE.FORMAL_INPUT_ROLES:
        target = authority / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        source = ROOT / relative
        if source.is_file():
            shutil.copy2(source, target)
        elif relative.endswith(".json"):
            write_canonical_json(target, {"fixture_role": role})
        else:
            target.write_text(f"formal fixture role: {role}\n", encoding="utf-8")

    review = authority / dict(MODULE.FORMAL_INPUT_ROLES)["prefreeze_review"]
    review.write_text(
        "Independent implementation fixture review\n"
        f"{MODULE.PREFREEZE_ACCEPT_LINE}\n",
        encoding="utf-8",
    )
    binary = authority / dict(MODULE.FORMAL_INPUT_ROLES)["branch_evaluator_binary"]
    binary.chmod(0o755)

    role_paths = dict(MODULE.FORMAL_INPUT_ROLES)
    scheduler_sha = MODULE.sha256(authority / role_paths["scheduler"])
    static_sha = MODULE.sha256(authority / role_paths["static_evaluator"])
    plan_sha = MODULE.sha256(authority / role_paths["l1_final_plan"])
    source_sha = MODULE.sha256(authority / role_paths["branch_evaluator_source"])
    binary_sha = MODULE.sha256(binary)
    branch_build_id, branch_dt_needed, branch_soname = MODULE._elf_metadata(
        binary.read_bytes(), "fixture branch binary"
    )
    assert branch_dt_needed == MODULE.MACHINE_BRANCH_DT_NEEDED
    assert branch_soname is None
    (
        interpreter,
        conda_algorithm,
        conda_file_count,
        conda_manifest_root,
    ) = _fixture_conda_python_prefix((tmp_path / "conda-prefix").absolute())
    interpreter_sha = MODULE.sha256_bytes(interpreter.read_bytes())
    python_version = MODULE.MACHINE_PYTHON_VERSION
    site_packages = Path("/root/miniconda3/lib/python3.12/site-packages")
    flint_module = site_packages / "flint/__init__.py"
    flint_record = site_packages / "python_flint-0.9.0.dist-info/RECORD"
    arb_extension = site_packages / "flint/types/arb.abi3.so"
    fmpq_extension = site_packages / "flint/types/fmpq.abi3.so"
    assert all(
        path.is_file()
        for path in (flint_module, flint_record, arb_extension, fmpq_extension)
    )
    record_raw = flint_record.read_bytes()
    record_sha = MODULE.sha256_bytes(record_raw)
    installed_count, installed_root = MODULE.recompute_python_flint_manifest(
        str(flint_record), record_raw
    )
    assert record_sha == MODULE.PYTHON_FLINT_RECORD_SHA256
    assert installed_count == MODULE.PYTHON_FLINT_INSTALLED_FILE_COUNT
    assert installed_root == MODULE.PYTHON_FLINT_INSTALLED_MANIFEST_ROOT_SHA256
    static_payload = _resource_static_payload(
        authority,
        evaluator_sha=static_sha,
        plan_sha=plan_sha,
        interpreter_sha=interpreter_sha,
        interpreter_path=str(interpreter),
        python_version=python_version,
        flint_module=flint_module,
        flint_record=flint_record,
        arb_extension=arb_extension,
        installed_count=installed_count,
        installed_root=installed_root,
        record_sha=record_sha,
    )
    branch_payload = _resource_branch_payload(
        authority=authority, binary_path=str(binary), binary_sha=binary_sha
    )
    static_raw = MODULE.canonical_json_bytes(static_payload)
    branch_raw = MODULE.pretty_json_bytes(branch_payload)
    runtime_root = (tmp_path / "runtime-libraries").absolute()
    python_libraries = []
    for index, soname in enumerate(MODULE.MACHINE_PYTHON_BUNDLED_SONAMES):
        marker = format(index + 1, "x")
        path = runtime_root / "python" / soname
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(_fixture_elf(marker * 40, soname=soname))
        path.chmod(0o755)
        python_libraries.append(_runtime_binding(path, soname, marker * 40))
    capd_libraries = []
    for index, soname in enumerate(MODULE.MACHINE_CAPD_SYSTEM_SONAMES):
        marker = format(index + 8, "x")
        path = runtime_root / "capd" / soname
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(_fixture_elf(marker * 40, soname=soname))
        path.chmod(0o755)
        capd_libraries.append(_runtime_binding(path, soname, marker * 40))
    runtime_libraries = {
        "python_bundled": python_libraries,
        "capd_system": capd_libraries,
    }
    capd_checkout = (tmp_path / "capd-checkout").absolute()
    capd_commit, capd_tree_root, capd_paths, capd_raw_flags = (
        _fixture_capd_checkout(capd_checkout)
    )
    capd_flag_tokens = MODULE.shlex.split(capd_raw_flags, posix=True)
    compiler_executable = (tmp_path / "compiler/bin/g++").absolute()
    compiler_executable.parent.mkdir(parents=True)
    compiler_executable.write_bytes(b"fixture g++ 11.4.0\n")
    compiler_executable.chmod(0o755)
    machine_project_root = authority
    build_argv_template = [
        str(compiler_executable), "-Wall", "-Wextra", "-Wpedantic", "-Werror",
        str(machine_project_root / role_paths["branch_evaluator_source"]),
        *capd_flag_tokens, "-o",
        "@STAGING_BINARY@",
    ]
    staging_directory = "/tmp/a416-l3a1-fixture-build"
    staging_output = (
        f"{staging_directory}/capd_r401_phase_branch_tube_mp_a1"
    )
    build_argv = [*build_argv_template[:-1], staging_output]
    requirements = MODULE.formal_machine_requirements()
    filesystem_stats = os.statvfs(machine_project_root / "results")
    live_free_bytes = filesystem_stats.f_bavail * filesystem_stats.f_frsize
    observations = {
        "logical_cpu_count": requirements["logical_cpu_count"],
        "memory_limit_bytes": requirements["memory_limit_bytes"],
        "result_parent_free_bytes": live_free_bytes,
        "idle_baseline_rss_bytes": 1_200,
        "representative_static_peak_rss_bytes": 100 * 1024,
        "representative_branch_peak_rss_bytes": 200 * 1024,
    }
    static_required = (
        observations["idle_baseline_rss_bytes"]
        + requirements["static_workers"] * observations["representative_static_peak_rss_bytes"]
        + requirements["reserve_bytes"]
    )
    branch_required = (
        observations["idle_baseline_rss_bytes"]
        + requirements["branch_workers"] * observations["representative_branch_peak_rss_bytes"]
        + requirements["reserve_bytes"]
    )
    device_id = machine_project_root.stat().st_dev
    machine_payload = {
        "schema_version": 1,
        "protocol_id": MODULE.PROTOCOL_ID,
        "artifact_role": "MACHINE_FREEZE",
        "status": "FROZEN_FOR_PRODUCTION",
        "authority": "MACHINE_ADMISSION_ONLY",
        "scientific_licensing_enabled": True,
        "production_authorized": False,
        "capture": {
            "captured_at_utc": datetime.now(timezone.utc).strftime(
                "%Y-%m-%dT%H:%M:%SZ"
            ),
            "capture_tool_path": role_paths["scheduler"],
            "capture_tool_sha256": scheduler_sha,
            "boot_id_sha256": MODULE.sha256_bytes(
                Path("/proc/sys/kernel/random/boot_id").read_bytes()
            ),
        },
        "machine_requirements": requirements,
        "machine_observations": observations,
        "python_arb": {
            "executable_path": str(interpreter),
            "executable_sha256": interpreter_sha,
            "python_version": python_version, "implementation": "CPython",
            "python_flint_version": "0.9.0", "flint_version": "3.6.0",
            "arb_version": "FLINT-3.6.0",
            "conda_manifest_algorithm": conda_algorithm,
            "conda_manifest_file_count": conda_file_count,
            "conda_installed_manifest_root_sha256": conda_manifest_root,
            "python_flint_record_sha256": record_sha,
            "python_flint_installed_manifest_root_sha256": installed_root,
            "arb_extension": _live_file_binding(
                arb_extension,
                MODULE._elf_metadata(
                    arb_extension.read_bytes(), "fixture Arb extension"
                )[0],
            ),
            "fmpq_extension": _live_file_binding(
                fmpq_extension,
                MODULE._elf_metadata(
                    fmpq_extension.read_bytes(), "fixture fmpq extension"
                )[0],
            ),
            "bundled_libraries": python_libraries,
        },
        "capd": {
            "checkout_path": str(capd_checkout), "commit": capd_commit,
            "tree_algorithm": MODULE.CAPD_TREE_ALGORITHM,
            "tree_sha256": capd_tree_root, "clean": True,
            "cmake_cache_path": str(capd_paths["cache"]),
            "cmake_cache_sha256": MODULE.sha256(capd_paths["cache"]),
            "config_path": str(capd_paths["config"]),
            "config_sha256": MODULE.sha256(capd_paths["config"]),
            "raw_flags": capd_raw_flags,
            "raw_flags_sha256": MODULE.sha256_bytes(capd_raw_flags.encode("utf-8")),
            "libcapd": {
                "path": str(capd_paths["libcapd"]), "mode": 0o644,
                "size_bytes": capd_paths["libcapd"].stat().st_size,
                "sha256": MODULE.sha256(capd_paths["libcapd"]), "build_id": None,
            },
            "libfilib": {
                "path": str(capd_paths["libfilib"]), "mode": 0o644,
                "size_bytes": capd_paths["libfilib"].stat().st_size,
                "sha256": MODULE.sha256(capd_paths["libfilib"]), "build_id": None,
            },
        },
        "compiler": {
            "executable_path": str(compiler_executable),
            "executable_sha256": MODULE.sha256(compiler_executable),
            "version": MODULE.MACHINE_COMPILER_VERSION,
            "build_recipe": {
                "cwd": str(machine_project_root),
                "environment": MODULE.formal_build_environment(),
                "umask": "0022", "staging_output_token": "@STAGING_BINARY@",
                "argv_template": build_argv_template,
                "argv_template_sha256": MODULE.sha256_bytes(
                    MODULE.canonical_json_bytes(build_argv_template)
                ),
            },
            "fresh_rebuild_receipt": {
                "cwd": str(machine_project_root),
                "environment": MODULE.formal_build_environment(),
                "umask": "0022", "staging_directory": staging_directory,
                "staging_output_path": staging_output, "argv": build_argv,
                "argv_sha256": MODULE.sha256_bytes(
                    MODULE.canonical_json_bytes(build_argv)
                ),
                "stdout": "", "stderr": "",
                "stdout_sha256": MODULE.sha256_bytes(b""),
                "stderr_sha256": MODULE.sha256_bytes(b""), "return_code": 0,
                "output_sha256": binary_sha,
                "output_size_bytes": binary.stat().st_size,
                "output_mode": binary.stat().st_mode & 0o777,
                "output_build_id": branch_build_id,
                "output_dt_needed": branch_dt_needed,
                "output_dt_needed_sha256": MODULE.sha256_bytes(
                    MODULE.canonical_json_bytes(branch_dt_needed)
                ),
                "output_soname": None, "shell_used": False,
            },
            "transfer_evidence": {
                "branch_calibration_binary_sha256": binary_sha,
                "staging_output_sha256": binary_sha,
                "staging_output_size_bytes": binary.stat().st_size,
                "staging_output_mode": binary.stat().st_mode & 0o777,
                "persistent_before_sha256": binary_sha,
                "persistent_before_size_bytes": binary.stat().st_size,
                "persistent_before_mode": binary.stat().st_mode & 0o777,
                "persistent_before_device_id": binary.stat().st_dev,
                "persistent_before_inode": binary.stat().st_ino,
                "persistent_after_sha256": binary_sha,
                "persistent_after_size_bytes": binary.stat().st_size,
                "persistent_after_mode": binary.stat().st_mode & 0o777,
                "persistent_after_device_id": binary.stat().st_dev,
                "persistent_after_inode": binary.stat().st_ino,
                "byte_for_byte_equal": True,
                "persistent_identity_unchanged": True,
                "persistent_overwrite_performed": False,
            },
        },
        "branch_binary": {
            "path": role_paths["branch_evaluator_binary"], "sha256": binary_sha,
            "size_bytes": binary.stat().st_size,
            "executable_mode": binary.stat().st_mode & 0o777,
            "build_id": branch_build_id,
            "source_path": role_paths["branch_evaluator_source"],
            "source_sha256": source_sha, "elf_sha256": binary_sha,
            "dt_needed": branch_dt_needed,
            "dt_needed_sha256": MODULE.sha256_bytes(MODULE.canonical_json_bytes(branch_dt_needed)),
            "runtime_libraries_sha256": MODULE.sha256_bytes(MODULE.canonical_json_bytes(runtime_libraries)),
        },
        "runtime_libraries": runtime_libraries,
        "resource_evidence": {
            "static_payload_raw_utf8": static_raw.decode("utf-8"),
            "static_payload_sha256": MODULE.sha256_bytes(static_raw),
            "branch_payload_raw_utf8": branch_raw.decode("utf-8"),
            "branch_payload_sha256": MODULE.sha256_bytes(branch_raw),
            "persistent_binary_sha256": binary_sha,
        },
        "resource_admission": {
            "static_required_bytes": static_required,
            "branch_required_bytes": branch_required,
            "admitted_required_bytes": max(static_required, branch_required),
            "admission_limit_bytes": requirements["memory_admission_limit_bytes"],
            "static_inequality_passed": True, "branch_inequality_passed": True,
            "storage_launch_passed": True,
        },
        "filesystem": {
            "project_root": str(machine_project_root),
            "result_parent": str(machine_project_root / "results"),
            "operational_parent": str(machine_project_root / "results"),
            "project_device_id": device_id, "result_device_id": device_id,
            "operational_device_id": device_id, "same_filesystem": True,
        },
        "claim_boundary": MODULE.MACHINE_CLAIM_BOUNDARY,
        "component_status": None, "milestone_status": None,
        "theorem_status": None, "final_status": None,
    }
    machine = authority / role_paths["machine_freeze"]
    write_canonical_json(machine, machine_payload)

    role_records = [
        MODULE.formal_role_binding(authority, role, relative)[0]
        for role, relative in MODULE.FORMAL_INPUT_ROLES
    ]
    roles = [item.payload() for item in role_records]
    machine_hash = next(
        item.sha256 for item in role_records if item.role == "machine_freeze"
    )
    role_map = {item.role: item for item in role_records}
    freeze = {
        "schema_version": 1,
        "protocol_id": MODULE.PROTOCOL_ID,
        "artifact_role": "MAIN_FREEZE",
        "status": "FROZEN_FOR_PRODUCTION",
        "authority": "INDEPENDENT_PREFREEZE_REVIEW",
        "scientific_licensing_enabled": True,
        "matrix": MODULE.matrix_payload(),
        "matrix_id": MODULE.canonical_matrix_id(),
        "machine_freeze_sha256": machine_hash,
        "input_roles": roles,
        "prefreeze_review": {
            "path": role_map["prefreeze_review"].path,
            "sha256": role_map["prefreeze_review"].sha256,
            "verdict": "ACCEPT_FOR_FREEZE",
        },
        "serializers": MODULE.formal_serializers(),
        "scheduler": MODULE.formal_scheduler_policy(),
        "limits": MODULE.formal_limits(),
        "status_tables": MODULE.formal_status_tables(),
        "evaluators": {
            "static": {
                "path": role_map["static_evaluator"].path,
                "sha256": role_map["static_evaluator"].sha256,
                "abi": "PYTHON_STATIC_ABI_26_STRINGS_V1", "argv_count": 26,
            },
            "branch": {
                "source_path": role_map["branch_evaluator_source"].path,
                "source_sha256": role_map["branch_evaluator_source"].sha256,
                "binary_path": role_map["branch_evaluator_binary"].path,
                "binary_sha256": role_map["branch_evaluator_binary"].sha256,
                "runtime_path": role_map["branch_runtime"].path,
                "runtime_sha256": role_map["branch_runtime"].sha256,
                "abi": "CAPD_BRANCH_ABI_12_STRINGS_V1", "argv_count": 12,
            },
        },
        "checkers": {
            name: {"path": role_map[role].path, "sha256": role_map[role].sha256}
            for name, role in (
                ("static", "static_checker_source"),
                ("branch", "branch_checker_source"),
                ("composite", "composite_checker_source"),
                ("release_builder", "release_builder"),
            )
        },
        "archive_layout": MODULE.formal_archive_layout(),
        "machine_requirements": MODULE.formal_machine_requirements(),
        "failure_policy": MODULE.formal_failure_policy(),
        "execution_policy": MODULE.formal_execution_policy(),
        "claim_boundary": MODULE.MAIN_FREEZE_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    write_canonical_json(
        authority / "research/route_a_wave_trace/R401_VAL_L3_A1_FREEZE.json",
        freeze,
    )
    return authority


def pure_machine_candidate(machine: dict[str, object]) -> dict[str, object]:
    resource = machine["resource_evidence"]
    assert isinstance(resource, dict)
    capture = machine["capture"]
    assert isinstance(capture, dict)
    return MODULE.build_formal_machine_freeze_candidate(
        captured_at_utc=capture["captured_at_utc"],
        capture_tool_sha256=capture["capture_tool_sha256"],
        boot_id_sha256=capture["boot_id_sha256"],
        machine_observations=machine["machine_observations"],
        python_arb=machine["python_arb"],
        capd=machine["capd"],
        compiler=machine["compiler"],
        branch_binary=machine["branch_binary"],
        runtime_libraries=machine["runtime_libraries"],
        static_payload_raw=resource["static_payload_raw_utf8"].encode("utf-8"),
        branch_payload_raw=resource["branch_payload_raw_utf8"].encode("utf-8"),
        filesystem=machine["filesystem"],
    )


def synthetic_formal_static_pass_proof(
    transaction: object,
) -> dict[str, object]:
    """Build only the cheap producer-ABI envelope; never evaluate a cell."""

    assert isinstance(transaction, MODULE.FormalStaticTransactionPlan)
    echo = MODULE._formal_static_expected_input_echo(transaction)
    payload: dict[str, object] = {
        "schema_version": MODULE.SCHEMA_VERSION,
        "protocol_id": MODULE.PROTOCOL_ID,
        "artifact_role": "STATIC_CELL_PROOF",
        "authority": "PRODUCER_ONLY",
        "scientific_licensing_enabled": False,
        "matrix_id": transaction.matrix_id,
        "freeze_sha256": transaction.freeze_sha256,
        "run_config_sha256": transaction.run_config_sha256,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
        "evaluator_status": "STATIC_CELL_CERTIFIED",
        "slab_id": transaction.cell.slab_id,
        "precision_bits": transaction.cell.precision_bits,
        "epsilon": MODULE._formal_static_interval_record(
            Fraction(str(echo["epsilon_lower"])),
            Fraction(str(echo["epsilon_upper"])),
        ),
        "period_window": MODULE._formal_static_interval_record(
            Fraction(64, 100), Fraction(69, 100)
        ),
        "input_echo": echo,
        "claim_boundary": MODULE.FORMAL_STATIC_CELL_CLAIM_BOUNDARY,
        "proof_complete": True,
        "outer_containment": {},
        "trees": [],
        "counts": {},
        "source_bindings": transaction.expected_source_bindings(),
        "proof_content_hash_definition": (
            "sha256(canonical_json(proof_without_proof_content_sha256))"
        ),
    }
    payload["proof_content_sha256"] = MODULE.sha256_bytes(
        MODULE.canonical_json_bytes(payload)
    )
    return payload


def test_exact_matrix_and_matrix_id_are_canonical() -> None:
    matrix = MODULE.exact_matrix()
    assert len(matrix) == len(set(matrix)) == 102
    assert matrix == tuple(
        MODULE.CellKey(bits, f"S{index:03d}")
        for bits in (128, 256)
        for index in range(51)
    )
    assert matrix[0].label == "128:S000"
    assert matrix[50].label == "128:S050"
    assert matrix[51].label == "256:S000"
    assert matrix[-1].label == "256:S050"
    assert MODULE.canonical_matrix_id() == MODULE.sha256_bytes(
        MODULE.canonical_json_bytes(MODULE.matrix_payload())
    )
    assert len(MODULE.canonical_matrix_id()) == 64


@pytest.mark.parametrize(
    "raw",
    [
        '{"x":1,"x":1}',
        '{"x":NaN}',
        '{"x":Infinity}',
        '{"x":1e9999}',
    ],
)
def test_strict_json_rejects_duplicate_and_nonfinite_values(raw: str) -> None:
    with pytest.raises(MODULE.StrictJSONError):
        MODULE.strict_json_loads(raw)


def test_exact_json_equality_rejects_boolean_and_integral_float_aliases() -> None:
    assert not MODULE.exact_json_equal({"x": True}, {"x": 1})
    assert not MODULE.exact_json_equal({"x": 1.0}, {"x": 1})
    assert MODULE.exact_json_equal({"x": [1, None]}, {"x": [1, None]})


@pytest.mark.parametrize(
    "value",
    ["", "/absolute", "../escape", "a/../b", "./a", "a//b", "a\\b", "a/"],
)
def test_safe_relative_path_rejects_aliases(value: str) -> None:
    with pytest.raises(MODULE.PathContractError):
        MODULE.safe_relative_path(value)


def test_symlink_and_hardlink_controls_are_rejected(tmp_path: Path) -> None:
    target = tmp_path / "target.json"
    target.write_text("{}\n", encoding="utf-8")
    link = tmp_path / "link.json"
    link.symlink_to(target)
    with pytest.raises(MODULE.PathContractError):
        MODULE.strict_json_load(link)

    alias = tmp_path / "alias.json"
    os.link(target, alias)
    with pytest.raises(MODULE.PathContractError, match="hard-link"):
        MODULE.strict_json_load(target)


def test_staging_and_interrupted_names_are_exact() -> None:
    run_config_sha256 = "a" * 64
    for cell in MODULE.exact_matrix():
        name = MODULE.staging_basename(cell, run_config_sha256)
        assert MODULE.STAGING_BASENAME.fullmatch(name)
        assert name == f".{cell.slab_id}.tmp-aaaaaaaaaaaaaaaa-0"
    for invalid in (
        ".S051.tmp-aaaaaaaaaaaaaaaa-0",
        "S000.tmp-aaaaaaaaaaaaaaaa-0",
        ".S000.tmp-AAAAAAAAAAAAAAAA-0",
        ".S000.tmp-aaaaaaaaaaaaaaaa-00",
        ".S000.tmp-aaaaaaaaaaaaaaa-0",
        ".S000.tmp-aaaaaaaaaaaaaaaa-0.extra",
    ):
        assert MODULE.STAGING_BASENAME.fullmatch(invalid) is None
    with pytest.raises(MODULE.PathContractError):
        MODULE.staging_basename(MODULE.CellKey(128, "S000"), "a" * 63)


def test_static_and_branch_staging_namespace_matches_reviewed_design() -> None:
    template = ".{slab_id}.tmp-{generation_prefix_16hex}-{attempt_decimal}"
    assert template in PREFREEZE_DESIGN.read_text(encoding="utf-8")
    assert template in SCHEDULER_CONTRACT.read_text(encoding="utf-8")
    runtime_source = BRANCH_RUNTIME.read_text(encoding="utf-8")
    assert 'f".{task.slab_id}.tmp-{generation_prefix}-{attempt}"' in runtime_source
    cell = MODULE.CellKey(128, "S000")
    assert MODULE.staging_path(Path("/tmp/operational"), cell, "b" * 64, 7) == Path(
        "/tmp/operational/staging/static/128/.S000.tmp-bbbbbbbbbbbbbbbb-7"
    )


def test_candidate_role_map_counts_and_new_direct_bindings_are_consistent() -> None:
    release_text = RELEASE_CONTRACT.read_text(encoding="utf-8")
    input_section = release_text.split(
        "## 2. Exact 53-role main-freeze input map candidate", 1
    )[1].split("## 3. Main freeze edge", 1)[0]
    input_rows = re.findall(r"^\| (\d+) \| `([^`]+)` \| `([^`]+)` \|$", input_section, re.M)
    assert [int(index) for index, _role, _path in input_rows] == list(range(1, 54))
    roles = [role for _index, role, _path in input_rows]
    paths = [path for _index, _role, path in input_rows]
    assert len(roles) == len(set(roles)) == 53
    assert len(paths) == len(set(paths)) == 53
    direct_bindings = {
        "implementation_design_review": (
            "research/route_a_wave_trace/R401_VAL_L3_A1_DESIGN_REVIEW.md"
        ),
        "branch_runtime": "scripts/r401_val_l3_a1_branch_runtime.py",
        "test_static_evaluator": "tests/test_r401_val_l3_a1_static_cell.py",
        "test_s0_compatibility": "tests/test_r401_val_l3_a1_s0_compatibility.py",
    }
    table = {role: path for _index, role, path in input_rows}
    assert {role: table[role] for role in direct_bindings} == direct_bindings
    assert all((ROOT / path).is_file() for path in direct_bindings.values())

    release_section = release_text.split(
        "## 4. Exact 68-role release map candidate", 1
    )[1].split("## 5. Candidate exact release schema", 1)[0]
    release_rows = re.findall(
        r"^\| (\d+) \| `([^`]+)` \| `([^`]+)` \|$", release_section, re.M
    )
    assert [int(index) for index, _role, _path in release_rows] == list(range(55, 69))
    for path in (PROTOCOL, SCHEDULER_CONTRACT, CHECKER_CONTRACT, RELEASE_CONTRACT):
        text = path.read_text(encoding="utf-8")
        assert "53" in text and "68" in text


def test_mock_binding_is_sealed_nonlicensing_and_type_strict(tmp_path: Path) -> None:
    output, operational = roots(tmp_path)
    binding = MODULE.build_mock_binding(output, operational)
    MODULE.validate_mock_binding(binding)
    assert binding["matrix_id"] == MODULE.canonical_matrix_id()
    assert binding["mock_only"] is True
    assert binding["production_authorized"] is False
    assert binding["scientific_licensing_enabled"] is False
    assert binding["main_freeze"] == {"path": None, "sha256": None}
    assert binding["milestone_status"] is None
    assert binding["theorem_status"] is None
    assert binding["final_status"] is None

    forged = dict(binding)
    forged["schema_version"] = True
    with pytest.raises(MODULE.StrictJSONError):
        MODULE.validate_mock_binding(forged)

    forged = json.loads(json.dumps(binding))
    forged["paths"]["extra"] = "/tmp/forged"
    with pytest.raises(MODULE.StrictJSONError, match="key set mismatch"):
        MODULE.validate_mock_binding(forged)

    forged = json.loads(json.dumps(binding))
    forged["paths"]["operational_root"] = 7
    with pytest.raises(MODULE.PathContractError):
        MODULE.validate_mock_binding(forged)

    forged = json.loads(json.dumps(binding))
    forged["limits"]["static"]["workers"] = 7
    with pytest.raises(MODULE.StrictJSONError, match="resource limits"):
        MODULE.validate_mock_binding(forged)


def test_run_config_is_write_once_and_resume_is_exact(tmp_path: Path) -> None:
    output, operational = roots(tmp_path)
    binding = MODULE.build_mock_binding(output, operational)
    stored, first_hash = MODULE.ensure_run_config(output, binding, resume=False)
    before = MODULE.run_config_path(output).read_bytes()
    resumed, second_hash = MODULE.ensure_run_config(output, binding, resume=True)
    assert MODULE.exact_json_equal(stored, resumed)
    assert first_hash == second_hash
    assert MODULE.run_config_path(output).read_bytes() == before

    changed = json.loads(json.dumps(binding))
    changed["limits"]["static"]["workers"] = 7
    with pytest.raises(MODULE.StrictJSONError, match="resource limits"):
        MODULE.ensure_run_config(output, changed, resume=True)


def test_run_config_resume_rejects_semantically_equal_noncanonical_bytes(
    tmp_path: Path,
) -> None:
    output, operational = roots(tmp_path)
    binding = MODULE.build_mock_binding(output, operational)
    MODULE.ensure_run_config(output, binding, resume=False)
    target = MODULE.run_config_path(output)
    noncanonical = (json.dumps(binding, indent=2, sort_keys=False) + "\n").encode()
    assert noncanonical != MODULE.canonical_json_bytes(binding)
    target.write_bytes(noncanonical)
    before = target.read_bytes()
    with pytest.raises(MODULE.StrictJSONError, match="noncanonical JSON bytes"):
        MODULE.ensure_run_config(output, binding, resume=True)
    assert target.read_bytes() == before


def test_atomic_static_cell_and_manifest_contract(tmp_path: Path) -> None:
    output, operational, binding, config_hash = initialize(tmp_path)
    cell = MODULE.CellKey(128, "S000")
    state, manifest = MODULE.commit_mock_static_cell(
        output, operational, cell, binding["matrix_id"], config_hash
    )
    assert state == "COMMITTED"
    directory = MODULE.static_cell_path(output, cell)
    assert {path.name for path in directory.iterdir()} == {"proof.json", "record.json"}
    assert not MODULE.staging_path(operational, cell, config_hash).exists()
    assert MODULE.static_manifest_path(output, cell).is_file()
    record = MODULE.strict_json_load(directory / "record.json")
    assert set(record) == {
        "schema_version",
        "protocol_id",
        "artifact_role",
        "artifact_status",
        "authority",
        "mock_only",
        "cell",
        "matrix_id",
        "main_freeze_sha256",
        "run_config_sha256",
        "scheduler_classification",
        "evaluator_status",
        "returncode",
        "evaluator_payload",
        "scientific_licensing_enabled",
        "claim_boundary",
        "component_status",
        "milestone_status",
        "theorem_status",
        "final_status",
    }
    assert record["main_freeze_sha256"] is None
    assert record["evaluator_payload"] == {
        "path": "proof.json",
        "sha256": MODULE.sha256(directory / "proof.json"),
        "size_bytes": (directory / "proof.json").stat().st_size,
    }
    assert set(manifest) == {
        "schema_version",
        "protocol_id",
        "artifact_role",
        "artifact_status",
        "authority",
        "mock_only",
        "cell",
        "matrix_id",
        "main_freeze_sha256",
        "run_config_sha256",
        "scheduler_classification",
        "evaluator_status",
        "files",
        "scientific_licensing_enabled",
        "claim_boundary",
        "component_status",
        "milestone_status",
        "theorem_status",
        "final_status",
    }
    assert manifest["main_freeze_sha256"] is None
    assert manifest["component_status"] is None
    assert manifest["milestone_status"] is None
    assert manifest["theorem_status"] is None
    assert manifest["final_status"] is None
    checked = MODULE.validate_static_manifest(
        output, cell, binding["matrix_id"], config_hash
    )
    assert MODULE.exact_json_equal(manifest, checked)


def test_committed_cell_resume_is_read_only(tmp_path: Path) -> None:
    output, operational, binding, config_hash = initialize(tmp_path)
    cell = MODULE.CellKey(256, "S050")
    MODULE.commit_mock_static_cell(
        output, operational, cell, binding["matrix_id"], config_hash
    )
    directory = MODULE.static_cell_path(output, cell)
    manifest_path = MODULE.static_manifest_path(output, cell)
    before = {
        "proof": (directory / "proof.json").read_bytes(),
        "record": (directory / "record.json").read_bytes(),
        "manifest": manifest_path.read_bytes(),
    }
    state, _ = MODULE.commit_mock_static_cell(
        output, operational, cell, binding["matrix_id"], config_hash
    )
    assert state == "RESUMED_COMMITTED"
    assert (directory / "proof.json").read_bytes() == before["proof"]
    assert (directory / "record.json").read_bytes() == before["record"]
    assert manifest_path.read_bytes() == before["manifest"]


def test_manifestless_crash_recovers_without_rewriting_cell(tmp_path: Path) -> None:
    output, operational, binding, config_hash = initialize(tmp_path)
    cell = MODULE.CellKey(128, "S025")
    with pytest.raises(MODULE.SyntheticCrash):
        MODULE.commit_mock_static_cell(
            output,
            operational,
            cell,
            binding["matrix_id"],
            config_hash,
            fail_after_cell_rename=True,
        )
    directory = MODULE.static_cell_path(output, cell)
    assert directory.is_dir()
    assert not MODULE.static_manifest_path(output, cell).exists()
    proof_before = (directory / "proof.json").read_bytes()
    record_before = (directory / "record.json").read_bytes()

    state, manifest = MODULE.commit_mock_static_cell(
        output, operational, cell, binding["matrix_id"], config_hash
    )
    assert state == "RECOVERED_MANIFEST"
    assert manifest["mock_only"] is True
    assert (directory / "proof.json").read_bytes() == proof_before
    assert (directory / "record.json").read_bytes() == record_before


def test_corrupt_manifestless_cell_fails_without_overwrite(tmp_path: Path) -> None:
    output, operational, binding, config_hash = initialize(tmp_path)
    cell = MODULE.CellKey(128, "S001")
    with pytest.raises(MODULE.SyntheticCrash):
        MODULE.commit_mock_static_cell(
            output,
            operational,
            cell,
            binding["matrix_id"],
            config_hash,
            fail_after_cell_rename=True,
        )
    proof = MODULE.static_cell_path(output, cell) / "proof.json"
    proof.write_text('{"corrupt":true}\n', encoding="utf-8")
    corrupt = proof.read_bytes()
    with pytest.raises(MODULE.CorruptGeneration):
        MODULE.commit_mock_static_cell(
            output, operational, cell, binding["matrix_id"], config_hash
        )
    assert proof.read_bytes() == corrupt
    assert not MODULE.static_manifest_path(output, cell).exists()


def test_live_complete_staging_is_published_on_resume(tmp_path: Path) -> None:
    output, operational, binding, config_hash = initialize(tmp_path)
    cell = MODULE.CellKey(256, "S002")
    stage = MODULE.staging_path(operational, cell, config_hash)
    MODULE.write_mock_stage(stage, cell, binding["matrix_id"], config_hash)
    assert stage.is_dir()
    state, _ = MODULE.commit_mock_static_cell(
        output, operational, cell, binding["matrix_id"], config_hash
    )
    assert state == "COMMITTED"
    assert not stage.exists()
    assert MODULE.static_manifest_path(output, cell).is_file()


def test_static_staging_scan_rejects_hidden_foreign_and_duplicate_owners(
    tmp_path: Path,
) -> None:
    output, operational, binding, config_hash = initialize(tmp_path)
    precision_root = operational / "staging/static/128"
    precision_root.mkdir(parents=True)
    invalid = precision_root / ".unexpected"
    invalid.mkdir()
    with pytest.raises(MODULE.CorruptGeneration, match="invalid static staging"):
        MODULE.commit_mock_static_cell(
            output,
            operational,
            MODULE.CellKey(128, "S000"),
            binding["matrix_id"],
            config_hash,
        )
    invalid.rmdir()

    foreign = precision_root / ".S000.tmp-ffffffffffffffff-0"
    foreign.mkdir()
    with pytest.raises(MODULE.CorruptGeneration, match="foreign-generation"):
        MODULE.validate_static_staging_namespace(operational, config_hash)
    foreign.rmdir()

    first = precision_root / f".S000.tmp-{config_hash[:16]}-0"
    second = precision_root / f".S000.tmp-{config_hash[:16]}-1"
    second.mkdir()
    with pytest.raises(MODULE.CorruptGeneration, match="noncanonical active"):
        MODULE.commit_mock_static_cell(
            output,
            operational,
            MODULE.CellKey(128, "S000"),
            binding["matrix_id"],
            config_hash,
        )
    second.rmdir()
    first.mkdir()
    second.mkdir()
    with pytest.raises(MODULE.CorruptGeneration, match="multiple active"):
        MODULE.validate_static_staging_namespace(operational, config_hash)


def test_cell_rename_flushes_staging_then_canonical_parent(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    output, operational, binding, config_hash = initialize(tmp_path)
    cell = MODULE.CellKey(128, "S003")
    stage = MODULE.staging_path(operational, cell, config_hash)
    target = MODULE.static_cell_path(output, cell)
    events: list[tuple[str, Path, Path | None]] = []
    original_rename = MODULE.rename_directory_noreplace
    original_fsync = MODULE.fsync_directory

    def tracked_rename(source: Path, destination: Path) -> None:
        events.append(("rename", Path(source), Path(destination)))
        original_rename(source, destination)

    def tracked_fsync(path: Path) -> None:
        events.append(("fsync", Path(path), None))
        original_fsync(path)

    monkeypatch.setattr(MODULE, "rename_directory_noreplace", tracked_rename)
    monkeypatch.setattr(MODULE, "fsync_directory", tracked_fsync)
    MODULE.commit_mock_static_cell(
        output, operational, cell, binding["matrix_id"], config_hash
    )
    rename_index = events.index(("rename", stage, target))
    assert events[rename_index + 1] == ("fsync", stage.parent, None)
    assert events[rename_index + 2] == ("fsync", target.parent, None)


def test_whole_generation_quarantine_preserves_authoritative_and_operational(
    tmp_path: Path,
) -> None:
    output, operational, binding, config_hash = initialize(tmp_path)
    cell = MODULE.CellKey(128, "S000")
    MODULE.commit_mock_static_cell(
        output, operational, cell, binding["matrix_id"], config_hash
    )
    marker = operational / "telemetry.txt"
    marker.write_text("preserve me\n", encoding="utf-8")
    q_output, q_operational = MODULE.quarantine_incompatible_generation(
        output, "RUN_CONFIG_BINDING_MISMATCH"
    )
    assert not output.exists()
    assert not operational.exists()
    assert (q_output / "run_config.json").is_file()
    assert (q_output / "QUARANTINE_RECORD.json").is_file()
    assert q_operational is not None
    assert (q_operational / "telemetry.txt").read_text(encoding="utf-8") == "preserve me\n"
    record = MODULE.strict_json_load(q_output / "QUARANTINE_RECORD.json")
    assert record["reason"] == "RUN_CONFIG_BINDING_MISMATCH"
    assert record["operational_present"] is True
    assert MODULE.HEX_SHA256.fullmatch(record["transaction_journal_sha256"])
    assert record["milestone_status"] is None
    assert record["final_status"] is None
    assert not MODULE.quarantine_journal_path(output).exists()


@pytest.mark.parametrize("failure_point", sorted(MODULE.QUARANTINE_FAILURE_POINTS))
def test_quarantine_journal_recovers_every_durable_boundary(
    tmp_path: Path, failure_point: str
) -> None:
    output, operational, binding, config_hash = initialize(tmp_path)
    MODULE.commit_mock_static_cell(
        output,
        operational,
        MODULE.CellKey(128, "S000"),
        binding["matrix_id"],
        config_hash,
    )
    marker = operational / "telemetry.txt"
    marker.write_text("recoverable\n", encoding="utf-8")
    with pytest.raises(MODULE.SyntheticQuarantineCrash):
        MODULE.quarantine_incompatible_generation(
            output,
            "BOUNDARY_TEST",
            fail_at=failure_point,
        )
    journal = MODULE.quarantine_journal_path(output)
    assert journal.is_file()
    q_output, q_operational = MODULE.recover_quarantine_transaction(output)
    assert not output.exists()
    assert not operational.exists()
    assert not journal.exists()
    assert q_operational is not None
    assert (q_output / "run_config.json").is_file()
    assert (q_output / "QUARANTINE_RECORD.json").is_file()
    assert (q_operational / "telemetry.txt").read_text(encoding="utf-8") == "recoverable\n"


def test_mock_resume_completes_pending_quarantine_then_fails_closed(
    tmp_path: Path,
) -> None:
    output, operational, _binding, _config_hash = initialize(tmp_path)
    with pytest.raises(MODULE.SyntheticQuarantineCrash):
        MODULE.quarantine_incompatible_generation(
            output,
            "RESUME_RECOVERY_TEST",
            fail_at="AFTER_AUTHORITATIVE_RENAME",
        )
    with pytest.raises(MODULE.RunBindingMismatch, match="quarantined generation"):
        MODULE.run_mock_static(output, 0, resume=True)
    q_output, q_operational = MODULE.quarantine_paths(output, 1)
    assert q_output.is_dir()
    assert q_operational.is_dir()
    assert (q_output / "QUARANTINE_RECORD.json").is_file()
    assert not MODULE.quarantine_journal_path(output).exists()


def test_mock_output_cannot_use_canonical_production_namespace() -> None:
    for path in (
        MODULE.CANONICAL_RESULT,
        MODULE.CANONICAL_RESULT / "child",
        MODULE.CANONICAL_OPERATIONAL,
        MODULE.CANONICAL_OPERATIONAL / "child",
    ):
        with pytest.raises(MODULE.PathContractError):
            MODULE.ensure_mock_output_allowed(path)


def test_production_and_initialize_only_fail_before_output_creation(tmp_path: Path) -> None:
    for mode in ("--production", "--initialize-only"):
        output = tmp_path / mode.removeprefix("--")
        completed = subprocess.run(
            [sys.executable, str(SCRIPT), mode, "--output", str(output)],
            text=True,
            capture_output=True,
            check=False,
        )
        assert completed.returncode == 1
        assert "production rejected" in completed.stderr
        assert not output.exists()


def test_formal_authority_exact_53_role_handshake_and_initialize_only(
    tmp_path: Path,
) -> None:
    authority = formal_authority_fixture(tmp_path)
    output = (tmp_path / "formal-preflight-output").absolute()
    snapshot = MODULE.load_formal_authority(authority)
    assert len(snapshot.input_roles) == 53
    assert tuple(item.role for item in snapshot.input_roles) == tuple(
        role for role, _ in MODULE.FORMAL_INPUT_ROLES
    )
    assert snapshot.main_freeze_sha256 == MODULE.sha256(snapshot.main_freeze_path)

    completed = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--initialize-only",
            "--authority-root",
            str(authority),
            "--output",
            str(output),
        ],
        text=True,
        capture_output=True,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr
    result = json.loads(completed.stdout)
    assert result["artifact_status"] == "SEALED_CONTROL_PLANE_BINDING"
    assert result["input_role_count"] == 53
    assert result["freeze_sha256"] == result["main_freeze_sha256"]
    assert result["production_authorized"] is False
    assert result["scientific_licensing_enabled"] is False
    assert {path.name for path in output.iterdir()} == {"run_config.json"}
    config = MODULE.strict_json_load(output / "run_config.json", require_canonical=True)
    assert config["artifact_role"] == "RUN_CONFIG"
    assert config["authority"] == "PRODUCER_ONLY"
    assert config["dispatch_authorized_by_artifact"] is False
    assert config["scientific_licensing_enabled"] is False
    assert config["freeze_sha256"] == config["main_freeze_sha256"]
    assert config["component_status"] is None
    assert not MODULE.operational_root_for(output).exists()


def test_exact_machine_schema_raw_calibration_and_build_receipt_fail_closed(
    tmp_path: Path,
) -> None:
    authority = formal_authority_fixture(tmp_path)
    machine_path = authority / dict(MODULE.FORMAL_INPUT_ROLES)["machine_freeze"]
    machine = MODULE.strict_json_load(machine_path, require_canonical=True)
    MODULE._validate_formal_machine_envelope(machine)

    forged = json.loads(json.dumps(machine))
    forged["extra"] = None
    with pytest.raises(MODULE.StrictJSONError, match="key set"):
        MODULE._validate_formal_machine_envelope(forged)

    forged = json.loads(json.dumps(machine))
    forged["machine_observations"]["logical_cpu_count"] = True
    with pytest.raises(MODULE.SchedulerContractError):
        MODULE._validate_formal_machine_envelope(forged)

    for alias_field in (
        "python_flint_record_sha256",
        "python_flint_installed_manifest_root_sha256",
    ):
        forged = json.loads(json.dumps(machine))
        forged["python_arb"][alias_field] = forged["python_arb"][
            "conda_installed_manifest_root_sha256"
        ]
        with pytest.raises(MODULE.ProductionAuthorityError, match="pairwise distinct"):
            MODULE._validate_formal_machine_envelope(forged)

    forged = json.loads(json.dumps(machine))
    static_payload = MODULE.strict_json_loads(
        forged["resource_evidence"]["static_payload_raw_utf8"]
    )
    static_payload["unknown"] = None
    raw = MODULE.canonical_json_bytes(static_payload)
    forged["resource_evidence"]["static_payload_raw_utf8"] = raw.decode("utf-8")
    forged["resource_evidence"]["static_payload_sha256"] = MODULE.sha256_bytes(raw)
    with pytest.raises(MODULE.StrictJSONError, match="key set"):
        MODULE._validate_formal_machine_envelope(forged)

    forged = json.loads(json.dumps(machine))
    branch_payload = MODULE.strict_json_loads(
        forged["resource_evidence"]["branch_payload_raw_utf8"]
    )
    compact = MODULE.canonical_json_bytes(branch_payload)
    forged["resource_evidence"]["branch_payload_raw_utf8"] = compact.decode("utf-8")
    forged["resource_evidence"]["branch_payload_sha256"] = MODULE.sha256_bytes(compact)
    with pytest.raises(MODULE.ProductionAuthorityError, match="PRETTY"):
        MODULE._validate_formal_machine_envelope(forged)

    forged = json.loads(json.dumps(machine))
    forged["compiler"]["fresh_rebuild_receipt"]["argv"][1:3] = list(
        reversed(forged["compiler"]["fresh_rebuild_receipt"]["argv"][1:3])
    )
    forged["compiler"]["fresh_rebuild_receipt"]["argv_sha256"] = MODULE.sha256_bytes(
        MODULE.canonical_json_bytes(
            forged["compiler"]["fresh_rebuild_receipt"]["argv"]
        )
    )
    with pytest.raises(MODULE.ProductionAuthorityError, match="actual argv"):
        MODULE._validate_formal_machine_envelope(forged)

    forged = json.loads(json.dumps(machine))
    forged["capd"]["tree_algorithm"] = "GIT_STATUS_ALIAS"
    with pytest.raises(MODULE.ProductionAuthorityError, match="tree algorithm"):
        MODULE._validate_formal_machine_envelope(forged)

    forged = json.loads(json.dumps(machine))
    forged["branch_binary"]["build_id"] = "0" * 40
    with pytest.raises(MODULE.ProductionAuthorityError, match="binary/source live"):
        MODULE._validate_formal_machine_envelope(forged)

    forged = json.loads(json.dumps(machine))
    static_payload = MODULE.strict_json_loads(
        forged["resource_evidence"]["static_payload_raw_utf8"]
    )
    static_payload["bindings"]["python_flint"]["module_path"] = (
        "/root/miniconda3/lib/python3.12/site-packages/flint/typing.py"
    )
    static_raw = MODULE.canonical_json_bytes(static_payload)
    forged["resource_evidence"]["static_payload_raw_utf8"] = static_raw.decode(
        "utf-8"
    )
    forged["resource_evidence"]["static_payload_sha256"] = MODULE.sha256_bytes(
        static_raw
    )
    with pytest.raises(MODULE.ProductionAuthorityError, match="site-packages"):
        MODULE._validate_formal_machine_envelope(forged)


def test_pure_machine_builder_success_and_deterministic_serializer(
    tmp_path: Path,
) -> None:
    authority = formal_authority_fixture(tmp_path)
    machine = MODULE.strict_json_load(
        authority / dict(MODULE.FORMAL_INPUT_ROLES)["machine_freeze"],
        require_canonical=True,
    )
    first = pure_machine_candidate(machine)
    second = pure_machine_candidate(machine)
    assert first == second == machine
    assert len(first) == len(MODULE.MACHINE_FREEZE_KEYS) == 23
    assert MODULE.canonical_json_bytes(first) == MODULE.canonical_json_bytes(second)
    assert MODULE.strict_json_loads(
        MODULE.canonical_json_bytes(first).decode("utf-8")
    ) == first
    assert first["production_authorized"] is False
    assert first["compiler"]["fresh_rebuild_receipt"]["shell_used"] is False


def test_pure_machine_builder_rejects_stale_calibration_and_build_mismatch(
    tmp_path: Path,
) -> None:
    authority = formal_authority_fixture(tmp_path)
    machine = MODULE.strict_json_load(
        authority / dict(MODULE.FORMAL_INPUT_ROLES)["machine_freeze"],
        require_canonical=True,
    )
    stale = json.loads(json.dumps(machine))
    branch = MODULE.strict_json_loads(
        stale["resource_evidence"]["branch_payload_raw_utf8"]
    )
    branch["binary_sha256"] = "0" * 64
    stale["resource_evidence"]["branch_payload_raw_utf8"] = (
        MODULE.pretty_json_bytes(branch).decode("utf-8")
    )
    with pytest.raises(MODULE.ProductionAuthorityError, match="stale"):
        pure_machine_candidate(stale)

    mismatch = json.loads(json.dumps(machine))
    mismatch["compiler"]["fresh_rebuild_receipt"]["output_sha256"] = "0" * 64
    with pytest.raises(
        MODULE.ProductionAuthorityError,
        match="recipe/receipt differs",
    ):
        MODULE._validate_formal_machine_envelope(mismatch)

    forged_dispatch = [
        str(ROOT / dict(MODULE.FORMAL_INPUT_ROLES)["static_evaluator"]),
        "--slab-id", "S000",
    ]
    with pytest.raises(
        MODULE.ProductionAuthorityError, match="scientific dispatch"
    ):
        MODULE._capture_command(
            forged_dispatch,
            cwd=ROOT,
            environment=MODULE.formal_build_environment(),
            timeout_seconds=1,
        )


def test_machine_capture_paths_are_tmp_only_write_once_and_unaliased(
    tmp_path: Path,
) -> None:
    target = tmp_path / "machine-candidate.json"
    assert MODULE.machine_capture_output_path(str(target)) == target
    for invalid in (
        "relative.json",
        "/var/tmp/machine-candidate.json",
        str(ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_MACHINE_FREEZE.json"),
        str(tmp_path / "nested/../machine.json"),
    ):
        with pytest.raises(MODULE.PathContractError):
            MODULE.machine_capture_output_path(invalid)

    target.write_bytes(b"existing\n")
    with pytest.raises(MODULE.PathContractError, match="already exists"):
        MODULE.machine_capture_output_path(str(target))
    target.unlink()
    target.symlink_to(tmp_path / "missing-target")
    with pytest.raises(MODULE.PathContractError, match="already exists"):
        MODULE.machine_capture_output_path(str(target))

    calibration = tmp_path / "calibration.json"
    calibration.write_bytes(MODULE.canonical_json_bytes({"fixture": True}))
    alias = tmp_path / "calibration-alias.json"
    os.link(calibration, alias)
    with pytest.raises(MODULE.PathContractError, match="hard-link"):
        MODULE._machine_tmp_file(
            str(calibration), "fixture calibration", serializer="CJ_COMPACT_V1"
        )


def test_machine_capture_cli_is_exact_exclusive_and_never_dispatches(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    authority = formal_authority_fixture(tmp_path)
    machine = MODULE.strict_json_load(
        authority / dict(MODULE.FORMAL_INPUT_ROLES)["machine_freeze"],
        require_canonical=True,
    )
    calls: list[dict[str, object]] = []

    def fake_capture(**kwargs: object) -> tuple[dict[str, object], str]:
        calls.append(dict(kwargs))
        return machine, "a" * 64

    monkeypatch.setattr(
        MODULE, "capture_and_publish_formal_machine_freeze", fake_capture
    )
    arguments = [
        "--capture-machine-freeze",
        "--authority-root", str(ROOT),
        "--static-calibration", str(tmp_path / "static.json"),
        "--branch-calibration", str(tmp_path / "branch.json"),
        "--output", str(tmp_path / "candidate.json"),
    ]
    assert MODULE.main(arguments) == 0
    summary = json.loads(capsys.readouterr().out)
    assert summary == {
        "artifact_role": "TEMP_MACHINE_FREEZE_CANDIDATE",
        "artifact_status": "CAPTURED_VALIDATED_TEMP_ONLY",
        "authority": "MACHINE_ADMISSION_ONLY",
        "candidate_sha256": "a" * 64,
        "machine_artifact_role": "MACHINE_FREEZE",
        "machine_status": "FROZEN_FOR_PRODUCTION",
        "output_path": str(tmp_path / "candidate.json"),
        "serializer": "CJ_COMPACT_V1",
        "production_authorized": False,
        "scientific_dispatch_performed": False,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    assert len(calls) == 1

    assert MODULE.main([*arguments, "--production"]) == 1
    error = capsys.readouterr().err
    assert "exact-exclusive" in error
    assert len(calls) == 1


def test_capture_command_timeout_kills_the_whole_process_group(
    tmp_path: Path,
) -> None:
    original_subreaper_state = MODULE._capture_child_subreaper_state()
    child_pid_path = tmp_path / "descendant.pid"
    source = (
        "import pathlib,subprocess,sys,time;"
        "p=subprocess.Popen([sys.executable,'-c','import time;time.sleep(30)']);"
        f"pathlib.Path({str(child_pid_path)!r}).write_text(str(p.pid));"
        "time.sleep(30)"
    )
    with pytest.raises(MODULE.ProductionAuthorityError, match="timed out"):
        MODULE._capture_command(
            [sys.executable, "-I", "-c", source],
            cwd=ROOT,
            environment=MODULE.formal_build_environment(),
            timeout_seconds=1,
        )
    assert MODULE._capture_child_subreaper_state() is original_subreaper_state
    assert child_pid_path.is_file()
    descendant = int(child_pid_path.read_text(encoding="ascii"))
    for _ in range(100):
        if not Path(f"/proc/{descendant}").exists():
            break
        time.sleep(0.02)
    assert not Path(f"/proc/{descendant}").exists()


def test_machine_candidate_roundtrips_independent_release_validator(
    tmp_path: Path,
) -> None:
    authority = formal_authority_fixture(tmp_path)
    machine_path = authority / dict(MODULE.FORMAL_INPUT_ROLES)["machine_freeze"]
    machine = MODULE.strict_json_load(machine_path, require_canonical=True)
    assert pure_machine_candidate(machine) == machine
    expected_role_hashes = {
        role: MODULE.sha256(authority / relative)
        for role, relative in MODULE.FORMAL_INPUT_ROLES
    }
    release = load_release_builder()
    validated = release.validate_formal_machine_freeze(
        authority,
        machine_path=machine_path,
        expected_role_hashes=expected_role_hashes,
    )
    assert validated["artifact_role"] == "MACHINE_FREEZE"
    assert validated["production_authorized"] is False


def test_capd_index_must_equal_detached_head_tree(tmp_path: Path) -> None:
    authority = formal_authority_fixture(tmp_path)
    machine_path = authority / dict(MODULE.FORMAL_INPUT_ROLES)["machine_freeze"]
    machine = MODULE.strict_json_load(machine_path, require_canonical=True)
    checkout = Path(machine["capd"]["checkout_path"])
    (checkout / "README.md").write_bytes(b"staged but not committed\n")
    subprocess.run(
        ["git", "-C", str(checkout), "add", "README.md"], check=True
    )
    with pytest.raises(
        MODULE.ProductionAuthorityError,
        match="index tree differs from detached HEAD tree",
    ):
        MODULE.recompute_capd_git_index_tree(str(checkout))


def test_machine_live_toolchain_rejects_coherent_self_rebinding(
    tmp_path: Path,
) -> None:
    authority = formal_authority_fixture(tmp_path)
    machine_path = authority / dict(MODULE.FORMAL_INPUT_ROLES)["machine_freeze"]
    machine = MODULE.strict_json_load(machine_path, require_canonical=True)

    forged = json.loads(json.dumps(machine))
    forged["capture"]["boot_id_sha256"] = "0" * 64
    with pytest.raises(MODULE.ProductionAuthorityError, match="boot ID"):
        MODULE._validate_formal_machine_envelope(forged)

    forged = json.loads(json.dumps(machine))
    forged["capture"]["captured_at_utc"] = "2000-01-01T00:00:00Z"
    with pytest.raises(MODULE.ProductionAuthorityError, match="live boot window"):
        MODULE._validate_formal_machine_envelope(forged)

    forged = json.loads(json.dumps(machine))
    forged["machine_observations"]["result_parent_free_bytes"] = 1
    forged["resource_admission"]["storage_launch_passed"] = False
    with pytest.raises(MODULE.ProductionAuthorityError, match="admission did not pass"):
        MODULE._validate_formal_machine_envelope(forged)

    forged = json.loads(json.dumps(machine))
    forged["compiler"]["executable_sha256"] = "0" * 64
    with pytest.raises(MODULE.ProductionAuthorityError, match="compiler executable"):
        MODULE._validate_formal_machine_envelope(forged)

    forged = json.loads(json.dumps(machine))
    forged["compiler"]["version"] = "g++ forged 11.4.0"
    with pytest.raises(MODULE.ProductionAuthorityError, match="compiler version"):
        MODULE._validate_formal_machine_envelope(forged)

    forged = json.loads(json.dumps(machine))
    forged["compiler"]["fresh_rebuild_receipt"]["return_code"] = 0.0
    with pytest.raises(MODULE.ProductionAuthorityError, match="receipt"):
        MODULE._validate_formal_machine_envelope(forged)

    forged = json.loads(json.dumps(machine))
    forged["compiler"]["fresh_rebuild_receipt"]["umask"] = "0002"
    with pytest.raises(MODULE.ProductionAuthorityError, match="umask"):
        MODULE._validate_formal_machine_envelope(forged)

    forged = json.loads(json.dumps(machine))
    forged["compiler"]["fresh_rebuild_receipt"]["stdout"] = "forged\n"
    forged["compiler"]["fresh_rebuild_receipt"]["stdout_sha256"] = MODULE.sha256_bytes(
        b"forged\n"
    )
    with pytest.raises(MODULE.ProductionAuthorityError, match="receipt"):
        MODULE._validate_formal_machine_envelope(forged)

    forged = json.loads(json.dumps(machine))
    forged["python_arb"]["executable_sha256"] = "0" * 64
    with pytest.raises(MODULE.ProductionAuthorityError, match="Python executable"):
        MODULE._validate_formal_machine_envelope(forged)

    forged = json.loads(json.dumps(machine))
    forged_version = "3.12.3 | forged self-consistent version"
    forged["python_arb"]["python_version"] = forged_version
    static_payload = MODULE.strict_json_loads(
        forged["resource_evidence"]["static_payload_raw_utf8"]
    )
    static_payload["bindings"]["interpreter"]["version"] = forged_version
    static_raw = MODULE.canonical_json_bytes(static_payload)
    forged["resource_evidence"]["static_payload_raw_utf8"] = static_raw.decode(
        "utf-8"
    )
    forged["resource_evidence"]["static_payload_sha256"] = MODULE.sha256_bytes(
        static_raw
    )
    with pytest.raises(MODULE.ProductionAuthorityError, match="version binding"):
        MODULE._validate_formal_machine_envelope(forged)

    forged = json.loads(json.dumps(machine))
    forged["python_arb"]["arb_extension"]["build_id"] = "0" * 40
    with pytest.raises(MODULE.ProductionAuthorityError, match="GNU build-id"):
        MODULE._validate_formal_machine_envelope(forged)

    forged = json.loads(json.dumps(machine))
    forged["runtime_libraries"]["capd_system"][0]["build_id"] = "f" * 40
    forged["branch_binary"]["runtime_libraries_sha256"] = MODULE.sha256_bytes(
        MODULE.canonical_json_bytes(forged["runtime_libraries"])
    )
    with pytest.raises(MODULE.ProductionAuthorityError, match="build-id"):
        MODULE._validate_formal_machine_envelope(forged)

    forged = json.loads(json.dumps(machine))
    forged_record_sha = "7" * 64
    forged["python_arb"]["python_flint_record_sha256"] = forged_record_sha
    static_payload = MODULE.strict_json_loads(
        forged["resource_evidence"]["static_payload_raw_utf8"]
    )
    static_payload["bindings"]["python_flint"]["record_sha256"] = (
        forged_record_sha
    )
    static_raw = MODULE.canonical_json_bytes(static_payload)
    forged["resource_evidence"]["static_payload_raw_utf8"] = static_raw.decode(
        "utf-8"
    )
    forged["resource_evidence"]["static_payload_sha256"] = MODULE.sha256_bytes(
        static_raw
    )
    with pytest.raises(MODULE.ProductionAuthorityError, match="frozen RECORD"):
        MODULE._validate_formal_machine_envelope(forged)


def test_machine_resource_receipts_reject_coherent_semantic_rebinding(
    tmp_path: Path,
) -> None:
    authority = formal_authority_fixture(tmp_path)
    machine = MODULE.strict_json_load(
        authority / dict(MODULE.FORMAL_INPUT_ROLES)["machine_freeze"],
        require_canonical=True,
    )

    def forged_static(mutator: object) -> dict[str, object]:
        forged = json.loads(json.dumps(machine))
        payload = MODULE.strict_json_loads(
            forged["resource_evidence"]["static_payload_raw_utf8"]
        )
        assert callable(mutator)
        mutator(payload)
        raw = MODULE.canonical_json_bytes(payload)
        forged["resource_evidence"]["static_payload_raw_utf8"] = raw.decode(
            "utf-8"
        )
        forged["resource_evidence"]["static_payload_sha256"] = (
            MODULE.sha256_bytes(raw)
        )
        return forged

    static_mutations = [
        lambda payload: payload["measurement"].__setitem__(
            "sample_interval_seconds", 0.06
        ),
        lambda payload: payload["sequential_runs"][0]["argv"].__setitem__(
            7, "0.9999"
        ),
        lambda payload: payload["concurrent_runs"][0].__setitem__(
            "label", "forged-label"
        ),
        lambda payload: (
            payload["sequential_runs"][0].__setitem__("stdout_bytes", 1),
            payload["sequential_runs"][0].__setitem__(
                "stdout_sha256", MODULE.sha256_bytes(b"x")
            ),
        ),
        lambda payload: (
            payload["sequential_runs"][0].__setitem__("output", "/etc/passwd"),
            payload["sequential_runs"][0]["argv"].__setitem__(-1, "/etc/passwd"),
        ),
        lambda payload: payload["measurement"].__setitem__(
            "baseline_samples_bytes",
            payload["measurement"]["baseline_samples_bytes"][:-1],
        ),
        lambda payload: payload["bindings"]["evaluator"].__setitem__(
            "mode", "0600"
        ),
    ]
    for mutator in static_mutations:
        with pytest.raises(MODULE.SchedulerContractError):
            MODULE._validate_formal_machine_envelope(forged_static(mutator))

    def forged_branch(mutator: object) -> dict[str, object]:
        forged = json.loads(json.dumps(machine))
        payload = MODULE.strict_json_loads(
            forged["resource_evidence"]["branch_payload_raw_utf8"]
        )
        assert callable(mutator)
        mutator(payload)
        raw = MODULE.pretty_json_bytes(payload)
        forged["resource_evidence"]["branch_payload_raw_utf8"] = raw.decode(
            "utf-8"
        )
        forged["resource_evidence"]["branch_payload_sha256"] = (
            MODULE.sha256_bytes(raw)
        )
        return forged

    branch_mutations = [
        lambda payload: payload.__setitem__("binary_sha256", "7" * 64),
        lambda payload: payload["results"][0]["argv"].__setitem__(
            2, "0.9999"
        ),
        lambda payload: payload.__setitem__(
            "baseline_samples_bytes", payload["baseline_samples_bytes"][:-1]
        ),
        lambda payload: payload["results"][0].__setitem__("stdout_bytes", 0),
        lambda payload: payload["results"][0].__setitem__(
            "stderr_sha256", MODULE.sha256_bytes(b"forged stderr")
        ),
    ]
    for mutator in branch_mutations:
        with pytest.raises(MODULE.SchedulerContractError):
            MODULE._validate_formal_machine_envelope(forged_branch(mutator))

    # A zero sampled cgroup increment is a valid nonnegative lower-bound
    # observation; it does not relax the independent per-process RSS bound.
    zero_increment = forged_branch(
        lambda payload: (
            payload.__setitem__(
                "sampled_concurrent_peak_bytes",
                payload["baseline_conservative_bytes"],
            ),
            payload.__setitem__("sampled_concurrent_increment_bytes", 0),
        )
    )
    MODULE._validate_formal_machine_envelope(zero_increment)


def test_machine_persistent_binary_mode_is_exact_0755(tmp_path: Path) -> None:
    authority = formal_authority_fixture(tmp_path)
    machine_path = authority / dict(MODULE.FORMAL_INPUT_ROLES)["machine_freeze"]
    machine = MODULE.strict_json_load(machine_path, require_canonical=True)
    binary = authority / machine["branch_binary"]["path"]
    binary.chmod(0o750)
    machine["branch_binary"]["executable_mode"] = 0o750
    with pytest.raises(MODULE.ProductionAuthorityError, match="executable/ELF"):
        MODULE._validate_formal_machine_envelope(machine)


@pytest.mark.parametrize("target", ("project_binary", "static_evaluator", "compiler", "capd"))
def test_machine_live_authority_artifacts_reject_hardlink_aliases(
    tmp_path: Path, target: str
) -> None:
    authority = formal_authority_fixture(tmp_path)
    machine = MODULE.strict_json_load(
        authority / dict(MODULE.FORMAL_INPUT_ROLES)["machine_freeze"],
        require_canonical=True,
    )
    if target == "project_binary":
        path = authority / machine["branch_binary"]["path"]
    elif target == "static_evaluator":
        static = MODULE.strict_json_loads(
            machine["resource_evidence"]["static_payload_raw_utf8"]
        )
        path = Path(static["bindings"]["evaluator"]["path"])
    elif target == "compiler":
        path = Path(machine["compiler"]["executable_path"])
    else:
        path = Path(machine["capd"]["libcapd"]["path"])
    alias = path.with_name(f"{path.name}.hardlink-alias")
    os.link(path, alias)
    with pytest.raises(MODULE.PathContractError, match="hard-link"):
        MODULE._validate_formal_machine_envelope(machine)


def test_machine_external_symlink_is_replayed_at_transaction_end(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    authority = formal_authority_fixture(tmp_path)
    machine = MODULE.strict_json_load(
        authority / dict(MODULE.FORMAL_INPUT_ROLES)["machine_freeze"],
        require_canonical=True,
    )
    lexical = Path(machine["compiler"]["executable_path"])
    first = lexical.with_name("g++-target-a")
    second = lexical.with_name("g++-target-b")
    raw = lexical.read_bytes()
    lexical.rename(first)
    second.write_bytes(raw)
    first.chmod(0o755)
    second.chmod(0o755)
    lexical.symlink_to(first.name)

    real_statvfs = MODULE.os.statvfs
    swapped = False

    def swap_at_last_gate(path: object) -> object:
        nonlocal swapped
        if not swapped:
            swapped = True
            lexical.unlink()
            lexical.symlink_to(second.name)
        return real_statvfs(path)

    monkeypatch.setattr(MODULE.os, "statvfs", swap_at_last_gate)
    with pytest.raises(MODULE.PathContractError, match="changed during validation"):
        MODULE._validate_formal_machine_envelope(machine)


def test_machine_live_cpu_cgroup_and_disk_gates_are_not_declared_facts(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    authority = formal_authority_fixture(tmp_path)
    machine = MODULE.strict_json_load(
        authority / dict(MODULE.FORMAL_INPUT_ROLES)["machine_freeze"],
        require_canonical=True,
    )

    real_affinity = MODULE.os.sched_getaffinity
    monkeypatch.setattr(MODULE.os, "sched_getaffinity", lambda _pid: set(range(31)))
    with pytest.raises(MODULE.ProductionAuthorityError, match="CPU affinity"):
        MODULE._validate_formal_machine_envelope(machine)
    monkeypatch.setattr(MODULE.os, "sched_getaffinity", real_affinity)

    real_read_text = MODULE.Path.read_text

    def forged_cgroup(path: Path, *args: object, **kwargs: object) -> str:
        if str(path) == "/sys/fs/cgroup/memory/memory.limit_in_bytes":
            return "1\n"
        return real_read_text(path, *args, **kwargs)

    monkeypatch.setattr(MODULE.Path, "read_text", forged_cgroup)
    with pytest.raises(MODULE.ProductionAuthorityError, match="cgroup memory"):
        MODULE._validate_formal_machine_envelope(machine)
    monkeypatch.setattr(MODULE.Path, "read_text", real_read_text)

    real_statvfs = MODULE.os.statvfs
    statvfs_result = real_statvfs(ROOT / "results")
    low_disk = types.SimpleNamespace(
        f_bavail=1,
        f_frsize=statvfs_result.f_frsize,
    )
    monkeypatch.setattr(MODULE.os, "statvfs", lambda _path: low_disk)
    with pytest.raises(MODULE.ProductionAuthorityError, match="filesystem.*launch"):
        MODULE._validate_formal_machine_envelope(machine)


def test_exact_main_and_final_run_config_nested_schemas_fail_closed(
    tmp_path: Path,
) -> None:
    authority = formal_authority_fixture(tmp_path)
    snapshot = MODULE.load_formal_authority(authority)
    main = MODULE.strict_json_load(snapshot.main_freeze_path, require_canonical=True)
    MODULE._validate_formal_main_envelope(
        main, snapshot.input_roles, snapshot.machine_freeze_sha256
    )
    forged = json.loads(json.dumps(main))
    forged["serializers"]["branch_pretty_json"]["indent"] = 2.0
    with pytest.raises(MODULE.ProductionAuthorityError, match="serializers"):
        MODULE._validate_formal_main_envelope(
            forged, snapshot.input_roles, snapshot.machine_freeze_sha256
        )
    forged = json.loads(json.dumps(main))
    forged["execution_policy"]["branch_millisecond_migration_complete"] = False
    with pytest.raises(MODULE.ProductionAuthorityError, match="execution_policy"):
        MODULE._validate_formal_main_envelope(
            forged, snapshot.input_roles, snapshot.machine_freeze_sha256
        )
    forged = json.loads(json.dumps(main))
    forged["evaluators"]["static"]["sha256"] = "0" * 64
    with pytest.raises(MODULE.ProductionAuthorityError, match="evaluator"):
        MODULE._validate_formal_main_envelope(
            forged, snapshot.input_roles, snapshot.machine_freeze_sha256
        )

    output = (tmp_path / "exact-final-config").absolute()
    config = MODULE.build_formal_run_binding(snapshot, output)
    MODULE.validate_formal_run_binding(config, snapshot, output)
    assert set(config) == MODULE.FINAL_RUN_CONFIG_KEYS
    assert config["freeze_sha256"] == config["main_freeze_sha256"]
    assert config["execution_policy"]["branch_millisecond_migration_complete"] is True
    for mutation in (
        lambda item: item.update({"extra": None}),
        lambda item: item.update({"dispatch_authorized_by_artifact": True}),
        lambda item: item.update({"freeze_sha256": "0" * 64}),
    ):
        forged_config = json.loads(json.dumps(config))
        mutation(forged_config)
        with pytest.raises(MODULE.SchedulerContractError):
            MODULE.validate_formal_run_binding(forged_config, snapshot, output)


def test_formal_initialize_execute_xor_and_migration_gate(tmp_path: Path) -> None:
    authority = formal_authority_fixture(tmp_path)
    for index, flags in enumerate(
        (
            ("--initialize-only", "--resume"),
            ("--production",),
            ("--execute-scientific-dispatch", "--resume"),
            ("--production", "--execute-scientific-dispatch", "--resume"),
        )
    ):
        output = (tmp_path / f"xor-{index}").absolute()
        completed = subprocess.run(
            [
                sys.executable, str(SCRIPT), *flags, "--authority-root",
                str(authority), "--output", str(output),
            ],
            text=True,
            capture_output=True,
            check=False,
        )
        assert completed.returncode == 1
        assert "production" in completed.stderr or "XOR" in completed.stderr
        assert not output.exists()
    assert MODULE.formal_execution_policy()["branch_millisecond_migration_complete"] is True


def test_formal_preflight_cannot_resume_promote_or_use_canonical_root(
    tmp_path: Path,
) -> None:
    authority = formal_authority_fixture(tmp_path)
    output = (tmp_path / "formal-preflight-once").absolute()
    snapshot = MODULE.load_formal_authority(authority)
    config, _ = MODULE.initialize_formal_preflight(snapshot, output)
    before = (output / "run_config.json").read_bytes()
    with pytest.raises(MODULE.RunBindingMismatch, match="cannot be resumed or promoted"):
        MODULE.initialize_formal_preflight(snapshot, output)
    assert (output / "run_config.json").read_bytes() == before
    promoted = dict(config)
    promoted["dispatch_authorized_by_artifact"] = True
    with pytest.raises(MODULE.ProductionAuthorityError):
        MODULE.validate_formal_preflight_binding(promoted, snapshot, output)
    with pytest.raises(MODULE.PathContractError, match="canonical production"):
        MODULE.initialize_formal_preflight(snapshot, MODULE.CANONICAL_RESULT)

    rejected = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--production",
            "--execute-scientific-dispatch",
            "--resume",
            "--authority-root",
            str(authority),
            "--output",
            str(output),
        ],
        text=True,
        capture_output=True,
        check=False,
    )
    assert rejected.returncode == 1
    assert "unconditionally disabled" in rejected.stderr
    assert (output / "run_config.json").read_bytes() == before


def test_formal_authority_rejects_role_reorder_and_decorated_review(
    tmp_path: Path,
) -> None:
    authority = formal_authority_fixture(tmp_path)
    freeze_path = authority / "research/route_a_wave_trace/R401_VAL_L3_A1_FREEZE.json"
    freeze = MODULE.strict_json_load(freeze_path, require_canonical=True)
    freeze["input_roles"][0], freeze["input_roles"][1] = (
        freeze["input_roles"][1], freeze["input_roles"][0]
    )
    write_canonical_json(freeze_path, freeze)
    with pytest.raises(MODULE.ProductionAuthorityError, match="53-role"):
        MODULE.load_formal_authority(authority)

    authority = formal_authority_fixture(tmp_path / "second")
    review = authority / dict(MODULE.FORMAL_INPUT_ROLES)["prefreeze_review"]
    review.write_text(" Verdict: ACCEPT_FOR_FREEZE\n", encoding="utf-8")
    with pytest.raises(MODULE.ProductionAuthorityError):
        MODULE.load_formal_authority(authority)


@pytest.mark.parametrize(
    "extra",
    [
        "- Verdict: REJECT_FOR_FREEZE",
        "> Verdict: PENDING",
        "| Verdict | REJECT_FOR_FREEZE |",
        "**Verdict:** REJECT_FOR_FREEZE",
        "Verdict：PENDING",
        r"\Verdict: PENDING",
        "Verdict&#58; PENDING",
        "V&#101;rdict: PENDING",
        "V&#x65;rdict: PENDING",
        "Ver\u200bdict: PENDING",
        "Ver\ufe0fdict: PENDING",
        "Ver\u034fdict: PENDING",
        "V&#xFE0F;erdict: PENDING",
        "V&amp;#101;rdict: PENDING",
        "V&#101rdict: PENDING",
        "V&#x65rdict: PENDING",
        "V&#00101rdict: PENDING",
        "V&#x0065rdict: PENDING",
        "verdict = PENDING",
    ],
)
def test_formal_review_rejects_every_standalone_decorated_verdict(
    tmp_path: Path, extra: str
) -> None:
    authority = formal_authority_fixture(tmp_path)
    review = authority / dict(MODULE.FORMAL_INPUT_ROLES)["prefreeze_review"]
    review.write_text(
        f"{MODULE.PREFREEZE_ACCEPT_LINE}\n{extra}\n", encoding="utf-8"
    )
    with pytest.raises(MODULE.ProductionAuthorityError):
        MODULE.load_formal_authority(authority)


@pytest.mark.parametrize(
    "raw",
    [
        "relative/output",
        "/tmp/formal/../output",
        "//tmp/formal-output",
        "/tmp/formal-output/",
    ],
)
def test_formal_paths_reject_noncanonical_raw_spelling(raw: str) -> None:
    with pytest.raises(MODULE.PathContractError):
        MODULE.ensure_formal_preflight_output_allowed(raw, str(ROOT))


def test_formal_paths_reject_parent_symlinks(tmp_path: Path) -> None:
    real = tmp_path / "real"
    real.mkdir()
    alias = tmp_path / "alias"
    alias.symlink_to(real, target_is_directory=True)
    with pytest.raises(MODULE.PathContractError, match="symlink"):
        MODULE.ensure_formal_preflight_output_allowed(
            str(alias / "output"), str(ROOT)
        )
    authority = formal_authority_fixture(tmp_path / "fixture")
    authority_alias = tmp_path / "authority-alias"
    authority_alias.symlink_to(authority, target_is_directory=True)
    with pytest.raises(MODULE.PathContractError, match="symlink"):
        MODULE.load_formal_authority(str(authority_alias))


def test_formal_transaction_plans_are_exact_and_dispatch_stays_locked(
    tmp_path: Path,
) -> None:
    authority = formal_authority_fixture(tmp_path)
    output = (tmp_path / "formal-transaction-output").absolute()
    snapshot = MODULE.load_formal_authority(authority)
    binding, run_hash = MODULE.initialize_formal_preflight(snapshot, output)
    cell = MODULE.CellKey(128, "S000")
    static_plan = MODULE.build_formal_static_transaction_plan(
        snapshot, binding, run_hash, output, cell
    )
    assert len(static_plan.argv) == len(static_plan.semantic_argv) == 26
    assert static_plan.argv[-2] == "--output"
    assert static_plan.semantic_argv[-1] == "<STAGING_PROOF_PATH>"
    assert tuple(
        path.name
        for path in (
            static_plan.proof_path,
            static_plan.stdout_path,
            static_plan.stderr_path,
            static_plan.record_path,
        )
    ) == ("proof.json", "stdout.txt", "stderr.txt", "record.json")
    called: list[str] = []
    with pytest.raises(MODULE.ProductionAuthorityError, match="unconditionally"):
        MODULE.dispatch_formal_static_transaction(
            static_plan, executor=lambda *_: called.append("static")
        )
    assert called == []
    branch_plan = MODULE.build_formal_branch_transaction_plan(
        snapshot, binding, run_hash, output, cell
    )
    assert branch_plan.task.argv()[0] == str(branch_plan.evaluator_binary_path)
    assert branch_plan.freeze_sha256 == branch_plan.main_freeze_sha256
    with pytest.raises(MODULE.ProductionAuthorityError, match="unconditionally"):
        MODULE.dispatch_formal_branch_transaction(
            branch_plan, transaction_runner=lambda *_: called.append("branch")
        )
    assert called == []


def test_formal_static_four_file_packager_replays_in_independent_checker(
    tmp_path: Path,
) -> None:
    authority = formal_authority_fixture(tmp_path)
    output = (tmp_path / "formal-static-packager").absolute()
    snapshot = MODULE.load_formal_authority(authority)
    binding, run_hash = MODULE.initialize_formal_run_binding(snapshot, output)
    cell = MODULE.CellKey(128, "S000")
    transaction = MODULE.build_formal_static_transaction_plan(
        snapshot, binding, run_hash, output, cell
    )
    raw_files, manifest = MODULE.build_formal_static_archive_candidates(
        transaction,
        scheduler_classification="CELL_TIMEOUT",
        proof_raw=None,
        stdout_raw=b"partial evaluator output\n",
        stderr_raw=b"",
        return_code=None,
        evaluator_status=None,
    )
    assert tuple(raw_files) == (
        "proof.json", "stdout.txt", "stderr.txt", "record.json"
    )
    sentinel = MODULE.strict_json_loads(raw_files["proof.json"].decode("utf-8"))
    assert set(sentinel) == MODULE.STATIC_PROOF_SENTINEL_KEYS
    assert sentinel["artifact_role"] == "STATIC_PROOF_ABSENT"
    assert sentinel["reason_code"] == "TIMEOUT"
    record = MODULE.strict_json_loads(raw_files["record.json"].decode("utf-8"))
    assert set(record) == MODULE.FORMAL_STATIC_RECORD_KEYS
    assert set(manifest) == MODULE.FORMAL_STATIC_MANIFEST_KEYS
    assert record["files"]["proof.json"]["serializer"] == "CJ_COMPACT_V1"

    cell_dir = output / "static/cells/128/S000"
    manifest_path = output / "static/cell_manifests/128/S000.json"
    cell_dir.mkdir(parents=True)
    manifest_path.parent.mkdir(parents=True)
    for name, raw in raw_files.items():
        (cell_dir / name).write_bytes(raw)
    manifest_path.write_bytes(MODULE.canonical_json_bytes(manifest))

    checker = load_static_checker()
    plan_payload = MODULE.strict_json_load(
        authority / dict(MODULE.FORMAL_INPUT_ROLES)["l1_final_plan"],
        reject_hardlink=False,
    )
    plan = MODULE.validate_plan_payload(plan_payload)
    limits = MODULE.formal_limits()["static"]
    context = checker.FormalStaticContext(
        matrix_id=MODULE.canonical_matrix_id(),
        freeze_sha256=snapshot.main_freeze_sha256,
        run_config_sha256=run_hash,
        max_depth=limits["max_depth_per_tree"],
        max_nodes_per_tree=limits["max_nodes_per_tree"],
        max_nodes_per_cell=limits["max_nodes_per_cell"],
    )
    checked = checker.validate_formal_static_cell(
        cell_dir,
        manifest_path,
        expected_bits=128,
        expected_slab="S000",
        plan=plan,
        context=context,
        expected_semantic_argv=transaction.semantic_argv,
        expected_limits=limits,
    )
    assert checked["component_eligible"] is False
    assert checked["scheduler_classification"] == "CELL_TIMEOUT"
    assert checked["proof_kind"] == "SCHEDULER_NO_PROOF_SENTINEL"


def test_formal_static_packager_is_type_and_mapping_fail_closed(tmp_path: Path) -> None:
    authority = formal_authority_fixture(tmp_path)
    output = (tmp_path / "formal-static-packager-negative").absolute()
    snapshot = MODULE.load_formal_authority(authority)
    binding, run_hash = MODULE.initialize_formal_run_binding(snapshot, output)
    transaction = MODULE.build_formal_static_transaction_plan(
        snapshot, binding, run_hash, output, MODULE.CellKey(128, "S000")
    )
    with pytest.raises(MODULE.SchedulerContractError):
        MODULE.build_formal_static_archive_candidates(
            transaction,
            scheduler_classification="CELL_TIMEOUT",
            proof_raw=None,
            stdout_raw=b"",
            stderr_raw=b"",
            return_code=False,
            evaluator_status=None,
        )
    with pytest.raises(MODULE.SchedulerContractError):
        MODULE.build_formal_static_archive_candidates(
            transaction,
            scheduler_classification="COMMITTED_EVALUATOR_RESULT",
            proof_raw=None,
            stdout_raw=b"evaluator_status=STATIC_CELL_CERTIFIED\n",
            stderr_raw=b"",
            return_code=0,
            evaluator_status="STATIC_CELL_CERTIFIED",
        )
    with pytest.raises(MODULE.SchedulerContractError):
        MODULE.build_formal_static_archive_candidates(
            transaction,
            scheduler_classification="CELL_OUTPUT_BUDGET_EXHAUSTED",
            proof_raw=b"not-json",
            stdout_raw=b"",
            stderr_raw=b"",
            return_code=None,
            evaluator_status=None,
        )
    with pytest.raises(MODULE.SchedulerContractError, match="truncation evidence"):
        MODULE.build_formal_static_archive_candidates(
            transaction,
            scheduler_classification="CELL_OUTPUT_BUDGET_EXHAUSTED",
            proof_raw=None,
            stdout_raw=b"",
            stderr_raw=b"",
            return_code=None,
            evaluator_status=None,
        )


def test_formal_static_output_budget_sentinel_replays_as_noneligible(
    tmp_path: Path,
) -> None:
    authority = formal_authority_fixture(tmp_path)
    output = (tmp_path / "formal-static-output-budget").absolute()
    snapshot = MODULE.load_formal_authority(authority)
    binding, run_hash = MODULE.initialize_formal_run_binding(snapshot, output)
    transaction = MODULE.build_formal_static_transaction_plan(
        snapshot, binding, run_hash, output, MODULE.CellKey(128, "S000")
    )
    raw_files, manifest = MODULE.build_formal_static_archive_candidates(
        transaction,
        scheduler_classification="CELL_OUTPUT_BUDGET_EXHAUSTED",
        proof_raw=None,
        stdout_raw=b"truncated output",
        stderr_raw=b"",
        return_code=None,
        evaluator_status=None,
        truncated={
            "proof.json": False,
            "stdout.txt": True,
            "stderr.txt": False,
        },
    )
    cell_dir = output / "static/cells/128/S000"
    manifest_path = output / "static/cell_manifests/128/S000.json"
    cell_dir.mkdir(parents=True)
    manifest_path.parent.mkdir(parents=True)
    for name, raw in raw_files.items():
        (cell_dir / name).write_bytes(raw)
    manifest_path.write_bytes(MODULE.canonical_json_bytes(manifest))

    checker = load_static_checker()
    plan_payload = MODULE.strict_json_load(
        authority / dict(MODULE.FORMAL_INPUT_ROLES)["l1_final_plan"],
        reject_hardlink=False,
    )
    limits = MODULE.formal_limits()["static"]
    checked = checker.validate_formal_static_cell(
        cell_dir,
        manifest_path,
        expected_bits=128,
        expected_slab="S000",
        plan=MODULE.validate_plan_payload(plan_payload),
        context=checker.FormalStaticContext(
            matrix_id=MODULE.canonical_matrix_id(),
            freeze_sha256=snapshot.main_freeze_sha256,
            run_config_sha256=run_hash,
            max_depth=limits["max_depth_per_tree"],
            max_nodes_per_tree=limits["max_nodes_per_tree"],
            max_nodes_per_cell=limits["max_nodes_per_cell"],
        ),
        expected_semantic_argv=transaction.semantic_argv,
        expected_limits=limits,
    )
    assert checked["component_eligible"] is False
    assert checked["scheduler_classification"] == "CELL_OUTPUT_BUDGET_EXHAUSTED"
    assert checked["proof_kind"] == "SCHEDULER_NO_PROOF_SENTINEL"


def test_formal_static_committed_proof_requires_exact_bytes_and_abi_envelope(
    tmp_path: Path,
) -> None:
    authority = formal_authority_fixture(tmp_path)
    output = (tmp_path / "formal-static-committed-proof").absolute()
    snapshot = MODULE.load_formal_authority(authority)
    binding, run_hash = MODULE.initialize_formal_run_binding(snapshot, output)
    transaction = MODULE.build_formal_static_transaction_plan(
        snapshot, binding, run_hash, output, MODULE.CellKey(128, "S000")
    )
    proof = synthetic_formal_static_pass_proof(transaction)
    proof_raw = MODULE.canonical_json_bytes(proof)
    raw_files, manifest = MODULE.build_formal_static_archive_candidates(
        transaction,
        scheduler_classification="COMMITTED_EVALUATOR_RESULT",
        proof_raw=proof_raw,
        stdout_raw=b"evaluator_status=STATIC_CELL_CERTIFIED\n",
        stderr_raw=b"",
        return_code=0,
        evaluator_status="STATIC_CELL_CERTIFIED",
    )
    assert raw_files["proof.json"] == proof_raw
    assert manifest["scheduler_classification"] == "COMMITTED_EVALUATOR_RESULT"

    with pytest.raises(MODULE.SchedulerContractError, match="exact bytes"):
        MODULE.build_formal_static_archive_candidates(
            transaction,
            scheduler_classification="COMMITTED_EVALUATOR_RESULT",
            proof_raw=bytearray(proof_raw),  # type: ignore[arg-type]
            stdout_raw=b"evaluator_status=STATIC_CELL_CERTIFIED\n",
            stderr_raw=b"",
            return_code=0,
            evaluator_status="STATIC_CELL_CERTIFIED",
        )

    minimal_raw = MODULE.canonical_json_bytes(
        {"evaluator_status": "STATIC_CELL_CERTIFIED"}
    )
    with pytest.raises((MODULE.StrictJSONError, MODULE.SchedulerContractError)):
        MODULE.build_formal_static_archive_candidates(
            transaction,
            scheduler_classification="COMMITTED_EVALUATOR_RESULT",
            proof_raw=minimal_raw,
            stdout_raw=b"evaluator_status=STATIC_CELL_CERTIFIED\n",
            stderr_raw=b"",
            return_code=0,
            evaluator_status="STATIC_CELL_CERTIFIED",
        )

    forged = json.loads(json.dumps(proof))
    forged["source_bindings"]["checker_sha256"] = "0" * 64
    without_hash = dict(forged)
    without_hash.pop("proof_content_sha256")
    forged["proof_content_sha256"] = MODULE.sha256_bytes(
        MODULE.canonical_json_bytes(without_hash)
    )
    with pytest.raises(MODULE.SchedulerContractError, match="source-binding"):
        MODULE.build_formal_static_archive_candidates(
            transaction,
            scheduler_classification="COMMITTED_EVALUATOR_RESULT",
            proof_raw=MODULE.canonical_json_bytes(forged),
            stdout_raw=b"evaluator_status=STATIC_CELL_CERTIFIED\n",
            stderr_raw=b"",
            return_code=0,
            evaluator_status="STATIC_CELL_CERTIFIED",
        )

def test_formal_aggregate_candidates_are_null_authority_and_complete_only(
    tmp_path: Path,
) -> None:
    authority = formal_authority_fixture(tmp_path)
    snapshot = MODULE.load_formal_authority(authority)
    entries = [
        {
            "cell": cell.payload(),
            "path": f"static/cell_manifests/{cell.precision_bits}/{cell.slab_id}.json",
            "sha256": MODULE.sha256_bytes(cell.label.encode("ascii")),
            "size_bytes": 1,
            "evaluator_status": "STATIC_CELL_CERTIFIED",
            "scheduler_classification": "COMMITTED_EVALUATOR_RESULT",
        }
        for cell in MODULE.exact_matrix()
    ]
    run_hash = "a" * 64
    summary, manifest = MODULE.build_formal_component_aggregate_candidates(
        "STATIC", snapshot, run_hash, entries
    )
    assert summary["status_counts"] == {"STATIC_CELL_CERTIFIED": 102}
    assert summary["scheduler_classification_counts"] == {
        "COMMITTED_EVALUATOR_RESULT": 102
    }
    assert summary["authority"] == manifest["authority"] == "PRODUCER_ONLY"
    assert summary["artifact_role"] == "STATIC_AGGREGATE_SUMMARY"
    assert manifest["artifact_role"] == "STATIC_AGGREGATE_MANIFEST"
    assert summary["artifact_status"] == "COMPLETE_PRODUCER_ARCHIVE"
    assert set(summary) == MODULE.FORMAL_AGGREGATE_SUMMARY_KEYS
    assert set(manifest) == MODULE.FORMAL_AGGREGATE_MANIFEST_KEYS
    assert summary["scientific_licensing_enabled"] is False
    assert summary["component_status"] is None
    assert summary["freeze_sha256"] == summary["main_freeze_sha256"]
    assert manifest["summary"]["sha256"] == MODULE.sha256_bytes(
        MODULE.canonical_json_bytes(summary)
    )
    with pytest.raises(MODULE.CorruptGeneration, match="102"):
        MODULE.build_formal_component_aggregate_candidates(
            "STATIC", snapshot, run_hash, entries[:-1]
        )

    wrong = [dict(item) for item in entries]
    wrong[1]["path"] = wrong[0]["path"]
    with pytest.raises(MODULE.CorruptGeneration, match="path/order"):
        MODULE.build_formal_component_aggregate_candidates(
            "STATIC", snapshot, run_hash, wrong
        )
    wrong = [dict(item) for item in entries]
    wrong[0]["evaluator_status"] = "STATIC_UNRESOLVED_DEPTH"
    with pytest.raises(MODULE.CorruptGeneration, match="not producer-certified"):
        MODULE.build_formal_component_aggregate_candidates(
            "STATIC", snapshot, run_hash, wrong
        )
    wrong = [dict(item) for item in entries]
    wrong[0]["path"] = "branch/cell_manifests/128/S000.json"
    with pytest.raises(MODULE.CorruptGeneration, match="path/order"):
        MODULE.build_formal_component_aggregate_candidates(
            "STATIC", snapshot, run_hash, wrong
        )


def replace_with_same_bytes(path: Path) -> None:
    replacement = path.with_name(path.name + ".replacement")
    replacement.write_bytes(path.read_bytes())
    replacement.chmod(path.stat().st_mode)
    os.replace(replacement, path)


def test_formal_snapshot_is_deeply_immutable_and_detects_same_byte_inode_swap(
    tmp_path: Path,
) -> None:
    authority = formal_authority_fixture(tmp_path)
    snapshot = MODULE.load_formal_authority(authority)
    with pytest.raises(FrozenInstanceError):
        snapshot.input_roles[0].role = "forged"  # type: ignore[misc]
    assert isinstance(snapshot.main_freeze_raw, bytes)
    plan = authority / dict(MODULE.FORMAL_INPUT_ROLES)["l1_final_plan"]
    replace_with_same_bytes(plan)
    with pytest.raises(MODULE.ProductionAuthorityError, match="inode/image"):
        MODULE.revalidate_formal_snapshot(snapshot, ("l1_final_plan",))

    authority = formal_authority_fixture(tmp_path / "main")
    snapshot = MODULE.load_formal_authority(authority)
    replace_with_same_bytes(snapshot.main_freeze_path)
    with pytest.raises(MODULE.ProductionAuthorityError, match="main freeze inode"):
        MODULE.revalidate_formal_snapshot(snapshot, ("l1_final_plan",))


def test_formal_initialize_atomic_staging_failure_leaves_no_output(
    tmp_path: Path,
) -> None:
    authority = formal_authority_fixture(tmp_path)
    snapshot = MODULE.load_formal_authority(authority)
    for index, boundary in enumerate(
        ("AFTER_STAGE_DIR", "AFTER_CONFIG_FSYNC", "BEFORE_RENAME")
    ):
        output = (tmp_path / f"atomic-preflight-{index}").absolute()
        with pytest.raises(MODULE.SyntheticCrash):
            MODULE.initialize_formal_preflight(
                snapshot, output, _fail_at=boundary
            )
        assert not output.exists()
        assert not list(tmp_path.glob(f".{output.name}.formal-preflight-*"))


def test_formal_builders_reject_swapped_l1_images_before_parse_or_runtime_load(
    tmp_path: Path,
) -> None:
    authority = formal_authority_fixture(tmp_path)
    output = (tmp_path / "formal-swap-output").absolute()
    snapshot = MODULE.load_formal_authority(authority)
    binding, run_hash = MODULE.initialize_formal_preflight(snapshot, output)
    cell = MODULE.CellKey(128, "S000")

    plan_path = authority / dict(MODULE.FORMAL_INPUT_ROLES)["l1_final_plan"]
    replace_with_same_bytes(plan_path)
    with pytest.raises(MODULE.ProductionAuthorityError, match="l1_final_plan"):
        MODULE.build_formal_static_transaction_plan(
            snapshot, binding, run_hash, output, cell
        )

    authority = formal_authority_fixture(tmp_path / "branch")
    output = (tmp_path / "formal-branch-swap-output").absolute()
    snapshot = MODULE.load_formal_authority(authority)
    binding, run_hash = MODULE.initialize_formal_preflight(snapshot, output)
    summary = authority / dict(MODULE.FORMAL_INPUT_ROLES)["l1_summary"]
    replace_with_same_bytes(summary)
    MODULE._BRANCH_RUNTIME_MODULE = None
    with pytest.raises(MODULE.ProductionAuthorityError, match="l1_summary"):
        MODULE.build_formal_branch_transaction_plan(
            snapshot, binding, run_hash, output, cell
        )
    assert MODULE._BRANCH_RUNTIME_MODULE is None


def test_formal_static_dispatch_rehashes_evaluator_and_never_calls_executor(
    tmp_path: Path,
) -> None:
    authority = formal_authority_fixture(tmp_path)
    output = (tmp_path / "formal-evaluator-rehash").absolute()
    snapshot = MODULE.load_formal_authority(authority)
    binding, run_hash = MODULE.initialize_formal_preflight(snapshot, output)
    plan = MODULE.build_formal_static_transaction_plan(
        snapshot, binding, run_hash, output, MODULE.CellKey(128, "S000")
    )
    plan.evaluator_path.write_text("changed after plan\n", encoding="utf-8")
    called: list[bool] = []
    with pytest.raises(MODULE.ProductionAuthorityError, match="changed after plan"):
        MODULE.dispatch_formal_static_transaction(
            plan, executor=lambda *_: called.append(True)
        )
    assert called == []


def test_formal_branch_executes_captured_runtime_not_reopened_live_path(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    authority = formal_authority_fixture(tmp_path)
    output = (tmp_path / "captured-runtime-output").absolute()
    snapshot = MODULE.load_formal_authority(authority)
    binding, run_hash = MODULE.initialize_formal_preflight(snapshot, output)
    runtime_role = next(
        item for item in snapshot.input_roles if item.role == "branch_runtime"
    )
    module_name = MODULE._formal_runtime_module_name(runtime_role.sha256)
    MODULE._FORMAL_BRANCH_RUNTIME_MODULES.pop(runtime_role.sha256, None)
    sys.modules.pop(module_name, None)
    marker = tmp_path / "runtime-side-effect"
    trap = tmp_path / "live-runtime-trap.py"
    trap.write_text(
        f"from pathlib import Path\nPath({str(marker)!r}).write_text('opened')\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(MODULE, "BRANCH_RUNTIME_PATH", trap)
    monkeypatch.setattr(
        MODULE,
        "_load_branch_runtime",
        lambda: (_ for _ in ()).throw(AssertionError("mock loader called")),
    )
    plan = MODULE.build_formal_branch_transaction_plan(
        snapshot,
        binding,
        run_hash,
        output,
        MODULE.CellKey(128, "S000"),
    )
    assert plan.task.argv()[0] == str(plan.evaluator_binary_path)
    loaded = sys.modules[module_name]
    assert loaded.__formal_runtime_sha256__ == runtime_role.sha256
    assert loaded.__file__ == str(trap)
    assert not marker.exists()


def test_formal_branch_rejects_unbound_precached_runtime(
    tmp_path: Path,
) -> None:
    authority = formal_authority_fixture(tmp_path)
    output = (tmp_path / "precache-runtime-output").absolute()
    snapshot = MODULE.load_formal_authority(authority)
    binding, run_hash = MODULE.initialize_formal_preflight(snapshot, output)
    runtime_role = next(
        item for item in snapshot.input_roles if item.role == "branch_runtime"
    )
    name = MODULE._formal_runtime_module_name(runtime_role.sha256)
    MODULE._FORMAL_BRANCH_RUNTIME_MODULES.pop(runtime_role.sha256, None)
    previous = sys.modules.get(name)
    sys.modules[name] = types.ModuleType(name)
    try:
        with pytest.raises(MODULE.ProductionAuthorityError, match="pre-cached"):
            MODULE.build_formal_branch_transaction_plan(
                snapshot,
                binding,
                run_hash,
                output,
                MODULE.CellKey(128, "S000"),
            )
    finally:
        if previous is None:
            sys.modules.pop(name, None)
        else:
            sys.modules[name] = previous


def test_explicit_mock_initialize_and_cells_never_gain_authority(tmp_path: Path) -> None:
    output = tmp_path / "cli-mock"
    completed = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--mock-only",
            "--initialize-only",
            "--mock-static-cells",
            "3",
            "--output",
            str(output),
        ],
        text=True,
        capture_output=True,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr
    payload = json.loads(completed.stdout)
    assert payload["artifact_status"] == "MOCK_ONLY_NON_LICENSING"
    assert payload["completed_cells"] == 3
    assert payload["production_authorized"] is False
    assert payload["component_status"] is None
    assert payload["milestone_status"] is None
    assert payload["theorem_status"] is None
    assert payload["final_status"] is None
    assert payload["aggregate_finalized"] is False
    assert payload["aggregate"] is None
    assert len(list((output / "static/cell_manifests").rglob("*.json"))) == 3
    assert not MODULE.static_aggregate_summary_path(output).exists()
    assert not MODULE.static_aggregate_manifest_path(output).exists()
    assert not MODULE.CANONICAL_RESULT.exists()


def test_full_mock_matrix_publishes_write_once_static_aggregate(tmp_path: Path) -> None:
    output = tmp_path / "full-static-mock"
    first = MODULE.run_mock_static(output, 102, resume=False)
    assert first["completed_cells"] == 102
    assert first["aggregate_finalized"] is True
    assert first["aggregate"]["state"] == "COMMITTED"
    summary_path = MODULE.static_aggregate_summary_path(output)
    manifest_path = MODULE.static_aggregate_manifest_path(output)
    summary_before = summary_path.read_bytes()
    manifest_before = manifest_path.read_bytes()
    summary = MODULE.strict_json_load(summary_path)
    manifest = MODULE.strict_json_load(manifest_path)
    assert summary["cell_count"] == 102
    assert summary["matrix"] == MODULE.matrix_payload()
    assert summary["main_freeze_sha256"] is None
    assert summary["component_status"] is None
    assert summary["theorem_status"] is None
    assert len(manifest["cell_manifests"]) == 102
    assert manifest["cell_manifests"][0]["cell"] == {
        "precision_bits": 128,
        "slab_id": "S000",
    }
    assert manifest["cell_manifests"][-1]["cell"] == {
        "precision_bits": 256,
        "slab_id": "S050",
    }
    assert manifest["ordered_cell_manifest_root"] == MODULE.sha256_bytes(
        MODULE.canonical_json_bytes(manifest["cell_manifests"])
    )
    assert manifest["summary"] == {
        "path": "static/aggregate_summary.json",
        "sha256": MODULE.sha256(summary_path),
        "size_bytes": summary_path.stat().st_size,
    }

    resumed = MODULE.run_mock_static(output, 102, resume=True)
    assert resumed["aggregate"]["state"] == "RESUMED_COMMITTED"
    assert summary_path.read_bytes() == summary_before
    assert manifest_path.read_bytes() == manifest_before


def test_static_aggregate_rejects_live_stage_for_committed_cell(
    tmp_path: Path,
) -> None:
    output = tmp_path / "archive"
    first = MODULE.run_mock_static(output, 102, resume=False)
    assert first["aggregate_finalized"] is True
    config_hash = MODULE.sha256(MODULE.run_config_path(output))
    stage = MODULE.staging_path(
        MODULE.operational_root_for(output),
        MODULE.CellKey(128, "S000"),
        config_hash,
    )
    stage.mkdir(parents=True)
    with pytest.raises(MODULE.CorruptGeneration, match="live staging owners"):
        MODULE.run_mock_static(output, 102, resume=True)


def test_static_aggregate_rejects_extra_manifest_namespace(tmp_path: Path) -> None:
    output, operational, binding, config_hash = initialize(tmp_path)
    for cell in MODULE.exact_matrix():
        MODULE.commit_mock_static_cell(
            output, operational, cell, binding["matrix_id"], config_hash
        )
    extra = output / "static/cell_manifests/128/EXTRA.json"
    extra.write_text("{}\n", encoding="utf-8")
    with pytest.raises(MODULE.CorruptGeneration, match="namespace mismatch"):
        MODULE.finalize_static_mock_aggregate(
            output, binding["matrix_id"], config_hash
        )
    assert not MODULE.static_aggregate_summary_path(output).exists()
    assert not MODULE.static_aggregate_manifest_path(output).exists()


def test_static_aggregate_rejects_extra_cell_subtree(tmp_path: Path) -> None:
    output = tmp_path / "extra-cell-subtree"
    result = MODULE.run_mock_static(output, 102, resume=False)
    assert result["aggregate_finalized"] is True
    extra = output / "static/cells/128/EXTRA"
    extra.mkdir()
    (extra / "junk.json").write_text("{}\n", encoding="utf-8")
    run_config = MODULE.strict_json_load(
        MODULE.run_config_path(output), require_canonical=True
    )
    with pytest.raises(MODULE.CorruptGeneration, match="cell namespace mismatch"):
        MODULE.validate_static_mock_aggregate(
            output,
            run_config["matrix_id"],
            MODULE.sha256(MODULE.run_config_path(output)),
        )


def test_mock_cli_requires_explicit_action_and_resume(tmp_path: Path) -> None:
    output = tmp_path / "explicit"
    no_action = MODULE.main(["--mock-only", "--output", str(output)])
    assert no_action == 1
    assert not output.exists()

    assert MODULE.main(
        [
            "--mock-only",
            "--mock-static-cells",
            "1",
            "--output",
            str(output),
        ]
    ) == 0
    assert MODULE.main(
        [
            "--mock-only",
            "--mock-static-cells",
            "1",
            "--resume",
            "--output",
            str(output),
        ]
    ) == 0


def test_directory_publication_is_atomic_no_replace(tmp_path: Path) -> None:
    source = tmp_path / "source"
    destination = tmp_path / "destination"
    source.mkdir()
    destination.mkdir()
    marker = destination / "marker"
    marker.write_text("keep\n", encoding="utf-8")
    with pytest.raises(MODULE.CorruptGeneration, match="destination collision"):
        MODULE.rename_directory_noreplace(source, destination)
    assert source.is_dir()
    assert marker.read_text(encoding="utf-8") == "keep\n"


def test_strict_json_image_binds_parse_hash_and_size_to_one_snapshot(
    tmp_path: Path,
) -> None:
    path = tmp_path / "object.json"
    payload = {"authority": "PRODUCER_ONLY", "value": 1}
    raw = MODULE.canonical_json_bytes(payload)
    path.write_bytes(raw)
    parsed, captured, info = MODULE.strict_json_image(
        path, require_canonical=True
    )
    assert parsed == payload
    assert captured == raw
    assert MODULE.sha256_bytes(captured) == MODULE.file_binding(path)["sha256"]
    assert info.st_size == len(raw)


@pytest.mark.parametrize(
    "payload",
    [
        ("tuple-alias",),
        {1: "non-string-key"},
        {"value": float("nan")},
        {"value": float("inf")},
        {"value": float("-inf")},
    ],
)
def test_scheduler_serializers_reject_non_exact_json_domain(payload: object) -> None:
    for serializer in (MODULE.canonical_json_bytes, MODULE.pretty_json_bytes):
        with pytest.raises(MODULE.StrictJSONError):
            serializer(payload)
    assert MODULE.canonical_json_bytes(
        {"array": [None, False, 0, 1.25, "text"]}
    ) == b'{"array":[null,false,0,1.25,"text"]}\n'
