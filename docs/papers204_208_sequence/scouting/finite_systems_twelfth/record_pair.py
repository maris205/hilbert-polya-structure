"""Record two actual isolated producer runs; never overwrite an output path."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys
import time

BASE = Path(__file__).resolve().parent
INPUTS = (BASE / "INTAKE.md", BASE / "pilot.py", BASE / "record_pair.py")


def pins():
    return {str(path): hashlib.sha256(path.read_bytes()).hexdigest() for path in INPUTS}


def save(path, value):
    with path.open("xb") as handle:
        handle.write(value)


def main():
    target = BASE / "execution_pair_v1"
    target.mkdir(exist_ok=False)
    before = pins()
    save(target / "input_pins_before.json", json.dumps(before, sort_keys=True, indent=2).encode() + b"\n")
    records = []
    outputs = []
    for idx in (1, 2):
        run = target / f"run{idx}"
        run.mkdir(exist_ok=False)
        command = [sys.executable, "-I", "-B", str(BASE / "pilot.py")]
        probe_command = [sys.executable, "-I", "-B", "-c",
                         "import json,sys; print(json.dumps({'version':sys.version,'executable':sys.executable,'isolated':sys.flags.isolated,'dont_write_bytecode':sys.dont_write_bytecode,'optimize':sys.flags.optimize,'path':sys.path},sort_keys=True))"]
        probe = subprocess.run(probe_command, cwd=run, capture_output=True)
        save(run / "runtime_probe.stdout", probe.stdout)
        save(run / "runtime_probe.stderr", probe.stderr)
        start = time.time()
        child = subprocess.run(command, cwd=run, capture_output=True)
        elapsed = time.time() - start
        save(run / "producer.stdout", child.stdout)
        save(run / "producer.stderr", child.stderr)
        record = dict(command=command, cwd=str(run), returncode=child.returncode,
                      runtime_probe_command=probe_command, runtime_probe_returncode=probe.returncode,
                      started_unix=start, elapsed_seconds=elapsed,
                      stdout_sha256=hashlib.sha256(child.stdout).hexdigest(),
                      stderr_sha256=hashlib.sha256(child.stderr).hexdigest(),
                      input_pins_after=pins())
        save(run / "receipt.json", json.dumps(record, sort_keys=True, indent=2).encode() + b"\n")
        records.append(record)
        outputs.append(child.stdout)
        if probe.returncode or child.returncode or pins() != before:
            save(target / "FAILED.json", json.dumps(records, sort_keys=True, indent=2).encode() + b"\n")
            raise SystemExit(1)
    # A distinct actual comparator process, not a claimed textual comparison.
    cmp_command = ["cmp", "--", str(target / "run1/producer.stdout"), str(target / "run2/producer.stdout")]
    compared = subprocess.run(cmp_command, cwd=target, capture_output=True)
    save(target / "cmp.stdout", compared.stdout)
    save(target / "cmp.stderr", compared.stderr)
    after = pins()
    save(target / "input_pins_after.json", json.dumps(after, sort_keys=True, indent=2).encode() + b"\n")
    valid = compared.returncode == 0 and outputs[0] == outputs[1] and after == before
    result = dict(schema="twelfth-actual-pair-v1", passed=valid,
                  producer_returncodes=[x["returncode"] for x in records],
                  comparator_command=cmp_command, comparator_returncode=compared.returncode,
                  complete_raw_stdout_equal=outputs[0] == outputs[1], unchanged_inputs=after == before,
                  assertion_counts=[json.loads(output)["assertions"] for output in outputs])
    save(target / "PAIR_RECEIPT.json", json.dumps(result, sort_keys=True, indent=2).encode() + b"\n")
    print(json.dumps(result, sort_keys=True, indent=2))
    if not valid:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
