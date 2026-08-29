# P112 paper-local final QA

Status: **PASS / FROZEN PAPER-LOCAL ARTIFACT / EXTERNAL HOLD**.

QA date: 2026-08-29 UTC.

Scope: only `papers/112-tournament-score-upset-reversal/`.  The frozen
`main.tex`, `references.bib`, verifier, canonical verifier output, support
documents, hostile reviews, and `main.pdf` were treated as read-only.  The
four-stage build and render products were created in an isolated temporary
directory.  This QA adds only `FINAL_QA.md` and `SHA256SUMS`; it does not alter
the paper, verifier, canonical output, PDF content, batch documents, or Git
state.

This is a mechanical and internal-consistency clearance.  It does not change
the manuscript's owner, novelty, priority, or external-dissemination status;
those remain **HOLD**.

## 1. Frozen input inventory

All required frozen inputs were present before QA:

- `main.tex`: 24,431 bytes;
- `main.pdf`: 332,780 bytes;
- `references.bib`: 4,086 bytes;
- `code/verify.py`: 12,581 bytes;
- `code/verification_output.txt`: 781 bytes;
- `README.md`, `BUILD.md`, `CONTROL_RESULTS.md`, `CLAIMS_EVIDENCE.md`,
  `NARRATIVE_REPORT.md`, and `PAPER_PLAN.md`;
- `HOSTILE_REVIEW_A.md`, `HOSTILE_REVIEW_B.md`, and consolidated
  `HOSTILE_REVIEW.md`.

No section fragments, figures, or other manuscript source dependencies are
present; `main.tex` and `references.bib` are the complete LaTeX inputs.

## 2. Fresh exact verifier and canonical comparison

Fresh command:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
```

Byte comparison:

```bash
cmp -s code/verification_output.txt \
  <(PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py)
