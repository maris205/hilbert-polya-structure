# Paper30 V4 two-root production and root whole-PDF read

Date: 2026-09-09. Status: `BUILD_PAGE_DETERMINISM_ROOT_PDF_PASS_PENDING_INDEPENDENT_ACCEPTANCE`.

## Actual result

The complete V4 source was frozen in the
[pre-execution protocol](V4_COMPLETE_PRODUCTION_PROTOCOL_V1_20260909.md)
before either new root was created. r4 and r5 each started absent and received
only the complete eleven-file source. Each executed exactly the four prescribed
processes: pdfLaTeX 1, BibTeX, pdfLaTeX 2, pdfLaTeX 3. **All eight process exit
statuses were 0**. No extra convergence pass, trial source or root rerun occurred.
All original and copied eleven-source checksum checks passed before and after
production. Old r0/r2 and V1/V2/V3 were neither edited nor cleaned.

Both final PDFs have 546617 bytes and SHA-256
`40f05a156cbedc16a881b090a19af299c12c41a1fd9fb62a0290406a83737007`.
A direct `cmp` also returned 0: this is byte equality, not rendered similarity.
The accepted-output candidate is [r4/work/main.pdf](../build/natural-20260909-r4/work/main.pdf);
[r5/work/main.pdf](../build/natural-20260909-r5/work/main.pdf) is its independent-root twin.
Neither is yet declared finally accepted by this record.

## Actual page, log, source and font checks

- pdfinfo: 41 pages, 612 × 792 pt letter, PDF 1.5, empty author metadata,
  no encryption, JavaScript or forms. Visible title page says Anonymous.
- Both main.aux files place LastBodyPage at 39 and the absolute final page at 41.
- Actual r4 pdftotext output has 41 nonempty physical pages: the full final
  proof and limitations end on page 39, References start on 40 and end on 41.
- The root personally viewed every printed footer 1–41 in the rendered PDF.
  Thus the actual count is **39 substantive body + 2 reference pages**.
  It passes the user-approved [22–40 window](PUBLICATION_PAGE_ADDENDUM_V2_20260909.md).
  It does not retroactively pass the unchanged old 22–30 contract.
- Both converged LaTeX/BibTeX logs have no warning, overfull/underfull box,
  missing character/font, undefined reference/citation or rerun requirement.
  A diagnostic rg returning 1 means no matching warning, not a failed compiler.
- BibTeX processed 17 entries without warnings. The root read the entire r4
  main.blg and visually read both reference pages. All 23 font-resource rows
  returned by pdffonts are Type 1, embedded and subset, with Unicode mappings.
- Static final-source scan: 135 labels, 0 duplicates,
  0 missing cross-reference targets, 17 actual cited keys and 17 bibliography keys,
  0 missing and 0 uncited keys. No TODO/TBD/VERIFY/placeholder marker.
  Actual extracted PDF text has no unresolved ?? or [?] marker.

## Root's complete actual visual read

The root rendered this exact r4 PDF with `pdftoppm -r 110 -png` into
`build/natural-20260909-r4/inspection/page-01.png` through `page-41.png`,
then personally opened **each of all 41 page images**, in order, including the
reference pages. This is a full actual PDF read, not the old seven-page diagnostic
sample, nor an inference from page metadata or source-only reading.

| Actual pages read | Content and checks |
|---|---|
| 1–4 | Anonymous title/abstract; full V1–V3 hypotheses, theorem formulas, state-order table, characteristic-two and literature limits. |
| 5–10 | Eight centers, four terminal charts, boundary transport table, constants/node frames, complete primitive pencil and characteristic-independent smoothness proof. |
| 11–15 | Finite critical algebra, complete spectral charts, actual module/state inverse, Picard difference, no-kernel and original-field torsor descent. |
| 16–19 | Complete smooth closed fibers, henselian section citation, minimal-model comparison, Cartier/Hasse convention and both state directions. |
| 19–22 | Integral insertion, residue multiplier, original-model regularity and nonreduced terminal-chart restriction. |
| 22–26 | Bockstein, prime trace, integer Taylor quotient, actual image-sheaf class and full first-layer ideal. |
| 26–32 | Odd-prime complete block deformation, weighted commutator, support/unique selection, gluing and exact truncated ideal. |
| 32–39 | Characteristic-two base/higher blocks, actual characteristic-four tangent comparison, both local divisibility steps, mixed ideals, transverse length/base action and exact-versus-bound state orders. |
| 40–41 | All 17 references, accents, mathematical title notation, DOI/URL line breaks and final footer. |

All formulas, tables, indices, fractions, margins and page transitions are readable;
no clipping, collision, missing glyph, blank inserted body page or proof appendix
was observed. The V4 matrix display on p14 and cohomology display on p22 fit
normally; the latter's sentence continues on p23 without losing its hypotheses.
The retained V3 insertion display on p20 and corrected cases intervals on p30
remain correct. Natural proof/page continuations and the short final reference
page do not amount to padding. Every necessary proof remains in the body.

