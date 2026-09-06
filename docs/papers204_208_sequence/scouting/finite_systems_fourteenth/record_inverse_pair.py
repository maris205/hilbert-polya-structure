"""Exclusive new inverse-check pair; same disclosed recorder design as record_pair."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import time

BASE = Path(__file__).resolve().parent
INPUTS = tuple(BASE / path for path in (
    "INTAKE.md", "pilot.py", "record_pair.py", "PROOF_AND_DISPOSITION.md",
    "execution_pair_v1/run1/producer.stdout", "execution_pair_v1/run2/producer.stdout",
    "execution_pair_v1/PAIR_RECEIPT.json", "inverse_check.py", "record_inverse_pair.py"))


def pins():
    return {str(path): hashlib.sha256(path.read_bytes()).hexdigest() for path in INPUTS}


def save(path, value):
    with path.open("xb") as handle:
        handle.write(value)


def main():
    target = BASE / "inverse_pair_v1"
    target.mkdir(exist_ok=False)
    before = pins()
    save(target / "input_pins_before.json", json.dumps(before, sort_keys=True, indent=2).encode() + b"\n")
    records, outputs = [], []
    for idx in (1, 2):
        run = target / f"run{idx}"
        run.mkdir(exist_ok=False)
        command = [sys.executable, "-I", "-B", str(BASE / "inverse_check.py")]
        probe_command = [sys.executable, "-I", "-B", "-c",
                         "import json,sys; print(json.dumps({'version':sys.version,'executable':sys.executable,'isolated':sys.flags.isolated,'dont_write_bytecode':sys.dont_write_bytecode,'optimize':sys.flags.optimize,'path':sys.path},sort_keys=True))"]
        probe = subprocess.run(probe_command, cwd=run, capture_output=True)
        save(run / "runtime_probe.stdout", probe.stdout)
        save(run / "runtime_probe.stderr", probe.stderr)
        started = time.time()
        child = subprocess.run(command, cwd=run, capture_output=True)
        elapsed = time.time() - started
        save(run / "producer.stdout", child.stdout)
        save(run / "producer.stderr", child.stderr)
        receipt = dict(command=command, cwd=str(run), returncode=child.returncode,
                       runtime_probe_command=probe_command, runtime_probe_returncode=probe.returncode,
                       started_unix=started, elapsed_seconds=elapsed,
                       stdout_sha256=hashlib.sha256(child.stdout).hexdigest(),
                       stderr_sha256=hashlib.sha256(child.stderr).hexdigest(), input_pins_after=pins())
        save(run / "receipt.json", json.dumps(receipt, sort_keys=True, indent=2).encode() + b"\n")
        records.append(receipt)
        outputs.append(child.stdout)
        if probe.returncode or child.returncode or pins() != before:
            save(target / "FAILED.json", json.dumps(records, sort_keys=True, indent=2).encode() + b"\n")
            raise SystemExit(1)
    command = ["cmp", "--", str(target / "run1/producer.stdout"), str(target / "run2/producer.stdout")]
    comparison = subprocess.run(command, cwd=target, capture_output=True)
    save(target / "cmp.stdout", comparison.stdout)
    save(target / "cmp.stderr", comparison.stderr)
    after = pins()
    save(target / "input_pins_after.json", json.dumps(after, sort_keys=True, indent=2).encode() + b"\n")
    passed = comparison.returncode == 0 and outputs[0] == outputs[1] and before == after
    result = dict(schema="fourteenth-inverse-actual-pair-v1", passed=passed,
                  producer_returncodes=[x["returncode"] for x in records],
                  comparator_command=command, comparator_returncode=comparison.returncode,
                  complete_raw_stdout_equal=outputs[0] == outputs[1], unchanged_inputs=before == after,
                  assertion_counts=[json.loads(raw)["assertions"] for raw in outputs])
    save(target / "PAIR_RECEIPT.json", json.dumps(result, sort_keys=True, indent=2).encode() + b"\n")
    print(json.dumps(result, sort_keys=True, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
