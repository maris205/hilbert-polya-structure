#!/usr/bin/env python3
"""Compact desk-only capture/seal producer. It never executes a scientific map."""
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
    "docs/papers204_208_sequence/scouting/algebra_fourth/OTHER_MAP_ADAPTERS.md",
    "docs/papers204_208_sequence/scouting/algebra_fourth/pilot.py",
    "docs/papers204_208_sequence/scouting/algebra_fourth/SCOUT_REPORT.md",
    "docs/papers204_208_sequence/scouting/algebra_fourth/SOURCE_AND_COLLISION_NOTES.md",
    "docs/papers187_191_sequence/scouting/algebra_lane/replacement/CANDIDATES.md",
    "docs/papers187_191_sequence/scouting/algebra_lane/replacement/KILL_LEDGER.md",
    "docs/papers187_191_sequence/scouting/algebra_lane/replacement/pilot.py",
    "docs/papers162_166_sequence/scouting/replacement_posets_languages/SCOUT.md",
    "docs/papers162_166_sequence/scouting/replacement_posets_languages/verify_scout.py",
    "papers/130-crossing-component-fibre-geometry/main.tex",
]
SOURCES = [
    ("riverbend_lesson.pdf", "https://riverbendmath.org/modules/Candy_Sharing_Game/Lesson_Plan/Candy_Sharing_Lesson_Plan.pdf"),
    ("bal_degaetani.pdf", "https://msuweb.montclair.edu/~bald/files/candy-sharing.pdf"),
    ("dijkstra_ewd386.html", "https://www.cs.utexas.edu/~EWD/transcriptions/EWD03xx/EWD386.html"),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def fresh(path, data):
    if path.exists():
        raise FileExistsError(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def fresh_json(path, data):
    fresh(path, (json.dumps(data, indent=2, sort_keys=True) + "\n").encode())


def pin(path):
    raw = path.read_bytes()
    return {"bytes": len(raw), "sha256": sha(raw)}


def capture():
    if (HERE / "native").exists():
        raise FileExistsError("capture is write-once; preserve the old attempt")
    (HERE / "native").mkdir()
    (HERE / "sources").mkdir()
    records = []
    inputs = []
    for i, rel in enumerate(INPUTS, 1):
        source = ROOT / rel
        raw = source.read_bytes()
        target = HERE / "snapshots" / f"{i:02d}_{source.name}"
        fresh(target, raw)
        assert target.read_bytes() == raw
        inputs.append({"source": rel, "snapshot": str(target.relative_to(HERE)),
                       "bytes": len(raw), "sha256": sha(raw)})
    fresh_json(HERE / "INPUT_PINS.json", {"root": str(ROOT), "inputs": inputs})

    def run(argv, timeout=45):
        number = len(records) + 1
        exe = shutil.which(argv[0])
        started = datetime.datetime.now(datetime.timezone.utc).isoformat()
        try:
            proc = subprocess.run(argv, cwd=HERE, stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE, timeout=timeout, check=False)
            out, err, code = proc.stdout, proc.stderr, proc.returncode
            timeout_hit = False
        except subprocess.TimeoutExpired as exc:
            out, err, code = exc.stdout or b"", exc.stderr or b"", None
            timeout_hit = True
        outname, errname = f"native/{number:02d}.stdout", f"native/{number:02d}.stderr"
        fresh(HERE / outname, out)
        fresh(HERE / errname, err)
        records.append({"argv": argv, "cwd": str(HERE), "started_utc": started,
                        "exit": code, "timeout": timeout_hit,
                        "stdout": outname, "stderr": errname,
                        "executable": str(Path(exe).resolve()) if exe else None,
                        "executable_pin": pin(Path(exe).resolve()) if exe else None})
        fresh_json(HERE / "native" / f"{number:02d}.record.json", records[-1])
        print(json.dumps({"command": number, "exit": code, "timeout": timeout_hit}), flush=True)
        return code

    run(["curl", "--version"])
    run(["pdftotext", "-v"])
    run(["rg", "-n", "MG:|tagged|g_i'|anchor|MG.1", str(ROOT / INPUTS[0])])
    run(["sed", "-n", "127,141p", str(ROOT / INPUTS[1])])
    run(["sed", "-n", "426,431p", str(ROOT / INPUTS[6])])
    run(["sed", "-n", "774,781p", str(ROOT / INPUTS[8])])
    for name, url in SOURCES:
        code = run(["curl", "--location", "--fail", "--max-time", "25",
                    "--dump-header", f"sources/{name}.headers",
                    "--output", f"sources/{name}", url], timeout=30)
        if code == 0 and name.endswith(".pdf"):
            run(["pdftotext", "-layout", f"sources/{name}", f"sources/{name}.txt"])
    for entry in inputs:
        raw = (ROOT / entry["source"]).read_bytes()
        assert sha(raw) == entry["sha256"] and len(raw) == entry["bytes"]
        assert raw == (HERE / entry["snapshot"]).read_bytes()
    fresh_json(HERE / "native" / "COMMANDS.json", records)
    fresh_json(HERE / "native" / "CAPTURE_RECEIPT.json", {
        "status": "CAPTURE_COMPLETE", "scientific_runs": 0,
        "input_copies_raw_equal_and_before_after_unchanged": len(inputs),
        "native_commands": len(records), "producer": pin(Path(__file__)),
        "python_executable": str(Path(sys.executable).resolve()),
        "python_executable_pin": pin(Path(sys.executable).resolve()),
        "python_version": sys.version, "pid": os.getpid(),
        "argv": sys.argv, "cwd": str(Path.cwd()),
        "limitation": "No full runtime/shared-library/configuration/network closure; not hermetic."})


def seal():
    target = HERE / "MANIFEST.json"
    if target.exists():
        raise FileExistsError(target)
    entries = []
    for path in sorted(HERE.rglob("*")):
        if path.is_file():
            entries.append({"path": str(path.relative_to(HERE)), **pin(path)})
    fresh_json(target, {"scope": "all regular lane files except MANIFEST.json",
                        "files": entries, "scientific_runs": 0})
    for entry in entries:
        assert pin(HERE / entry["path"]) == {k: entry[k] for k in ("bytes", "sha256")}
    inputs = json.loads((HERE / "INPUT_PINS.json").read_text())["inputs"]
    for entry in inputs:
        raw = (ROOT / entry["source"]).read_bytes()
        assert sha(raw) == entry["sha256"] and len(raw) == entry["bytes"]
        assert raw == (HERE / entry["snapshot"]).read_bytes()
    print(json.dumps({"status": "SEALED", "payloads": len(entries),
                      "inputs_and_exact_copies": len(inputs),
                      "bytes_excluding_manifest": sum(e["bytes"] for e in entries),
                      "scientific_runs": 0}, sort_keys=True))


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ("capture", "seal"):
        raise SystemExit("usage: capture.py capture|seal")
    {"capture": capture, "seal": seal}[sys.argv[1]]()
