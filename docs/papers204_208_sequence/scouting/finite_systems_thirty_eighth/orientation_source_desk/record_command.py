"""Documentary subprocess recorder; no candidate dynamics or verifier."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import time

ROOT = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument("label")
parser.add_argument("--input", action="append", default=[])
parser.add_argument("argv", nargs=argparse.REMAINDER)
args = parser.parse_args()
argv = args.argv[1:] if args.argv[:1] == ["--"] else args.argv
if not argv or not args.label.replace("_", "").isalnum():
    parser.error("safe label and native argv required")
record = ROOT / "commands" / args.label
record.mkdir(parents=True, exist_ok=False)

def pin(path):
    path = Path(path).resolve(strict=True)
    return {"path": str(path), "sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "bytes": path.stat().st_size}

inputs = [pin(p) for p in args.input]
exe = shutil.which(argv[0])
metadata = {"argv": argv, "cwd": str(ROOT), "inputs_before": inputs,
            "executable": pin(exe), "recorder": pin(__file__), "start_utc_epoch": time.time()}
(record / "invocation.json").write_text(json.dumps(metadata, indent=2) + "\n")
with (record / "stdout.bin").open("xb") as out, (record / "stderr.bin").open("xb") as err:
    completed = subprocess.run(argv, cwd=ROOT, stdout=out, stderr=err, check=False)
metadata.update({"exit_code": completed.returncode, "end_utc_epoch": time.time(),
                 "stdout": pin(record / "stdout.bin"), "stderr": pin(record / "stderr.bin"),
                 "inputs_after": [pin(p["path"]) for p in inputs]})
(record / "receipt.json").write_text(json.dumps(metadata, indent=2) + "\n")
print(json.dumps({"label": args.label, "exit_code": completed.returncode,
                  "stdout_bytes": metadata["stdout"]["bytes"], "stderr_bytes": metadata["stderr"]["bytes"],
                  "record": str(record)}))
