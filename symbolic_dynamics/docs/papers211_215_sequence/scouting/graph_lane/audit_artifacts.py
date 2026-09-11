#!/usr/bin/env python3
"""Read-only audit of recorded CBF evidence; does not execute any map."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CHECKS = 0


def check(value):
    global CHECKS
    CHECKS += 1
    if not value:
        raise AssertionError(CHECKS)


def main():
    receipt = json.loads((HERE / "execution_01/receipt.json").read_bytes())
    check(receipt["returncode"] == 0)
    check(receipt["seconds"] < 60)
    check(receipt["inputs_before"] == receipt["inputs_after"])
    check(receipt["input_pins_unchanged"] is True)
    for item in receipt["inputs_before"] + [receipt["stdout"], receipt["stderr"]]:
        data = Path(item["path"]).read_bytes()
        check(len(data) == item["bytes"])
        check(hashlib.sha256(data).hexdigest() == item["sha256"])
    check((HERE / "execution_01/stderr.txt").read_bytes() == b"")
    oldpins = 0
    for line in (HERE / "INPUTS.sha256").read_text().splitlines():
        digest, path = line.split("  ", 1)
        check(hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest)
        oldpins += 1
    raw = (HERE / "execution_01/stdout.jsonl").read_bytes()
    rows = [json.loads(line) for line in raw.splitlines()]
    counts = [0] * 7
    boxes = []
    completion = []
    for row in rows:
        if row["kind"] == "state":
            n = row["n"]
            check(0 <= n <= 6)
            size = 1 << (n * (n - 1) // 2)
            check(row["source"] == counts[n])
            check(0 <= row["next"] < size)
            check(row["depth"] >= 0 and row["period"] >= 1 and row["indegree"] >= 0)
            counts[n] += 1
        elif row["kind"] == "box":
            check(row["n"] == len(boxes))
            boxes.append(row)
        elif row["kind"] == "complete":
            completion.append(row)
        else:
            raise AssertionError("unknown record type")
    check(counts == [1, 1, 2, 8, 64, 1024, 32768])
    check(len(boxes) == 7 and len(completion) == 1)
    check(completion[0]["states"] == sum(counts) == 33868)
    check(completion[0]["checks"] == 270731)
    check(len(rows) == 33876)
    print(json.dumps({"status": "PASS_RECORDED_ARTIFACTS_ONLY", "checks": CHECKS,
                      "old_input_pins": oldpins, "raw_records": len(rows),
                      "state_records": sum(counts), "stdout_bytes": len(raw),
                      "stdout_sha256": hashlib.sha256(raw).hexdigest(),
                      "new_scientific_executions": 0}, sort_keys=True))


if __name__ == "__main__":
    main()
