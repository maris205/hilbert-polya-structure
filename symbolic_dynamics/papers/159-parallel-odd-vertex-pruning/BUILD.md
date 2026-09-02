# Build and review-artifact record — P159

**Date:** 2026-09-02 UTC  
**Status:** `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

## Toolchain and command

- Engine: pdfTeX 1.40.22 / LaTeX2e 2021-11-15.
- Class: anonymous amsart, 10 pt, A4, 27 mm margins.
- Typography: Latin Modern; microtype protrusion retained and font expansion
  disabled.
- Settled sequence:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The retained command logs are `build_pdflatex_1.log`, `build_bibtex.log`,
`build_pdflatex_2.log`, and `build_pdflatex_3.log`.  A further settling pass
left the PDF byte-identical.

## Round-0 artifact

| Check | Value |
|---|---|
| Immutable Round-0 freeze | `main_round0_original.pdf` |
| Freeze integrity | preserved unchanged after Review A |
| Pages / format | 5 / A4 |
| Size | 363,455 bytes |
| SHA-256 | `bba68d57e9f46cda2996db072b703ff0b18e5d19c7edab2a53ef24d3032c8602` |
| References | 6/6 cited and resolved |
| Encryption / forms / JavaScript | none / none / none |
| Identifying metadata | title, author, subject, and keywords blank |

The settled pass has no unresolved citation or reference, rerun request,
build error, overfull box, underfull box, or pdfTeX font-expansion warning.
All 27 reported font rows are embedded, subsetted, and Unicode mapped.

Two independent temporary directories were then populated with only
`main.tex` and `references.bib` and ran the same four-command sequence.  The
two source-only PDFs were byte-identical to one another and to the settled
current/Round-0 artifact, with the same size and SHA-256.

## Exact-control freeze

- Fresh verifier replays versus `verification_output.txt`: 2/2 byte-identical.
- Assertions: 3,167,525, using integer and GF(2) exact arithmetic.
- States: 41,658 through ambient order six.
- Independent parity systems: 511 through total order nine.
- Transcript SHA-256:
  `363d77a151dfa0b1d6b4ded84700d01dd249ed242573bff98fa38d490a1d4879`.
- Verifier SHA-256:
  `ffb7e464f665731a2dcb2dc3fabff724594d7420eea8edded64d33e13b413c5d`.

## Content and visual gate

- The extracted PDF contains no `??`, `[?]`, `TODO`, `FIXME`, `XXX`, or
  `[VERIFY]` marker.
- Matrix direction and all mandatory `d=0`, `s=0,d=2`, `n=0,1`, and `t=0`
  boundaries occur in the manuscript, not only in supporting documents.
- All five pages were rasterized for Round-0 visual inspection; equations,
  theorem lists, audit table, declarations, and six references are within the
  page bounds and legible.

## Review boundary

The phase-one hostile gate was a pre-paper candidate gate.  It is not a formal
Review A or Review B of this manuscript.  No manuscript hostile-review file or
post-review PDF is created at Round 0.  External state remains `HOLD_EXTERNAL`.

## Review-A pass and Round-1 artifact

Formal Review A returned zero Critical, zero Major, and zero Minor findings.
No mathematical or executable repair was made.  The declarations sentence
was made lifecycle-neutral before the Round-1 freeze; all external
prohibitions are unchanged.

| Check | Value |
|---|---|
| Current / Round-1 PDFs | `main.pdf` / `main_round1.pdf` |
| Pages / format | 5 / A4 |
| Size | 363,444 bytes |
| SHA-256 | `72c0ca96d3afde550b05677e61454ba5c9fcdb819c6332c92baaa0045fe4b05d` |
| Current versus Round 1 | byte-identical |
| Current versus Round 0 | lifecycle-label difference only; Round 0 preserved |

The retained Round-1 logs are `build_round1_pdflatex_1.log`,
`build_round1_bibtex.log`, `build_round1_pdflatex_2.log`, and
`build_round1_pdflatex_3.log`.  The settled log has zero selected warning,
bad-box, undefined-reference, or rerun lines.  All 27 font rows remain
embedded, subsetted, and Unicode mapped; all five pages passed visual QA.

## Review-B ledger repair and Round-2 freeze

Review B returned zero Critical, zero Major, and one Minor finding: a stale
review-status sentence in `CLAIMS_EVIDENCE.md`.  That ledger sentence was
corrected.  No manuscript or executable artifact changed, so `main.pdf`,
`main_round1.pdf`, and `main_round2.pdf` are byte-identical: 5 A4 pages,
363,444 bytes, SHA-256
`72c0ca96d3afde550b05677e61454ba5c9fcdb819c6332c92baaa0045fe4b05d`.
Both Review-B source-only builds matched this PDF; its settled log remains
warning-free and all 27 font rows remain embedded, subsetted, and Unicode
mapped.
