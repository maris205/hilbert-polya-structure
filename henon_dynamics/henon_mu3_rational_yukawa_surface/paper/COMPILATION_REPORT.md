# HCS-C55 compilation report

Status: **PASS; official final build against RELEASE_CANDIDATE evidence**

## Build

- Engine: pdfLaTeX 1.40.22 through latexmk 4.76.
- Command:
  `latexmk -C && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.
- Exit status: zero.
- PDF: `paper/main.pdf`.
- Total pages: 19 A4 pages.
- Appendix begins on page 15; references begin on page 18.
- File size: 478222 bytes.
- PDF SHA-256:
  `ea75d7e0134531bd02b9ed32ae96aa8cd4416214d3913e19816922af6c30ccae`.
- Final LaTeX log SHA-256:
  `690ea4a3fd8af63384f02cf05eebadab5c2a4b9746bc7da999e54c18c59135a2`.

The final build supersedes the previously bound documentation build.  Its
source changes are release-provenance-only: the persistent scoped-manifest
digest is rebound to the frozen wording-repair successor, and the relationship
between that default identity and the separately verified full-project
successor is stated accurately.  All theorem statements, formulas,
coefficients, and mathematical certificate fields are unchanged.

No conference page limit is asserted; the project uses the inherited
single-column mathematical-article format.

## Paper-source lock

- Source set: the 17 TeX files and `paper/references.bib`.
- Digest definition: SHA-256 of their lexicographically ordered `sha256sum`
  lines, evaluated from the project root.
- Paper-source SHA-256:
  `93495af19048605bd814af264bcf3b2d745a5fdd4f94af31c9422d3bc3782221`.

## Automated checks

- Undefined citations: 0.
- Undefined cross-references: 0.
- LaTeX/package/pdfTeX warnings after the final stabilized pass: 0.
- Duplicate PDF destinations or multiply defined labels: 0.
- Overfull boxes: 0.
- Underfull boxes: 0.
- Rerun requests: 0.
- Stale section files: 0; every file in `paper/sections/` is input by
  `paper/main.tex`.
- Bibliography: 11 entries, all cited; BibTeX warnings: 0.
- Text extraction: PASS, with 1006 lines, 6981 words, and 55350 bytes.
- Extracted-text SHA-256:
  `6eb5fb4b9bb4a23b68cadbce75c9cf16a61637031a3dba7dc3106a4cf5d32b19`.
- Residual TODO/FIXME/XXX/[VERIFY] markers in extracted PDF: 0.
- Literal `??` or `[?]` placeholders in extracted PDF: 0.

## Release-candidate evidence lock

- Artifact status: `RELEASE_CANDIDATE`.
- Payload SHA-256:
  `6afc529d2ab9e849592d9eba7b76324cc7a840670f50c669f90fdd079c0b4323`.
- Schema SHA-256:
  `2961eb6b5b4aefa0e12ffcb59c9e1095b14f0309e2045fd6d8a7f636dc6dca53`.
- Certificate SHA-256:
  `aa6a57bc496d78afd5728640083179bb0dd24963deb44e31459c59edc71c381f`.
- Independent-check SHA-256:
  `e24c90fac1b222ed161eec677c06209c901f0decc335e769dc7df4ce53c68469`.
- Persistent 11-entry code/results-manifest SHA-256:
  `7f1fa8bc6f22dd89b6b9a41ae2353129853f39430ba932f048ff295e56ba30e6`.
- Scoped wording-repair member SHA-256 values:
  `code/run_c55.sh` =
  `8cce25318f34eb36f3347fce8111074845c98277c89489d9e686dc10a64dba35`,
  `code/README.md` =
  `0a261ea79e670ab36fa1839c9d260e8a882c4d38bad3d13b7f197380f2d60be1`,
  and `results/TEST_REPORT.md` =
  `65eeabd3b5a1b3598c795e57e60a83d4adfa40e05130f820335f614798dc8375`.
- Producer SHA-256:
  `3975ad77301939f23754920643b3baa205d67f1451791db3643df693d99c27ba`.
- Checker SHA-256:
  `38d7c144389ba116fc9f6d52bb4327cbe4479f7b7ac71f447c406e69c633834b`.
- Test-suite SHA-256:
  `ccff76d883b2511a2f7491ed28a3f0af2384af2777c402829ef72de6cdf82281`.
- Read-only replay: 13/13 named semantic gates and 15/15 test methods.
- Scalar-leaf inventory: 1589 = 292 central semantic + 1296 independently
  derived + 1 chronology-only; all 292 central leaves pass rebound mutation.
- Status-only promotion control: after removing `artifact_status`, both
  canonical mathematical subpayloads are 30949 bytes and have SHA-256
  `a3da70ceaea6f0ac270cb746a78840ca63367e9b01e02835ad6020e4c76f37ec`.

The persistent scoped manifest is the default identity for this paper build
and release.  The current 47-entry full-project successor is verified
separately under an external-only hash policy; it does not replace the
embedded scoped identity or create a self-hash cycle.  No code or result file
was changed by the documentation and compilation lane.

## PDF checks

- `pdfinfo` parses the file as unencrypted PDF 1.5 with 19 A4 pages, no forms,
  and no JavaScript.
- Title and author metadata are present and correct.
- All 28 fonts are embedded and subsetted.
- No Type 3 font occurs.
- Fresh raster inspection of pages 1, 10, 12, 14, 17, 18, and 19 is clean.
  This covers the title/abstract, top-line descent and Yukawa cubic, the
  realization/comparator firewall, the release-candidate digest block, the
  coefficient table, the exact gradients, and the bibliography.
- The reformatted test-suite digest on page 14 is complete, centered,
  unclipped, and text-extractable as the exact 64-hex value.

## Scope checks visible in the paper

- The four-dimensional object is a rational transverse slice in the smooth
  fixed Hilbert germ, not the full fixed locus and not a displayed literal
  linear family.
- The nonconstant finite etale group scheme and the relative Reynolds
  correspondence are handled without asserting a relative Chow--Kunneth
  decomposition.
- The rank-10 invariant variation becomes CY3-type after exactly one Tate
  twist; no honest Calabi--Yau threefold is constructed or ruled out.
- The Cayley stages distinguish the tangent operator, first through third
  variations, and the top pairing; the semilinear extension uses
  `D(z)=rho*z`.
- The cubic is defined over Q, while no Q-rationality claim is made for its
  smooth geometrically irreducible zero surface.
- Projective Yukawa equivalence is stated only as a necessary local gate; no
  Hodge, Yukawa, or finite-prime match is promoted to a motivic conclusion.
- The Dic3/Z12 branch remains
  `NOT-COMPARABLE-WITH-CURRENT-DATA`; the mirror-side scalar calculation is
  not identified with a restriction of the missing four-variable B-model
  tensor.

This compilation report is frozen with the official final PDF.  Its digest is
recorded externally to avoid a self-hash cycle.
