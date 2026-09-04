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
import struct
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
    191: (
        PAPERS[191] / "reviews/round1/reviewer_a",
        SEQ / "reviews/p191_b",
    ),
}
REQUIRED = (
    "README.md", "BUILD.md", "CLAIMS_EVIDENCE.md", "FIGURE_PLAN.md",
    "IMPROVEMENT_LOG.md", "NARRATIVE_REPORT.md", "PAPER_PLAN.md",
    "PROOF_PACKAGE.md", "SELF_QA.md", "SOURCE_VERIFICATION.md",
    "FINAL_QA.md", "main.tex", "references.bib", "main.pdf",
    "main_round0_original.pdf", "main_round1.pdf", "main_round2.pdf",
    "main.log", "main.blg", "qa_final/SHA256SUMS", "SHA256SUMS",
)
ROUND_PDFS = (
    "main_round0_original.pdf", "main_round1.pdf", "main_round2.pdf", "main.pdf"
)
ASSERTIONS = 0
REVIEW_REPLAYS = 0


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
        local_target = directory / target_rel
        root_target = ROOT / target_rel
        if local_target.is_file():
            target = local_target
        elif root_target.is_file():
            target = root_target
        else:
            target = local_target
        check(target.is_file() and not target.is_symlink(),
              f"manifest target missing/symlink: {target}")
        try:
            normalized = target.resolve().relative_to(directory.resolve()).as_posix()
        except ValueError:
            check(False, f"manifest target escapes package: {path}:{relative}")
            normalized = relative
        check(sha(target) == expected, f"manifest digest mismatch: {target}")
        names.append(normalized)
    check(bool(names), f"empty manifest: {path}")
    check(len(names) == len(set(names)), f"duplicate manifest target: {path}")
    return set(names)


def pinned_inputs(path: Path, label: str) -> int:
    check(path.is_file() and not path.is_symlink(), f"missing {label} pins")
    count = 0
    targets: set[str] = set()
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        match = re.fullmatch(r"([0-9a-f]{64})\s+\*?(.+)", line)
        check(match is not None, f"bad pin row {path}:{line_no}")
        if match is None:
            continue
        expected, relative = match.groups()
        target_rel = Path(relative.strip())
        check(not target_rel.is_absolute() and ".." not in target_rel.parts,
              f"unsafe pin path: {path}:{relative}")
        target = ROOT / target_rel
        normalized = target_rel.as_posix()
        check(normalized not in targets,
              f"duplicate pinned input: {path}:{normalized}")
        targets.add(normalized)
        check(target.is_file() and not target.is_symlink(),
              f"missing/symlink pinned input: {target}")
        check(sha(target) == expected, f"pinned input drift: {target}")
        count += 1
    check(count > 0, f"empty pinned-input population: {path}")
    return count


def citation_gate(number: int, tex: str, bib: str) -> int:
    bib_key_list = [
        match.group(1).strip()
        for match in re.finditer(
            r"@(?!comment\b|string\b|preamble\b)[A-Za-z]+\s*\{\s*([^,\s]+)",
            bib, flags=re.I,
        )
    ]
    check(len(bib_key_list) == len(set(bib_key_list)),
          f"P{number} duplicate bibliography key")
    bib_keys = set(bib_key_list)
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
    return len(bib_key_list)


def canonical_assertions(path: Path, label: str) -> int:
    values = re.findall(
        r"(?im)^(?:exact_)?assertions\s*=\s*([0-9]+)\s*$",
        path.read_text(encoding="utf-8"),
    )
    check(len(values) == 1, f"{label} must disclose exactly one assertion total")
    return int(values[0])


def canonical_severity_values(text: str, severity: str) -> list[int]:
    """Return all disclosed values for one severity census."""
    values = [
        int(match.group(1))
        for match in re.finditer(
            rf"(?im)^{severity}(?:_findings)?\s*=\s*([0-9]+)\s*$", text
        )
    ]
    for line in text.splitlines():
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        if key.strip().lower() != "findings":
            continue
        entries: dict[str, str] = {}
        for token in value.split(","):
            if ":" not in token:
                continue
            name, count = token.split(":", 1)
            entries[name.strip().lower()] = count.strip()
        if severity in entries and entries[severity].isdigit():
            values.append(int(entries[severity]))
    return values


def canonical_accepted(text: str) -> bool:
    accepted = {
        "PASS", "PASS_INTERNAL", "PASS_DELTA_ACCEPTED",
        "PROVABLE_AS_STATED",
    }
    for line in text.splitlines():
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        if key.strip().lower() not in {"verdict", "status", "result"}:
            continue
        value = value.strip().upper()
        if value in accepted:
            return True
    return False


