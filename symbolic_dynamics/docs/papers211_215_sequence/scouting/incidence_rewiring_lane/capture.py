#!/usr/bin/env python3
"""Write-once documentary capture and nonself seal; no scientific map code."""
from pathlib import Path
import datetime
import hashlib
import json
import os
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
INPUTS = [
    "docs/papers204_208_sequence/scouting/finite_systems_sixteenth/INTAKE.md",
    "docs/papers204_208_sequence/scouting/finite_systems_sixteenth/PROOF_AND_DISPOSITION.md",
    "docs/papers162_166_sequence/scouting/replacement_matchings_incidence/SCOUT.md",
    "docs/papers167_171_sequence/scouting/combinatorial_crossdomain/IDEA_LEDGER.md",
    "docs/papers132_136_sequence/scouting/combinatorial/SCOUT.md",
    "docs/papers204_208_sequence/scouting/ROOT_PREINTAKE_EXCLUSIONS_20260906.md",
    "docs/papers211_215_sequence/scouting/graph_lane/INTAKE.md",
    "docs/papers211_215_sequence/scouting/graph_lane/SOURCE_AND_COLLISION.md",
    "docs/papers204_208_sequence/scouting/finite_systems_thirty_second/INTAKE.md",
    "docs/papers204_208_sequence/scouting/finite_systems_thirty_second/PROOF_PACKAGE.md",
]
SOURCES = [
    ("schweitzer.html", "https://www.sciencedirect.com/science/article/pii/S0166218X13000127"),
    ("shangguan.html", "https://www.mdpi.com/2075-1680/11/10/540"),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def pin(path):
    data = path.read_bytes()
    return {"bytes": len(data), "sha256": sha(data)}


def fresh(path, data):
    if path.exists():
        raise FileExistsError(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def fresh_json(path, data):
    fresh(path, (json.dumps(data, indent=2, sort_keys=True) + "\n").encode())


def capture():
    if (HERE / "native").exists():
        raise FileExistsError("write-once capture; retain any old attempt")
    (HERE / "native").mkdir()
    (HERE / "sources").mkdir()
    records, inputs = [], []
    for i, rel in enumerate(INPUTS, 1):
        source = ROOT / rel
        raw = source.read_bytes()
        target = HERE / "snapshots" / f"{i:02d}_{source.name}"
        fresh(target, raw)
        assert target.read_bytes() == raw
        inputs.append({"source": rel, "snapshot": str(target.relative_to(HERE)),
                       "bytes": len(raw), "sha256": sha(raw)})
    fresh_json(HERE / "INPUT_PINS.json", {"root": str(ROOT), "inputs": inputs})

    def run(argv, timeout=30):
        number = len(records) + 1
        exe = shutil.which(argv[0])
        started = datetime.datetime.now(datetime.timezone.utc).isoformat()
        try:
            p = subprocess.run(argv, cwd=HERE, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, timeout=timeout, check=False)
            out, err, code, timed_out = p.stdout, p.stderr, p.returncode, False
        except subprocess.TimeoutExpired as exc:
            out, err, code, timed_out = exc.stdout or b"", exc.stderr or b"", None, True
        outname = f"native/{number:02d}.stdout"
        errname = f"native/{number:02d}.stderr"
        fresh(HERE / outname, out)
        fresh(HERE / errname, err)
        record = {"argv": argv, "cwd": str(HERE), "started_utc": started,
                  "exit": code, "timeout": timed_out, "stdout": outname, "stderr": errname,
                  "executable": str(Path(exe).resolve()) if exe else None,
                  "executable_pin": pin(Path(exe).resolve()) if exe else None}
        records.append(record)
        fresh_json(HERE / "native" / f"{number:02d}.record.json", record)
        print(json.dumps({"command": number, "exit": code, "timeout": timed_out}), flush=True)

    run(["sed", "-n", "179,260p", str(ROOT / INPUTS[4])])
    run(["sed", "-n", "40,47p", str(ROOT / INPUTS[0])])
    run(["sed", "-n", "85,228p", str(ROOT / INPUTS[1])])
    run(["sed", "-n", "30,38p", str(ROOT / INPUTS[3])])
    for name, url in SOURCES:
        run(["curl", "--location", "--fail", "--max-time", "20",
             "--max-filesize", "1500000", "--dump-header", f"sources/{name}.headers",
             "--output", f"sources/{name}", url], timeout=25)
    for entry in inputs:
        raw = (ROOT / entry["source"]).read_bytes()
        assert len(raw) == entry["bytes"] and sha(raw) == entry["sha256"]
        assert raw == (HERE / entry["snapshot"]).read_bytes()
    fresh_json(HERE / "native" / "COMMANDS.json", records)
    fresh_json(HERE / "native" / "CAPTURE_RECEIPT.json", {
        "status": "DOCUMENTARY_CAPTURE_COMPLETE", "scientific_runs": 0,
        "input_raw_copy_pairs_checked_before_after": len(inputs),
        "commands": len(records), "producer": pin(Path(__file__)),
        "python": str(Path(sys.executable).resolve()),
        "python_pin": pin(Path(sys.executable).resolve()), "version": sys.version,
        "pid": os.getpid(), "argv": sys.argv, "cwd": str(Path.cwd()),
        "limits": "Not hermetic or complete network/runtime provenance. Documentary output only; not scientific replay or source proof certification."})


def seal():
    target = HERE / "MANIFEST.json"
    if target.exists():
        raise FileExistsError(target)
    entries = [{"path": str(p.relative_to(HERE)), **pin(p)}
               for p in sorted(HERE.rglob("*")) if p.is_file()]
    fresh_json(target, {"scope": "all regular files except MANIFEST.json",
                        "files": entries, "scientific_runs": 0})
    assert {str(p.relative_to(HERE)) for p in HERE.rglob("*") if p.is_file()} == {
        "MANIFEST.json", *(entry["path"] for entry in entries)}
    for entry in entries:
        assert pin(HERE / entry["path"]) == {k: entry[k] for k in ("bytes", "sha256")}
    inputs = json.loads((HERE / "INPUT_PINS.json").read_text())["inputs"]
    for entry in inputs:
        raw = (ROOT / entry["source"]).read_bytes()
        assert len(raw) == entry["bytes"] and sha(raw) == entry["sha256"]
        assert raw == (HERE / entry["snapshot"]).read_bytes()
    print(json.dumps({"status": "SEALED", "payloads": len(entries),
                      "input_copy_pairs": len(inputs),
                      "bytes": sum(e["bytes"] for e in entries),
                      "scientific_runs": 0}, sort_keys=True))


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ("capture", "seal"):
        raise SystemExit("usage: capture.py capture|seal")
    {"capture": capture, "seal": seal}[sys.argv[1]]()
