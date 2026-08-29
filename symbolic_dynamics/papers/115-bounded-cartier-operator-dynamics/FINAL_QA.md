# Paper-local final QA — P115

## Verdict and scope

**PASS — frozen paper-local package.** This audit is limited to
`papers/115-bounded-cartier-operator-dynamics/`. It does not alter or reassess
the manuscript's external **HOLD** on release, novelty, or priority. The
manuscript source, verifier, canonical verifier output, bibliography, support
documents, hostile reviews, and frozen PDF were not edited during final QA.
All compilation and rendering intermediates were created in an isolated
temporary directory.

## Frozen artifact

- PDF: `main.pdf`
- Pages: **7**, all A4
- Bytes: **397,625**
- SHA-256:
  `deacaa7eea3c0c5734a2cc7a100e3e16951f90d5205af3e49b2f2d05c3d5c3de`
- PDF version: 1.5

## Exact verifier and canonical-output closure

A fresh `python3 code/verify.py` run exited zero and ended with:

```text
PASS: 2,259,162 exact assertions
```

- Fresh stdout: **14 lines, 1,449 bytes**
- Fresh/canonical `cmp`: **0** (byte-identical)
- Fresh and canonical stdout SHA-256:
  `bee01c4b0e94a0bc3682e7cc6d9ff716f43b100baf4bab5ea1d0ab0bc9ef7011`

The assertion total is the verifier's raw count of executed checks, not a
count of logically independent mathematical statements.

## Isolated deterministic build

The isolated build used the following settled sequence:

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex  # extra determinism pass
```

All five commands exited zero. The fourth-stage PDF, extra-pass PDF, and
frozen paper-local PDF were byte-identical:

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| fourth-stage PDF | 397,625 | `deacaa7eea3c0c5734a2cc7a100e3e16951f90d5205af3e49b2f2d05c3d5c3de` |
| extra-pass PDF | 397,625 | `deacaa7eea3c0c5734a2cc7a100e3e16951f90d5205af3e49b2f2d05c3d5c3de` |
| frozen `main.pdf` | 397,625 | `deacaa7eea3c0c5734a2cc7a100e3e16951f90d5205af3e49b2f2d05c3d5c3de` |

Both byte comparisons returned zero. The extra pass therefore made no PDF
content change.

## Settled diagnostics and bibliography

The final isolated `main.log` and `main.blg` have:

- LaTeX/package/class/font warnings: **0**
- errors: **0**
- overfull boxes: **0**
- underfull boxes: **0**
- undefined or multiply defined citations/references: **0**
- rerun requests: **0**
- BibTeX warnings/errors: **0**

Bibliographic closure is **9/9**: the nine unique citation keys in `main.aux`,
the nine entries in `references.bib`, and the nine items in `main.bbl` are
identical sets. There are no missing or uncited entries. The closed keys are:

```text
Bridy2017, Cartier1957, Elspas1959, HernandezToledo2005, Jeong2018,
LidlNiederreiter1997, PanarioReis2019, Reis2023, Wang1967
```

## PDF metadata and safety surface

`pdfinfo main.pdf` gives the following closed checks:

- pages: **7**
- page size: **595.276 x 841.89 pts (A4)**
- CreationDate/ModDate: **absent**
- Author: **empty**
- Form: **none**
- JavaScript: **no**
- encrypted: **no**
- page rotation: **0**

## Fonts and text extraction

`pdffonts main.pdf` reports **27/27 embedded**, **27/27 subsetted**, and
**27/27 Unicode-mapped** fonts; no font row fails any of the three checks.

Fresh `pdftotext` extraction contains **662 lines and 22,920 bytes** and
resolves to seven text pages. Positive sentinels include the title; the six
principal theorem headings; the `2,259,162 exact assertion executions` line;
the references heading; Jeong and Hernández Toledo bibliography entries; and
the external-HOLD statement. The strings `??`, `[?]`, `[VERIFY]`, and
`Internal Stage 2` are absent.

## Visual audit

All seven frozen PDF pages were freshly rendered at 150 dpi and individually
inspected. No page has clipping, collision, blank content, missing glyphs,
malformed displays, broken rules, unreadable references, or visible hyperlink
damage. Page flow across theorem/proof boundaries and the final bibliography
is intact.

## Integrity manifest

`SHA256SUMS` contains **15** paper-local entries covering the manuscript
source, frozen PDF, bibliography, verifier source, canonical verifier output,
README/build/control/claims/narrative/plan documents, both hostile reviews,
the consolidated hostile-review ledger, and this final-QA report.

The manifest intentionally excludes itself and all generated
`aux/bbl/blg/log/out` files and `__pycache__` artifacts. The final command

```text
sha256sum -c SHA256SUMS
```

returns **15/15 OK**. This is a byte-integrity record for the frozen local
package, not an owner-completeness or external-release certificate.
