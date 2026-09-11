#!/usr/bin/env python3
"""Read-only audit of archived executions; does not rerun scientific code."""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess

BASE = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    comparisons = []
    inspected = []
    for prefix in ("execution", "tree_execution", "ofs_theorem_execution"):
        for serial in (1, 2):
            folder = BASE/(prefix+"_"+str(serial).zfill(2))
            record = json.loads((folder/"RECORD.json").read_text())
            stdout = folder/"stdout.json"
            stderr = folder/"stderr.txt"
            assert record["child_exit"] == 0
            assert record["stderr_bytes"] == len(stderr.read_bytes()) == 0
            assert record["stdout_bytes"] == len(stdout.read_bytes())
            assert record["stdout_sha256"] == digest(stdout)
            assert record["inputs_unchanged"]
            assert record["before_inputs"] == record["after_inputs"]
            for name, expected in record["before_inputs"].items():
                assert digest(folder/name) == expected
                assert digest(BASE/name) == expected
            result = json.loads(stdout.read_text())
            inspected.append({"folder": folder.name,
                              "archived_started_utc": record["started_utc"],
                              "archived_ended_utc": record["ended_utc"],
                              "assertions": result["assertions"],
                              "stdout_sha256": digest(stdout),
                              "stdout_bytes": len(stdout.read_bytes()),
                              "input_pins_checked": len(record["before_inputs"]),
                              "frozen_and_live_inputs_match": True})
        command = ["cmp", str(BASE/(prefix+"_01/stdout.json")),
                   str(BASE/(prefix+"_02/stdout.json"))]
        start = datetime.datetime.now(datetime.timezone.utc).isoformat()
        child = subprocess.run(command, capture_output=True)
        end = datetime.datetime.now(datetime.timezone.utc).isoformat()
        assert child.returncode == 0 and not child.stdout and not child.stderr
        comparisons.append({"command": command, "started_utc": start,
                            "ended_utc": end, "exit": child.returncode,
                            "stdout": child.stdout.decode(), "stderr": child.stderr.decode()})
    print(json.dumps({"role": "archived_process_pin_audit_and_fresh_byte_comparisons_only",
                      "fresh_scientific_execution": False,
                      "inspected_archives": inspected,
                      "actual_raw_comparisons": comparisons,
                      "status": "PASS"}, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
