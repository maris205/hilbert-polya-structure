#!/usr/bin/env python3
"""Create the freezer's flat stdout aliases, not new numerical executions."""

from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys


BASE = Path(__file__).resolve().parent
PAIR = BASE / "pair_01"
EXPORT = BASE / "export_pair_01"


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def save(path, data):
    with path.open("xb") as stream:
        stream.write(data)


def main():
    receipt = json.loads((PAIR / "RECEIPT.json").read_text())
    if receipt["status"] != "PASS" or any(c["exit_code"] for c in receipt["commands"]):
        raise RuntimeError("pair receipt is not a completed passing execution")
    targets = [BASE / f"run{number}.stdout" for number in (1, 2)]
    if any(path.exists() for path in targets) or EXPORT.exists():
        raise FileExistsError("refusing to overwrite a flat alias or export receipt")
    EXPORT.mkdir()
    summary = {"kind": "immutable raw-byte copies of the existing two author runs",
               "new_numerical_runs": 0, "started_utc": datetime.now(timezone.utc).isoformat(),
               "exporter_sha256": digest(Path(__file__)), "pair_receipt_sha256": digest(PAIR / "RECEIPT.json"),
               "source_canonical_sha256": receipt["canonical_input_sha256"], "commands": []}
    env = os.environ.copy()
    env.update({"LC_ALL": "C", "TZ": "UTC"})
    for number, target in zip((1, 2), targets):
        source = PAIR / f"run{number}.stdout"
        data = source.read_bytes()
        if sha256(data).hexdigest() != receipt["canonical_input_sha256"]:
            raise RuntimeError("source run bytes no longer match the actual receipt")
        save(target, data)
        for label, other in (("original", source), ("canonical", BASE.parent / "CANONICAL.json")):
            command = ["cmp", str(target), str(other)]
            stem = f"run{number}.{label}.cmp"
            with (EXPORT / f"{stem}.stdout").open("xb") as output, (EXPORT / f"{stem}.stderr").open("xb") as errors:
                child = subprocess.run(command, cwd=EXPORT, env=env, stdout=output, stderr=errors, check=False)
            summary["commands"].append({"argv": command, "cwd": str(EXPORT), "exit_code": child.returncode,
                                        "stdout": f"{stem}.stdout", "stderr": f"{stem}.stderr"})
    summary["flat_aliases"] = [{"path": path.name, "bytes": path.stat().st_size, "sha256": digest(path)}
                               for path in targets]
    summary["finished_utc"] = datetime.now(timezone.utc).isoformat()
    summary["status"] = "PASS" if all(c["exit_code"] == 0 for c in summary["commands"]) else "FAIL"
    save(EXPORT / "RECEIPT.json", (json.dumps(summary, sort_keys=True, indent=2) + "\n").encode())
    pins = "".join(f"{digest(path)}  {path.name}\n" for path in sorted(EXPORT.iterdir()) if path.is_file())
    save(EXPORT / "MANIFEST.sha256", pins.encode())
    print(json.dumps(summary, sort_keys=True, indent=2))
    return 0 if summary["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
