# Paper 28 Stage-5 finalization package

Status: **Stage 5 final paper complete; Stage 6 remains pending**.

## Authoritative deliverables

- `manuscript.tex` is the author-confirmed, marker-stripped LaTeX source,
  SHA-256
  `14ad8eeaa7cdd55bc889adc250630a7b18a9e20e316d4fb6becddb9e05922d22`.
- `references.bib` is the unchanged six-entry bibliography, SHA-256
  `95728b0a7120e5df341a364ff77f65f5c1d4628d55a6e584e2de7d747d8ca63e`.
- `paper.pdf` is the reproducible 14-page A4 final paper, SHA-256
  `be156f76fcf3f31ecdc2d8be5dde5ccf7aaf7f0b530c7dc8efc9b889e3633cc9`.
- `content_proof.pdf` is the accepted 14-page Stage-4.5 proof, retained as
  provenance, SHA-256
  `253d10080331076a14d658afc423a72b2f687eadcfb68c6e482cec03aabae382`.
- `provenance_summary.md` records input locks, build equivalence, #660/#672
  limitations, Route boundaries, and every non-passing package-verifier row.
- `submission_verification_report.json` is the machine-readable ARS package
  report; its freshness must be checked before reuse.

The final PDF and accepted proof have the identical `pdftotext -layout`
SHA-256
`2e7c021043d9d5e00e561bcc134a047df00f957d39b91bf48fd856f74861f1ff`.
The citation profile remains
`natbib[numbers,sort&compress] + \bibliographystyle{plainnat}`.  No scientific,
declaration, bibliography, Route, subtype, canonical-source, or result content
changed during finalization.

## Reproducible build

Set `SOURCE_DATE_EPOCH=1788220800`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`, then
run LuaLaTeX -> BibTeX -> LuaLaTeX -> LuaLaTeX.  Every LuaLaTeX pass uses:

```text
lualatex -jobname=paper -interaction=nonstopmode -halt-on-error '\pdfvariable suppressoptionalinfo 512\relax\input{manuscript.tex}'
```

Two builds in completely independent temporary directories produced
byte-identical PDFs.  The final log has zero fatal errors, undefined
citations, undefined references, overfull boxes, and missing-character/glyph
diagnostics; BibTeX records `warning$ -- 0`.

All 17 font programs are embedded and subsetted.  Five text/CJK fonts carry
explicit ToUnicode maps.  The 12 legacy Type-1 Computer Modern math fonts
report `uni=no` in `pdffonts`, exactly as in the accepted content proof; this
is not represented as full per-font ToUnicode coverage.  Unicode text
extraction remains byte-identical to the accepted proof.  All 14 pages were
rendered through a four-sheet `pdfpages` 2x2 contact view and inspected; no
clipping, overlap, blank-page defect, broken equation/table, unreadable CJK,
or reference truncation was observed.

Pandoc 2.9.2.1 remains diagnostic only because its conversion drops the
bibliography command and an artifact path and weakens theorem/cross-reference
structure.  No DOCX or Pandoc-derived manuscript is promoted.

## Scientific and Route boundary

The paper's significant landed result is the positive control consisting of
the exact nonarithmeticity proof, finite completeness certificate, and exact
systole chain.  It does **not** claim the later magnetic/arithmetic transfer.
The work remains in the early control-infrastructure layer of Route A; the
batch positive-arithmetic A2 count remains `0/5`, Route-B invocations remain
`0/5`, and the 19 recorded model instances are not independent statistical
samples.  Governing Route-file hashes are unchanged.

#660 and #672 remain non-clean advisories.  No venue profile is declared, so
venue-limit checks are advisory `not_checked` rather than guessed.  No
submission, venue-readiness certification, public release, external contact,
Git action, corresponding-author designation, or Route advancement has been
performed or authorized.

