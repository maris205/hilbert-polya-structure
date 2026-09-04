#!/usr/bin/env python3
"""Terminal artifact audit for Route-A papers P187--P191.

This program checks byte-level provenance, build mechanics, review-package
replays, and declared lifecycle boundaries. It cannot certify a uniform proof,
novelty, priority, ownership, or freedom to operate.
"""

from __future__ import annotations

import hashlib
import os
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[3]
SEQ = ROOT / "docs" / "papers187_191_sequence"
PAPERS = {
    187: ROOT / "papers" / "187-cyclic-divisor-quotient",
    188: ROOT / "papers" / "188-self-cardinality-truncation",
    189: ROOT / "papers" / "189-transpose-row-compression",
    190: ROOT / "papers" / "190-brandt-sandwich-erosion",
    191: ROOT / "papers" / "191-prefix-divisibility-cuts",
}
AUTHOR = {
    187: ("code/verify_p187.py", "code/CANONICAL.txt"),
    188: ("verify_p188.py", "CANONICAL.txt"),
    189: ("code/verify_p189.py", "code/CANONICAL.txt"),
    190: ("code/verify_p190.py", "code/CANONICAL.txt"),
    191: ("code/verify.py", "code/CANONICAL.txt"),
}
REVIEWS = {
    187: (SEQ / "reviews/p187_a", SEQ / "reviews/p187_b"),
    188: (SEQ / "reviews/p188_a", SEQ / "reviews/p188_b"),
    189: (
        PAPERS[189] / "reviews/round1/reviewer_a",
        PAPERS[189] / "reviews/round2/reviewer_b",
    ),
    190: (SEQ / "reviews/p190_a", SEQ / "reviews/p190_b"),
    191: (SEQ / "reviews/p191_a", SEQ / "reviews/p191_b"),
}
REQUIRED = (
    "README.md", "BUILD.md", "CLAIMS_EVIDENCE.md", "FIGURE_PLAN.md",
    "IMPROVEMENT_LOG.md", "NARRATIVE_REPORT.md", "PAPER_PLAN.md",
    "PROOF_PACKAGE.md", "SELF_QA.md", "SOURCE_VERIFICATION.md",
    "FINAL_QA.md", "main.tex", "references.bib", "main.pdf",
    "main_round0_original.pdf", "main_round1.pdf", "main_round2.pdf",
    "SHA256SUMS",
)
ROUND_PDFS = (
    "main_round0_original.pdf", "main_round1.pdf", "main_round2.pdf", "main.pdf"
)
ASSERTIONS = 0


