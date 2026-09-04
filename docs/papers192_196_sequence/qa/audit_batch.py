#!/usr/bin/env python3
"""Terminal mechanical audit for Route-A papers P192--P196.

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
SEQ = ROOT / "docs" / "papers192_196_sequence"
PAPERS = {
    192: ROOT / "papers" / "192-first-collision-hurwitz",
    193: ROOT / "papers" / "193-mutual-best-block-refinement",
    194: ROOT / "papers" / "194-least-raising-crystal-words",
    195: ROOT / "papers" / "195-odd-side-least-neighbor-trees",
    196: ROOT / "papers" / "196-cyclic-godel-implication",
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
        check(not rel.is_absolute() and ".." not in rel.parts,
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
        r"(?im)^(?:(?:exact_)?assertions|checks)\s*=\s*([0-9]+)\s*$", expected
    )
    check(len(values) == 1, f"{label} must disclose one assertion/check total")
    check(re.search(
        r"(?im)^(?:status|result|verdict)\s*=\s*(?:PASS(?:_INTERNAL)?|PROVABLE_AS_STATED)\s*$",
        expected,
    ) is not None, f"{label} lacks an accepted status")
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
    names = parse_manifest(directory)
    payload = {path.name for path in directory.iterdir()
               if path.is_file() and path.name != "SHA256SUMS"}
    check(names == payload, f"P{number}-{suffix} manifest coverage mismatch")
    verifiers = list(directory.glob("verify*.py"))
    canonicals = list(directory.glob("CANONICAL.txt"))
    deltas = list(directory.glob("DELTA.md"))
    reviews = list(directory.glob("*REVIEW*.md"))
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
    for severity in ("critical", "major", "minor"):
        check(severity_zero(canonical_text, severity),
              f"P{number}-{suffix} nonzero/absent {severity} census")
    review_text = reviews[0].read_text(encoding="utf-8")
    delta_text = deltas[0].read_text(encoding="utf-8")
    check("HOLD_EXTERNAL" in review_text.upper(), f"P{number}-{suffix} lacks hold")
    check(re.search(r"(?i)\b(?:PASS|ACCEPT|ACCEPTED)\b", delta_text) is not None,
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
    package_names = parse_manifest(directory)
    check(set(REQUIRED_PAPER) - {"SHA256SUMS"} <= package_names,
          f"P{number} package manifest misses required payload")
    parse_manifest(directory / "qa_final")
    for name in ("main_round0_original.pdf", "main_round1.pdf", "main_round2.pdf"):
        pdf_gate(number, directory / name)
    pages = cold_gate(number, directory)
    citations = citation_gate(number, directory)
    assertions = replay(*AUTHOR[number], f"P{number} author")
    return pages, citations, assertions


def main() -> None:
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
    check((SEQ / "CANONICAL_PDF_MANIFEST.sha256").is_file(),
          "missing canonical PDF manifest")
    check((SEQ / "PACKAGE_MANIFESTS.sha256").is_file(),
          "missing package-manifest manifest")
    print("route A P192-P196 terminal artifact audit")
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
    print("external_status=OWNER_RED_AMBER_P192;OWNER_AMBER_P193_P196;HOLD_EXTERNAL")
    print(f"audit_assertions={ASSERTIONS}")
    print("status=PASS")


if __name__ == "__main__":
    main()
