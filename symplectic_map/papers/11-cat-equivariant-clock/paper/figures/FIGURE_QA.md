# Paper 11 Figure QA

**Local asset-QA verdict:** `PASS`  
**Independent asset-review state at freeze:** pending; manuscript integration
requires a separate `ASSET_PASS` review artifact.

## Inventory and semantic gate

The package contains exactly three figure stems and exactly nine rendered
files: one PDF, one selectable-text SVG, and one 300 dpi PNG for each stem.
No fourth figure, table rendering, candidate output, or analyzer output is
present in the asset directory.

The post-run scope correction was checked against all panels and frozen
captions:

- Figure 1 says point-cardinality retains “support $r_q$; exponent $m_q$;
  unit when $m_q=1$,” shows $q=2$ as the sole locked exception, and states
  only family-uniform nonattainment.
- Figure 2 contains exactly one star at the $q=2$ point-cardinality cell
  $(3,1)^\star$, says “no family-uniform starred column,” and shows
  $r_2=r_4=3$ as the reason the exception is not modulus-specific.
- Figure 3 states the action-kernel/label-recovery boundary and the effective
  $C_6$ counterexample. It makes no scalar-reduction per-row claim.

Searches of the figure scripts, trace, provenance, and LaTeX contract found no
forbidden statement that every row lacks a source-support/unit-exponent pair.

## Mechanical QA

| Stem | PDF page size | PDF fonts | PDF raster objects | SVG text/path/image nodes | PNG pixels | PNG dpi |
|---|---:|---:|---:|---:|---:|---:|
| `fig1_retention_hierarchy` | 518.4 x 378 pt | 5 | 0 | 94 / 78 / 0 | 2160 x 1575 | 299.9994 x 299.9994 |
| `fig2_nine_row_retention` | 518.4 x 421.2 pt | 4 | 0 | 137 / 107 / 0 | 2160 x 1755 | 299.9994 x 299.9994 |
| `fig3_effectivity_counterexamples` | 518.4 x 349.2 pt | 6 | 0 | 35 / 38 / 0 | 2160 x 1455 | 299.9994 x 299.9994 |

For every PDF, `pdfinfo` reports exactly one page; `pdffonts` reports all
fonts embedded, subset, and Unicode-mapped; no Type-3 font occurs; and
`pdfimages -list` reports no raster object. Every SVG parses as XML, contains
selectable text and vector paths, and contains no image node. Every PNG is
RGBA, exceeds 2000 pixels in width and 1000 pixels in height, and passes the
300 dpi metadata tolerance.

## Original-resolution visual inspection

All three final 300 dpi PNGs were inspected at original resolution.

### Figure 1

- The source, retained-data path, and compressed/static path are visually
  separated by geometry, arrow direction, labels, hue, and distinct hatches.
- The six carrier rows and their exact order/twist/isotropy/period entries are
  readable with no clipped cell text.
- The scalar ledger separates name, support/exponent, and scope columns. The
  point-cardinality phrase and the three-line $q=2$ callout fit inside their
  boxes without overlap.
- The bottom family-level conclusion is fully visible and does not claim
  rowwise nonattainment.

### Figure 2

- All 27 bar labels reproduce the exact nine $(n_q,r_q,m_q)$ triples in the
  frozen order; the prime/composite divider is visible.
- Only the exact pairs $q=2,4$ and $q=6,9$ are joined in the collision panel.
- All 36 support--exponent cells are readable. The unique star, red border,
  and crosshatch occur only at $q=2$ point-cardinality.
- The family-uniform and non-modulus-specific footer lines are fully visible
  and separated from the axis labels.

### Figure 3

- The regular, trivial, and effective-$C_6$ cases remain distinct at a glance
  without depending on color alone.
- The regular and trivial action-kernel statements, $BC$ inertia count, and
  $C_6/C_2\sqcup C_6/C_3$ factors are not clipped.
- The general kernel, labelled-stabilizer, and stack formulas have a clear
  left-to-right arrow sequence. The no-period-six control statement is fully
  inside its callout.
- The structural-control footer makes clear that $C_6$ is not a tenth modulus
  row or a candidate.

## Typography, vector, and accessibility checks

- The shared serif/math typography is consistent across all panels.
- PDF text is vector text with embedded TrueType/CID fonts; SVG text remains
  selectable. No bitmap is embedded in either vector format.
- Color is redundant with box position, labels, marker shape, line style, or
  hatch. Prime/composite points use circle/square markers; the unique $q=2$
  exception uses a star, border, and crosshatch.
- Titles are panel descriptors rather than manuscript-style figure titles;
  full captions live in `latex_includes.tex`.

## LaTeX inclusion contract

`latex_includes.tex` contains exactly three `figure*` environments in this
fixed order:

1. `fig1_retention_hierarchy.pdf` / `fig:retention-hierarchy`;
2. `fig2_nine_row_retention.pdf` / `fig:nine-row-retention`;
3. `fig3_effectivity_counterexamples.pdf` /
   `fig:effectivity-counterexamples`.

The captions name direct prior constructions, preserve the $q=2$ exception,
state only the family-uniform conclusion, and identify the $C_6$ object as a
structural control.

## Local conclusion

The exact inventory, semantic scope, original-resolution visual inspection,
vector/font properties, selectable SVG text, and 300 dpi PNG properties pass
the local publication-asset gate. Final manuscript integration remains
blocked until an independent reviewer binds the frozen asset graph and issues
`ASSET_PASS`.
