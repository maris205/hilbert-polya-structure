#!/usr/bin/env python3
"""Build State B from the frozen core and atomically exchange full-root outputs."""

from __future__ import annotations

import argparse
import ctypes
import errno
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
from typing import Any


STATIC_MANIFEST = "STATIC_TREE_MANIFEST.json"
STATIC_SEAL = "PREOUTPUT_STATIC_SEAL.json"
STATIC_MANIFEST_SHA256 = "5f93fd2595a173e30e8d745c18fc74550fb6415df2f63429c4433576f05a30b0"
STATIC_SEAL_SHA256 = "2135bb54e94326b336cb384f25340339df1c057497d7eaeb170632e482122fec"
PAPER_MANIFEST = "outputs/PAPER_MANIFEST.sha256"
HEX64 = re.compile(r"[0-9a-f]{64}\Z")
HEX40 = re.compile(r"[0-9a-f]{40}\Z")
AT_FDCWD = -100
RENAME_EXCHANGE = 2


class TargetChangedDuringStaging(Exception):
    pass


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       separators=(",", ": "), allow_nan=False) + "\n").encode("ascii")


def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def sha_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def sha_file(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def safe_relative(value: Any) -> bool:
    if type(value) is not str or not value or "\\" in value:
        return False
    path = Path(value)
    return not path.is_absolute() and all(part not in {"", ".", ".."} for part in path.parts)


def emit(status: str, code: str, payload: dict[str, Any], exit_code: int) -> int:
    sys.stdout.buffer.write(canonical({
        "payload": {"code": code, **payload},
        "schema": "paper44-stateb-bridge-transaction-v1",
        "status": status,
    }))
    return exit_code


def secure_root(path: Path, label: str) -> Path:
    if not path.is_absolute() or path.is_symlink() or not path.is_dir() \
            or path.resolve(strict=True) != path \
            or stat.S_IMODE(os.lstat(path).st_mode) != 0o755:
        raise ValueError("unsafe " + label)
    return path


def invoke(command: list[str], cwd: Path) -> tuple[int, bytes, bytes, dict[str, Any] | None]:
    environment = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "PYTHONPATH": "",
                   "PYTHONDONTWRITEBYTECODE": "1", "TZ": "UTC", "LC_ALL": "C", "LANG": "C"}
    process = subprocess.run(command, cwd=cwd, env=environment, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, check=False)
    value: dict[str, Any] | None = None
    try:
        parsed = json.loads(process.stdout.decode("ascii"), object_pairs_hook=unique)
        if type(parsed) is dict and process.stdout == canonical(parsed):
            value = parsed
    except Exception:
        pass
    return process.returncode, process.stdout, process.stderr, value


def audit(auditor: Path, root: Path, source: Path, anchor: str,
          commit: str, relocated: bool,
          allow_checklist: bool) -> tuple[int, bytes, bytes, dict[str, Any] | None]:
    command = [
        sys.executable, "-I", "-B", str(auditor), "--root", str(root),
        "--overlay-source", str(source), "--expected-publication-seal-sha256", anchor,
        "--expected-stage1-commit", commit,
    ]
    if relocated:
        command.append("--relocated-disposable")
    if allow_checklist:
        command.append("--allow-unexecuted-checklist")
    return invoke(command, root.parent)


