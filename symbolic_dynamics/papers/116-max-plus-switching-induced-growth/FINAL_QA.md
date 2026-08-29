# Paper-local final QA

Status: **PASS / SEALED LOCALLY / EXTERNAL HOLD**  
QA date: 2026-08-29  
Scope: `papers/116-max-plus-switching-induced-growth/` only

This is a paper-local reproducibility and production audit. It does not
alter or re-review the mathematical content, establish novelty or priority,
authorize circulation, or constitute repository-wide batch QA. During this
QA run, the manuscript sources, verifier, canonical verifier output, support
documents, and canonical PDF were read-only; only this file and
`SHA256SUMS` were added.

## Exact verifier

The verifier was run in a fresh Python process with bytecode disabled:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B code/verify.py
```

Result:

```text
status: PASS
exact assertions: 1,183,356
literal words: 131,071 through n <= 16
biased law/PGF horizon: n <= 32
fresh/canonical transcript: byte-for-byte equal
transcript size: 34 lines, 974 bytes
transcript SHA256: 1dbcb360f41fe4b5adf9f2b57f9d4d75a329f8e3d7451514a6912b7d2239baf2
bytecode artifacts created: 0
```

The canonical transcript is `code/verify.out`; it is included in the seal.

## Clean-equivalent build and PDF determinism

Only `main.tex`, `math_commands.tex`, `references.bib`, and the eight files
under `sections/` were copied into a newly created temporary directory. The
isolated build used

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
7832e9d8b16e5fd72b34b5cf7c683b66ab201b92e2e5fcdafe96995833148c59
```

This establishes byte-level settled-build determinism for the audited
environment and source tree.

The settled `main.log` and `main.blg` have zero instances of actual LaTeX,
package, class, or BibTeX warnings/errors; undefined references, citations,
or control sequences; multiply defined labels; overfull or underfull boxes;
and rerun requests. Informational package names and BibTeX's
`warning$ -- 0` statistic were not misclassified as warnings.

## Bibliography, PDF structure, and fonts

The bibliography contains 14 database entries and the settled BBL contains
14 resolved `bibitem` entries. Comparing the reference-key set with the
settled `bibcite` key set gives an empty difference: every database entry is
cited and every citation is resolved.

Canonical PDF properties:

```text
pages: 10
bytes: 419,711
format: PDF 1.5, A4 (595.276 x 841.89 pt)
page rotation: 0
Author metadata: empty
Title/Subject/Keywords metadata: empty
CreationDate/ModDate metadata: absent
custom metadata: no
form: none
JavaScript: no
encrypted: no
font rows: 29
fonts embedded/subset/Unicode mapped: 29/29/29
```

## Extracted-text audit

`pdftotext` extraction found no placeholder marker, unfinished-work marker,
double-question-mark reference, literal `qquad`, internal-author-draft
phrase, verification marker, dummy prose, or citation-needed marker. The
Perron-derivative display extracts with spacing between the first and second
derivative identities; the former visible `qquad` defect is absent.

## All-page visual audit

All ten canonical PDF pages were rendered to PNG at 105 dpi and inspected
individually.

| Page | Material inspected | Result |
|---:|---|---|
| 1 | title, anonymous author line, abstract, introduction opening | PASS: no clipping, collision, missing glyph, or footer conflict |
| 2 | contribution list, proof-route description, neutral-generator proposition | PASS: equations and page break are clean |
| 3 | four-word reset table and proof, endpoints, projective-dynamics opening | PASS: matrix rows, rules, and theorem text are aligned and legible |
| 4 | five-gap and lumped tables, orientation sentinel, finite PGF/cubic | PASS: tables and boxed equations are intact |
| 5 | stationary law, drift, SLLN/CLT, martingale table | PASS: formulas and table rules are unobstructed |
| 6 | variance derivation, Perron derivatives, pressure theorem opening | PASS: intended derivative spacing is visible; no `qquad` text |
| 7 | Gärtner--Ellis proof, exact support, rare masses, temperature edge | PASS: boxed support and construction are fully visible |
| 8 | negative-temperature limit, complementary routes, owner subtraction | PASS: wide table and list fit without collision |
| 9 | mechanism-comparison table, exact controls, conclusion, references start | PASS: table cells, HOLD line, and reference transition are clean |
| 10 | remaining bibliography | PASS: all 14 entries are legible; no truncation or orphan artifact |

No page shows clipping, overlap, broken rules, missing fonts, blank content,
or an unreadable equation.

## Local seal

`SHA256SUMS` contains 24 entries covering the frozen paper sources,
canonical PDF, bibliography, verifier and canonical stdout, support
documents, both independent hostile reviews, consolidated resolution
ledger, and this QA report. In particular, it includes
`math_commands.tex`, every `sections/*.tex` file, and `code/verify.out`.

The manifest excludes itself and all derived `aux`, `bbl`, `blg`, `log`, and
`out` files, as well as bytecode caches. `sha256sum -c SHA256SUMS` passes for
all 24 entries. No Git operation was performed.

External circulation, novelty, and priority remain **HOLD**.
