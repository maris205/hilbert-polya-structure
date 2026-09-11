"""KIP gate evidence only: no scientific model is imported or executed."""
from pathlib import Path
import datetime
import hashlib
import json
import subprocess
import sys

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[3]
AUTHOR = BASE.parent / "finite_semigroup_lane"
SOURCE_DESK = BASE.parent / "kip_source_desk"
PILOT = BASE.parent / "finite_semigroup_pilot"


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def pin(path):
    raw = path.read_bytes()
    return {"path": str(path), "bytes": len(raw), "sha256": sha(raw)}


def checked_manifest(folder, name):
    rows = []
    if name.endswith(".json"):
        manifest = json.loads((folder / name).read_text())
        assert manifest["self_excluded"] == name
        input_rows = [(row["sha256"], row["path"], row["bytes"]) for row in manifest["files"]]
    else:
        input_rows = [(digest, rel, None) for digest, rel in
                      (line.split("  ", 1) for line in (folder / name).read_text().splitlines())]
    for digest, rel, expected_size in input_rows:
        assert rel and not Path(rel).is_absolute() and ".." not in Path(rel).parts
        raw = (folder / rel).read_bytes()
        assert sha(raw) == digest, rel
        assert expected_size is None or len(raw) == expected_size, rel
        rows.append({"path": rel, "bytes": len(raw), "sha256": digest})
    actual = sorted(str(path.relative_to(folder)) for path in folder.rglob("*")
                    if path.is_file() and path != folder / name)
    assert sorted(row["path"] for row in rows) == actual, (folder, "membership")
    return {"directory": str(folder), "manifest": pin(folder / name),
            "payload_files": len(rows), "payload_bytes": sum(r["bytes"] for r in rows),
            "payload": rows}