def logical_tree(root: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in [root] + sorted(root.rglob("*"), key=lambda item: item.relative_to(root).as_posix()):
        metadata = os.lstat(path)
        relative = "." if path == root else path.relative_to(root).as_posix()
        if stat.S_ISDIR(metadata.st_mode):
            kind, digest = "directory", None
        elif stat.S_ISREG(metadata.st_mode):
            kind, digest = "regular", sha_file(path)
        elif stat.S_ISLNK(metadata.st_mode):
            kind, digest = "symlink", os.readlink(path)
        else:
            kind, digest = "nonregular", None
        rows.append({"kind": kind, "mode": stat.S_IMODE(metadata.st_mode),
                     "path": relative, "sha256": digest})
    return rows


def load_static_rows(root: Path) -> tuple[list[dict[str, Any]], bytes, bytes]:
    raw = (root / STATIC_MANIFEST).read_bytes()
    seal_raw = (root / STATIC_SEAL).read_bytes()
    if sha_bytes(raw) != STATIC_MANIFEST_SHA256 or sha_bytes(seal_raw) != STATIC_SEAL_SHA256:
        raise ValueError("legacy static anchor drift")
    value = json.loads(raw.decode("ascii"), object_pairs_hook=unique)
    if type(value) is not dict or raw != canonical(value) \
            or set(value) != {"payload", "schema", "status"} \
            or value["schema"] != "paper44-static-tree-manifest-v2" \
            or value["status"] != "SEALED" or type(value["payload"]) is not dict \
            or set(value["payload"]) != {"entry_count", "excluded_paths", "rows"} \
            or type(value["payload"]["entry_count"]) is not int \
            or value["payload"]["entry_count"] != 58 \
            or value["payload"]["excluded_paths"] \
            != [STATIC_SEAL, STATIC_MANIFEST, "outputs"]:
        raise ValueError("noncanonical static manifest")
    rows = value["payload"]["rows"]
    if type(rows) is not list or len(rows) != 58 \
            or rows != sorted(rows, key=lambda row: row.get("path", "")
                              if type(row) is dict else ""):
        raise ValueError("static row count")
    seen: set[str] = set()
    for row in rows:
        if type(row) is not dict or not safe_relative(row.get("path")) \
                or row["path"] in seen or type(row.get("mode")) is not str \
                or re.fullmatch(r"0[0-7]{3}", row["mode"]) is None:
            raise ValueError("unsafe static row")
        seen.add(row["path"])
        if row.get("kind") == "directory":
            if set(row) != {"kind", "mode", "path"}:
                raise ValueError("static directory row")
        elif row.get("kind") == "regular":
            if set(row) != {"kind", "mode", "path", "sha256"} \
                    or type(row["sha256"]) is not str \
                    or HEX64.fullmatch(row["sha256"]) is None:
                raise ValueError("static regular row")
        else:
            raise ValueError("static kind")
    return rows, raw, seal_raw


def project_legacy_core(source: Path, projection: Path) -> None:
    projection.mkdir(mode=0o755)
    rows, manifest_raw, seal_raw = load_static_rows(source)
    for row in sorted((row for row in rows if row["kind"] == "directory"),
                      key=lambda item: (len(Path(item["path"]).parts), item["path"])):
        path = projection / row["path"]
        path.mkdir(parents=True, exist_ok=True)
        path.chmod(int(row["mode"], 8))
    for row in sorted((row for row in rows if row["kind"] == "regular"),
                      key=lambda item: item["path"]):
        path = projection / row["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        source_path = source / row["path"]
        metadata = os.lstat(source_path)
        if not stat.S_ISREG(metadata.st_mode) \
                or stat.S_IMODE(metadata.st_mode) != int(row["mode"], 8):
            raise ValueError("legacy static kind/mode changed during projection")
        file_raw = source_path.read_bytes()
        if sha_bytes(file_raw) != row["sha256"]:
            raise ValueError("legacy static byte changed during projection")
        path.write_bytes(file_raw)
        path.chmod(int(row["mode"], 8))
    (projection / STATIC_MANIFEST).write_bytes(manifest_raw)
    (projection / STATIC_SEAL).write_bytes(seal_raw)
    (projection / STATIC_MANIFEST).chmod(0o644)
    (projection / STATIC_SEAL).chmod(0o644)
    projection.chmod(0o755)


def paper_manifest(root: Path, output: Path) -> bytes:
    rows: list[tuple[str, str, str, str]] = []
    for path in root.rglob("*"):
        relative = path.relative_to(root).as_posix()
        if relative == "outputs" or relative.startswith("outputs/") \
                or relative == STATIC_SEAL:
            continue
        metadata = os.lstat(path)
        mode = f"{stat.S_IMODE(metadata.st_mode):04o}"
        if stat.S_ISDIR(metadata.st_mode):
            rows.append((relative, "directory", mode, "-"))
        elif stat.S_ISREG(metadata.st_mode):
            rows.append((relative, "regular", mode, sha_file(path)))
        else:
            raise ValueError("paper manifest nonregular root node")
    for path in output.rglob("*"):
        relative_output = path.relative_to(output).as_posix()
        if relative_output == "PAPER_MANIFEST.sha256":
            continue
        relative = "outputs/" + relative_output
        metadata = os.lstat(path)
        mode = f"{stat.S_IMODE(metadata.st_mode):04o}"
        if stat.S_ISDIR(metadata.st_mode):
            rows.append((relative, "directory", mode, "-"))
        elif stat.S_ISREG(metadata.st_mode):
            rows.append((relative, "regular", mode, sha_file(path)))
        else:
            raise ValueError("paper manifest nonregular output node")
    rows.sort()
    header = "paper44-state-b-manifest-v2 exclude=PREOUTPUT_STATIC_SEAL.json,PAPER_MANIFEST.sha256\n"
    return (header + "".join(f"{kind} {mode} {digest} {path}\n"
                              for path, kind, mode, digest in rows)).encode("ascii")


def exchange(left: Path, right: Path) -> None:
    library = ctypes.CDLL(None, use_errno=True)
    function = getattr(library, "renameat2", None)
    if function is None:
        raise OSError(errno.ENOSYS, "renameat2 unavailable")
    function.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p,
                         ctypes.c_uint]
    function.restype = ctypes.c_int
    result = function(AT_FDCWD, os.fsencode(left), AT_FDCWD, os.fsencode(right),
                      RENAME_EXCHANGE)
    if result != 0:
        observed = ctypes.get_errno()
        raise OSError(observed, os.strerror(observed))


def direct_final(root: Path, output: Path, commit: str) \
        -> tuple[int, bytes, bytes, dict[str, Any] | None]:
    return invoke([
        sys.executable, "-I", "-B", str(root / "code/integration/audit_integrity.py"),
        "--root", str(root), "--output-root", str(output), "--state", "B",
        "--phase", "FINAL", "--commit", commit,
    ], root.parent)


def main() -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--source", required=True)
    parser.add_argument("--target", required=True)
    parser.add_argument("--expected-publication-seal-sha256")
    parser.add_argument("--expected-stage1-commit")
    parser.add_argument("--force-late-failure", action="store_true")
    parser.add_argument("--inject-post-exchange-failure", action="store_true")
    parser.add_argument("--relocated-disposable", action="store_true")
    parser.add_argument("--allow-unexecuted-checklist", action="store_true")
    arguments = parser.parse_args()

    anchor = arguments.expected_publication_seal_sha256
    commit = arguments.expected_stage1_commit
    if anchor is None:
        return emit("REJECT", "EXPECTED_PUBLICATION_SEAL_SHA256_MISSING", {}, 2)
    if type(anchor) is not str or HEX64.fullmatch(anchor) is None:
        return emit("REJECT", "EXPECTED_PUBLICATION_SEAL_SHA256_INVALID", {}, 2)
    if commit is None:
        return emit("REJECT", "EXPECTED_STAGE1_COMMIT_MISSING", {}, 2)
    if type(commit) is not str or HEX40.fullmatch(commit) is None or commit == "0" * 40:
        return emit("REJECT", "EXPECTED_STAGE1_COMMIT_INVALID", {}, 2)

    try:
        source = secure_root(Path(arguments.source), "source")
        target = secure_root(Path(arguments.target), "target")
    except Exception as error:
        return emit("REJECT", "UNSAFE_ROOT", {"exception_type": type(error).__name__}, 2)
    if arguments.relocated_disposable and (
            not str(source).startswith("/tmp/") or not str(target).startswith("/tmp/")):
        return emit("REJECT", "RELOCATED_MODE_OUTSIDE_TMP_FORBIDDEN", {}, 2)
    if arguments.inject_post_exchange_failure and not arguments.relocated_disposable:
        return emit("REJECT", "INJECTION_REQUIRES_RELOCATED_DISPOSABLE", {}, 2)
    if arguments.force_late_failure and arguments.inject_post_exchange_failure:
        return emit("REJECT", "CONFLICTING_FAILURE_INJECTIONS", {}, 2)
    if arguments.allow_unexecuted_checklist and not arguments.relocated_disposable:
        return emit("REJECT", "CHECKLIST_OVERRIDE_REQUIRES_RELOCATED_DISPOSABLE", {}, 2)

    # The command protocol runs this bridge and its sibling auditor from an
    # externally authenticated, read-only controller copy.
    controller_auditor = Path(__file__).resolve(strict=True).with_name(
        "publication_auditor.py")
    pre = audit(controller_auditor, target, source, anchor, commit,
                arguments.relocated_disposable, arguments.allow_unexecuted_checklist)
    if pre[0] != 0 or pre[2] or pre[3] is None:
        nested = pre[3].get("payload", {}).get("code") if pre[3] else "INVALID_ENVELOPE"
        return emit("REJECT", "TARGET_PREFLIGHT_REJECT", {"nested_code": nested}, 2)
    state = pre[3].get("payload", {}).get("state")
    if state == "PUBLISHED_STATE_B_EXACT":
        return emit("PASS", "ALREADY_STATE_B_EXACT", {
            "atomic_output_exchanges": 0,
            "physical_target_replacements": 0,
            "stage1_commit_bound_three_times": True,
            "state": state,
        }, 0)
    if state != "PUBLISHED_STATE_A_EXACT":
        return emit("REJECT", "STATE_B_SOURCE_STATE_FORBIDDEN", {"state": state}, 2)

    before_target = logical_tree(target)
    before_outputs = logical_tree(target / "outputs")
    root_metadata = os.lstat(target)
    root_times = (root_metadata.st_atime_ns, root_metadata.st_mtime_ns)
    temporary = Path(tempfile.mkdtemp(prefix=".paper44-stateb-bridge-", dir=target.parent))
    projection = temporary / "legacy_core"
    full_stage = temporary / "full_published"
    exchanged = False
    try:
        project_legacy_core(target, projection)
        runner = invoke([
            sys.executable, "-I", "-B", str(projection / "code/integration/run_integration.py"),
            "--state", "B", "--commit", commit,
        ], projection.parent)
        if runner[0] != 0 or runner[2] or runner[3] is None \
                or runner[3].get("status") != "PASS" \
                or runner[3].get("payload", {}).get("state") != "B" \
                or runner[3].get("payload", {}).get("atomic_rename_count") != 1:
            raise ValueError("legacy-core State B build rejected")

        shutil.copytree(target, full_stage, copy_function=shutil.copy2)
        shutil.rmtree(full_stage / "outputs")
        shutil.copytree(projection / "outputs", full_stage / "outputs", copy_function=shutil.copy2)
        manifest_raw = paper_manifest(full_stage, full_stage / "outputs")
        (full_stage / PAPER_MANIFEST).write_bytes(manifest_raw)
        (full_stage / PAPER_MANIFEST).chmod(0o644)
        direct = direct_final(full_stage, full_stage / "outputs", commit)
        if direct[0] != 0 or direct[2] or direct[3] is None \
                or direct[3].get("status") != "PASS" \
                or direct[3].get("payload", {}).get("state") != "B":
            raise ValueError("full-root direct FINAL B rejected")
        staged = audit(controller_auditor, full_stage, source, anchor, commit,
                       arguments.relocated_disposable,
                       arguments.allow_unexecuted_checklist)
        if staged[0] != 0 or staged[2] or staged[3] is None \
                or staged[3].get("payload", {}).get("state") != "PUBLISHED_STATE_B_EXACT":
            nested = staged[3].get("payload", {}).get("code") if staged[3] else "INVALID_ENVELOPE"
            raise ValueError("full-root publication audit rejected: " + nested)

        if logical_tree(target) != before_target:
            raise TargetChangedDuringStaging("target changed during State B staging")

        if arguments.force_late_failure:
            unchanged = logical_tree(target / "outputs") == before_outputs
            shutil.rmtree(temporary)
            return emit("FORCED_FAILURE", "FORCED_LATE_FAILURE", {
                "atomic_output_exchanges": 0,
                "full_state_B_bytes_staged": True,
                "physical_target_replacements": 0,
                "target_outputs_unchanged": unchanged,
            }, 86)

        exchange(target / "outputs", full_stage / "outputs")
        exchanged = True
        os.utime(target, ns=root_times)
        if arguments.inject_post_exchange_failure:
            raise RuntimeError("injected post-exchange failure")
        post = audit(controller_auditor, target, source, anchor, commit,
                     arguments.relocated_disposable,
                     arguments.allow_unexecuted_checklist)
        if post[0] != 0 or post[2] or post[3] is None \
                or post[3].get("payload", {}).get("state") != "PUBLISHED_STATE_B_EXACT":
            nested = post[3].get("payload", {}).get("code") if post[3] else "INVALID_ENVELOPE"
            raise RuntimeError("post-exchange audit rejected: " + nested)
        final_tree = post[3]["payload"]["runtime"]["final_tree_sha256"]
        paper_rows = post[3]["payload"]["paper_manifest_entry_count"]
        shutil.rmtree(temporary)
        return emit("PASS", "TRANSITIONED_TO_STATE_B_EXACT", {
            "atomic_output_exchanges": 1,
            "direct_final_verification_sha256": sha_bytes(direct[1]),
            "legacy_core_runner_result_sha256": sha_bytes(runner[1]),
            "paper_manifest_entry_count": paper_rows,
            "physical_target_replacements": 1,
            "stage1_commit_bound_three_times": True,
            "state": "PUBLISHED_STATE_B_EXACT",
            "state_B_final_tree_sha256": final_tree,
        }, 0)
    except TargetChangedDuringStaging:
        shutil.rmtree(temporary, ignore_errors=True)
        return emit("REJECT", "TARGET_CHANGED_DURING_STAGING", {
            "atomic_output_exchanges": 0,
            "physical_target_replacements": 0,
            "target_writes_by_bridge": 0,
        }, 2)
    except Exception as error:
        rollback_ok = True
        rollback_performed = False
        if exchanged:
            try:
                exchange(target / "outputs", full_stage / "outputs")
                rollback_performed = True
                exchanged = False
                os.utime(target, ns=root_times)
                rollback = audit(controller_auditor, target, source, anchor, commit,
                                 arguments.relocated_disposable,
                                 arguments.allow_unexecuted_checklist)
                rollback_ok = rollback[0] == 0 and not rollback[2] and rollback[3] is not None \
                    and rollback[3].get("payload", {}).get("state") == "PUBLISHED_STATE_A_EXACT" \
                    and logical_tree(target / "outputs") == before_outputs
            except Exception:
                rollback_ok = False
        else:
            rollback_ok = logical_tree(target / "outputs") == before_outputs
        shutil.rmtree(temporary, ignore_errors=True)
        if isinstance(error, RuntimeError) and "injected post-exchange" in str(error):
            return emit("ROLLED_BACK" if rollback_ok else "ROLLBACK_FAILED",
                        "INJECTED_POST_EXCHANGE_FAILURE_ROLLED_BACK" if rollback_ok
                        else "STATE_B_ROLLBACK_FAILED", {
                            "atomic_output_exchanges_before_rollback": 1,
                            "rollback_exchange_count": 1 if rollback_ok else 0,
                            "target_outputs_unchanged": rollback_ok,
                        }, 87 if rollback_ok else 88)
        return emit("REJECT", "STATE_B_STAGING_FAILED", {
            "exception_type": type(error).__name__,
            "rollback_performed": rollback_performed,
            "target_outputs_unchanged": rollback_ok,
        }, 2 if rollback_ok else 88)


if __name__ == "__main__":
    raise SystemExit(main())
