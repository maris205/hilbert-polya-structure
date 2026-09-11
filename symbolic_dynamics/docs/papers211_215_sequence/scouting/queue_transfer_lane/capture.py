"""Read-only desk evidence capture and compact complete nonself seal.

No mathematical enumeration is implemented or invoked. Generated evidence
is restricted to this file's directory; all historical inputs are read-only.
"""
import hashlib
import json
import pathlib
import subprocess
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def pin(path):
    data = path.read_bytes()
    return {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def capture():
    run = HERE / "native"
    run.mkdir(exist_ok=False)
    sources = [
        ".agents/skills/symbolic-dynamics-research/SKILL.md",
        "docs/research_state/WORKFLOW.md",
        "docs/papers211_215_sequence/PROBLEM_ANCHOR.md",
        "SYMBOLIC_DYNAMICS_STATE.md",
        "docs/papers211_215_sequence/PIPELINE_STATE.md",
        "docs/papers204_208_sequence/scouting/finite_systems_twenty_first/INTAKE.md",
        "docs/papers204_208_sequence/scouting/finite_systems_thirty_eighth/LC_LITERAL.md",
        "docs/papers157_161_sequence/scouting/carry_replacement/SCOUT.md",
        "docs/papers187_191_sequence/scouting/algebra_lane/replacement/CANDIDATES.md",
        "docs/papers187_191_sequence/scouting/algebra_lane/replacement/KILL_LEDGER.md",
    ]
    rows = []
    for i, rel in enumerate(sources, 1):
        src = ROOT / rel
        data = src.read_bytes()
        dst = HERE / "snapshots" / f"{i:02d}_{src.name}"
        dst.parent.mkdir(exist_ok=True)
        dst.write_bytes(data)
        same = src.read_bytes() == dst.read_bytes()
        if not same:
            raise AssertionError(f"source changed during capture: {rel}")
        rows.append({"source": rel, "snapshot": str(dst.relative_to(HERE)),
                     **pin(dst), "raw_equal": same})
    write_json(HERE / "HISTORY_PINS.json", rows)
    commands = [
        ["rg", "-n", "-i", "mancala|owari|sowing", "papers", "docs",
         "-g", "main.tex", "-g", "SCOUT*.md", "-g", "CANDIDATES.md",
         "-g", "*LITERAL*.md", "-g", "*LEDGER*.md", "-g", "INTAKE.md",
         "-g", "!**/queue_transfer_lane/**", "-g", "!**/inputs/**",
         "-g", "!**/originals/**", "-g", "!**/snapshots/**",
         "-g", "!**/execution*/**", "-g", "!**/source_inputs/**",
         "-g", "!**/source_context/**", "-g", "!**/frozen_round*/**"],
        ["cat", *[row["snapshot"] for row in rows]],
        ["df", "-B1", str(HERE)],
    ]
    for i, argv in enumerate(commands, 1):
        cwd = HERE if i == 2 else ROOT
        started = time.time_ns()
        proc = subprocess.run(argv, cwd=cwd, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE, check=False)
        stem = f"{i:02d}"
        (run / f"{stem}.stdout").write_bytes(proc.stdout)
        (run / f"{stem}.stderr").write_bytes(proc.stderr)
        write_json(run / f"{stem}.json", {
            "argv": argv, "cwd": str(cwd), "started_ns": started,
            "finished_ns": time.time_ns(), "exit_code": proc.returncode,
            "stdout": pin(run / f"{stem}.stdout"),
            "stderr": pin(run / f"{stem}.stderr"),
            "kind": "read_only_source_collection_not_science",
        })
    for row in rows:
        if pin(ROOT / row["source"]) != {k: row[k] for k in ("bytes", "sha256")}:
            raise AssertionError(f"historical input changed: {row['source']}")
    print(json.dumps({"snapshots": len(rows), "native_commands": len(commands),
                      "raw_snapshot_comparisons": len(rows),
                      "scientific_executions": 0}))


def seal():
    out = HERE / "MANIFEST.json"
    if out.exists():
        raise FileExistsError(out)
    rows = [{"path": str(p.relative_to(HERE)), **pin(p)}
            for p in sorted(HERE.rglob("*")) if p.is_file() and p != out]
    write_json(out, {"scope": "complete_package_except_this_manifest",
                     "self_excluded": "MANIFEST.json", "files": rows})
    print(json.dumps({"sealed_payloads": len(rows),
                      "bytes": sum(row["bytes"] for row in rows)}))


def verify():
    manifest = json.loads((HERE / "MANIFEST.json").read_text())
    expected = {row["path"] for row in manifest["files"]}
    actual = {str(p.relative_to(HERE)) for p in HERE.rglob("*")
              if p.is_file() and p.name != "MANIFEST.json"}
    if actual != expected:
        raise AssertionError("nonself manifest file-set mismatch")
    for row in manifest["files"]:
        if pin(HERE / row["path"]) != {k: row[k] for k in ("bytes", "sha256")}:
            raise AssertionError(f"payload mismatch: {row['path']}")
    rows = json.loads((HERE / "HISTORY_PINS.json").read_text())
    for row in rows:
        if pin(HERE / row["snapshot"]) != {k: row[k] for k in ("bytes", "sha256")}:
            raise AssertionError(f"snapshot mismatch: {row['snapshot']}")
    for i in range(1, 4):
        rec = json.loads((HERE / "native" / f"{i:02d}.json").read_text())
        for suffix in ("stdout", "stderr"):
            if pin(HERE / "native" / f"{i:02d}.{suffix}") != rec[suffix]:
                raise AssertionError(f"native output mismatch: {i}, {suffix}")
        expected_exit = 1 if i == 1 else 0
        if rec["exit_code"] != expected_exit:
            raise AssertionError(f"unexpected captured exit: {i}")
    expected_cat = b"".join((HERE / row["snapshot"]).read_bytes() for row in rows)
    if expected_cat != (HERE / "native" / "02.stdout").read_bytes():
        raise AssertionError("raw concatenated historical read mismatch")
    print(json.dumps({"payloads": len(expected), "snapshots": len(rows),
                      "native_receipts": 3, "raw_concatenation_equal": True,
                      "scientific_executions": 0,
                      "scope": "self_integrity_only_not_independent_review"}))


if __name__ == "__main__":
    if sys.argv[1:] == ["capture"]:
        capture()
    elif sys.argv[1:] == ["seal"]:
        seal()
    elif sys.argv[1:] == ["verify"]:
        verify()
    else:
        raise SystemExit("usage: capture.py capture|seal|verify")
