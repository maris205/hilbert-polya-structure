# Paper 25 Stage-5 finalization workspace

Status: **Stage 5 in progress; awaiting one scholar content confirmation**.

## Preflight package

- `manuscript.tex` is the accepted Stage-4.5 source with 116 standalone block
  lines and eight inline `ref`/`anchor` provenance comments mechanically
  removed, SHA-256
  `9c7782ebf6a90f0e33ab86f2e77d7ce78ecfb2ad0ddb9413e4829cfe33f776e1`.
- `references.bib` is the byte-identical accepted corrected derived
  bibliography, SHA-256
  `a0bf0cd2f022f1b5dcc0bffdd1b28d135cef7c287f77c2a46e514480e2b3b5ab`.
  Canonical `paper/references.bib` remains unchanged.
- `content_proof.pdf` is the byte-identical 13-page Stage-4.5 preview, SHA-256
  `34c5351403f81c22a16b8de0fa4e9011b0b3b5a5b7be6c321a25d47e4724fe65`.
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