def native(label, argv, cwd=ROOT):
    folder = BASE / "native"
    folder.mkdir(exist_ok=True)
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    proc = subprocess.run(argv, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ended = datetime.datetime.now(datetime.timezone.utc).isoformat()
    out, err = folder / (label + ".stdout"), folder / (label + ".stderr")
    out.write_bytes(proc.stdout)
    err.write_bytes(proc.stderr)
    receipt = {"argv": argv, "cwd": str(cwd), "started_utc": started,
               "ended_utc": ended, "exit_code": proc.returncode,
               "stdout": pin(out), "stderr": pin(err),
               "scope": "documentation_source_or_archived_evidence_only"}
    dump(folder / (label + ".json"), receipt)
    print(json.dumps({"native": label, "exit_code": proc.returncode,
                      "stdout_bytes": len(proc.stdout), "stderr_bytes": len(proc.stderr)}))
    return proc.returncode


def historical_capture():
    rows = json.loads((AUTHOR / "HISTORY_PINS.json").read_text())
    captures = []
    for index, row in enumerate(rows, 1):
        old = ROOT / row["source"]
        snap = AUTHOR / row["snapshot"]
        raw = old.read_bytes()
        assert raw == snap.read_bytes()
        assert len(raw) == row["bytes"] and sha(raw) == row["sha256"]
        target = BASE / "historical" / (f"{index:02d}_" + old.name)
        target.parent.mkdir(exist_ok=True)
        target.write_bytes(raw)
        captures.append({"source": str(old), "author_snapshot": str(snap),
                         "gate_snapshot": str(target.relative_to(BASE)),
                         "bytes": len(raw), "sha256": sha(raw),
                         "raw_equal": raw == target.read_bytes() == snap.read_bytes()})
    extra = []
    for name in ["PROBLEM_ANCHOR.md", "HOSTILE_REVIEW_PROTOCOL.md"]:
        path = ROOT / "docs/papers197_201_sequence" / name
        out = BASE / "historical" / ("inherited_" + name)
        raw = path.read_bytes()
        out.write_bytes(raw)
        extra.append({"source": str(path), "gate_snapshot": str(out.relative_to(BASE)),
                      "bytes": len(raw), "sha256": sha(raw), "raw_equal": raw == out.read_bytes()})
    dump(BASE / "HISTORICAL_PINS.json", {"author_historical": captures, "inherited": extra})
    dump(BASE / "AUTHOR_PACKAGE_CHECK.json", checked_manifest(AUTHOR, "MANIFEST.json"))
    dump(BASE / "SOURCE_DESK_CHECK.json", checked_manifest(SOURCE_DESK, "MANIFEST.sha256"))
    all_paths = [ROOT / row["source"] for row in rows]
    all_paths += [ROOT / "docs/papers197_201_sequence" / name
                  for name in ["PROBLEM_ANCHOR.md", "HOSTILE_REVIEW_PROTOCOL.md"]]
    (BASE / "HISTORICAL_INPUTS.sha256").write_text("".join(
        sha(path.read_bytes()) + "  " + str(path) + "\n" for path in all_paths))
    native("01_historical_sha", ["sha256sum", "-c", str(BASE / "HISTORICAL_INPUTS.sha256")])
    native("02_author_seal", ["python", "capture.py", "verify"], AUTHOR)
    native("03_source_desk_seal", ["sha256sum", "-c", "MANIFEST.sha256"], SOURCE_DESK)


def source_capture():
    folder = BASE / "sources"
    folder.mkdir(exist_ok=True)
    pdf = folder / "higgins_2019.pdf"
    status = native("04_higgins_download", ["curl", "--fail", "--location", "--max-time", "45",
        "https://repository.essex.ac.uk/24377/1/Semigroup%20Forum%20Involution%20paper%202019.pdf",
        "--output", str(pdf)])
    if status == 0:
        native("05_higgins_text", ["pdftotext", "-layout", str(pdf), str(folder / "higgins_2019.txt")])
        native("06_higgins_pages", ["pdftoppm", "-f", "12", "-l", "13", "-scale-to", "1500", "-png",
                                     str(pdf), str(folder / "higgins_page")])


def archived_pilot_check():
    """Check recorded relationships only; never evaluate the KIP update."""
    receipt = json.loads((PILOT / "execution_01/NATIVE_RECEIPT.json").read_text())
    locks = json.loads((PILOT / "PRE_EXECUTION_PINS.json").read_text())
    assert receipt["native_exit"] == 0 and not receipt["timed_out"]
    assert receipt["launch_error"] is None and receipt["scientific_producer_invocations"] == 1
    assert receipt["input_pins_before"] == receipt["input_pins_after"]
    assert len(receipt["input_pins_before"]) == len(locks["rows"]) == 98
    allowed = {}
    for before, row in zip(receipt["input_pins_before"], locks["rows"]):
        orig, frozen = Path(row["origin"]), PILOT / row["frozen"]
        raw = orig.read_bytes()
        assert raw == frozen.read_bytes()
        expected = {"bytes": len(raw), "sha256": sha(raw)}
        assert expected == {key: row[key] for key in ("bytes", "sha256")}
        assert before == {"origin": row["origin"], "frozen": row["frozen"],
                          "origin_pin": expected, "frozen_pin": expected}
        allowed[str(orig.resolve())] = expected
        allowed[str(frozen.resolve())] = expected
    pin_raw = (PILOT / "PRE_EXECUTION_PINS.json").read_bytes()
    expected_pin = {"bytes": len(pin_raw), "sha256": sha(pin_raw)}
    assert receipt["pre_execution_pins_before"] == receipt["pre_execution_pins_after"] == expected_pin
    for field, file in [("stdout", "stdout.jsonl"), ("stderr", "stderr.txt")]:
        raw = (PILOT / "execution_01" / file).read_bytes()
        assert {"bytes": len(raw), "sha256": sha(raw)} == receipt[field]
    records = [json.loads(line) for line in (PILOT / "execution_01/stdout.jsonl").read_bytes().splitlines()]
    assert records[0]["kind"] == "contract" and records[-2]["kind"] == "runtime" and records[-1]["kind"] == "complete"
    assert set(row["kind"] for row in records) == {"contract", "state", "box", "runtime", "complete"}
    states = [row for row in records if row["kind"] == "state"]
    boxes = [row for row in records if row["kind"] == "box"]
    assert len(states) == 2353 and [row["n"] for row in boxes] == list(range(1, 8))
    for n, size, box in zip(range(1, 8), (1, 3, 10, 35, 126, 462, 1716), boxes):
        rows = [row for row in states if row["n"] == n]
        table = {tuple(row["source"]): row for row in rows}
        assert len(rows) == len(table) == box["states"] == size
        reverse = {key: [] for key in table}
        for source, row in table.items():
            assert row["predecessors"] == row["decoded_predecessors"] == sorted(row["predecessors"])
            assert len(row["predecessors"]) == row["laurent_count"]
            assert row["target_in_image"] == bool(row["predecessors"])
            assert row["height"] == row["predicted_height"]
            assert row["period"] == len(row["cycle"]) == 1
            assert row["terminal"] == row["cycle"][0]
            assert tuple(row["successor"]) in reverse
            reverse[tuple(row["successor"])].append(list(source))
        for target, predecessors in reverse.items():
            assert sorted(predecessors) == table[target]["predecessors"]
        assert box["image"] == sum(bool(row["predecessors"]) for row in rows)
        assert box["inverse_mass"] == sum(row["laurent_count"] for row in rows) == size
        assert box["maximum_height"] == max(row["height"] for row in rows) == box["theorem_height"]
        assert box["fixed"] == box["recurrent"] == sum(row["height"] == 0 for row in rows)
    complete = records[-1]
    totals = {key: sum(box["assertions"][key] for box in boxes) for key in complete["assertions"]}
    assert totals == complete["assertions"] and sum(totals.values()) == complete["assertion_total"] == 14523
    assert complete["total_states"] == 2353 and complete["scientific_producer_invocations"] == 1
    probe_receipt = json.loads((PILOT / "preflight/NATIVE_RECEIPT.json").read_text())
    for field, name in [("stdout", "runtime_probe.stdout.json"), ("stderr", "runtime_probe.stderr.txt")]:
        raw = (PILOT / "preflight" / name).read_bytes()
        assert {"bytes": len(raw), "sha256": sha(raw)} == probe_receipt[field]
    assert probe_receipt["native_exit"] == 0
    probe = json.loads((PILOT / "preflight/runtime_probe.stdout.json").read_text())
    runtime = {}
    for name, row in [("child", records[-2]), ("probe", probe), ("launcher", receipt["launcher_runtime"])]:
        missing = [p["path"] for p in row["file_pins"] if allowed.get(str(Path(p["path"]).resolve())) !=
                   {key: p[key] for key in ("bytes", "sha256")}]
        runtime[name] = {"observed_files": len(row["file_pins"]), "not_prelocked": missing}
    assert runtime["child"] == {"observed_files": 38, "not_prelocked": []}
    assert runtime["probe"] == {"observed_files": 52, "not_prelocked": []}
    assert runtime["launcher"] == {"observed_files": 54, "not_prelocked": [
        "/usr/lib/locale/C.utf8/LC_CTYPE", "/usr/lib/x86_64-linux-gnu/gconv/gconv-modules.cache"]}
    recapture = json.loads((PILOT / "postrun_diagnostic_v2/AUDIT_RECAPTURE_NATIVE_RECEIPT.json").read_text())
    assert recapture["native_exit"] == 1 and not recapture["retrospective_original_receipt"]
    assert recapture["scientific_producer_invocations_in_this_diagnostic"] == 0
    for field in ["stdout", "stderr"]:
        raw = (PILOT / "postrun_diagnostic_v2" / ("audit_recapture." + field + ".txt")).read_bytes()
        assert {"bytes": len(raw), "sha256": sha(raw)} == recapture[field]
    assert recapture["stdout"]["bytes"] == 0 and recapture["stderr"]["bytes"] == 535
    return {"scope": "INDEPENDENT_ARCHIVED_RECORD_CONSISTENCY_ONLY_NO_MODEL_EVALUATION",
            "state_records": len(states), "box_records": len(boxes), "assertions_from_record": totals,
            "assertion_total_from_record": 14523, "input_raw_pairs": 98,
            "science_native_exit_from_original": 0, "scientific_runs_by_gate": 0,
            "scientific_runs_in_original_receipt": 1, "runtime": runtime,
            "strict_observed_runtime_prelock": "FAIL_PRESERVED",
            "strict_reuse_eligible": False, "frozen_audit_recapture_native_exit": 1,
            "bounded_categories_observed_without_counterexample": True,
            "boundary": "No formula, literal successor, or orbit was scientifically recomputed by this checker."}


def pilot_capture():
    dump(BASE / "PILOT_PACKAGE_CHECK.json", checked_manifest(PILOT, "MANIFEST.json"))
    selected = ["HANDOFF.md", "AUTHORIZATION.md", "PRE_EXECUTION_PINS.json", "producer.py",
                "run_pilot.py", "freeze.py", "audit.py", "artifact_closeout.py", "artifact_closeout_v2.py",
                "FAILED_ARTIFACT_ATTEMPTS.md", "execution_01/NATIVE_RECEIPT.json", "execution_01/stdout.jsonl",
                "execution_01/stderr.txt", "postrun_diagnostic_v2/DIAGNOSIS.json",
                "postrun_diagnostic_v2/AUDIT_RECAPTURE_NATIVE_RECEIPT.json",
                "postrun_diagnostic_v2/audit_recapture.stdout.txt",
                "postrun_diagnostic_v2/audit_recapture.stderr.txt"]
    pins = []
    for rel in selected:
        raw = (PILOT / rel).read_bytes()
        target = BASE / "pilot_archive" / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw)
        pins.append({"source": str(PILOT / rel), "snapshot": str(target.relative_to(BASE)),
                     "bytes": len(raw), "sha256": sha(raw), "raw_equal": raw == target.read_bytes()})
    dump(BASE / "PILOT_ARCHIVE_PINS.json", pins)
    native("07_pilot_archive_only", ["/usr/bin/python3.10", "-I", "-S", "-B",
        str(PILOT / "artifact_closeout_v2.py"), "verify"])
    result = archived_pilot_check()
    dump(BASE / "PILOT_ARCHIVED_RECORD_CHECK.json", result)
    print(json.dumps(result))


