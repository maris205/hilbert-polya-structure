#!/usr/bin/env python3
"""Terminal mechanical audit executable for Route-A papers P182--P186.

Run only after every Round-2 receipt, final manifest, dual-review delta, and
source-only cold build exists.  This executable checks artifact mechanics and
provenance consistency; it does not certify mathematical truth, novelty,
bibliographic completeness, or permission for external release.

The script is prepared before terminal artifacts exist.  Its stdout becomes a
canonical candidate only after the coordinator explicitly runs the final gate.
"""

from __future__ import annotations

import hashlib
import os
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[3]
SEQUENCE = ROOT / "docs" / "papers182_186_sequence"
PAPERS = {
    182: ROOT / "papers" / "182-cyclic-subspace-lattice-comparator",
    183: ROOT / "papers" / "183-random-incoming-copy-symmetrization",
    184: ROOT / "papers" / "184-co-gcd-translation-prime-powers",
    185: ROOT / "papers" / "185-prefix-diversity-delay",
    186: ROOT / "papers" / "186-rank-compression-support",
}
AUTHOR_CONTROLS = {
    182: ("code/verify_p182.py", "code/CANONICAL.txt"),
    183: ("code/verify_p183.py", "code/CANONICAL.txt"),
    184: ("code/verify_p184.py", "code/CANONICAL.txt"),
    185: ("verify_p185.py", "CANONICAL.txt"),
    186: ("verify_p186.py", "CANONICAL.txt"),
}
COLD_BUILDS = ("qa_final/cold_build_1", "qa_final/cold_build_2")

REQUIRED_FINAL = (
    "main.tex",
    "references.bib",
    "main.pdf",
    "main_round0_original.pdf",
    "main_round1.pdf",
    "main_round2.pdf",
    "README.md",
    "NARRATIVE_REPORT.md",
    "PAPER_PLAN.md",
    "FIGURE_PLAN.md",
    "CLAIMS_EVIDENCE.md",
    "PROOF_PACKAGE.md",
    "SOURCE_VERIFICATION.md",
    "BUILD.md",
    "SELF_QA.md",
    "IMPROVEMENT_LOG.md",
    "FINAL_QA.md",
    "SHA256SUMS",
)
PDF_OBJECTS = (
    "main_round0_original.pdf",
    "main_round1.pdf",
    "main_round2.pdf",
    "main.pdf",
)
PLACEHOLDER_PATTERN = re.compile(
    r"(?i)(TO_BE_FILLED|REPLACE_ME|INSERT_HERE|\bTBD\b|\bPENDING\b|<\s*fill[^>]*>)"
)
UNRESOLVED_BOX_PATTERN = re.compile(r"-\s*\[\s\]")
PASS_PATTERN = re.compile(
    r"(?im)^(?:status|result)\s*=\s*PASS(?:$|_[A-Z0-9_]+\s*$)"
)


ASSERTIONS = 0


