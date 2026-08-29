# Final mechanical QA — P109

QA date: 2026-08-29 UTC.  Status: **PASS / INTERNAL FREEZE / EXTERNAL
HOLD**.

This is a mechanical production audit of the frozen, anonymously authored
P109 package.  It is not an external referee report, specialist ownership
clearance, novelty finding, or authorization to circulate.  No mathematical
source repair was required during this QA.

## 1. Canonical exact control

Run from the paper directory:

```bash
python3 code/verify.py > /tmp/p109-final-qa-verifier.txt
diff -u code/verification_output.txt /tmp/p109-final-qa-verifier.txt
python3 -m py_compile code/verify.py code/verify_nilpotent_image.py
```

Results:

- verifier exit status: 0;
- final line: `PASS: 515,379 exact assertions`;
- fresh stdout versus stored stdout: byte-identical, empty diff;
- stored stdout: 1,388 bytes;
- stored stdout SHA-256:
  `21f744fbeb1f952de370d8dd0604727ff196d1d8798f679f038a9baa079ce99c`;
- syntax check of both verifier files: PASS.

## 2. Four-stage build and determinism

The complete sequence was run twice on the unchanged final source:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Both sequences passed.  The PDF hash after each sequence was exactly

```text
d71468be5407a28719fe755074a63d3006377572866bf9aa3a160367fc652d34  main.pdf
```

The deterministic rebuild comparison was an empty diff.

## 3. Log and bibliography audit

The final `main.log`, `main.blg`, and captured output of all eight build
stages were scanned for LaTeX/package/pdfTeX/BibTeX warnings, undefined
citations or references, multiply defined labels, overfull and underfull
boxes, fatal errors, emergency stops, and actionable rerun requests.

| check | count |
|---|---:|
| actionable warnings | 0 |
| undefined citations | 0 |
| undefined references | 0 |
| multiply defined labels | 0 |
| overfull boxes | 0 |
| underfull boxes | 0 |
| fatal errors / emergency stops | 0 / 0 |
| actionable rerun requests | 0 |
| BibTeX warnings (`warning$`) | 0 |

Occurrences of the package name `rerunfilecheck` and its final unchanged-file
informational line are not rerun requests.  The final log reports that
`main.out` is unchanged.

The bibliography has 7 database keys, 7 cited keys in `main.aux`, and 7
resolved `main.bbl` items.  The three exact set differences
`bib-minus-bbl`, `bib-minus-cited`, and `cited-minus-bib` are empty.  The
resolved keys are:

```text
ArtinMazur1965
BenderEtAl1992
BrickmanFillmore1967
Fripertinger2011
GoldmanRota1970
Prasad2010
Ram2026
```

## 4. PDF structure and searchable text

`pdfinfo main.pdf` reports:

- pages: 5;
- file size: 302,089 bytes;
- page size: `595.276 x 841.89 pts (A4)`;
- PDF version: 1.5;
- Author: empty;
- encryption: no;
- form: none;
- JavaScript: no;
- page rotation: 0;
- suspicious objects: none.

Both `pdftotext -layout` and plain `pdftotext` completed successfully:

- layout extraction: 17,773 bytes, 267 lines;
- plain extraction: 13,161 bytes, 421 lines.

The extracted text is nonempty and searchable.  Searches of both extractions
found zero occurrences of `??`, `[?]`, `TODO`, `FIXME`, `VERIFY`, or literal
`qquad`.  A PCRE negative-lookbehind scan also found no bare `qquad` in the
LaTeX/BibTeX sources; valid `\qquad` commands are not flagged.

## 5. Fonts

`pdffonts main.pdf` reports 22 font entries.  Every one has
`emb=yes`, `sub=yes`, and `uni=yes`; noncompliant rows: 0.

## 6. Visual inspection

All five pages were independently rasterized and visually inspected at both
requested resolutions:

| render | images | pixel dimensions per page | result |
|---|---:|---:|---|
| 120 dpi | 5 | 993 x 1,404 | PASS |
| 150 dpi | 5 | 1,241 x 1,754 | PASS |

No clipping, overlap, missing glyph, malformed formula, unresolved citation,
broken color link, blank page, orphan reference page, or illegible material
was found.  The title/anonymous byline, all displayed formulas, theorem
boundaries, the control table, and all seven references render correctly.

## 7. Frozen manifest

`SHA256SUMS` contains exactly these 14 files:

```text
main.tex
references.bib
code/verify.py
code/verify_nilpotent_image.py
code/verification_output.txt
README.md
CLAIMS_EVIDENCE.md
CONTROL_RESULTS.md
BUILD.md
HOSTILE_REVIEW_A.md
HOSTILE_REVIEW_B.md
HOSTILE_REVIEW.md
FINAL_QA.md
main.pdf
```

The manifest excludes itself and all transient build products
(`main.aux`, `main.bbl`, `main.blg`, `main.log`, and `main.out`).  Final
`sha256sum -c SHA256SUMS` result: **PASS, 14/14**.

## Final disposition

- mathematical package after hostile reviews A/B: **GO_INTERNAL**;
- canonical exact evidence: **PASS**;
- final PDF and reproducibility checks: **PASS**;
- package integrity manifest: **PASS**;
- public posting, submission, specialist contact, novelty, and priority:
  **HOLD_EXTERNAL**.
