#!/usr/bin/env python3
"""One documentary snapshot operation; no mathematical or build execution."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import sys
import traceback

PAPER = Path(__file__).resolve().parent
ROOT = PAPER.parents[1]
OUT = PAPER / "source_context"
NAMES = (
    "AGENTS.md", "SYMBOLIC_DYNAMICS_STATE.md",
    ".agents/skills/symbolic-dynamics-research/SKILL.md",
    "docs/research_state/WORKFLOW.md", "docs/research_state/HISTORY_AND_CAVEATS.md",
    "docs/papers204_208_sequence/PIPELINE_STATE.md",
    "docs/papers204_208_sequence/PROBLEM_ANCHOR.md",
    "docs/papers197_201_sequence/PROBLEM_ANCHOR.md",
    "docs/papers204_208_sequence/ARTIFACT_CONTRACT.md",
    "docs/papers204_208_sequence/FINAL_THEOREM_CONTRACTS.md",
    "docs/papers204_208_sequence/P209_ROOT_ADMISSION.md",
    "docs/papers204_208_sequence/scouting/finite_systems_nineteenth/FTH_PROOF_PACKAGE.md",
    "docs/papers204_208_sequence/scouting/FTH_GATE/CANDIDATE_GATE.md",
    "docs/papers204_208_sequence/scouting/FTH_GATE/SOURCE_AND_PROOF.md",
    "docs/papers204_208_sequence/scouting/finite_systems_nineteenth/SOURCE_AND_HISTORY.md",
    "docs/papers204_208_sequence/scouting/finite_systems_nineteenth/public_sources/linearization-ALENEX07.pdf",
    "docs/papers204_208_sequence/scouting/finite_systems_nineteenth/public_sources/linearization-ALENEX07.txt",
    "docs/papers204_208_sequence/scouting/finite_systems_nineteenth/public_sources/isprp_correctness_2005.pdf",
    "docs/papers204_208_sequence/scouting/finite_systems_nineteenth/public_sources/isprp_correctness_2005.txt",
    "docs/papers204_208_sequence/scouting/FTH_GATE/public_sources/rn_TR2005_25.pdf",
    "docs/papers204_208_sequence/scouting/FTH_GATE/public_sources/rn_TR2005_25.txt",
    "docs/papers204_208_sequence/scouting/FTH_GATE/public_sources/tree_path_2504.02448v1.html",
    "docs/papers204_208_sequence/scouting/FTH_GATE/public_sources/tree_path_selected_sections.txt",
    "docs/papers172_176_sequence/scouting/fresh_geometry_automata/SCOUT_AND_KILL_LEDGER.md",
    "docs/papers177_181_sequence/scouting/combinatorial_lane/SCOUT_AND_KILL_LEDGER.md",
    "docs/papers204_208_sequence/scouting/combinatorial_second/PROOF_NOTES.md",
    "papers/167-minimum-inverse-position-feedback/main.tex",
    "docs/papers162_166_sequence/scouting/degree_feedback_jump/SCOUT.md",
    "papers/169-successor-transfer-set-partitions/main.tex",
    "docs/papers172_176_sequence/scouting/combinatorial_crossdomain/focused_nonextractive/IDEA_LEDGER.md",
    "docs/papers204_208_sequence/qa/run_root_fth_gate_pair.py",
    "docs/papers204_208_sequence/scouting/FTH_GATE/bootstrap.py",
    "docs/papers204_208_sequence/qa/run_p208_terminal_builds_v2.py",
)
SKILLS = (
    "paper-plan/SKILL.md", "proof-writer/SKILL.md", "paper-write/SKILL.md",
    "paper-compile/SKILL.md", "shared-references/writing-principles.md",
    "shared-references/citation-discipline.md",
)


def info(path):
    raw = path.read_bytes()
    return {"sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)}


def save(path, data):
    with path.open("x") as stream:
        json.dump(data, stream, indent=2, sort_keys=True)
        stream.write("\n")


def main():
    if OUT.exists() or OUT.is_symlink():
        raise RuntimeError("REFUSE_EXISTING_CONTEXT")
    OUT.mkdir()
    before, after, copies, failure = {}, {}, {}, None
    sources = {str(ROOT / name): "workspace/" + name for name in NAMES}
    sources.update({str(Path("/root/autodl-tmp/.codex/skills") / name): "skills/" + name
                    for name in SKILLS})
    sources[str(Path(__file__).resolve())] = "collection_source.py"
    save(OUT / "ATTEMPT.json", {"argv": sys.argv, "orig_argv": sys.orig_argv,
         "cwd": os.getcwd(), "env": dict(os.environ), "flags": str(sys.flags),
         "scope": "Documentary byte copies only; no science, review, build or view."})
    try:
        before = {path: info(Path(path)) for path in sources}
        save(OUT / "ORIGINALS_BEFORE.json", before)
        for path, relative in sources.items():
            target = OUT / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, target)
            copies[path] = {"snapshot": str(target.relative_to(PAPER)), **info(target)}
            if info(target) != before[path]:
                raise RuntimeError(("COPY_DIFFERS", path))
        after = {path: info(Path(path)) for path in sources}
        if before != after:
            raise RuntimeError("SOURCE_CHANGED_DURING_COPY")
    except BaseException:
        failure = traceback.format_exc()
    finally:
        save(OUT / "ORIGINALS_AFTER.json", after)
        save(OUT / "MAPPING.json", copies)
        save(OUT / "RECEIPT.json", {"status": "PASS" if failure is None else "FAIL_PRESERVED",
             "failure": failure, "copied_files": len(copies),
             "scope": "Historical/documentary copies. Later reuse consumes snapshots, not mutable live originals.",
             "links": "Inside a workspace snapshot, resolve links by its recorded workspace origin; do not erase origin."})
        payloads = sorted(p for p in OUT.rglob("*") if p.is_file())
        with (OUT / "SHA256SUMS").open("x") as seal:
            for path in payloads:
                seal.write(info(path)["sha256"] + "  " + path.relative_to(OUT).as_posix() + "\n")
    print(json.dumps({"status": "PASS" if failure is None else "FAIL_PRESERVED", "copies": len(copies)}))
    return int(failure is not None)


if __name__ == "__main__":
    raise SystemExit(main())