def check(condition: bool, message: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def command(args: list[str], cwd: Path | None = None, timeout: int = 900) -> str:
    env = os.environ.copy()
    env.update({"LC_ALL": "C", "TZ": "UTC", "PYTHONDONTWRITEBYTECODE": "1"})
    result = subprocess.run(
        args, cwd=cwd or ROOT, env=env, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=timeout,
    )
    check(result.returncode == 0,
          f"command failed ({result.returncode}): {' '.join(args)}\n{result.stdout}")
    return result.stdout


def manifest(directory: Path) -> set[str]:
    path = directory / "SHA256SUMS"
    check(path.is_file(), f"missing manifest: {path}")
    names: list[str] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        match = re.fullmatch(r"([0-9a-f]{64})\s+\*?(.+)", line)
        check(match is not None, f"bad manifest row {path}:{line_no}")
        if match is None:
            continue
        expected, relative = match.groups()
        relative = relative.strip()
        target_rel = Path(relative)
        check(not target_rel.is_absolute() and ".." not in target_rel.parts,
              f"unsafe manifest path: {path}:{relative}")
        check(relative != "SHA256SUMS", f"self-referential manifest: {path}")
        target = directory / target_rel
        check(target.is_file(), f"manifest target missing: {target}")
        check(sha(target) == expected, f"manifest digest mismatch: {target}")
        names.append(relative)
    check(bool(names), f"empty manifest: {path}")
    check(len(names) == len(set(names)), f"duplicate manifest target: {path}")
    return set(names)


def citation_gate(number: int, tex: str, bib: str) -> int:
    bib_keys = {
        match.group(1).strip()
        for match in re.finditer(
            r"@(?!comment\b|string\b|preamble\b)[A-Za-z]+\s*\{\s*([^,\s]+)",
            bib, flags=re.I,
        )
    }
    cite_keys = {
        key.strip()
        for group in re.findall(
            r"\\cite[A-Za-z*]*(?:\s*\[[^\]]*\]){0,2}\s*\{([^{}]+)\}", tex
        )
        for key in group.split(",") if key.strip()
    }
    check(bool(bib_keys), f"P{number} has no bibliography records")
    check(bib_keys == cite_keys,
          f"P{number} citation mismatch: bib_only={bib_keys-cite_keys}, "
          f"cite_only={cite_keys-bib_keys}")
    return len(bib_keys)


def pdf_gate(number: int, path: Path) -> int:
    check(path.is_file() and path.stat().st_size > 50_000,
          f"P{number} missing/small PDF: {path.name}")
    raw = command(["pdfinfo", str(path)])
    fields = {}
    for line in raw.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    check(fields.get("Pages", "").isdigit(), f"P{number} bad page count")
    check("(A4)" in fields.get("Page size", ""), f"P{number} non-A4 PDF")
    check(fields.get("Page rot") == "0", f"P{number} rotated PDF")
    for key in ("Title", "Subject", "Keywords", "Author", "Creator", "Producer"):
        check(key in fields and fields[key] == "",
              f"P{number} identity metadata {key}: {fields.get(key)!r}")
    check(fields.get("Encrypted") == "no", f"P{number} encrypted PDF")
    check(fields.get("JavaScript") == "no", f"P{number} JavaScript PDF")
    check(fields.get("Metadata Stream") == "no", f"P{number} metadata stream")

    font_lines = command(["pdffonts", str(path)]).splitlines()[2:]
    rows = [line for line in font_lines if line.strip()]
    check(bool(rows), f"P{number} PDF has no fonts")
    for row in rows:
        columns = row.split()
        check(columns[-5:-2] == ["yes", "yes", "yes"],
              f"P{number} font emb/sub/uni failure: {row}")
    text = command(["pdftotext", str(path), "-"])
    check("??" not in text and "[?]" not in text,
          f"P{number} unresolved PDF token")
    check("HOLD_EXTERNAL" in text.upper() or "HOLD EXTERNAL" in text.upper(),
          f"P{number} PDF lacks HOLD_EXTERNAL")
    return int(fields["Pages"])


def replay(verifier: Path, canonical: Path, label: str) -> None:
    check(verifier.is_file(), f"missing {label} verifier")
    check(canonical.is_file(), f"missing {label} canonical")
    output = command([sys.executable, "-B", str(verifier)], cwd=ROOT)
    check(output.encode("utf-8") == canonical.read_bytes(),
          f"{label} canonical replay mismatch")


def review_gate(number: int, directory: Path, label: str) -> int:
    check(directory.is_dir() and not directory.is_symlink(),
          f"P{number} missing {label} review dir: {directory}")
    names = manifest(directory)
    verifiers = list(directory.glob("verify*.py"))
    canonicals = list(directory.glob("CANONICAL.txt"))
    deltas = list(directory.glob("*DELTA*.md"))
    if not deltas:
        deltas = list(directory.glob("DELTA.md"))
    reports = [path for path in directory.glob("*.md") if "REVIEW" in path.name]
    check(len(verifiers) == len(canonicals) == len(deltas) == 1,
          f"P{number} {label} package cardinality failure")
    check(bool(reports), f"P{number} {label} lacks review report")
    verifier, canonical, delta = verifiers[0], canonicals[0], deltas[0]
    check({verifier.name, canonical.name, delta.name} <= names,
          f"P{number} {label} manifest omits core files")
    replay(verifier, canonical, f"P{number} {label}")
    canonical_text = canonical.read_text(encoding="utf-8")
    for severity in ("critical", "major", "minor"):
        patterns = (
            rf"(?im)^{severity}(?:_findings)?\s*=\s*0\s*$",
            rf"(?im)^findings=.*{severity}:0",
        )
        check(any(re.search(pattern, canonical_text) for pattern in patterns),
              f"P{number} {label} nonzero/absent {severity} census")
    check(re.search(r"(?im)^(?:verdict|status)\s*=\s*.*PASS", canonical_text) is not None,
          f"P{number} {label} canonical lacks PASS")
    report_text = "\n".join(path.read_text(encoding="utf-8") for path in reports)
    delta_text = delta.read_text(encoding="utf-8")
    check("HOLD_EXTERNAL" in report_text.upper(), f"P{number} {label} lacks hold")
    check(re.search(r"-\s*\[\s\]", delta_text) is None,
          f"P{number} {label} has unchecked delta box")
    check(re.search(r"(?i)\b(?:PASS|ACCEPT|ACCEPTED)\b", delta_text) is not None,
          f"P{number} {label} delta lacks acceptance")
    return 1


def cold_build_gate(number: int, directory: Path) -> None:
    live = directory / "main.pdf"
    seen: set[tuple[int, int]] = set()
    for name in ("cold_build_1", "cold_build_2"):
        cold = directory / "qa_final" / name
        check(cold.is_dir() and not cold.is_symlink(),
              f"P{number} missing physical {name}")
        for required in ("main.tex", "references.bib", "main.aux", "main.bbl",
                         "main.blg", "main.log", "main.pdf"):
            target = cold / required
            check(target.is_file() and not target.is_symlink(),
                  f"P{number} {name} missing/symlink {required}")
        check((cold / "main.tex").read_bytes() == (directory / "main.tex").read_bytes(),
              f"P{number} {name} source drift")
        check((cold / "references.bib").read_bytes()
              == (directory / "references.bib").read_bytes(),
              f"P{number} {name} bibliography drift")
        inputs = {
            path.relative_to(cold).as_posix()
            for path in cold.rglob("*")
            if path.is_file() and path.suffix.lower() in {".tex", ".bib", ".sty", ".cls", ".bst"}
        }
        check(inputs == {"main.tex", "references.bib"},
              f"P{number} {name} not source-only: {sorted(inputs)}")
        check((cold / "main.pdf").read_bytes() == live.read_bytes(),
              f"P{number} {name} PDF differs from live")
        stat = (cold / "main.pdf").stat()
        seen.add((stat.st_dev, stat.st_ino))
    check(len(seen) == 2, f"P{number} cold PDFs alias/hardlink")


def paper_gate(number: int, directory: Path) -> tuple[int, int]:
    for relative in REQUIRED:
        check((directory / relative).is_file(), f"P{number} missing {relative}")
    tex = (directory / "main.tex").read_text(encoding="utf-8")
    bib = (directory / "references.bib").read_text(encoding="utf-8")
    check(re.search(r"\\author\s*\{\s*Anonymous\s*\}", tex) is not None,
          f"P{number} nonanonymous manuscript")
    for token in (r"\email{", r"\address{", r"\affiliation{", r"\institute{"):
        check(token not in tex, f"P{number} anonymity token: {token}")
    for token in (r"\pdfinfoomitdate=1", r"\pdftrailerid{}", r"\pdfsuppressptexinfo=15"):
        check(token in tex, f"P{number} missing deterministic control: {token}")
    check(re.search(r"(?i)\b(?:TODO|TBD|VERIFY|REPLACE_ME)\b", tex) is None,
          f"P{number} draft marker in manuscript")
    references = citation_gate(number, tex, bib)
    names = manifest(directory)
    check(set(REQUIRED) - {"SHA256SUMS"} <= names,
          f"P{number} final manifest omits required files")
    check((directory / "main.pdf").read_bytes()
          == (directory / "main_round2.pdf").read_bytes(),
          f"P{number} live PDF differs from Round 2")
    pages = [pdf_gate(number, directory / name) for name in ROUND_PDFS]
    check(len(set(pages)) == 1, f"P{number} page counts drift across rounds")
    log = (directory / "main.log").read_text(encoding="utf-8", errors="replace")
    check(re.search(
        r"(?i)(LaTeX Warning|Package .* Warning|undefined references|"
        r"Citation .* undefined|Reference .* undefined|Overfull \\hbox|Underfull \\hbox)",
        log,
    ) is None, f"P{number} settled log diagnostic")
    author_verifier, author_canonical = AUTHOR[number]
    replay(directory / author_verifier, directory / author_canonical,
           f"P{number} author")
    for label, review in zip(("Review A", "Review B"), REVIEWS[number]):
        review_gate(number, review, label)
    cold_build_gate(number, directory)
    visual = sorted((directory / "qa_final/visual").glob("page-*.png"))
    check(len(visual) == pages[-1], f"P{number} visual-page count mismatch")
    return pages[-1], references


def main() -> None:
    total_pages = 0
    total_refs = 0
    for number, directory in PAPERS.items():
        pages, references = paper_gate(number, directory)
        total_pages += pages
        total_refs += references
        print(f"P{number}=PASS pages={pages} references={references} "
              f"pdf_sha256={sha(directory / 'main.pdf')}")
    for required in (
        "phase2/ROUND0_REPORT.md", "phase2/ROUND1_REPORT.md",
        "phase2/ROUND2_REPORT.md", "phase2/DUAL_REVIEW_REPORT.md",
        "phase2/INTEGRITY_REPORT_INITIAL.md", "phase2/INTEGRITY_REPORT_FINAL.md",
        "phase2/ORIGINALITY_AUDIT_INITIAL.md", "phase2/ORIGINALITY_AUDIT_FINAL.md",
        "qa/FINAL_BATCH_QA.md", "PIPELINE_STATE.md",
    ):
        check((SEQ / required).is_file(), f"missing batch artifact: {required}")
    print(f"papers=5")
    print(f"pages={total_pages}")
    print(f"bibliography_records={total_refs}")
    print(f"audit_assertions={ASSERTIONS + 1}")
    print("open_findings=critical:0,major:0,minor:0")
    print("external_status=OWNER_AMBER/HOLD_EXTERNAL")
    print("status=PASS")


if __name__ == "__main__":
    main()