```

Result: **PASS**.

- assertions: **1,677,508**;
- labelled states enumerated: **33,868**;
- canonical stdout size: **781 bytes**;
- fresh/canonical byte comparison: **identical**;
- regular counts: `[0,1,0,2,0,24,0]`;
- fixed counts: `[1,1,2,8,40,264,2048]`;
- scan-qualified nonidempotence output remains
  `least_nonidempotent_in_specified_scan`, with the recorded order-six state
  `148 -> 4 -> 0 -> 0`.

## 3. Isolated build and PDF determinism

Only `main.tex` and `references.bib` were copied to an isolated directory.
The repository-standard build was run there:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

An additional settled pass was then run:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The SHA-256 digest after the four-stage build, after the additional pass, and
for the frozen paper-local PDF was identical:

```text
034d0242693c5f62b478f54f761aa04b6b42102293e5f67f5ad6ac017813c77d
```

Direct byte comparison between the isolated PDF and frozen `main.pdf` also
passed.  Thus the extra pass is settled and the PDF is byte-deterministic in
the tested environment.

## 4. Settled LaTeX, BibTeX, and bibliography closure

The final isolated `main.log` and `main.blg` were scanned directly.

- LaTeX/package/pdfTeX warnings: **0**;
- BibTeX warnings or errors: **0**;
- undefined citations: **0**;
- undefined references: **0**;
- multiply defined labels: **0**;
- overfull boxes: **0**;
- underfull boxes: **0**;
- fatal TeX errors: **0**.

Bibliography closure was checked three ways:

- entries in `references.bib`: **13**;
- `\bibcite` records in the settled auxiliary file: **13**;
- `\bibitem` records in the settled bibliography: **13**;
- database-key versus cited-key set difference: **empty**.

Result: **13/13 bibliography closure PASS**.

## 5. PDF structure and metadata

`pdfinfo`, a raw PDF date-key scan, `pdfdetach`, and per-page geometry checks
gave:

- pages: **8**;
- file size: **332,780 bytes**;
- PDF version: **1.5**;
- all pages: **595.276 x 841.89 pt (A4)**;
- all page rotations: **0**;
- `Author`: **empty**;
- printed manuscript date: **absent**;
- `CreationDate` and `ModDate`: **absent** from `pdfinfo` and raw PDF keys;
- `Form`: **none**;
- `JavaScript`: **no**;
- encryption: **no**;
- embedded files: **0**;
- metadata stream: **no**;
- custom metadata: **no**.

The visible author line remains the intended anonymous label; there is no
identity-bearing PDF author metadata.

## 6. Fonts

`pdffonts` reports **23** fonts.  All are Type 1, and all **23/23** are:

- embedded;
- subsetted;
- Unicode-mapped.

Result: **font gate PASS**.

## 7. Extracted-text and source sentinels

The complete eight-page PDF was extracted with `pdftotext -layout` and scanned
for unresolved or stale material.  All of the following counts are zero:

- `??` and `[?]`;
- `[VERIFY]`, `TODO`, `FIXME`, and `TBD`;
- `Internal author draft` and the removed internal draft date;
- an erroneous comma before `t-1` in the iterate formula;
- text claiming that `Phi_C` is undefined.

The positive context checks also passed:

- page 2 states that every edge reads the unchanged input scores and that all
  decisions are applied simultaneously;
- page 2 defines `Phi_C` on label set `C` using internal scores;
- page 3 identifies `Phi_{C_i}` as the restriction/update operator;
- displayed equation (7) visibly has both superscripts `t-1` with no comma;
- the source contains no `^{,` superscript fragment.

Result: **text/sentinel gate PASS**.

## 8. Eight-page visual inspection

All pages were freshly rendered at 120 dpi and inspected individually.

| Page | Inspection focus | Result |
|---:|---|---|
| 1 | anonymous title block, no printed date, abstract, recurrence/EGF display, introduction | PASS |
| 2 | arbitrary-label definition, simultaneous update, `Phi_C` definition, Lyapunov statement | PASS |
| 3 | incidence proof, factorization, corrected equation (7), well-foundedness text | PASS |
| 4 | depth recursion and bound, boundary cases, regular-block theorem | PASS |
| 5 | recurrence/EGF, zeta, start of exact controls | PASS |
| 6 | exhaustive table, scan-qualified mask 148 orbit, mechanics table, owner ledger | PASS |
| 7 | scope/HOLD language, P106 firewall, limits, conclusion, references 1--8 | PASS |
| 8 | references 9--13 and terminal whitespace | PASS |

No page has clipping, overlap, missing glyphs, broken rules, blank content,
unreadable tables, malformed mathematics, or unexpected rotation.  The owner
mechanics table is dense but legible, and all reference continuations remain
inside the text block.

## 9. Integrity manifest

`SHA256SUMS` covers exactly these 15 frozen or QA files:

1. `main.tex`;
2. `main.pdf`;
3. `references.bib`;
4. `code/verify.py`;
5. `code/verification_output.txt`;
6. `README.md`;
7. `BUILD.md`;
8. `CONTROL_RESULTS.md`;
9. `CLAIMS_EVIDENCE.md`;
10. `NARRATIVE_REPORT.md`;
11. `PAPER_PLAN.md`;
12. `HOSTILE_REVIEW_A.md`;
13. `HOSTILE_REVIEW_B.md`;
14. `HOSTILE_REVIEW.md`;
15. `FINAL_QA.md`.

The manifest deliberately excludes itself and all generated build products
other than the frozen PDF, including `main.aux`, `main.bbl`, `main.blg`,
`main.log`, `main.out`, render files, temporary build outputs, and
`__pycache__`.

Verification command:

```bash
sha256sum -c SHA256SUMS
```

Result: **15/15 OK**.

## Final disposition

**PAPER-LOCAL FINAL QA PASS.**  The frozen source, bibliography, verifier,
canonical output, support/review record, and PDF are mutually consistent; the
PDF is reproducible under the specified isolated build and passes the stated
mechanical, metadata, font, text, and visual gates.  External dissemination
remains **HOLD**.  No batch document or Git operation was performed.