def audit():
    historical = json.loads((BASE / "HISTORICAL_PINS.json").read_text())
    total = 0
    for group in historical.values():
        for row in group:
            raw = (BASE / row["gate_snapshot"]).read_bytes()
            assert raw == Path(row["source"]).read_bytes()
            if "author_snapshot" in row:
                assert raw == Path(row["author_snapshot"]).read_bytes()
            assert len(raw) == row["bytes"] and sha(raw) == row["sha256"]
            total += 1
    for file, folder, name in [("AUTHOR_PACKAGE_CHECK.json", AUTHOR, "MANIFEST.json"),
                                ("SOURCE_DESK_CHECK.json", SOURCE_DESK, "MANIFEST.sha256")]:
        assert json.loads((BASE / file).read_text()) == checked_manifest(folder, name)
    native_count = 0
    for path in sorted((BASE / "native").glob("*.json")):
        row = json.loads(path.read_text())
        for stream in ["stdout", "stderr"]:
            assert pin(Path(row[stream]["path"])) == row[stream]
        assert isinstance(row["argv"], list) and row["cwd"]
        native_count += 1
    author_native = 0
    for path in sorted((AUTHOR / "native").glob("*.json")):
        row = json.loads(path.read_text())
        assert row["exit_code"] == 0 and row["argv"] and row["cwd"]
        for stream in ["stdout", "stderr"]:
            raw = path.with_suffix("." + stream).read_bytes()
            assert {"bytes": len(raw), "sha256": sha(raw)} == row[stream]
        author_native += 1
    expected_concat = b"".join((BASE / row["gate_snapshot"]).read_bytes()
                               for row in historical["author_historical"])
    assert expected_concat == (AUTHOR / "native/01.stdout").read_bytes()
    if (BASE / "PILOT_PACKAGE_CHECK.json").exists():
        assert json.loads((BASE / "PILOT_PACKAGE_CHECK.json").read_text()) == checked_manifest(PILOT, "MANIFEST.json")
        for row in json.loads((BASE / "PILOT_ARCHIVE_PINS.json").read_text()):
            raw = (BASE / row["snapshot"]).read_bytes()
            assert raw == Path(row["source"]).read_bytes()
            assert len(raw) == row["bytes"] and sha(raw) == row["sha256"]
        assert json.loads((BASE / "PILOT_ARCHIVED_RECORD_CHECK.json").read_text()) == archived_pilot_check()
    print(json.dumps({"audit": "archived_documentation_only", "historical_raw_pairs": total,
                      "gate_native_bindings": native_count,
                      "author_native_bindings": author_native,
                      "author_full_snapshot_concat_raw_equal": True,
                      "scientific_executions_by_gate": 0}))


def seal():
    paths = sorted(path for path in BASE.rglob("*") if path.is_file() and path != BASE / "SHA256SUMS")
    (BASE / "SHA256SUMS").write_text("".join(
        sha(path.read_bytes()) + "  " + str(path.relative_to(BASE)) + "\n" for path in paths))
    print(json.dumps({"files": len(paths), "bytes": sum(p.stat().st_size for p in paths),
                      "manifest": pin(BASE / "SHA256SUMS")}))


if __name__ == "__main__":
    {"historical": historical_capture, "sources": source_capture,
     "pilot": pilot_capture, "audit": audit, "seal": seal}[sys.argv[1]]()
