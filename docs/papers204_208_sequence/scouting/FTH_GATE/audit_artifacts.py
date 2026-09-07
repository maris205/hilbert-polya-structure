"""Read-only array/provenance reconciliation; no feedback kernel executions.

This maps recorded coordinate arrays to recorded indices. It is archival
reconciliation, not a third scientific replay and not author-code import.
"""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[3]
AUTHOR = BASE.parent / "finite_systems_nineteenth"
checks = []


def require(condition, label):
    checks.append({"label": label, "pass": bool(condition)})
    if not condition:
        raise AssertionError(label)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def by_parameter(path, rule):
    rows = [json.loads(line) for line in path.read_text().splitlines()]
    return {row["parameter"]: row for row in rows if row.get("rule") == rule}


def normalized_cycles(cycles):
    result = []
    for cycle in cycles:
        start = min(range(len(cycle)), key=cycle.__getitem__)
        result.append(tuple(cycle[start:] + cycle[:start]))
    return sorted(result)


before_paths = [BASE / "CANONICAL.json", BASE / "record_pair.py", BASE / "bootstrap.py",
                BASE / "pre_author_code/kernel_v0.py", Path(__file__).resolve()]
before_paths += [p for folder in [BASE / "replay_01", BASE / "replay_02", BASE / "comparison"]
                 for p in folder.rglob("*") if p.is_file()]
before_paths += [AUTHOR / name / "producer.stdout" for name in
                 ["execution_01", "execution_02", "proof_execution_01", "proof_execution_02"]]
before = {str(p): sha(p) for p in before_paths}
canonical = read(BASE / "CANONICAL.json")
require(canonical["boxes"] == list(range(6)), "exact_original_boxes")
require(canonical["total_states"] == canonical["total_decoded_sources"] == 3414, "all_source_mass_3414")
summary = []
for row in canonical["rows"]:
    n = row["n"]
    entries = row["complete_transitions_sources_geometry_and_inverse_codes"]
    state_tuples = [tuple(entry["state"]) for entry in entries]
    require(state_tuples == sorted(set(state_tuples)), [n, "unique_lexicographic_states"])
    require(len(entries) == row["state_count"] == (n ** n if n else 1), [n, "full_array_length"])
    index = {state: i for i, state in enumerate(state_tuples)}
    transitions = [index[tuple(entry["transition"])] for entry in entries]
    predecessor_indices = [[index[tuple(f)] for f in entry["predecessors"]] for entry in entries]
    depths = [entry["entrance_depth"] for entry in entries]
    periods = [entry["eventual_period"] for entry in entries]
    predictions = [entry["recurrent_predicted_period"] or 0 for entry in entries]
    counts = list(map(len, predecessor_indices))
    cycles = normalized_cycles([[index[tuple(state)] for state in cycle]
                                for cycle in row["complete_whole_function_cycles"]])
    for run in ["execution_01", "execution_02"]:
        old = by_parameter(AUTHOR / run / "producer.stdout", "FTH")[n]
        require(transitions == old["transition"], [n, run, "all_transitions"])
        original_reverse = [[] for _ in entries]
        for source, target in enumerate(old["transition"]):
            original_reverse[target].append(source)
        require(predecessor_indices == original_reverse, [n, run, "all_original_source_sets"])
        require(depths == old["depths"], [n, run, "all_depths"])
        require(counts == old["indegrees"], [n, run, "all_fibre_sizes"])
        require(cycles == normalized_cycles(old["cycle_state_indices"]), [n, run, "all_function_cycles"])
        require(row["all_maximizers"] == old["max_fibre_targets"], [n, run, "all_maximizers"])
    for run in ["proof_execution_01", "proof_execution_02"]:
        old = by_parameter(AUTHOR / run / "producer.stdout", "FTH_PROOF_CHECK")[n]
        require(transitions == old["transition"], [n, run, "all_transitions"])
        require(depths == old["depths"] and periods == old["periods"], [n, run, "all_depths_periods"])
        require(predictions == old["predicted_recurrent_periods"], [n, run, "all_recurrent_predictions"])
        require(counts == old["inverse_counts"], [n, run, "all_fibre_sizes"])
        require(row["all_maximizers"] == old["maximizing_targets"], [n, run, "all_maximizers"])
    summary.append({key: row[key] for key in ["n", "state_count", "recurrent_state_count",
                   "maximum_one_step_fibre", "all_maximizers", "observed_maximum_entrance_depth_not_all_size_theorem"]})
for run in ["replay_01", "replay_02"]:
    folder = BASE / run
    require(read(folder / "science.before.json") == read(folder / "science.after.json"), [run, "science_pins_equal"])
    require(read(folder / "runtime.before.json") == read(folder / "runtime.after.json"), [run, "runtime_pins_equal"])
    require(read(folder / "ldd.bootstrap.before.json") == read(folder / "ldd.bootstrap.after.json"), [run, "ldd_bootstrap_equal"])
    receipt = read(folder / "RECEIPT.json")
    require(receipt["status"] == "PASS" and not receipt["uncovered"] and not receipt["consumed_bytecode"], [run, "coverage_no_bytecode"])
    links = read(folder / "ldd.index.json")["links"]
    for link in links:
        command = read(folder / "ldd" / link["receipt"])
        require(command["exit"] == 0, [run, "actual_ldd_exit", link["target"]])
    runtime = read(folder / "runtime.before.json")
    for name in ["/usr/bin/ldd", "/bin/bash", "/bin/sh", sys.executable, "/usr/bin/cmp"]:
        require(str(Path(name).resolve()) in runtime, [run, "explicit_runtime_tool", name])
    require(sha(folder / "source_inputs/kernel_v0.py") == "d172db91901a2d087ed96cadb8e6a38690330cce414b117f07a0e769910c5107", [run, "pre_author_kernel_unchanged"])
    require(sha(folder / "producer.stdout") == sha(BASE / "CANONICAL.json"), [run, "canonical_hash"])
process = subprocess.run(["/usr/bin/sha256sum", "-c", str(BASE / "INPUT_PINS.sha256")], cwd=ROOT, capture_output=True, check=False)
(BASE / "final_input_pin_check.stdout").write_bytes(process.stdout)
(BASE / "final_input_pin_check.stderr").write_bytes(process.stderr)
require(process.returncode == 0, "all_164_original_inputs_still_pinned")
after = {str(p): sha(p) for p in before_paths}
require(before == after, "audited_artifacts_unchanged")
report = {"kind": "ARCHIVAL_ARRAY_AND_PROVENANCE_RECONCILIATION_ZERO_NEW_KERNEL_RUNS", "status": "PASS",
          "argv": sys.argv, "flags": str(sys.flags), "finished_epoch": time.time(),
          "before": before, "after": after, "checks": checks, "check_count": len(checks),
          "canonical_summary": summary, "independent_scientific_checks_per_run": canonical["checks"],
          "ldd_commands_per_run": len(read(BASE / "replay_01/ldd.index.json")["links"]),
          "final_input_pin_check_exit": process.returncode}
(BASE / "ARTIFACT_AUDIT.json").write_text(json.dumps(report, sort_keys=True, indent=2) + "\n")
print(json.dumps({key: report[key] for key in ["kind", "status", "check_count", "canonical_summary",
                   "independent_scientific_checks_per_run", "ldd_commands_per_run", "final_input_pin_check_exit"]}, sort_keys=True))
