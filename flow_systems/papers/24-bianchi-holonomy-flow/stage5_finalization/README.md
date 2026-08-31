# Paper 24 Stage-5 finalization workspace

Status: **Stage 5 in progress; awaiting one scholar content confirmation**.

## Preflight package

- `manuscript.tex` is the accepted Stage-4.5 source with only 121 standalone
  ARS block-marker lines removed, SHA-256
  `153e80d360b35c25cac8f0ad2fc1cea14ba43afed07ce7fbb59b9f48c7baeb4e`.
- `references.bib` is the byte-identical accepted bibliography, SHA-256
  `11e7dd42f07ecf22744f5d9c829d13a22212e0d43cb2591c0e9dfd66bde86d87`.
- `content_proof.pdf` is the byte-identical 15-page Stage-4.5 preview, SHA-256
  `7422198864a2c980c2033ab1851e4ef03886a4633cc644bb4fcef7b33576eaea`.
- No `paper.pdf` has been created. The content proof is for author review, not
  a promoted final deliverable.

The citation profile remains
`natbib[numbers,sort&compress] + \bibliographystyle{plainnat}`. An isolated
LuaLaTeX/BibTeX replay has zero final unresolved citations/references and
byte-identical `pdftotext -layout` content relative to the proof. Full facts are
recorded in `../notes/stage5_content_preflight.md` and
`../notes/stage5_preflight_build_receipt.json`.

Pandoc is not an authoritative path here: the installed version cannot run its
citation processor and its raw DOCX trial loses mathematical/theorem/citation
structure. No DOCX was retained or promoted.

Stage 5 is format-only. Scientific content, canonical `paper/` and `results/`
artifacts, the frozen dynamical system, declarations, and Route A/B state remain
unchanged. Final PDF creation must wait for the scholar's explicit content
confirmation.
