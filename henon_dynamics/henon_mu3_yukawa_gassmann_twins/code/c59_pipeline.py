#!/usr/bin/env python3
"""Backend preflights and deterministic subprocess-report parsing for C59."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import stat
import subprocess
import sys
from typing import Any, Sequence

from c59_exact import (
    StrictDataError,
    read_stable,
    reject_optimized_python,
    sha256_bytes,
    strict_json_loads,
    canonical_json_bytes,
)


EXPECTED_BACKENDS = {
    "math": {
        "python": [3, 12, 3],
        "flint": "0.9.0",
        "sympy": "1.14.0",
        "networkx": "3.5",
        "jsonschema": "4.25.0",
        "executable_sha256": "9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101",
        "executable_size_bytes": 30626264,
    },
}
EXPECTED_GAP = {
    "resolved_executable": "/usr/bin/gap",
    "executable_sha256": "9aa736f13150c363d7c31d33513d849482dd52692e7534f51ecfac0d303bb1e3",
    "executable_size_bytes": 1942,
    "gap_version": "4.11.1",
    "tomlib_version": "1.2.9",
    "smallgrp_version": "1.4.1",
    "ctbllib_version": "1.3.1",
}


def executable(path: Path, label: str) -> Path:
    resolved = path.resolve(strict=True)
    metadata = resolved.stat()
    if not stat.S_ISREG(metadata.st_mode) or not os.access(resolved, os.X_OK):
        raise StrictDataError(f"{label} backend is not an executable regular file")
    return resolved


def clean_environment() -> dict[str, str]:
    # Reject hostile optimization at the orchestration boundary.  Never erase
    # it and continue, since doing that would turn a requested unsafe run into
    # an apparently valid one.
    reject_optimized_python()
    return {
        "PATH": "/usr/bin:/bin",
        "LANG": "C.UTF-8",
        "LC_ALL": "C.UTF-8",
        "TZ": "UTC",
        "PYTHONDONTWRITEBYTECODE": "1",
        "PYTHONHASHSEED": "0",
        "PYTHONNOUSERSITE": "1",
    }


def python_preflight(math_python: Path) -> dict[str, Any]:
    math_backend = executable(math_python, "FLINT/SymPy/NetworkX")
    snippets = {
        "math": (
            math_backend,
            "import importlib.metadata,json,sys,flint,sympy,networkx,jsonschema; "
            "assert not sys.flags.optimize; "
            "print(json.dumps({'backend':'FLINT_SYMPY_NETWORKX',"
            "'python':list(sys.version_info[:3]),"
            "'flint':getattr(flint,'__version__','unknown'),"
            "'sympy':sympy.__version__,'networkx':networkx.__version__,"
            "'jsonschema':importlib.metadata.version('jsonschema')},sort_keys=True,separators=(',',':')))",
        ),
    }
    result = {}
    for key, (binary, source) in snippets.items():
        binary_raw, binary_fingerprint = read_stable(binary, max_bytes=40_000_000)
        completed_runs = [
            subprocess.run(
                [str(binary), "-s", "-B", "-c", source],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                env=clean_environment(),
                cwd="/",
                check=True,
                timeout=60,
            )
            for _ in range(2)
        ]
        if any(completed.stderr for completed in completed_runs):
            raise StrictDataError(f"{key} backend preflight emitted stderr")
        if completed_runs[0].stdout != completed_runs[1].stdout:
            raise StrictDataError(f"{key} backend preflight is nondeterministic")
        completed = completed_runs[0]
        value = strict_json_loads(completed.stdout.strip(), max_bytes=10_000)
        expected_versions = {
            "backend": "FLINT_SYMPY_NETWORKX",
            **{
                name: expected
                for name, expected in EXPECTED_BACKENDS[key].items()
                if not name.startswith("executable_")
            },
        }
        if value != expected_versions:
            raise StrictDataError(f"unsupported {key} backend versions: {value}")
        if (
            sha256_bytes(binary_raw) != EXPECTED_BACKENDS[key]["executable_sha256"]
            or binary_fingerprint.size_bytes
            != EXPECTED_BACKENDS[key]["executable_size_bytes"]
        ):
            raise StrictDataError(f"unsupported {key} Python executable bytes")
        result[key] = {
            "resolved_executable": str(binary),
            "versions": value,
            "executable_sha256": sha256_bytes(binary_raw),
            "executable_size_bytes": binary_fingerprint.size_bytes,
        }
    return result


def gap_preflight(gap_path: Path) -> dict[str, Any]:
    gap = executable(gap_path, "GAP")
    raw, fingerprint = read_stable(gap, max_bytes=1_000_000)
    source = (
        'Print(GAPInfo.Version,"|",PackageInfo("TomLib")[1].Version,"|",'
        'PackageInfo("SmallGrp")[1].Version,"|",'
        'PackageInfo("ctbllib")[1].Version,"\\n"); QUIT;'
    )
    completed_runs = [
        subprocess.run(
            [str(gap), "-q", "-c", source],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=clean_environment(),
            cwd="/",
            check=True,
            timeout=60,
        )
        for _ in range(2)
    ]
    if any(completed.stderr for completed in completed_runs):
        raise StrictDataError("GAP preflight emitted stderr")
    if completed_runs[0].stdout != completed_runs[1].stdout:
        raise StrictDataError("GAP preflight is nondeterministic")
    try:
        fields = completed_runs[0].stdout.decode("ascii", errors="strict").strip().split("|")
    except UnicodeDecodeError as exc:
        raise StrictDataError("GAP preflight output is malformed") from exc
    if len(fields) != 4:
        raise StrictDataError("GAP preflight output has the wrong field count")
    observed = {
        "resolved_executable": str(gap),
        "executable_sha256": sha256_bytes(raw),
        "executable_size_bytes": fingerprint.size_bytes,
        "gap_version": fields[0],
        "tomlib_version": fields[1],
        "smallgrp_version": fields[2],
        "ctbllib_version": fields[3],
    }
    if observed != EXPECTED_GAP:
        raise StrictDataError(f"unsupported GAP backend: {observed}")
    return observed


def run_canonical_report(
    python: Path,
    script: Path,
    arguments: Sequence[str | Path],
    *,
    timeout: int,
    max_stdout_bytes: int = 10_000_000,
) -> tuple[dict[str, Any], str]:
    binary = executable(python, "Python")
    if not script.is_file() or script.is_symlink():
        raise StrictDataError(f"report script must be a regular non-symlink file: {script}")
    completed = subprocess.run(
        [str(binary), "-s", "-B", str(script), *(str(value) for value in arguments)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=clean_environment(),
        check=True,
        timeout=timeout,
    )
    if completed.stderr:
        raise StrictDataError(f"report script emitted stderr: {script.name}")
    if len(completed.stdout) > max_stdout_bytes:
        raise StrictDataError(f"report stdout exceeds limit: {script.name}")
    lines = completed.stdout.splitlines()
    json_lines = [line for line in lines if line.startswith(b"{") and line.endswith(b"}")]
    if len(json_lines) != 1:
        raise StrictDataError(f"report must have exactly one JSON line: {script.name}")
    raw = json_lines[0]
    report = strict_json_loads(raw, max_bytes=max_stdout_bytes)
    if type(report) is not dict:
        raise StrictDataError("canonical report must be an object")
    canonical = json.dumps(
        report,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    if raw != canonical:
        raise StrictDataError(f"report JSON line is not canonical: {script.name}")
    declared = [line.split(b" ", 1)[1].decode() for line in lines if line.startswith(b"report_sha256 ")]
    actual = hashlib.sha256(raw).hexdigest()
    if declared != [actual]:
        raise StrictDataError(f"canonical report digest line mismatch: {script.name}")
    permitted_progress = {
        line
        for line in lines
        if line.startswith(b"division_step ")
    }
    unexplained = [
        line
        for line in lines
        if line not in permitted_progress
        and line != raw
        and not line.startswith(b"report_sha256 ")
    ]
    if unexplained:
        raise StrictDataError(f"unexpected report stdout line: {script.name}")
    return report, actual


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--preflight", action="store_true", required=True)
    parser.add_argument(
        "--math-python",
        type=Path,
        default=Path("/root/miniconda3/bin/python3"),
    )
    parser.add_argument("--gap", type=Path, default=Path("/usr/bin/gap"))
    arguments = parser.parse_args()
    reject_optimized_python()
    value = {
        "python": python_preflight(arguments.math_python),
        "gap": gap_preflight(arguments.gap),
    }
    sys.stdout.buffer.write(canonical_json_bytes(value))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
