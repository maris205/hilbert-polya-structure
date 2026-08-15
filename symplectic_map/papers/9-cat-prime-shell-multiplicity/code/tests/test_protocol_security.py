from __future__ import annotations

import os
from pathlib import Path
import shutil
import stat

import pytest

from prime_shell.protocol import (
    DuplicateJSONKeyError,
    canonical_json_bytes,
    code_inventory,
    code_tree_sha256,
    executable_isolation_scan,
    write_bytes,
    strict_json_loads,
)


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def test_duplicate_json_and_nonfinite_values_fail_closed() -> None:
    with pytest.raises(DuplicateJSONKeyError):
        strict_json_loads('{"a":1,"a":2}')
    with pytest.raises(ValueError):
        strict_json_loads('{"value":NaN}')
    with pytest.raises(TypeError):
        canonical_json_bytes({"value": 1.25})


def test_code_inventory_and_executable_scan_are_closed() -> None:
    inventory = code_inventory(PROJECT_ROOT / "code")
    assert inventory["pass"] is True, inventory
    scan = executable_isolation_scan(PROJECT_ROOT / "code")
    assert scan["pass"] is True, scan
    assert scan["network_modules_imported"] == 0
    assert scan["external_data_loaders"] == 0
    assert scan["floating_literals"] == 0


def test_framed_tree_hash_is_stable() -> None:
    first = code_tree_sha256(PROJECT_ROOT)
    second = code_tree_sha256(PROJECT_ROOT)
    assert first == second
    assert len(first) == 64


def test_scanner_rejects_alias_container_dynamic_import_and_loader_attacks(
    tmp_path: Path,
) -> None:
    isolated_code = tmp_path / "code"
    shutil.copytree(PROJECT_ROOT / "code", isolated_code)
    attack = '''import os as allowed_os
import sys
from pathlib import Path

def latent_capabilities():
    imported_alias = allowed_os.system
    capability_box = {"run": imported_alias}
    capability_alias = capability_box["run"]
    capability_alias("true")
    dynamic_alias = getattr(allowed_os, "system")
    dynamic_alias("true")
    dynamic_module = __import__("socket")
    dynamic_module.socket()
    module_alias = sys.modules["socket"]
    module_alias.socket()
    return Path("forbidden.data").read_text()
'''
    (isolated_code / "prime_shell" / "candidate.py").write_text(
        attack, encoding="utf-8"
    )
    audit = executable_isolation_scan(isolated_code)
    assert audit["pass"] is False
    candidate = next(
        record for record in audit["records"] if record["path"] == "prime_shell/candidate.py"
    )
    assert candidate["pass"] is False
    assert audit["process_capabilities"] > 0
    assert audit["network_modules_imported"] > 0
    assert audit["external_data_loaders"] > 0
    assert audit["dynamic_capabilities"] > 0


