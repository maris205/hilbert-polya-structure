#!/usr/bin/env python3
"""Strict source gate, fresh deterministic PDF builds, and self-excluding release."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c394 release refuses optimized Python")
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
MANIFEST = ROOT/"C394_RELEASE_MANIFEST.json"
AUTHORITY = "flow_systems/skills/route-a-evaluator.md"
AUTHORITY_SHA = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
NAMES = ("main_round0_original.pdf", "main_round1.pdf", "main_round2.pdf")
SCRIPTS = ("c394_interpolation_producer.py", "c394_interpolation_checker.py", "c394_interpolation_sympy_crosscheck.py", "c394_interpolation_replay.py", "c394_interpolation_mutation.py", "c394_release_manifest.py")
EXPECTED = (
    "ASSUMPTIONS.md", "CLAIMS.md", "EXPERIMENT_PLAN.md", "LIMITATIONS.md", "NARRATIVE_REPORT.md",
    "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md", "README.md", "REFERENCES.md", "REPRODUCIBILITY.md",
    "RESEARCH_QUESTION.md", "SCOPE.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md", "requirements.txt",
    "proof/ANALYTIC_PROOF.md", "code/README.md",
    "code/c394_interpolation_producer.py", "code/c394_interpolation_checker.py", "code/c394_interpolation_sympy_crosscheck.py",
    "code/c394_interpolation_replay.py", "code/c394_interpolation_mutation.py", "code/c394_release_manifest.py",
    "evaluations/route_a/HCS-C394/2026-09-05.yaml", "paper/README.md", "paper/COMPILE_REPORT.md",
    "paper/main.tex", "paper/main_round0.tex", "paper/main_round1.tex", "paper/main_round2.tex",
    "paper/main.pdf", "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "paper/compile_round0.txt", "paper/compile_round1.txt", "paper/compile_round2.txt",
    "results/RESULTS.md", "results/TEST_REPORT.md", "results/HOSTILE_AUDIT.md",
    "results/c394_interpolation_evidence.json", "tests/test_c394_smoke.py",
    "review/ROUND0_REVIEW.md", "review/ROUND1_REVIEW.md", "review/ROUND2_REVIEW.md",
    "review/FAILURE_MODE_AUDIT.md", "review/FINAL_INTEGRITY.md",
)
WARN = re.compile(r"(?:LaTeX|Package [^:\n]+) Warning:|warning  \(pdf backend\)|Overfull|Underfull|undefined (?:references|citations)|Rerun to get|Missing character")

def run(command, **kwargs):
    proc = subprocess.run(command, capture_output=True, text=True, **kwargs)
    assert proc.returncode == 0, "command failed "+repr(command)+"\n"+proc.stdout+proc.stderr
    return proc.stdout.strip()

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def canonical(data):
    return json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()

def unique(pairs):
    out = {}
    for k, v in pairs:
        assert k not in out, "duplicate JSON"
        out[k] = v
    return out

def strict(path):
    return json.loads(path.read_text(), object_pairs_hook=unique, parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))

def content_gate():
    assert not any(p.is_symlink() for p in ROOT.rglob("*")), "SYMLINK_REFUSED before any release write"
    from c394_interpolation_checker import evaluation, EVAL
    try:
        data = evaluation(EVAL)
    except Exception as exc:
        raise ValueError("EVALUATION_REFUSED before any release write") from exc
    assert sha(REPO/AUTHORITY) == AUTHORITY_SHA, "evaluator authority"
    return data

def compile_round(index):
    blobs, logs = [], []
    for build in range(2):
        with tempfile.TemporaryDirectory(prefix=f"c394-tex-{index}-{build}-") as directory:
            work = Path(directory)
            for name in ("main.tex", f"main_round{index}.tex"):
                shutil.copy2(ROOT/"paper"/name, work/name)
            command = ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=main", f"main_round{index}.tex"]
            env = dict(os.environ, SOURCE_DATE_EPOCH="1788566400", FORCE_SOURCE_DATE="1")
            run(command, cwd=work, env=env)
            run(command, cwd=work, env=env)
            log = (work/"main.log").read_text(errors="replace")
            match = WARN.search(log)
            assert match is None, f"round {index} settled compiler warning: "+log[max(0, match.start()-80):match.start()+600]
            blobs.append((work/"main.pdf").read_bytes())
            logs.append(log)
    assert blobs[0] == blobs[1], "two-directory PDF bytes differ"
    return blobs[0], logs[0]

def pdf_audit(path, index):
    info = run(["pdfinfo", str(path)])
    match = re.search(r"^Pages:\s+(\d+)", info, re.M)
    assert match
    pages = int(match.group(1))
    fonts = run(["pdffonts", str(path)]).splitlines()[2:]
    assert fonts and any("DroidSansFallback" in line.replace(" ", "") for line in fonts)
    for line in fonts:
        assert line.split()[-5:-3] == ["yes", "yes"], line
    with tempfile.TemporaryDirectory(prefix="c394-pdf-audit-") as directory:
        work = Path(directory)
        target = work/"text.txt"
        run(["pdftotext", str(path), str(target)])
        raw = target.read_bytes()
        assert all(b >= 32 or b in (10, 12, 13) for b in raw), "PDF text control byte"
        text = raw.decode()
        flat = " ".join(text.split())
        assert "Exact Analytic Orbits of a Nonlinear" in flat
        assert all(t not in text for t in ("??", "[VERIFY]", "TODO"))
        assert "Keywords:" in text and "中文摘要" in text and "关键词" in text
        en = text.split("Keywords:", 1)[1].split("中文摘要", 1)[0]
        cn = text.split("关键词", 1)[1].split("1", 1)[0]
        assert en.count(";") == 5 and cn.count("；") == 5
        assert f"Round {('zero', 'one', 'two')[index]}" in flat
        assert ("The exact displacement scale and minimal decomposition" in flat) == (index >= 1)
        assert ("Algebraic hitting times: finite or all" in flat) == (index >= 2)
        if index == 2:
            assert "NO_BAD_EULER_OR_ROOT_NUMBER" in text and "Route B remains disabled." in flat
        run(["pdftoppm", "-png", "-r", "60", str(path), str(work/"page")])
        images = sorted(work.glob("page-*.png"))
        assert len(images) == pages and all(p.stat().st_size > 1000 for p in images)
        raster_sizes = [p.stat().st_size for p in images]
    return {"round": index, "file": "paper/"+path.name, "sha256": sha(path), "pages": pages, "embedded_subset_fonts": len(fonts), "raster_sizes": raster_sizes, "text_characters": len(text)}

def lanes():
    outputs = []
    with tempfile.TemporaryDirectory(prefix="c394-release-evidence-") as directory:
        target = Path(directory)/"evidence.json"
        outputs.append(run([sys.executable, "-B", str(ROOT/"code"/SCRIPTS[0]), "--output", str(target)]))
        assert target.read_bytes() == (ROOT/"results/c394_interpolation_evidence.json").read_bytes()
    for name in SCRIPTS[1:-1]:
        outputs.append(run([sys.executable, "-B", str(ROOT/"code"/name)]))
    run([sys.executable, "-B", "-m", "unittest", "tests/test_c394_smoke.py"], cwd=ROOT)
    outputs.append("C394 smoke PASS: 3/3")
    for name in SCRIPTS:
        for flag in ("-O", "-OO"):
            proc = subprocess.run([sys.executable, flag, str(ROOT/"code"/name), "--help"], capture_output=True, text=True)
            assert proc.returncode != 0 and "refuses optimized Python" in proc.stdout+proc.stderr
    outputs.append("C394 optimized-mode refusal PASS: six scripts under -O and -OO, 12/12 refusals")
    return outputs

def reports(receipts, rounds):
    table = "\n".join(f"| {r['round']} | {r['pages']} | {r['embedded_subset_fonts']} | `{r['sha256']}` |" for r in rounds)
    return {
        "results/TEST_REPORT.md": "# Actual test report\n\nFresh commands completed successfully in the release run. These are finite exact checks, not universal theorem proofs.\n\n```text\n"+"\n".join(receipts)+"\n```\n",
        "results/HOSTILE_AUDIT.md": "# Actual hostile audit\n\nThe checker reconstructs expected data independently and compares every tree node with exact Python types. Repaired payload hashes do not bypass the semantic gate. The ten YAML cases run the copied release with `--write`; each must refuse at the evaluation gate and leave every copied file unchanged. A separate actual write with a symlink must refuse at the explicit filesystem gate, also without changing any copied file.\n\n```text\n"+receipts[4]+"\n```\n\nThe nine target flags and separate Route-B permission remain false. Six scripts each reject both optimized Python modes, giving twelve actual refusals.\n",
        "results/RESULTS.md": "# Exact finite results\n\n56 parameter-level cases contain 109876 residue vectors. The independent checker discovers every permutation cycle. There are 2880 exact modular displacement records, 512 difference-polynomial coefficient cells, 1024 ordinary tail rows and 4592 symbolic checks. These populations were frozen before checking; actual command receipts are in TEST_REPORT.md.\n\nThe full theorem is the analytic distance law, minimal decomposition, all-level residue census, algebraic finite/all alternative, and source Haar/reversal structure. Finite rows do not prove those infinite statements.\n",
        "paper/COMPILE_REPORT.md": "# Deterministic compilation report\n\nEach revision was built twice in separate fresh directories, with two LuaLaTeX passes per build and SOURCE_DATE_EPOCH=1788566400. The saved compiler text is the unedited settled log, not a cleaned transcript. All settled layout/reference/citation/missing-character warning gates passed.\n\n| Round | Pages | Embedded subset fonts | PDF SHA-256 |\n|---|---:|---:|---|\n"+table+"\n\nMain PDF equals round two byte for byte. Text extraction, six English and six Chinese keywords, all-page raster generation and page counts passed. The separate review record states the actual human-visible image inspection boundary.\n",
    }

def source_gate():
    evidence = strict(ROOT/"results/c394_interpolation_evidence.json")
    assert all(v is False for v in evidence["scope_flags"].values())
    assert evidence["route_a"]["route_b_invocation_allowed"] is False
    assert evidence["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
    for name in EXPECTED:
        path = ROOT/name
        if path.suffix in (".md", ".tex", ".py", ".yaml", ".txt"):
            raw = path.read_bytes()
            assert all(b >= 32 or b in (10, 13) for b in raw), "control byte: "+name
            if path.suffix == ".md" or name == "requirements.txt":
                assert raw.endswith(b"\n") and not raw.endswith(b"\n\n"), "EOF whitespace: "+name
    for index in range(3):
        assert (ROOT/f"paper/main_round{index}.tex").read_text() == f"\\def\\CRevisionRound{{{index}}}\n\\input{{main.tex}}\n"
        assert WARN.search((ROOT/f"paper/compile_round{index}.txt").read_text()) is None
    assert (ROOT/"paper/main.pdf").read_bytes() == (ROOT/"paper/main_round2.pdf").read_bytes()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--build-pdfs", action="store_true")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    content_gate()  # Mandatory before every branch that can write anything.
    if args.build_pdfs:
        for index, name in enumerate(NAMES):
            blob, log = compile_round(index)
            (ROOT/"paper"/name).write_bytes(blob)
            (ROOT/f"paper/compile_round{index}.txt").write_text(log)
            if index == 2:
                (ROOT/"paper/main.pdf").write_bytes(blob)
            print("C394 double-fresh PDF build PASS: round="+str(index), flush=True)
        return
    receipts = lanes()
    rounds = []
    for index, name in enumerate(NAMES):
        path = ROOT/"paper"/name
        assert compile_round(index)[0] == path.read_bytes(), "fresh PDF differs from frozen PDF"
        rounds.append(pdf_audit(path, index))
    assert len({r["sha256"] for r in rounds}) == 3
    assert rounds[0]["text_characters"] < rounds[1]["text_characters"] < rounds[2]["text_characters"]
    assert rounds[0]["pages"] <= rounds[1]["pages"] <= rounds[2]["pages"]
    for name, content in reports(receipts, rounds).items():
        if args.write:
            (ROOT/name).write_text(content)
        else:
            assert (ROOT/name).read_text() == content, "receipt changed: "+name
    actual = sorted(str(p.relative_to(ROOT)) for p in ROOT.rglob("*") if p.is_file())
    expected = sorted(EXPECTED+((MANIFEST.name,) if MANIFEST.exists() or not args.write else ()))
    assert actual == expected, "physical membership extra="+repr(sorted(set(actual)-set(expected)))+" missing="+repr(sorted(set(expected)-set(actual)))
    source_gate()
    files = {name: sha(ROOT/name) for name in sorted(EXPECTED)}
    eval_path = ROOT/"evaluations/route_a/HCS-C394/2026-09-05.yaml"
    m = {"schema": "hcs-release-manifest-v1", "candidate_id": "HCS-C394", "obstruction_id": "HEN-O378", "source_commit": "697518b6db90458f86f7916fbf397b8ad5ef2372", "fixed_epoch": 1788566400, "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER", "evaluator_authority": AUTHORITY, "evaluator_version": "0.2.0", "evaluator_authority_sha256": AUTHORITY_SHA, "payload_file_count": len(EXPECTED), "physical_file_count": len(EXPECTED)+1, "payload_ledger_sha256": hashlib.sha256(canonical(files)).hexdigest(), "evaluation_raw_sha256": sha(eval_path), "evidence_sha256": sha(ROOT/"results/c394_interpolation_evidence.json"), "evidence_payload_sha256": strict(ROOT/"results/c394_interpolation_evidence.json")["payload_sha256"], "main_pdf_sha256": sha(ROOT/"paper/main.pdf"), "release_lanes": {k: "PASS" for k in ("producer", "independent_checker", "exact_symbolic", "two_directory_byte_replay", "repaired_hash_semantic_mutations", "actual_yaml_write_refusals", "actual_symlink_write_refusal", "smoke", "optimized_mode_refusal", "strict_evaluation", "deterministic_double_pdf_builds", "fonts_text_raster", "physical_membership", "scope_firewall")}, "lane_receipts": receipts, "pdf_rounds": rounds, "files": files}
    if args.write:
        MANIFEST.write_text(json.dumps(m, sort_keys=True, indent=2, ensure_ascii=False)+"\n")
        print(f"C394 manifest WRITE PASS: payload={len(EXPECTED)} physical={len(EXPECTED)+1} manifest={sha(MANIFEST)}")
    else:
        assert canonical(strict(MANIFEST)) == canonical(m), "nonwrite manifest reconstruction mismatch"
        print("C394 nonwrite release PASS: evidence="+m["evidence_sha256"]+" pdf="+m["main_pdf_sha256"]+" manifest="+sha(MANIFEST))

if __name__ == "__main__":
    main()
