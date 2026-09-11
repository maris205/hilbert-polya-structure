"""Post-pilot archive diagnostics, not science, repair, or a strict-runtime pass.

The original lock/audit.py is never modified or bypassed in a replay.  collect
captures a NEW invocation of that read-only audit and preserves its failure.
verify reads the sealed package and never launches either audit or producer.
"""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

BASE = Path(__file__).resolve().parent
OUT = BASE / "postrun_diagnostic_v2"
MISSING = "/usr/lib/locale/C.utf8/LC_CTYPE"
ALL_MISSING = [MISSING, "/usr/lib/x86_64-linux-gnu/gconv/gconv-modules.cache"]


def digest(path):
    raw = Path(path).read_bytes()
    return {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}


def expected(row):
    return {key: row[key] for key in ("bytes", "sha256")}


def dump(path, value):
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


def manifest_check(base):
    manifest = base / "MANIFEST.json"
    data = json.loads(manifest.read_text())
    listed = [row["path"] for row in data["files"]]
    actual = {str(path.relative_to(base)) for path in base.rglob("*")
              if path.is_file() and path != manifest}
    if len(listed) != len(set(listed)) or set(listed) != actual:
        raise AssertionError(("manifest inventory mismatch", str(base)))
    for row in data["files"]:
        if digest(base / row["path"]) != expected(row):
            raise AssertionError(("manifest payload mismatch", row["path"]))
    return {"payloads": len(actual), "bytes": sum(row["bytes"] for row in data["files"])}


