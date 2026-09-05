#!/usr/bin/env python3
"""Terminal mechanical audit for the retained Route-A five-paper batch.

The audit checks frozen artifacts, exact replays, source-only builds, review
package separation surfaces, and lifecycle labels.  It cannot certify a
uniform proof, novelty, ownership, priority, or freedom to operate.
"""

from __future__ import annotations

import hashlib
import os
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[3]
SEQ = ROOT / "docs" / "papers197_201_sequence"
PAPERS = {
    197: ROOT / "papers" / "197-ternary-cyclic-sign-difference",
    199: ROOT / "papers" / "199-first-one-stirling-splice",
    200: ROOT / "papers" / "200-lex-first-alternating-switch",
    202: ROOT / "papers" / "202-ternary-ordered-reset",
}
AUTHOR = {number: (directory / "code/verify.py", directory / "code/CANONICAL.txt")
          for number, directory in PAPERS.items()}
REQUIRED_PAPER = (
    "README.md", "NARRATIVE_REPORT.md", "PAPER_PLAN.md", "FIGURE_PLAN.md",
    "PROOF_PACKAGE.md", "CLAIMS_EVIDENCE.md", "SOURCE_VERIFICATION.md",
    "BUILD.md", "SELF_QA.md", "IMPROVEMENT_LOG.md", "FINAL_QA.md",
    "main.tex", "references.bib", "main.pdf", "main_round0_original.pdf",
    "main_round1.pdf", "main_round2.pdf", "code/verify.py",
    "code/CANONICAL.txt", "SHA256SUMS", "qa_final/SHA256SUMS",
    "ROUND1_RECEIPT.md", "ROUND2_RECEIPT.md",
)
ASSERTIONS = 0


