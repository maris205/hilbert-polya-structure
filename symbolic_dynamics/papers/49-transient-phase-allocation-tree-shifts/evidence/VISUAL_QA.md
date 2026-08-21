# Full-PDF Visual QA

## Artifact inspected

- PDF: `main.pdf` in the final writer overlay
- SHA-256: `aa2a5df28cd7139d9e19aea9bb035cd03f5d787e36260d8a52ed2d33ead930a4`
- Format: 19 A4 pages, 11 pt, single column
- Render: every page rasterized at 110 dpi and assembled into four contact
  sheets covering pages 1--5, 6--10, 11--15, and 16--19.

## Manual page audit

All nineteen repaired-PDF pages were freshly rendered and inspected in
sequence.  The four contact-sheet hashes are identical to the reviewed
pre-reaudit rendering.  Pages 4, 5, 6, and 9, which contain every delimiter
site identified by the independent C0 audit, are also individually
pixel-identical.  The audit found:

- no clipped text, equations, theorem boxes, page numbers, figures, tables,
  or bibliography entries;
- no text--figure collision, overlapping legend, orphaned caption, accidental
  blank page, duplicate page, or broken hyperlink rendering;
- consistent margins, heading hierarchy, theorem typography, equation
  numbering, link color, and footer placement;
- legible Figure 1 labels and arrows, distinct Figure 2 analytic curves and
  legend, and readable Figure 3 panels, legends, and dashed certificates;
- readable Table 1 and Table 2 columns without protrusion into the margins;
- clean Appendix B hash lines and negative-control list; and
- an intentionally sparse final bibliography page, with both remaining
  references fully visible.

The affected-page raster hashes, unchanged from the withdrawn rendering, are:

| Page | SHA-256 |
|---:|---|
| 4 | `bfca6e7bcc0c165a329e18762aaf9e696f88a66d3f94318b9d93aab602a1569f` |
| 5 | `c2f02116e86de6fef0f7a7e71a22e24e12f4cfa723230511aa66dfac0f5843e5` |
| 6 | `31ef2e3905d3f0975e8f9bbd47ff19418f1309f94d255cdc1ce168ab0f33a1f5` |
| 9 | `6de2e93fdd716f9e41938411933d20f89bb5d0ed27c41277ed331bee45425c4b` |

The four contact sheets remain in the historical writer candidate rather than
being duplicated in this minimal overlay.  Their bound SHA-256 values are:

| Pages | SHA-256 |
|---|---|
| 1--5 | `b5f58a219856b032487629abd2638e9d4b20fcedb25622e7d07606ad0ade33cc` |
| 6--10 | `837c4e58f676c97a772fd6bc1fdc232b46ac0db55d4d6abd1a66dd9c1811a545` |
| 11--15 | `d15471c4bb7f9246aa907ba732488230e319eccbdb9b5c3757f77ab20167fecf` |
| 16--19 | `bbacf006eb4aa8ac3031e0331f4cac71b7958c34c556477f8bbdfc1a17321db2` |

## Programmatic complement

`qa/pdf_qa.json` records a separate fail-closed extraction/bounding-box audit:
both raw bbox XML streams parse strictly without sanitization, each contains
7,968 extracted words and zero words outside page bounds, and all six text
extractors contain zero illegal C0, DEL, C1, U+FFFD, or PUA characters.  It
also records 33 embedded fonts, exact equality among five fresh-build copies,
and no run-dependent PDF trailer identifier.  The full build log reports zero
warning lines.

The pre-reaudit PDF hash
`b7a7fab18f3d3bd9bd87eddf02ea2003fb91a96b6ec3731f6e1b32b448f89d5b`
is withdrawn because its raw bbox XHTML failed the strict XML gate; visual
identity does not override that extraction failure.

**Visual verdict:** `VISUAL_QA_CLEAN`.
