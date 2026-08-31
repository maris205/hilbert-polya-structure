# Paper 28 Stage-5 finalization workspace

Status: **Stage 5 in progress; awaiting one scholar content confirmation**.

## Current preflight package

- `manuscript.tex` is the marker-stripped copy of the accepted Stage-4′ draft,
  SHA-256
  `14ad8eeaa7cdd55bc889adc250630a7b18a9e20e316d4fb6becddb9e05922d22`.
  Its only change is removal of 127 standalone `<!--block:B####-->` lines.
- `references.bib` is byte-identical to `paper/references.bib`, SHA-256
  `95728b0a7120e5df341a364ff77f65f5c1d4628d55a6e584e2de7d747d8ca63e`.
- `content_proof.pdf` is the byte-identical Stage-4.5 preview supplied for
  content confirmation, SHA-256
  `253d10080331076a14d658afc423a72b2f687eadcfb68c6e482cec03aabae382`.
  It is 14 A4 pages.
- `paper.pdf` has deliberately **not** been created.  It remains gated on the
  scholar's single in-stage content confirmation.

The citation profile remains
`natbib[numbers,sort&compress] + \bibliographystyle{plainnat}`.  The isolated
preflight replay uses LuaLaTeX → BibTeX → LuaLaTeX → LuaLaTeX and does not
modify these three files.

## Content confirmation

Review `content_proof.pdf` against the accepted article.  The next valid action
is one explicit confirmation that the content is correct.  Only after that
confirmation may the final PDF be compiled and the Stage-5 completion package
be produced.

No scientific/declaration/Route/subtype/canonical-source/result/bibliography
change, submission, public release, external contact, Git action, or venue
readiness claim has been performed or authorized here.
