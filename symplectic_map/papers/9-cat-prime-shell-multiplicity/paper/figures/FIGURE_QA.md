# Prime-shell figure quality assurance

Status: **ROUND-1 BOUNDED REVISION PASS — READY FOR INDEPENDENT ROUND 2**  
Inspection date: 2026-08-15 UTC  
Scope: publication assets only; no candidate execution, new prime/modulus scan,
numeric evaluation of `s` or `log p`, centralizer computation, or manuscript
drafting.

## Determinism and format checks

- The complete generator was run twice with `PYTHONHASHSEED=0`,
  `SOURCE_DATE_EPOCH=1471132800`, bytecode writes disabled, and an isolated
  Matplotlib configuration directory.
- All nine publication outputs (three figures in PDF, SVG, and PNG) were
  byte-identical between the two runs.
- Every PDF is a one-page vector document with zero raster-image objects,
  zero Type 3 fonts, and all fonts embedded, subset, and Unicode mapped.
- Every SVG parses as XML, contains selectable text, and contains zero raster
  image nodes.
- Every PNG is RGBA at 299.9994 dpi (within the 300 dpi tolerance). Pixel
  dimensions are 2160 x 1335, 2160 x 1425, and 2160 x 1500 for Figures 1--3.
- Mechanical details and per-file hashes are recorded in
  `FIGURE_MANIFEST.json`; the two-run comparison is recorded in
  `DETERMINISM_AUDIT.json`.

## Original-resolution visual inspection

All three final PNGs were inspected at original resolution after the bounded
Round-1 wording revision.  Figure 3 changed only standalone route wording;
Figures 1 and 2 retain their visual content.  All three formats also use
standalone anonymous generator metadata, so every output has a new byte hash.

### Figure 1 — fixed shell profiles and multiplicity

- Panel A: prime labels, period legend, segment values, and the `p=2`/`p=5`
  boundary rows are legible and unclipped.
- Panel B: all five bars and `m_p` annotations are distinct; the dashed
  `single factor` reference is inset from the crowded bar/label region.  The
  displayed scale is linear, matching the revised planning description.
- Panel C: all three boundary/control cards are readable; hatching does not
  obscure text; the scope footer is fully visible.

### Figure 2 — raw-return versus orbit-label products

- Panel A: arrows and both construction pipelines are unambiguous. The
  `retains |gamma|` and `imports m_p` labels are inset from the right boundary
  and do not clip.
- Panel B: both exact `p=5` products, the two cycle counts, and the conclusion
  remain separated and readable.
- Panel C: the complete `m_p/r` grid for `r=1,2,3` is visible; row and column
  labels do not collide with the heatmap or footer.

### Figure 3 — mechanism boundary

- Panel A: all five mechanism cards are distinct. The final `centralizer
  quotient / UNTESTED / follow-up route` card uses an unpatterned background
  and separated lines; no title, status, or route label overlaps.
- Panel B: all equal-weight power sums and the target label are readable.
- Panel C: fractional-exponent and selector-discard columns remain distinct;
  the symbolic composite-control box is unclipped and does not imply a scan.
- The classification footer is fully visible, uses standalone follow-up
  centralizer wording, and retains the exact frozen boundary:
  `A0_FAIL_GLOBAL_NORMALIZATION_ONLY / ROUTE_B_NOT_OPENED`.

## Author-side gate conclusion

The revised package passes deterministic regeneration, font/vector/raster
format checks, and original-resolution visual inspection. This document is
not an independent review authority; the package is frozen for a fresh
independent Round-2 manuscript review.
