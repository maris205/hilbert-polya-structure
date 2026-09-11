#!/usr/bin/env python3
"""Source-only desk capture; raw native streams embedded as base64, no pilot."""
from pathlib import Path
import base64
import datetime
import hashlib
import json
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
INPUTS = [
    "docs/papers204_208_sequence/scouting/discrete_geometry_seventh/INTAKE.md",
    "docs/papers204_208_sequence/scouting/finite_systems_fortieth/INTAKE.md",
    "docs/papers204_208_sequence/scouting/finite_systems_fortieth/PROOF_PACKAGE.md",
    "docs/papers127_131_sequence/scouting/combinatorial/SCOUT.md",
    "docs/papers127_131_sequence/scouting/combinatorial/pilot_breadth.py",
    "papers/120-odd-fringe-mirror-plane-trees/main.tex",
    "papers/148-even-level-plane-tree-contraction/main.tex",
    "docs/papers211_215_sequence/scouting/tree_order_lane/INTAKE.md",
]
SOURCES = [
    ("tfpl", "https://arxiv.org/pdf/1406.1657v1"),
    ("ornament", "https://arxiv.org/pdf/2501.10311v1"),
    ("billiards", "https://arxiv.org/pdf/2202.06943v2"),
    ("zhu", "https://arxiv.org/pdf/2309.00100v3"),
]


def pin(data):
    return {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def fresh(path, data):
    if path.exists():
        raise FileExistsError(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def fresh_json(path, data):
    fresh(path, (json.dumps(data, indent=2, sort_keys=True) + "\n").encode())


def capture():
    if (HERE / "native").exists():
        raise FileExistsError("preserve existing capture; no overwrite")
    (HERE / "native").mkdir()
    (HERE / "sources").mkdir()
    inputs, records = [], []
    for number, rel in enumerate(INPUTS, 1):
        raw = (ROOT / rel).read_bytes()
        snapshot = f"snapshots/{number:02d}_{Path(rel).name}"
        fresh(HERE / snapshot, raw)
        assert (HERE / snapshot).read_bytes() == raw
        inputs.append({"source": rel, "snapshot": snapshot, **pin(raw)})
    fresh_json(HERE / "INPUT_PINS.json", {"root": str(ROOT), "inputs": inputs})

    def run(argv, timeout=30):
        started = datetime.datetime.now(datetime.timezone.utc).isoformat()
        executable = Path(shutil.which(argv[0])).resolve()
        try:
            p = subprocess.run(argv, cwd=HERE, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, timeout=timeout, check=False)
            code, out, err, timed_out = p.returncode, p.stdout, p.stderr, False
        except subprocess.TimeoutExpired as exc:
            code, out, err, timed_out = None, exc.stdout or b"", exc.stderr or b"", True
        record = {"argv": argv, "cwd": str(HERE), "started_utc": started,
                  "exit": code, "timed_out": timed_out,
                  "executable": str(executable), "executable_pin": pin(executable.read_bytes()),
                  "stdout_b64": base64.b64encode(out).decode(), "stdout_pin": pin(out),
                  "stderr_b64": base64.b64encode(err).decode(), "stderr_pin": pin(err)}
        records.append(record)
        fresh_json(HERE / "native" / f"{len(records):02d}.json", record)
        print(json.dumps({"command": len(records), "exit": code, "timed_out": timed_out}), flush=True)
        return code

    for name, url in SOURCES:
        code = run(["curl", "--location", "--fail", "--max-time", "25",
                    "--max-filesize", "2500000", "--dump-header", f"sources/{name}.headers",
                    "--output", f"sources/{name}.pdf", url])
        if code == 0:
            run(["pdftotext", "-layout", f"sources/{name}.pdf", f"sources/{name}.txt"])
    if (HERE / "sources/tfpl.pdf").exists():
        for page in (6, 10, 11, 12):
            run(["pdftoppm", "-f", str(page), "-l", str(page), "-singlefile",
                 "-scale-to", "1450", "-png", "sources/tfpl.pdf", f"sources/tfpl_page{page}"])
    for row in inputs:
        raw = (ROOT / row["source"]).read_bytes()
        assert pin(raw) == {k: row[k] for k in ("bytes", "sha256")}
        assert raw == (HERE / row["snapshot"]).read_bytes()
    fresh_json(HERE / "native" / "RECEIPT.json", {
        "scientific_runs": 0, "commands": len(records), "input_raw_copy_pairs": len(inputs),
        "raw_stream_encoding": "Each native NN.json embeds complete stdout/stderr as base64 and raw byte pins.",
        "producer": pin(Path(__file__).read_bytes()), "argv": sys.argv,
        "python": str(Path(sys.executable).resolve()), "python_version": sys.version,
        "python_pin": pin(Path(sys.executable).resolve().read_bytes()),
        "limits": "Source retrieval/rendering and raw-copy checks only, not hermetic or complete runtime provenance; file existence is not visual review."})


def seal():
    target = HERE / "MANIFEST.json"
    if target.exists():
        raise FileExistsError(target)
    entries = [{"path": str(path.relative_to(HERE)), **pin(path.read_bytes())}
               for path in sorted(HERE.rglob("*")) if path.is_file()]
    for path in sorted((HERE / "native").glob("[0-9][0-9].json")):
        record = json.loads(path.read_text())
        for stream in ("stdout", "stderr"):
            assert pin(base64.b64decode(record[f"{stream}_b64"], validate=True)) == record[f"{stream}_pin"]
    for row in json.loads((HERE / "INPUT_PINS.json").read_text())["inputs"]:
        raw = (ROOT / row["source"]).read_bytes()
        assert pin(raw) == {k: row[k] for k in ("bytes", "sha256")}
        assert raw == (HERE / row["snapshot"]).read_bytes()
    fresh_json(target, {"scope": "all regular files except MANIFEST.json", "files": entries,
                        "new_literals": 0, "scientific_runs": 0})
    assert {str(p.relative_to(HERE)) for p in HERE.rglob("*") if p.is_file()} == {
        "MANIFEST.json", *(row["path"] for row in entries)}
    for row in entries:
        assert pin((HERE / row["path"]).read_bytes()) == {k: row[k] for k in ("bytes", "sha256")}
    print(json.dumps({"status": "SEALED_NO_FRESH_SLATE", "payloads": len(entries),
                      "bytes": sum(r["bytes"] for r in entries), "new_literals": 0,
                      "scientific_runs": 0}, sort_keys=True))


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ("capture", "seal"):
        raise SystemExit("usage: capture.py capture|seal")
    {"capture": capture, "seal": seal}[sys.argv[1]]()
