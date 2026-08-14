# Figure specification — Paper 28 / SD-C30

All figures are vector TikZ and contain no external or generated raster
assets.

## Figure 1 — common Schatten strip

**File:** figures/schatten_strip.tex

Display horizontal \(\sigma=\Re s\) axes for \(q=2,3,4\). Mark the
two inequalities \(\sigma>1/q\) and \(\sigma<1-1/q\). The \(q=2\)
row collapses to the excluded point \(1/2\); the \(q=3\) row is the
first open strip containing the critical line. Use amber for the
excluded \(\mathcal S_2\) boundary and green for honest strips.

**Claim:** the first integer-order modified determinant that reaches
the critical line is \(\det_3\).

## Figure 2 — native/metric trilemma

**File:** figures/metric_trilemma.tex

Left branch: source incidence \(\to\) native reflected block \(\to\)
mixed Gram \(\to\) exact fourth-order \(t\)-motion \(\to\) generic
controls.

Right branch: source incidence \(\to\) positive common metric \(\to\)
\(Z^*GZ\) atom diagonal \(\to\) independent \(2\times2\) blocks
\(\to\) no \(t\)-motion.

The bottom stop box states that neither branch supplies a fixed
Hilbert–Pólya operator.

## Figure 3 — adversarial control matrix

**File:** figures/control_matrix.tex

Rows: standard divisibility, mutated divisibility, composite-only
subposet, seeded generic DAG. Columns: nonzero mixed Gram, native
\(B^2\) phase, native \(B^4\) phase, orthogonalized phase. The first
three columns pass for every row; the last column is absent for every
row. This visualizes genericity rather than ranking numerical effect
sizes.

## Accessibility

- Every color distinction is paired with text or shape.
- Captions state the inference, not merely the objects.
- No font below the surrounding manuscript's small-caption size.
- Route rejection uses both red color and an explicit STOP label.
