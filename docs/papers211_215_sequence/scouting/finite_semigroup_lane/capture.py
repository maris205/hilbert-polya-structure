"""Collect this bounded desk's inputs; never execute a scientific candidate."""
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
    "docs/papers132_136_sequence/replacement_scout/nondivisor_algebra/SCOUT.md",
    "docs/papers187_191_sequence/scouting/algebra_lane/replacement/CANDIDATES.md",
    "docs/papers187_191_sequence/scouting/algebra_lane/replacement/KILL_LEDGER.md",
    "papers/167-minimum-inverse-position-feedback/main.tex",
    "papers/190-brandt-sandwich-erosion/main.tex",
    "papers/209-ordered-fibre-threading/sections/01_setup.tex",
    "papers/209-ordered-fibre-threading/sections/02_recurrence.tex",
    "papers/209-ordered-fibre-threading/sections/03_inverse.tex",
    "papers/193-mutual-best-block-refinement/main.tex",
    "docs/papers204_208_sequence/scouting/algebra_second/SCOUT_REPORT.md",
    "docs/papers211_215_sequence/scouting/nonlinear_lane/PROOF_AND_SUBTRACTION.md",
    "docs/papers211_215_sequence/scouting/rational_coupling_lane/PROOF_AND_SUBTRACTION.md",
]


def digest(path):
    raw = path.read_bytes()
    return {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}


def dump(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


def capture():
    (BASE / "native").mkdir(exist_ok=False)
    (BASE / "snapshots").mkdir(exist_ok=False)
    rows = []
    for index, relative in enumerate(SOURCES, 1):
        original = ROOT / relative
        target = BASE / "snapshots" / f"{index:02d}_{original.name}"
        target.write_bytes(original.read_bytes())
        if original.read_bytes() != target.read_bytes():
            raise AssertionError(f"raw snapshot inequality: {relative}")
        rows.append({"source": relative,
                     "snapshot": str(target.relative_to(BASE)),
                     **digest(target), "raw_equal_at_capture": True})
    dump(BASE / "HISTORY_PINS.json", rows)
    commands = [
        (["cat", *[row["snapshot"] for row in rows]], BASE),
        (["rg", "-n", "TM[1-5]|R0[12459]|R10|pointwise|eq:update|eq:literal|eq:rule|\\\\Phi_n|TP |F\\^4",
          *[row["snapshot"] for row in rows[3:]]], BASE),
        (["df", "-B1", str(BASE)], ROOT),
    ]
    for index, (argv, cwd) in enumerate(commands, 1):
        started = time.time_ns()
        result = subprocess.run(argv, cwd=cwd, capture_output=True, check=False)
        stem = BASE / "native" / f"{index:02d}"
        stem.with_suffix(".stdout").write_bytes(result.stdout)
        stem.with_suffix(".stderr").write_bytes(result.stderr)
        dump(stem.with_suffix(".json"), {
            "argv": argv, "cwd": str(cwd), "started_ns": started,
            "finished_ns": time.time_ns(), "exit_code": result.returncode,
            "stdout": digest(stem.with_suffix(".stdout")),
            "stderr": digest(stem.with_suffix(".stderr")),
            "kind": "new_read_only_history_collection_not_science",
        })
        if result.returncode != 0:
            raise AssertionError(f"collection command {index} failed; original evidence retained")
    for row in rows:
        if digest(ROOT / row["source"]) != {key: row[key] for key in ("bytes", "sha256")}:
            raise AssertionError(f"input changed during collection: {row['source']}")
    print(json.dumps({"historical_snapshots": len(rows), "raw_copy_pairs": len(rows),
                      "native_commands": len(commands), "scientific_runs": 0}))


def seal():
    target = BASE / "MANIFEST.json"
    if target.exists():
        raise FileExistsError(target)
    rows = [{"path": str(path.relative_to(BASE)), **digest(path)}
            for path in sorted(BASE.rglob("*")) if path.is_file() and path != target]
    dump(target, {"self_excluded": "MANIFEST.json", "files": rows})
    print(json.dumps({"payloads": len(rows), "bytes": sum(row["bytes"] for row in rows)}))


def verify():
    target = BASE / "MANIFEST.json"
    manifest = json.loads(target.read_text())
    actual = {str(path.relative_to(BASE)) for path in BASE.rglob("*")
              if path.is_file() and path != target}
    if actual != {row["path"] for row in manifest["files"]}:
        raise AssertionError("nonself inventory mismatch")
    for row in manifest["files"]:
        if digest(BASE / row["path"]) != {key: row[key] for key in ("bytes", "sha256")}:
            raise AssertionError(f"payload mismatch: {row['path']}")
    inputs = json.loads((BASE / "HISTORY_PINS.json").read_text())
    for row in inputs:
        if digest(BASE / row["snapshot"]) != {key: row[key] for key in ("bytes", "sha256")}:
            raise AssertionError(f"historical snapshot mismatch: {row['snapshot']}")
    for index in range(1, 4):
        stem = BASE / "native" / f"{index:02d}"
        receipt = json.loads(stem.with_suffix(".json").read_text())
        if receipt["exit_code"] != 0:
            raise AssertionError("unexpected native exit")
        for suffix in ("stdout", "stderr"):
            if digest(stem.with_suffix(f".{suffix}")) != receipt[suffix]:
                raise AssertionError("native raw stream mismatch")
    expected = b"".join((BASE / row["snapshot"]).read_bytes() for row in inputs)
    if expected != (BASE / "native" / "01.stdout").read_bytes():
        raise AssertionError("native full input concatenation mismatch")
    print(json.dumps({"payloads": len(actual), "historical_snapshots": len(inputs),
                      "native_receipts": 3, "raw_concat_equal": True,
                      "scientific_runs": 0,
                      "scope": "author_artifact_integrity_not_review"}))


if __name__ == "__main__":
    {"capture": capture, "seal": seal, "verify": verify}[sys.argv[1]]()
