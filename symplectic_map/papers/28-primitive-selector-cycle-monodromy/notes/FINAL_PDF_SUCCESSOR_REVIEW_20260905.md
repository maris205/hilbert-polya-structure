# Paper28 successor: independent final visual and delivery-integrity review

Date: 2026-09-05.
Decision: `FINAL_PDF_SUCCESSOR_REVIEW_PASS`.
Handoff: `INDEPENDENT_LOCAL_ACCEPTANCE_READY`.

The exact successor delivery below is ready for the main agent's separate
formal local-acceptance record. This document does not itself overwrite that
record or change any controller/validator decision.

## Exact delivery binding

Root: `build-capsule-successor-20260905`.

- `r0/work/main.pdf` and `r1/work/main.pdf`: each 836,405 bytes, SHA-256
  `ebbd943cba592de21658248779ea3fb4da2cbcbf9a297131df5a358e731b38ca`.
  The reviewer directly read both files, checked their byte counts/hashes,
  and compared their actual bytes for equality.
- `evidence/outcome.json`: 59,824 bytes, SHA-256
  `ff4e9440a4b055a78135996bcd9ebd70ac1b492054af5277b218f9a4531faa5b`.
- Both `work/report/acceptance.json` files: each 21,476 bytes, SHA-256
  `d191787beede459620fdc1b4192246a65e1dbe0d7120673bad6fcec2deeb99f3`.
- Total: 25 physical pages, consisting of 23 main-text pages and two
  reference pages. The actual page images show the main text ending on
  page 23 and References beginning on a fresh page 24.

The original outcome remains
`AUTOMATED_TWO_ROOT_PASS_VISUAL_REVIEW_PENDING`, with
`local_acceptance: NOT_GRANTED_BY_CONTROLLER`. The original validator reports
retain `visual_review: PENDING_INDEPENDENT_REVIEW`. This independent report
supplies the subsequent visual disposition without rewriting those records.

## Actual visual review: all 25 pages

The reviewer individually displayed and inspected each existing image
`r0/work/report/page-001.png` through `page-025.png`, in small batches.
These are the recorded 72-dpi, 612-by-792 renders. No page was substituted by
text extraction or another reviewer's observation. No new rendering or
contact sheet was created. The integrity check below binds every displayed
image hash to the sealed final work manifest and validator page record.
Because the two PDFs are actually byte-identical, this visual disposition
applies to their common PDF bytes; it does not claim a second independent
visual pass over the r1 image files.

| Page | Actual visual disposition |
|---|---|
| 1 | Anonymous title, abstract and opening section are complete, with readable spacing and no clipped text. |
| 2 | Main theorem and its first numbered clauses render normally; the continuation at the page break is readable. |
| 3 | Remaining theorem clauses, dependency prose and positioning section render without missing glyphs or overlap. |
| 4 | Table 1 is complete and within its rules/margins. Its narrow left column has visibly loose word spacing, addressed below. Support definitions and displayed equations fit. |
| 5 | Table 2's notation rows are complete. The shear/Jacobian arrays, inverse formula and their numbers remain separated. |
| 6 | Selected-matrix equations and the formal/actual boundary render clearly and stay within the text block. |
| 7 | The normal-cone formulas, residual identities and beginning of the fan criterion are readable and unobstructed. |
| 8 | New Section 3.2 row count, margin, perturbation estimate and certificate render fully. Equation (3.8) remains above the footer. |
| 9 | Certificate continuation, singleton/wall discussion and the selector/carry box are legible; the box does not obscure its text. |
| 10 | Score constants, score table equations and incidence theorem render normally. |
| 11 | The repeated-label fixture and strict-growth statement/formula are complete, with clear vector notation. |
| 12 | Carry inequalities, transport formula and leading-survival statement are readable; the final statement continues normally. |
| 13 | New Section 5.3 fixed-ring definitions and V/W leading-form products render with visible indices/exponents; equation numbers do not collide with the formulas. |
| 14 | Permuted leading-form indices, noncancellation discussion and cancellation example are intact. Section 6 begins with substantive text. |
| 15 | Scalar forcing and ordered-prefix/monodromy formulas fit, including the long phase-prefix display near the page bottom. |
| 16 | Monodromy proof, digit inequalities and fixture digit vectors are complete and readable. |
| 17 | Table 3 is complete. The three-level decoder and new rotated digit rows render without clipping or overlap. |
| 18 | New prefix rows, all four rows of the period matrix, base expansion, floor-division formula and reversed-product display render clearly. |
| 19 | Missing-data boundary and least-period discussion have normal heading and proof spacing. |
| 20 | Position and phase recurrences have readable subscripts/superscripts and separated equation numbers. |
| 21 | Initial-state boundary, counterexample and planar formula stay within margins and do not touch the footer. |
| 22 | Proof closure and limitations/conclusion paragraphs render normally. |
| 23 | The main text ends visibly after Section 8.3's proof-only evidence statement. Remaining white space is the terminal body page, not missing content or a substituted blank page. |
| 24 | References starts at the top of a fresh page. Entries and long URLs remain readable; entry 15 continues across the page break. |
| 25 | Entry 15's continuation and entries 16–18 are visible and complete. This is a normal final reference page, with no cropped last line. |

