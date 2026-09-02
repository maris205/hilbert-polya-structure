# Build and Round-2 freeze record — P152

**Date:** 2026-09-02 UTC.  
**Status:** ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL.

## Toolchain and command

- Engine: pdfTeX 1.40.22 / LaTeX2e 2021-11-15.
- Class: anonymous amsart, 10 pt, A4, 27 mm margins.
- Settled sequence:

~~~bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
~~~

The retained paper-local logs are `build_pdflatex_1.log`,
`build_bibtex.log`, `build_pdflatex_2.log`, and `build_pdflatex_3.log`.
A further settling pass left the PDF byte-identical.

## Historical Round-0 artifact

`main_round0_original.pdf` was not overwritten.  It remains 5 A4 pages,
338,268 bytes, with SHA-256
`f2c2476df00d223fdacaf8fb28954d5f620b10611087c3ff35b16ea158f17e57`.
It records the exact pre-Review-A author freeze.

## Historical Round-1 artifact

`main_round1.pdf` remains the immutable Review-A repair freeze: 5 A4 pages,
339,258 bytes, SHA-256
`2ac0da7bc87f8ce1fcc8d730eb95a9dd0c79c7bc870f5f7e40a30593bc2f59d9`.
It is intentionally distinct from both Round 0 and the candidate-domain
wording repair in Round 2.

## Settled Round-2 artifact

| Check | Value |
|---|---|
| Current PDF | `main.pdf` |
| Round-2 freeze | `main_round2.pdf` |
| Pages / format | 5 / A4 |
| Size | 338,933 bytes |
| SHA-256 | `6671feaadf044abe0e4597a0c81064d9e1bc7590e3891e2acbbd6bf94daec8f6` |
| Current versus Round 2 | byte-identical |
| Historical freezes | Round 0 and Round 1 preserved unchanged |
| References | 5/5 cited and resolved |
| Encryption / forms / JavaScript | none / none / none |
| Identifying metadata | title, author, subject, and keywords blank |

## Deterministic source-only reproduction

Two independent temporary directories were populated only with `main.tex`
and `references.bib`.  Each ran the four-command sequence above.  Both
isolated PDFs were byte-identical to each other and to the settled current
and Round-2 artifacts, with the same 338,933-byte size and SHA-256.

The final pass has no unresolved citation/reference, rerun request, build
error, overfull box, or underfull box.  All 25 reported font rows are
embedded, subsetted, and Unicode mapped.

## Exact control and visual gate

- A fresh verifier replay matched `verification_output.txt` byte for byte.
- Assertions: 199,581, all exact integer/rational.
- Transcript SHA-256:
  `da908cb14d7825573b0c43870c96155c55b1b40d4d394eef3f1e972071fa1083`.
- The new exact lanes include 7,335 inverse candidates, 12 explicit
  infeasible candidates, both scalar collision pairs, 8,190 weighted
  private/spine words, and 546 finite tail-bound instances.
- All five pages were rasterized and inspected.  The ownership table,
  theorem, `r=1/r=2/z=0` display, Chebyshev proof, inverse counterexamples,
  expanded audit table, repaired candidate-domain statement, declarations,
  and five references are legible and
  within page bounds.

## Manifest and review state

At the Round-1 checkpoint, `SHA256SUMS` covered all 27 other then-retained
files and passed a cold checksum replay.  For final Round-2 freeze it is
regenerated separately, after these ledgers settle, over all 29 other
retained paper-local files, including both reviews and all three historical
round PDFs.

Review A returned 0 Critical / 0 Major / 2 Minor and Review B returned
0 Critical / 0 Major / 1 Minor.  Every item is repaired and documented in
`IMPROVEMENT_LOG.md`; surviving severity is 0 / 0 / 0.  No external service
is part of this record; scoped repository synchronization is recorded at the
batch level.