def check(condition: bool, message: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def command(args: list[str], *, cwd: Path | None = None, timeout: int = 600) -> str:
    environment = os.environ.copy()
    environment.update({
        "LC_ALL": "C",
        "TZ": "UTC",
        "PYTHONDONTWRITEBYTECODE": "1",
    })
    result = subprocess.run(
        args,
        cwd=cwd or ROOT,
        env=environment,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=timeout,
    )
    check(result.returncode == 0,
          f"command failed ({result.returncode}): {' '.join(args)}\n{result.stdout}")
    return result.stdout


def parse_manifest(directory: Path) -> set[str]:
    manifest = directory / "SHA256SUMS"
    check(manifest.is_file(), f"missing manifest: {manifest}")
    names: list[str] = []
    for line_number, line in enumerate(manifest.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        match = re.fullmatch(r"([0-9a-f]{64})\s+\*?(.+)", line)
        check(match is not None,
              f"malformed manifest row {manifest}:{line_number}: {line!r}")
        if match is None:  # keeps type checkers and failure messages simple
            continue
        expected, relative = match.groups()
        relative = relative.strip()
        relative_path = Path(relative)
        check(not relative_path.is_absolute() and ".." not in relative_path.parts,
              f"unsafe manifest path in {manifest}: {relative}")
        check(relative != "SHA256SUMS",
              f"self-referential manifest row in {manifest}")
        target = directory / relative_path
        check(target.is_file(), f"manifest target missing: {target}")
        check(digest(target) == expected, f"manifest digest mismatch: {target}")
        names.append(relative)
    check(bool(names), f"empty manifest: {manifest}")
    check(len(names) == len(set(names)), f"duplicate manifest path in {manifest}")
    return set(names)


def extract_info(pdf: Path) -> tuple[str, dict[str, str]]:
    raw = command(["pdfinfo", str(pdf)])
    fields: dict[str, str] = {}
    for line in raw.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    return raw, fields


def audit_pdf(number: int, pdf: Path) -> int:
    check(pdf.is_file() and pdf.stat().st_size > 50_000,
          f"P{number} missing or implausibly small PDF: {pdf.name}")
    raw, fields = extract_info(pdf)
    pages_text = fields.get("Pages", "")
    check(pages_text.isdigit() and int(pages_text) > 0,
          f"P{number} invalid page count in {pdf.name}: {pages_text!r}")
    check("(A4)" in fields.get("Page size", ""),
          f"P{number} non-A4 page in {pdf.name}: {fields.get('Page size', '')}")
    check(fields.get("Page rot") == "0",
          f"P{number} rotated page in {pdf.name}")
    for field in ("Title", "Subject", "Keywords", "Author", "Creator", "Producer"):
        check(field in fields and fields[field] == "",
              f"P{number} nonblank/missing metadata {field} in {pdf.name}")
    for date_field in ("CreationDate", "ModDate"):
        check(date_field not in fields or fields[date_field] == "",
              f"P{number} timestamp metadata {date_field} in {pdf.name}")
    check(fields.get("Custom Metadata") == "no",
          f"P{number} custom metadata present in {pdf.name}")
    check(fields.get("Metadata Stream") == "no",
          f"P{number} metadata stream present in {pdf.name}")
    check(fields.get("JavaScript") == "no",
          f"P{number} JavaScript present/unknown in {pdf.name}")
    check(fields.get("Encrypted") == "no",
          f"P{number} encrypted/unknown PDF {pdf.name}")

    font_output = command(["pdffonts", str(pdf)])
    font_lines = font_output.splitlines()
    separator = next((i for i, line in enumerate(font_lines)
                      if line and set(line) <= {"-", " "}), None)
    check(separator is not None, f"P{number} malformed pdffonts output for {pdf.name}")
    rows = [] if separator is None else [line for line in font_lines[separator + 1:]
                                         if line.strip()]
    check(bool(rows), f"P{number} no font rows in {pdf.name}")
    for row in rows:
        columns = row.split()
        check(len(columns) >= 5 and columns[-5:-2] == ["yes", "yes", "yes"],
              f"P{number} font not emb/sub/uni in {pdf.name}: {row}")

    text = command(["pdftotext", str(pdf), "-"])
    check("??" not in text and "[?]" not in text,
          f"P{number} unresolved reference token in {pdf.name}")
    check(re.search(r"(?i)\b(?:TODO|VERIFY)\b", text) is None,
          f"P{number} draft marker in {pdf.name}")
    check("HOLD_EXTERNAL" in text.upper() or "HOLD EXTERNAL" in text.upper(),
          f"P{number} PDF omits HOLD_EXTERNAL in {pdf.name}")
    return int(pages_text)


def exact_citation_sets(number: int, tex: str, bib: str) -> None:
    bib_keys = {
        match.group(1).strip()
        for match in re.finditer(
            r"@(?!comment\b|string\b|preamble\b)[A-Za-z]+\s*\{\s*([^,\s]+)",
            bib,
            flags=re.IGNORECASE,
        )
    }
    cite_groups = re.findall(
        r"\\cite[A-Za-z*]*(?:\s*\[[^\]]*\]){0,2}\s*\{([^{}]+)\}",
        tex,
    )
    cite_keys = {
        key.strip()
        for group in cite_groups
        for key in group.split(",")
        if key.strip()
    }
    check(bool(bib_keys), f"P{number} bibliography has no entries")
    check(bib_keys == cite_keys,
          f"P{number} exact bib/cite mismatch: "
          f"bib_only={sorted(bib_keys - cite_keys)}, "
          f"cite_only={sorted(cite_keys - bib_keys)}")


def canonical_has_zero_findings(text: str) -> bool:
    separate = all(
        re.search(rf"(?im)^{severity}_findings\s*=\s*0\s*$", text) is not None
        for severity in ("critical", "major", "minor")
    )
    combined = re.search(
        r"(?im)^findings\s*=\s*critical:0\s*,\s*major:0\s*,\s*minor:0\s*$",
        text,
    ) is not None
    return separate or combined


def replay(number: int, verifier: Path, canonical: Path, role: str) -> None:
    check(verifier.is_file(), f"P{number} missing {role} verifier: {verifier}")
    check(canonical.is_file(), f"P{number} missing {role} canonical: {canonical}")
    output = command([sys.executable, "-B", str(verifier)], cwd=ROOT)
    check(output.encode("utf-8") == canonical.read_bytes(),
          f"P{number} {role} canonical replay mismatch: {verifier}")


def audit_cold_builds(number: int, directory: Path, live: Path) -> None:
    resolved: list[Path] = []
    pdf_inodes: list[tuple[int, int]] = []
    for relative in COLD_BUILDS:
        cold = directory / relative
        check(cold.is_dir() and not cold.is_symlink(),
              f"P{number} missing/nonphysical cold build: {relative}")
        resolved.append(cold.resolve())
        for required in ("main.tex", "references.bib", "main.aux", "main.bbl",
                         "main.blg", "main.log", "main.pdf"):
            check((cold / required).is_file(),
                  f"P{number} cold build {relative} missing {required}")
            check(not (cold / required).is_symlink(),
                  f"P{number} cold build {relative} symlinks {required}")
        check((cold / "main.tex").read_bytes() == (directory / "main.tex").read_bytes(),
              f"P{number} cold source mismatch in {relative}")
        check((cold / "references.bib").read_bytes()
              == (directory / "references.bib").read_bytes(),
              f"P{number} cold bibliography mismatch in {relative}")
        local_inputs = {
            path.relative_to(cold).as_posix()
            for path in cold.rglob("*")
            if path.is_file() and path.suffix.lower() in {".tex", ".bib", ".sty", ".cls", ".bst"}
        }
        check(local_inputs == {"main.tex", "references.bib"},
              f"P{number} cold build {relative} is not source-only: {sorted(local_inputs)}")
        check((cold / "main.pdf").read_bytes() == live.read_bytes(),
              f"P{number} cold PDF mismatch in {relative}")
        log = (cold / "main.log").read_text(encoding="utf-8", errors="replace")
        blg = (cold / "main.blg").read_text(encoding="utf-8", errors="replace")
        check("Output written on main.pdf" in log,
              f"P{number} cold build {relative} lacks compilation completion")
        check(re.search(r"(?i)(Citation .* undefined|Reference .* undefined|undefined references)",
                        log) is None,
              f"P{number} cold build {relative} has undefined reference/citation")
        check("This is BibTeX" in blg,
              f"P{number} cold build {relative} lacks BibTeX execution receipt")
        stat = (cold / "main.pdf").stat()
        pdf_inodes.append((stat.st_dev, stat.st_ino))
    check(len(set(resolved)) == 2, f"P{number} cold build directories alias")
    check(len(set(pdf_inodes)) == 2, f"P{number} cold build PDFs are hard-linked")


def audit_reviews(number: int) -> int:
    review_root = SEQUENCE / "reviews" / f"paper{number}"
    check(review_root.is_dir(), f"P{number} missing review root")
    reviewer_dirs = sorted(
        (path for path in review_root.iterdir()
         if path.is_dir() and not path.name.startswith(".")),
        key=lambda path: path.name,
    )
    check(len(reviewer_dirs) == 2,
          f"P{number} requires exactly two reviewer dirs, found "
          f"{[path.name for path in reviewer_dirs]}")
    replay_count = 0
    for reviewer in reviewer_dirs:
        check(not reviewer.is_symlink(), f"P{number} symlink reviewer dir: {reviewer}")
        names = parse_manifest(reviewer)
        canonicals = list(reviewer.glob("CANONICAL.txt"))
        verifiers = list(reviewer.glob("verify_*.py"))
        reports = list(reviewer.glob("HOSTILE_REVIEW*.md"))
        deltas = list(reviewer.glob("DELTA*.md"))
        check(len(canonicals) == len(verifiers) == len(reports) == len(deltas) == 1,
              f"P{number} reviewer package cardinality failure in {reviewer}")
        canonical, verifier = canonicals[0], verifiers[0]
        report, delta = reports[0], deltas[0]
        required_names = {canonical.name, verifier.name, report.name, delta.name}
        check(required_names <= names,
              f"P{number} reviewer manifest omits "
              f"{sorted(required_names - names)} in {reviewer}")

        canonical_text = canonical.read_text(encoding="utf-8")
        check(PASS_PATTERN.search(canonical_text) is not None,
              f"P{number} reviewer canonical lacks PASS sentinel in {reviewer}")
        check(canonical_has_zero_findings(canonical_text),
              f"P{number} reviewer canonical has nonzero/absent finding census in {reviewer}")
        report_text = report.read_text(encoding="utf-8")
        delta_text = delta.read_text(encoding="utf-8")
        check("HOLD_EXTERNAL" in report_text.upper(),
              f"P{number} review report lacks HOLD_EXTERNAL in {reviewer}")
        check(UNRESOLVED_BOX_PATTERN.search(delta_text) is None,
              f"P{number} reviewer delta has unresolved checkbox in {reviewer}")
        check(PLACEHOLDER_PATTERN.search(delta_text) is None,
              f"P{number} reviewer delta has unresolved placeholder in {reviewer}")
        check(re.search(r"(?i)\b(?:ACCEPT|ACCEPTED|PASS)\b", delta_text) is not None,
              f"P{number} reviewer delta lacks acceptance sentinel in {reviewer}")

        replay(number, verifier, canonical, f"reviewer {reviewer.name}")
        replay_count += 1
    return replay_count


def audit_paper(number: int, directory: Path) -> tuple[str, int, int]:
    check(directory.is_dir(), f"P{number} paper directory absent")
    for relative in REQUIRED_FINAL:
        check((directory / relative).is_file(), f"P{number} missing final file {relative}")

    tex = (directory / "main.tex").read_text(encoding="utf-8")
    bib = (directory / "references.bib").read_text(encoding="utf-8")
    check(re.search(r"\\author\s*\{\s*Anonymous\s*\}", tex) is not None,
          f"P{number} author is not exactly Anonymous")
    for forbidden in (r"\email{", r"\address{", r"\affiliation{", r"\institute{", r"\thanks{"):
        check(forbidden not in tex, f"P{number} anonymity leak token {forbidden}")
    check("HOLD" in tex.upper() and "EXTERNAL" in tex.upper(),
          f"P{number} manuscript lacks HOLD_EXTERNAL")
    for control in (r"\pdfinfoomitdate=1", r"\pdftrailerid{}", r"\pdfsuppressptexinfo=15"):
        check(control in tex, f"P{number} deterministic PDF control absent: {control}")
    check(re.search(r"(?i)\b(?:TODO|VERIFY|TBD)\b", tex) is None,
          f"P{number} manuscript contains draft marker")
    exact_citation_sets(number, tex, bib)

    live = directory / "main.pdf"
    round2 = directory / "main_round2.pdf"
    check(live.read_bytes() == round2.read_bytes(), f"P{number} live PDF != Round 2")
    page_counts = [audit_pdf(number, directory / relative) for relative in PDF_OBJECTS]

    log = (directory / "main.log").read_text(encoding="utf-8", errors="replace")
    check(re.search(r"(?i)(Citation .* undefined|Reference .* undefined|undefined references)",
                    log) is None,
          f"P{number} final build log has undefined reference/citation")

    manifest_names = parse_manifest(directory)
    verifier_relative, canonical_relative = AUTHOR_CONTROLS[number]
    manifest_required = set(REQUIRED_FINAL) - {"SHA256SUMS"}
    manifest_required.update((verifier_relative, canonical_relative))
    check(manifest_required <= manifest_names,
          f"P{number} final manifest omits {sorted(manifest_required - manifest_names)}")

    verifier = directory / verifier_relative
    canonical = directory / canonical_relative
    canonical_text = canonical.read_text(encoding="utf-8")
    check(PASS_PATTERN.search(canonical_text) is not None,
          f"P{number} author canonical lacks PASS sentinel")
    check("HOLD_EXTERNAL" in canonical_text.upper(),
          f"P{number} author canonical lacks HOLD_EXTERNAL")
    replay(number, verifier, canonical, "author")

    final_qa = (directory / "FINAL_QA.md").read_text(encoding="utf-8")
    check(re.search(r"(?i)\bPASS\b", final_qa) is not None,
          f"P{number} FINAL_QA lacks PASS sentinel")
    check("HOLD_EXTERNAL" in final_qa.upper(),
          f"P{number} FINAL_QA lacks HOLD_EXTERNAL")
    check(UNRESOLVED_BOX_PATTERN.search(final_qa) is None,
          f"P{number} FINAL_QA has unresolved checkbox")
    check(PLACEHOLDER_PATTERN.search(final_qa) is None,
          f"P{number} FINAL_QA has unresolved placeholder")

    audit_cold_builds(number, directory, live)
    reviewer_replays = audit_reviews(number)
    return digest(live), page_counts[-1], reviewer_replays


def main() -> None:
    rows = []
    for number in sorted(PAPERS):
        pdf_hash, pages, reviewer_replays = audit_paper(number, PAPERS[number])
        rows.append((number, pdf_hash, pages, reviewer_replays))

    print("ROUTE_A_P182_P186_TERMINAL_MECHANICAL_AUDIT")
    for number, pdf_hash, pages, reviewer_replays in rows:
        print(f"P{number}_PDF_SHA256={pdf_hash} PAGES={pages} "
              f"AUTHOR_REPLAYS=1 REVIEWER_REPLAYS={reviewer_replays} COLD_BUILDS=2")
    print(f"ASSERTIONS={ASSERTIONS}")
    print("SCOPE=artifact/reference-set/PDF/manifest/replay/cold-build mechanics only")
    print("RESULT=PASS")
    print("RELEASE_SENTINEL=HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