The previously accepted complete-source static review and narrow successor
checks remain the mathematical-transcription evidence. This visual read does
not reopen their unchanged inputs or claim a new independent mathematical proof.
The Vlasenko correction-content gap remains explicitly unknown in the citation
record; that source is related work, not a proof black box.

## Remaining independent steps

The bounded V4 layout/contract check, fresh non-author complete actual manuscript/
PDF review and subsequent independent final integrity check must be dispositioned
before local acceptance. The layout checker coauthored unchanged §§7–8; its
limited check of root-authored §§3/6 is not the fresh complete-review seat.
Batch07 remains 3/5 in this record; Paper31 has not been selected or opened.

## Exact current artifact identities

Paths are project-relative. No claim is made that a main.fls is an inventory
of all historical workspace artifacts; it records actual TeX inputs for its root.

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| `notes/SOURCE_V4_20260909.sha256` | 993 | `f57b18fdd0549183ec4250350158ffa721a82a351c15f3b4b792de51043655a9` |
| `notes/V4_COMPLETE_PRODUCTION_PROTOCOL_V1_20260909.md` | 5676 | `8be634dc8011462a04a247f9ef8d8d76d5a42ebfbcaece35883b010555cb069b` |
| `notes/PUBLICATION_PAGE_ADDENDUM_V2_20260909.md` | 3167 | `9cc96e76d8bd22dc7b76a4bb35791279c06fd1b83e24c3a74fe136f895a76380` |
| `build/natural-20260909-r4/work/main.pdf` | 546617 | `40f05a156cbedc16a881b090a19af299c12c41a1fd9fb62a0290406a83737007` |
| `build/natural-20260909-r4/work/main.log` | 23386 | `fe3c5b8695dfd86abf8e61121a328f023fa1267741b4fa96b9dd4a9d2404c9a3` |
| `build/natural-20260909-r4/work/main.aux` | 19856 | `e4f7f8ef7bb67eb727d1ee4beb3c61f514c2cbfef99edfc419e7cec48be93098` |
| `build/natural-20260909-r4/work/main.bbl` | 6040 | `41d28bd7f9d20856e5e70d22879183dd8c6458d0e5f490e053f7a61bed79f819` |
| `build/natural-20260909-r4/work/main.blg` | 914 | `1199addeddc0e44a5028f0cca03ef758bd702c07331ba70f7b4c78a74d1136f4` |
| `build/natural-20260909-r4/work/main.fls` | 51361 | `4183d9e434b90fa2c5c7027f0e784f8617aaf33b2798f11f17a298c9065b8c6f` |
| `build/natural-20260909-r4/pdflatex-1.stdout.log` | 25050 | `0e18153a70378fe391f837889d9cd889599e262532d6926b96c2fc78bbd10eff` |
| `build/natural-20260909-r4/bibtex.stdout.log` | 158 | `7b0a0a8d2f1749b44546479273ee9d474d9656cc2a276630ff83cc8a72044dc9` |
| `build/natural-20260909-r4/pdflatex-2.stdout.log` | 9973 | `96bea78c3e5f87721c30d8ba1ed9242def95740d71ed14cef023ebd9349f721c` |
| `build/natural-20260909-r4/pdflatex-3.stdout.log` | 6670 | `e36c4b130c7ad9dd5141b37b0cfabe381185ca6bd09940d2f2969c0a00f5629c` |
| `build/natural-20260909-r5/work/main.pdf` | 546617 | `40f05a156cbedc16a881b090a19af299c12c41a1fd9fb62a0290406a83737007` |
| `build/natural-20260909-r5/work/main.log` | 23386 | `fe3c5b8695dfd86abf8e61121a328f023fa1267741b4fa96b9dd4a9d2404c9a3` |
| `build/natural-20260909-r5/work/main.aux` | 19856 | `e4f7f8ef7bb67eb727d1ee4beb3c61f514c2cbfef99edfc419e7cec48be93098` |
| `build/natural-20260909-r5/work/main.bbl` | 6040 | `41d28bd7f9d20856e5e70d22879183dd8c6458d0e5f490e053f7a61bed79f819` |
| `build/natural-20260909-r5/work/main.blg` | 914 | `1199addeddc0e44a5028f0cca03ef758bd702c07331ba70f7b4c78a74d1136f4` |
| `build/natural-20260909-r5/work/main.fls` | 51361 | `1db73515548572024ad23d18c9f9cbc0248986969bbb38d8925bd37ff2ecc836` |
| `build/natural-20260909-r5/pdflatex-1.stdout.log` | 25050 | `0e18153a70378fe391f837889d9cd889599e262532d6926b96c2fc78bbd10eff` |
| `build/natural-20260909-r5/bibtex.stdout.log` | 158 | `7b0a0a8d2f1749b44546479273ee9d474d9656cc2a276630ff83cc8a72044dc9` |
| `build/natural-20260909-r5/pdflatex-2.stdout.log` | 9973 | `96bea78c3e5f87721c30d8ba1ed9242def95740d71ed14cef023ebd9349f721c` |
| `build/natural-20260909-r5/pdflatex-3.stdout.log` | 6670 | `e36c4b130c7ad9dd5141b37b0cfabe381185ca6bd09940d2f2969c0a00f5629c` |
