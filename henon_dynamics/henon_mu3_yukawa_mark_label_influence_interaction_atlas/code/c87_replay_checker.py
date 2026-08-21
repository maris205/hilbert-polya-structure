#!/usr/bin/env python3
"""Clean-process deterministic replay for C87."""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from hashlib import sha256
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c87_label_influence_interaction_atlas_evidence.json"
PRODUCER = PROJECT / "code/c87_label_influence_interaction_atlas.py"
CHECKER = PROJECT / "code/c87_label_influence_interaction_atlas_checker.py"
SYMPY = PROJECT / "code/c87_sympy_crosscheck.py"


def run(command: list[str]) -> dict[str, object]:
    environment = {**os.environ, "PYTHONHASHSEED": "0", "LC_ALL": "C"}
    result = subprocess.run(
        command,
        cwd=PROJECT,
        env=environment,
        capture_output=True,
        text=True,
        check=True,
    )
    return json.loads(result.stdout.strip().splitlines()[-1])


def main() -> None:
    before = EVIDENCE.read_bytes()
    before_hash = sha256(before).hexdigest()
    with tempfile.TemporaryDirectory(prefix="c87-replay-") as directory:
        replay = Path(directory) / "evidence.json"
        producer = run([sys.executable, str(PRODUCER), "--output", str(replay)])
        assert producer["status"] == "PREFREEZE_G3_PASS"
        assert replay.read_bytes() == before
    checker = run([sys.executable, str(CHECKER)])
    symbolic = run([sys.executable, str(SYMPY)])
    assert checker["status"] == "C87_INDEPENDENT_CHECK_PASS"
    assert symbolic["status"] == "C87_SYMPY_FINITE_CROSSCHECK_PASS"
    after_hash = sha256(EVIDENCE.read_bytes()).hexdigest()
    assert before_hash == after_hash
    print(json.dumps({
        "status": "C87_REPLAY_PASS",
        "evidence_sha256": after_hash,
        "producer_byte_identical": True,
        "independent_checker": checker["status"],
        "symbolic_crosscheck": symbolic["status"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