def pdf_gate(number: int, path: Path) -> int:
    check(path.is_file() and path.stat().st_size > 50_000,
          f"P{number} missing/small PDF: {path.name}")
    raw = command(["pdfinfo", str(path)])
    fields = {}
    for line in raw.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    check(fields.get("Pages", "").isdigit()
          and int(fields["Pages"]) > 0, f"P{number} bad page count")
    check("(A4)" in fields.get("Page size", ""), f"P{number} non-A4 PDF")
    check(fields.get("Page rot") == "0", f"P{number} rotated PDF")
    for key in ("Title", "Subject", "Keywords", "Author", "Creator", "Producer"):
        check(key in fields and fields[key] == "",
              f"P{number} identity metadata {key}: {fields.get(key)!r}")
    check(fields.get("Encrypted") == "no", f"P{number} encrypted PDF")
    check(fields.get("Custom Metadata") == "no",
          f"P{number} custom PDF metadata")
    check(fields.get("Form") == "none", f"P{number} PDF forms present")
    check(fields.get("JavaScript") == "no", f"P{number} JavaScript PDF")
    check(fields.get("Metadata Stream") == "no", f"P{number} metadata stream")
    for key in ("CreationDate", "ModDate"):
        check(key not in fields or fields[key] == "",
              f"P{number} nondeterministic PDF field {key}")

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
    global REVIEW_REPLAYS
    check(directory.is_dir() and not directory.is_symlink(),
          f"P{number} missing {label} review dir: {directory}")
    names = manifest(directory)
    payload_names = {
        path.name for path in directory.iterdir()
        if path.is_file() and path.name != "SHA256SUMS"
    }
    check(payload_names == names,
          f"P{number} {label} manifest coverage mismatch")
    for name in payload_names:
        check((directory / name).stat().st_size > 0,
              f"P{number} {label} contains empty payload: {name}")
    check(not list(directory.rglob("__pycache__"))
          and not list(directory.rglob("*.pyc")),
          f"P{number} {label} contains Python cache artifacts")
    verifiers = list(directory.glob("verify*.py"))
    canonicals = list(directory.glob("CANONICAL.txt"))
    deltas = list(directory.glob("*DELTA*.md"))
    if not deltas:
        deltas = list(directory.glob("DELTA.md"))
    reports = [path for path in directory.glob("*.md") if "REVIEW" in path.name]
    check(len(verifiers) == len(canonicals) == len(deltas) == 1,
          f"P{number} {label} package cardinality failure")
    check(len(reports) == 1,
          f"P{number} {label} review-report cardinality failure")
    verifier, canonical, delta = verifiers[0], canonicals[0], deltas[0]
    check({verifier.name, canonical.name, delta.name, reports[0].name} <= names,
          f"P{number} {label} manifest omits core files")
    pins = directory / "PINNED_INPUTS.sha256"
    if pins.is_file():
        pin_count = pinned_inputs(pins, f"P{number} {label}")
        check(pin_count >= 6, f"P{number} {label} pins too few inputs")
    if label == "Review B":
        check(pins.name in names, f"P{number} Review B manifest omits pins")
        check("BUILD_PDF_QA.md" in names,
              f"P{number} Review B lacks build/PDF QA")
        check("REPLAY_LOG.md" in names,
              f"P{number} Review B lacks replay receipt")
        replay_text = (directory / "REPLAY_LOG.md").read_text(encoding="utf-8")
        check(re.search(r"(?i)\breplay\s*1\b", replay_text) is not None
              and re.search(r"(?i)\breplay\s*2\b", replay_text) is not None
              and "canonical" in replay_text.lower()
              and "byte" in replay_text.lower(),
              f"P{number} Review B replay receipt lacks two byte checks")
        check(any(name.startswith("PROOF_REDERIVATION") for name in names),
              f"P{number} Review B lacks proof rederivation")
        check(any("SOURCE_OWNER" in name or "OWNER_COLLISION" in name
                  for name in names),
              f"P{number} Review B lacks source/owner audit")
    replay(verifier, canonical, f"P{number} {label}")
    REVIEW_REPLAYS += 1
    canonical_text = canonical.read_text(encoding="utf-8")
    for severity in ("critical", "major", "minor"):
        values = canonical_severity_values(canonical_text, severity)
        check(values == [0],
              f"P{number} {label} nonzero/absent/duplicate {severity} "
              f"census: {values}")
    check(canonical_accepted(canonical_text),
          f"P{number} {label} canonical lacks an accepted verdict")
    report_text = "\n".join(path.read_text(encoding="utf-8") for path in reports)
    delta_text = delta.read_text(encoding="utf-8")
    check("HOLD_EXTERNAL" in report_text.upper(), f"P{number} {label} lacks hold")
    check(re.search(r"-\s*\[\s\]", delta_text) is None,
          f"P{number} {label} has unchecked delta box")
    check(re.search(r"(?i)\b(?:PASS|ACCEPT|ACCEPTED)\b", delta_text) is not None,
          f"P{number} {label} delta lacks acceptance")
    return canonical_assertions(canonical, f"P{number} {label}")


