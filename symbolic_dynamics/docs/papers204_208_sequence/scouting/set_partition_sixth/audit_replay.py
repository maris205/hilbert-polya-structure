#!/usr/bin/env python3
"""Read-only fresh raw replay gate for this negative scout package."""
from hashlib import sha256
from pathlib import Path
import json
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    mapping = [("pilot.py", "CANONICAL.json"),
               ("replacement_pilot.py", "REPLACEMENT_CANONICAL.json"),
               ("proof_checks.py", "PROOF_CHECKS_CANONICAL.json")]
    paths = sorted({name for pair in mapping for name in pair} |
                   {"audit_replay.py", "INTAKE.md", "INPUT_PINS.sha256"})
    before = {name: digest(HERE / name) for name in paths}
    input_pins = []
    for line in (HERE / "INPUT_PINS.sha256").read_text().splitlines():
        expected, relative = line.split("  ", 1)
        actual = digest(ROOT / relative)
        assert expected == actual, relative
        input_pins.append({"path": relative, "sha256": actual})
    receipts = []
    for script, canonical in mapping:
        command = [sys.executable, "-B", str((HERE / script).relative_to(ROOT))]
        children = [subprocess.run(command, cwd=ROOT, capture_output=True) for _ in range(2)]
        expected_bytes = (HERE / canonical).read_bytes()
        receipt = {"script": script, "command": command,
                   "child_exits": [x.returncode for x in children],
                   "stderr_bytes": [len(x.stderr) for x in children],
                   "stdout_bytes": [len(x.stdout) for x in children],
                   "raw_pair_equal": children[0].stdout == children[1].stdout,
                   "canonical_equal": [x.stdout == expected_bytes for x in children],
                   "stdout_sha256": [sha256(x.stdout).hexdigest() for x in children]}
        assert receipt["child_exits"] == [0, 0], receipt
        assert receipt["stderr_bytes"] == [0, 0], receipt
        assert receipt["raw_pair_equal"] and all(receipt["canonical_equal"]), receipt
        output = json.loads(expected_bytes)
        receipt["assertions_per_child"] = output["assertions"]
        receipt["boxes_per_child"] = output["boxes"]
        receipt["states_per_child"] = output["states_across_boxes"]
        receipts.append(receipt)
    after = {name: digest(HERE / name) for name in paths}
    assert before == after
    print(json.dumps({"status": "FRESH_AUTHOR_REPLAY_PASS_NOT_INDEPENDENT_REVIEW",
                      "python": sys.version, "workspace": str(ROOT),
                      "sources_and_canonicals_unchanged": before == after,
                      "dependency_sha256": before, "historical_input_pins": input_pins,
                      "receipts": receipts}, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
