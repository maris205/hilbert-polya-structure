#!/usr/bin/env python3
"""Write-once desk source/input capture and nonself seal; no scientific map code."""
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
    "papers/210-weakly-increasing-run-aggregation/PROOF_PACKAGE.md",
    "papers/210-weakly-increasing-run-aggregation/SOURCE_AUDIT.md",
    "papers/147-adjacent-run-consolidation/main.tex",
    "docs/papers162_166_sequence/scouting/replacement_crossclass/SCOUT.md",
    "papers/149-iterated-endpoint-peak-extraction/main.tex",
    "papers/121-random-product-plus-one-coalescence/main.tex",
    "papers/129-rootward-active-pile-coalescence/sections/1_model.tex",
    "papers/129-rootward-active-pile-coalescence/sections/3_interfaces.tex",
]
SOURCES = [
    ("hcp.html", "https://arxiv.org/html/1012.4912"),
    ("huffman_1952.pdf", "https://compression.ru/download/articles/huff/huffman_1952_minimum-redundancy-codes.pdf"),
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
        raise FileExistsError("write-once attempt; preserve existing evidence")
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

    def run(argv, timeout=40):
        number = len(records) + 1
        exe = shutil.which(argv[0])
        started = datetime.datetime.now(datetime.timezone.utc).isoformat()
        try:
            p = subprocess.run(argv, cwd=HERE, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, timeout=timeout, check=False)
            out, err, code, timed_out = p.stdout, p.stderr, p.returncode, False
        except subprocess.TimeoutExpired as exc:
            out, err, code, timed_out = exc.stdout or b"", exc.stderr or b"", None, True
        outname, errname = f"native/{number:02d}.stdout", f"native/{number:02d}.stderr"
        fresh(HERE / outname, out)
        fresh(HERE / errname, err)
        record = {"argv": argv, "cwd": str(HERE), "started_utc": started,
                  "exit": code, "timeout": timed_out, "stdout": outname, "stderr": errname,
                  "executable": str(Path(exe).resolve()) if exe else None,
                  "executable_pin": pin(Path(exe).resolve()) if exe else None}
        records.append(record)
        fresh_json(HERE / "native" / f"{number:02d}.record.json", record)
        print(json.dumps({"command": number, "exit": code, "timeout": timed_out}), flush=True)
        return code

    run(["curl", "--version"])
    run(["pdftotext", "-v"])
    run(["pdftoppm", "-v"])
    run(["sed", "-n", "35,96p", str(ROOT / INPUTS[0])])
    run(["sed", "-n", "171,198p", str(ROOT / INPUTS[3])])
    for name, url in SOURCES:
        code = run(["curl", "--location", "--fail", "--max-time", "25",
                    "--max-filesize", "2500000", "--dump-header", f"sources/{name}.headers",
                    "--output", f"sources/{name}", url], timeout=30)
        if code == 0 and name.endswith(".pdf"):
            run(["pdftotext", "-layout", f"sources/{name}", f"sources/{name}.txt"])
            run(["pdftoppm", "-f", "2", "-l", "2", "-singlefile", "-scale-to", "1400",
                 "-png", f"sources/{name}", "sources/huffman_page2"])
    for entry in inputs:
        raw = (ROOT / entry["source"]).read_bytes()
        assert sha(raw) == entry["sha256"] and len(raw) == entry["bytes"]
        assert raw == (HERE / entry["snapshot"]).read_bytes()
    fresh_json(HERE / "native" / "COMMANDS.json", records)
    fresh_json(HERE / "native" / "CAPTURE_RECEIPT.json", {
        "status": "CAPTURE_COMPLETE", "scientific_runs": 0,
        "inputs_before_after_unchanged_and_raw_equal_copies": len(inputs),
        "commands": len(records), "producer": pin(Path(__file__)),
        "python": str(Path(sys.executable).resolve()),
        "python_pin": pin(Path(sys.executable).resolve()), "version": sys.version,
        "pid": os.getpid(), "argv": sys.argv, "cwd": str(Path.cwd()),
        "limits": "Incomplete full runtime/config/network provenance; not hermetic; source rendering is not a science run or manuscript page review."})


def seal():
    target = HERE / "MANIFEST.json"
    if target.exists():
        raise FileExistsError(target)
    entries = [{"path": str(p.relative_to(HERE)), **pin(p)}
               for p in sorted(HERE.rglob("*")) if p.is_file()]
    fresh_json(target, {"scope": "all regular files except MANIFEST.json", "files": entries,
                        "scientific_runs": 0})
    for entry in entries:
        assert pin(HERE / entry["path"]) == {k: entry[k] for k in ("bytes", "sha256")}
    inputs = json.loads((HERE / "INPUT_PINS.json").read_text())["inputs"]
    for entry in inputs:
        raw = (ROOT / entry["source"]).read_bytes()
        assert sha(raw) == entry["sha256"] and len(raw) == entry["bytes"]
        assert raw == (HERE / entry["snapshot"]).read_bytes()
    print(json.dumps({"status": "SEALED", "payloads": len(entries), "input_copy_pairs": len(inputs),
                      "bytes": sum(e["bytes"] for e in entries), "scientific_runs": 0}, sort_keys=True))


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ("capture", "seal"):
        raise SystemExit("usage: capture.py capture|seal")
    {"capture": capture, "seal": seal}[sys.argv[1]]()