def test_writers_fsync_file_then_parent_directory(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    observed_directory_flags: list[bool] = []
    real_fsync = os.fsync

    def recording_fsync(descriptor: int) -> None:
        observed_directory_flags.append(stat.S_ISDIR(os.fstat(descriptor).st_mode))
        real_fsync(descriptor)

    monkeypatch.setattr("prime_shell.protocol.os.fsync", recording_fsync)
    output = tmp_path / "durable.json"
    write_bytes(output, b"first\n", exclusive=True)
    assert observed_directory_flags == [False, True]
    observed_directory_flags.clear()
    write_bytes(output, b"second\n")
    assert observed_directory_flags == [False, True]
    assert output.read_bytes() == b"second\n"


def test_scanner_rejects_exact_import_dunder_bypasses_and_counts_float(
    tmp_path: Path,
) -> None:
    attacks = {
        "process": (
            "prime_shell/protocol.py",
            '''\n\ndef latent_process_bypass():
    runner = os.__getattribute__("system")
    return runner("true")
''',
            "process_capabilities",
        ),
        "network": (
            "prime_shell/candidate.py",
            '''\n\ndef latent_network_bypass():
    loader = __builtins__.__getitem__("__import__")
    module = loader("socket")
    constructor = module.__getattribute__("socket")
    return constructor()
''',
            "network_modules_imported",
        ),
        "loader": (
            "prime_shell/cli.py",
            '''\n\ndef latent_path_bypass():
    target = Path("outside")
    loader = target.__getattribute__("read_text")
    return loader()
''',
            "external_data_loaders",
        ),
    }
    for label, (relative, suffix, counter) in attacks.items():
        isolated = tmp_path / label / "code"
        shutil.copytree(PROJECT_ROOT / "code", isolated)
        path = isolated / relative
        path.write_text(path.read_text(encoding="utf-8") + suffix, encoding="utf-8")
        audit = executable_isolation_scan(isolated)
        assert audit["pass"] is False
        assert audit[counter] > 0
        assert audit["dynamic_capabilities"] > 0

    floating = tmp_path / "float" / "code"
    shutil.copytree(PROJECT_ROOT / "code", floating)
    candidate = floating / "prime_shell" / "candidate.py"
    candidate.write_text(
        candidate.read_text(encoding="utf-8") + "\nFLOAT_SENTINEL = 1.25\n",
        encoding="utf-8",
    )
    float_audit = executable_isolation_scan(floating)
    assert float_audit["pass"] is False
    assert float_audit["floating_literals"] > 0


def test_scanner_rejects_unreviewed_os_family_and_low_level_read_sites(
    tmp_path: Path,
) -> None:
    isolated = tmp_path / "round3" / "code"
    shutil.copytree(PROJECT_ROOT / "code", isolated)
    protocol = isolated / "prime_shell" / "protocol.py"
    protocol.write_text(
        protocol.read_text(encoding="utf-8")
        + '''

def round3_latent_process_bypass() -> int:
    return os.spawnl(os.P_WAIT, "/bin/true", "true")


def round3_latent_external_read_bypass() -> bytes:
    descriptor = os.open("/outside-source-lock", os.O_RDONLY)
    return os.read(descriptor, 1)


def round3_extra_nominally_allowed_os_call() -> None:
    os.fsync(1)
''',
        encoding="utf-8",
    )
    audit = executable_isolation_scan(isolated)
    assert audit["pass"] is False
    assert audit["process_capabilities"] > 0
    assert audit["external_data_loaders"] > 0
    assert audit["dynamic_capabilities"] > 0
    protocol_record = next(
        record
        for record in audit["records"]
        if record["path"] == "prime_shell/protocol.py"
    )
    assert any("UNREVIEWED_OS_ATTRIBUTE_SITE:spawnl" in error for error in protocol_record["errors"])
    assert any("UNREVIEWED_OS_ATTRIBUTE_SITE:open" in error for error in protocol_record["errors"])
    assert any("UNREVIEWED_OS_ATTRIBUTE_SITE:read" in error for error in protocol_record["errors"])
    assert any("UNREVIEWED_OS_ATTRIBUTE_SITE:fsync" in error for error in protocol_record["errors"])

    wrapper = tmp_path / "wrapper" / "code"
    shutil.copytree(PROJECT_ROOT / "code", wrapper)
    wrapper_protocol = wrapper / "prime_shell" / "protocol.py"
    wrapper_protocol.write_text(
        wrapper_protocol.read_text(encoding="utf-8")
        + '''

def round3_latent_reviewed_wrapper_bypass() -> bytes:
    return stable_file_bytes(Path("/outside-source-lock"))
''',
        encoding="utf-8",
    )
    wrapper_audit = executable_isolation_scan(wrapper)
    assert wrapper_audit["pass"] is False
    assert wrapper_audit["dynamic_capabilities"] > 0
    wrapper_record = next(
        record
        for record in wrapper_audit["records"]
        if record["path"] == "prime_shell/protocol.py"
    )
    assert any("EXECUTABLE_AST_SIGNATURE_NOT_EXACT" in error for error in wrapper_record["errors"])
