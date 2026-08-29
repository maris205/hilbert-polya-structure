# Paper-local final QA

Status: **PASS / SEALED LOCALLY / EXTERNAL HOLD**  
QA date: 2026-08-29  
Scope: `papers/113-principal-hook-partition-dynamics/` only

This is a paper-local reproducibility and production audit. It does not
alter or re-review the mathematics, establish novelty or priority, authorize
circulation, or constitute repository-wide batch QA. During this QA run,
the manuscript source, bibliography, verifier, canonical verifier output,
support documents, and canonical PDF were read-only; only this file and
`SHA256SUMS` were added.

## Exact verifier

The verifier was run in a fresh Python process with bytecode disabled:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B code/verify.py
```

Result:

```text
status: PASS
exhaustive range: every partition for 1 <= n <= 40
exact assertions: 10,110,035
fresh/canonical transcript: byte-for-byte equal
transcript size: 45 lines, 6,053 bytes
transcript SHA256: bb0f9de4f5fdbec05b24a2c4636ca09675025a4f0c6b0a8524ec1b6870911571
bytecode artifacts created: 0
```

The canonical transcript is `code/verification_output.txt`; it is included
in the seal.

## Clean-equivalent build and PDF determinism

Only `main.tex` and `references.bib` were copied into a newly created
temporary directory. The isolated build used

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

An additional fifth `pdflatex` pass was then run. All five stages exited
zero. The PDF after the four-stage build, after the extra pass, and the
canonical `main.pdf` have the identical SHA256

```text
2500424b6f42f16ac68e6eac66e6809e3bfdf5ebb212f9450afefd593cfd3569
```

This establishes byte-level settled-build determinism for the audited
environment and source tree.

The settled `main.log` and `main.blg` have zero instances of actual LaTeX,
package, class, or BibTeX warnings/errors; undefined references, citations,
or control sequences; multiply defined labels; overfull or underfull boxes;
and rerun requests. Informational package names and BibTeX's
`warning$ -- 0` statistic were not misclassified as warnings.

## Bibliography, PDF structure, and fonts

The bibliography contains four database entries and the settled BBL contains
four resolved `bibitem` entries. Comparing the reference-key set with the
settled `bibcite` key set gives an empty difference: every database entry is
cited and every citation is resolved.

Canonical PDF properties:

```text
pages: 4
bytes: 325,001
format: PDF 1.5, A4 (595.276 x 841.89 pt)
page rotation: 0
Author metadata: empty
Title/Subject/Keywords metadata: empty
CreationDate/ModDate metadata: absent
custom metadata: no
form: none
JavaScript: no
encrypted: no
font rows: 23
fonts embedded/subset/Unicode mapped: 23/23/23
```

## Extracted-text audit

`pdftotext` extraction found no placeholder marker, unfinished-work marker,
double-question-mark reference, literal `qquad`, internal-author-draft
phrase, verification marker, dummy prose, or citation-needed marker.

## All-page visual audit

All four canonical PDF pages were rendered to PNG at 120 dpi and inspected
individually.

| Page | Material inspected | Result |
|---:|---|---|
| 1 | title, anonymous line, abstract, ownership scope, principal-hook setup | PASS: no clipping, collision, missing glyph, or footer conflict |
| 2 | owned one-step result, global absorption, main gap/depth theorem | PASS: products, theorem numbering, and page break are clean |
| 3 | sharpness proof, small weights, layer transport, conjugation exception | PASS: displayed sums and corollary text are fully legible |
| 4 | fixed-weight zeta, proof routes, falsification controls, bibliography | PASS: zeta display and all four references are intact |

No page shows clipping, overlap, broken rules, missing fonts, blank content,
or an unreadable equation.

## Local seal

`SHA256SUMS` contains 15 entries covering the frozen manuscript source,
canonical PDF, bibliography, verifier and canonical stdout, support
documents, both independent hostile reviews, consolidated resolution ledger,
and this QA report. It includes `code/verification_output.txt` and excludes
the manifest itself and all derived `aux`, `bbl`, `blg`, `log`, and `out`
files, as well as bytecode caches.

`sha256sum -c SHA256SUMS` passes for all 15 entries. No Git operation was
performed. External dissemination, novelty, and priority remain **HOLD**.
