# Response to Independent Manuscript Review — Round 1

Response date: 2026-08-15 UTC  
Candidate: `cat_prime_shell_multiplicity_obstruction_v1`  
Round-1 review: `MINOR REVISION`, four bounded findings  
Revision status: **4/4 IMPLEMENTED; AUTHOR VERIFIED; AWAITING INDEPENDENT ROUND 2**

This response is limited to M1--M4 in the independent review at SHA-256
`dc34ea65a091680e3a2e0f89b15f804f45b3a7be7ae11502d82c668ec6d58ed8`.
No source lock, proof package, candidate code, registered result, official
result report, or result manifest changed.  The candidate and tests were not
rerun, and no prime, numerical analytic, composite-shell, or centralizer
calculation was added.

## M1 — final claim map and locators

Appendix B now has exactly nine one-to-one rows, C1--C9, matching the final
`CLAIM_MANIFEST.json`; the obsolete X1/X2 identifiers are absent.  The
manifest locators were checked against the revised source: C1 at line 172,
C2 at 348, C3 at 412, C4 at 454, C5 at 474, C6 at 517, C7 at 552, C8 at
627, and C9 at 604.  Each row preserves its proof/evidence role and scope
boundary.

## M2 — qualitative novelty wording

The manuscript no longer states a numerical novelty score.  It instead
describes the contribution as a low-novelty synthesis and audit and retains
the direct prior-art collisions.  The numerical calibration remains only in
internal planning notes; it is not part of the reader-facing manuscript or
current public configuration.

## M3 — standalone manuscript and figure wording

Reader-facing project-internal `Paper 9`/`Paper 10` wording was replaced by
`the present audit` and `follow-up centralizer route`.  Figure 3's generator,
caption include, card, and footer were updated.  Publication metadata was
made anonymous and standalone, so all nine output byte hashes changed: the
Figure 1 and Figure 2 changes are metadata-only and visually unchanged;
Figure 3 also contains the bounded wording repair.  Two complete renders
matched for all nine PDF/SVG/PNG outputs.  The current figure manifest is
`23468908fb020e80677e7a5b8e8686c2d14edbec2dc1e74f06973940c12adb8e`,
the determinism audit is
`a6aab23da51635f07e68104507a5ab55f49d64abdf33f70205e5317478b71129`,
and the revision 24-path framed tree is
`0526235c1b3581aba830e054d1f883fd677cb7a752180bb8a0eeb0dbab7a862e`.
The historical independently reviewed predecessor remains explicitly bound
as `312c4b095b58acb9e8047d7113308d28870e3db7633f37d17bd904ca2c7ebfaa`.

## M4 — Figure 1 axis description

`PAPER_PLAN.md` now says that Figure 1 uses a compact linear axis, matching
the frozen data and actual plot.  No data value or axis implementation was
changed.

## Build, visual, citation, and originality checks

- Two clean deterministic builds produced byte-identical 15-page PDFs at
  `96a560712ae7fb34e1d0ecfcd59e9b2c210ad61fe8ee0537c3a5ff5c860b4cd6`.
- The terminal build has zero LaTeX/package/box warning, zero undefined
  reference or citation, and exact citation closure 11/11.
- All 37 PDF fonts are embedded and subset; the PDF has zero raster image
  objects.  All 15 rendered pages and all three original-resolution figures
  were inspected with no overlap, clipping, or corrupt glyph.
- The project-local normalized body has 3,789 tokens and 3,755 unique
  contiguous 12-word shingles; comparison with Papers 1--8 and
  `propose-symplectic-map.md` found zero common shingle in every case.
- The immutable pre-review PDF remains byte-unchanged at
  `9b63f190e7c751c27682d1a9cc9246f0153edddfec61d4539c573ab70070d51c`.

## Bound revision snapshot

| Object | SHA-256 |
|---|---|
| revised `paper/manuscript.tex` | `fb54cb9273c89ad5f76a9485d67a815555050b3c71e630e47d367b043ae6e26c` |
| `paper/paper_round1_revision.pdf` | `96a560712ae7fb34e1d0ecfcd59e9b2c210ad61fe8ee0537c3a5ff5c860b4cd6` |
| revised `PAPER_PLAN.md` | `41a1e6e9356c3820c3890fca232b60302673c1a28a83d8ba26f932eec5f73e3e` |
| `paper/figures/FIGURE_MANIFEST.json` | `23468908fb020e80677e7a5b8e8686c2d14edbec2dc1e74f06973940c12adb8e` |
| `paper/PAPER_CONFIGURATION.md` | `fde14dcf6020fb183a6d69b0790bccc482dec6dc55961f8f0fd7f8650bd75932` |
| `paper/CLAIM_MANIFEST.json` | `8dd511a2775460bcd9d33a925df60c780fd946f46ca015c3bf6f41b6fa80ccc8` |
| `paper/EXPERIMENT_PASSPORT.json` | `847c3655ff9ff2e27f1d0755a8f5913ad81d4b8c07c4a48849bf3ac2acfcbac0` |
| `paper/FIGURE_PACKAGE.json` | `477e63151c7b203d3199b5e98122f1b2df315910ec05f1c262cadb3044a4032c` |
| `paper/PLAGIARISM_MANIFEST.json` | `479415a2c9bd1985ee14925ba31c193cae479f38ca6a3676b5154a8230497316` |
| `paper/PIPELINE_STATE.json` | `32253ea26d7fb485b4e61f2e2df0c2f661a811319716b77ca4ae963f85087d5a` |

Disposition: `ROUND1_BOUNDED_REVISION_COMPLETE_READY_FOR_INDEPENDENT_ROUND2`.

This is author-side evidence, not an independent Round-2 verdict.  It does
not authorize finalization or creation of `paper_final.pdf`.
