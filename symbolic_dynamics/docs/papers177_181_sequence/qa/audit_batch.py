#!/usr/bin/env python3
"""Deterministic artifact audit for Route-A papers P177--P181.

Run only after Round 2.  This script checks file/provenance structure and PDF
mechanics; it does not certify mathematical truth, experiment design, novelty,
or bibliographic completeness.
"""

from pathlib import Path
import hashlib
import re
import subprocess


ROOT = Path(__file__).resolve().parents[3]
SEQUENCE = ROOT / "docs" / "papers177_181_sequence"
PAPERS = {
    177: ROOT / "papers" / "177-random-projective-hyperplane-toggling",
    178: ROOT / "papers" / "178-state-selected-finite-differences",
    179: ROOT / "papers" / "179-random-singleton-isolation",
    180: ROOT / "papers" / "180-bilinear-radial-scaling",
    181: ROOT / "papers" / "181-first-descent-prefix-reversal",
}
AUTHOR_CONTROLS = {
    177: ("verify_p177.py", "verification_output.txt"),
    178: ("verify_p178.py", "verification_output.txt"),
    179: ("code/verify_p179.py", "code/CANONICAL.txt"),
    180: ("code/verify_p180.py", "code/CANONICAL.txt"),
    181: ("verify_p181.py", "verification_output.txt"),
}
COLD_BUILDS = {
    177: ("qa_final/cold_build_1", "qa_final/cold_build_2"),
    178: ("qa_final/cold_build_1", "qa_final/cold_build_2"),
    179: ("qa_final/cold_build_1", "qa_final/cold_build_2"),
    180: ("qa_final/cold_build_1", "qa_final/cold_build_2"),
    181: ("qa_final/cold_build_1", "qa_final/cold_build_2"),
}


assertions = 0


def check(condition, message):
    global assertions
    assertions += 1
    if not condition:
        raise AssertionError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def command(*args):
    return subprocess.run(args, check=True, text=True,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT).stdout