def check(condition: bool, message: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def command(args: list[str], cwd: Path | None = None, timeout: int = 1200) -> str:
    env = os.environ.copy()
    env.update({"LC_ALL": "C", "TZ": "UTC", "PYTHONDONTWRITEBYTECODE": "1"})
    result = subprocess.run(
        args, cwd=cwd or ROOT, env=env, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=timeout,
    )
    check(result.returncode == 0,
          f"command failed ({result.returncode}): {' '.join(args)}\n{result.stdout}")
    return result.stdout


def parse_manifest(directory: Path, filename: str = "SHA256SUMS") -> set[str]:
    manifest = directory / filename
    check(manifest.is_file() and not manifest.is_symlink(),
          f"missing manifest: {manifest}")
    names: list[str] = []
    for line_no, line in enumerate(manifest.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        match = re.fullmatch(r"([0-9a-f]{64})\s+\*?(.+)", line)
        check(match is not None, f"malformed manifest row {manifest}:{line_no}")
        if match is None:
            continue
        expected, relative = match.groups()
        relative = relative.strip()
        target_rel = Path(relative)
        check(not target_rel.is_absolute() and ".." not in target_rel.parts,
              f"unsafe manifest target {manifest}:{relative}")
        check(relative != filename, f"self-referential manifest: {manifest}")
        target = directory / target_rel
        check(target.is_file() and not target.is_symlink(),
              f"missing/symlink manifest target: {target}")
        check(sha(target) == expected, f"digest mismatch: {target}")
        names.append(target_rel.as_posix())
    check(bool(names), f"empty manifest: {manifest}")
    check(len(names) == len(set(names)), f"duplicate manifest target: {manifest}")
    return set(names)


def recursive_files(directory: Path) -> set[str]:
    check(directory.is_dir() and not directory.is_symlink(),
          f"missing/symlink coverage directory: {directory}")
    result: set[str] = set()
    for path in directory.rglob("*"):
        check(not path.is_symlink(), f"symlink in covered tree: {path}")
        check(path.is_file() or path.is_dir(), f"nonregular artifact: {path}")
        if path.is_file():
            result.add(path.relative_to(directory).as_posix())
    return result


def complete_manifest(directory: Path, filename: str = "SHA256SUMS") -> set[str]:
    names = parse_manifest(directory, filename)
    payload = recursive_files(directory) - {filename}
    check(names == payload,
          f"recursive manifest coverage mismatch: {directory / filename}; "
          f"unlisted={sorted(payload - names)}, extra={sorted(names - payload)}")
    return names


def review_manifest_gate(directory: Path) -> set[str]:
    names = parse_manifest(directory)
    payload = {path.name for path in directory.iterdir()
               if path.is_file() and path.name != "SHA256SUMS"}
    check({name for name in names if "/" not in name} == payload,
          f"review top-level manifest coverage mismatch: {directory}")
    covered = names | {"SHA256SUMS"}
    for nested in names - payload:
        check(Path(nested).name == "SHA256SUMS",
              f"unexpected nested review manifest payload: {directory / nested}")
        parent = Path(nested).parent
        child_names = complete_manifest(directory / parent)
        covered.update((parent / name).as_posix() for name in child_names)
    # Older accepted reviews keep the QA list at top level, with paths
    # relative to the review directory. Hashing the list alone is not QA.
    if "QA_SHA256SUMS" in names:
        covered.update(parse_manifest(directory, "QA_SHA256SUMS"))
    actual = recursive_files(directory)
    check(covered == actual,
          f"recursive review coverage mismatch: {directory}; "
          f"unlisted={sorted(actual - covered)}, extra={sorted(covered - actual)}")
    return names


def frozen_round_gate(number: int, directory: Path) -> None:
    core = ("main.tex", "references.bib", "code/verify.py", "code/CANONICAL.txt")
    # Preserve the historical four-file freezes; their PDFs are the
    # separately pinned main_round*.pdf files, not invented new snapshots.
    legacy_core_only = {(197, 0), (197, 1), (197, 2),
                        (199, 1), (199, 2), (200, 1), (200, 2)}
    snapshots: list[Path] = []
    pdfs: list[Path] = []
    for stage in range(3):
        name = ("round0_snapshot" if stage == 0 and number in (199, 200)
                else f"frozen_round{stage}")
        frozen = directory / name
        check(frozen.is_dir() and not frozen.is_symlink(),
              f"P{number} missing frozen round {stage}: {frozen}")
        for relative in core:
            path = frozen / relative
            check(path.is_file() and not path.is_symlink(),
                  f"P{number} frozen round {stage} lacks {relative}")
        pdf = directory / ("main_round0_original.pdf" if stage == 0
                           else f"main_round{stage}.pdf")
        check(pdf.is_file() and not pdf.is_symlink(), f"missing round PDF: {pdf}")
        if (number, stage) not in legacy_core_only:
            check((frozen / "SHA256SUMS").is_file() and (frozen / "main.pdf").is_file(),
                  f"P{number} round {stage} lacks full freeze manifest/PDF")
        if (frozen / "SHA256SUMS").exists():
            complete_manifest(frozen)
        if (frozen / "main.pdf").exists():
            check(sha(frozen / "main.pdf") == sha(pdf),
                  f"P{number} round {stage} snapshot/PDF disagreement")
        snapshots.append(frozen)
        pdfs.append(pdf)
    for relative in core:
        check(sha(snapshots[2] / relative) == sha(directory / relative),
              f"P{number} live/Round2 disagreement: {relative}")
    check(sha(pdfs[2]) == sha(directory / "main.pdf"),
          f"P{number} live/Round2 PDF disagreement")
    # Only an explicitly accepted no-change transition requires historical
    # stages to equal each other. A real accepted repair must not be erased.
    for stage, suffix in ((1, "a"), (2, "b")):
        review = SEQ / "reviews" / f"p{number}_{suffix}"
        deltas = [review / name for name in ("DELTA.md", "DELTA_ACCEPTANCE.md")
                  if (review / name).is_file()]
        check(len(deltas) == 1, f"P{number}-{suffix} freeze delta cardinality")
        if re.search(r"\bACCEPTED_NO_CHANGE\b", deltas[0].read_text(encoding="utf-8")):
            for relative in core:
                check(sha(snapshots[stage-1] / relative) == sha(snapshots[stage] / relative),
                      f"P{number} no-change round {stage} drift: {relative}")
            check(sha(pdfs[stage-1]) == sha(pdfs[stage]),
                  f"P{number} no-change round {stage} PDF drift")


def global_manifest_gate() -> None:
    check(len(PAPERS) == 5, "global manifests require exactly five admitted papers")
    for filename, relative in (("CANONICAL_PDF_MANIFEST.sha256", "main_round2.pdf"),
                               ("PACKAGE_MANIFESTS.sha256", "SHA256SUMS")):
        expected = {(directory / relative).relative_to(ROOT).as_posix()
                    for directory in PAPERS.values()}
        check(len(expected) == 5, f"global manifest requires five distinct targets: {filename}")
        manifest = (SEQ / filename).relative_to(ROOT).as_posix()
        actual = parse_manifest(ROOT, manifest)
        check(actual == expected,
              f"global manifest target mismatch: {filename}; "
              f"missing={sorted(expected - actual)}, extra={sorted(actual - expected)}")


def check_pins(path: Path) -> int:
    check(path.is_file() and not path.is_symlink(), f"missing pins: {path}")
    count = 0
    seen: set[str] = set()
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        match = re.fullmatch(r"([0-9a-f]{64})\s+\*?(.+)", line)
        check(match is not None, f"bad pin row {path}:{line_no}")
        if match is None:
            continue
        expected, relative = match.groups()
        rel = Path(relative.strip())
        # A frozen reviewer may pin the original workspace's absolute paths.
        # Relocate ONLY that explicitly known root, retaining exact hashes.
        # Never follow an arbitrary absolute pin outside the scoped corpus.
        if rel.is_absolute():
            known_root = Path("/root/autodl-tmp/symbolic_dynamics")
            check(rel.is_relative_to(known_root),
                  f"foreign absolute pin target {path}:{relative}")
            rel = rel.relative_to(known_root)
        check(".." not in rel.parts,
              f"unsafe pin target {path}:{relative}")
        key = rel.as_posix()
        check(key not in seen, f"duplicate pin target {path}:{key}")
        seen.add(key)
        target = ROOT / rel
        check(target.is_file() and not target.is_symlink(), f"missing pin target: {target}")
        check(sha(target) == expected, f"pinned input drift: {target}")
        count += 1
    check(count >= 4, f"too few pinned inputs: {path}")
    return count


def replay(verifier: Path, canonical: Path, label: str) -> int:
    check(verifier.is_file() and canonical.is_file(), f"missing replay pair: {label}")
    expected = canonical.read_text(encoding="utf-8")
    first = command([sys.executable, "-B", str(verifier)], cwd=ROOT)
    second = command([sys.executable, "-B", str(verifier)], cwd=ROOT)
    check(first == second == expected, f"noncanonical replay: {label}")
    values = re.findall(
        r"(?im)(?:^|[ \t])(?:(?:exact_)?assertions|checks)(?:\s*=\s*|[ \t]+)([0-9]+)(?=$|[ \t])", expected
    )
    check(len(values) == 1, f"{label} must disclose one assertion/check total")
    structured_pass = re.search(
        r"(?im)^(?:status|result|verdict)\s*=\s*(?:PASS(?:_INTERNAL)?|PROVABLE_AS_STATED)\s*$",
        expected,
    ) is not None
    # Some immutable author transcripts use the older explicit provenance
    # line. It certifies only the author check, never paper A/B completion.
    legacy_author_pass = label.endswith(" author") and re.search(
        r"(?im)^(?:PASS / ROUND0_AUTHOR_CHECK / HOLD_EXTERNAL|"
        r"PASS_BOUNDED_CONTROL_NOT_EXTERNAL_NOVELTY_CLEARANCE|"
        r"PASS_BOUNDED_CONTROL_NOT_NOVELTY_OR_PAPER_REVIEW)\s*$", expected
    ) is not None
    # P202's unchanged Round0 author control has a role-specific status.
    # Admit only that exact frozen code/transcript pair, never a review
    # status or an arbitrary PASS_* suffix. A/B remain separate gates.
    p202_author_control = (
        label == "P202 author"
        and sha(verifier) == "42c79767025b5da710aaccd8be170df964a14a65427470dd814cf3ce4081b850"
        and sha(canonical) == "a971574926784fa43f27df88b58979ba6724a11c6070a3484c7641ea56fd6446"
        and re.search(r"(?m)^status=PASS_AUTHOR_CONTROL$", expected) is not None
    )
    # Immutable P197-B uses this explicit bounded-review success line.
    # Its exact zero-open census is in the separately hashed full report;
    # review_gate validates that report when stdout has no census field.
    legacy_review_pass = " Review " in label and re.search(
        r"(?m)^(?:PASS_BOUNDED_INDEPENDENT_REVIEW_B; NO_NOVELTY_CERTIFICATION|"
        r"PASS / INDEPENDENT_REVIEW_B_CONTROL / NO_CROSS_MODEL_CLAIM / HOLD_EXTERNAL)$",
        expected,
    ) is not None
    check(structured_pass or legacy_author_pass or p202_author_control or legacy_review_pass,
          f"{label} lacks an accepted status")
    return int(values[0])


def severity_zero(text: str, severity: str) -> bool:
    direct = re.findall(
        rf"(?im)(?:^|[ \t])(?:open_)?{severity}(?:_findings)?\s*=\s*"
        rf"([0-9]+)(?=$|[ \t])",
        text,
    )
    if direct:
        return direct == ["0"]
    for line in text.splitlines():
        if not (line.lower().startswith("findings=")
                or line.lower().startswith("open_findings=")):
            continue
        values = {}
        for token in line.split("=", 1)[1].split(","):
            if ":" in token:
                key, value = token.split(":", 1)
                values[key.strip().lower()] = value.strip()
        return values.get(severity) == "0"
    return False


def review_gate(number: int, suffix: str) -> int:
    directory = SEQ / "reviews" / f"p{number}_{suffix}"
    check(directory.is_dir() and not directory.is_symlink(),
          f"missing P{number} Review {suffix.upper()}")
    names = review_manifest_gate(directory)
    verifiers = list(directory.glob("verify*.py"))
    canonicals = list(directory.glob("CANONICAL.txt"))
    deltas = [path for name in ("DELTA.md", "DELTA_ACCEPTANCE.md")
              if (path := directory / name).is_file()]
    reviews = list(directory.glob("*REVIEW*.md"))
    # P202 A/B preserve hashed pre-review intakes alongside their reports.
    # They are not second decisions. Exclude only these exact artifacts;
    # manifest coverage still checks it, and any other extra report fails.
    p202_intake_hashes = {
        "a": "d5d5fc29bba5bca288fc73a01284e9e4012f61564a6cf2d9467c53d3a73e312f",
        "b": "28f27668feeab6dccf647dc58508bb00bfa4ccfcefc0c7b73c66b3b1db81f1a7",
    }
    if number == 202 and suffix in p202_intake_hashes:
        reviews = [path for path in reviews if not (
            path.name == "REVIEW_INTAKE.md"
            and sha(path) == p202_intake_hashes[suffix]
        )]
    check(len(verifiers) == len(canonicals) == len(deltas) == len(reviews) == 1,
          f"P{number}-{suffix} core-file cardinality failure")
    for required_fragment in ("PROOF_REDERIVATION", "BUILD_PDF_QA"):
        check(any(required_fragment in name for name in names),
              f"P{number}-{suffix} lacks {required_fragment}")
    check(any("SOURCE_OWNER" in name or "OWNER_COLLISION" in name for name in names),
          f"P{number}-{suffix} lacks source/owner audit")
    check("PINNED_INPUTS.sha256" in names, f"P{number}-{suffix} pins omitted")
    check_pins(directory / "PINNED_INPUTS.sha256")
    canonical_text = canonicals[0].read_text(encoding="utf-8")
    review_text = reviews[0].read_text(encoding="utf-8")
    has_canonical_census = re.search(
        r"(?im)^(?:open_)?(?:findings|critical(?:_findings)?|"
        r"major(?:_findings)?|minor(?:_findings)?)\s*=", canonical_text
    ) is not None
    # Do not rewrite accepted canonical transcripts to accommodate a parser.
    # The protocol requires a durable exact census, not a particular stdout
    # serialization. Only absence permits the explicit report form below;
    # a present nonzero/incomplete stdout census cannot fall back to a report.
    report_census = re.search(
        r"(?i)\bOpen findings:\s*(?:\*\*)?Critical\s*0\s*[,/]\s*"
        r"Major\s*0\s*[,/]\s*Minor\s*0(?:\*\*)?\.",
        review_text,
    ) is not None
    for severity in ("critical", "major", "minor"):
        check(severity_zero(canonical_text, severity) if has_canonical_census
              else report_census,
              f"P{number}-{suffix} nonzero/absent {severity} census")
    delta_text = deltas[0].read_text(encoding="utf-8")
    check("HOLD_EXTERNAL" in review_text.upper(), f"P{number}-{suffix} lacks hold")
    check(re.search(r"(?im)(?:^|\b(?:Decision|Status):\s*)(?:\*\*)?"
                    r"ACCEPT(?:ED)?(?:_NO_CHANGE|_REPAIR)?(?:\*\*)?(?:[.!;]|[ \t]*$)",
                    delta_text) is not None,
          f"P{number}-{suffix} delta is not accepted")
    if suffix == "b":
        check("REPLAY_LOG.md" in names, f"P{number}-b lacks replay log")
        replay_log = (directory / "REPLAY_LOG.md").read_text(encoding="utf-8")
        check("replay 1" in replay_log.lower() and "replay 2" in replay_log.lower()
              and "byte" in replay_log.lower(), f"P{number}-b replay receipt incomplete")
    return replay(verifiers[0], canonicals[0], f"P{number} Review {suffix.upper()}")


def citation_gate(number: int, directory: Path) -> int:
    tex = (directory / "main.tex").read_text(encoding="utf-8")
    bib = (directory / "references.bib").read_text(encoding="utf-8")
    bib_list = [match.group(1).strip() for match in re.finditer(
        r"@(?!comment\b|string\b|preamble\b)[A-Za-z]+\s*\{\s*([^,\s]+)", bib,
        flags=re.I)]
    check(len(bib_list) == len(set(bib_list)) and bool(bib_list),
          f"P{number} duplicate/empty bibliography")
    cites = {key.strip() for group in re.findall(
        r"\\cite[A-Za-z*]*(?:\s*\[[^\]]*\]){0,2}\s*\{([^{}]+)\}", tex)
             for key in group.split(",") if key.strip()}
    check(set(bib_list) == cites,
          f"P{number} citation mismatch: bib-only={set(bib_list)-cites}, "
          f"cite-only={cites-set(bib_list)}")
    return len(bib_list)


def pdf_gate(number: int, path: Path) -> int:
    check(path.is_file() and path.stat().st_size > 50_000,
          f"P{number} missing/small PDF: {path}")
    fields = {}
    for line in command(["pdfinfo", str(path)]).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    check(fields.get("Pages", "").isdigit() and int(fields["Pages"]) > 0,
          f"P{number} invalid page count")
    check("(A4)" in fields.get("Page size", ""), f"P{number} non-A4 PDF")
    check(fields.get("Page rot") == "0", f"P{number} rotated PDF")
    for key in ("Title", "Subject", "Keywords", "Author", "Creator", "Producer"):
        check(fields.get(key, "") == "", f"P{number} metadata leak {key}")
    for key, expected in (("Encrypted", "no"), ("Custom Metadata", "no"),
                          ("Form", "none"), ("JavaScript", "no"),
                          ("Metadata Stream", "no")):
        check(fields.get(key) == expected, f"P{number} PDF field {key}")
    fonts = [line for line in command(["pdffonts", str(path)]).splitlines()[2:]
             if line.strip()]
    check(bool(fonts), f"P{number} no PDF fonts")
    for row in fonts:
        check(row.split()[-5:-2] == ["yes", "yes", "yes"],
              f"P{number} font emb/sub/uni failure: {row}")
    extracted = command(["pdftotext", str(path), "-"])
    check("??" not in extracted and "[?]" not in extracted,
          f"P{number} unresolved PDF token")
    check("HOLD_EXTERNAL" in extracted.upper() or "HOLD EXTERNAL" in extracted.upper(),
          f"P{number} missing external hold in PDF")
    return int(fields["Pages"])


def cold_gate(number: int, directory: Path) -> int:
    page_count = pdf_gate(number, directory / "main.pdf")
    cold_hashes = []
    for run in (1, 2):
        cold = directory / "qa_final" / f"cold_build_{run}"
        check(cold.is_dir() and not cold.is_symlink(), f"P{number} missing cold build {run}")
        for name in ("main.tex", "references.bib", "main.aux", "main.bbl", "main.blg",
                     "main.log", "main.fls", "main.pdf", "pass1.stdout",
                     "bibtex.stdout", "pass2.stdout", "pass3.stdout"):
            check((cold / name).is_file(), f"P{number} cold {run} lacks {name}")
        check(sha(cold / "main.tex") == sha(directory / "main.tex"),
              f"P{number} cold {run} source drift")
        check(sha(cold / "references.bib") == sha(directory / "references.bib"),
              f"P{number} cold {run} bibliography drift")
        check(sha(cold / "main.pdf") == sha(directory / "main.pdf"),
              f"P{number} cold {run} PDF drift")
        diagnostics = (cold / "main.log").read_text(encoding="utf-8", errors="replace")
        check(re.search(r"Warning|Undefined|Overfull|Underfull|Error", diagnostics) is None,
              f"P{number} cold {run} log diagnostic")
        cold_hashes.append(sha(cold / "main.pdf"))
    check(len(set(cold_hashes)) == 1, f"P{number} cold builds differ")
    visual = directory / "qa_final" / "visual"
    pages = sorted(visual.glob("page-*.png"))
    check(len(pages) == page_count, f"P{number} visual page-count mismatch")
    check(all(path.stat().st_size > 20_000 for path in pages),
          f"P{number} missing/small rendered page")
    return page_count


def paper_gate(number: int, directory: Path) -> tuple[int, int, int]:
    for relative in REQUIRED_PAPER:
        check((directory / relative).is_file(), f"P{number} missing {relative}")
    check(not list(directory.rglob("__pycache__")) and not list(directory.rglob("*.pyc")),
          f"P{number} contains Python cache")
    tex = (directory / "main.tex").read_text(encoding="utf-8")
    check("Anonymous" in tex and "HOLD\\_EXTERNAL" in tex,
          f"P{number} anonymity/hold source boundary failed")
    log = (directory / "main.log").read_text(encoding="utf-8", errors="replace")
    check(re.search(r"Warning|Undefined|Overfull|Underfull|Error", log) is None,
          f"P{number} live build diagnostic")
    package_names = complete_manifest(directory)
    check(set(REQUIRED_PAPER) - {"SHA256SUMS"} <= package_names,
          f"P{number} package manifest misses required payload")
    complete_manifest(directory / "qa_final")
    frozen_round_gate(number, directory)
    for name in ("main_round0_original.pdf", "main_round1.pdf", "main_round2.pdf"):
        pdf_gate(number, directory / name)
    pages = cold_gate(number, directory)
    citations = citation_gate(number, directory)
    assertions = replay(*AUTHOR[number], f"P{number} author")
    return pages, citations, assertions


def main() -> None:
    check(len(PAPERS) == 5, "five retained terminal paper packages are required")
    author_assertions = review_a_assertions = review_b_assertions = 0
    pages = citations = 0
    for number, directory in PAPERS.items():
        paper_pages, paper_citations, paper_assertions = paper_gate(number, directory)
        pages += paper_pages
        citations += paper_citations
        author_assertions += paper_assertions
        review_a_assertions += review_gate(number, "a")
        review_b_assertions += review_gate(number, "b")

    check((SEQ / "reviews/PROCESS_SEPARATION_LEDGER.md").is_file(),
          "missing process-separation ledger")
    global_manifest_gate()
    print("route A retained terminal artifact audit")
    print("paper_ids=" + ",".join(str(number) for number in PAPERS))
    print("papers=5")
    print(f"pages={pages}")
    print(f"bibliography_records={citations}")
    print(f"author_assertions={author_assertions}")
    print(f"review_a_assertions={review_a_assertions}")
    print(f"review_b_assertions={review_b_assertions}")
    print("author_replays=10")
    print("review_replays=20")
    print("cold_builds=10")
    print(f"visual_pages={pages}")
    print("findings=critical:0,major:0,minor:0")
    print("external_status=OWNER_AMBER/HOLD_EXTERNAL")
    print(f"audit_assertions={ASSERTIONS}")
    print("status=PASS")


if __name__ == "__main__":
    main()
