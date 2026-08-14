# HCS-C56 compilation report

Status: **PASS; official final build against exact
`PREFREEZE_CODE_RESULTS_PASS` machine evidence**

## Build

- Engine: pdfLaTeX 1.40.22 through latexmk 4.76.
- Command:
  `latexmk -C`, followed by
  `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.
- Exit status: zero.
- PDF: `paper/main.pdf`.
- Total pages: 19 A4 pages.
- Appendix A begins on page 13; references begin on page 19.
- File size: 449889 bytes.
- PDF SHA-256:
  `ae8f422e3183455206f3459f0952d7e5175633bc534c318bfb7326b08c6c604e`.
- Final LaTeX log SHA-256:
  `afd4dc0323cc3139d6a1e8c441210d453c4c51ab4c5b14aa68d2197a7033af60`.

No conference page limit is asserted.  The project uses a single-column
mathematical-article format.

## Build history and authority

The final build supersedes two non-authoritative predecessors:

1. a fresh isolated source-audit build, performed outside the live tree;
2. the controlled live bootstrap build whose three diagnostic digests are
   printed in section 7 of the paper and explicitly labelled chronology-only.

The bootstrap build was used only to replace the precompile/null prose with a
truthful compiled-evidence statement.  The final PDF, log, text, source, and
report identifiers in this report and the Route record are the documentation
authority.  No source edit or compilation follows this final build.

## Paper-source lock

- Source set: 15 TeX files and `paper/references.bib` (16 files total).
- Digest definition: SHA-256 of their lexicographically ordered `sha256sum`
  lines, evaluated from the project root.
- Paper-source SHA-256:
  `b284a2f17a53b979374a5525a0642472bd7a14cb72f8260de87bea9a15628a29`.

## Automated checks

- Undefined citations: 0.
- Undefined cross-references: 0.
- LaTeX/package/pdfTeX warnings after the final stabilized pass: 0.
- BibTeX warnings: 0.
- Duplicate PDF destinations or multiply defined labels: 0.
- Overfull boxes: 0.
- Underfull boxes: 0.
- Rerun requests: 0.
- Stale section files: 0; every one of the 13 files in `paper/sections/` is
  input by `paper/main.tex`.
- Bibliography: 6 entries, all cited.
- Text extraction: PASS, with 1356 lines, 6838 words, and 44922 bytes.
- Extracted-text SHA-256:
  `7c1722fa8286b4dcbb03a3acbe1fcec09a3a26890638599168e8844c9c3ae718`.
- Residual TODO/FIXME/XXX/[VERIFY] markers in extracted PDF: 0.
- Literal `??` or `[?]` placeholders in extracted PDF: 0.
- Ghostscript null-device parse: PASS.

## Exact code/results evidence lock

- Machine state: `PREFREEZE_CODE_RESULTS_PASS`; this exact byte state is
  intentionally not rewritten to `RELEASE_CANDIDATE` by the documentation
  lane.
- Payload SHA-256:
  `5b17c9ed7bea60680556af70297199b653d51188bb30ce59f7c2c6bfbc94f661`.
- Canonical schema SHA-256:
  `ef26d7204a38e28aaf00eed8188b31d34d590c9c8a19924f1d0798e40b052d5f`.
- Schema-file SHA-256:
  `adab34998a944c8a4af8db774e511f0453839ea6a6e14e9437ffc259be3da504`.
- Certificate SHA-256:
  `26739ce5aedb4a3467645f9c1b2036d4d3eec9ce4d0dbce23d67ea7b67e5fbc4`.
- Independent-check SHA-256:
  `4ccfb09139a4bfa812ea9c57ff8b65a6a8e603dbdb00e245355a4563386489a9`.
- Scoped 12-entry code/results-manifest SHA-256:
  `20d29af97128e766bb5e59bf6f82f8401c6ed62f279371b031febcefd5d99b4a`.
- Read-only replay: 10/10 semantic gates and 15/15 test methods.
- Scalar-leaf inventory and rebound sweep:
  2684 = 2662 payload + 20 schema + 2 envelope; 2684/2684 pass.
- Direct producer/checker/test digests are bound by the scoped manifest and
  are not separately promoted in the root Route record.
- Implementation/provenance commits: unset at this no-commit
  release-candidate milestone.
- Full-project successor: root `FULL_PROJECT_HASHES.sha256`, 46 entries and
  self-excluding; verified separately, with its digest external-only.

The scoped manifest remains the default exact code/results identity and runner
scope.  The full-project successor is a separate release-wide integrity ledger
and does not replace it.  No code or result file was changed by the
documentation and compilation lane.

## PDF checks

- `pdfinfo` parses the file as unencrypted PDF 1.5 with 19 A4 pages, no forms,
  and no JavaScript.
- Title and author metadata are present and correct.
- All 26 fonts are embedded and subsetted Type 1 fonts.
- No Type 3 font occurs.
- Fresh raster inspection of all 19 pages is clean.  It covers the
  title/abstract, theorem and scope firewalls, cubic and line-section formulas,
  chart/clopen proof, modular irreducibility, Galois/parity ledger,
  Hochschild--Serre rank bridge, exact tuple/bootstrap block, declarations,
  source ledger, eliminant table, modular factors, Picard lattice, and
  bibliography.
- The long hashes on page 11 and the 28 eliminant coefficients on page 16 are
  complete, unclipped, and text-extractable.

## Scope checks visible in the paper

- The global degree 27 comes from Kass--Wickelgren Theorem 2/classical line
  count; Corollary 53 supplies simple zeros, not the count.
- The chart immersion is promoted globally only through the finite-etale
  open-and-closed bridge and equal-rank argument.
- `E` is the non-Galois degree-27 residue field; `K` is its distinct normal
  closure and common normal line field.
- Coxeter/reflection determinant, not ordinary permutation sign in `S27`,
  excludes the index-two subgroup; every `W(E6)` line permutation is even.
- The machine certifies fixed-space rank one in the geometric Picard lattice.
  The written Hochschild--Serre torsion/rank bridge, together with
  `Pic^0(Y_bar)=0`, gives arithmetic Picard rank one without integral Picard
  surjectivity.
- The no-line statement concerns finite extensions defining a line.  It does
  not imply absence of rational points, nonrationality, a Hasse failure, or a
  Brauer--Manin obstruction.
- No motive, VHS, Calabi--Yau, automorphy, generic-family, dynamical, RH, or
  exhaustive novelty claim is made.

This report is frozen with the official final PDF.  Its own digest and the
Route-record digest are recorded externally to avoid self-hash cycles.
