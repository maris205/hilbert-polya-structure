"""Bounded independent literal/mechanism discovery with raw read-only receipts."""
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import time

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[3]
MIRROR = Path("/root/autodl-tmp/hilbert-polya-structure")
RG = shutil.which("rg")
DEST = BASE / "history_discovery"
DEST.mkdir(exist_ok=False)
ENV = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8", "TZ": "UTC"}


def save(name, value):
    (DEST / name).write_text(json.dumps(value, sort_keys=True, indent=2) + "\n")


def run(argv, tag):
    started = time.time()
    process = subprocess.run(argv, env=ENV, cwd=ROOT, capture_output=True, check=False)
    (DEST / (tag + ".stdout")).write_bytes(process.stdout)
    (DEST / (tag + ".stderr")).write_bytes(process.stderr)
    save(tag + ".command.json", {"argv": argv, "cwd": str(ROOT), "env": ENV,
         "exit": process.returncode, "started_epoch": started, "finished_epoch": time.time()})
    if process.returncode not in {0, 1}:
        raise RuntimeError((tag, process.returncode))
    return process


roots = [ROOT / "papers", ROOT / "docs", MIRROR / "symbolic_dynamics/papers",
         MIRROR / "symbolic_dynamics/docs", MIRROR / "papers", MIRROR / "docs"]
inventory = run([RG, "--files", *map(str, roots)], "inventory")
selected = []
for name in inventory.stdout.decode().splitlines():
    path = Path(name)
    low = name.lower()
    parts = path.parts
    if any(p in {"FTH_GATE", "finite_systems_nineteenth", "reviews", "qa", "qa_final", "source_inputs",
                 "history_inputs", "reviewed_input_snapshot", "assignment_context"} for p in parts):
        continue
    if re.search(r"(?:/208[-/]|/p208|ofs|finite_systems_tenth|word_pattern_tenth|frozen|snapshot|replay|execution|cold_build)", low):
        continue
    if path.suffix == ".tex" or (path.suffix == ".md" and re.search(r"SCOUT|KILL|PROOF|LEDGER|INTAKE", path.name)):
        selected.append(name)
selected = sorted(set(selected))
save("selected.json", selected)


def pins():
    return {name: hashlib.sha256(Path(name).read_bytes()).hexdigest() for name in selected + [RG, str(Path(__file__).resolve())]}


before = pins()
save("before.json", before)
patterns = {
    "threading": r"(fibr[ee]|fiber|preimage).{0,65}(thread|chain|successor)|next[- ]sibling|ordered preimages",
    "inverse": r"increasing.{0,35}path.{0,15}cover|minimum inverse.position|minimum preimage|least predecessor",
    "mechanism": r"functional (di)?graph.{0,40}lineariz|star.to.chain|successor.pointer.{0,20}rewir|kernel.partition.{0,35}encod",
}
receipts = []
for tag, pattern in patterns.items():
    for batch in range(0, len(selected), 500):
        key = tag + "_" + str(batch // 500).zfill(2)
        process = run([RG, "-n", "-i", "--no-heading", "--", pattern, *selected[batch:batch + 500]], key)
        receipts.append({"tag": key, "exit": process.returncode, "bytes": len(process.stdout)})
after = pins()
save("after.json", after)
save("RECEIPT.json", {"kind": "READ_ONLY_BOUNDED_DISCOVERY_NOT_FULL_FILE_REVIEW_OR_NOVELTY", "selected_files": len(selected),
     "patterns": patterns, "runs": receipts, "before_after_equal": before == after,
     "rg_resolved": RG, "roots": list(map(str, roots))})
print(json.dumps({"selected_files": len(selected), "runs": len(receipts), "before_after_equal": before == after,
                  "output_bytes": sum(r["bytes"] for r in receipts)}, sort_keys=True))
if before != after:
    raise SystemExit(1)