No visible clipping, text/formula collision, missing-glyph box, placeholder
reference marker, missing table or unintended blank page was found. The
visual review did not reopen the mathematics or citation-research review.

## Final warning disposition

Both actual final `main.log` files contain the same seven retained underfull
hbox lines at source lines 258–258: badness 10000 four times, and badness
2772, 4353 and 1097 once each. Their exact strings match both sealed
`*-final-log-check.json` records. The source location is Table 1's tabular
block termination, and the affected narrow-column spacing is visible on
page 4. All table rows and citations are readable; no content protrudes,
overlaps or disappears.

Disposition: `ACCEPTED_COSMETIC_NO_SOURCE_CHANGE`. The warning lines are
retained, not suppressed, erased or recast as absent. The raw final-log
search found no overfull, undefined-reference/citation or other warning/error
line matching the checked final-log patterns. The recorded final LaTeX and
BibTeX fatal-line lists are empty. This disposition is limited to these
specific inherited table-spacing warnings, not a general waiver of warnings.

## Independent integrity rechecks actually performed

1. Rechecked all 250 rows of the outcome's sealed-evidence map against the
   actual new evidence tree, using exact membership, type, mode, uid/gid,
   regular-file bytes and SHA-256. The evidence-root membership comparison
   excludes only `outcome.json`, which was created after the prospective
   seal and is bound separately above. No time, inode or directory-size
   comparison was substituted for the recorded predicate.
2. Rechecked all 49 rows of each final work manifest against the actual
   r0/r1 work trees. Both final maps also equal their respective validator
   stage work manifests and equal each other. The recorded cross-root
   differences list is empty; the actual PDFs were separately compared byte
   for byte. All 25 page-image identities agree with the respective report
   page records as well as the final work seals.
3. Checked all 18 stage status records: nine stages per root, every one with
   `spawned: true`, `reaped: true`, `returncode: 0`, and `timeout: false`.
   This verifies the sealed child-outcome records, not a newly rerun process
   history or an independent reconstruction of the OS isolation mechanism.
4. Compared each root's entire stored read-only-input before/after map:
   6,908 rows per map, exactly equal. The stored source entries are read-only
   and match the actual current successor sources. The reviewer did not
   revisit or rehash the approximately 314 MB dependency/resource tree;
   runtime input preservation remains the controller's recorded check.
5. Compared the opening and closing contracts: they are equal after removing
   the opening-only review-hash field. The embedded independent-review bytes
   match that review hash. All five current named note/control bindings
   match the contract and their evidence copies; no code logic was re-reviewed.
6. Rehashed the actual current `paper-successor-20260905` source trio and
   checked byte/LF counts against both contracts and source hashes against
   both validator reports:

   | Source | Bytes | LF | SHA-256 |
   |---|---:|---:|---|
   | `main.tex` | 84,983 | 1,855 | `7beb4f783cd370dc4b0d9d1e9178e3e48ce1ef9ed1497e0e9883b10739d4a1f9` |
   | `math_commands.tex` | 444 | 14 | `16b1e55f52f21b63811a0d34eb64eba955533334f8e5f58005841d6da0a85ce5` |
   | `references.bib` | 6,104 | 204 | `e6a6bdb24a7db3a75b481c8363aa7733cb3dd4c1e8a121d9d9526eb83228882e` |

7. Inspected both sealed acceptance reports: automated status PASS,
   `findings: []`, finding count zero, 25 total/23 content pages and reference
   start page 24. The recorded metadata is anonymous, and the recorded
   `pdffonts` output marks all displayed font entries embedded. These are
   verified bound reports, not a claim that this reviewer reran the PDF
   parser, font tools, security checks or validator.

## Scope and handoff

The `paper-compile` skill was used only for applicable post-build output
checks and explicit warning retention. Its generic compile/repair/template
actions and conference page defaults do not override this project's locked
acceptance requirements or the read-only review request.

No substantive visual or delivery-integrity blocker remains for the exact
hashes above. Only this review document was created. No PDF, source, macro,
bibliography, control, old outcome or warning log was changed; no build,
capture, render or external action was run. The reviewer did not access old
failed roots, capture archives, host dependencies or Paper27.

The main agent may now write the separate formal local-acceptance record for
this successor. This conclusion does not authorize submission, upload or
publication, and does not change the scientific or Route A/B claim boundary.
