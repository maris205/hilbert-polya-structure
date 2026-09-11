"""Resolve only the archived Path-versus-string coverage-order mismatch."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import time

BASE = Path(__file__).resolve().parent
DEST = BASE / "final_resume_closure"
DEST.mkdir(exist_ok=False)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save(name, value):
    (DEST / name).write_text(json.dumps(value, sort_keys=True, indent=2) + "\n")


def command(argv, tag):
    started = time.time()
    process = subprocess.run(argv, cwd=BASE, capture_output=True, check=False)
    (DEST / (tag + ".stdout")).write_bytes(process.stdout)
    (DEST / (tag + ".stderr")).write_bytes(process.stderr)
    row = {"argv": argv, "cwd": str(BASE), "exit": process.returncode,
           "started_epoch": started, "finished_epoch": time.time(),
           "stdout": tag + ".stdout", "stderr": tag + ".stderr"}
    save(tag + ".command.json", row)
    if process.returncode:
        raise RuntimeError(row)
    return row


outer = BASE / "SHA256SUMS"
expected_attempt = "5f8148dfc52d5fede1929d97fa72b2a14af4cefbbe5dd9d191a67da7be530858"
if sha(outer) != expected_attempt:
    raise RuntimeError("ATTEMPT_SEAL_CHANGED")
shutil.copyfile(outer, DEST / "PRESERVED_ATTEMPT_SHA256SUMS")
attempt_rows = [line.split("  ", 1) for line in outer.read_text().splitlines()]
original = BASE / "resume_closure/INITIAL_COMPLETE_SHA256SUMS"
original_rows = [line.split("  ", 1) for line in original.read_text().splitlines()]
tools_before = {p: sha(p) for p in ["/usr/bin/sha256sum", "/usr/bin/cmp"]}
commands = [command(["/usr/bin/sha256sum", "-c", str(outer)], "preserved_attempt"),
            command(["/usr/bin/sha256sum", "-c", str(original)], "original_complete_seal")]
listed = [rel for digest, rel in attempt_rows]
if len(listed) != len(set(listed)):
    raise RuntimeError("DUPLICATE_PATH")
existing = [rel for rel in listed if (BASE / rel).is_file()]
if len(existing) != len(listed):
    raise RuntimeError("ACTUAL_MISSING_PATH")
(DEST / "attempt_paths.normalized.txt").write_text("\n".join(sorted(listed)) + "\n")
(DEST / "existing_paths.normalized.txt").write_text("\n".join(sorted(existing)) + "\n")
commands.append(command(["/usr/bin/cmp", "--", str(DEST / "attempt_paths.normalized.txt"),
                         str(DEST / "existing_paths.normalized.txt")], "normalized_path_coverage"))
current_checks = []
for run in ["replay_01", "replay_02"]:
    for kind in ["science", "runtime"]:
        expected = json.loads((BASE / run / (kind + ".before.json")).read_text())
        current = {path: sha(path) for path in expected}
        if expected != current:
            raise RuntimeError(("CURRENT_DEPENDENCY_CHANGED", run, kind))
        current_checks.append({"run": run, "kind": kind, "files": len(current), "unchanged": True})
history = json.loads((BASE / "history_discovery/before.json").read_text())
if history != {path: sha(path) for path in history}:
    raise RuntimeError("CURRENT_HISTORY_CHANGED")
for digest, rel in original_rows + attempt_rows:
    if sha(BASE / rel) != digest:
        raise RuntimeError(("PRESERVED_PAYLOAD_CHANGED", rel))
tools_after = {p: sha(p) for p in tools_before}
if tools_before != tools_after:
    raise RuntimeError("AUDIT_TOOL_CHANGED")
receipt = {"kind": "FINAL_OPERATIONAL_RESUMPTION_ARCHIVAL_CLOSURE", "status": "PASS",
           "argv": sys.argv, "flags": str(sys.flags), "finished_epoch": time.time(),
           "resolved_failure": "Path component ordering versus relative-string ordering only",
           "failure_original": "../RESUME_CLOSURE_ORDERING_FAILURE.md",
           "commands": commands, "original_payload_count": len(original_rows),
           "attempt_payload_count": len(attempt_rows), "all_original_and_attempt_payloads_unchanged": True,
           "current_science_runtime_checks": current_checks, "current_history_pins_unchanged": len(history),
           "tools_before": tools_before, "tools_after": tools_after,
           "new_scientific_runs": 0, "total_scientific_runs": 2,
           "canonical_sha256": sha(BASE / "CANONICAL.json")}
save("RECEIPT.json", receipt)
all_files = sorted((p for p in BASE.rglob("*") if p.is_file() and p != outer),
                   key=lambda p: str(p.relative_to(BASE)))
manifest = "".join(sha(p) + "  " + str(p.relative_to(BASE)) + "\n" for p in all_files)
outer.write_text(manifest)
actual = subprocess.run(["/usr/bin/sha256sum", "-c", "SHA256SUMS"], cwd=BASE, capture_output=True, check=False)
if actual.returncode:
    raise RuntimeError(actual.stderr.decode())
expected_paths = [line.split("  ", 1)[1] for line in manifest.splitlines()]
actual_paths = sorted(str(p.relative_to(BASE)) for p in BASE.rglob("*") if p.is_file() and p != outer)
if expected_paths != actual_paths:
    raise RuntimeError("ACTUAL_FINAL_COVERAGE_FAILURE")
print(json.dumps({"status": "FINAL_RESUMPTION_SEALED", "final_payload_count": len(all_files),
                  "actual_final_checksum_exit": actual.returncode,
                  "actual_final_ok_lines": len(actual.stdout.splitlines()),
                  "complete_nonself_coverage": True, "manifest_sha256": sha(outer),
                  "canonical_sha256": sha(BASE / "CANONICAL.json"),
                  "original_payloads_unchanged": len(original_rows),
                  "preserved_attempt_payloads_unchanged": len(attempt_rows),
                  "current_history_pins_unchanged": len(history), "new_scientific_runs": 0}, sort_keys=True))