def cold_build_gate(number: int, directory: Path) -> None:
    live = directory / "main.pdf"
    seen: set[tuple[int, int]] = set()
    for name in ("cold_build_1", "cold_build_2"):
        cold = directory / "qa_final" / name
        check(cold.is_dir() and not cold.is_symlink(),
              f"P{number} missing physical {name}")
        for required in ("main.tex", "references.bib", "main.aux", "main.bbl",
                         "main.blg", "main.log", "main.fls", "main.pdf", "pass1.stdout",
                         "bibtex.stdout", "pass2.stdout", "pass3.stdout"):
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
        fls_inputs = []
        for line in (cold / "main.fls").read_text(
            encoding="utf-8", errors="replace"
        ).splitlines():
            if not line.startswith("INPUT "):
                continue
            candidate = Path(line[6:])
            if not candidate.is_absolute():
                candidate = (cold / candidate).resolve()
            else:
                candidate = candidate.resolve()
            fls_inputs.append(candidate)
        check(bool(fls_inputs), f"P{number} {name} has empty recorder input set")
        trusted_system_roots = tuple(Path(path).resolve() for path in (
            "/etc/texmf", "/usr/share/texlive", "/usr/share/texmf",
            "/var/lib/texmf",
        ))
        untrusted_inputs = [
            path for path in fls_inputs
            if cold not in (path, *path.parents)
            and not any(root in (path, *path.parents)
                        for root in trusted_system_roots)
        ]
        check(not untrusted_inputs,
              f"P{number} {name} recorder input outside cold/system "
              f"allowlist: {untrusted_inputs}")
        check((cold / "main.pdf").read_bytes() == live.read_bytes(),
              f"P{number} {name} PDF differs from live")
        for stdout_name in ("pass1.stdout", "bibtex.stdout", "pass2.stdout",
                            "pass3.stdout"):
            check((cold / stdout_name).stat().st_size > 0,
                  f"P{number} {name} empty stdout receipt: {stdout_name}")
        check("Output written on main.pdf" in (cold / "pass3.stdout").read_text(
            encoding="utf-8", errors="replace"
        ), f"P{number} {name} final stdout lacks PDF receipt")
        check("This is BibTeX" in (cold / "bibtex.stdout").read_text(
            encoding="utf-8", errors="replace"
        ), f"P{number} {name} BibTeX stdout lacks receipt")
        log = (cold / "main.log").read_text(encoding="utf-8", errors="replace")
        check("Output written on main.pdf" in log,
              f"P{number} {name} lacks settled PDF receipt")
        check(re.search(
            r"(?i)(LaTeX Warning|Package .* Warning|undefined references|"
            r"Citation .* undefined|Reference .* undefined|"
            r"Overfull \\hbox|Underfull \\hbox|! LaTeX Error|"
            r"Emergency stop|Fatal error)", log,
        ) is None, f"P{number} {name} log diagnostic")
        blg = (cold / "main.blg").read_text(encoding="utf-8", errors="replace")
        check("This is BibTeX" in blg, f"P{number} {name} lacks BibTeX receipt")
        check(re.search(r"(?i)(Warning--|I couldn't open|I found no)", blg) is None,
              f"P{number} {name} BibTeX diagnostic")
        stat = (cold / "main.pdf").stat()
        check(stat.st_nlink == 1,
              f"P{number} {name} PDF has multiple hard links")
        receipt_inodes = {
            ((directory / receipt).stat().st_dev,
             (directory / receipt).stat().st_ino)
            for receipt in ROUND_PDFS
        }
        check((stat.st_dev, stat.st_ino) not in receipt_inodes,
              f"P{number} {name} PDF aliases a round receipt")
        seen.add((stat.st_dev, stat.st_ino))
    check(len(seen) == 2, f"P{number} cold PDFs alias/hardlink")