def diagnose_existing():
    """Read and reconcile existing receipts without evaluating the KIP map."""
    desk = manifest_check(BASE.with_name("finite_semigroup_lane"))
    frozen_desk = manifest_check(BASE / "lock" / "desk")
    pins_path = BASE / "PRE_EXECUTION_PINS.json"
    pins = json.loads(pins_path.read_text())
    allowed = {}
    for row in pins["rows"]:
        pin = expected(row)
        for path in (Path(row["origin"]), BASE / row["frozen"]):
            if digest(path) != pin:
                raise AssertionError(("original locked file changed", str(path)))
            allowed[str(path.resolve())] = pin
    receipts = {}
    for directory, streams in (("preflight", (("stdout", "runtime_probe.stdout.json"),
                                             ("stderr", "runtime_probe.stderr.txt"))),
                               ("execution_01", (("stdout", "stdout.jsonl"),
                                                 ("stderr", "stderr.txt")))):
        receipts[directory] = json.loads((BASE / directory / "NATIVE_RECEIPT.json").read_text())
        for field, name in streams:
            if digest(BASE / directory / name) != receipts[directory][field]:
                raise AssertionError(("native stream changed", directory, name))
    receipt = receipts["execution_01"]
    if receipt["native_exit"] != 0 or receipt["timed_out"] or receipt["launch_error"] is not None:
        raise AssertionError("science native status differs from bounded successful run")
    if receipt["scientific_producer_invocations"] != 1:
        raise AssertionError("recorded invocation count is not one")
    if receipt["pre_execution_pins_before"] != digest(pins_path) or receipt["pre_execution_pins_after"] != digest(pins_path):
        raise AssertionError("pre-execution pins changed")
    if receipt["input_pins_before"] != receipt["input_pins_after"]:
        raise AssertionError("recorded input pins changed during science")
    if len(receipt["input_pins_before"]) != len(pins["rows"]):
        raise AssertionError("recorded input inventory differs")
    for row, observed in zip(pins["rows"], receipt["input_pins_before"]):
        if observed != {"origin": row["origin"], "frozen": row["frozen"],
                        "origin_pin": expected(row), "frozen_pin": expected(row)}:
            raise AssertionError(("recorded pin row changed", row["origin"]))
    records = [json.loads(line) for line in (BASE / "execution_01" / "stdout.jsonl").read_bytes().splitlines()]
    kinds = [record["kind"] for record in records]
    if kinds.count("contract") != 1 or kinds.count("runtime") != 1 or kinds.count("complete") != 1:
        raise AssertionError("canonical markers differ")
    if kinds[0] != "contract" or kinds[-2:] != ["runtime", "complete"]:
        raise AssertionError("canonical marker order differs")
    boxes = [row for row in records if row["kind"] == "box"]
    states = [row for row in records if row["kind"] == "state"]
    if [row["n"] for row in boxes] != list(range(1, 8)) or len(states) != 2353:
        raise AssertionError("native box/state census differs")
    for n, size, box in zip(range(1, 8), (1, 3, 10, 35, 126, 462, 1716), boxes):
        rows = [row for row in states if row["n"] == n]
        table = {tuple(row["source"]): row for row in rows}
        if len(rows) != size or len(table) != size or box["states"] != size:
            raise AssertionError(("native carrier census differs", n))
        reverse = {source: [] for source in table}
        for source, row in table.items():
            successor = tuple(row["successor"])
            if successor not in reverse:
                raise AssertionError(("recorded edge exits recorded carrier", n))
            reverse[successor].append(list(source))
            if row["predecessors"] != sorted(row["predecessors"]) or row["decoded_predecessors"] != row["predecessors"]:
                raise AssertionError(("recorded decoder rows differ", n))
        for target, predecessors in reverse.items():
            if sorted(predecessors) != table[target]["predecessors"]:
                raise AssertionError(("recorded reverse edges differ", n))
    complete = records[-1]
    if complete["total_states"] != 2353 or complete["scientific_producer_invocations"] != 1:
        raise AssertionError("native completion scope differs")
    totals = {key: sum(box["assertions"][key] for box in boxes) for key in complete["assertions"]}
    if totals != complete["assertions"] or sum(totals.values()) != complete["assertion_total"]:
        raise AssertionError("native assertion sums differ")
    child = next(row for row in records if row["kind"] == "runtime")
    probe = json.loads((BASE / "preflight" / "runtime_probe.stdout.json").read_text())
    observations = {"preflight_probe": probe, "scientific_child": child,
                    "launcher": receipt["launcher_runtime"]}
    runtime_comparison = {}
    for name, observation in observations.items():
        missing = [pin for pin in observation["file_pins"]
                   if allowed.get(str(Path(pin["path"]).resolve())) != expected(pin)]
        runtime_comparison[name] = {"observed_file_count": len(observation["file_pins"]),
                                    "observed_mapped_paths": observation["mapped_runtime_paths"],
                                    "not_prelocked": missing}
    if runtime_comparison["scientific_child"]["not_prelocked"] or runtime_comparison["preflight_probe"]["not_prelocked"]:
        raise AssertionError("new child or preflight runtime discrepancy")
    if [pin["path"] for pin in runtime_comparison["launcher"]["not_prelocked"]] != ALL_MISSING:
        raise AssertionError("launcher discrepancy differs from complete posthoc scan")
    return {
        "scope": "POSTHOC_READ_ONLY_ARCHIVE_DIAGNOSTIC_NOT_SCIENTIFIC_REEXECUTION",
        "strict_observed_runtime_prelock_status": "FAIL_PRESERVED",
        "hermetic_or_strict_replay_certified": False,
        "original_desk": desk, "frozen_desk": frozen_desk,
        "physical_lock_rows_unchanged": len(pins["rows"]),
        "native_streams_digest_reconciled": 4,
        "scientific_producer_invocations_from_original_receipt": 1,
        "scientific_native_exit_from_original_receipt": receipt["native_exit"],
        "elapsed_seconds_from_original_receipt": receipt["elapsed_seconds"],
        "state_records": len(states), "assertion_total_from_native": complete["assertion_total"],
        "assertions_from_native": complete["assertions"], "boxes_from_native": boxes,
        "runtime_comparison": runtime_comparison,
        "scientific_child_environment_from_receipt": receipt["environment"],
        "preflight_probe_environment_from_receipt": probe["environment"],
        "launcher_environment_at_original_run": "NOT_RECORDED_DO_NOT_RECONSTRUCT",
        "launcher_setting_evidence": "Frozen run_pilot.py does not set its own environment and launches the child with explicit C locale; original launcher /proc/self/maps observes C.utf8/LC_CTYPE and gconv-modules.cache. This localizes the missing prelock to the launcher, but does not recover its contemporaneous locale variables.",
        "conclusion": "Bounded author pilot observations retained. Original strict-runtime audit remains failed. No extra science run, input-list repair, or blanket verification PASS.",
    }


