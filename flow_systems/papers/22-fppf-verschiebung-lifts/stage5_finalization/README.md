# Paper 22 Stage-5 finalization workspace

Status: **Stage 5 final paper complete; awaiting the scholar's FULL-checkpoint
decision about optional Stage 6**.

## Authoritative deliverables

- `manuscript.tex` is the author-confirmed, byte-locked LaTeX source, SHA-256
  `e90dd88109d4e53d1f789808286c15cc917003cd38b69f49ddaff8661b9158ed`.
- `references.bib` is the verified three-entry bibliography, SHA-256
  `bd03813691db911316b18620ee4a1d212ac284fce7fb79af9f1b1cbc7ea71093`.
- `paper.pdf` is the reproducible 13-page A4 final paper, SHA-256
  `e030259bb34c6d92af8fd53af80dce0e43200133c9bbdc91efb4f54e8f6c761a`.
- `content_proof.pdf` is the accepted 13-page Stage-4.5 PDF supplied for the
  scholar's content confirmation, retained as provenance rather than as a
  second final version.
- `provenance_summary.md` records the Stage-4.5 lock, content-equivalence
  result, #660/#672 advisory boundaries, Route boundary, and every
  package-verifier non-passing row.
- `submission_verification_report.json` is the machine-readable ARS package
  report. Its freshness must be rechecked before reuse.

The citation profile remains
`natbib[numbers,sort&compress] + \bibliographystyle{plainnat}`.  No manuscript
content was changed during finalization.

## Reproducible build

Set `SOURCE_DATE_EPOCH=1787702400`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`, then
run LuaLaTeX -> BibTeX -> LuaLaTeX -> LuaLaTeX. Each LuaLaTeX invocation uses
the following input wrapper without modifying `manuscript.tex`:

```text
\pdfvariable suppressoptionalinfo 512\relax\input{manuscript.tex}
```

Bit 512 suppresses LuaTeX's random PDF trailer ID. Two builds in independent
temporary directories produced the same final SHA-256. The final PDF and the
content-proof PDF also produced the same `pdftotext -layout` SHA-256,
`5bdca519563858a0c084c2315f5f28d0132f0ad9b1459c07294953bfdab64c67`.

The final build has zero unresolved citations or references, zero overfull
boxes, zero output missing-character diagnostics, and zero fatal errors. Two
underfull Chinese-abstract lines and package-level `lualatex-math`,
`unicode-math`, and `microtype` messages are retained as nonblocking log
information.

DOCX is not part of the configured authoritative output.  The available
Pandoc 2.9.2.1 conversion loses theorem-environment labels, citation rendering,
and parts of the mathematical source, so a lossy DOCX will not be represented
as content-equivalent. No submission, public release, external contact, Git
action, corresponding-author designation, venue-readiness claim, or Route A/B
advancement has been performed or authorized.