def paper_gate(number: int, directory: Path) -> tuple[int, int, int, list[int]]:
    check(directory.is_dir() and not directory.is_symlink(),
          f"P{number} paper directory missing/symlink")
    for relative in REQUIRED:
        target = directory / relative
        check(target.is_file() and not target.is_symlink(),
              f"P{number} missing/symlink {relative}")
    tex = (directory / "main.tex").read_text(encoding="utf-8")
    bib = (directory / "references.bib").read_text(encoding="utf-8")
    check(re.search(r"\\author\s*\{\s*Anonymous\s*\}", tex) is not None,
          f"P{number} nonanonymous manuscript")
    for token in (r"\email{", r"\address{", r"\affiliation{", r"\institute{",
                  r"\thanks{"):
        check(token not in tex, f"P{number} anonymity token: {token}")
    for token in (r"\pdfinfoomitdate=1", r"\pdftrailerid{}", r"\pdfsuppressptexinfo=15"):
        check(token in tex, f"P{number} missing deterministic control: {token}")
    check(re.search(r"(?i)(?:\b(?:TODO|TBD|REPLACE_ME)\b|\[VERIFY\])", tex) is None,
          f"P{number} draft marker in manuscript")
    references = citation_gate(number, tex, bib)
    names = manifest(directory)
    author_verifier, author_canonical = AUTHOR[number]
    required_manifest = (
        set(REQUIRED) - {"SHA256SUMS"}
        | {author_verifier, author_canonical}
    )
    approved_manifest_extras = {
        187: {"qa_round0/ROUND0_QA.md"},
        188: {"qa_round0/ROUND0_QA.md"},
    }.get(number, set())
    check(names == required_manifest | approved_manifest_extras,
          f"P{number} final manifest population mismatch")
    check((directory / "main.pdf").read_bytes()
          == (directory / "main_round2.pdf").read_bytes(),
          f"P{number} live PDF differs from Round 2")
    pages = [pdf_gate(number, directory / name) for name in ROUND_PDFS]
    check(len(set(pages)) == 1, f"P{number} page counts drift across rounds")
    receipt_inodes = {
        ((directory / name).stat().st_dev, (directory / name).stat().st_ino)
        for name in ROUND_PDFS
    }
    check(len(receipt_inodes) == len(ROUND_PDFS),
          f"P{number} PDF receipts alias/hardlink")
    for name in ROUND_PDFS:
        check((directory / name).stat().st_nlink == 1,
              f"P{number} PDF receipt has multiple hard links: {name}")
    log = (directory / "main.log").read_text(encoding="utf-8", errors="replace")
    check(re.search(
        r"(?i)(LaTeX Warning|Package .* Warning|undefined references|"
        r"Citation .* undefined|Reference .* undefined|Overfull \\hbox|"
        r"Underfull \\hbox|! LaTeX Error|Emergency stop|Fatal error)",
        log,
    ) is None, f"P{number} settled log diagnostic")
    check("Output written on main.pdf" in log,
          f"P{number} live log lacks settled PDF receipt")
    blg = (directory / "main.blg").read_text(encoding="utf-8", errors="replace")
    check("This is BibTeX" in blg and re.search(
        r"(?i)(Warning--|I couldn't open|I found no)", blg
    ) is None, f"P{number} live BibTeX diagnostic")
    replay(directory / author_verifier, directory / author_canonical,
           f"P{number} author")
    author_text = (directory / author_canonical).read_text(encoding="utf-8")
    check(canonical_accepted(author_text),
          f"P{number} author canonical lacks an accepted status")
    author_count = canonical_assertions(
        directory / author_canonical, f"P{number} author"
    )
    check(len(REVIEWS[number]) == 2, f"P{number} must have exactly two reviews")
    review_counts = [
        review_gate(number, review, label)
        for label, review in zip(("Review A", "Review B"), REVIEWS[number])
    ]
    cold_build_gate(number, directory)
    qa_final_names = manifest(directory / "qa_final")
    qa_final_payload = {
        path.relative_to(directory / "qa_final").as_posix()
        for path in (directory / "qa_final").rglob("*")
        if path.is_file() and path != directory / "qa_final/SHA256SUMS"
    }
    check(qa_final_names == qa_final_payload,
          f"P{number} qa_final manifest population mismatch")
    visual = sorted((directory / "qa_final/visual").glob("page-*.png"))
    visual_source = directory / "qa_final/visual/SOURCE_PDF.sha256"
    renderer_receipt = directory / "qa_final/visual/RENDERER.txt"
    check(visual_source.is_file() and not visual_source.is_symlink(),
          f"P{number} visual source receipt missing/symlink")
    source_match = re.match(
        r"([0-9a-f]{64})\s+", visual_source.read_text(encoding="utf-8")
    )
    check(source_match is not None and source_match.group(1) == sha(
        directory / "main.pdf"
    ), f"P{number} visual source hash mismatch")
    check(renderer_receipt.is_file() and not renderer_receipt.is_symlink()
          and "pdftoppm" in renderer_receipt.read_text(
              encoding="utf-8", errors="replace"
          ).lower(), f"P{number} visual renderer receipt missing")
    check(len(visual) == pages[-1], f"P{number} visual-page count mismatch")
    check([path.name for path in visual]
          == [f"page-{index}.png" for index in range(1, pages[-1] + 1)],
          f"P{number} visual-page names are not consecutive")
    for path in visual:
        check(path.is_file() and not path.is_symlink() and path.stat().st_size > 10_000,
              f"P{number} invalid visual artifact: {path.name}")
        raw_png = path.read_bytes()
        check(raw_png[:8] == b"\x89PNG\r\n\x1a\n" and len(raw_png) >= 24,
              f"P{number} invalid PNG signature: {path.name}")
        width, height = struct.unpack(">II", raw_png[16:24])
        check(width >= 1700 and height >= 2400,
              f"P{number} undersized visual artifact: {path.name}")
    final_qa = (directory / "FINAL_QA.md").read_text(encoding="utf-8")
    check(re.search(r"(?im)^terminal_status=PASS\s*$", final_qa) is not None,
          f"P{number} FINAL_QA lacks terminal PASS")
    check(re.search(
        r"(?im)^open_findings=critical:0,major:0,minor:0\s*$", final_qa
    ) is not None, f"P{number} FINAL_QA lacks exact zero census")
    check(re.search(
        r"(?im)^external_status=OWNER_AMBER/HOLD_EXTERNAL\s*$", final_qa
    ) is not None, f"P{number} FINAL_QA lacks lifecycle boundary")
    check(re.search(r"(?im)^cold_builds=2\s*$", final_qa) is not None,
          f"P{number} FINAL_QA lacks cold-build census")
    final_fields = {
        "pdf_sha256": sha(directory / "main.pdf"),
        "pages": str(pages[-1]),
        "bibliography_records": str(references),
        "author_assertions": str(author_count),
        "review_a_assertions": str(review_counts[0]),
        "review_b_assertions": str(review_counts[1]),
        "visual_pages": str(len(visual)),
        "visual_inspection": f"PASS_{len(visual)}_OF_{pages[-1]}",
    }
    for field, value in final_fields.items():
        check(re.search(rf"(?im)^{field}={re.escape(value)}\s*$", final_qa)
              is not None, f"P{number} FINAL_QA field mismatch: {field}")
    observation_rows = re.findall(r"(?im)^- page ([0-9]+): .+", final_qa)
    check(observation_rows == [str(index) for index in range(1, pages[-1] + 1)],
          f"P{number} FINAL_QA visual observation rows mismatch")
    return pages[-1], references, author_count, review_counts