def audit_paper(number, directory):
    required = [
        "main.tex", "references.bib", "main.pdf",
        "main_round0_original.pdf", "main_round1.pdf", "main_round2.pdf",
        "NARRATIVE_REPORT.md", "PAPER_PLAN.md", "FIGURE_PLAN.md",
        "CLAIMS_EVIDENCE.md", "SOURCE_VERIFICATION.md", "BUILD.md",
        "SELF_QA.md", "IMPROVEMENT_LOG.md", "FINAL_QA.md", "SHA256SUMS",
    ]
    for relative in required:
        check((directory / relative).is_file(), f"P{number} missing {relative}")

    tex = (directory / "main.tex").read_text(encoding="utf-8")
    bib = (directory / "references.bib").read_text(encoding="utf-8")
    check("\\author{Anonymous}" in tex, f"P{number} author is not anonymous")
    check("HOLD" in tex.upper() and "EXTERNAL" in tex.upper(),
          f"P{number} lacks external hold in manuscript")
    check("\\pdfinfoomitdate=1" in tex and "\\pdftrailerid{}" in tex,
          f"P{number} deterministic PDF controls absent")

    bib_keys = set(re.findall(r"@[A-Za-z]+\s*\{\s*([^,\s]+)", bib))
    cite_groups = re.findall(r"\\cite[A-Za-z*]*\{([^}]+)\}", tex)
    cite_keys = {key.strip() for group in cite_groups for key in group.split(",")}
    check(bib_keys == cite_keys,
          f"P{number} citation mismatch bib={sorted(bib_keys)} cite={sorted(cite_keys)}")

    live = directory / "main.pdf"
    round2 = directory / "main_round2.pdf"
    check(live.read_bytes() == round2.read_bytes(), f"P{number} live != Round2")
    for receipt in ("main_round0_original.pdf", "main_round1.pdf", "main_round2.pdf"):
        info = command("pdfinfo", str(directory / receipt))
        check("Pages:" in info and "Encrypted:       no" in info,
              f"P{number} invalid PDF receipt {receipt}")

    info = command("pdfinfo", str(live))
    for field in ("Title", "Author", "Creator", "Producer"):
        match = re.search(rf"^{re.escape(field)}:[ \t]*(.*)$", info,
                          flags=re.MULTILINE)
        check(match is not None and match.group(1).strip() == "",
              f"P{number} metadata {field} is not blank")
    check("JavaScript:      no" in info and "Encrypted:       no" in info,
          f"P{number} PDF active/encrypted")

    fonts = command("pdffonts", str(live)).splitlines()[2:]
    check(bool(fonts), f"P{number} has no font rows")
    for row in fonts:
        fields = row.split()
        check(fields[-5:-2] == ["yes", "yes", "yes"],
              f"P{number} font not embedded/subsetted/Unicode: {row}")

    manifest = subprocess.run(["sha256sum", "-c", "SHA256SUMS"],
                              cwd=directory, text=True,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT)
    check(manifest.returncode == 0, f"P{number} manifest failure\n{manifest.stdout}")

    manifest_names = {
        line.split(None, 1)[1].lstrip("* ")
        for line in (directory / "SHA256SUMS").read_text(encoding="utf-8").splitlines()
        if line.strip()
    }
    verifier_relative, canonical_relative = AUTHOR_CONTROLS[number]
    manifest_required = set(required) - {"SHA256SUMS"}
    manifest_required.update((verifier_relative, canonical_relative))
    check(manifest_required <= manifest_names,
          f"P{number} manifest omits {sorted(manifest_required - manifest_names)}")

    verifier = directory / verifier_relative
    canonical = directory / canonical_relative
    output = command("python3", str(verifier))
    check(output.encode("utf-8") == canonical.read_bytes(),
          f"P{number} author replay mismatch")

    for cold_relative in COLD_BUILDS[number]:
        cold = directory / cold_relative
        check((cold / "main.tex").read_bytes() == (directory / "main.tex").read_bytes(),
              f"P{number} cold source mismatch in {cold_relative}")
        check((cold / "references.bib").read_bytes() ==
              (directory / "references.bib").read_bytes(),
              f"P{number} cold bibliography mismatch in {cold_relative}")
        check((cold / "main.pdf").read_bytes() == live.read_bytes(),
              f"P{number} cold PDF mismatch in {cold_relative}")

    review_root = SEQUENCE / "reviews" / f"paper{number}"
    reviewer_dirs = sorted(path.parent for path in review_root.glob("*/SHA256SUMS"))
    check(len(reviewer_dirs) == 2,
          f"P{number} requires exactly two reviewer manifests")
    for reviewer in reviewer_dirs:
        result = subprocess.run(["sha256sum", "-c", "SHA256SUMS"],
                                cwd=reviewer, text=True,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        check(result.returncode == 0,
              f"P{number} reviewer manifest failure {reviewer}\n{result.stdout}")
        review_manifest_names = {
            line.split(None, 1)[1].lstrip("* ")
            for line in (reviewer / "SHA256SUMS").read_text(
                encoding="utf-8").splitlines()
            if line.strip()
        }
        canonical = next(iter(reviewer.glob("CANONICAL.txt")), None)
        verifier = next(iter(reviewer.glob("verify_*.py")), None)
        check(canonical is not None and verifier is not None,
              f"P{number} reviewer executable evidence missing in {reviewer}")
        output = command("python3", str(verifier))
        check(output.encode("utf-8") == canonical.read_bytes(),
              f"P{number} reviewer replay mismatch in {reviewer}")
        canonical_text = canonical.read_text(encoding="utf-8")
        check(re.search(r"(?im)^result=pass(?:$|_with_)", canonical_text) is not None,
              f"P{number} reviewer canonical lacks a PASS sentinel in {reviewer}")
        check("EXPECTED_MANUSCRIPT_SUPPORT_DEFECT" not in canonical_text,
              f"P{number} reviewer canonical retains a repaired defect sentinel")

        reports = list(reviewer.glob("HOSTILE_REVIEW*.md"))
        deltas = list(reviewer.glob("DELTA*.md"))
        check(len(reports) == 1 and len(deltas) == 1,
              f"P{number} reviewer report/delta receipt missing in {reviewer}")
        review_required = {
            canonical.name, verifier.name, reports[0].name, deltas[0].name
        }
        check(review_required <= review_manifest_names,
              f"P{number} reviewer manifest omits "
              f"{sorted(review_required - review_manifest_names)} in {reviewer}")
        check("- [ ]" not in deltas[0].read_text(encoding="utf-8"),
              f"P{number} reviewer delta has an unresolved checkbox in {reviewer}")

    return digest(live)


def main():
    hashes = []
    for number, directory in PAPERS.items():
        hashes.append((number, audit_paper(number, directory)))
    print("ROUTE_A_P177_P181_FINAL_ARTIFACT_AUDIT")
    for number, value in hashes:
        print(f"P{number}_PDF_SHA256={value}")
    print(f"ASSERTIONS={assertions}")
    print("SCOPE=artifact/reference-set/PDF/reviewer-replay mechanics only")
    print("RESULT=PASS")
    print("RELEASE_SENTINEL=HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
