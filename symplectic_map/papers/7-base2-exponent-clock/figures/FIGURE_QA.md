# Figure Quality Audit

Audit date: 2026-08-14 UTC  
Verdict: `PASS`

## Visual inspection

The three final 300 dpi previews were inspected at original resolution after
the second layout pass.

- `fig1_boundary_map.png` (2721 x 1005): theorem chain, branch junction, status
  labels, and hatch remain separated; no text or arrow collision was observed.
- `fig2_registered_ledger.png` (2035 x 1714): degree labels were moved inside
  sufficiently tall bars, the development-seen badge no longer intersects the
  period-seven data, and the evidence-boundary footer no longer overlaps the
  horizontal-axis label.
- `fig3_frobenius_filter.png` (3163 x 1895): the flow boxes, coefficient table,
  degree-four necessary-only warning, and four control badges are legible and
  nonoverlapping.  The warning says in words that equality remains open, so a
  negated implication glyph cannot be misread.

No panel contains a decorative title.  Panel letters, box/table headings, axis
labels, and source-derived status labels serve structural or evidentiary roles.
All palettes combine color with borders, hatching, text, or marker shape, so
meaning does not depend on hue alone.

## Mechanical rendering checks

- `pdffonts` reports every font in all three PDFs as embedded, subsetted, and
  Unicode-mapped (`emb=yes`, `sub=yes`, `uni=yes`).
- `pdfimages -list` reports no raster image object in any PDF; plotted geometry
  and text remain vector content.
- All three SVG companions parse successfully as XML and preserve text as text.
- Pillow reports approximately 300 dpi for all PNG previews.
- `DETERMINISM_AUDIT.json` records two regenerations with byte-identical PDF,
  SVG, and PNG outputs for every figure.
- No `__pycache__` directory was created by the no-bytecode generation commands.

## Scientific display boundary

- Figure 1 separates the all-period 2-adic theorem from rational equality,
  complex modulus, and characteristic-exponent statements.
- Figure 2 labels all registered periods as development-seen reproduction and
  states that the all-period equality remains open.
- Figure 3 labels the degree-four polynomial as passing a necessary filter
  only; it is never presented as an equality cycle or a sufficiency witness.