def main() -> None:
    cache_artifacts = [
        path for base in (SEQ, *PAPERS.values())
        for path in base.rglob("*")
        if path.name == "__pycache__" or path.suffix == ".pyc"
    ]
    check(not cache_artifacts,
          f"unexpected Python cache artifacts: {cache_artifacts}")
    staging_artifacts = [
        path for directory in PAPERS.values()
        for path in (directory / "qa_final").glob(".*")
        if path.name.startswith((".cold_build_", ".visual."))
    ]
    check(not staging_artifacts,
          f"unfinished cold-build staging artifacts: {staging_artifacts}")
    batch_review_dirs = {
        path.name for path in (SEQ / "reviews").iterdir() if path.is_dir()
    }
    expected_batch_review_dirs = {
        "p187_a", "p187_b", "p188_a", "p188_b",
        "p189_b_duplicate_mirror_excluded", "p189_b_preliminary_superseded",
        "p190_a", "p190_b",
        "p191_a_preliminary_superseded", "p191_b",
    }
    check(batch_review_dirs == expected_batch_review_dirs,
          "batch review-directory allowlist mismatch")
    check({path.name for path in (PAPERS[189] / "reviews/round1").iterdir()
           if path.is_dir()} == {"reviewer_a"},
          "P189 Round-1 review-directory allowlist mismatch")
    check({path.name for path in (PAPERS[189] / "reviews/round2").iterdir()
           if path.is_dir()} == {"reviewer_b"},
          "P189 Round-2 review-directory allowlist mismatch")
    check({path.name for path in (PAPERS[191] / "reviews/round1").iterdir()
           if path.is_dir()} == {"reviewer_a"},
          "P191 Round-1 review-directory allowlist mismatch")
    rows = []
    total_pages = 0
    total_refs = 0
    total_author_assertions = 0
    total_review_a_assertions = 0
    total_review_b_assertions = 0
    for number, directory in PAPERS.items():
        pages, references, author_count, review_counts = paper_gate(
            number, directory
        )
        total_pages += pages
        total_refs += references
        total_author_assertions += author_count
        total_review_a_assertions += review_counts[0]
        total_review_b_assertions += review_counts[1]
        rows.append((
            number, sha(directory / "main.pdf"), pages, references,
            author_count, review_counts[0], review_counts[1],
        ))
    check(REVIEW_REPLAYS == 10, "terminal audit must replay exactly 10 reviews")

    batch_required = (
        "phase2/ROUND0_REPORT.md", "phase2/ROUND1_REPORT.md",
        "phase2/ROUND2_REPORT.md", "phase2/DUAL_REVIEW_REPORT.md",
        "phase2/INTEGRITY_REPORT_INITIAL.md", "phase2/INTEGRITY_REPORT_FINAL.md",
        "phase2/ORIGINALITY_AUDIT_INITIAL.md", "phase2/ORIGINALITY_AUDIT_FINAL.md",
        "qa/FINAL_BATCH_QA.md", "reviews/PROCESS_SEPARATION_LEDGER.md",
        "FINAL_QA_REPORT.md", "CANONICAL_PDF_MANIFEST.sha256",
        "PACKAGE_MANIFESTS.sha256",
        "PIPELINE_STATE.md", "SHA256SUMS", "qa/CANONICAL.txt",
        "qa/SHA256SUMS", "qa/audit_batch.py", "qa/run_final_cold_builds.sh",
    )
    for relative in batch_required:
        target = SEQ / relative
        check(target.is_file() and not target.is_symlink(),
              f"missing/symlink batch artifact: {relative}")
        check(target.stat().st_size > 0, f"empty batch artifact: {relative}")

    for relative in batch_required:
        if not relative.endswith(".md"):
            continue
        text = (SEQ / relative).read_text(encoding="utf-8")
        check(re.search(r"(?i)\b(?:TODO|TBD|REPLACE_ME)\b", text) is None,
              f"placeholder token in batch artifact: {relative}")

    terminal_docs = (
        "phase2/ROUND2_REPORT.md", "phase2/DUAL_REVIEW_REPORT.md",
        "phase2/INTEGRITY_REPORT_FINAL.md",
        "phase2/ORIGINALITY_AUDIT_FINAL.md", "qa/FINAL_BATCH_QA.md",
        "FINAL_QA_REPORT.md", "PIPELINE_STATE.md",
    )
    for relative in terminal_docs:
        text = (SEQ / relative).read_text(encoding="utf-8")
        check("HOLD_EXTERNAL" in text,
              f"terminal batch artifact lacks lifecycle boundary: {relative}")

    round2 = (SEQ / "phase2/ROUND2_REPORT.md").read_text(encoding="utf-8")
    dual = (SEQ / "phase2/DUAL_REVIEW_REPORT.md").read_text(encoding="utf-8")
    integrity_final = (
        SEQ / "phase2/INTEGRITY_REPORT_FINAL.md"
    ).read_text(encoding="utf-8")
    originality_final = (
        SEQ / "phase2/ORIGINALITY_AUDIT_FINAL.md"
    ).read_text(encoding="utf-8")
    final_batch = (SEQ / "qa/FINAL_BATCH_QA.md").read_text(encoding="utf-8")
    final_report = (SEQ / "FINAL_QA_REPORT.md").read_text(encoding="utf-8")
    pipeline = (SEQ / "PIPELINE_STATE.md").read_text(encoding="utf-8")
    expected_fields = {
        "author_assertions": total_author_assertions,
        "review_a_assertions": total_review_a_assertions,
        "review_b_assertions": total_review_b_assertions,
    }
    check(re.search(
        rf"(?im)^review_b_assertions={total_review_b_assertions}\s*$", round2
    ) is not None, "Round-2 report assertion aggregate mismatch")
    for field, value in (
        ("round2_status", "PASS"), ("papers", "5"),
        ("review_replays", "5"),
        ("open_findings", "critical:0,major:0,minor:0"),
        ("external_status", "OWNER_AMBER/HOLD_EXTERNAL"),
    ):
        check(re.search(rf"(?im)^{field}={re.escape(value)}\s*$", round2)
              is not None, f"Round-2 report field mismatch: {field}")
    for number, _, _, _, _, _, review_b_count in rows:
        check(re.search(
            rf"(?im)^P{number}_review_b_assertions={review_b_count}\s*$", round2
        ) is not None, f"Round-2 per-paper aggregate mismatch: P{number}")
    for field, value in expected_fields.items():
        check(re.search(rf"(?im)^{field}={value}\s*$", dual) is not None,
              f"dual-review report aggregate mismatch: {field}")
        check(re.search(rf"(?im)^{field}={value}\s*$", final_batch) is not None,
              f"final batch QA aggregate mismatch: {field}")
    for field, value in (
        ("dual_review_status", "PASS"), ("papers", "5"),
        ("review_replays", "10"),
        ("open_findings", "critical:0,major:0,minor:0"),
        ("external_status", "OWNER_AMBER/HOLD_EXTERNAL"),
    ):
        check(re.search(rf"(?im)^{field}={re.escape(value)}\s*$", dual)
              is not None, f"dual-review report field mismatch: {field}")
    for field, value in (
        ("terminal_status", "PASS"), ("papers", "5"),
        ("review_replays", "10"),
        ("pages", str(total_pages)), ("bibliography_records", str(total_refs)),
        ("cold_builds", "10"), ("visual_pages", str(total_pages)),
        ("pdf_manifest_rows", "20"),
        ("open_findings", "critical:0,major:0,minor:0"),
        ("external_status", "OWNER_AMBER/HOLD_EXTERNAL"),
    ):
        check(re.search(rf"(?im)^{field}={re.escape(value)}\s*$", final_batch)
              is not None, f"final batch QA field mismatch: {field}")
    for text, label in (
        (integrity_final, "integrity final"), (final_report, "final QA report"),
    ):
        for field, value in (
            ("terminal_status", "PASS"), ("papers", "5"),
            ("review_replays", "10"), ("cold_builds", "10"),
            ("visual_pages", str(total_pages)), ("pdf_manifest_rows", "20"),
            ("open_findings", "critical:0,major:0,minor:0"),
            ("external_status", "OWNER_AMBER/HOLD_EXTERNAL"),
        ):
            check(re.search(rf"(?im)^{field}={re.escape(value)}\s*$", text)
                  is not None, f"{label} field mismatch: {field}")
    for field, value in (
        ("failure_mode_population_completeness", "RESOLVED"),
        ("failure_mode_source_drift", "RESOLVED"),
        ("failure_mode_review_collision", "RESOLVED"),
        ("failure_mode_replay_drift", "RESOLVED"),
        ("failure_mode_build_reproducibility", "RESOLVED"),
        ("failure_mode_pdf_anonymity_rendering", "RESOLVED"),
        ("failure_mode_owner_originality_overclaim", "CONTAINED_NOT_CLEARED"),
    ):
        check(re.search(rf"(?im)^{field}={value}\s*$", integrity_final)
              is not None, f"integrity failure-mode field mismatch: {field}")
    for field, value in (
        ("originality_status", "BOUNDED_NONHIT_NOT_NOVELTY"),
        ("papers", "5"), ("public_web_screen", "NOT_CHECKED"),
        ("self_plagiarism_closed_corpus", "NOT_CHECKED"),
        ("external_status", "OWNER_AMBER/HOLD_EXTERNAL"),
    ):
        check(re.search(rf"(?im)^{field}={re.escape(value)}\s*$",
                        originality_final) is not None,
              f"originality final field mismatch: {field}")
    check(re.search(r"(?im)^- current stage: Stage 6\b", pipeline) is not None,
          "pipeline is not at Stage 6")
    check(re.search(
        r"(?im)^- current status: .*COMPLETE.*HOLD_EXTERNAL\s*$", pipeline
    ) is not None, "pipeline terminal status is not complete/held")
    check(re.search(
        r"(?im)^\| 5\. hostile Review B \| \*\*complete\*\* \|", pipeline
    ) is not None, "pipeline Review-B row is not complete")
    check(re.search(
        r"(?im)^\| 6\. cold QA and manifests \| \*\*complete\*\* \|", pipeline
    ) is not None, "pipeline terminal-QA row is not complete")

    sequence_names = manifest(SEQ)
    sequence_payload = {
        path.relative_to(SEQ).as_posix() for path in SEQ.rglob("*")
        if path.is_file() and path != SEQ / "SHA256SUMS"
    }
    check(sequence_names == sequence_payload,
          "sequence manifest population mismatch")
    qa_names = manifest(SEQ / "qa")
    check(qa_names == {"audit_batch.py", "run_final_cold_builds.sh",
                       "CANONICAL.txt", "FINAL_BATCH_QA.md"},
          "QA manifest population mismatch")

    expected_pdf_rows = {
        f"papers/{directory.name}/{name}": sha(directory / name)
        for directory in PAPERS.values() for name in ROUND_PDFS
    }
    actual_pdf_rows = {}
    pdf_manifest = SEQ / "CANONICAL_PDF_MANIFEST.sha256"
    for line_no, line in enumerate(
        pdf_manifest.read_text(encoding="utf-8").splitlines(), 1
    ):
        if not line.strip():
            continue
        match = re.fullmatch(r"([0-9a-f]{64})\s+(.+)", line)
        check(match is not None, f"bad PDF manifest row {line_no}")
        if match is None:
            continue
        digest, relative = match.groups()
        check(relative not in actual_pdf_rows,
              f"duplicate PDF manifest target: {relative}")
        actual_pdf_rows[relative] = digest
    check(actual_pdf_rows == expected_pdf_rows,
          "canonical PDF manifest population/hash mismatch")

    expected_package_rows = {
        (directory / "SHA256SUMS").relative_to(ROOT).as_posix()
        for directory in PAPERS.values()
    } | {
        (directory / "qa_final/SHA256SUMS").relative_to(ROOT).as_posix()
        for directory in PAPERS.values()
    } | {
        (directory / "SHA256SUMS").relative_to(ROOT).as_posix()
        for review_pair in REVIEWS.values() for directory in review_pair
    } | {(SEQ / "qa/SHA256SUMS").relative_to(ROOT).as_posix()}
    actual_package_rows: dict[str, str] = {}
    package_manifest = SEQ / "PACKAGE_MANIFESTS.sha256"
    for line_no, line in enumerate(
        package_manifest.read_text(encoding="utf-8").splitlines(), 1
    ):
        if not line.strip():
            continue
        match = re.fullmatch(r"([0-9a-f]{64})\s+(.+)", line)
        check(match is not None, f"bad package-manifest row {line_no}")
        if match is None:
            continue
        digest, relative = match.groups()
        target_rel = Path(relative)
        check(not target_rel.is_absolute() and ".." not in target_rel.parts,
              f"unsafe package-manifest target: {relative}")
        check(relative not in actual_package_rows,
              f"duplicate package-manifest target: {relative}")
        target = ROOT / target_rel
        check(target.is_file() and not target.is_symlink(),
              f"missing/symlink package manifest target: {relative}")
        check(sha(target) == digest,
              f"package-manifest digest mismatch: {relative}")
        actual_package_rows[relative] = digest
    check(set(actual_package_rows) == expected_package_rows,
          "package-manifest population mismatch")

    print("ROUTE_A_P187_P191_TERMINAL_MECHANICAL_AUDIT")
    for (number, pdf_hash, pages, references, author_count,
         review_a_count, review_b_count) in rows:
        print(f"P{number}_PDF_SHA256={pdf_hash} PAGES={pages} "
              f"REFERENCES={references} AUTHOR_ASSERTIONS={author_count} "
              f"REVIEW_A_ASSERTIONS={review_a_count} "
              f"REVIEW_B_ASSERTIONS={review_b_count} AUTHOR_REPLAYS=1 "
              f"REVIEWER_REPLAYS=2 COLD_BUILDS=2")
    print(f"TOTAL_PAGES={total_pages}")
    print(f"TOTAL_BIBLIOGRAPHY_RECORDS={total_refs}")
    print(f"TOTAL_AUTHOR_ASSERTIONS={total_author_assertions}")
    print(f"TOTAL_REVIEW_A_ASSERTIONS={total_review_a_assertions}")
    print(f"TOTAL_REVIEW_B_ASSERTIONS={total_review_b_assertions}")
    print(f"TOTAL_PAPER_EVIDENCE_ASSERTIONS="
          f"{total_author_assertions + total_review_a_assertions + total_review_b_assertions}")
    print(f"REVIEW_REPLAYS={REVIEW_REPLAYS}")
    print(f"ASSERTIONS={ASSERTIONS}")
    print("SCOPE=artifact/reference-set/PDF/manifest/replay/cold-build mechanics only")
    print("RESULT=PASS")
    print("RELEASE_SENTINEL=HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
