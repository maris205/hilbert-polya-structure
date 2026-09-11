"""Read existing native pilot output and locks; never rerun scientific code."""
import hashlib
import json
from pathlib import Path
import sys

BASE = Path(__file__).resolve().parent
if BASE.name == "lock":
    BASE = BASE.parent
DESK = BASE.with_name("finite_semigroup_lane")


def digest(path):
    raw = Path(path).read_bytes()
    return {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}


def expected(row):
    return {key: row[key] for key in ("bytes", "sha256")}


def check_manifest(directory):
    target = directory / "MANIFEST.json"
    data = json.loads(target.read_text())
    actual = {str(path.relative_to(directory)) for path in directory.rglob("*")
              if path.is_file() and path != target}
    if actual != {row["path"] for row in data["files"]}:
        raise AssertionError(("manifest inventory", str(directory)))
    for row in data["files"]:
        if digest(directory / row["path"]) != expected(row):
            raise AssertionError(("manifest bytes", row["path"]))
    return len(actual)


def audit():
    desk_payloads = check_manifest(DESK)
    frozen_desk_payloads = check_manifest(BASE / "lock" / "desk")
    pins_file = BASE / "PRE_EXECUTION_PINS.json"
    locked = json.loads(pins_file.read_text())
    allowed_runtime = {}
    for row in locked["rows"]:
        pin = expected(row)
        if digest(row["origin"]) != pin or digest(BASE / row["frozen"]) != pin:
            raise AssertionError(("locked input mismatch", row["origin"]))
        allowed_runtime[str(Path(row["origin"]).resolve())] = pin
        allowed_runtime[str((BASE / row["frozen"]).resolve())] = pin
    preflight = BASE / "preflight"
    probe_receipt = json.loads((preflight / "NATIVE_RECEIPT.json").read_text())
    if probe_receipt["native_exit"] != 0:
        raise AssertionError("preflight failed")
    if digest(preflight / "runtime_probe.stdout.json") != probe_receipt["stdout"]:
        raise AssertionError("preflight stdout")
    if digest(preflight / "runtime_probe.stderr.txt") != probe_receipt["stderr"]:
        raise AssertionError("preflight stderr")
    output = BASE / "execution_01"
    receipt = json.loads((output / "NATIVE_RECEIPT.json").read_text())
    if receipt["native_exit"] != 0 or receipt["timed_out"] or receipt["launch_error"] is not None:
        raise AssertionError("pilot native failure")
    if receipt["scientific_producer_invocations"] != 1:
        raise AssertionError("wrong producer invocation count")
    if receipt["pre_execution_pins_before"] != digest(pins_file) or receipt["pre_execution_pins_after"] != digest(pins_file):
        raise AssertionError("pre-execution binding changed")
    if receipt["input_pins_before"] != receipt["input_pins_after"]:
        raise AssertionError("native pre/post mismatch")
    for before, row in zip(receipt["input_pins_before"], locked["rows"]):
        if before["origin"] != row["origin"] or before["frozen"] != row["frozen"]:
            raise AssertionError("native input row identity")
        if before["origin_pin"] != expected(row) or before["frozen_pin"] != expected(row):
            raise AssertionError("native input pin mismatch")
    if len(receipt["input_pins_before"]) != len(locked["rows"]):
        raise AssertionError("native input count")
    for name, file in (("stdout", "stdout.jsonl"), ("stderr", "stderr.txt")):
        if digest(output / file) != receipt[name]:
            raise AssertionError(("raw native stream", name))
    records = [json.loads(line) for line in (output / "stdout.jsonl").read_bytes().splitlines()]
    kinds = [record["kind"] for record in records]
    if kinds.count("contract") != 1 or kinds.count("runtime") != 1 or kinds.count("complete") != 1:
        raise AssertionError("missing or duplicate canonical markers")
    if kinds[0] != "contract" or kinds[-2:] != ["runtime", "complete"]:
        raise AssertionError("canonical record order")
    boxes = [record for record in records if record["kind"] == "box"]
    states = [record for record in records if record["kind"] == "state"]
    if [record["n"] for record in boxes] != list(range(1, 8)) or len(states) != 2353:
        raise AssertionError("canonical declared scope")
    sizes = [1, 3, 10, 35, 126, 462, 1716]
    for n, size, summary in zip(range(1, 8), sizes, boxes):
        rows = [record for record in states if record["n"] == n]
        if summary["states"] != size or len(rows) != size:
            raise AssertionError(("canonical box population", n))
        targets = {tuple(record["source"]): record for record in rows}
        if len(targets) != size:
            raise AssertionError(("duplicate canonical source", n))
        for record in rows:
            for key in ("predecessors", "decoded_predecessors"):
                if record[key] != sorted(record[key]):
                    raise AssertionError(("noncanonical predecessor order", n))
            if record["predecessors"] != record["decoded_predecessors"]:
                raise AssertionError(("recorded representation disagreement", n))
        recorded_reverse = {key: [] for key in targets}
        for source, record in targets.items():
            target = tuple(record["successor"])
            if target not in recorded_reverse:
                raise AssertionError(("recorded successor outside carrier", n))
            recorded_reverse[target].append(list(source))
        for target, predecessors in recorded_reverse.items():
            if sorted(predecessors) != targets[target]["predecessors"]:
                raise AssertionError(("recorded full reverse-edge binding", n))
    runtime = next(record for record in records if record["kind"] == "runtime")
    for observation in (runtime, receipt["launcher_runtime"]):
        for pin in observation["file_pins"]:
            path = str(Path(pin["path"]).resolve())
            if allowed_runtime.get(path) != expected(pin):
                raise AssertionError(("unfrozen observed runtime file", path))
    complete = records[-1]
    if complete["total_states"] != 2353 or complete["scientific_producer_invocations"] != 1:
        raise AssertionError("completion scope")
    totals = {key: sum(box["assertions"][key] for box in boxes) for key in complete["assertions"]}
    if totals != complete["assertions"] or sum(totals.values()) != complete["assertion_total"]:
        raise AssertionError("assertion census aggregation")
    print(json.dumps({"scope": "read_only_artifact_audit_no_new_science_or_review",
                      "desk_payloads": desk_payloads,
                      "frozen_desk_payloads": frozen_desk_payloads,
                      "physical_lock_rows": len(locked["rows"]),
                      "state_records": len(states), "box_records": len(boxes),
                      "assertion_total_from_native": complete["assertion_total"],
                      "runtime_files_child": len(runtime["file_pins"]),
                      "native_streams_bound": 4, "scientific_runs": 1}, sort_keys=True))


def seal():
    target = BASE / "MANIFEST.json"
    if target.exists():
        raise FileExistsError(target)
    rows = [{"path": str(path.relative_to(BASE)), **digest(path)}
            for path in sorted(BASE.rglob("*")) if path.is_file() and path != target]
    target.write_text(json.dumps({"self_excluded": "MANIFEST.json", "files": rows},
                                 sort_keys=True, indent=2) + "\n")
    print(json.dumps({"payloads": len(rows), "bytes": sum(row["bytes"] for row in rows)}, sort_keys=True))


def verify():
    count = check_manifest(BASE)
    audit()
    print(json.dumps({"complete_nonself_payloads": count, "manifest_ok": True}, sort_keys=True))


if __name__ == "__main__":
    {"audit": audit, "seal": seal, "verify": verify}[sys.argv[1]]()
