"""Operational resume closure; validates archives, never executes science.

Preserves the previously completed 2026-09-06 outer seal and appends only
archival records. Scientific kernels, capsules, canonical and gate reports
are not changed.
"""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import time

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[3]
DEST = BASE / "resume_closure"
DEST.mkdir(exist_ok=False)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save(name, value):
    (DEST / name).write_text(json.dumps(value, sort_keys=True, indent=2) + "\n")


def command(argv, cwd, tag):
    started = time.time()
    process = subprocess.run(argv, cwd=cwd, capture_output=True, check=False)
    (DEST / (tag + ".stdout")).write_bytes(process.stdout)
    (DEST / (tag + ".stderr")).write_bytes(process.stderr)
    row = {"argv": argv, "cwd": str(cwd), "exit": process.returncode,
           "started_epoch": started, "finished_epoch": time.time(),
           "stdout": tag + ".stdout", "stderr": tag + ".stderr"}
    save(tag + ".command.json", row)
    if process.returncode:
        raise RuntimeError(row)
    return row


old_manifest = BASE / "SHA256SUMS"
expected_old_seal = "fcd3589bddc5aef6fd237b2b3ec72658f2a305025d329eda174bee7d1887ed76"
if sha(old_manifest) != expected_old_seal:
    raise RuntimeError("OLD_COMPLETE_SEAL_CHANGED")
shutil.copyfile(old_manifest, DEST / "INITIAL_COMPLETE_SHA256SUMS")
old_entries = {line.split("  ", 1)[1]: line.split("  ", 1)[0]
               for line in old_manifest.read_text().splitlines()}
commands = [command(["/usr/bin/sha256sum", "-c", str(old_manifest)], BASE, "initial_complete_seal")]
for name, cwd, tag in [("INPUT_PINS.sha256", ROOT, "input_originals"),
                       ("SUPPLEMENT_INPUTS.sha256", ROOT, "supplement_originals"),
                       ("INPUT_PINS.sha256", BASE / "reviewed_input_snapshot", "input_snapshots"),
                       ("SUPPLEMENT_INPUTS.sha256", BASE / "supplementary_source_snapshot", "supplement_snapshots")]:
    commands.append(command(["/usr/bin/sha256sum", "-c", str(BASE / name)], cwd, tag))
for left, right, tag in [("replay_01/producer.stdout", "replay_02/producer.stdout", "pair"),
                         ("CANONICAL.json", "replay_01/producer.stdout", "canonical_01"),
                         ("CANONICAL.json", "replay_02/producer.stdout", "canonical_02")]:
    commands.append(command(["/usr/bin/cmp", "--", str(BASE / left), str(BASE / right)], BASE, tag))
checks = []
for run in ["replay_01", "replay_02"]:
    for kind in ["science", "runtime"]:
        before = json.loads((BASE / run / (kind + ".before.json")).read_text())
        after = json.loads((BASE / run / (kind + ".after.json")).read_text())
        current = {path: sha(path) for path in before}
        mismatch = {path: {"before": digest, "after": after.get(path), "current": current[path]}
                    for path, digest in before.items() if digest != after.get(path) or digest != current[path]}
        save(run + "." + kind + ".current.json", current)
        checks.append({"run": run, "kind": kind, "files": len(before), "mismatches": mismatch})
        if mismatch:
            raise RuntimeError(checks[-1])
history_before = json.loads((BASE / "history_discovery/before.json").read_text())
history_after = json.loads((BASE / "history_discovery/after.json").read_text())
history_current = {path: sha(path) for path in history_before}
history_changed = {path: {"before": digest, "after": history_after.get(path), "current": history_current[path]}
                   for path, digest in history_before.items()
                   if digest != history_after.get(path) or digest != history_current[path]}
save("history.current.json", history_current)
save("history.current_differences.json", history_changed)
if history_before != history_after:
    raise RuntimeError("HISTORICAL_SEARCH_ORIGINAL_PIN_MISMATCH")
# Historical discovery inputs not consumed by the kernels are reported
# separately; no unrelated later manuscript edit is hidden as gate science.
for rel, digest in old_entries.items():
    if sha(BASE / rel) != digest:
        raise RuntimeError(("OLD_SEALED_ARTIFACT_CHANGED", rel))
receipt = {"kind": "OPERATIONAL_RESUME_ARCHIVAL_CLOSURE_ZERO_NEW_SCIENTIFIC_RUNS", "status": "PASS",
           "invocation": sys.argv, "flags": str(sys.flags), "finished_epoch": time.time(),
           "preserved_initial_seal_sha256": expected_old_seal, "preserved_initial_payload_count": len(old_entries),
           "initial_sealer_completion": {"actual_exit": 0, "polled_after_resume": True,
              "new_stdout": "", "meaning": "completed sealer; no failed producer"},
           "commands": commands, "science_runtime_current_checks": checks,
           "history_pinned_files_including_rg_and_searcher": len(history_before),
           "history_current_difference_count": len(history_changed),
           "history_current_differences": "history.current_differences.json",
           "original_sealed_artifacts_unchanged": True,
           "scientific_replays_total": 2, "new_scientific_replays_on_resume": 0,
           "canonical_sha256": sha(BASE / "CANONICAL.json")}
save("RECEIPT.json", receipt)
all_files = sorted(p for p in BASE.rglob("*") if p.is_file() and p != old_manifest)
final_manifest = "".join(sha(p) + "  " + str(p.relative_to(BASE)) + "\n" for p in all_files)
old_manifest.write_text(final_manifest)
process = subprocess.run(["/usr/bin/sha256sum", "-c", "SHA256SUMS"], cwd=BASE, capture_output=True, check=False)
if process.returncode:
    raise RuntimeError(process.stderr.decode())
actual_files = sorted(str(p.relative_to(BASE)) for p in BASE.rglob("*") if p.is_file() and p != old_manifest)
if actual_files != [str(p.relative_to(BASE)) for p in all_files]:
    raise RuntimeError("INCOMPLETE_NONSELF_MANIFEST")
print(json.dumps({"status": "RESUME_CLOSURE_SEALED", "old_payloads_unchanged": len(old_entries),
                  "final_payload_count": len(all_files), "final_sha256_check_exit": process.returncode,
                  "final_ok_lines": len(process.stdout.splitlines()), "manifest_sha256": sha(old_manifest),
                  "canonical_sha256": sha(BASE / "CANONICAL.json"), "history_current_difference_count": len(history_changed),
                  "new_scientific_runs": 0}, sort_keys=True))
