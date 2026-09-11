"""Compact negative-desk collection; no scientific execution or external writes."""
import hashlib
import json
import pathlib
import subprocess
import sys
import time

BASE = pathlib.Path(__file__).resolve().parent
ROOT = BASE.parents[3]
SOURCES = [
    ".agents/skills/symbolic-dynamics-research/SKILL.md",
    "docs/research_state/WORKFLOW.md",
    "docs/papers211_215_sequence/PROBLEM_ANCHOR.md",
    "SYMBOLIC_DYNAMICS_STATE.md",
    "docs/papers211_215_sequence/PIPELINE_STATE.md",
    "docs/papers204_208_sequence/scouting/finite_structures_eighth/INTAKE.md",
    "docs/papers204_208_sequence/scouting/finite_structures_eighth/PROOF_BOUNDARIES.md",
    "docs/papers187_191_sequence/scouting/combinatorial_lane/CANDIDATES.md",
    "docs/papers187_191_sequence/scouting/combinatorial_lane/KILL_LEDGER.md",
    "papers/113-principal-hook-partition-dynamics/main.tex",
    "papers/160-rectangular-corner-stripping-atlas/main.tex",
]


def digest(p):
    raw = p.read_bytes()
    return {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}


def dump(p, obj):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


def capture():
    (BASE / "native").mkdir(exist_ok=False)
    (BASE / "snapshots").mkdir(exist_ok=False)
    rows = []
    for i, rel in enumerate(SOURCES, 1):
        source = ROOT / rel
        dest = BASE / "snapshots" / f"{i:02d}_{source.name}"
        raw = source.read_bytes()
        dest.write_bytes(raw)
        if source.read_bytes() != dest.read_bytes():
            raise AssertionError(f"raw copy failed: {rel}")
        rows.append({"source": rel, "snapshot": str(dest.relative_to(BASE)),
                     **digest(dest), "raw_equal_at_capture": True})
    dump(BASE / "HISTORY_PINS.json", rows)
    commands = [
        (["cat", *[row["snapshot"] for row in rows]], BASE),
        (["rg", "-n", "C17_TRR|WGP|DSR|eq:map|h_i=",
          *[row["snapshot"] for row in rows[5:]]], BASE),
        (["df", "-B1", str(BASE)], ROOT),
    ]
    for i, (argv, cwd) in enumerate(commands, 1):
        start = time.time_ns()
        result = subprocess.run(argv, cwd=cwd, capture_output=True, check=False)
        stem = BASE / "native" / f"{i:02d}"
        stem.with_suffix(".stdout").write_bytes(result.stdout)
        stem.with_suffix(".stderr").write_bytes(result.stderr)
        dump(stem.with_suffix(".json"), {
            "argv": argv, "cwd": str(cwd), "started_ns": start,
            "finished_ns": time.time_ns(), "exit_code": result.returncode,
            "stdout": digest(stem.with_suffix(".stdout")),
            "stderr": digest(stem.with_suffix(".stderr")),
            "kind": "read_only_history_collection_not_science",
        })
        if result.returncode != 0:
            raise AssertionError(f"native collection {i} failed; evidence preserved")
    for row in rows:
        if digest(ROOT / row["source"]) != {k: row[k] for k in ("bytes", "sha256")}:
            raise AssertionError(f"input changed: {row['source']}")
    print(json.dumps({"snapshots": len(rows), "raw_copy_pairs": len(rows),
                      "native_commands": len(commands), "science": 0}))


def seal():
    target = BASE / "MANIFEST.json"
    if target.exists():
        raise FileExistsError(target)
    rows = [{"path": str(p.relative_to(BASE)), **digest(p)}
            for p in sorted(BASE.rglob("*")) if p.is_file() and p != target]
    dump(target, {"self_excluded": "MANIFEST.json", "files": rows})
    print(json.dumps({"payloads": len(rows),
                      "bytes": sum(row["bytes"] for row in rows)}))


def verify():
    manifest = json.loads((BASE / "MANIFEST.json").read_text())
    actual = {str(p.relative_to(BASE)) for p in BASE.rglob("*")
              if p.is_file() and p.name != "MANIFEST.json"}
    if actual != {row["path"] for row in manifest["files"]}:
        raise AssertionError("nonself inventory mismatch")
    for row in manifest["files"]:
        if digest(BASE / row["path"]) != {k: row[k] for k in ("bytes", "sha256")}:
            raise AssertionError(f"payload mismatch: {row['path']}")
    rows = json.loads((BASE / "HISTORY_PINS.json").read_text())
    for row in rows:
        if digest(BASE / row["snapshot"]) != {k: row[k] for k in ("bytes", "sha256")}:
            raise AssertionError(f"snapshot mismatch: {row['snapshot']}")
    for i in range(1, 4):
        stem = BASE / "native" / f"{i:02d}"
        rec = json.loads(stem.with_suffix(".json").read_text())
        if rec["exit_code"] != 0:
            raise AssertionError("unexpected native exit")
        for suffix in ("stdout", "stderr"):
            if digest(stem.with_suffix(f".{suffix}")) != rec[suffix]:
                raise AssertionError("native raw stream mismatch")
    expected = b"".join((BASE / row["snapshot"]).read_bytes() for row in rows)
    if expected != (BASE / "native" / "01.stdout").read_bytes():
        raise AssertionError("raw concatenation mismatch")
    print(json.dumps({"payloads": len(actual), "snapshots": len(rows),
                      "native_receipts": 3, "raw_concat_equal": True,
                      "scientific_runs": 0,
                      "scope": "author_integrity_not_independent_review"}))


if __name__ == "__main__":
    {"capture": capture, "seal": seal, "verify": verify}[sys.argv[1]]()
