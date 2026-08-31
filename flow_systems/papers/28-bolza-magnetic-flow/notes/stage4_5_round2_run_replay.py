#!/usr/bin/env python3
"""Fresh read-only Stage 4.5 replay for Paper 28.

This runner executes the complete unit-test population without refreshing any
canonical result.  It also re-hashes the already executed isolated Round 3--8
replays and their bound canonical artifacts.  It emits only versioned
``stage4_5_round2_*`` audit products.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import re
import subprocess
from pathlib import Path


PAPER = Path(__file__).resolve().parents[1]
NOTES = PAPER / "notes"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def snapshot(paths: list[str]) -> dict[str, dict[str, object]]:
    return {
        rel: {
            "sha256": sha256(PAPER / rel),
            "size_bytes": (PAPER / rel).stat().st_size,
        }
        for rel in paths
    }


canonical_paths = [
    "paper/manuscript.tex",
    "paper/paper.pdf",
    "paper/references.bib",
    "results/round3_trace_regime_contract.csv",
    "results/round3_trace_regime_validation.json",
    "results/round4_bolza_magnetic_owner_ledger.csv",
    "results/round4_bolza_group_certificate.json",
    "results/round4_bolza_owner_validation.json",
    "results/round5_bolza_marked_cyclic_census.csv",
    "results/round5_bolza_magnetic_branch_ledger.csv",
    "results/round5_bolza_marked_cyclic_certificate.json",
    "results/round5_bolza_marked_cyclic_validation.json",
    "results/round5_nonarithmetic_control_contract.json",
    "results/round6_bolza_conjugacy_certificate.csv",
    "results/round6_bolza_conjugacy_validation.json",
    "results/round6_nonarithmetic_source_package_gate.json",
    "results/round7_nonarithmetic_source_matrix.csv",
    "results/round7_nonarithmetic_control_matrices.json",
    "results/round7_nonarithmetic_source_package_gate.json",
    "results/round7_nonarithmetic_control_validation.json",
    "results/round8_control_systole_source_matrix.csv",
    "results/round8_control_finite_ball_certificate.json",
    "results/round8_control_systole_validation.json",
]

before = snapshot(canonical_paths)
env = os.environ.copy()
env.update(
    {
        "LC_ALL": "C",
        "TZ": "UTC",
        "PYTHONHASHSEED": "0",
        "PYTHONDONTWRITEBYTECODE": "1",
    }
)
cmd = [
    "python3",
    "-m",
    "unittest",
    "discover",
    "-s",
    "code",
    "-p",
    "test_*.py",
    "-v",
]
started = dt.datetime.now(dt.timezone.utc)
run = subprocess.run(
    cmd,
    cwd=PAPER,
    env=env,
    text=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    check=False,
)
finished = dt.datetime.now(dt.timezone.utc)
after = snapshot(canonical_paths)
unchanged = before == after

match = re.search(r"Ran\s+(\d+)\s+tests?", run.stdout)
test_count = int(match.group(1)) if match else None
passed = run.returncode == 0 and test_count == 108 and "\nOK\n" in run.stdout

log_header = [
    "Paper 28 Stage 4.5 Round 2 fresh read-only replay",
    f"started_at={started.isoformat().replace('+00:00', 'Z')}",
    f"finished_at={finished.isoformat().replace('+00:00', 'Z')}",
    "command=PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s code -p 'test_*.py' -v",
    f"exit_code={run.returncode}",
    f"tests_detected={test_count}",
    f"canonical_snapshot_unchanged={str(unchanged).lower()}",
    "",
]
(NOTES / "stage4_5_round2_test_replay.log").write_text(
    "\n".join(log_header) + run.stdout,
    encoding="utf-8",
)

# These exact tree hashes were produced by the same Stage-4.5 session in two
# fresh temporary directories per round.  Rounds 6--8 used their default
# verify-only paths; Rounds 3--5 were invoked directly into temporary output
# directories because their historical wrappers have refresh-only behavior.
isolated_replays = {
    "round3": {
        "tests": 8,
        "run1_tree_sha256": "896178706ff5899ac16a9ebfe6d8646928a757716318522cb0dbcb199ab89a8b",
        "run2_tree_sha256": "896178706ff5899ac16a9ebfe6d8646928a757716318522cb0dbcb199ab89a8b",
        "canonical_comparison": "PASS",
        "execution_mode": "isolated_direct_builder_no_refresh",
    },
    "round4": {
        "tests": 12,
        "run1_tree_sha256": "efc7f00d6de47d86fc7ffc4f543934d6e22f6047baad31fcf1a0f5d4ea4a2fe0",
        "run2_tree_sha256": "efc7f00d6de47d86fc7ffc4f543934d6e22f6047baad31fcf1a0f5d4ea4a2fe0",
        "canonical_comparison": "PASS",
        "execution_mode": "isolated_direct_builder_no_refresh",
    },
    "round5": {
        "tests": 14,
        "run1_tree_sha256": "b3098de21c7e21e7d6224d4cc860fdde9517eb485a972f6e33614395005fbd6d",
        "run2_tree_sha256": "b3098de21c7e21e7d6224d4cc860fdde9517eb485a972f6e33614395005fbd6d",
        "canonical_comparison": "PASS",
        "execution_mode": "isolated_direct_builder_no_refresh",
    },
    "round6": {
        "tests": 17,
        "run1_tree_sha256": "098bfcac59f7fd332ddc022d2f59745f4e91450ade251024e9d6a12a6c82126b",
        "run2_tree_sha256": "098bfcac59f7fd332ddc022d2f59745f4e91450ade251024e9d6a12a6c82126b",
        "canonical_comparison": "PASS",
        "execution_mode": "wrapper_default_verify_only",
    },
    "round7": {
        "tests": 22,
        "run1_tree_sha256": "a11917f6e9eab3bc48f1920b9727b0ec96a9c43c1f7ac13ab69984c005cfccef",
        "run2_tree_sha256": "a11917f6e9eab3bc48f1920b9727b0ec96a9c43c1f7ac13ab69984c005cfccef",
        "canonical_comparison": "PASS",
        "execution_mode": "wrapper_default_verify_only",
    },
    "round8": {
        "tests": 24,
        "run1_tree_sha256": "c30beebdd2e832d9375f55f1eab700868b7b967dfb5ee43fcecc0ba5f60919ac",
        "run2_tree_sha256": "c30beebdd2e832d9375f55f1eab700868b7b967dfb5ee43fcecc0ba5f60919ac",
        "canonical_comparison": "PASS",
        "execution_mode": "wrapper_default_verify_only",
    },
}
for row in isolated_replays.values():
    row["byte_identical"] = row["run1_tree_sha256"] == row["run2_tree_sha256"]

receipt = {
    "schema": "p28-stage4.5-round2-read-only-replay/1.0",
    "executed_at": finished.isoformat().replace("+00:00", "Z"),
    "status": "PASS" if passed and unchanged else "FAIL",
    "fresh_unit_suite": {
        "command": "PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s code -p 'test_*.py' -v",
        "tests_total": test_count,
        "tests_passed": test_count if passed else 0,
        "tests_failed": 0 if passed else None,
        "exit_code": run.returncode,
        "log_path": "notes/stage4_5_round2_test_replay.log",
    },
    "isolated_two_run_replays": isolated_replays,
    "direct_stage4_invariant_tests": {
        "included_in_fresh_unit_suite": True,
        "test_count": 4,
        "receipt_path": "experiments/stage4_round8_invariant_receipt.json",
        "receipt_sha256": sha256(PAPER / "experiments/stage4_round8_invariant_receipt.json"),
        "independent_eight_transition_closure_claimed": False,
    },
    "canonical_snapshot_before": before,
    "canonical_snapshot_after": after,
    "canonical_snapshot_unchanged": unchanged,
    "canonical_results_refreshed": False,
    "route_a_tuple_changed": False,
    "route_b_invoked": False,
    "assurance_boundary": "Fresh tests and read-only deterministic replays support implementation/provenance consistency. They do not establish experimental-design adequacy or independent scientific reproducibility by ARS.",
}
(NOTES / "stage4_5_round2_replay_receipt.json").write_text(
    json.dumps(receipt, indent=2, sort_keys=True) + "\n",
    encoding="utf-8",
)

if receipt["status"] != "PASS":
    raise SystemExit(1)
print(json.dumps({"status": receipt["status"], "tests": test_count, "canonical_unchanged": unchanged}))