def collect():
    OUT.mkdir(exist_ok=False)
    before = diagnose_existing()
    dump(OUT / "DIAGNOSIS.json", before)
    argv = ["/usr/bin/python3.10", "-I", "-S", "-B", str(BASE / "lock" / "audit.py"), "audit"]
    environment = {"LANG": "C", "LC_ALL": "C", "PATH": "/usr/bin:/bin", "TZ": "UTC"}
    started = time.time_ns()
    result = subprocess.run(argv, cwd=BASE, env=environment, capture_output=True, timeout=60, check=False)
    finished = time.time_ns()
    (OUT / "audit_recapture.stdout.txt").write_bytes(result.stdout)
    (OUT / "audit_recapture.stderr.txt").write_bytes(result.stderr)
    dump(OUT / "AUDIT_RECAPTURE_NATIVE_RECEIPT.json", {
        "kind": "NEW_READ_ONLY_AUDIT_INVOCATION_NOT_THE_INITIAL_FAILURE_NOT_SCIENCE",
        "argv": argv, "cwd": str(BASE), "environment": environment,
        "source": {"path": str(BASE / "lock" / "audit.py"), **digest(BASE / "lock" / "audit.py")},
        "diagnostic_driver": {"path": str(Path(__file__).resolve()), **digest(__file__)},
        "started_ns": started, "finished_ns": finished, "native_exit": result.returncode,
        "stdout": digest(OUT / "audit_recapture.stdout.txt"),
        "stderr": digest(OUT / "audit_recapture.stderr.txt"),
        "scientific_producer_invocations_in_this_diagnostic": 0,
        "original_science_runs_unchanged": True,
        "retrospective_original_receipt": False,
    })
    after = diagnose_existing()
    if before != after:
        raise AssertionError("existing artifact diagnosis changed during read-only audit")
    if result.returncode != 1 or result.stdout or ("AssertionError: ('unfrozen observed runtime file', '" + MISSING + "')").encode() not in result.stderr:
        raise AssertionError("original strict audit no longer shows the same failure")
    print(json.dumps({"scope": "read_only_artifact_closeout", "strict_runtime_status": "FAIL_PRESERVED",
                      "new_read_only_audit_native_exit": result.returncode,
                      "new_scientific_producer_invocations": 0,
                      "state_records_from_original": before["state_records"],
                      "assertion_total_from_original": before["assertion_total_from_native"]}, sort_keys=True))


def verify():
    inventory = manifest_check(BASE)
    current = diagnose_existing()
    if current != json.loads((OUT / "DIAGNOSIS.json").read_text()):
        raise AssertionError("sealed diagnosis mismatch")
    receipt = json.loads((OUT / "AUDIT_RECAPTURE_NATIVE_RECEIPT.json").read_text())
    for key, name in (("stdout", "audit_recapture.stdout.txt"), ("stderr", "audit_recapture.stderr.txt")):
        if digest(OUT / name) != receipt[key]:
            raise AssertionError(("audit recapture stream mismatch", name))
    if receipt["native_exit"] != 1 or receipt["scientific_producer_invocations_in_this_diagnostic"] != 0 or receipt["retrospective_original_receipt"]:
        raise AssertionError("recapture semantics changed")
    if receipt["diagnostic_driver"]["sha256"] != digest(__file__)["sha256"]:
        raise AssertionError("diagnostic driver changed after recapture")
    print(json.dumps({"scope": "SEALED_ARCHIVE_INTEGRITY_ONLY_NOT_STRICT_RUNTIME_OR_REVIEW",
                      "complete_nonself_manifest": inventory,
                      "strict_runtime_prelock_status": "FAIL_PRESERVED",
                      "science_runs_reexecuted": 0, "hermetic_replay_certified": False}, sort_keys=True))


if __name__ == "__main__":
    {"collect": collect, "verify": verify}[sys.argv[1]]()

